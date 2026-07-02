---
name: CC Switch
slug: cc-switch
repo: https://github.com/farion1231/cc-switch
category: agent-frameworks
tags: [desktop-app, ai-tools, provider-management, mcp, skills-management]
language: Rust
license: MIT
maturity: v0.x, active, 111.6k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T09:05:19Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: "?"
  overall_score: 0.0
  scored_axes: 0
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
---

# CC Switch

一款跨平台桌面 All-in-One 管理器，用于管理 Claude Code、Claude Desktop、Codex、Gemini CLI、OpenCode、OpenClaw 和 Hermes Agent——基于 Rust 与 Tauri 2 构建。

![CC Switch — 健康度雷达](../../assets/health/cc-switch.zh.svg)

## 何时使用

你是一名在日常工作流中同时使用多种 AI 编码智能体与助手的开发者。你在深度代码库工作中用 Claude Code，在快速任务中用 Codex，在需要 Google 集成查询时用 Gemini CLI，在个人消息中用 OpenClaw。管理每个工具的凭证、设置和模型提供商很繁琐，你希望有一个桌面控制平面将它们统一起来。你安装 CC Switch，一次性连接所有提供商，即可在一个跨平台界面中管理所有 AI 工具，并支持提供商路由、技能管理和 MCP 集成。

## 何时不用

- **仅使用单一工具的用户**——如果你只使用一个智能体（例如只用 Claude Code），CC Switch 会带来不必要的额外开销。
- **无界面/纯服务器环境**——CC Switch 是基于 Tauri 构建的桌面 GUI 应用，无法在无头服务器或 CI 流水线中运行。
- **团队级策略管控**——没有 RBAC 或团队级管理层面，它是个人生产力工具，不是企业治理平台。
- **不需要提供商管理**——如果你不在多个 LLM 提供商之间切换，也不管理自定义技能或 MCP 服务器，那么这层抽象毫无意义。
- **偏好轻量终端**——如果你完全不想离开终端、不需要 GUI 覆盖层，那么 Tauri 桌面应用不适合你。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [OpenClaw](openclaw.zh.md) | ✅ | 跨多渠道的个人 AI 助手。 | OpenClaw 是自托管的跨消息应用助手；CC Switch 是编码智能体的桌面管理器，不是对话机器人。 |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | 带学习循环的自我改进 AI 智能体。 | Hermes Agent 是自治智能体；CC Switch 是其他智能体的管理层，本身不是智能体。 |
| [OpenCode](opencode.zh.md) | ✅ | 开源终端编码智能体。 | OpenCode 是 CC Switch 管理的工具之一，两者互补而非竞争。 |
| Claude Code / Claude Desktop | 未收录 | Anthropic 官方桌面 IDE 集成。 | 第一方闭源工具；CC Switch 增加了多提供商统一能力，但代价是第三方抽象层。 |
| Cursor / Windsurf | 未收录 | 内置多模型支持的 AI 原生 IDE。 | 这些是带智能体功能的完整编辑器；CC Switch 是元管理器，不是代码编辑器。 |

## 技术栈

- **Rust**——核心后端逻辑与 Tauri 2 集成
- **TypeScript**——前端 UI 层
- **Tauri 2**——跨平台桌面应用框架
- **MCP（Model Context Protocol）**——用于连接自定义技能与集成

## 依赖

- 受支持的桌面操作系统（Windows、macOS 或 Linux）
- 你想管理的 AI 工具（Claude Code、Codex、Gemini CLI 等）需单独安装
- 每个配置的 LLM 提供商的 API 密钥/凭证
- 系统 Webview（由操作系统提供；Tauri 2 使用原生 Webview 引擎）

## 运维难度

**低**。CC Switch 是通过标准安装包分发的桌面 GUI 应用。运维负担仅限于配置你的智能体凭证和保持应用更新。无需维护服务器或数据库。但你需要独立管理每个底层智能体的凭证和更新。

## 健康度与可持续性

- **维护**：活跃——截至 2026-07 每日推送，大量开放 issue（1,636）表明社区参与度高。[推断]
- **治理**：由单个用户（`farion1231`）所有，而非组织——bus factor 实际上为 1。[未验证]
- **背书**：未见企业背书；似乎是独立项目。[未验证]
- **采用**：star 数较高（111.6k）但项目非常年轻（2025-08 创建）。star 数可能反映的是炒作而非已验证的长期存续。
- **风险旗标**：极其年轻，毫无 Lindy 记录。单一维护者带来 bus factor 隐患。[未验证]

## 存疑（未验证）

- [未验证] 该仓库 2025-08 创建却已有 111.6k star，star 数可能受炒作或机器人活动推动，而非有机采用。
- [未验证] `farion1231` 是个人 GitHub 账户，可能没有团队或备份维护者。
- [未验证] 「官方网站」声明（`ccswitch.io`）尚未验证其真伪或持续运营情况。
- [推断] 作为元管理器，CC Switch 的价值取决于其所管理智能体的持续兼容性；上游 API 变动可能迅速破坏集成。
