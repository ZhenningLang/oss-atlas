# on-device-ml

> Category node. Run ML/LLM inference locally on edge devices (phone, laptop, IoT) instead of the cloud.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **LiteRT-LM** | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). | [→](litert-lm.md) |
| **BitNet** | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. | [→](bitnet.md) |
| **Google AI Edge Gallery** | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. | [→](ai-edge-gallery.md) |
| **TimesFM** | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. | [→](timesfm.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [LiteRT-LM](litert-lm.md) | ✅ | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). |
| [BitNet](bitnet.md) | ✅ | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. |
| [Google AI Edge Gallery](ai-edge-gallery.md) | ✅ | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. |
| [TimesFM](timesfm.md) | ✅ | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. |
| llama.cpp / Ollama / MLC LLM / ONNX Runtime | 未收录 | Other on-device inference runtimes named across the pages. |

## What belongs here

Runtimes and models meant to **run inference locally / on-device** — phone, laptop, edge, CPU. Not cloud training (see `llm-training`), not RAG retrieval (see `rag-retrieval`).
