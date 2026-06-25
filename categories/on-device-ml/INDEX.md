# on-device-ml

> Level 2 of 3. Run ML / LLM inference locally on edge devices (phone, laptop, IoT) instead of
> in the cloud. 选「端侧/边缘跑模型」的运行时。
> ← back to [category route](../../INDEX.md)

## Projects in this category

| Project | Use when (一句话) | License | Page |
|---|---|---|---|
| **LiteRT-LM** | Ship a mobile/cross-platform app that runs an LLM offline on-device (especially Gemma on Android) with CPU/GPU/NPU acceleration. 跨平台 App 端侧离线跑 LLM(尤其 Android + Gemma)。 | Apache-2.0 | [→](litert-lm.md) |

## Comparison matrix

Substitutes named in the project page but **not yet indexed** (`未收录`).

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [LiteRT-LM](litert-lm.md) | ✅ | Google-maintained, one runtime across Android/iOS/desktop/edge, Gemma sweet spot, NPU support — but Gemma-centric catalog, pre-1.0 churn, Bazel/C++ build, `.litertlm` lock-in. |
| llama.cpp | 未收录 | Far broader model/quantization support (GGUF), ubiquitous — but more build complexity, no single blessed mobile SDK. |
| MLX / mlx-lm (Apple) | 未收录 | Fast on Apple silicon, clean ergonomics — but Apple-only, can't be cross-platform. |
| MediaPipe LLM Inference API | 未收录 | Easier higher-level drop-in (`.task` models) — but less low-level control, overlapping/superseded by LiteRT-LM. |
| ONNX Runtime (+ GenAI/Mobile) | 未收录 | Vendor-neutral, many formats/backends — but heavier, less tuned for the latest small mobile LLMs. |

## What belongs here

Runtimes and orchestration layers whose primary job is **local inference on edge/consumer
hardware**. Not cloud-served inference (vLLM, TGI), not training frameworks.
