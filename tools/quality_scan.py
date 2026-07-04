#!/usr/bin/env python3
"""Report-only quality scanner for oss-atlas project pages.

This tool is intentionally separate from tools/lint.py. It catches deterministic
weak-model artifacts and audit signals, but it does not claim semantic approval.
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ZH_SUFFIX = ".zh.md"
ZERO_SHA = "0000000000000000000000000000000000000000"
GENERIC_TEMPLATES = ["Use this page for its stated niche", "当前页用于它的主场景"]
TRUNCATION_FRAGMENTS = ["trac.", "(Node.", "and.", "per-har.", "before co."]
KNOWN_CATEGORIES = [
    "generic-comparison-template",
    "health-prose-grade-drift",
    "health-prose-raw-drift",
    "indexed-page-marked-not-indexed",
    "truncation-fragment",
    "zero-placeholder-upstream-sha",
    "zh-link-to-english-sibling",
]
NOT_INDEXED_MARKERS = ["not indexed", "未收录"]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEALTH_AXES = ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]
AXIS_LABELS = {
    "maintenance": ["Maintenance", "维护活跃度"],
    "responsiveness": ["Responsiveness", "响应速度", "响应性"],
    "adoption": ["Adoption", "采用广度", "采用度"],
    "longevity": ["Longevity", "长青度"],
    "governance": ["Governance", "Bus factor", "Bus Factor", "治理集中度", "维护者分散度"],
    "risk_license": ["Risk", "License", "Risk/License", "许可宽松度", "许可证风险"],
}
RAW_NUMERIC_FIELDS = {
    "responsiveness": ["median_ttfr_hours", "qualifying_issues"],
    "adoption": ["downloads_last_month", "dependent_repos_count"],
    "longevity": ["repo_age_days", "last_commit_age_days"],
    "governance": ["top3_share", "top1_share", "active_maintainers_12mo"],
}
RAW_FIELD_TRIGGERS = {
    "median_ttfr_hours": ["median", "first-response", "首次响应", "中位"],
    "qualifying_issues": ["qualifying", "issues/PRs", "issue/PR"],
    "downloads_last_month": ["download", "downloads", "下载量"],
    "dependent_repos_count": ["dependent", "dependents", "dependent repos", "依赖仓库"],
    "repo_age_days": ["days old", "repo age", "created", "创建", "已创建"],
    "last_commit_age_days": ["last commit", "last pushed", "最后提交", "最后 push", "最近推送"],
    "top3_share": ["top-3", "top3", "前三"],
    "top1_share": ["top-1", "top1", "第一贡献者"],
    "active_maintainers_12mo": ["active maintainer", "active maintainers", "活跃维护者"],
}


@dataclass(frozen=True)
class Finding:
    category: str
    severity: str
    path: str
    line: int
    message: str
    evidence: str


@dataclass
class ScanResult:
    findings: list[Finding]
    health_unknowns: Counter[tuple[str, str]]
    project_page_count: int
    english_canonical_page_count: int


def is_project_page(path: Path) -> bool:
    return path.suffix == ".md" and path.name not in {"INDEX.md", "INDEX.zh.md"}


def project_pages(root: Path) -> list[Path]:
    categories = root / "categories"
    if not categories.exists():
        return []
    return sorted(path for path in categories.rglob("*.md") if is_project_page(path))


def relpath(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def body_start(text: str) -> int:
    if not text.startswith("---"):
        return 0
    end = text.find("\n---", 3)
    return end + 4 if end != -1 else 0


def base_slug(name: str) -> str:
    return name[: -len(ZH_SUFFIX)] if name.endswith(ZH_SUFFIX) else name[: -len(".md")]


def canonical_target(path: Path) -> Path:
    if path.name.endswith(ZH_SUFFIX):
        return path.with_name(f"{base_slug(path.name)}.md").resolve()
    return path.resolve()


def slugify_label(label: str) -> str:
    plain = re.sub(r"`([^`]+)`", r"\1", label).strip()
    plain = re.sub(r"\[[^\]]+\]\([^)]+\)", "", plain).strip()
    plain = plain.split("/", 1)[0].strip()
    plain = re.sub(r"\([^)]*\)", "", plain).strip()
    plain = plain.replace("（", " ").replace("）", " ")
    plain = plain.lower().replace("_", "-")
    plain = re.sub(r"[^a-z0-9]+", "-", plain).strip("-")
    return plain


def resolve_markdown_target(source: Path, href: str) -> Path | None:
    target = href.split("#", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if not target.endswith(".md"):
        return None
    return (source.parent / target).resolve()


def table_cells(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [cell.strip() for cell in body.split("|")]


def is_table_separator(line: str) -> bool:
    cells = table_cells(line)
    return bool(cells) and all(cell and set(cell) <= set("-: ") and cell.count("-") >= 3 for cell in cells)


def section_lines(text: str, heading: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() != heading:
            continue
        end = next((j for j in range(i + 1, len(lines)) if re.match(r"^##[ \t]+\S", lines[j])), len(lines))
        return [(j + 1, lines[j]) for j in range(i + 1, end)]
    return []


def is_boundary(text: str, index: int) -> bool:
    return index < 0 or index >= len(text) or not text[index].isalnum()


def truncation_fragments_in_line(line: str) -> list[str]:
    hits: list[str] = []
    for fragment in TRUNCATION_FRAGMENTS:
        start = 0
        while True:
            offset = line.find(fragment, start)
            if offset == -1:
                break
            before = offset - 1
            after = offset + len(fragment)
            if is_boundary(line, before) and is_boundary(line, after):
                hits.append(fragment)
            start = offset + len(fragment)
    return hits


def unknown_health_axes(text: str) -> Counter[tuple[str, str]]:
    counts: Counter[tuple[str, str]] = Counter()
    lines = text.splitlines()
    unknown_reasons: dict[str, str] = {}
    for i, line in enumerate(lines):
        if line.strip() != "unknowns:":
            continue
        section_end = next((j for j in range(i + 1, len(lines)) if lines[j] and not lines[j].startswith("    ")), len(lines))
        for entry in lines[i + 1 : section_end]:
            stripped = entry.strip()
            match = re.match(r"([a-z_]+):\s*\{\s*reason:\s*([^}]+?)\s*\}", stripped)
            if match:
                unknown_reasons[match.group(1)] = match.group(2).strip().strip('"\'') or "(missing_reason)"
    for i, line in enumerate(lines):
        stripped = line.strip()
        axis = stripped[:-1] if stripped.endswith(":") else ""
        if axis not in HEALTH_AXES:
            continue
        section_end = next(
            (
                j
                for j in range(i + 1, len(lines))
                if lines[j].startswith("    ") and not lines[j].startswith("      ") and lines[j].strip().endswith(":")
            ),
            len(lines),
        )
        block = [line.strip() for line in lines[i + 1 : section_end]]
        if not any(re.fullmatch(r"grade:\s*[\"']?\?[\"']?", entry) for entry in block):
            continue
        reason_line = next((entry for entry in block if entry.startswith("reason:")), "")
        reason = reason_line.partition(":")[2].strip() if reason_line else unknown_reasons.get(axis, "(missing_reason)")
        counts[(axis, reason or "(missing_reason)")] += 1
    return counts


def health_axis_grades(text: str) -> dict[str, str]:
    grades: dict[str, str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        axis = stripped[:-1] if stripped.endswith(":") else ""
        if axis not in HEALTH_AXES:
            continue
        section_end = next(
            (
                j
                for j in range(i + 1, len(lines))
                if lines[j].startswith("    ") and not lines[j].startswith("      ") and lines[j].strip().endswith(":")
            ),
            len(lines),
        )
        for entry in lines[i + 1 : section_end]:
            match = re.search(r"grade:\s*[\"']?([A-E?])[\"']?", entry.strip())
            if match:
                grades[axis] = match.group(1)
                break
    return grades


def yaml_scalar(raw: str) -> str:
    return raw.strip().strip('"\'')


def health_axis_raw_values(text: str) -> dict[tuple[str, str], str]:
    values: dict[tuple[str, str], str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        axis = stripped[:-1] if stripped.endswith(":") else ""
        if axis not in HEALTH_AXES:
            continue
        section_end = next(
            (
                j
                for j in range(i + 1, len(lines))
                if lines[j].startswith("    ") and not lines[j].startswith("      ") and lines[j].strip().endswith(":")
            ),
            len(lines),
        )
        raw_fields = set(RAW_NUMERIC_FIELDS.get(axis, []))
        for entry in lines[i + 1 : section_end]:
            match = re.match(r"\s*([a-z_]+):\s*([-+]?[0-9][0-9.,]*)\s*$", entry)
            if match and match.group(1) in raw_fields:
                values[(axis, match.group(1))] = yaml_scalar(match.group(2))
    return values


def health_section_heading(page: Path) -> str:
    return "## 健康度与可持续性" if page.name.endswith(ZH_SUFFIX) else "## Health & viability"


def detect_health_prose_grade_drift(page: Path, text: str, root: Path) -> list[Finding]:
    grades = health_axis_grades(text)
    if not grades:
        return []
    findings: list[Finding] = []
    heading = health_section_heading(page)
    for line_no, line in section_lines(text, heading):
        prose_grade = re.search(r"\bGrade\s+([A-E?])\b", line)
        if not prose_grade:
            continue
        for axis, labels in AXIS_LABELS.items():
            if any(label in line for label in labels):
                frontmatter_grade = grades.get(axis)
                if frontmatter_grade and frontmatter_grade != prose_grade.group(1):
                    findings.append(
                        Finding(
                            "health-prose-grade-drift",
                            "high",
                            relpath(page, root),
                            line_no,
                            f"Health prose Grade {prose_grade.group(1)} disagrees with frontmatter {axis} grade {frontmatter_grade}.",
                            line.strip(),
                        )
                    )
                break
    return findings


def numeric_variants(value: str) -> set[str]:
    normalized = value.replace(",", "")
    variants = {value, normalized}
    try:
        number = float(normalized)
    except ValueError:
        return variants
    variants.add(f"{number:.1f}")
    if number.is_integer():
        variants.add(str(int(number)))
        variants.add(f"{int(number):,}")
    return variants


def extract_numbers(line: str) -> set[str]:
    return {match.group(0) for match in re.finditer(r"(?<![A-Za-z])\d[\d,]*(?:\.\d+)?", line)}


def line_mentions_raw_field(line: str, field: str) -> bool:
    lowered = line.lower()
    return any(trigger.lower() in lowered for trigger in RAW_FIELD_TRIGGERS.get(field, []))


def detect_health_prose_raw_drift(page: Path, text: str, root: Path) -> list[Finding]:
    raw_values = health_axis_raw_values(text)
    if not raw_values:
        return []
    findings: list[Finding] = []
    heading = health_section_heading(page)
    for line_no, line in section_lines(text, heading):
        prose_numbers = extract_numbers(line)
        if not prose_numbers:
            continue
        for axis, labels in AXIS_LABELS.items():
            if not any(label in line for label in labels):
                continue
            for field in RAW_NUMERIC_FIELDS.get(axis, []):
                if not line_mentions_raw_field(line, field):
                    continue
                frontmatter_value = raw_values.get((axis, field))
                if not frontmatter_value:
                    continue
                if prose_numbers & numeric_variants(frontmatter_value):
                    continue
                findings.append(
                    Finding(
                        "health-prose-raw-drift",
                        "high",
                        relpath(page, root),
                        line_no,
                        f"Health prose numeric values do not include frontmatter {axis}.{field}={frontmatter_value}.",
                        line.strip(),
                    )
                )
                break
            break
    return findings


def scan(root: Path | str) -> ScanResult:
    root = Path(root).resolve()
    pages = project_pages(root)
    indexed_targets = {canonical_target(page) for page in pages}
    english_canonical_page_count = sum(1 for page in pages if not page.name.endswith(ZH_SUFFIX))
    findings: list[Finding] = []
    health_unknowns: Counter[tuple[str, str]] = Counter()

    for page in pages:
        text = page.read_text(encoding="utf-8")
        rel = relpath(page, root)
        body = text[body_start(text) :]

        for template in GENERIC_TEMPLATES:
            offset = text.find(template)
            if offset != -1:
                findings.append(
                    Finding("generic-comparison-template", "high", rel, line_number(text, offset), "Generic comparison template prose found.", template)
                )

        offset = text.find(f"default_branch_sha: {ZERO_SHA}")
        if offset != -1:
            findings.append(
                Finding("zero-placeholder-upstream-sha", "medium", rel, line_number(text, offset), "Placeholder zero upstream SHA found.", ZERO_SHA)
            )

        health_unknowns.update(unknown_health_axes(text))
        findings.extend(detect_health_prose_grade_drift(page, text, root))
        findings.extend(detect_health_prose_raw_drift(page, text, root))

        if page.name.endswith(ZH_SUFFIX):
            for match in LINK_RE.finditer(body):
                target = resolve_markdown_target(page, match.group(2))
                if target is None or target.name.endswith(ZH_SUFFIX):
                    continue
                zh_target = target.with_name(f"{base_slug(target.name)}.zh.md")
                if zh_target.exists():
                    findings.append(
                        Finding(
                            "zh-link-to-english-sibling",
                            "medium",
                            rel,
                            line_number(body, match.start()) + line_number(text, body_start(text)) - 1,
                            f"Chinese page links to English target while {zh_target.name} exists.",
                            match.group(0),
                        )
                    )

        heading = "## 横向对比" if page.name.endswith(ZH_SUFFIX) else "## Comparison"
        for line_no, line in section_lines(text, heading):
            if not line.strip().startswith("|") or is_table_separator(line):
                continue
            cells = table_cells(line)
            for fragment in truncation_fragments_in_line(line):
                findings.append(
                    Finding(
                        "truncation-fragment",
                        "high",
                        rel,
                        line_no,
                        "High-confidence truncation fragment found in a comparison row.",
                        fragment,
                    )
                )
            if not any(marker in line for marker in NOT_INDEXED_MARKERS):
                continue
            linked_indexed_targets = [
                target for _label, href in LINK_RE.findall(line) if (target := resolve_markdown_target(page, href)) and canonical_target(target) in indexed_targets
            ]
            indexed_plain_target = False
            if len(cells) >= 2 and not LINK_RE.search(cells[0]):
                candidate_slug = slugify_label(cells[0])
                if candidate_slug:
                    sibling = page.with_name(f"{candidate_slug}.md").resolve()
                    indexed_plain_target = sibling in indexed_targets
            if linked_indexed_targets or indexed_plain_target:
                findings.append(
                    Finding(
                        "indexed-page-marked-not-indexed",
                        "high",
                        rel,
                        line_no,
                        "Comparison row marks a linked existing indexed page as not indexed.",
                        line.strip(),
                    )
                )

    return ScanResult(
        findings=sorted(findings, key=lambda f: (f.severity, f.category, f.path, f.line, f.evidence)),
        health_unknowns=health_unknowns,
        project_page_count=len(pages),
        english_canonical_page_count=english_canonical_page_count,
    )


def render_report(result: ScanResult, root: Path | str) -> str:
    root = Path(root).resolve()
    severity_counts = Counter(f.severity for f in result.findings)
    category_counts = Counter(f.category for f in result.findings)
    zero_sha_count = category_counts.get("zero-placeholder-upstream-sha", 0)
    zero_sha_english_count = sum(1 for f in result.findings if f.category == "zero-placeholder-upstream-sha" and not f.path.endswith(ZH_SUFFIX))
    lines = [
        "# oss-atlas quality scan report",
        "",
        "Mode: report-only. Deterministic findings are triage signals, not full semantic approval.",
        "Count scope: deterministic finding counts are page-level over English canonical pages plus Chinese mirrors unless explicitly labeled otherwise.",
        "Truncation fragments are high-confidence only: comparison-row hits with non-alphanumeric boundaries around the sampled fragment.",
        f"Root: `{root}`",
        f"Project pages scanned: {result.project_page_count}",
        f"English canonical pages scanned: {result.english_canonical_page_count}",
        "",
        "## Summary counts",
        "",
        "### By severity",
        "",
    ]
    for severity in ("high", "medium", "low"):
        lines.append(f"- {severity}: {severity_counts.get(severity, 0)}")
    lines += ["", "### By category", ""]
    for category in KNOWN_CATEGORIES:
        lines.append(f"- {category}: {category_counts[category]}")
    lines += [
        "",
        f"Zero placeholder upstream SHA count (page-level): {zero_sha_count}",
        f"Zero placeholder upstream SHA count (English canonical): {zero_sha_english_count}",
        "",
        "## Deterministic findings",
        "",
    ]
    if not result.findings:
        lines.append("No deterministic findings.")
    else:
        for finding in result.findings:
            lines.append(f"- [{finding.severity}] `{finding.category}` {finding.path}:{finding.line} — {finding.message} Evidence: `{finding.evidence}`")
    lines += [
        "",
        "## Health ? distribution",
        "",
        "Count scope: page-level over English canonical pages plus Chinese mirrors; divide by mirror parity only after confirming frontmatter parity.",
        "",
        "| Axis | Reason | Page-level count |",
        "|---|---|---:|",
    ]
    if result.health_unknowns:
        for (axis, reason), count in sorted(result.health_unknowns.items()):
            lines.append(f"| {axis} | {reason} | {count} |")
    else:
        lines.append("| (none) | (none) | 0 |")
    lines += [
        "",
        "## Reviewer-only dimensions",
        "",
        "These dimensions are not hard failures and are not scanner approval. A reviewer must still inspect them semantically:",
        "",
        "- reviewer-only: weak or non-second-person `When to use` signals.",
        "- reviewer-only: `Comparison` rows lacking an obvious decisive tradeoff.",
        "- reviewer-only: Caveats sections that may be too thin for inferred or unverified prose.",
        "- reviewer-only: Chinese monolingual mirror quality beyond link targets.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report deterministic oss-atlas quality signals.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    parser.add_argument("--report", help="Optional Markdown report path to write.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report = render_report(scan(root), root)
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
