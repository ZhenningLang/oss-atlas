# llm-eval

> 分类节点。对提示词、agent 与 RAG 做测试、基准与安全红队扫描。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | [→](promptfoo.zh.md) |
| **Pezzo** | 一个开源、可自托管的 LLMOps 平台，做 prompt 管理、版本化、可观测性和成本/延迟监控——一个集中编写 prompt 并观察它们在生产中表现的地方。 | [→](pezzo.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [promptfoo](promptfoo.zh.md) | ✅ | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 |
| [Pezzo](pezzo.zh.md) | ✅ | 一个开源、可自托管的 LLMOps 平台，做 prompt 管理、版本化、可观测性和成本/延迟监控——一个集中编写 prompt 并观察它们在生产中表现的地方。 |
| DeepEval / Ragas / OpenAI Evals / Giskard | 未收录 | 各页对比里点到的其他 LLM 评测 / 红队框架。 |

## 什么该放这里

主要职责是对 LLM 提示词/agent/RAG 做**评测、基准或红队**的工具。不含代码评审(见 `ai-code-review`)，不含训练(见 `llm-training`)。
