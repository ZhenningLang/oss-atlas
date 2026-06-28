#!/usr/bin/env python3
"""Structural linter for oss-atlas.

This repo has no runtime logic, so it has no unit tests. THIS LINTER IS THE TEST:
it enforces the entry schema (tools/schema.md) so the index stays machine-navigable
for the coding agents that read it.

Model:
  - Bilingual pair: each project is <slug>.md (English, canonical) + <slug>.zh.md.
  - Recursive taxonomy: categories/ is a tree of arbitrary depth. A directory with an
    INDEX.md is a *category node*; it may hold project pages AND/OR child sub-categories.
    Routing splits by language: INDEX.md (EN) + INDEX.zh.md (ZH) at every node and the root.
  - type-adaptive sections: frontmatter `type` decides which body sections are required.
    skill-pack pages omit Tech stack / Dependencies / Ops difficulty.

Checks (ERROR = non-zero exit; WARNING = printed, exit still 0):
  - each page: required frontmatter keys + types, slug==base filename, category==parent dir,
    type in the allowed set, required body sections for its type+language, sibling parity
  - each page starts with an H1 title (`# <name>`) -> ERROR if absent
  - bilingual pair frontmatter is identical (facts are language-neutral) -> ERROR on any drift
  - skill-pack pages must OMIT Tech stack / Dependencies / Ops difficulty (not pad them) -> ERROR if present
  - last_verified parses; staleness > STALE_DAYS -> WARNING
  - every page: a Caveats ledger section (## Caveats (unverified) / ## 存疑（未验证）) -> ERROR if absent
  - prose-region [未验证]/[推断] density > PROSE_LABEL_MAX -> WARNING (converge into the Caveats section)
  - every directory under categories/ is a category node: must have INDEX.md + INDEX.zh.md
    (traversal is NOT gated on INDEX existence, so a dir missing its INDEX is reported, not skipped)
  - pages/sub-categories linked from their node INDEX; root INDEX links the top categories
  - recursive: sub-categories validated to any depth
  - leaf category with > MAX_FANOUT pages -> WARNING (self-balancing: split via refactor-index)
  - internal relative links resolve
  - .zh.md bodies use fullwidth Chinese punctuation: ASCII , ; ! ? : adjacent to a CJK char
    -> ERROR (frontmatter / code / links / URLs are exempt; facts stay language-neutral)
  - README.md / README.zh.md master listing stays in parity with the indexed pages
    (every EN page listed in README.md, every ZH page in README.zh.md) -> ERROR on drift

NOTE: this linter is a STRUCTURAL gate, not a semantic review. It cannot judge whether a
"When to use" is a real User Story, whether a Comparison compares real substitutes, or whether
prose is accurate — those stay human/agent judgment (see tools/schema.md).

Pure stdlib. Usage:  python3 tools/lint.py [--root .]
Env: OSS_ATLAS_STALE_DAYS (default 90), OSS_ATLAS_MAX_FANOUT (default 12),
     OSS_ATLAS_PROSE_LABEL_MAX (default 3)
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

REQUIRED_KEYS = ["name", "slug", "repo", "category", "tags", "language", "license", "maturity", "last_verified", "type"]
ALLOWED_TYPES = {"tool", "library", "app", "framework", "service", "model", "skill-pack"}
CORE_EN = ["## When to use", "## When NOT to use", "## Comparison"]
EXTRA_EN = ["## Tech stack", "## Dependencies", "## Ops difficulty"]
CORE_ZH = ["## 何时使用", "## 何时不用", "## 横向对比"]
EXTRA_ZH = ["## 技术栈", "## 依赖", "## 运维难度"]
NO_EXTRA_TYPES = {"skill-pack"}  # these omit Tech stack / Dependencies / Ops difficulty

INDEX_EN = "INDEX.md"
INDEX_ZH = "INDEX.zh.md"
ZH_SUFFIX = ".zh.md"
STALE_DAYS = int(os.environ.get("OSS_ATLAS_STALE_DAYS", "90"))
MAX_FANOUT = int(os.environ.get("OSS_ATLAS_MAX_FANOUT", "12"))
PROSE_LABEL_MAX = int(os.environ.get("OSS_ATLAS_PROSE_LABEL_MAX", "3"))

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
# Caveats ledger heading — tolerant prefix match (the parenthetical varies: (unverified)/（未验证）).
CAVEATS_RE_EN = re.compile(r"(?m)^##\s+Caveats\b")
CAVEATS_RE_ZH = re.compile(r"(?m)^##\s+存疑")
LABEL_RE = re.compile(r"\[未验证\]|\[推断\]")
# Chinese punctuation: ASCII , ; ! ? : adjacent to a CJK char in a .zh.md body should be the
# fullwidth form (，；！？：). Detection mirrors the normalizer: skip frontmatter, fenced/inline
# code, link targets, and URLs; flag only ASCII punctuation touching a CJK ideograph.
CJK_RANGE = "㐀-䶿一-鿿"
ZH_PUNCT_PROTECT = re.compile(r"`[^`]*`|\]\([^)]*\)|https?://\S+")
ZH_PUNCT_HIT = re.compile(r"[" + CJK_RANGE + r"][,;!?:]|[,;!?:][" + CJK_RANGE + r"]")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: Path | str, msg: str) -> None:
        self.errors.append(f"ERROR  {where}: {msg}")

    def warn(self, where: Path | str, msg: str) -> None:
        self.warnings.append(f"WARN   {where}: {msg}")


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    data: dict = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key, raw = key.strip(), raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = raw.strip().strip('"').strip("'")
    return data


def md_links(text: str) -> list[str]:
    return LINK_RE.findall(text)


def zh_punct_violations(text: str) -> int:
    """Count ASCII , ; ! ? : adjacent to a CJK char in a .zh.md body.

    Skips YAML frontmatter (facts, kept identical to the EN sibling), fenced code blocks,
    inline code, link targets, and URLs — the same regions the normalizer protects.
    """
    n = 0
    in_front = in_fence = False
    for i, line in enumerate(text.split("\n")):
        if i == 0 and line.strip() == "---":
            in_front = True
            continue
        if in_front:
            if line.strip() == "---":
                in_front = False
            continue
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        n += len(ZH_PUNCT_HIT.findall(ZH_PUNCT_PROTECT.sub("", line)))
    return n


def linked_targets(index_path: Path) -> set[Path]:
    if not index_path.exists():
        return set()
    return {
        (index_path.parent / l.split("#", 1)[0]).resolve()
        for l in md_links(index_path.read_text(encoding="utf-8"))
        if not l.startswith(("http://", "https://", "#", "mailto:"))
    }


def is_page(name: str) -> bool:
    return name.endswith(".md") and name not in (INDEX_EN, INDEX_ZH)


def base_slug(name: str) -> str:
    return name[: -len(ZH_SUFFIX)] if name.endswith(ZH_SUFFIX) else name[: -len(".md")]


def required_sections(ptype: str, zh: bool) -> list[str]:
    core = CORE_ZH if zh else CORE_EN
    extra = EXTRA_ZH if zh else EXTRA_EN
    return core + ([] if ptype in NO_EXTRA_TYPES else extra)


def check_page(path: Path, category_dir: Path, rep: Report, today: dt.date) -> None:
    name = path.name
    zh = name.endswith(ZH_SUFFIX)
    base = base_slug(name)
    text = path.read_text(encoding="utf-8")

    fm = parse_frontmatter(text)
    if fm is None:
        rep.error(path, "missing or malformed YAML frontmatter (must start with '---')")
        return

    for key in REQUIRED_KEYS:
        if key not in fm or fm[key] in ("", None, []):
            rep.error(path, f"frontmatter missing required key: {key}")

    if fm.get("slug") and fm["slug"] != base:
        rep.error(path, f"slug '{fm['slug']}' != base filename '{base}'")
    if fm.get("category") and fm["category"] != category_dir.name:
        rep.error(path, f"category '{fm['category']}' != parent dir '{category_dir.name}'")
    if "tags" in fm and not isinstance(fm["tags"], list):
        rep.error(path, "tags must be an inline list: tags: [a, b]")

    ptype = fm.get("type", "")
    if ptype and ptype not in ALLOWED_TYPES:
        rep.error(path, f"type '{ptype}' not in {sorted(ALLOWED_TYPES)}")

    lv = fm.get("last_verified", "")
    if lv:
        try:
            d = dt.date.fromisoformat(str(lv))
            age = (today - d).days
            if age > STALE_DAYS:
                rep.warn(path, f"stale: last_verified {lv} is {age}d old (> {STALE_DAYS}); run sync-entry")
            if d > today:
                rep.error(path, f"last_verified {lv} is in the future")
        except ValueError:
            rep.error(path, f"last_verified '{lv}' is not a valid YYYY-MM-DD date")

    # H1 title: schema requires every page to open with `# <name>` (then a one-line TL;DR).
    if not re.search(r"(?m)^#[ \t]+\S", text):
        rep.error(path, "missing H1 title (`# <name>`) at the top of the page")

    for section in required_sections(ptype if ptype in ALLOWED_TYPES else "tool", zh):
        if not re.search(r"(?m)^" + re.escape(section) + r"\s*$", text):
            rep.error(path, f"missing required section: {section}")

    # skill-pack pages must OMIT the extra sections, not pad them — forbid, don't just not-require.
    if ptype in NO_EXTRA_TYPES:
        for section in (EXTRA_ZH if zh else EXTRA_EN):
            if re.search(r"(?m)^" + re.escape(section) + r"\s*$", text):
                rep.error(path, f"skill-pack must omit (not include) section: {section}")

    # Caveats ledger (all types): the uncertainty list lives here, not sprinkled across the prose.
    cav_re = CAVEATS_RE_ZH if zh else CAVEATS_RE_EN
    cav = cav_re.search(text)
    if cav is None:
        rep.error(path, "missing required section: ## 存疑（未验证） / ## Caveats (unverified)")
    # Prose-region label density: keep only load-bearing [未验证]/[推断] inline; converge the rest.
    prose = text[: cav.start()] if cav else text
    n_inline = len(LABEL_RE.findall(prose))
    if n_inline > PROSE_LABEL_MAX:
        rep.warn(path, f"{n_inline} inline [未验证]/[推断] before the Caveats section (> {PROSE_LABEL_MAX}); "
                       f"keep load-bearing ones, move the rest into the Caveats ledger")

    sibling = category_dir / (base + (".md" if zh else ZH_SUFFIX))
    if not sibling.exists():
        rep.error(path, f"missing {'English' if zh else 'Chinese'} sibling: {sibling.name}")
    elif not zh:
        # Frontmatter is facts (language-neutral) -> must be identical across the bilingual pair.
        # Compare parsed key/value (tolerant of quoting/whitespace; catches real fact drift).
        zh_fm = parse_frontmatter(sibling.read_text(encoding="utf-8"))
        if zh_fm is not None and fm is not None:
            drift = sorted(k for k in set(fm) | set(zh_fm) if fm.get(k) != zh_fm.get(k))
            if drift:
                rep.error(path, f"frontmatter drift vs {sibling.name} (must be identical): {drift}")

    for link in md_links(text):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (path.parent / link.split("#", 1)[0]).resolve().exists():
            rep.error(path, f"broken internal link: {link}")


def walk_category(catdir: Path, rep: Report, today: dt.date) -> None:
    en_index, zh_index = catdir / INDEX_EN, catdir / INDEX_ZH
    if not en_index.exists():
        rep.error(catdir, f"category node has no {INDEX_EN}")
    if not zh_index.exists():
        rep.error(catdir, f"category node has no {INDEX_ZH}")
    en_linked, zh_linked = linked_targets(en_index), linked_targets(zh_index)

    pages = sorted(p for p in catdir.glob("*.md") if is_page(p.name))
    n_en_pages = 0
    for page in pages:
        check_page(page, catdir, rep, today)
        zh = page.name.endswith(ZH_SUFFIX)
        if not zh:
            n_en_pages += 1
        idx_linked = zh_linked if zh else en_linked
        idx_name = INDEX_ZH if zh else INDEX_EN
        if (zh_index if zh else en_index).exists() and page.resolve() not in idx_linked:
            rep.error(page, f"orphan: not linked from {idx_name}")
    if n_en_pages > MAX_FANOUT:
        rep.warn(catdir, f"overflow: {n_en_pages} pages > MAX_FANOUT={MAX_FANOUT}; split into sub-categories (refactor-index)")

    # Treat EVERY non-hidden subdirectory as a category node — do NOT gate on INDEX.md existing,
    # or a dir missing its INDEX (e.g. only INDEX.zh.md, or just pages) would be silently skipped.
    # walk_category() reports the missing INDEX, so the subtree is inspected instead of dropped.
    subcats = sorted(d for d in catdir.iterdir() if d.is_dir() and not d.name.startswith("."))
    for sub in subcats:
        if en_index.exists() and (sub / INDEX_EN).resolve() not in en_linked and sub.resolve() not in en_linked:
            rep.error(en_index, f"sub-category '{sub.name}' not linked from {INDEX_EN}")
        if zh_index.exists() and (sub / INDEX_ZH).resolve() not in zh_linked and sub.resolve() not in zh_linked:
            rep.error(zh_index, f"sub-category '{sub.name}' not linked from {INDEX_ZH}")
        walk_category(sub, rep, today)

    # INDEX internal links resolve
    for idx in (en_index, zh_index):
        if not idx.exists():
            continue
        for link in md_links(idx.read_text(encoding="utf-8")):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (idx.parent / link.split("#", 1)[0]).resolve().exists():
                rep.error(idx, f"broken internal link: {link}")


def check_root_index(root: Path, index_name: str, cat_index_name: str,
                     top_categories: list[Path], rep: Report) -> None:
    root_index = root / index_name
    if not root_index.exists():
        rep.error(root, f"missing root {index_name}")
        return
    linked = linked_targets(root_index)
    for cat in top_categories:
        if (cat / cat_index_name).resolve() not in linked and cat.resolve() not in linked:
            rep.error(root_index, f"top category '{cat.name}' not linked (expected {cat.name}/{cat_index_name})")
    for link in md_links(root_index.read_text(encoding="utf-8")):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (root / link.split("#", 1)[0]).resolve().exists():
            rep.error(root_index, f"broken internal link: {link}")


def count_pages(catdir: Path) -> tuple[int, int]:
    en = zh = 0
    for p in catdir.rglob("*.md"):
        if not is_page(p.name):
            continue
        if p.name.endswith(ZH_SUFFIX):
            zh += 1
        else:
            en += 1
    return en, zh


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    rep = Report()
    today = dt.date.today()

    categories_dir = root / "categories"
    if not categories_dir.is_dir():
        rep.error(root, "no categories/ directory")
        print("\n".join(rep.errors))
        return 1

    # Every non-hidden dir under categories/ is a top-level category node (not gated on INDEX.md;
    # see walk_category — a node missing its INDEX is reported, never skipped).
    top_categories = sorted(d for d in categories_dir.iterdir() if d.is_dir() and not d.name.startswith("."))
    for cat in top_categories:
        walk_category(cat, rep, today)

    check_root_index(root, INDEX_EN, INDEX_EN, top_categories, rep)
    check_root_index(root, INDEX_ZH, INDEX_ZH, top_categories, rep)

    # Chinese punctuation: fullwidth in CJK context across every .zh.md (pages, INDEX, README).
    for zh in sorted(root.rglob("*.zh.md")):
        if any(part.startswith(".") for part in zh.relative_to(root).parts):
            continue
        v = zh_punct_violations(zh.read_text(encoding="utf-8"))
        if v:
            rep.error(zh, f"{v} ASCII , ; ! ? : adjacent to CJK — use fullwidth 中文标点 （，；！？：）")

    # README master listing must stay in parity with the indexed pages (guards silent drift):
    # README.md lists every EN page, README.zh.md lists every ZH page.
    en_pages = [p for p in categories_dir.rglob("*.md")
                if is_page(p.name) and not p.name.endswith(ZH_SUFFIX)]
    for readme_name, want_zh in (("README.md", False), ("README.zh.md", True)):
        rp = root / readme_name
        if not rp.exists():
            rep.error(root, f"missing {readme_name}")
            continue
        body = rp.read_text(encoding="utf-8")
        for en in sorted(en_pages):
            rel = en.relative_to(root).as_posix()
            target = (rel[: -len(".md")] + ZH_SUFFIX) if want_zh else rel
            if target not in body:
                rep.error(rp, f"indexed page not listed in {readme_name}: {target}")

    for w in rep.warnings:
        print(w)
    for e in rep.errors:
        print(e)

    n_en, n_zh = count_pages(categories_dir)
    n_nodes = sum(1 for d in categories_dir.rglob("*") if d.is_dir() and (d / INDEX_EN).exists())
    print(f"\n{n_nodes} category nodes, {n_en} EN + {n_zh} ZH pages, "
          f"{len(rep.errors)} errors, {len(rep.warnings)} warnings.")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
