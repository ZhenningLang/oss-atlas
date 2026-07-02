---
name: Codex
slug: codex
repo: https://github.com/openai/codex
category: agent-frameworks
tags: [coding-agent, terminal, ai-agent, openai, code-execution]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 94.8k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T09:13:07Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
    responsiveness:
      grade: ?
      raw: {}
    adoption:
      grade: B
      raw:
        stars: 94997
    longevity:
      grade: D
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Codex

OpenAI 出品的轻量级编码智能体，在本地终端运行。可读取文件、执行 shell 命令、编辑代码并提交修改——全部通过自然语言界面完成。

![Codex — 健康度雷达](../../assets/health/codex.zh.svg)

## 何时使用

你是一名开发者，希望有一款 AI 助手直接住在终端里，并能真正修改你的代码库。你用自然语言描述需求——「把这个函数重构为 async/await」或「给这条 API 路由加上错误处理」——Codex 就会读取相关文件、做出编辑、运行测试并提交变更。你偏爱本地工作流而非依赖云 IDE，并且希望智能体拥有真实的 shell 访问权限（带沙箱隔离），从而能够验证自身修改。你可以通过单条 curl 命令或 npm 安装它，并与你现有的 Git 工作流配合。

## 何时不用

- **你需要多模型灵活性。** Codex 针对 OpenAI 模型优化。如果你想在 DeepSeek、Anthropic 或本地模型之间频繁切换，请改用 [Open Interpreter](open-interpreter.zh.md)。
- **你处于高度受监管的环境。** Codex 在沙箱中执行代码，但仍在你的机器上运行任意命令。如果你的安全策略禁止带 shell 访问权限的 AI 智能体，则完全不可行。
- **你想要可视化 IDE 体验。** Codex 仅限终端。如果你偏好点击编辑、内联建议与可视化 diff，请使用 GitHub Copilot 或 Cursor 等 IDE 插件。
- **你需要复杂的多智能体编排。** Codex 是单智能体编码工具，并非 LangChain 或 AutoGPT 那样的多智能体框架。构建多智能体协作工作流请另寻他处。
- **你需要离线运行。** Codex 需要联网访问 OpenAI API；不支持本地模型推理。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 带可切换 harness 的 Codex-fork，面向低成本/开源模型。 | Open Interpreter 支持多家提供商和本地模型；Codex 仅限 OpenAI，但拥有第一方集成与更精致体验。 |
| [OpenCode](opencode.zh.md) | ✅ | 开源终端编码智能体。 | OpenCode 模型无关且由社区驱动；Codex 由 OpenAI 背书，与 GPT 集成更紧密。 |
| [Gemini CLI](gemini-cli.zh.md) | ✅ | Google 的终端 AI 智能体。 | Gemini CLI 仅限 Google 模型且带免费层；Codex 仅限 OpenAI，可能需要 API 额度。 |
| Claude Code | 未收录 | 官方 Anthropic 终端编码智能体。 | 闭源，仅限 Anthropic；Codex 开源且原生终端，但锁定 OpenAI 模型。 |
| GitHub Copilot | 未收录 | AI 结对编程 IDE 扩展。 | Copilot 集成在 IDE 中且按订阅收费；Codex 终端优先、独立运行。 |

## 技术栈

- **Rust** — 核心实现，兼顾性能与安全
- **OpenAI API** — 后端 LLM 提供商（GPT-4o / GPT-4.5 级别模型）
- **沙箱隔离** — 在 macOS、Linux 和 Windows 上提供操作系统级代码执行沙箱
- **Git** — 内置版本控制集成，用于提交变更
- **MCP（Model Context Protocol）** — 自定义工具与集成的扩展层

## 依赖

- OpenAI API key（或订阅）
- macOS、Linux 或 Windows 终端
- Git 仓库（推荐，用于变更追踪）
- 网络连接（访问 OpenAI API）

## 运维难度

**低。** Codex 通过 shell 脚本或 npm 安装，作为本地 CLI 进程运行。无需维护服务器。运维负担主要在于管理 OpenAI API 凭证，并在接受智能体修改前进行审查。沙箱机制提供了安全性，但你仍应审计执行的命令。

## 健康度与可持续性

- **维护活跃度**：非常活跃——截至 2026-07 每日推送，迭代迅速，issue 数量庞大（8,147 个 open issues）。[推断]
- **治理与 bus factor**：由 OpenAI（`openai` GitHub 组织）持有。项目获得 OpenAI 的明确支持，但路线图由单一商业实体控制。[未验证]
- **背书与 longevity**：由 OpenAI 官方背书。Apache-2.0 许可证宽松，但 OpenAI 历史上未对主要项目重新许可。[推断]
- **采用与生态**：爆发式采用，约 94.8k stars、约 14.1k forks，2025-04 创建。OpenAI 品牌与终端原生工作流推动快速增长。[推断]
- **风险信号**：极其年轻（2025-04 创建），无 Lindy 记录。与 OpenAI 的 API 和定价紧密耦合，后者可能随时变动。项目的未来取决于 OpenAI 对开源终端工具的投入持续性。[推断]

## 存疑（未验证）

- [未验证] Codex 需要 OpenAI API key；重度使用的确切定价与速率限制尚未核实。
- [推断] 作为 OpenAI 项目，路线图可能优先推动 API 用量或 OpenAI 生态锁定。
- [未验证] 沙箱机制针对恶意对抗性提示的安全保证尚未经过独立审计。
- [推断] 对于 2025-04 创建的项目，star 数极高；部分 inflate 来自 OpenAI 品牌效应，但真实采用度也很强劲。
