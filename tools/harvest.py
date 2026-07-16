#!/usr/bin/env python3
"""
oss-atlas project harvester — batch discovery and intake automation.

One trigger = one wave. Collect → dedupe → filter → classify → report.

Usage:
  python3 tools/harvest.py search --query "language:python stars:>1000" --per-page 20 --output wave.json
  python3 tools/harvest.py dedupe --input wave.json --index-root categories/ --output wave-new.json
  python3 tools/harvest.py filter --input wave-new.json --min-stars 100 --output wave-filt.json
  python3 tools/harvest.py classify --input wave-filt.json --category-index categories/ --output wave-cls.json
  python3 tools/harvest.py report --input wave-cls.json --output wave-report.md
  python3 tools/harvest.py wave --directions 5 --per-page 5 --output wave-report.md
  python3 tools/harvest.py wave --query '"LLM inference" in:name,description' --per-page 15

Requires: Python 3.9+ (stdlib only). GitHub auth via GITHUB_TOKEN or GH_TOKEN.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


def _github_headers() -> dict:
    """Return Authorization header if GITHUB_TOKEN is set, else empty."""
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        return {"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"}
    return {"Accept": "application/vnd.github+json"}


def _api_get(url: str) -> dict:
    """GET GitHub API (or generic URL), return parsed JSON."""
    req = urllib.request.Request(url, headers=_github_headers())
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def search_repos(query: str, per_page: int = 20) -> list[dict]:
    """Call GitHub Search API (REST) and return simplified repo stubs."""
    q = urllib.parse.quote(query, safe="")
    url = f"https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page={per_page}"
    data = _api_get(url)
    items = data.get("items", [])
    results = []
    for it in items:
        lic = it.get("license") or {}
        results.append({
            "repo": it["full_name"],
            "html_url": it["html_url"],
            "stars": it.get("stargazers_count", 0),
            "forks": it.get("forks_count", 0),
            "language": it.get("language") or "",
            "license": lic.get("spdx_id") or lic.get("key") or "",
            "description": (it.get("description") or "").strip(),
            "pushed_at": it.get("pushed_at", ""),
            "created_at": it.get("created_at", ""),
            "topics": it.get("topics", []),
            "archived": it.get("archived", False),
            "fork": it.get("fork", False),
        })
    return results


QUERY_QUALIFIERS = {
    "archived",
    "created",
    "fork",
    "forks",
    "in",
    "is",
    "language",
    "license",
    "name",
    "description",
    "readme",
    "mirror",
    "org",
    "pushed",
    "size",
    "sort",
    "stars",
    "topic",
    "user",
}

CATEGORY_ROW_RE = re.compile(
    r"^\|\s*\*\*([^*]+)\*\*\s*\|\s*(.*?)\s*\|\s*\[→\]\(([^)]+)\)\s*\|$"
)


def load_discovery_directions(index_path: Path) -> list[dict]:
    """Read top-level category directions from the root route table."""
    directions = []
    for line in index_path.read_text(encoding="utf-8").splitlines():
        match = CATEGORY_ROW_RE.match(line)
        if not match:
            continue
        category, description, route = match.groups()
        directions.append(
            {
                "category": category.strip(),
                "description": description.strip(),
                "route": route.strip(),
            }
        )
    if not directions:
        raise ValueError(f"no discovery directions found in {index_path}")
    return directions


def load_discovery_recipes(index_path: Path, recipes_path: Path) -> list[dict]:
    """Load curated search recipes whose categories exist in the root route."""
    route_directions = {
        item["category"]: item for item in load_discovery_directions(index_path)
    }
    raw = json.loads(recipes_path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"discovery recipes must be a JSON list: {recipes_path}")
    recipes = []
    seen_categories = set()
    for recipe in raw:
        if not isinstance(recipe, dict):
            raise ValueError("each discovery recipe must be an object")
        category = str(recipe.get("category") or "").strip()
        query = str(recipe.get("query") or "").strip()
        if category not in route_directions:
            raise ValueError(
                f"discovery recipe category is not in root INDEX.md: {category}"
            )
        if category in seen_categories:
            raise ValueError(f"duplicate discovery recipe category: {category}")
        validate_discovery_query(query)
        combined = dict(route_directions[category])
        combined["query"] = query
        recipes.append(combined)
        seen_categories.add(category)
    if not recipes:
        raise ValueError(f"no discovery recipes found in {recipes_path}")
    return recipes


def select_discovery_directions(
    index_path: Path,
    recipes_path: Path,
    count: int = 5,
    seed: int | None = None,
) -> list[dict]:
    """Randomly select curated category recipes with a reproducible seed."""
    directions = load_discovery_recipes(index_path, recipes_path)
    if count < 1:
        raise ValueError("direction count must be at least 1")
    if count > len(directions):
        raise ValueError(
            f"direction count {count} exceeds available categories {len(directions)}"
        )
    return random.Random(seed).sample(directions, count)


def build_direction_query(direction: dict, pushed_after: str) -> str:
    """Build a domain-specific repository search query for one category."""
    base_query = direction["query"].strip()
    if re.search(r"\bpushed:", base_query, re.IGNORECASE):
        return base_query
    return f"{base_query} pushed:>{pushed_after}"


def validate_discovery_query(query: str) -> None:
    """Reject generic language/popularity searches without a domain signal."""
    quoted = re.findall(r'"([^"\n]+)"', query)
    if any(len(term.split()) >= 2 for term in quoted):
        return
    terms = re.findall(r"\b[a-zA-Z][a-zA-Z0-9_-]*\b", re.sub(r'"[^"\n]+"', "", query))
    free_terms = [
        term
        for term in terms
        if term.lower() not in QUERY_QUALIFIERS
        and not re.fullmatch(
            r"(?:python|javascript|typescript|rust|go|java|c|cpp)",
            term,
            re.IGNORECASE,
        )
        and not re.fullmatch(r"\d{4}-\d{2}-\d{2}|\d+", term)
    ]
    topic_values = re.findall(r"\btopic:([^\s]+)", query, re.IGNORECASE)
    if free_terms or topic_values:
        return
    raise ValueError(
        "discovery query needs a domain or task signal; language/high-star-only searches are not allowed"
    )


def _read_repo_from_frontmatter(path: Path) -> str | None:
    """Parse a .md file, extract repo: from YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm = text[3:end].strip()
    # naive line-by-line parsing of repo: key
    for line in fm.splitlines():
        if line.strip().startswith("repo:"):
            return line.split("repo:", 1)[1].strip()
    return None


