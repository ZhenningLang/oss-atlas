#!/usr/bin/env python3
"""Apply a verified project-intake queue into first-pass oss-atlas pages.

This is an operational helper for the 2026-07-06 intake wave. It deliberately
does not compute health grades; run tools/health_backfill.py after page creation.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today().isoformat()


CATEGORY_TAGS = {
    "agent-runtimes": ["llm-agent", "agent-runtime"],
    "workflow-builders": ["llm-workflow", "agent-builder"],
    "coding-agents": ["coding-agent", "developer-tool"],
    "agent-memory": ["agent-memory", "knowledge-graph"],
    "llm-eval": ["llm-eval", "testing"],
    "llm-training": ["llm-training", "fine-tuning"],
    "llm-inference": ["llm-inference", "serving"],
    "web-ui": ["frontend", "ui"],
    "web-automation": ["browser-automation", "testing"],
    "workflow-orchestration": ["workflow", "orchestration"],
    "document-parsing": ["document-parsing", "pdf"],
    "pdf-tools": ["pdf", "document"],
    "markdown-tools": ["markdown", "document"],
    "databases": ["database", "data"],
    "observability": ["observability", "monitoring"],
    "auth": ["auth", "authorization"],
    "rag-retrieval": ["rag", "retrieval"],
}


def run_json(cmd: list[str], timeout: int = 30) -> dict:
    out = subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.STDOUT, timeout=timeout)
    return json.loads(out)


def owner_repo(url: str) -> str:
    m = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        raise ValueError(f"not a GitHub repo URL: {url}")
    return f"{m.group(1)}/{m.group(2).removesuffix('.git')}"


def branch_sha(repo_url: str, branch: str) -> str:
    data = run_json(["gh", "api", f"repos/{owner_repo(repo_url)}/branches/{branch}"], timeout=30)
    return data["commit"]["sha"]


def rel_health(page_dir: Path, slug: str, zh: bool) -> str:
    card = f"{slug}.zh.svg" if zh else f"{slug}.svg"
    return os.path.relpath(ROOT / "assets" / "health" / card, start=page_dir)


def esc(s: object) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def slug_tag(slug: str) -> str:
    return slug.replace("-", "_") if slug and slug[0].isdigit() else slug


def tags_for(item: dict) -> list[str]:
    leaf = Path(item["category_path"]).name
    tags = list(CATEGORY_TAGS.get(leaf, [leaf]))
    tags.append(slug_tag(item["slug"]))
    tags.append(item["type"])
    out = []
    for tag in tags:
        tag = re.sub(r"[^a-z0-9_-]+", "-", tag.lower()).strip("-")
        if tag and tag not in out:
            out.append(tag)
    return out[:8]


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            fm[key.strip()] = [x.strip() for x in raw[1:-1].split(",") if x.strip()]
        else:
            fm[key.strip()] = raw.strip('"\'')
    return fm


def existing_pages(cat_dir: Path, exclude_slug: str) -> list[tuple[str, str, str, str]]:
    pages = []
    for page in sorted(cat_dir.glob("*.md")):
        if page.name.startswith("INDEX") or page.name.endswith(".zh.md") or page.stem == exclude_slug:
            continue
        try:
            fm = parse_frontmatter(page)
        except Exception:
            continue
        name = fm.get("name", page.stem)
        health = "? (0/6)"
        if fm.get("health"):
            health = "? (0/6)"
        pages.append((name, page.name, page.with_name(page.stem + ".zh.md").name, health))
    return pages[:4]


def frontmatter(item: dict, sha: str) -> str:
    gh = item["github"]
    license_id = gh.get("license") or "NOASSERTION"
    state = "archived" if gh.get("archived") else "active"
    stars = gh.get("stars") or 0
    maturity = f"{state}, ~{stars:,} stars (as of 2026-07)"
    tags = ", ".join(tags_for(item))
    return f"""---
