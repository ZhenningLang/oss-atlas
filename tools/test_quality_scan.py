#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quality_scan


ZERO_SHA = "0000000000000000000000000000000000000000"


def write_page(root: Path, rel: str, body: str, *, sha: str = "0123456789abcdef0123456789abcdef01234567") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    slug = path.name.removesuffix(".zh.md").removesuffix(".md")
    path.write_text(
        f"""---
name: {slug}
slug: {slug}
repo: https://github.com/example/{slug}
category: {path.parent.name}
tags: [demo]
language: Python
license: MIT
maturity: active
last_verified: 2026-07-04
type: tool
upstream:
  pushed_at: 2026-07-04T00:00:00Z
  default_branch: main
  default_branch_sha: {sha}
  archived: false
health:
  schema: 1
  axes:
    maintenance:
      grade: ?
      reason: missing releases
    responsiveness:
      grade: B
---

# {slug}

{body}
""",
        encoding="utf-8",
    )
    return path


def write_page_with_health(root: Path, rel: str, body: str, health_axes: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    slug = path.name.removesuffix(".zh.md").removesuffix(".md")
    path.write_text(
        f"""---
name: {slug}
slug: {slug}
repo: https://github.com/example/{slug}
category: {path.parent.name}
tags: [demo]
language: Python
license: MIT
maturity: active
last_verified: 2026-07-04
type: tool
upstream:
  pushed_at: 2026-07-04T00:00:00Z
  default_branch: main
  default_branch_sha: 0123456789abcdef0123456789abcdef01234567
  archived: false
health:
  schema: 1
  axes:
{health_axes}---

# {slug}

{body}
""",
        encoding="utf-8",
    )
    return path


class QualityScanTest(unittest.TestCase):
    def test_detects_generic_templates_truncation_and_zero_sha(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Other | not indexed | Use this page for its stated niche before co. |
""",
                sha=ZERO_SHA,
            )

            result = quality_scan.scan(root)
            categories = {finding.category for finding in result.findings}

            self.assertIn("generic-comparison-template", categories)
            self.assertIn("truncation-fragment", categories)
            self.assertIn("zero-placeholder-upstream-sha", categories)

    def test_detects_chinese_generic_template(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.zh.md", "当前页用于它的主场景；如果更看重别的能力，再选 Other。")

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "generic-comparison-template" and f.evidence == "当前页用于它的主场景" for f in result.findings))

    def test_truncation_detection_skips_common_word_endings_and_node_js(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Other | not indexed | Configure by hand. Run the command. Track demand. Avoid land. Do not rebrand. Uses zustand. Runtime (Node.js) is supported. |
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "truncation-fragment" for f in result.findings))

    def test_truncation_detection_keeps_sampled_row_end_fragments(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Selenium | not indexed | Browser automation with trac. |
| Node option | not indexed | JavaScript library (Node. |
| Karpathy | not indexed | Use before co. |
| Partial | not indexed | Needs per-har. |
| Flowchart | not indexed | Actively developed and. |
""",
            )

            result = quality_scan.scan(root)
            evidence = {f.evidence for f in result.findings if f.category == "truncation-fragment"}

            self.assertEqual(evidence, {"trac.", "(Node.", "before co.", "per-har.", "and."})

    def test_detects_zh_links_to_english_when_sibling_exists(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/target.md", "## Comparison\n")
            write_page(root, "categories/demo/target.zh.md", "## 横向对比\n")
            write_page(root, "categories/demo/source.zh.md", "See [Target](target.md).")

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "zh-link-to-english-sibling" and "target.zh.md" in f.message for f in result.findings))

    def test_detects_indexed_link_marked_not_indexed_in_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/target.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| [Target](target.md) | not indexed | Target is already indexed. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" for f in result.findings))

    def test_detects_chinese_indexed_link_marked_unindexed_in_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/target.zh.md", "## 横向对比\n")
            write_page(root, "categories/demo/target.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.zh.md",
                """## 横向对比

| 替代品 | 是否收录 | 我们的评价 |
|---|---|---|
| [Target](target.zh.md) | 未收录 | Target 已经收录。 |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" and "未收录" in f.evidence for f in result.findings))

    def test_counts_health_unknown_axes_by_axis_and_reason(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "## Comparison\n")

            result = quality_scan.scan(root)

            self.assertEqual(result.health_unknowns[("maintenance", "missing releases")], 1)

    def test_counts_quoted_health_unknowns_from_unknowns_block(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = write_page(root, "categories/demo/demo.md", "## Comparison\n")
            page.write_text(
                page.read_text(encoding="utf-8")
                .replace("grade: ?", 'grade: "?"')
                .replace("      reason: missing releases\n", "")
                .replace("    responsiveness:\n      grade: B", "  unknowns:\n    maintenance: { reason: no_traffic }\n    responsiveness:\n      grade: B"),
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            self.assertEqual(result.health_unknowns[("maintenance", "no_traffic")], 1)

    def test_detects_health_prose_grade_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Responsiveness**: Grade C — median first-response time 4.2 hours across 2 qualifying issues/PRs.
""",
                """    responsiveness:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-grade-drift" and "Responsiveness" in f.evidence for f in result.findings))

    def test_detects_chinese_health_prose_grade_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **响应速度**：Grade C，样本不足。
""",
                """    responsiveness:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-grade-drift" and "响应速度" in f.evidence for f in result.findings))

    def test_chinese_governance_line_with_maintainer_word_is_not_maintenance_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **治理集中度**：Grade B，若核心维护者退出，项目仍有多人维护。
""",
                """    maintenance:
      grade: A
      raw: {}
    governance:
      grade: B
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift" for f in result.findings))

    def test_matching_chinese_health_prose_grade_is_not_reported(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **维护活跃度**：Grade A，提交活跃。
""",
                """    maintenance:
      grade: A
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift" for f in result.findings))

    def test_report_labels_reviewer_only_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "## Comparison\n")

            report = quality_scan.render_report(quality_scan.scan(root), root)

            self.assertIn("## Reviewer-only dimensions", report)
            self.assertIn("not hard failures", report)
            self.assertIn("weak or non-second-person `When to use` signals", report)


if __name__ == "__main__":
    unittest.main()