def _repo_key(value: str | None) -> str | None:
    """Normalize GitHub repo references to owner/repo for dedupe."""
    if not value:
        return None
    value = value.strip().strip('"\'')
    if not value:
        return None
    match = re.search(r"github\.com[:/]([^/]+)/([^/#?]+)", value, re.IGNORECASE)
    if match:
        owner, repo = match.group(1), match.group(2)
    else:
        parts = value.split("/")
        if len(parts) < 2:
            return None
        owner, repo = parts[0], parts[1]
    repo = repo.removesuffix(".git")
    return f"{owner.lower()}/{repo.lower()}"


def dedupe_candidates(candidates: list[dict], index_root: Path) -> list[dict]:
    """Filter out repos already present in the index."""
    existing: set[str] = set()
    for md in index_root.rglob("*.md"):
        if md.name in ("INDEX.md", "INDEX.zh.md"):
            continue
        repo = _read_repo_from_frontmatter(md)
        key = _repo_key(repo)
        if key:
            existing.add(key)
    new = [c for c in candidates if _repo_key(c.get("repo") or c.get("html_url")) not in existing]
    return new


RESOURCE_COLLECTION_TOPICS = {
    "awesome",
    "awesome-list",
    "books",
    "education",
    "interview",
    "interview-practice",
    "interview-questions",
    "learn",
    "list",
    "lists",
    "practice",
    "resource",
    "resources",
    "tutorial",
    "tutorial-code",
    "tutorial-exercises",
    "tutorials",
}
RESOURCE_COLLECTION_RE = re.compile(
    r"\b(?:awesome|curated|collective|opinionated)\s+list\b|"
    r"\b(?:a\s+)?collection\s+of\b|\blist\s+of\b|\bprogramming\s+books?\b|"
    r"\bproject-based\s+tutorials?\b|\blearn\s+how\s+to\b|"
    r"\bmaster\s+programming\s+by\b",
    re.IGNORECASE,
)


