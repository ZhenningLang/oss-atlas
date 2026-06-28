# llm-inference

> 分类节点。高性能 LLM/模型推理与服务引擎，以及 AI 系统语言。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | [→](modular.zh.md) |
| **omlx** | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 | [→](omlx.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Modular Platform (MAX + Mojo)](modular.zh.md) | ✅ | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 |
| [omlx](omlx.zh.md) | ✅ | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 |
| vLLM / TGI / TensorRT-LLM / Ray Serve | 未收录 | 各页对比里点到的其他 LLM 推理/服务引擎。 |

## 什么该放这里

主要职责是**高性能 LLM/模型推理与服务**的引擎与系统语言。不含端侧/边缘运行时（见 `on-device-ml`），不含 LLM 微调（见 `llm-training`）。
