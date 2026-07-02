---
name: OpenClaw
slug: openclaw
repo: https://github.com/openclaw/openclaw
category: agent-frameworks
tags: [personal-ai, assistant, multi-channel, self-hosted]
language: TypeScript
license: MIT
maturity: v0.x, active, 381k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-01T10:37:46Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T12:51:57Z
  overall: "?"
  overall_score: null
  scored_axes: 1
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: openclaw
        dependent_repos_count: 0
        downloads_last_month: 14326323
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    maintenance: { reason: recency_unreadable }
    responsiveness: { reason: no_traffic }
    longevity: { reason: not_found }
    governance: { reason: empty_or_gated }
    risk_license: { reason: repo_unreachable }
---
# OpenClaw

一款在自有设备上运行的个人 AI 助手。它在你已使用的消息渠道上应答——包括 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、IRC、Microsoft Teams、Matrix、Feishu、LINE、Mattermost、Nextcloud Talk、Nostr、Synology Chat、Tlon、Twitch、Zalo、WeChat、QQ 和 WebChat——并可在 macOS、iOS 和 Android 上说话、收听，以及渲染你控制的实时 Canvas。

![OpenClaw — health radar](../../assets/health/openclaw.zh.svg)

## 何时使用

你是一位注重隐私的专业人士，想要一个能跟随你穿梭于所有设备与消息应用之间的单一 AI 助手。你试过 Claude 或 ChatGPT 这类纯云服务，但你不愿把对话交给别人的服务器，也希望在 WhatsApp、Telegram、Slack、Discord、iMessage 和 WeChat 等渠道上无需切换不同机器人即可被助手响应。你选择 OpenClaw 而不是 Hermes Agent，因为 OpenClaw 开箱即用地覆盖多渠道——Hermes 是学习循环框架，不是消息原生助手。你选择它而不是 Claude Code 或 OpenCode，因为后者是编程专用工具，不是通用对话助手。你在自己的硬件上安装 OpenClaw，连接偏好的 LLM 提供商，它就成了一个常驻的个人智能体，在你已用的渠道上随时应答。

## 何时不用

- **多用户或团队场景**——OpenClaw 设计为单用户个人助手，没有 RBAC、团队工作区或共享管理后台。如需团队协作，请改用 AutoGPT 或 Hermes Agent，因为这些平台支持多用户编排。
- **零配置 SaaS 偏好**——自托管需要管理 Node.js 运行时、LLM API 凭证和每个渠道的配置，没有托管云选项。如果你希望无需安装即可使用，请改用 Claude 或 ChatGPT，因为它们是云原生服务，零配置负担。
- **企业合规需求**——无审计日志、企业 SSO 或正式安全认证，这是个人工具，不是受治理的企业平台。如需企业治理，请改用 Dify 或 n8n，因为这些平台提供 RBAC、审计轨迹和 SSO。
- **编程专用智能体工作**——OpenClaw 是通用对话助手。如需代码生成与重构等软件工程任务，请改用 OpenCode 或 Claude Code，因为它们是专为编码设计的，具备文件编辑与终端执行能力。
- **你需要从经验中自我改进的学习循环**——OpenClaw 不会创建技能或以自我改进的方式跨会话持久化知识。如果你希望智能体越用越聪明，请改用 Hermes Agent，因为 Hermes 内置了从对话中合成技能的学习循环。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | Nous Research 出品的带学习循环的自我改进智能体。 | Hermes 侧重技能进化与记忆；OpenClaw 侧重多渠道无处不在与对话触达。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 复杂的工作流自动化平台，带部署 UI。 | AutoGPT 面向自主多步任务执行；OpenClaw 是轻量个人聊天助手。 |
| [OpenCode](opencode.zh.md) | ✅ | 模型无关的终端编码智能体。 | OpenCode 用于 shell 中的软件工程；OpenClaw 是通用消息聊天机器人。 |
| [LangChain](langchain.zh.md) | ✅ | 构建自定义智能体管线的底层框架。 | LangChain 是供你构建的库；OpenClaw 是开箱即用的个人助手应用。 |
| Claude / ChatGPT 原生应用 | 未收录 | 闭源、纯云端的助手。 | 专有且需联网；OpenClaw 可自托管、MIT 许可、不绑定渠道。 |

## 技术栈

- **TypeScript**——主要实现语言
- **Node.js**——网关与控制平面运行时
- **跨平台**——支持 macOS、iOS、Android 及服务器操作系统

## 依赖

- LLM 提供商（OpenAI API、Anthropic API 或本地模型端点）
- 网关所需的 Node.js 运行时
- 托管助手的设备或服务器

## 运维难度

**低**。网关是单一控制平面；对习惯运行 Node.js 应用的用户来说安装简单。主要持续负担是配置消息渠道和轮换 LLM 凭证。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护**：Grade A——截至 2026-07 每日推送，13 周中有 13 周活跃，6,749 个开放 issue 表明社区参与度高。
- **治理**：Grade B——由 OpenClaw 组织所有，过去 12 个月有 487 位活跃维护者。首位维护者占 52.8% 的提交，存在集中度风险。
- **长期性**：Grade C——仅 220 天历史（2025-11 创建）。毫无 Lindy 记录；项目极其年轻，尽管 visibility 很高。
- **采用**：Grade A——据健康雷达，GitHub 381k star，npm 月下载量 1430 万。
- **风险旗标**：GitHub 元数据许可为 `NOASSERTION`，而 README 显示 MIT badge，两者存在差异，商用前需澄清。

## 存疑（未验证）

- [未验证] GitHub 元数据中的 `NOASSERTION` 许可可能与 README 上显示的 MIT badge 不一致；商用前请核实。
- [推断] 该仓库 2025 年末创建却已有 381k star，star 数可能受炒作推动，而非有机生产级采用。
- [未验证] “20 余条消息渠道”列表中包含 WeChat、QQ 等平台，其集成 API 可能不稳定或为非官方方案。
- [推断] 健康雷达显示 volume tier 为 A 而 graph tier 为 E，可能表明大部分 npm 下载为直接安装而非传递依赖，暗示个人探索而非嵌入生产使用。
