#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint


HEALTH_BLOCK = """health:
  schema: 1
  computed_at: 2026-06-29T00:00:00Z
  overall: A
  overall_score: 4.0
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw: {}
    responsiveness:
      grade: A
      raw: {}
    adoption:
      grade: A
      raw: {}
    longevity:
      grade: A
      raw: {}
    governance:
      grade: A
      raw: {}
    risk_license:
      grade: A
      raw: {}
"""

UPSTREAM_BLOCK = """upstream:
  pushed_at: 2026-06-29T00:00:00Z
  default_branch: main
  default_branch_sha: 0123456789abcdef0123456789abcdef01234567
  archived: false
"""


def page_text(*, slug: str = "demo", zh: bool = False, health: bool = True, verdict: bool = True) -> str:
    title = "Demo"
    comparison = "横向对比" if zh else "Comparison"
    if zh:
        header = "| 替代品 | 是否收录 | 我们的评价 | 取舍 |" if verdict else "| 替代品 | 是否收录 | 取舍 |"
        row = "| Other | 未收录 | 优先用 Demo。 | Other is broader. |" if verdict else "| Other | 未收录 | Other is broader. |"
    else:
        header = "| Alternative | In index | Our verdict | Tradeoff |" if verdict else "| Alternative | In index | Tradeoff |"
        row = "| Other | not indexed | Prefer Demo for this case. | Other is broader. |" if verdict else "| Other | not indexed | Other is broader. |"
    separator = "|---|---|---|---|" if verdict else "|---|---|---|"
    health_block = HEALTH_BLOCK if health else ""
    card = f"![{slug} — {'健康度雷达' if zh else 'health radar'}](../../assets/health/{slug}{'.zh' if zh else ''}.svg)"
    return f"""---
name: Demo
slug: {slug}
repo: https://github.com/example/{slug}
category: demo
tags: [demo]
language: Python
license: MIT
maturity: active, 1 star (as of 2026-06)
last_verified: 2026-06-29
type: tool
{UPSTREAM_BLOCK}{health_block}---

# {title}

One-line summary.

{card if health else ''}

## {'何时使用' if zh else 'When to use'}

You use it.

## {'何时不用' if zh else 'When NOT to use'}

- Do not use it otherwise.

## {comparison}

{header}
{separator}
{row}

## {'技术栈' if zh else 'Tech stack'}

- Python.

## {'依赖' if zh else 'Dependencies'}

- None.

## {'运维难度' if zh else 'Ops difficulty'}

Low.

## {'健康度与可持续性' if zh else 'Health & viability'}

- Active.

## {'存疑（未验证）' if zh else 'Caveats (unverified)'}

- None.
"""


class LintContractTest(unittest.TestCase):
    def test_missing_health_block_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(health=False), encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("health: missing required frontmatter block" in e for e in rep.errors))

    def test_comparison_requires_our_verdict_column(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(verdict=False), encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("Comparison table must include 'Our verdict'" in e for e in rep.errors))

    def test_summary_project_table_requires_health_column(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "INDEX.md"
            path.write_text("""# demo

| Project | Use when | Page |
|---|---|---|
| Demo | Use it. | [→](demo.md) |
""", encoding="utf-8")
            rep = lint.Report()

            lint.check_summary_health_columns(path, rep)

            self.assertTrue(any("summary table must include 'Health' column" in e for e in rep.errors))

    def test_missing_upstream_block_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text().replace(UPSTREAM_BLOCK, ""), encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("upstream: missing required frontmatter block" in e for e in rep.errors))

    def test_frontmatter_parity_detects_nested_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            cat = root / "categories" / "demo"
            cat.mkdir(parents=True)
            page = cat / "demo.md"
            sibling = cat / "demo.zh.md"
            page.write_text(page_text(), encoding="utf-8")
            sibling.write_text(page_text(zh=True).replace("maintenance:\n      grade: A", "maintenance:\n      grade: E"), encoding="utf-8")

            lint.check_page(page, cat, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("frontmatter drift vs demo.zh.md" in e for e in rep.errors))

    def test_comparison_row_width_must_match_header(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            broken = page_text().replace(
                "| Other | not indexed | Prefer Demo for this case. | Other is broader. |",
                "| Other | not indexed | Prefer Demo for this case. |",
            )
            page.write_text(broken, encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("Comparison table row has 3 columns, expected 4" in e for e in rep.errors))


if __name__ == "__main__":
    unittest.main()
