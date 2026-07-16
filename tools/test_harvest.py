#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import harvest


class HarvestTest(unittest.TestCase):
    def test_select_discovery_directions_picks_five_unique_reproducibly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = root / "INDEX.md"
            directions_file = root / "directions.json"
            rows = [
                f"| **category-{i}** | Domain {i} tools. | [→](categories/category-{i}/INDEX.md) |"
                for i in range(8)
            ]
            index.write_text(
                "# route\n\n| Category | Use when | Route |\n|---|---|---|\n"
                + "\n".join(rows)
                + "\n",
                encoding="utf-8",
            )
            directions_file.write_text(
                "[\n"
                + ",\n".join(
                    f'  {{"category": "category-{i}", "query": "\\"domain {i}\\" in:name,description"}}'
                    for i in range(8)
                )
                + "\n]\n",
                encoding="utf-8",
            )

            first = harvest.select_discovery_directions(
                index, directions_file, count=5, seed=42
            )
            second = harvest.select_discovery_directions(
                index, directions_file, count=5, seed=42
            )

            self.assertEqual(first, second)
            self.assertEqual(len(first), 5)
            self.assertEqual(len({item["category"] for item in first}), 5)
            self.assertTrue(
                all(item["route"].endswith("/INDEX.md") for item in first)
            )
            self.assertTrue(all("in:name,description" in item["query"] for item in first))

    def test_build_direction_query_contains_domain_signal(self) -> None:
        query = harvest.build_direction_query(
            {
                "category": "agent-governance",
                "description": "Agent policy tools.",
                "query": '"agent governance" in:name,description',
            },
            pushed_after="2025-07-17",
        )

        self.assertIn("agent governance", query)
        self.assertIn("pushed:>2025-07-17", query)
        harvest.validate_discovery_query(query)

    def test_dedupe_normalizes_github_url_and_owner_repo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "demo.md"
            page.write_text(
                "---\nrepo: https://github.com/Example/Project.git\n---\n",
                encoding="utf-8",
            )

            candidates = [
                {"repo": "example/project"},
                {"repo": "example/new-project"},
            ]

            self.assertEqual(
                harvest.dedupe_candidates(candidates, root),
                [{"repo": "example/new-project"}],
            )

    def test_filter_excludes_resource_collections_by_default(self) -> None:
        candidates = [
            {
                "repo": "example/runtime",
                "stars": 1000,
                "license": "MIT",
                "description": "A runtime for executing workflow jobs",
                "topics": ["runtime", "workflow"],
                "archived": False,
                "fork": False,
            },
            {
                "repo": "example/awesome-list",
                "stars": 1000,
                "license": "MIT",
                "description": "An awesome list of Python libraries and resources",
                "topics": ["awesome", "list", "resources"],
                "archived": False,
                "fork": False,
            },
            {
                "repo": "example/tutorials",
                "stars": 1000,
                "license": "MIT",
                "description": "A curated list of project-based tutorials",
                "topics": ["tutorial", "education", "list"],
                "archived": False,
                "fork": False,
            },
        ]

        self.assertEqual(
            harvest.filter_candidates(
                candidates,
                min_stars=100,
                require_license=True,
                exclude_archived=True,
                exclude_forks=True,
                include_resource_collections=False,
            ),
            [candidates[0]],
        )
        self.assertEqual(
            harvest.filter_candidates(
                candidates,
                min_stars=100,
                require_license=True,
                exclude_archived=True,
                exclude_forks=True,
                include_resource_collections=True,
            ),
            candidates,
        )

    def test_filter_keeps_low_star_and_unparsed_license_by_default(self) -> None:
        candidate = {
            "repo": "example/niche-tool",
            "stars": 3,
            "license": "",
            "description": "A CLI for inspecting binary protocol frames",
            "topics": ["cli", "protocol"],
            "archived": False,
            "fork": False,
        }

        self.assertEqual(
            harvest.filter_candidates(
                [candidate],
                min_stars=0,
                require_license=False,
                exclude_archived=True,
                exclude_forks=True,
            ),
            [candidate],
        )

    def test_resource_filter_catches_awesome_collections_and_tutorial_corpora(self) -> None:
        candidates = [
            {
                "repo": "example/awesome-mcp-servers",
                "stars": 100,
                "license": "MIT",
                "description": "A collection of MCP servers.",
                "topics": ["ai", "mcp"],
                "archived": False,
                "fork": False,
            },
            {
                "repo": "example/build-your-own-x",
                "stars": 100,
                "license": "",
                "description": "Master programming by recreating technologies from scratch.",
                "topics": ["awesome-list", "tutorial-code", "tutorials"],
                "archived": False,
                "fork": False,
            },
        ]

        self.assertEqual(
            harvest.filter_candidates(
                candidates,
                min_stars=0,
                require_license=False,
                exclude_archived=True,
                exclude_forks=True,
            ),
            [],
        )

    def test_generic_language_high_star_query_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "domain or task signal"):
            harvest.validate_discovery_query(
                "language:python stars:>1000 pushed:>2026-01-01 sort:stars"
            )

        harvest.validate_discovery_query(
            '"agent governance" in:name,description,readme pushed:>2026-01-01'
        )

    def test_classify_report_preserves_nested_category_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            category = root / "agent-frameworks" / "workflow-builders"
            category.mkdir(parents=True)
            (category / "INDEX.md").write_text(
                "# workflow-builders\n\n## What belongs here\n\nWorkflow builders.\n",
                encoding="utf-8",
            )
            (category / "demo.md").write_text(
                "---\nname: Demo\nrepo: https://github.com/example/demo\n---\n",
                encoding="utf-8",
            )
            (category / "demo.zh.md").write_text(
                "---\nname: Demo\nrepo: https://github.com/example/demo\n---\n",
                encoding="utf-8",
            )

            report = harvest.generate_classify_report([], root)

            self.assertIn("### agent-frameworks/workflow-builders", report)
            self.assertIn(
                "`categories/agent-frameworks/workflow-builders/INDEX.md`",
                report,
            )
            self.assertIn("- **Examples:** Demo", report)
            self.assertNotIn("- **Examples:** Demo, Demo", report)


if __name__ == "__main__":
    unittest.main()
