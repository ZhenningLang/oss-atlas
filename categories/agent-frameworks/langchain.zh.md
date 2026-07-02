---
name: LangChain
slug: langchain
repo: https://github.com/langchain-ai/langchain
category: agent-frameworks
tags: [llm, agents, rag, framework, python, typescript]
language: Python
license: MIT
maturity: v0.x, active, 141k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T10:23:37Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:39:16Z
  overall: A
  overall_score: 3.67
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.3
        qualifying_issues: 30
        band: default
        window_offset_days: 6
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: langchain-text-splitters
        dependent_repos_count: 0
        downloads_last_month: 44773025
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: B
      raw:
        repo_age_days: 1354
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 48
        top1_share: 0.53
        top3_share: 0.757
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# LangChain

agent 工程平台——通过组合可互操作组件与第三方集成，构建 agent 与 LLM 驱动应用的框架。使用 `uv add langchain` 安装。

![LangChain — health radar](../../assets/health/langchain.zh.svg)

## 何时使用

你是一位 Python 开发者，正在构建需要把大模型连接到外部工具、数据库和 API 的 AI 应用。你想要一种结构化方式来编排 prompt 模板、管理对话记忆，并在不同模型与工具之间路由。你需要庞大的预构建集成生态（向量存储、文档加载器、模型提供商），以免自己写每个适配器。你计划构建能推理、使用工具并在多步之间保持状态的 agent。

## 何时不用

- **简单单 prompt 应用**——如果你只需要调用一次大模型 API，LangChain 会增加抽象开销而无实际收益。
- **生产级延迟敏感场景**——框架的抽象层可能引入开销。对毫秒级关键路径，考虑直接调用 API 或更轻量封装。
- **厌恶供应商锁定**——与 LangChain 生态的深度集成可能在你后续想迁移时产生摩擦。
- **小资源预算**——完整框架及其所有集成可能拉入大量依赖。采用前请验证部署目标的容量。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Dify](dify.zh.md) | ✅ | agentic 工作流可视化平台。 | Dify 是带内置 RAG 与部署能力的低代码平台；LangChain 是构建自定义 agent 的代码优先库。 |
| LlamaIndex | 未收录 | 面向 LLM 的 RAG 优先数据框架。 | LlamaIndex 专长于检索与数据摄入；LangChain 更广义，涵盖 agent、chain 和 tool。 |
| [DSPy](dspy.zh.md) | ✅ | 通过指标优化 prompt。 | DSPy 按指标优化 prompt/权重；LangChain 是通用组合框架。 |
| OpenAI SDK | 未收录 | OpenAI 模型的直接厂商 SDK。 | OpenAI SDK 极简快速，但缺乏 LangChain 的多提供商、多工具抽象能力。 |
| [smolagents](smolagents.zh.md) | ✅ | Hugging Face 出品的极简透明 agent 循环。 | smolagents 极简透明；LangChain 全面且集成丰富。 |

## 技术栈

- **Python**——主要实现（也有 TypeScript/JS 包）
- **Pydantic**——数据验证与序列化
- **LangGraph**——构建多 agent 工作流的配套库
- **LangServe**——LangChain chain 的部署层

## 依赖

- Python 3.9+ 环境
- LLM 提供商 API key（OpenAI、Anthropic、Gemini 等）或本地模型端点
- 可选：向量数据库（Pinecone、Weaviate、Chroma、FAISS）用于 RAG
- 可选：各类工具集成（搜索 API、数据库等）

## 运维难度

**低**。LangChain 是可 pip 安装的库，不是服务。运维负担在你的应用代码中：管理 API key、处理模型限速、优化 chain 延迟。部署是标准 Python 应用部署。主要复杂度来自庞大集成生态带来的依赖管理。

## 健康度与可持续性

- **维护**：Grade A——截至 2026-07 在 1 天内有推送，13 周中有 13 周活跃。对如此规模的项目，415 个 open issue 管理良好。
- **响应度**：Grade A——首次响应中位时间 0.3 小时，表明维护团队极其高效。
- **治理**：Grade B——由 LangChain AI, Inc. 支持，过去 12 个月有 48 位活跃维护者。首位维护者占 53% 的提交，存在集中度风险。
- **长期性**：Grade B——1,354 天历史（2022-10 创建），约 3.7 年记录。对一款仍在积极维护的 AI 项目而言，这是不错的 Lindy 信号。
- **采用**：Grade A——据健康雷达，GitHub 141k star，23k+ fork，PyPI 月下载量 4470 万。volume tier 为 A，生态采用广泛。
- **风险旗标**：LangChain AI 提供商业产品（LangSmith、LangGraph Cloud），可能产生 open-core 或功能阉割压力。框架的快速演进历史上曾导致版本间破坏性变更。

## 存疑（未验证）

- [未验证] LangSmith 和 LangGraph Cloud 的精确路线图以及开源与商业功能边界尚未确认。
- [未验证] 小版本间破坏性变更的历史频率可能已趋于稳定，但生产使用前请验证。
- [推断] 作为风险投资支持的公司，LangChain AI 可能将重心转向创收产品；若厂商独立性对你至关重要，请评估社区 fork 或替代方案。
