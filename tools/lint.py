#!/usr/bin/env python3
"""Structural linter for oss-atlas.

This repo has no runtime logic, so it has no unit tests. THIS LINTER IS THE TEST:
it enforces the entry schema (tools/schema.md) so that every project page stays
machine-navigable for the coding agents that read this index.

Checks (ERROR = non-zero exit; WARNING = printed, exit still 0):
  - project pages: frontmatter required keys + types
  - slug == filename, category == parent dir
  - all 7 required H2 sections present
  - last_verified parses; staleness > STALE_DAYS -> WARNING
  - every category dir has INDEX.md
  - root INDEX.md links every category and vice versa
  - every project page is linked from its category INDEX (no orphans)
  - internal relative links resolve

Pure stdlib. Usage:  python3 tools/lint.py [--root .]
Env: OSS_ATLAS_STALE_DAYS (default 90)
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

REQUIRED_KEYS = ["name", "slug", "repo", "category", "tags", "language", "license", "maturity", "last_verified"]
REQUIRED_SECTIONS = [
    "## 中文摘要",
    "## When to use",
    "## When NOT to use",
    "## Comparison",
    "## Tech stack",
    "## Dependencies",
    "## Ops difficulty",
]
STALE_DAYS = int(os.environ.get("OSS_ATLAS_STALE_DAYS", "90"))

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: Path | str, msg: str) -> None:
        self.errors.append(f"ERROR  {where}: {msg}")

    def warn(self, where: Path | str, msg: str) -> None:
        self.warnings.append(f"WARN   {where}: {msg}")


def parse_frontmatter(text: str) -> dict | None:
    """Minimal YAML frontmatter parser: scalars and inline lists `[a, b]` only."""
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
        key = key.strip()
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = raw.strip().strip('"').strip("'")
    return data


def md_links(text: str) -> list[str]:
    return LINK_RE.findall(text)


def check_project_page(path: Path, category_dir: Path, rep: Report, today: dt.date) -> None:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        rep.error(path, "missing or malformed YAML frontmatter (must start with '---')")
        return

    for key in REQUIRED_KEYS:
        if key not in fm or fm[key] in ("", None, []):
            rep.error(path, f"frontmatter missing required key: {key}")

    expected_slug = path.stem
    if fm.get("slug") and fm["slug"] != expected_slug:
        rep.error(path, f"slug '{fm['slug']}' != filename '{expected_slug}'")

    if fm.get("category") and fm["category"] != category_dir.name:
        rep.error(path, f"category '{fm['category']}' != parent dir '{category_dir.name}'")

    if "tags" in fm and not isinstance(fm["tags"], list):
        rep.error(path, "tags must be an inline list: tags: [a, b]")

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

    for section in REQUIRED_SECTIONS:
        if not re.search(r"(?m)^" + re.escape(section) + r"\s*$", text):
            rep.error(path, f"missing required section: {section}")

    # internal relative links resolve
    for link in md_links(text):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = (path.parent / link.split("#", 1)[0]).resolve()
        if not target.exists():
            rep.error(path, f"broken internal link: {link}")


def check_category(category_dir: Path, rep: Report, today: dt.date) -> set[str]:
    index = category_dir / "INDEX.md"
    if not index.exists():
        rep.error(category_dir, "category directory has no INDEX.md")
        linked = set()
    else:
        linked = {
            (category_dir / l.split("#", 1)[0]).resolve()
            for l in md_links(index.read_text(encoding="utf-8"))
            if not l.startswith(("http://", "https://", "#", "mailto:"))
        }

    pages = sorted(p for p in category_dir.glob("*.md") if p.name != "INDEX.md")
    for page in pages:
        check_project_page(page, category_dir, rep, today)
        if index.exists() and page.resolve() not in linked:
            rep.error(page, f"orphan: not linked from {index.name}")
    return {category_dir.name for _ in pages} if pages else set()


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

    category_dirs = sorted(d for d in categories_dir.iterdir() if d.is_dir())
    for cat in category_dirs:
        check_category(cat, rep, today)

    # root INDEX.md <-> categories consistency
    root_index = root / "INDEX.md"
    if not root_index.exists():
        rep.error(root, "missing root INDEX.md (level-1 category route)")
    else:
        idx_text = root_index.read_text(encoding="utf-8")
        linked = {
            (root / l.split("#", 1)[0]).resolve()
            for l in md_links(idx_text)
            if not l.startswith(("http://", "https://", "#", "mailto:"))
        }
        for cat in category_dirs:
            cat_index = (cat / "INDEX.md").resolve()
            if cat_index not in linked and cat.resolve() not in linked:
                rep.error(root_index, f"category '{cat.name}' not linked from root INDEX.md")
        for link in md_links(idx_text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (root / link.split("#", 1)[0]).resolve().exists():
                rep.error(root_index, f"broken internal link: {link}")

    for w in rep.warnings:
        print(w)
    for e in rep.errors:
        print(e)

    n_pages = sum(len(list(c.glob("*.md"))) - (1 if (c / "INDEX.md").exists() else 0) for c in category_dirs)
    print(f"\n{len(category_dirs)} categories, {n_pages} project pages, "
          f"{len(rep.errors)} errors, {len(rep.warnings)} warnings.")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
