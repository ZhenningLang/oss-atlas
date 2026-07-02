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
  computed_at: 2026-07-02T08:42:43Z
  overall: B
  overall_score: 3.25
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
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
      grade: C
      raw:
        repo_age_days: 220
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 487
        top1_share: 0.528
        top3_share: 0.753
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    risk_license: { reason: license_unparsed }
---
# OpenClaw

一款在自有设备上运行的个人 AI 助手。它在你已使用的消息渠道上应答——包括 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、IRC、Microsoft Teams、Matrix、Feishu、LINE、Mattermost、Nextcloud Talk、Nostr、Synology Chat、Tlon、Twitch、Zalo、WeChat、QQ 和 WebChat——并可在 macOS、iOS 和 Android 上说话、收听，以及渲染你控制的实时 Canvas。

![OpenClaw — health radar](../../assets/health/openclaw.zh.svg)

## 何时使用

你是一位注重隐私的专业人士，想要一个能跟随你穿梭于所有设备与消息应用之间的单一 AI 助手。你不愿把对话交给纯云服务，也希望在 WhatsApp、Telegram、Slack、Discord、iMessage、WeChat 等渠道上无需切换不同机器人即可被助手响应。你在自己的硬件上安装 OpenClaw，连接偏好的 LLM 提供商，它就成了一个常驻的个人智能体，在你已用的渠道上随时应答。

## 何时不用

- **多用户或团队场景**——OpenClaw 设计为单用户个人助手，没有 RBAC、团队工作区或共享管理后台。
- **零配置 SaaS 偏好**——自托管需要管理 Node.js 运行时、LLM API 凭证和每个渠道的配置，没有托管云选项。
- **企业合规需求**——无审计日志、企业 SSO 或正式安全认证，这是个人工具，不是受治理的企业平台。
- **编程专用智能体工作**——OpenClaw 是通用对话助手。如需代码生成与重构等软件工程任务，请使用 Claude Code、OpenCode 或 Open Interpreter。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | 类似个人助手角度，但带学习循环。 | Hermes 内置自我改进与技能创建；OpenClaw 侧重多渠道无处不在。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 复杂的工作流自动化平台。 | AutoGPT 面向自主任务执行与部署；OpenClaw 是对话助手。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 终端优先的编码智能体，带可切换 harness。 | Open Interpreter 用于终端编码；OpenClaw 是跨消息应用的聊天机器人。 |
| LangChain | 未收录 | 构建自定义智能体的底层库。 | LangChain 是从头搭建的框架；OpenClaw 是开箱即用的个人助手。 |
| Claude / ChatGPT 原生应用 | 未收录 | 闭源、纯云端的助手。 | 专有且需联网；OpenClaw 可自托管、不绑定渠道。 |

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

- **维护**：Grade A——截至 2026-07 每日推送，13 周中有 13 周活跃，大量开放 issue（6,749）表明社区参与度高。
- **治理**：Grade B——由 OpenClaw 组织所有，过去 12 个月有 487 位活跃维护者。首位维护者占 52.8% 的提交，存在集中度风险。
- **长期性**：Grade C——仅 220 天历史（2025-11 创建）。毫无 Lindy 记录；项目极其年轻，尽管 visibility 很高。
- **采用**：Grade A——据健康雷达，GitHub 381k star，npm 月下载量 1430 万。
- **风险旗标**：GitHub 元数据许可为 `NOASSERTION`，而 README 显示 MIT badge，两者存在差异，商用前需澄清。

## 存疑（未验证）

- [未验证] GitHub 元数据中的 `NOASSERTION` 许可可能与 README 上显示的 MIT badge 不一致；商用前请核实。
- [推断] 该仓库 2025 年末创建却已有 381k star，star 数可能受炒作推动，而非有机生产级采用。
- [未验证] “20 余条消息渠道”列表中包含 WeChat、QQ 等平台，其集成 API 可能不稳定或为非官方方案。
- [推断] 健康雷达显示 volume tier 为 A 而 graph tier 为 E，可能表明大部分 npm 下载为直接安装而非传递依赖，暗示个人探索而非嵌入生产使用。
