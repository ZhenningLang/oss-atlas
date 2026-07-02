---
name: Hermes Agent
slug: hermes-agent
repo: https://github.com/NousResearch/hermes-agent
category: agent-frameworks
tags: [ai-agent, learning-loop, self-improving, multi-channel]
language: Python
license: MIT
maturity: v0.x, active, 207k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T10:37:26Z
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

# Hermes Agent

Nous Research 构建的自我改进 AI 智能体——它从经验中创建技能，在使用过程中持续改进，并在跨会话中建立对你越来越深的模型。

![Hermes Agent — health radar](../../assets/health/hermes-agent.zh.svg)

## 何时使用

你是一位独立开发者或小团队，在 5 美元 VPS 或 GPU 集群上运行 AI 智能体，需要一个无需手工提示工程就能越用越好的智能体。你想要一个能搜索自己过往对话、跨会话持久化知识、并从真实经验中创建新技能的智能体。你还想在它于云端 VM 上工作的同时，通过 Telegram 与它对话，并可使用任意 LLM 提供商。Hermes Agent 提供了极少其他智能体具备的学习循环。

## 何时不用

- **如果你需要确定性、可重复的系统**——学习循环意味着行为随时间变化，可能让输出非确定性且更难调试。
- **如果你只想要简单的无状态聊天机器人**——Hermes 对一次性问答来说过重；其价值在于累积记忆与技能进化。
- **如果你需要企业安全合规**——Nous Research 是 AI 研究实验室，不是企业厂商；无 SOC 2、SSO 或审计轨迹保障。
- **如果你只需要编码专用智能体**——Hermes 是通用智能体框架，未针对 Claude Code 或 Open Interpreter 这类软件工程任务优化。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [OpenClaw](openclaw.zh.md) | ✅ | 侧重多渠道无处不在的个人助手。 | OpenClaw 是开箱即用的助手；Hermes 是可扩展的学习框架。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 面向部署的自主工作流平台。 | AutoGPT 面向自主任务执行；Hermes 面向通过学习实现自我改进。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 为低成本/开源模型调优的终端编码智能体。 | Open Interpreter 用于编码；Hermes 是带学习循环的通用对话智能体。 |
| LangChain | 未收录 | 构建自定义智能体管线的底层库。 | LangChain 是工具包；Hermes 是内置记忆与技能合成的高级智能体。 |
| CrewAI | 未收录 | 多智能体编排框架。 | CrewAI 聚焦多智能体团队；Hermes 聚焦单智能体自我改进。 |

## 技术栈

- **Python**——主要实现语言
- **CLI 工具**——交互式 shell、安装向导、迁移工具
- **Gateway**——面向 Telegram、Discord 等的消息网关

## 依赖

- Python 运行时（推荐 3.10+）
- LLM 提供商（OpenAI、Anthropic 或本地模型）
- 服务器或 VPS（可在 5 美元 VPS 上运行）
- 如使用网关功能，需消息应用凭证

## 运维难度

**低至中等**。通过 CLI 安装简单；智能体可在最低硬件上运行。学习循环与技能持久化增加了一些运维复杂度——你需要管理知识库并长期监控技能质量。

## 健康度与可持续性

- **维护**：非常活跃——截至 2026-07 每日推送，207k star、24,601 个开放 issue 表明社区庞大且活跃。
- **治理**：由 Nous Research 组织所有；有成熟 AI 研究实验室背书。
- **背书**：Nous Research 是知名 AI 研究组织，在开源模型训练方面有记录。
- **采用**：star 数极高（207k），但项目年轻（2025-07 创建）。快速增长表明有炒作，也有真实兴趣。
- **风险旗标**：项目极其年轻，无 Lindy 记录。学习循环功能新颖，其长期稳定性未经检验。[推断]

## 存疑（未验证）

- [推断] 不足一年即达 207k star，star 数可能反映炒作而非已验证的生产级采用。
- [未验证] 从经验中创建技能的“学习循环”可能产生低质量或意外的技能；生成技能可能需要人工审核。
- [未验证] “5 美元 VPS”的说法可能仅针对最低用量；大模型生产工作负载可能需要显著更多资源。
