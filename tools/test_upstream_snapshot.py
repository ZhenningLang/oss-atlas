#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import upstream_snapshot


PAGE = """---
name: Demo
slug: demo
repo: https://github.com/example/demo
category: demo
tags: [demo]
language: Python
license: MIT
maturity: active, 1 star (as of 2026-06)
last_verified: 2026-06-29
type: tool
health:
  schema: 1
---

# Demo
"""

SNAPSHOT = {
    "pushed_at": "2026-06-29T00:00:00Z",
    "default_branch": "main",
    "default_branch_sha": "0123456789abcdef0123456789abcdef01234567",
    "archived": False,
}


class UpstreamSnapshotTest(unittest.TestCase):
    def test_inserts_upstream_before_health(self) -> None:
        text, changed = upstream_snapshot.upsert_snapshot(PAGE, SNAPSHOT)

        self.assertTrue(changed)
        self.assertIn("upstream:\n  pushed_at: 2026-06-29T00:00:00Z", text)
        self.assertLess(text.index("upstream:"), text.index("health:"))

    def test_replaces_existing_upstream_block(self) -> None:
        existing = PAGE.replace("health:\n", "upstream:\n  pushed_at: old\n  default_branch: main\n  default_branch_sha: old\n  archived: false\nhealth:\n")

        text, changed = upstream_snapshot.upsert_snapshot(existing, SNAPSHOT)

        self.assertTrue(changed)
        self.assertNotIn("default_branch_sha: old", text)
        self.assertEqual(text.count("upstream:"), 1)

    def test_parse_upstream_round_trips_rendered_block(self) -> None:
        text, _ = upstream_snapshot.upsert_snapshot(PAGE, SNAPSHOT)

        self.assertEqual(upstream_snapshot.parse_upstream(text), SNAPSHOT)


if __name__ == "__main__":
    unittest.main()
