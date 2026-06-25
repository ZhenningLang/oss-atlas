---
name: LiteRT-LM
slug: litert-lm
repo: https://github.com/google-ai-edge/LiteRT-LM
category: on-device-ml
tags: [on-device-llm, edge-ai, litert, gemma, mobile-inference, npu, gpu-acceleration, android, ios, cross-platform, google-ai-edge, quantization]
language: C++ core; bindings Python/Kotlin/C++ stable, Swift/JS preview
license: Apache-2.0
maturity: Pre-1.0, fast cadence; stable v0.13.1 (2026-06-03), v0.14.0-alpha (2026-06-18); Google-maintained
last_verified: 2026-06-26
---

# LiteRT-LM

Google's C++ orchestration/runtime layer on top of LiteRT (the TensorFlow Lite successor) for running LLMs fully **on-device** — Gemma first-class (Llama/Phi/Qwen nominally supported but less optimized) on Android, iOS, desktop and edge hardware via CPU/GPU/NPU. Python/Kotlin/C++ bindings are marked *Stable* by Google, but the project itself is pre-1.0 — expect breaking changes; Swift/JS are preview.

## 中文摘要

LiteRT-LM 是 Google 推出的端侧大模型推理编排层,构建在 LiteRT(原 TensorFlow Lite 的继任者)之上,核心用 C++ 写成,提供 Python/Kotlin/C++ 三套稳定 API(Swift、JS/Web 为早期预览,Flutter 为社区维护)。它把模型权重打包成 `.litertlm` 格式,在手机/笔记本/树莓派等设备上用 CPU/GPU/NPU **离线**跑 Gemma、Llama、Phi-4、Qwen 等模型,主打隐私、零网络依赖和成本。**最适合**:Android/跨平台 App 需要离线小模型(尤其 Gemma 系列),且团队能接受 Google 生态与 Bazel 构建。**何时别用**:需要大量第三方/任意 HF 模型(其优化最好的 `.litertlm` 资产以 Gemma 为主);需要云级吞吐或低延迟(端侧比云慢 10-100 倍);设备 RAM 紧张(2-4B 模型常需 6-8GB RAM,内存压力下 Android 可能杀进程);或追求成熟稳定的多模型生态(此时 llama.cpp/MLX 通用性更强)。`[未验证]` 具体 tokens/s 与内存数字来自第三方博客,随机型/量化而变,不保证。

## When to use

Use it when you are shipping a **mobile or cross-platform app** (especially Android, where Kotlin support is stable and first-class) that needs offline/on-device LLM inference for privacy, zero-network operation, or to avoid per-call cloud costs — and your model choice is **Gemma** (or another model already published in `.litertlm` format).

Strong fit when you want one runtime spanning Android/iOS/desktop/Raspberry Pi with CPU plus optional GPU/NPU acceleration, prefer Google-maintained tooling over community glue, and can live with small-model quality limits (short, structured tasks: classification, extraction, summarization, on-device assistants). Third-party benchmarks show it competitive-to-fastest specifically on Gemma-class models on iPhone, so Gemma-centric latency-sensitive on-device apps are its sweet spot.

## When NOT to use

