---
name: OpenCode
slug: opencode
repo: https://github.com/anomalyco/opencode
category: agent-frameworks
tags: [coding-agent, ai-agent, terminal, cli, typescript]
language: TypeScript
license: MIT
maturity: v0.x, active, 181k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T09:44:42Z
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

# OpenCode

一款开源的终端 AI 编码智能体，可编辑文件、执行命令并与现有代码库协同工作。

![OpenCode — 健康度雷达](../../assets/health/opencode.zh.svg)

## 何时使用

你是一名开发者，想要在终端本地运行一个可审计源码、可按需扩展的 AI 编码智能体。你已厌倦在聊天界面里反复复制粘贴，希望智能体能读取项目文件、跨多文件提出修改建议、运行测试并自行迭代修复错误。你通过 npm 安装 OpenCode，连接 LLM API key，指向一个仓库——它就成了驻留在 shell 里的结对编程搭档，理解你的代码库上下文。

## 何时不用

- **非技术用户或排斥终端的团队**——OpenCode 是 CLI 优先工具；如果你的团队常驻 IDE 或 Web UI，不想学终端命令，它不适合。
- **企业合规需求**——无内置审计日志、RBAC 或管理后台；它是个人开发者工具，不是受控的团队平台。
- **零配置 SaaS 偏好**——你必须自备 LLM API key 并管理本地 Node.js 运行时；无托管云服务。
- **非编程任务**——OpenCode 专为软件工程工作流设计，不适合通用聊天、数据分析或文档生成。
- **重度 IDE 集成需求**——它不是 VS Code 或 JetBrains 扩展；如需 IDE 内 AI 补全，请考虑 Kilo Code 或 Copilot。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 带可切换 harness 的终端编码智能体，面向开源模型。 | Open Interpreter 是 Rust 重写，带 OS 沙箱执行；OpenCode 基于 TypeScript/npm，更年轻。 |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | Nous Research 出品的带学习循环的自我改进智能体。 | Hermes 侧重跨会话技能创建与个人成长；OpenCode 是专注的编码智能体。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 用于自主工作流自动化的平台。 | AutoGPT 面向复杂多步自主任务；OpenCode 是终端结对编程助手。 |
| Claude Code | 未收录 | Anthropic 出品的闭源终端编码智能体。 | 专有、无源码、需订阅；OpenCode 开源且 BYOK。 |
| Gemini CLI | 未收录 | Google 出品的开源终端 AI 智能体。 | Apache-2.0，Google 背书；OpenCode 是 MIT，社区驱动。 |

## 技术栈

- **TypeScript**——主要实现语言
- **Node.js**——运行时环境
- **npm**——通过 `npm install opencode-ai` 分发
- **Monorepo**——包含 console app 与核心逻辑的多个包

## 依赖

- **Node.js** 运行时（需满足包的版本要求）
- **LLM API key**——OpenAI、Anthropic 或兼容提供商
- **终端 / shell**——主要交互界面
- **Git**——用于与仓库协作

## 运维难度

**低**。安装方式类似 `npm install -g opencode-ai`；智能体作为本地进程运行，无需管理常驻服务。持续负担主要是 API key 轮换与保持 npm 包更新。

## 健康度与可持续性

- **维护**：截至 2026-07 非常活跃，每日推送，大量开放 issue（7,113）表明社区参与度高。
- **治理**：由 `anomalyco` 组织所有；bus factor 尚可，但项目很年轻（2025-04 创建），核心团队长期承诺未经检验。
- **背书**：无显著企业背书可见；社区驱动，Discord 活跃。
- **采用**：对一款不足 15 个月的项目来说，star 数极高（181k）。star 数反映的是炒作，而非已验证的有机生产级采用。[推断]
- **风险旗标**：项目极其年轻，毫无 Lindy 记录。MIT 许可干净，但 v0.x 项目如此年轻意味着应预期破坏性变更。

## 存疑（未验证）

- [推断] 2025 年 4 月创建的仓库已有 181k GitHub star，可能受炒作推动，而非有机生产级采用。
- [未验证] 具体 npm 包名与安装路径可能因项目尚处 v0.x 而变动。
- [未验证] 多语言 README 支持（列出 18 余种语言）显示全球化野心，但非英语文档深度未经检验。
- [未验证] `anomalyco` 与任何商业实体或盈利计划之间的关系未公开说明。
