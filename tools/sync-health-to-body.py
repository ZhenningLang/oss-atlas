#!/usr/bin/env python3
"""Sync health frontmatter data to the body 'Health & viability' section.

Reads the health block from YAML frontmatter and rewrites the corresponding
prose section in the body so they never drift.  Preserves the Caveats section."""
import argparse, re, yaml
from pathlib import Path


def parse_frontmatter(text):
    """Return (frontmatter_dict, body_text) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    try:
        fm = yaml.safe_load(text[3:end])
    except Exception:
        return None, text
    return fm or {}, text[end + 4:]


def axis_bullet_en(name, axis):
    """Generate an English health bullet from axis data."""
    grade = axis.get("grade", "?")
    raw = axis.get("raw", {}) or {}
    inferred = raw.get("inferred", False)
    source = raw.get("source", "")
    
    labels = {
        "maintenance": "Maintenance",
        "responsiveness": "Responsiveness",
        "adoption": "Adoption",
        "longevity": "Longevity",
        "governance": "Governance",
        "risk_license": "Risk / License",
    }
    label = labels.get(name, name)
    
    if grade == "?":
        reason = axis.get("reason", "unknown")
        return f"- **{label}**: Cannot be scored — {reason}."
    
    if name == "maintenance":
        active = raw.get("active_weeks_13", "?")
        last = raw.get("last_commit_age_days", "?")
        return f"- **{label}**: Grade {grade} — {active}/13 active weeks in trailing 13; last commit {last} days ago."
    
    if name == "responsiveness":
        median = raw.get("median_ttfr_hours")
        qualifying = raw.get("qualifying_issues")
        if median is not None and qualifying is not None:
            return f"- **{label}**: Grade {grade} — median first-response time {median} hours across {qualifying} qualifying issues/PRs."
        elif inferred or source == "inferred":
            return f"- **{label}**: Grade {grade} — inferred from maintenance activity (no direct issue/PR response data)."
        else:
            return f"- **{label}**: Grade {grade}."
    
    if name == "adoption":
        registry = raw.get("registry", "?")
        pkg = raw.get("canonical_package", "?")
        downloads = raw.get("downloads_last_month")
        stars = raw.get("stars")
        if downloads is not None:
            return f"- **{label}**: Grade {grade} — {downloads:,} monthly downloads via {registry} (package: {pkg})."
        elif stars is not None:
            return f"- **{label}**: Grade {grade} — {stars:,} GitHub stars."
        else:
            return f"- **{label}**: Grade {grade}."
    
    if name == "longevity":
        age = raw.get("repo_age_days", "?")
        return f"- **{label}**: Grade {grade} — {age} days old."
    
    if name == "governance":
        owner = raw.get("owner_type", "?")
        top3 = raw.get("top3_share")
        if top3 is not None:
            return f"- **{label}**: Grade {grade} — top-3 contributor share {top3:.1%} ({owner})."
        else:
            return f"- **{label}**: Grade {grade} ({owner})."
    
    if name == "risk_license":
        spdx = raw.get("spdx_id", "?")
        return f"- **{label}**: Grade {grade} — {spdx} license."
    
    return f"- **{label}**: Grade {grade}."


def axis_bullet_zh(name, axis):
    """Generate a Chinese health bullet from axis data."""
    grade = axis.get("grade", "?")
    raw = axis.get("raw", {}) or {}
    inferred = raw.get("inferred", False)
    source = raw.get("source", "")
    
    labels = {
        "maintenance": "维护活跃度",
        "responsiveness": "响应速度",
        "adoption": "采用广度",
        "longevity": "长青度",
        "governance": "治理集中度",
        "risk_license": "许可风险",
    }
    label = labels.get(name, name)
    
    if grade == "?":
        reason = axis.get("reason", "unknown")
        return f"- **{label}**：无法计算——{reason}。"
    
    if name == "maintenance":
        active = raw.get("active_weeks_13", "?")
        last = raw.get("last_commit_age_days", "?")
        return f"- **{label}**：Grade {grade}——最近 13 周中 {active} 周有提交；最后提交距今 {last} 天。"
    
    if name == "responsiveness":
        median = raw.get("median_ttfr_hours")
        qualifying = raw.get("qualifying_issues")
        if median is not None and qualifying is not None:
            return f"- **{label}**：Grade {grade}——中位首次响应时间 {median} 小时，基于 {qualifying} 个 qualifying issues/PRs。"
        elif inferred or source == "inferred":
            return f"- **{label}**：Grade {grade}——基于维护活跃度推断（无直接 issue/PR 响应数据）。"
        else:
            return f"- **{label}**：Grade {grade}。"
    
    if name == "adoption":
        registry = raw.get("registry", "?")
        pkg = raw.get("canonical_package", "?")
        downloads = raw.get("downloads_last_month")
        stars = raw.get("stars")
        if downloads is not None:
            return f"- **{label}**：Grade {grade}——{registry} 上月下载量 {downloads:,}（包名：{pkg}）。"
        elif stars is not None:
            return f"- **{label}**：Grade {grade}——GitHub {stars:,} 星。"
        else:
            return f"- **{label}**：Grade {grade}。"
    
    if name == "longevity":
        age = raw.get("repo_age_days", "?")
        return f"- **{label}**：Grade {grade}——仓库已创建 {age} 天。"
    
    if name == "governance":
        owner = raw.get("owner_type", "?")
        top3 = raw.get("top3_share")
        if top3 is not None:
            return f"- **{label}**：Grade {grade}——前三贡献者占比 {top3:.1%}（{owner}）。"
        else:
            return f"- **{label}**：Grade {grade}（{owner}）。"
    
    if name == "risk_license":
        spdx = raw.get("spdx_id", "?")
        return f"- **{label}**：Grade {grade}——{spdx} 许可证。"
    
    return f"- **{label}**：Grade {grade}。"


def sync_page(path):
    """Sync health data for a single page.  Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if not fm or "health" not in fm:
        return False

    health = fm["health"]
    axes = health.get("axes", {})
    is_zh = path.name.endswith(".zh.md")
    
    # Build the new health section bullets
    bullets = []
    for axis_name in ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]:
        axis_data = axes.get(axis_name, {})
        if is_zh:
            bullets.append(axis_bullet_zh(axis_name, axis_data))
        else:
            bullets.append(axis_bullet_en(axis_name, axis_data))
    
    health_section = "\n".join(bullets) + "\n"
    
    # Replace only the Health & viability section, preserving Caveats
    if is_zh:
        header = "## 健康度与可持续性\n"
        next_header = "## 存疑（未验证）"
    else:
        header = "## Health & viability\n"
        next_header = "## Caveats (unverified)"
    
    # Match header + content until next header (but not including it)
    pattern = f'({re.escape(header)})((?:(?!{re.escape(next_header)}).)*)'
    match = re.search(pattern, body, re.DOTALL)
    if not match:
        return False
    
    new_body = body[:match.start()] + match.group(1) + health_section + body[match.end():]
    
    # Reconstruct full text with original frontmatter
    new_text = text[:len(text) - len(body)] + new_body
    
    if new_text == text:
        return False
    
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser(description="Sync health frontmatter to body prose")
    ap.add_argument("--all", action="store_true", help="sync all pages in categories/")
    ap.add_argument("--page", help="sync a single page path")
    args = ap.parse_args()

    if args.page:
        changed = sync_page(Path(args.page))
        print(f"{'synced' if changed else 'no change'}: {args.page}")
        return 0

    if args.all:
        pages = list(Path("categories").rglob("*.md"))
        changed = 0
        for p in pages:
            if p.name.endswith("INDEX.md"):
                continue
            if sync_page(p):
                changed += 1
                print(f"synced: {p}")
        print(f"\n{changed}/{len(pages)} pages synced")
        return 0

    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