- **Not a general-purpose multi-model runtime** — the optimized `.litertlm` catalog is heavily Gemma-centric. For arbitrary Hugging Face models, exotic architectures, or Qwen/Mistral as first-class citizens, llama.cpp or MLX support far more models with less friction.
- **Not for cloud-grade throughput / low latency** — `[未验证]` on-device inference is reported 10–100× slower than cloud APIs (third-party benchmark, not official); synchronous/interactive flows (multi-minute generations) are unusable without architectural workarounds.
- **Risky on memory-constrained devices** — 2–4B models commonly need 6–8GB RAM and Android may kill the process under memory pressure; the KV cache fills after a few turns and degrades output, forcing session rotation.
- **Not for a frozen, stable API** — pre-1.0 with a fast release cadence `[推断]` (e.g. v0.13.1 → v0.14.0-alpha within ~2 weeks); several bindings are preview (Swift, JS/Web) or community (Flutter), implying ongoing churn.
- **Ecosystem / format lock-in** — models must be packaged into Google's `.litertlm` format and largely sourced from Google's HF community; you also inherit a Bazel-based C++ build.
- **Not for large-model / high-accuracy results** — this is a small-model edge runtime; teams report needing heavy defensive engineering (output parsing, language-drift mitigation, device gating) for reliable behavior.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| llama.cpp | 未收录 | Far broader model/quantization support (GGUF ecosystem) and ubiquitous reach, but more cross-platform build complexity and no single Google-blessed mobile SDK — you assemble more glue. |
| MLX / mlx-lm (Apple) | 未收录 | Faster than LiteRT-LM on many non-Gemma models with clean Swift/Python ergonomics on Apple silicon, but Apple-only — can't be your cross-platform answer. |
| MediaPipe LLM Inference API (Google) | 未收录 | Higher-level, easier drop-in on-device LLM from the same org using `.task` models, but less of a low-level orchestration layer and overlapping/superseded by LiteRT-LM in direction — the simpler-but-less-flexible sibling. |
| ONNX Runtime (+ GenAI / Mobile) | 未收录 | Vendor-neutral, mature, many formats and backends across ecosystems, but heavier, less tuned for the latest small mobile LLMs, and lacks LiteRT-LM's Gemma-specific mobile quantization wins. |
| Apple Core ML / Foundation Models | 未收录 | Best Apple Neural Engine integration and OS-level models on newer iPhones, but Apple-locked, conversion can be painful, no path to Android or generic edge hardware. |

## Tech stack

- C++ core runtime; LiteRT (TensorFlow Lite successor) inference engine
- Bazel build system; CMake; Cargo/Rust tooling
- Python bindings; Kotlin/JNI (Android); Swift/Metal (iOS/macOS, preview); JavaScript/WebAssembly (Web, preview)
- `.litertlm` packaged model format

## Dependencies

- **Bazel** + a pinned `.bazelversion` to build from source (heavy C++ toolchain)
- **LiteRT runtime**
- **Models in `.litertlm` format** from the LiteRT Community on Hugging Face / Kaggle
- **Per-platform native toolchains** — Android NDK, Xcode (iOS/macOS), Emscripten (Web)
- **GPU/NPU vendor drivers** for accelerated backends (NPU support is platform-limited / partly preview)

## Ops difficulty

**High.** Building from source uses Bazel with a pinned version and a large C++/Rust toolchain — non-trivial vs pip-installing a wrapper. Beyond the build, on-device LLM ops are inherently hard: device-tier RAM gating (2–4B models often need 6–8GB RAM or Android kills the process), GPU-init-then-CPU-fallback logic (GPU availability is inconsistent across devices), KV-cache session rotation every few turns `[未验证]` to stop quality decay, and defensive output parsing because small models emit malformed JSON / wrong-language text. Models must be converted/packaged to `.litertlm`. Several bindings (Swift, JS, Flutter) are preview/community, so API churn and gaps are likely pre-1.0.

## Caveats (unverified)

- **Counts** — stars/forks/issues (5,703 / 596 / 383) are from the GitHub API on 2026-06-26 and drift continuously; an earlier snippet reported only ~3,157 stars, so sources disagree. `[未验证]`
- **Throughput** — e.g. "Gemma-class E2B at 55.4 tok/s beating MLX 47.5 and llama.cpp 37.8 on iPhone" is a third-party dev.to benchmark, not official; varies by device/model/quantization. `[未验证]`
- **RAM figures** — ~1.5–8GB per model, ~3.66GB file, ~0.8GB text-only weights — aggregated from blogs and HF model cards, not verified against official specs. `[未验证]`
- **Catalog breadth** — "Gemma-only optimization" is third-party commentary; the README lists Llama/Phi-4/Qwen as supported, so nominal vs actually-available optimized `.litertlm` assets is unconfirmed. `[未验证]`
- **MediaPipe relationship** — the superseding/positioning vs the older MediaPipe LLM Inference API is inferred, not stated in the official overview. `[未验证]`
- **NPU availability specifics** — from docs summaries; may differ from the current release matrix. `[未验证]`
- **Build difficulty** — inferred from repo config (`.bazelrc`, `.bazelversion`, CMake, Cargo), not a measured build. `[推断]`
