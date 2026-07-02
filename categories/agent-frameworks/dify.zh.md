---
name: Dify
slug: dify
repo: https://github.com/langgenius/dify
category: agent-frameworks
tags: [agentic-workflow, low-code, rag, mcp, orchestration, nextjs]
language: TypeScript
license: NOASSERTION
maturity: v0.x, active, 147k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T10:38:29Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:40:35Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
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
      grade: A
      raw:
        median_ttfr_hours: 0.2
        qualifying_issues: 25
        band: default
        window_offset_days: 2
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: dify-client
        dependent_repos_count: 8
        downloads_last_month: 8835
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: B
      raw:
        repo_age_days: 1177
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 255
        top1_share: 0.111
        top3_share: 0.227
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Dify

一款用于构建和部署 agentic 工作流的低代码可视化编排平台，内置 RAG 与 MCP 支持。

![Dify — 健康度雷达](../../assets/health/dify.zh.svg)

## 何时使用

你是一支产品团队，需要快速交付 AI 驱动的工作流，又不想从零写起。你想要一个可视化构建器，让非工程师也能设计 agent 流程，而开发者仍能在需要时写代码。你需要内置 RAG 来做文档问答，需要多步工作流编排，还需要通过一个平台连接多种大模型提供商（OpenAI、Anthropic、Gemini、本地模型）。你自托管 Dify，在一个地方迭代聊天机器人、AI 智能体和自动化流水线。

## 何时不用

- **轻量或单用途应用**——Dify 是完整平台，用它做简单的一次性 API 调用属于杀鸡用牛刀。
- **纯代码优先的团队**——如果你的团队更喜欢在 Python 里手写每个 agent 循环，且不喜欢可视化工具，低代码层反而会成为摩擦。
- **严格的许可证合规场景**——GitHub 元数据显示许可为 `NOASSERTION`，商用再分发前请核实条款。[未验证]
- **小资源部署**——自托管需要 Docker、PostgreSQL、Redis 和向量数据库；小 VPS 会吃力。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [LangChain](langchain.zh.md) | ✅ | 底层 agent 工程库。 | LangChain 是代码优先的框架；Dify 是带内置 RAG 与部署能力的可视化平台。 |
| [n8n](../workflow-orchestration/n8n.zh.md) | ✅ | 通用工作流自动化，带 AI 节点。 | n8n 面向更广泛的业务流程自动化；Dify 专为 LLM/agent 工作流打造。 |
| [LangFlow](langflow.zh.md) | 未收录 | AI agent 与 workflow 可视化构建器。 | 两者都走可视化路线；LangFlow 偏 Python 优先且更年轻，Dify 的部署功能更成熟。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 自治持续运行 agent 平台。 | AutoGPT 面向完全自主的长期运行 agent；Dify 聚焦有人参与设计的编排式工作流。 |
| CrewAI / LlamaIndex | 未收录 | 专业化 agent 框架。 | CrewAI 偏重多 agent 团队协作；LlamaIndex 偏重 RAG。Dify 把两者整合到一个平台。 |

## 技术栈

- **TypeScript / Next.js**——前端与 API 层
- **Python**——后端工作流引擎与 AI 逻辑
- **PostgreSQL**——主元数据与配置存储
- **Redis**——缓存与消息代理
- **Docker**——容器化部署

## 依赖

- Docker 与 Docker Compose（推荐部署路径）
- PostgreSQL 数据库
- Redis 实例
- 向量数据库（Weaviate、Qdrant 或 Milvus）用于 RAG
- LLM 提供商 API key 或本地模型端点

## 运维难度

**中等**。Docker Compose 是标准路径，但生产运行 Dify 需要管理数据库、Redis、向量存储和 LLM 凭证。升级、PostgreSQL 备份以及 worker 层扩容都会增加运维面。使用云端托管版可省去这些，但会转为 SaaS 依赖。

## 健康度与可持续性

- **维护**：非常活跃——截至 2026-07 每日推送，社区参与度高（868 个 open issue，23k forks）。[推断]
- **治理**：由 LangGenius 组织背书，似乎有团队而非单一维护者。
- **背书**：LangGenius 看起来是专注本项目而成立的组织，未见大型基金会或企业背书。[未验证]
- **采用**：star 数高（147k），fork 量显著，表明关注度广。项目自 2023 年起活跃，已有约 3 年记录。
- **风险旗标**：GitHub 元数据中的 `NOASSERTION` 许可对商用是隐患——请核实实际许可条款。项目约 3 年历史且 star 数高，需警惕炒作与经检验的长期存续之间的区别。[未验证]

## 存疑（未验证）

- [未验证] GitHub API 返回的许可为 `NOASSERTION`，商用前必须核实实际许可条款。
- [未验证] 生产自托管所需的精确资源（CPU、内存、磁盘）尚未从官方文档确认。
- [推断] 约 3 年的仓库拥有 147k star，可能包含大量炒作驱动的增长；有机的企业级采用需独立验证。