def is_resource_collection(candidate: dict) -> bool:
    """Return true for lists, learning corpora, and reference collections."""
    repo_name = str(candidate.get("repo") or "").split("/")[-1].lower()
    if repo_name.startswith("awesome-") or repo_name.endswith("-awesome"):
        return True
    description = candidate.get("description") or ""
    if RESOURCE_COLLECTION_RE.search(description):
        return True
    topics = {str(topic).lower() for topic in candidate.get("topics") or []}
    return len(topics & RESOURCE_COLLECTION_TOPICS) >= 2


def filter_candidates(
    candidates: list[dict],
    min_stars: int,
    require_license: bool,
    exclude_archived: bool,
    exclude_forks: bool,
    include_resource_collections: bool = False,
) -> list[dict]:
    """Apply lightweight quality gate."""
    out = []
    for c in candidates:
        if c.get("stars", 0) < min_stars:
            continue
        if require_license and not c.get("license"):
            continue
        if exclude_archived and c.get("archived"):
            continue
        if exclude_forks and c.get("fork"):
            continue
        if not c.get("description"):
            continue
        if not include_resource_collections and is_resource_collection(c):
            continue
        out.append(c)
    return out


def _extract_tags_from_frontmatter(path: Path) -> list[str]:
    """Parse tags from YAML frontmatter of a project page."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end == -1:
        return []
    fm = text[3:end].strip()
    for line in fm.splitlines():
        if line.strip().startswith("tags:"):
            val = line.split("tags:", 1)[1].strip()
            if val.startswith("["):
                return [t.strip().strip('"') for t in val[1:-1].split(",") if t.strip()]
    return []


def generate_classify_report(candidates: list[dict], index_root: Path) -> str:
    """
    Produce a Markdown report that a coding agent (LLM) can read to perform
    semantic classification. Contains all category definitions + candidate info.
    """
    # Load all category definitions
    cats = {}
    for idx in index_root.rglob("INDEX.md"):
        cat = idx.parent.relative_to(index_root).as_posix()
        text = idx.read_text(encoding="utf-8")
        definition = ""
        for header in ("## What belongs here", "## 什么该放这里"):
            if header in text:
                start = text.index(header) + len(header)
                end = text.find("\n## ", start)
                if end == -1:
                    end = len(text)
                definition = text[start:end].strip()
                break
        # Collect 1-3 example project names from existing pages
        examples = []
        for md in sorted(idx.parent.rglob("*.md")):
            if md.name in ("INDEX.md", "INDEX.zh.md") or md.name.endswith(".zh.md"):
                continue
            text2 = md.read_text(encoding="utf-8")
            if not text2.startswith("---"):
                continue
            end2 = text2.find("\n---", 3)
            if end2 == -1:
                continue
            fm = text2[3:end2].strip()
            for line in fm.splitlines():
                if line.strip().startswith("name:"):
                    name = line.split("name:", 1)[1].strip()
                    if name:
                        examples.append(name)
                    break
            if len(examples) >= 3:
                break

        cats[cat] = {
            "definition": definition,
            "examples": examples,
        }

    seed = next(
        (c.get("discovery_seed") for c in candidates if c.get("discovery_seed") is not None),
        None,
    )
    source_directions = sorted(
        {
            direction
            for candidate in candidates
            for direction in candidate.get("discovery_directions") or []
        }
    )
    lines = [
        "# Classification Task — Agent Semantic Review",
        "",
        f"Discovery seed: {seed if seed is not None else 'explicit query'}",
        f"Source directions: {', '.join(source_directions) or 'explicit query'}",
        "",
        "> This report is for a coding agent (LLM) to perform semantic classification.",
        "> Read each category definition, compare it to the candidate repos, and assign",
        "> the most appropriate category by semantic fit. Do not rely on keyword matching.",
        "",
        "## Candidate Repositories",
        "",
        "| # | Repo | Directions | Stars | Lang | Description | Topics |",
        "|---|------|------------|-------|------|-------------|--------|",
    ]
    for i, c in enumerate(candidates, 1):
        stars = f"{c['stars']:,}" if c.get("stars") else "0"
        directions = ", ".join(c.get("discovery_directions") or []) or "explicit-query"
        lang = c.get("language", "")
        desc = (c.get("description") or "")[:120].replace("|", "\\|")
        topics = ", ".join(c.get("topics", []))[:80]
        lines.append(
            f"| {i} | {c['repo']} | {directions} | {stars} | {lang} | {desc} | {topics} |"
        )

    lines += [
        "",
        "## Available Categories",
        "",
        "> Read the full `categories/{cat}/INDEX.md` for deeper context if needed.",
        "",
    ]
    for cat, info in sorted(cats.items()):
        lines.append(f"### {cat}")
        lines.append(f"- **Definition:** {info['definition'][:200]}")
        lines.append(f"- **Examples:** {', '.join(info['examples'][:3]) if info['examples'] else 'none'}")
        lines.append(f"- **File:** `categories/{cat}/INDEX.md`")
        lines.append("")

    lines += [
        "## Agent Task",
        "",
        "For each candidate repo, choose the **single most appropriate** category.",
        "Consider the repo's description, topics, and what it actually does.",
        "",
        "If the repo does not fit any existing category, answer `needs-new-category`.",
        "If uncertain, answer `uncertain`.",
        "",
        "Return your classification in this exact format (one per line):",
        "",
        "```",
        "1. tauri-apps/tauri → web-ui",
        "2. rust-lang/rust → needs-new-category",
        "```",
        "",
        "After classifying, apply the results to the JSON file (set `suggested_category`),",
        "then run the report step to generate the final candidate report.",
    ]
    return "\n".join(lines)


def generate_report(candidates: list[dict]) -> str:
    """Produce a Markdown candidate report."""
    seed = next(
        (c.get("discovery_seed") for c in candidates if c.get("discovery_seed") is not None),
        None,
    )
    source_directions = sorted(
        {
            direction
            for candidate in candidates
            for direction in candidate.get("discovery_directions") or []
        }
    )
    lines = [
        "# Harvest Wave Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Discovery seed: {seed if seed is not None else 'explicit query'}",
        f"Source directions: {', '.join(source_directions) or 'explicit query'}",
        f"Candidates: {len(candidates)}",
        "",
        "> Source direction records where a candidate was discovered; semantic classification may assign a different category.",
        "",
        "| # | Repo | Directions | Stars | Lang | License | Suggested Category | Description |",
        "|---|------|------------|-------|------|---------|-------------------|-------------|",
    ]
    for i, c in enumerate(candidates, 1):
        stars = f"{c['stars']:,}" if c.get("stars") else "0"
        directions = ", ".join(c.get("discovery_directions") or []) or "explicit-query"
        lang = c.get("language", "")
        lic = c.get("license", "")
        cat = c.get("suggested_category", "")
        if not cat:
            cat = "(awaiting agent review)"
        desc = (c.get("description") or "")[:60].replace("|", "\\|")
        lines.append(
            f"| {i} | {c['repo']} | {directions} | {stars} | {lang} | {lic} | {cat} | {desc} |"
        )
    lines += [
        "",
        "## Next Steps",
        "",
        "Review the candidates and classifications. For selected repositories, run the repository's internal `add-project` skill; `harvest.py` does not create pages.",
        "",
    ]
    return "\n".join(lines)


def _cmd_search(args):
    validate_discovery_query(args.query)
    results = search_repos(args.query, args.per_page)
    Path(args.output).write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Collected {len(results)} candidates → {args.output}")


def _cmd_dedupe(args):
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    new = dedupe_candidates(data, Path(args.index_root))
    Path(args.output).write_text(json.dumps(new, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Deduplicated: {len(data)} → {len(new)} new ({len(data) - len(new)} already indexed)")


def _cmd_filter(args):
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    filt = filter_candidates(
        data,
        args.min_stars,
        args.require_license,
        args.exclude_archived,
        args.exclude_forks,
        args.include_resource_collections,
    )
    Path(args.output).write_text(json.dumps(filt, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Filtered: {len(data)} → {len(filt)} passed quality gate")


def _cmd_classify(args):
    """Output a classification task report for the agent (LLM) to review."""
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = generate_classify_report(data, Path(args.category_index))
    Path(args.output).write_text(report, encoding="utf-8")
    print(f"Classification task report written to {args.output}")
    print(f"  {len(data)} candidates × {len([p for p in Path(args.category_index).rglob('INDEX.md')])} categories")
    print(f"  Awaiting agent semantic review...")


def _cmd_report(args):
    """Generate Markdown report from classified candidates."""
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    md = generate_report(data)
    Path(args.output).write_text(md, encoding="utf-8")
    print(f"Report written to {args.output}")


def _cmd_finalize(args):
    """Generate final report after agent has assigned categories."""
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    md = generate_report(data)
    Path(args.output).write_text(md, encoding="utf-8")
    print(f"Final report written to {args.output}")
    print(f"  {len(data)} candidates with assigned categories")


def _cmd_wave(args):
    """One-shot: search → dedupe → filter → classify (agent review) → report."""
    print("=== Step 1: Search ===")
    if args.query:
        validate_discovery_query(args.query)
        discovery_seed = None
        directions = [
            {
                "category": "explicit-query",
                "description": args.query,
                "route": "",
                "query": args.query,
            }
        ]
    else:
        discovery_seed = (
            args.seed
            if args.seed is not None
            else random.SystemRandom().randrange(0, 2**32)
        )
        pushed_after = args.pushed_after or (
            datetime.now(timezone.utc).date() - timedelta(days=365)
        ).isoformat()
        directions = select_discovery_directions(
            Path(args.route_index),
            Path(args.directions_file),
            count=args.directions,
            seed=discovery_seed,
        )
        for direction in directions:
            direction["query"] = build_direction_query(direction, pushed_after)
        print(f"  seed={discovery_seed} directions={len(directions)}")

    by_repo: dict[str, dict] = {}
    for direction in directions:
        query = direction["query"]
        validate_discovery_query(query)
        found = search_repos(query, args.per_page)
        print(
            f"  direction={direction['category']} results={len(found)} query={query}"
        )
        for candidate in found:
            key = _repo_key(candidate.get("repo") or candidate.get("html_url"))
            if not key:
                continue
            if key not in by_repo:
                candidate["discovery_directions"] = [direction["category"]]
                candidate["discovery_queries"] = [query]
                if discovery_seed is not None:
                    candidate["discovery_seed"] = discovery_seed
                by_repo[key] = candidate
                continue
            existing = by_repo[key]
            if direction["category"] not in existing["discovery_directions"]:
                existing["discovery_directions"].append(direction["category"])
            if query not in existing["discovery_queries"]:
                existing["discovery_queries"].append(query)
    results = list(by_repo.values())
    print(f"  {len(results)} unique candidates across directions")

    print("=== Step 2: Deduplicate ===")
    new = dedupe_candidates(results, Path(args.index_root))
    print(f"  {len(new)} new ({len(results) - len(new)} already indexed)")

    print("=== Step 3: Filter ===")
    filt = filter_candidates(
        new,
        args.min_stars,
        args.require_license,
        args.exclude_archived,
        args.exclude_forks,
        args.include_resource_collections,
    )
    print(f"  {len(filt)} passed quality gate")

    if not filt:
        print("No candidates passed filters. Wave complete (empty).")
        return

    print("=== Step 4: Generate classification task (awaiting agent review) ===")
    # Output JSON without classification
    for c in filt:
        c["suggested_category"] = ""
    json_path = (args.output or "/tmp/harvest-wave-report.md").replace(".md", ".json")
    Path(json_path).write_text(json.dumps(filt, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  JSON: {json_path}")

    # Generate classification task report for the agent
    task_path = json_path.replace(".json", "-classify-task.md")
    task_report = generate_classify_report(filt, Path(args.index_root))
    Path(task_path).write_text(task_report, encoding="utf-8")
    print(f"  Classify task: {task_path}")
    print("  → A coding agent (LLM) should read this task and assign categories.")

    print("=== Step 5: Report (preliminary, categories pending) ===")
    report_path = args.output or "/tmp/harvest-wave-report.md"
    md = generate_report(filt)
    Path(report_path).write_text(md, encoding="utf-8")
    print(f"  Report: {report_path}")

    print("\n=== Wave Complete — Agent Review Required ===")
    print("Next: The coding agent reads the classify task and assigns categories.")
    print("      Then run: python3 tools/harvest.py finalize --input <json> --output <report.md>")


def main(argv=None):
    p = argparse.ArgumentParser(description="oss-atlas project harvester")
    sub = p.add_subparsers(dest="cmd", required=True)

    # search
    sp = sub.add_parser("search", help="Search GitHub for candidates")
    sp.add_argument("--query", required=True)
    sp.add_argument("--per-page", type=int, default=20)
    sp.add_argument("--output", required=True)
    sp.set_defaults(func=_cmd_search)

    # dedupe
    dp = sub.add_parser("dedupe", help="Deduplicate against existing index")
    dp.add_argument("--input", required=True)
    dp.add_argument("--index-root", required=True)
    dp.add_argument("--output", required=True)
    dp.set_defaults(func=_cmd_dedupe)

    # filter
    fp = sub.add_parser("filter", help="Apply quality gate")
    fp.add_argument("--input", required=True)
    fp.add_argument("--min-stars", type=int, default=0)
    fp.add_argument("--require-license", action="store_true")
    fp.add_argument("--exclude-archived", action="store_true")
    fp.add_argument("--exclude-forks", action="store_true")
    fp.add_argument("--include-resource-collections", action="store_true")
    fp.add_argument("--output", required=True)
    fp.set_defaults(func=_cmd_filter)

    # classify
    cp = sub.add_parser("classify", help="Infer category for each candidate")
    cp.add_argument("--input", required=True)
    cp.add_argument("--category-index", required=True)
    cp.add_argument("--output", required=True)
    cp.set_defaults(func=_cmd_classify)

    # report
    rp = sub.add_parser("report", help="Generate Markdown report")
    rp.add_argument("--input", required=True)
    rp.add_argument("--output", required=True)
    rp.set_defaults(func=_cmd_report)

    # wave (one-shot)
    wp = sub.add_parser("wave", help="Run full pipeline: search → dedupe → filter → agent classify → report")
    wp.add_argument("--query", help="explicit domain-specific GitHub query; omit for automatic multi-direction discovery")
    wp.add_argument("--per-page", type=int, default=5, help="results per direction")
    wp.add_argument("--directions", type=int, default=5, help="top-level categories to sample when --query is omitted")
    wp.add_argument("--seed", type=int, help="random seed for reproducible automatic direction sampling")
    wp.add_argument("--route-index", default="INDEX.md", help="root category route used for automatic direction sampling")
    wp.add_argument("--directions-file", default="tools/harvest-directions.json", help="curated category search recipes for automatic sampling")
    wp.add_argument("--pushed-after", help="YYYY-MM-DD lower bound; defaults to one year ago")
    wp.add_argument("--index-root", default="categories")
    wp.add_argument("--min-stars", type=int, default=0)
    wp.add_argument("--require-license", action="store_true")
    wp.add_argument("--exclude-archived", action="store_true", default=True)
    wp.add_argument("--exclude-forks", action="store_true", default=True)
    wp.add_argument("--include-resource-collections", action="store_true")
    wp.add_argument("--output", default="/tmp/harvest-wave-report.md")
    wp.set_defaults(func=_cmd_wave)

    # finalize (after agent assigns categories)
    fp = sub.add_parser("finalize", help="Generate final report after agent has assigned categories")
    fp.add_argument("--input", required=True, help="JSON file with agent-assigned categories")
    fp.add_argument("--output", required=True, help="Path to write final Markdown report")
    fp.set_defaults(func=_cmd_finalize)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
