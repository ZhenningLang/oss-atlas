#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import health_backfill


PAGE_TEMPLATE = """---
name: {name}
slug: {slug}
repo: https://github.com/example/{slug}
category: demo
tags: [demo]
language: Python
license: MIT
maturity: active, 1 star (2026-06)
last_verified: 2026-06-29
type: tool
{health}---

# {name}

One-line summary.

## When to use
"""


def write_page(root: Path, slug: str, *, health: bool = False) -> Path:
    cat = root / "categories" / "demo"
    cat.mkdir(parents=True, exist_ok=True)
    health_block = "health:\n  schema: 1\n  overall: A\n" if health else ""
    page = cat / f"{slug}.md"
    page.write_text(PAGE_TEMPLATE.format(name=slug.title(), slug=slug, health=health_block), encoding="utf-8")
    (cat / f"{slug}.zh.md").write_text(PAGE_TEMPLATE.format(name=slug.title(), slug=slug, health=health_block), encoding="utf-8")
    if health:
        health_backfill.ensure_card_embed(page, root)
        health_backfill.ensure_card_embed(cat / f"{slug}.zh.md", root)
    return page


def write_card(root: Path, slug: str) -> None:
    cards = root / "assets" / "health"
    cards.mkdir(parents=True, exist_ok=True)
    (cards / f"{slug}.svg").write_text("<svg />", encoding="utf-8")
    (cards / f"{slug}.zh.svg").write_text("<svg />", encoding="utf-8")


class HealthBackfillTest(unittest.TestCase):
    def test_discovers_only_english_project_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            missing = write_page(root, "missing")
            write_page(root, "already", health=True)
            (root / "categories" / "demo" / "INDEX.md").write_text("# Demo\n", encoding="utf-8")

            pages = health_backfill.discover_pages(root)

            self.assertEqual([p.relative_to(root) for p in pages], [Path("categories/demo/already.md"), missing.relative_to(root)])

    def test_plan_counts_existing_and_missing_health_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "missing")
            write_page(root, "already", health=True)
            write_card(root, "already")

            plan = health_backfill.build_plan(root, limit=None, resume_state=None)

            self.assertEqual(plan.total, 2)
            self.assertEqual(plan.missing_health, 1)
            self.assertEqual(plan.existing_health, 1)
            self.assertEqual([p.path.name for p in plan.items_to_process], ["missing.md"])

    def test_resume_skips_done_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            done = write_page(root, "done", health=True)
            todo = write_page(root, "todo")
            write_card(root, "done")
            state = health_backfill.BackfillState(done={str(done.relative_to(root))}, failed={})

            plan = health_backfill.build_plan(root, limit=None, resume_state=state)

            self.assertEqual([p.path.name for p in plan.items_to_process], [todo.name])
            self.assertEqual(plan.resume_skipped, 1)

    def test_resume_does_not_skip_done_page_when_card_file_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            done = write_page(root, "done", health=True)
            state = health_backfill.BackfillState(done={str(done.relative_to(root))}, failed={})

            plan = health_backfill.build_plan(root, limit=None, resume_state=state)

            self.assertEqual([p.path.name for p in plan.items_to_process], [done.name])
            self.assertEqual(plan.resume_skipped, 0)

    def test_ensure_card_embed_inserts_after_tldr(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = write_page(root, "radar", health=False)

            changed = health_backfill.ensure_card_embed(page, root)
            text = page.read_text(encoding="utf-8")

            self.assertTrue(changed)
            self.assertIn("![radar — health radar](../../assets/health/radar.svg)", text)
            self.assertLess(text.index("![radar"), text.index("## When to use"))

    def test_ensure_card_embed_uses_zh_label(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "radar", health=False)
            page = root / "categories" / "demo" / "radar.zh.md"

            health_backfill.ensure_card_embed(page, root)
            text = page.read_text(encoding="utf-8")

            self.assertIn("![radar — 健康度雷达](../../assets/health/radar.zh.svg)", text)

    def test_duplicate_slugs_use_category_prefixed_card_refs(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            first_cat = root / "categories" / "first"
            second_cat = root / "categories" / "second"
            first_cat.mkdir(parents=True, exist_ok=True)
            second_cat.mkdir(parents=True, exist_ok=True)
            (first_cat / "art.md").write_text(PAGE_TEMPLATE.format(name="Art", slug="art", health=""), encoding="utf-8")
            (second_cat / "art.md").write_text(PAGE_TEMPLATE.format(name="Art", slug="art", health=""), encoding="utf-8")
            page = first_cat / "art.md"

            health_backfill.ensure_card_embed(page, root)

            text = page.read_text(encoding="utf-8")
            self.assertIn("![art — health radar](../../assets/health/first-art.svg)", text)
            self.assertNotIn("assets/health/art.svg", text)

    def test_plan_includes_existing_health_when_card_embed_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = write_page(root, "needs-card", health=False)
            text = page.read_text(encoding="utf-8")
            page.write_text(text.replace("type: tool\n", "type: tool\nhealth:\n  schema: 1\n  overall: A\n"), encoding="utf-8")

            plan = health_backfill.build_plan(root, limit=None, resume_state=None)

            self.assertEqual([p.path.name for p in plan.items_to_process], ["needs-card.md"])
            self.assertTrue(plan.items_to_process[0].has_health)
            self.assertFalse(plan.items_to_process[0].has_card)


if __name__ == "__main__":
    unittest.main()
