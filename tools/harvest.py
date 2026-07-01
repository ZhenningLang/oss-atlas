#!/usr/bin/env python3
"""
oss-atlas project harvester — batch discovery and intake automation.

One trigger = one wave. Collect → dedupe → filter → classify → report → create.

Usage:
  python3 tools/harvest.py search --query "language:python stars:>1000" --per-page 20 --output wave.json
  python3 tools/harvest.py dedupe --input wave.json --index-root categories/ --output wave-new.json
  python3 tools/harvest.py filter --input wave-new.json --min-stars 100 --output wave-filt.json
  python3 tools/harvest.py classify --input wave-filt.json --category-index categories/ --output wave-cls.json
  python3 tools/harvest.py report --input wave-cls.json --output wave-report.md
  python3 tools/harvest.py wave --query "..." --per-page 15 --auto-create --git-commit

Requires: Python 3.9+ (stdlib only). GitHub auth via GITHUB_TOKEN env or gh CLI.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
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


def dedupe_candidates(candidates: list[dict], index_root: Path) -> list[dict]:
    """Filter out repos already present in the index."""
    existing: set[str] = set()
    for md in index_root.rglob("*.md"):
        if md.name in ("INDEX.md", "INDEX.zh.md"):
            continue
        repo = _read_repo_from_frontmatter(md)
        if repo:
            existing.add(repo)
    new = [c for c in candidates if c.get("repo") not in existing]
    return new


def filter_candidates(candidates: list[dict], min_stars: int, require_license: bool, exclude_archived: bool, exclude_forks: bool) -> list[dict]:
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
        cat = idx.parent.name
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
            if md.name in ("INDEX.md", "INDEX.zh.md"):
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

    lines = [
        "# Classification Task — Agent Semantic Review",
        "",
        "> This report is for a coding agent (LLM) to perform semantic classification.",
        "> Read each category definition, compare it to the candidate repos, and assign",
        "> the most appropriate category by semantic fit. Do not rely on keyword matching.",
        "",
        "## Candidate Repositories",
        "",
        "| # | Repo | Stars | Lang | Description | Topics |",
        "|---|------|-------|------|-------------|--------|",
    ]
    for i, c in enumerate(candidates, 1):
        stars = f"{c['stars']:,}" if c.get("stars") else "0"
        lang = c.get("language", "")
        desc = (c.get("description") or "")[:120].replace("|", "\\|")
        topics = ", ".join(c.get("topics", []))[:80]
        lines.append(f"| {i} | {c['repo']} | {stars} | {lang} | {desc} | {topics} |")

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
    lines = [
        "# Harvest Wave Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Candidates: {len(candidates)}",
        "",
        "| # | Repo | Stars | Lang | License | Suggested Category | Description |",
        "|---|------|-------|------|---------|-------------------|-------------|",
    ]
    for i, c in enumerate(candidates, 1):
        stars = f"{c['stars']:,}" if c.get("stars") else "0"
        lang = c.get("language", "")
        lic = c.get("license", "")
        cat = c.get("suggested_category", "")
        if not cat:
            cat = "(awaiting agent review)"
        desc = (c.get("description") or "")[:60].replace("|", "\\|")
        lines.append(f"| {i} | {c['repo']} | {stars} | {lang} | {lic} | {cat} | {desc} |")
    lines += ["", "## Next Steps", "", "Select which candidates to add, then run:", "", "```bash", "python3 tools/harvest.py create-page --repo <owner/repo> --category <cat>", "```", ""]
    return "\n".join(lines)


def _cmd_search(args):
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
    filt = filter_candidates(data, args.min_stars, args.require_license, args.exclude_archived, args.exclude_forks)
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
    results = search_repos(args.query, args.per_page)
    print(f"  {len(results)} candidates")

    print("=== Step 2: Deduplicate ===")
    new = dedupe_candidates(results, Path(args.index_root))
    print(f"  {len(new)} new ({len(results) - len(new)} already indexed)")

    print("=== Step 3: Filter ===")
    filt = filter_candidates(new, args.min_stars, args.require_license, args.exclude_archived, args.exclude_forks)
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
    fp.add_argument("--min-stars", type=int, default=100)
    fp.add_argument("--require-license", action="store_true")
    fp.add_argument("--exclude-archived", action="store_true")
    fp.add_argument("--exclude-forks", action="store_true")
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
    wp.add_argument("--query", required=True)
    wp.add_argument("--per-page", type=int, default=15)
    wp.add_argument("--index-root", default="categories")
    wp.add_argument("--min-stars", type=int, default=100)
    wp.add_argument("--require-license", action="store_true", default=True)
    wp.add_argument("--exclude-archived", action="store_true", default=True)
    wp.add_argument("--exclude-forks", action="store_true", default=True)
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
