#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import health_audit


def page(axes: dict[str, str], unknowns: dict[str, str]) -> str:
    axis_lines = []
    for name in health_audit.AXES:
        grade = axes.get(name, "A")
        axis_lines.append(f"    {name}:")
        axis_lines.append(f'      grade: {grade if grade != "?" else chr(34) + "?" + chr(34)}')
        axis_lines.append("      raw: {}")
    unknown_lines = []
    if unknowns:
        unknown_lines.append("  unknowns:")
        for axis, reason in unknowns.items():
            unknown_lines.append(f"    {axis}: {{ reason: {reason} }}")
    body = "\n".join(axis_lines + unknown_lines)
    return f"""---
name: Demo
slug: demo
health:
  schema: 1
  computed_at: 2026-07-01T00:00:00Z
  overall: A
  axes:
{body}
---

# Demo
"""


class HealthAuditTest(unittest.TestCase):
    def run_audit(self, pages: dict[str, str]) -> dict:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            cat = root / "categories" / "demo"
            cat.mkdir(parents=True)
            for name, text in pages.items():
                (cat / name).write_text(text, encoding="utf-8")
            return health_audit.audit(root)

    def test_structural_reason_is_not_flagged(self) -> None:
        result = self.run_audit({"a.md": page({"adoption": "?"}, {"adoption": "no_package_structural"})})
        self.assertEqual(result["unknown_axes"], 1)
        self.assertEqual(result["distribution"][0]["bucket"], "structural")
        self.assertFalse(any(result["flagged"].values()))

    def test_transient_reason_is_flagged_for_rerun(self) -> None:
        result = self.run_audit({"a.md": page({"risk_license": "?"}, {"risk_license": "repo_unreachable"})})
        self.assertEqual(result["flagged"]["transient"][0]["reason"], "repo_unreachable")

    def test_human_judgment_reason_is_needs_review(self) -> None:
        result = self.run_audit({"a.md": page({"risk_license": "?"}, {"risk_license": "license_unparsed"})})
        self.assertEqual(result["flagged"]["needs_review"][0]["reason"], "license_unparsed")

    def test_undocumented_reason_is_enum_drift(self) -> None:
        result = self.run_audit({"a.md": page({"risk_license": "?"}, {"risk_license": "custom_modified_license"})})
        drift = result["flagged"]["enum_drift"]
        self.assertEqual(len(drift), 1)
        self.assertEqual(drift[0]["reason"], "custom_modified_license")

    def test_reason_on_wrong_axis_is_enum_drift(self) -> None:
        result = self.run_audit({"a.md": page({"adoption": "?"}, {"adoption": "no_traffic"})})
        self.assertEqual(len(result["flagged"]["enum_drift"]), 1)

    def test_missing_reason_is_flagged(self) -> None:
        result = self.run_audit({"a.md": page({"governance": "?"}, {})})
        self.assertEqual(result["flagged"]["missing_reason"], [{"page": "categories/demo/a.md", "axis": "governance"}])

    def test_zh_and_index_files_are_skipped(self) -> None:
        result = self.run_audit({
            "a.md": page({}, {}),
            "a.zh.md": page({"adoption": "?"}, {"adoption": "no_package_structural"}),
            "INDEX.md": "# demo\n",
        })
        self.assertEqual(result["pages_scanned"], 1)
        self.assertEqual(result["unknown_axes"], 0)

    def test_page_without_health_block_is_reported_not_silently_skipped(self) -> None:
        result = self.run_audit({"a.md": "---\nname: Demo\n---\n\n# Demo\n"})
        self.assertEqual(result["pages_unparsed"], ["categories/demo/a.md"])


if __name__ == "__main__":
    unittest.main()
