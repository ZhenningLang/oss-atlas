---
name: Warp
slug: warp
repo: https://github.com/warpdotdev/warp
homepage: https://www.warp.dev
category: terminal-ui
tags: [terminal, ai-agent, coding-environment, rust, modern-shell]
language: Rust
license: AGPL-3.0
maturity: active, ~62k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T06:16:34Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:29:09Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 27
        band: relaxed_solo
        window_offset_days: 2
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: A
      raw:
        repo_age_days: 1820
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 94
        top1_share: 0.293
        top3_share: 0.396
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Warp

一款为 agent 而生的现代终端——**注意：这个 GitHub 仓库仅用于提交 issue，产品本身是专有闭源软件。**

![Warp — 健康度雷达](../../assets/health/warp.zh.svg)

## 何时使用

你是一名开发者，大部分时间泡在终端里，想要一个现代、快速、IDE 般的命令行体验。你需要命令块（让你像浏览文档一样浏览输出）、AI 辅助命令建议、以及集成编码 agent 等功能。你使用 macOS 或 Linux，想要一个感觉像 2026 年而非 1986 年的终端。你安装 Warp，它用基于 Rust 和 GPU 加速的 shell 取代你的默认终端，支持 bash、zsh 和 fish，内置 AI agent「Oz」可以帮你写命令和调试，或者你也可以在里面运行 Claude Code、Codex、Gemini CLI 等外部编码 agent。

## 何时不用

- **你需要完全开源的软件。** 这个 GitHub 仓库只是 issue 跟踪器。Warp 的实际源代码是专有闭源的。仓库上的 AGPL-3.0 许可证仅适用于极少的 issue 跟踪器代码，不覆盖产品。如果你需要可以审计、修改或自托管的终端，请选择 Alacritty、iTerm2 或 Tabby。[推断]
- **你需要轻量、极简的终端。** Warp 是一个功能丰富的应用（虽然基于 Rust），带有 AI 集成、云功能和现代 UI。如果你想要一个 10MB、50ms 启动的终端，这不是它。
- **你在使用 Windows。** 截至 2026 年中，Warp 主要支持 macOS 和 Linux；Windows 支持有限或不可用。[未验证]
- **你不想要 AI 功能或云连接。** Warp 的价值主张与 AI 辅助和云支持功能（协作、Drive 等）紧密绑定。如果你想要零网络请求、无 AI 的终端，传统终端更合适。
- **你需要通过 SSH 连接远程/无头服务器。** Warp 的高级功能（块、AI 等）在纯 SSH 会话中可能无法工作或完全失效；它面向本地交互使用设计。[推断]
- **你反对专有遥测或云端账户。** Warp 的某些功能需要登录，且是闭源产品；你无法完全审计它收集了哪些数据。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Alacritty | 未收录 | 快速、跨平台、OpenGL 终端模拟器——完全开源。 | 完全开源且极简，但没有原生 AI 功能、没有命令块、没有内置 shell 智能。 |
| iTerm2 | 未收录 | 最受欢迎的 macOS 终端，深度集成 macOS。 | 仅限 macOS，不是开源软件，但成熟且功能丰富，没有 Warp 那种 AI 中心设计。 |
| Tabby | 未收录 | 现代开源终端，带 SSH 客户端和串口支持。 | 开源且跨平台，带一些现代 UI 功能，但不如 Warp 那么原生面向 AI。 |
| [asciimatics](asciimatics.zh.md) | ✅ | 用于构建终端 UI 的 Python TUI 库，不是终端模拟器。 | 这是构建 TUI 的库，不是独立终端应用——不同类别。 |

## 技术栈

- **Rust** —— 核心终端和渲染引擎。
- **WASM** —— 用于某些内部组件和扩展。
- **GPU 加速** —— 现代渲染管线，实现平滑滚动和块。
- **专有代码库** —— 实际源码不开放；GitHub 仓库仅为 issue 跟踪器。

## 依赖

- **操作系统：** macOS 或 Linux（主要平台）。
- **Warp 应用：** 从官方网站或包管理器下载。
- **Shell：** bash、zsh 或 fish。
- **可选：** 如果你想在里面使用外部编码 agent，需要 LLM API 密钥。
- **账户：** 某些功能需要 Warp 账户（有免费层）。

## 运维难度

**低。** Warp 是终端用户桌面应用。下载、安装、使用即可。运维复杂度和任何其他桌面应用一样：保持更新、管理账户/登录需求，并理解它是闭源产品，按 Warp 自己的节奏更新（通常每周四）。无需运行服务器、管理数据库或自托管。

## 健康度与可持续性

- **维护——活跃的产品开发，但闭源。** 团队声称每周发布（通常周四）。GitHub 仓库有频繁的 issue 和功能请求活动，但这不是代码提交的代理，因为仓库仅用于 issue。[推断]
- **治理——厂商控制，单一公司。** Warp 是一家风投支持的公司（Warp.dev），完全拥有这个产品。路线图由公司决定，而非社区。GitHub 仓库存在是为了 issue 透明，不是为了社区治理。[推断]
- **年龄与 Lindy——约 4 年，仍在演进。** 2021-07 创建。对开发工具而言 4 年是中等年龄；终端领域保守，新入局者需要持续证明自己。「agent 终端」这一方向是近期转向，其耐久性未经检验。[推断]
- **采用与生态——增长中的心智份额，封闭生态。** 仅 issue 仓库就有约 62k star，说明兴趣浓厚。但闭源性质限制了生态——无插件、无社区 fork、无独立审计。[未验证]
- **风险信号——专有、闭源，AGPL-3.0 仅覆盖 issue 仓库。** issue 仓库上的 AGPL-3.0 许可证具有误导性，如果你以为它覆盖终端本身。公司改变定价、条款或停止功能的能力不受开源许可证约束。「agentic」功能转向是近期动作，可能改变产品焦点。[推断]

## 存疑（未验证）

- [未验证] 仓库事实，截至 2026-07-01 经 GitHub API：2021-07-08 创建、最后推送 2026-07-01、未归档、约 62.7k star、约 5.1k fork、AGPL-3.0、语言报告为 Rust、owner 类型为 Organization。
- [推断] GitHub 仓库在 README 中明确说明是「仅 issue」；实际产品是专有闭源软件。AGPL-3.0 许可证仅适用于 issue 跟踪器代码。
- [未验证] 平台支持声明（macOS、Linux）和 Windows 限制来自 README 和官网；请为你的操作系统验证当前可用性。
- [未验证] 「每周发布，通常周四」及功能列表（AI agent Oz、命令块、Warp Drive 等）来自 README；实际发布节奏和功能稳定性未经独立验证。
- [推断] 需要 Warp 账户及任何遥测/云数据实践，基于产品的闭源性质和同类工具的常见模式；没有源码访问就无法审计确切的数据处理方式。
- [未验证] 仅 issue 仓库的 star 数可能反映产品兴趣而非代码质量或社区贡献，因为不接受代码贡献。
