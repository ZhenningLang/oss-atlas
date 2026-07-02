---
name: AutoGPT
slug: autogpt
repo: https://github.com/Significant-Gravitas/AutoGPT
category: agent-frameworks
tags: [autonomous-agents, ai, workflow-automation, deployment]
language: Python
license: NOASSERTION
maturity: v0.x, active, 185k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T10:28:49Z
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

# AutoGPT

一款用于创建、部署和管理持续运行 AI 智能体以自动化复杂工作流的平台——可免费自托管，或加入云端托管测试版。

![AutoGPT — health radar](../../assets/health/autogpt.zh.svg)

## 何时使用

你是开发者或团队，需要用无需人工干预即可持续运行的 AI 智能体来自动化复杂的多步任务。你想构建能研究主题、编写代码、管理文件并按计划与 API 交互的智能体。你需要灵活地在自己的基础设施上免费自托管，或希望使用托管云选项。AutoGPT 提供了完整的平台，带有用于构建和监控智能体的 Web UI，而非仅仅是一个库。

## 何时不用

- **如果你需要简单、可靠的脚本**——AutoGPT 智能体非确定性，可能意外失败或陷入循环。确定性自动化请用传统脚本或工作流工具。
- **如果你需要低资源边缘部署**——最低要求 4 核 CPU 和 8GB 内存；平台并不轻量。
- **如果你需要编码专用智能体**——AutoGPT 是通用自主智能体平台；软件工程请用 Claude Code、Open Interpreter 或 Kilo Code。
- **如果你需要企业支持保障**——Significant Gravitas 是社区组织，不是企业厂商。无 SLA 或正式支持。
- **如果你想要成熟稳定的 API**——平台仍在快速演变；云端托管测试版尚未公开可用。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | 带学习循环的自我改进智能体。 | Hermes 聚焦技能进化与记忆；AutoGPT 聚焦工作流自动化与部署。 |
| [OpenClaw](openclaw.zh.md) | ✅ | 个人多渠道助手。 | OpenClaw 是对话助手；AutoGPT 是任务自动化平台。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 面向开源模型的终端编码智能体。 | Open Interpreter 是编码工具；AutoGPT 是通用智能体框架。 |
| LangChain | 未收录 | 构建智能体管线的底层框架。 | LangChain 是库；AutoGPT 是带 UI 和部署模型的高级平台。 |
| CrewAI | 未收录 | 多智能体编排框架。 | CrewAI 聚焦多智能体团队；AutoGPT 聚焦单智能体持续执行。 |

## 技术栈

- **Python**——主要实现语言
- **FastAPI**——后端 API 框架（推断）
- **React / Next.js**——平台 Web UI
- **PostgreSQL**——智能体状态与元数据库
- **Redis**——缓存与消息代理

## 依赖

- **硬件**：4 核以上 CPU，最低 8GB 内存（推荐 16GB），10GB 以上可用存储
- **操作系统**：Linux（推荐 Ubuntu 20.04+）、macOS 或带 WSL 的 Windows
- **数据库**：PostgreSQL 用于智能体状态持久化
- **LLM 提供商**：OpenAI API 或兼容端点
- **Docker**：推荐用于部署

## 运维难度

**高**。自托管 AutoGPT 平台需要多个服务（后端、前端、数据库、Redis）、环境配置和持续监控。系统资源密集，且智能体可能以意外方式失败，需要人工监督。

## 健康度与可持续性

- **维护**：活跃——截至 2026-07 每日推送，185k star，454 个开放 issue。自 2023 年发布以来项目经历了重大转向。
- **治理**：由 Significant Gravitas 所有，社区组织。bus factor 不明。
- **背书**：无主要企业背书；资金来自社区捐赠与云端托管候补名单。
- **采用**：star 数极高（185k），但 2023 年创建，仅约 3 年历史。项目在 2023 年经历了著名的炒作周期，此后转向平台模式。
- **长期性**：约 3 年历史且维护活跃，但项目方向已从最初的“自主 GPT”演示大幅转向完整平台。
- **风险旗标**：项目未声明许可（`NOASSERTION`），对商用构成法律风险。云端托管服务仍处于封闭测试。最初的炒作驱动增长可能不代表持续的生产级使用。

## 存疑（未验证）

- [未验证] 仓库未声明许可（`NOASSERTION`），为商用或再分发带来法律不确定性。
- [未验证] 云端托管测试版候补名单已开放较长时间；公开发布时间表不明。
- [推断] 185k star 数主要由 2023 年“自主 GPT”炒作周期推动；当前生产级采用可能显著低于 star 数所示。
- [未验证] 硬件要求（4 核以上、推荐 16GB 内存）针对完整平台；更轻量的使用可能可行，但无官方文档说明。
