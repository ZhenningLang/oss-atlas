#!/usr/bin/env python3
"""Reusable scoped quality verifier for oss-atlas content batches."""
from __future__ import annotations

import argparse
import subprocess
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import quality_scan


GATED_CATEGORIES = set(quality_scan.GATED_DETERMINISTIC_CATEGORIES)


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def run_command(command: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def write_scan_report(root: Path, scopes: list[str], report_path: Path) -> tuple[quality_scan.ScanResult, Path]:
    result = quality_scan.scan(root, scope_paths=scopes)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(quality_scan.render_report(result, root), encoding="utf-8")
    return result, report_path


def gated_finding_counts(result: quality_scan.ScanResult) -> Counter[str]:
    return Counter(finding.category for finding in result.findings if finding.category in GATED_CATEGORIES)


def scan_check(result: quality_scan.ScanResult) -> CheckResult:
    counts = gated_finding_counts(result)
    if not counts:
        return CheckResult("Scan gated findings", True, "0 gated deterministic findings")
    rendered = ", ".join(f"{category}={count}" for category, count in sorted(counts.items()))
    total = sum(counts.values())
    return CheckResult("Scan gated findings", False, f"{total} gated deterministic findings: {rendered}")


def diff_check(root: Path, scopes: list[str]) -> CheckResult:
    completed = run_command(["git", "diff", "--check", "--", *scopes], cwd=root)
    if completed.returncode == 0:
        return CheckResult("Diff check", True, "git diff --check passed")
    output = (completed.stdout + completed.stderr).strip()
    detail = output if output else f"git diff --check exited {completed.returncode}"
    return CheckResult("Diff check", False, detail)


def make_check(root: Path, target: str) -> CheckResult:
    completed = run_command(["make", target], cwd=root)
    name = f"make {target}"
    if completed.returncode == 0:
        return CheckResult(name, True, "passed")
    output = (completed.stdout + completed.stderr).strip()
    detail = output if output else f"exited {completed.returncode}"
    return CheckResult(name, False, detail)


def render_summary(report_path: Path, checks: list[CheckResult]) -> str:
    lines = ["# Quality batch verification", "", f"Report: {report_path}", ""]
    for check in checks:
        status = "PASS" if check.ok else "FAIL"
        lines.append(f"{check.name}: {status} - {check.detail}")
    final = "PASS" if all(check.ok for check in checks) else "FAIL"
    lines.extend(["", f"Final: {final}"])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a scoped oss-atlas quality batch.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--scope", action="append", required=True, help="Project page file or directory to verify. Repeatable.")
    parser.add_argument("--report", required=True, help="Markdown quality scan report path to write.")
    parser.add_argument("--full", action="store_true", help="Also run make test and make lint from the repo root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report_path = Path(args.report)
    result, written_report = write_scan_report(root, args.scope, report_path)

    checks = [scan_check(result), diff_check(root, args.scope)]
    if args.full:
        checks.extend([make_check(root, "test"), make_check(root, "lint")])

    print(render_summary(written_report, checks))
    return 0 if all(check.ok for check in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
