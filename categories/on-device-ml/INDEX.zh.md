# on-device-ml

> 分类节点。在端侧/边缘设备(手机、笔记本、IoT)本地跑 ML/LLM 推理，而非云端。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘(CPU/GPU/NPU)上跑 Gemma 级 LLM 时用它。 | [→](litert-lm.zh.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值(1.58-bit) LLM 时使用。 | [→](bitnet.zh.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | [→](ai-edge-gallery.zh.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | [→](timesfm.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [LiteRT-LM](litert-lm.zh.md) | ✅ | 想用 Google LiteRT 运行时在手机/笔记本/边缘(CPU/GPU/NPU)上跑 Gemma 级 LLM 时用它。 |
| [BitNet](bitnet.zh.md) | ✅ | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值(1.58-bit) LLM 时使用。 |
| [Google AI Edge Gallery](ai-edge-gallery.zh.md) | ✅ | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 |
| [TimesFM](timesfm.zh.md) | ✅ | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 |
| llama.cpp / Ollama / MLC LLM / ONNX Runtime | 未收录 | 各页对比里点到的其他端侧推理运行时。 |

## 什么该放这里

面向**本地/端侧推理**(手机、笔记本、边缘、CPU)的运行时与模型。不含云端训练(见 `llm-training`)，不含 RAG 检索(见 `rag-retrieval`)。