name: {item['name']}
slug: {item['slug']}
repo: {gh.get('html_url') or item['repo']}
category: {Path(item['category_path']).name}
tags: [{tags}]
language: {gh.get('language') or 'Unknown'}
license: {license_id}
maturity: {maturity}
last_verified: {TODAY}
type: {item['type']}
upstream:
  pushed_at: {gh.get('pushed_at')}
  default_branch: {gh.get('default_branch')}
  default_branch_sha: {sha}
  archived: {str(bool(gh.get('archived'))).lower()}
---
"""


def comparison_en(item: dict, cat_dir: Path) -> str:
    rows = ["| Alternative | In index | Our verdict | Tradeoff |", "|---|---|---|---|"]
    for name, en, _zh, _health in existing_pages(cat_dir, item["slug"]):
        rows.append(f"| [{name}]({en}) | ✅ | When you need the established in-index option for this category, compare it against {item['name']} before switching. | {item['name']} is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose {item['name']} only after verifying the repo-specific caveats below. |")
    if len(rows) == 2:
        rows.append(f"| Adjacent projects in this category | 未收录 | Use {item['name']} only after checking whether a narrower in-index page already covers the task. | This first-pass page records the project as a selectable repo, but the surrounding comparison set still needs semantic review. |")
    rows.append("| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |")
    return "\n".join(rows)


def comparison_zh(item: dict, cat_dir: Path) -> str:
    rows = ["| 替代品 | 是否收录 | 我们的评价 | 取舍 |", "|---|---|---|---|"]
    for name, _en, zh, _health in existing_pages(cat_dir, item["slug"]):
        rows.append(f"| [{name}]({zh}) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 {item['name']} 对照。 | {item['name']} 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |")
    if len(rows) == 2:
        rows.append(f"| 本分类相邻项目 | 未收录 | 只有在确认没有更窄的已收录页面覆盖任务时，才选择 {item['name']}。 | 这个首版页面先把仓库纳入可选集合，但周边对比关系仍需要后续语义复核。 |")
    rows.append(f"| 自写集成 | 未收录 | 只有需求很小、维护成本明确低于引入 {item['name']} 时，才自写。 | 自写能少一个依赖，但会失去上游项目、生态和本页记录的选型取舍。 |")
    return "\n".join(rows)


def caveats_en(item: dict) -> str:
    reasons = item.get("reasons") or []
    bullets = ["- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes."]
    if "license_missing_or_noassertion" in reasons:
        bullets.append("- [未验证] GitHub API returned no SPDX license or NOASSERTION; inspect the repository license files before commercial or redistribution use.")
    if "github_repo_archived" in reasons:
        bullets.append("- [未验证] GitHub marks this repository archived; treat it as a pattern or legacy option unless a maintained successor is confirmed.")
    if "split_mixed_candidate_review_needed" in reasons:
        bullets.append("- [推断] The backlog item was mixed; this page records the verified repository URL only, not every adjacent project implied by the original label.")
    bullets.append("- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.")
    return "\n".join(bullets)


def caveats_zh(item: dict) -> str:
    reasons = item.get("reasons") or []
    bullets = ["- [未验证] 这是依据 GitHub 元数据和 2026-07-06 backlog 生成的首版 intake 页面；高风险选型前，请重新阅读上游 README、文档、许可证文件和 release notes。"]
    if "license_missing_or_noassertion" in reasons:
        bullets.append("- [未验证] GitHub API 没有返回 SPDX license，或返回 NOASSERTION；商用或再分发前必须检查仓库内许可证文件。")
    if "github_repo_archived" in reasons:
        bullets.append("- [未验证] GitHub 将该仓库标为 archived；除非确认有维护中的继任项目，否则只应当作模式参考或遗留选项。")
    if "split_mixed_candidate_review_needed" in reasons:
        bullets.append("- [推断] backlog 原项是混合候选；本页只记录已核验的具体仓库 URL，不代表原标签暗含的所有相邻项目。")
    bullets.append("- [推断] 横向对比表先使用同分类已收录页面作为起点；后续语义复核应把泛化邻居替换成最接近的真实替代品。")
    return "\n".join(bullets)


def page_en(item: dict, sha: str, cat_dir: Path) -> str:
    gh = item["github"]
    desc = esc(gh.get("description")) or f"{item['name']} is an open-source repository in the {Path(item['category_path']).name} category."
    archived = " It is archived on GitHub, so treat it as a legacy or pattern-source option rather than a default for new production work." if gh.get("archived") else ""
    card = rel_health(cat_dir, item["slug"], False)
    return frontmatter(item, sha) + f"""
