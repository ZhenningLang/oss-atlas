---
name: soul.md
slug: soul-md
repo: https://github.com/aeonfun/soul.md
category: context-engineering
tags: [agent-skill, context-engineering, soul-md, skill-pack]
language: JavaScript
license: NOASSERTION
maturity: active, ~616 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-07-16T05:44:05Z
  default_branch: main
  default_branch_sha: af63feec7dacb0fd91cf9eaffeb608b275ad0e0a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-16T08:16:36Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 3
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 164
        last_commit_age_days: 3
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.9
        top3_share: 0.95
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
---
# soul.md

The best way to build a personality for your agent. Let Claude Code / OpenClaw ingest your data & build your AI soul.

![soul-md — 健康度雷达](../../../assets/health/soul-md.zh.svg)

## 何时使用

你正在评估 `context-engineering` 方向的任务，需要把一个真实仓库纳入 oss-atlas 候选，而不是只在 backlog 里看到一个名字。当上游描述贴合任务、许可证和维护画像经核验后可接受，并且采用公共项目比自写一次性方案更合适时，可以把 soul.md 纳入候选。

这是用户指定 backlog 的首版 intake 页面。用它来完成路由和邻近方案对比；在高风险场景依赖它之前，请重新阅读上游 README、许可证、示例和 release 历史。

## 何时不用

- **你今天就需要深度审过的 atlas 页面。** 在本页完成完整语义复核前，优先选横向对比表里更早收录、约束更清楚的页面。
- **许可证是硬约束。** GitHub 返回 `NOASSERTION`；商用、再分发或 vendoring 前必须检查仓库内许可证文件。
- **维护风险不可接受。** 如果项目很年轻、单人维护、star 少、没有版本线或长期安静，请选同分类里更成熟的替代品。
- **你的任务需要更窄的替代品。** 如果另一个页面的“何时不用”已经点名你的约束，优先用那个页面，而不是这个首版入口。
- **你无法核验上游工作流。** 在检查 README、脚本、依赖和外部 API 要求前，不要安装、运行或 vendor 这个仓库。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| 本叶子已收录技能 | ✅ | 如果已有更深审过的页面已经点名你的任务和约束，优先选它。 | 本页是首版 intake；已有页面的“何时不用”可能更锋利。 |
| 自写 SKILL.md | 未收录 | 当任务很窄、私有或强绑定某个仓库约定时，自写 skill。 | 自写更贴本地上下文，但失去上游维护和社区示例。 |


## 健康度与可持续性

- **维护快照（2026-07-16）：** GitHub 返回 `archived=false`，`pushed_at=2026-07-16T05:44:05Z`。
- **采用快照：** 2026-07 约 616 个 GitHub stars；这是有噪声的信号，低 star 项目只要是真实且相关，也会被纳入。
- **许可证快照：** GitHub 元数据返回 `NOASSERTION`；许可证关键时仍需人工核验许可证文件。
- **Lindy / 治理：** 本次 intake 未完整复核。长期采用前，请继续检查项目年龄、owner 类型、贡献者集中度、release 和 issue 响应。
- **风险信号：** 本页来自 2026-07-16 backlog 的首版生成；语义对比和依赖复核刻意保守。

## 存疑（未验证）

- [未验证] 本页依据公开 GitHub 元数据和用户提供的 intake 清单生成；上游 README、文档、示例、release 和依赖清单仍需深度复核。
- [未验证] 许可证、安装命令、支持的 harness 和运行时要求可能与 GitHub 元数据不同；使用前请在仓库中核验。
- [推断] 横向对比表先从邻近 atlas 分类出发，并不是完整替代品综述；读完上游项目和相邻方案后应继续细化。
