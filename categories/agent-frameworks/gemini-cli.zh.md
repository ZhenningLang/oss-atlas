---
name: Gemini CLI
slug: gemini-cli
repo: https://github.com/google-gemini/gemini-cli
category: agent-frameworks
tags: [ai-agent, cli, gemini, mcp-client, mcp-server, terminal]
language: TypeScript
license: Apache-2.0
maturity: v0.x, active, 105.7k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T01:49:23Z
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

# Gemini CLI

一款开源 AI 智能体，将 Gemini 的能力直接带入你的终端。提供轻量级访问 Gemini 模型的方式，内置工具、MCP 支持，并为个人 Google 账户提供免费层。

![Gemini CLI — 健康度雷达](../../assets/health/gemini-cli.zh.svg)

## 何时使用

你是一名常驻终端的开发者，希望有一个能推理你的代码库、运行 shell 命令、搜索网页和读取文件的 AI 助手——全部无需离开命令行。你偏爱 Google 的 Gemini 模型（尤其是 100 万 token 上下文窗口），并想要带有合理速率限制的免费层（60 请求/分钟，1,000 请求/天）。你通过 npm 安装 Gemini CLI，用 Google 账户认证，然后开始委派任务：重构代码、解释 API、生成测试或获取文档。MCP 可扩展性意味着你可以将其接入现有工具生态。

## 何时不用

- **非 Gemini 模型偏好**——Gemini CLI 与 Google 的 Gemini API 紧密耦合。如果你需要频繁在 OpenAI、Anthropic 或本地模型之间切换，这不是你的工具。
- **不允许 Google 账户策略**——免费层需要个人 Google 账户；如果你的组织禁止 Google 认证或你需要企业 SSO，这是障碍。
- **离线/隔离网络环境**——Gemini CLI 需要联网访问 Gemini API；不支持本地模型推理。
- **复杂多智能体编排**——Gemini CLI 是单智能体 CLI 工具，不是 LangChain 或 AutoGPT 那样的多智能体框架。如需构建多智能体协作工作流，请另寻他路。
- **企业审计需求**——无内置审计日志、RBAC 或管理控制；它是个人开发者工具。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [OpenCode](opencode.zh.md) | ✅ | 开源终端编码智能体。 | OpenCode 支持多模型且可自托管；Gemini CLI 仅限 Google，但提供免费层和深度 Gemini 集成。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 支持开源模型可切换 harness 的终端编码智能体。 | Open Interpreter 支持多个模型提供商和本地模型；Gemini CLI 仅限 Gemini，但拥有更强的 Google 生态集成。 |
| Claude Code | 未收录 | Anthropic 官方终端编码智能体。 | 闭源，仅限 Anthropic；Gemini CLI 开源且免费层友好，但锁定 Google 模型。 |
| [CC Switch](cc-switch.zh.md) | ✅ | 多编码智能体桌面管理器。 | CC Switch 可将 Gemini CLI 与其他智能体一并管理；两者互补而非竞争。 |
| GitHub Copilot CLI | 未收录 | GitHub/Microsoft 出品的 AI 驱动 CLI。 | Copilot CLI 基于 Copilot 订阅且 IDE 集成；Gemini CLI 独立且可通过免费层使用。 |

## 技术栈

- **TypeScript**——主要实现语言
- **Node.js**——运行时环境
- **Gemini API**——后端 LLM 提供商（Google）
- **MCP（Model Context Protocol）**——自定义集成的可扩展层
- **Google Search**——内置 grounding 工具

## 依赖

- Node.js 运行时（可通过 npm 安装）
- Google 账户（用于免费层 API 访问）
- 互联网连接（访问 Gemini API 端点）
- 终端/shell 环境

## 运维难度

**低**。Gemini CLI 通过 npm 安装，作为本地 Node.js 进程运行。无需维护服务器。运维负担仅限于保持 CLI 更新和管理 Google API 凭证。免费层有速率限制，重度使用可能需要升级，但没有任何基础设施需要运维。

## 健康度与可持续性

- **维护**：活跃——截至 2026-07 每日推送，issue 跟踪响应及时（1,347 个开放 issue）。[推断]
- **治理**：由 `google-gemini` 组织所有，Google 支持的 GitHub 组织。鉴于 Google 的背书，bus factor 合理，但项目的未来取决于 Google 对开源 CLI 的持续承诺。[未验证]
- **背书**：由 Google（Gemini 团队）官方背书。Apache-2.0 许可非常宽松，但 Google 有 sunset 开源项目的历史。[推断]
- **采用**：star 数强劲（105.7k），创建日期较近（2025-04）。Google 的背书和慷慨的免费层推动了快速采用。[推断]
- **风险旗标**：非常年轻（2025-04 创建），毫无 Lindy 记录。Google 有放弃开源和消费级项目的历史（如 Google Reader、Google+），Gemini 品牌虽看似战略优先，但长期承诺尚未验证。[推断]

## 存疑（未验证）

- [未验证] `google-gemini` 与更广泛的 Google DeepMind/Gemini 产品组织之间的确切关系尚未核实。
- [推断] Google 有推出后随后弃用开源和消费级项目的记录；Gemini CLI 的长期承诺未经检验。
- [未验证] 免费层速率限制（60 请求/分钟，1,000 请求/天）可能随产品成熟而调整。
- [未验证] MCP 服务器生态和第三方集成质量较新，尚未验证。
