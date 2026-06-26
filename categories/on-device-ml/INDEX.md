# on-device-ml

> Level 2 of 3. Run ML / LLM inference locally on edge devices (phone, laptop, IoT) instead of
> in the cloud.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | License | Page |
|---|---|---|---|
| **LiteRT-LM** | Ship a mobile/cross-platform app that runs an LLM offline on-device (especially Gemma on Android) with CPU/GPU/NPU acceleration. | Apache-2.0 | [→](litert-lm.md) |

## Comparison matrix

Substitutes named in the project page but **not yet indexed**.

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [LiteRT-LM](litert-lm.md) | ✅ | Google-maintained, one runtime across Android/iOS/desktop/edge, Gemma sweet spot, NPU support — but Gemma-centric catalog, pre-1.0 churn, Bazel/C++ build, `.litertlm` lock-in. |
| llama.cpp | not indexed | Far broader model/quantization support (GGUF), ubiquitous — but more build complexity, no single blessed mobile SDK. |
| MLX / mlx-lm (Apple) | not indexed | Fast on Apple silicon, clean ergonomics — but Apple-only, can't be cross-platform. |
| MediaPipe LLM Inference API | not indexed | Easier higher-level drop-in (`.task` models) — but less low-level control, overlapping/superseded by LiteRT-LM. |
| ONNX Runtime (+ GenAI/Mobile) | not indexed | Vendor-neutral, many formats/backends — but heavier, less tuned for the latest small mobile LLMs. |

## What belongs here

Runtimes and orchestration layers whose primary job is **local inference on edge/consumer
hardware**. Not cloud-served inference (vLLM, TGI), not training frameworks.