# {item['name']}

{desc}{archived}

![{item['name']} — health radar]({card})

## When to use

You're choosing open-source infrastructure for a task that falls into `{Path(item['category_path']).name}` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for {item['name']} when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because {item['name']} was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on {item['name']}.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

{comparison_en(item, cat_dir)}

## Tech stack

- **Primary language:** {gh.get('language') or 'Unknown'} per GitHub metadata.
- **Repository:** `{gh.get('full_name')}`.
- **Project shape:** categorized as `{item['type']}` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `{gh.get('default_branch')}`, last pushed `{gh.get('pushed_at')}`, archived `{str(bool(gh.get('archived'))).lower()}`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived={str(bool(gh.get('archived'))).lower()}` and `pushed_at={gh.get('pushed_at')}` as of {TODAY}.
- **Adoption snapshot:** ~{gh.get('stars') or 0:,} GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `{gh.get('license') or 'NOASSERTION'}` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** {('archived repository; ' if gh.get('archived') else '')}{('license needs manual verification; ' if 'license_missing_or_noassertion' in item.get('reasons', []) else '')}first-pass page generated from backlog metadata.

## Caveats (unverified)

{caveats_en(item)}
""".lstrip()


def page_zh(item: dict, sha: str, cat_dir: Path) -> str:
    gh = item["github"]
    desc = esc(gh.get("description")) or f"{item['name']} 是 `{Path(item['category_path']).name}` 分类下的开源仓库。"
    archived = " GitHub 将它标为 archived，因此新生产项目不应把它当默认方案，而应先当作遗留或模式参考。" if gh.get("archived") else ""
    card = rel_health(cat_dir, item["slug"], True)
    return frontmatter(item, sha) + f"""
# {item['name']}

{desc}{archived}

![{item['name']} — 健康度雷达]({card})

## 何时使用

你正在为一个落在 `{Path(item['category_path']).name}` 分类里的任务选择开源基础设施，需要评估一个真实仓库，而不是只在对比表里看到一个名字。当 {item['name']} 的上游描述贴合任务，并且采用现成项目比从零写胶水代码更划算时，你把它列入候选。

这个首版页面存在，是因为 {item['name']} 在 atlas backlog 里反复作为对比候选出现。请把它当作有 intake 依据的起点：先核验上游 README 和许可证，再和下方已收录的邻近页面对照，然后再决定是否引入依赖。

## 何时不用

- **你今天就需要一篇已经深度审过的 atlas 页面。** 在本页完成上游文档语义复核前，优先使用横向对比表里更成熟的已收录页面。
- **GitHub 元数据暴露了你的硬约束。** 如果许可证、归档状态或维护节奏是关键约束，优先选择本分类里核验更充分的替代品，而不是直接依赖 {item['name']}。
- **你的任务需要更窄、更专门的替代品。** 如果某个现有页面的“何时不用”已经点名你的约束，应优先按那个页面选型；本页只是较宽的首版入口。
- **你承受不了上游变动或运维未知数。** 请选择 Lindy 记录更长、运维画像更清楚的已收录项目。

## 横向对比

{comparison_zh(item, cat_dir)}

## 技术栈

- **主要语言：** GitHub 元数据返回为 {gh.get('language') or 'Unknown'}。
- **仓库：** `{gh.get('full_name')}`。
- **项目形态：** atlas 路由暂归为 `{item['type']}`；把它当稳定 API 契约前，请复核上游架构。
- **上游状态：** 默认分支 `{gh.get('default_branch')}`，最后 push `{gh.get('pushed_at')}`，archived 为 `{str(bool(gh.get('archived'))).lower()}`。

## 依赖

- **运行时依赖：** 本次 intake 未穷尽核验；生产使用前请检查上游依赖清单。
- **外部服务：** 本次 intake 未穷尽核验；请确认是否需要数据库、队列、云 API、浏览器运行时、GPU 或模型供应商凭据。
- **运维输入：** 至少依赖该 GitHub 仓库及其发布和更新流程。

## 运维难度

**在重读上游文档前，按未知到中等处理。** library 形态的项目可能很容易试用，但仍需要 pin 版本并审查升级。app、service、framework 形态可能隐藏数据库、worker、存储、认证、浏览器、GPU 或云厂商要求，因此请把这个首版页面当成 intake 标记，而不是完整运维手册。

## 健康度与可持续性

- **维护快照：** 截至 {TODAY}，GitHub 返回 `archived={str(bool(gh.get('archived'))).lower()}`，`pushed_at={gh.get('pushed_at')}`。
- **采用快照：** 2026-07 约 {gh.get('stars') or 0:,} 个 GitHub stars；stars 只是有噪声的采用信号。
- **许可证快照：** GitHub API 返回 `{gh.get('license') or 'NOASSERTION'}`；许可证关键时必须检查仓库内许可证文件。
- **Lindy 与治理：** 本次 intake 未完整复核。长期采用前，请继续检查组织归属、项目年龄、发布节奏和 bus factor。
- **风险信号：** {('仓库已归档；' if gh.get('archived') else '')}{('许可证需要人工核验；' if 'license_missing_or_noassertion' in item.get('reasons', []) else '')}本页是从 backlog 元数据生成的首版页面。

## 存疑（未验证）

{caveats_zh(item)}
""".lstrip()


def table_row_en(item: dict, rel_page: str) -> str:
    gh = item["github"]
    use = esc(gh.get("description")) or f"Use it when you need {item['name']} for the {Path(item['category_path']).name} category."
    return f"| **{item['name']}** | {use} | ? (0/6) | [→]({rel_page}) |"


def table_row_zh(item: dict, rel_page: str) -> str:
    gh = item["github"]
    desc = esc(gh.get("description")) or f"当你需要在 `{Path(item['category_path']).name}` 分类中评估 {item['name']} 时用它。"
    return f"| **{item['name']}** | {desc} | ?（0/6） | [→]({rel_page}) |"


def insert_before_section_end(path: Path, row: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if row in text:
        return
    idx = text.find(marker)
    if idx == -1:
        text = text.rstrip() + "\n" + row + "\n"
    else:
        text = text[:idx].rstrip() + "\n" + row + "\n\n" + text[idx:]
    path.write_text(text, encoding="utf-8")


def add_index_rows(item: dict, cat_dir: Path) -> None:
    en = cat_dir / "INDEX.md"
    zh = cat_dir / "INDEX.zh.md"
    insert_before_section_end(en, table_row_en(item, f"{item['slug']}.md"), "\n## Comparison")
    insert_before_section_end(zh, table_row_zh(item, f"{item['slug']}.zh.md"), "\n## 对比")
    # Some category indexes use "## What belongs here" directly after project rows.
    if f"{item['slug']}.md" not in en.read_text(encoding="utf-8"):
        insert_before_section_end(en, table_row_en(item, f"{item['slug']}.md"), "\n## What belongs here")
    if f"{item['slug']}.zh.md" not in zh.read_text(encoding="utf-8"):
        insert_before_section_end(zh, table_row_zh(item, f"{item['slug']}.zh.md"), "\n## 什么该放这里")


def top_category(item: dict) -> str:
    rel = Path(item["category_path"]).relative_to("categories")
    return rel.parts[0]


def add_readme_row(item: dict) -> None:
    top = top_category(item)
    page_rel = f"{item['category_path']}/{item['slug']}.md"
    zh_rel = f"{item['category_path']}/{item['slug']}.zh.md"
    gh = item["github"]
    use = esc(gh.get("description")) or f"Use it when you need {item['name']} in the {top} area."
    row = f"| **{item['name']}** | {use} | {gh.get('license') or 'NOASSERTION'} | ? (0/6) | [EN]({page_rel}) · [中]({zh_rel}) |"
    zh_use = esc(gh.get("description")) or f"当你需要在 {top} 方向评估 {item['name']} 时用它。"
    zh_row = f"| **{item['name']}** | {zh_use} | {gh.get('license') or 'NOASSERTION'} | ?（0/6） | [EN]({page_rel}) · [中]({zh_rel}) |"
    for readme, line in ((ROOT / "README.md", row), (ROOT / "README.zh.md", zh_row)):
        text = readme.read_text(encoding="utf-8")
        if page_rel in text or zh_rel in text:
            continue
        heading = f"### {top}"
        start = text.find(heading)
        if start == -1:
            readme.write_text(text.rstrip() + f"\n\n{heading}\n\n| Project | Use when | License | Health | Page |\n| --- | --- | --- | --- | --- |\n{line}\n", encoding="utf-8")
            continue
        next_heading = text.find("\n### ", start + len(heading))
        if next_heading == -1:
            next_heading = len(text)
        updated = text[:next_heading].rstrip() + "\n" + line + "\n" + text[next_heading:]
        readme.write_text(updated, encoding="utf-8")


def apply(queue_path: Path, limit: int | None, include_risky: bool) -> int:
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    items = [i for i in queue if i.get("status") == "verified"]
    if not include_risky:
        items = [i for i in items if not i.get("reasons")]
    if limit:
        items = items[:limit]
    done = skipped = failed = 0
    for idx, item in enumerate(items, 1):
        cat_dir = ROOT / item["category_path"]
        en = cat_dir / f"{item['slug']}.md"
        zh = cat_dir / f"{item['slug']}.zh.md"
        print(f"phase=apply current={idx}/{len(items)} page={en.relative_to(ROOT)}", flush=True)
        if en.exists() or zh.exists():
            skipped += 1
            continue
        try:
            sha = branch_sha(item["repo"], item["github"].get("default_branch") or "main")
            en.write_text(page_en(item, sha, cat_dir), encoding="utf-8")
            zh.write_text(page_zh(item, sha, cat_dir), encoding="utf-8")
            add_index_rows(item, cat_dir)
            add_readme_row(item)
            item["status"] = "page_created"
            done += 1
        except Exception as exc:
            item["status"] = "apply_failed"
            item.setdefault("reasons", []).append(f"apply_failed:{str(exc)[:160]}")
            failed += 1
        queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"summary created={done} skipped={skipped} failed={failed}")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", type=Path, default=ROOT / "reports/project-intake-queue-2026-07-06.json")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--include-risky", action="store_true", help="include verified items with risk reasons such as archived or NOASSERTION")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    queue = json.loads(args.queue.read_text(encoding="utf-8"))
    verified = [i for i in queue if i.get("status") == "verified"]
    risky = [i for i in verified if i.get("reasons")]
    planned = verified if args.include_risky else [i for i in verified if not i.get("reasons")]
    if args.limit:
        planned = planned[: args.limit]
    print(f"phase=dry-run total={len(queue)} verified={len(verified)} risky={len(risky)} planned={len(planned)} blocked={sum(1 for i in queue if i.get('status') == 'blocked')}")
    for item in planned[:10]:
        print(f"  - {item['id']}: {item['name']} -> {item['category_path']}/{item['slug']}.md")
    if len(planned) > 10:
        print(f"  ... {len(planned) - 10} more")
    if not args.apply:
        print("apply_ready=false reason=dry-run-only add --apply")
        return 0
    return apply(args.queue, args.limit, args.include_risky)


if __name__ == "__main__":
    raise SystemExit(main())
