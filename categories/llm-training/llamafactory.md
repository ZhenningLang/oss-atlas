---
name: LlamaFactory
slug: llamafactory
repo: https://github.com/hiyouga/LlamaFactory
category: llm-training
tags: [fine-tuning, lora, qlora, peft, rlhf, dpo, web-ui, vlm, multimodal, no-code]
language: Python
license: Apache-2.0
maturity: v0.9.5, active (2026-06)
last_verified: 2026-06-26
type: framework
---

# LlamaFactory

A zero-code, config-driven framework that unifies fine-tuning for 100+ LLMs and VLMs behind a CLI, a Gradio web UI (LlamaBoard), and an OpenAI-compatible API.

## When to use

You're an ML engineer or applied researcher who needs to fine-tune a wide range of open models — say Qwen3 this week, Llama-4 the next, a multimodal Qwen-VL after that — and you don't want to rewrite a bespoke training loop or hunt down a different repo for each architecture. You also want to move between methods (LoRA → QLoRA → full tuning → DPO/PPO) without re-plumbing your data pipeline. LlamaFactory resolves this by exposing one declarative interface: you register a dataset, pick a model and a `stage`/`finetuning_type`, and it dispatches to the right path across 100+ supported models. The same YAML config runs from the CLI (`llamafactory-cli train`) or is editable live in LlamaBoard, so you can prototype in the browser and then commit the config for reproducible runs.

It's also a strong fit when the people doing the tuning aren't full-time training engineers. The LlamaBoard web UI lets you launch SFT or preference-optimization jobs, watch loss curves, and run quick chat evals without touching Python — lowering the barrier for domain experts who want to adapt a model to their data. Under the hood it still leans on the standard Hugging Face stack (transformers/peft/trl) plus accelerators like FlashAttention-2, Unsloth kernels, and vLLM/SGLang for fast inference, so you get the convenience layer without being cut off from the ecosystem's primitives.

## When NOT to use

- **You want maximum single-GPU speed/VRAM efficiency.** [Unsloth](unsloth.md)'s custom Triton kernels are reported to be faster and lighter on a single GPU for the model families it supports; LlamaFactory wraps Unsloth optionally but its own dispatch adds initialization overhead. [未验证] benchmark numbers vary by config.
- **You need agentic / multi-turn RL or reward-from-environment training.** LlamaFactory targets the SFT→preference-optimization (DPO/KTO/ORPO/SimPO/PPO) lane, not rollout-based agent RL — see [ART](art.md) or [Agent Lightning](agent-lightning.md).
- **You want a minimal, auditable training loop you fully own.** The framework abstracts a lot; when something breaks deep in a `stage`/`template` interaction, debugging means tracing through LlamaFactory's dispatch layers on top of transformers/trl. A thinner library (torchtune, HF TRL) may be easier to reason about.
- **Config sprawl / template lock-in.** Behavior is driven by model `template`s and a large config surface; getting a custom chat template or unusual dataset format exactly right can be fiddly, and you're coupled to LlamaFactory's abstractions and release cadence.
- **Bleeding-edge architecture day-one.** New model support depends on a LlamaFactory release wiring up the template/dispatch, which may lag a raw transformers integration.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [Unsloth](unsloth.md) | ✅ | Faster/lower-VRAM on a single GPU via custom kernels; narrower model/method coverage and weaker multi-GPU story than LlamaFactory's broad-but-heavier dispatch. |
| [ART](art.md) | ✅ | Agentic RL (GRPO-style rollouts) for training agents; different problem than LlamaFactory's SFT/preference-tuning focus. |
| [Agent Lightning](agent-lightning.md) | ✅ | Trains agents from their own execution traces / RL; not a general SFT/LoRA toolbox. |
| axolotl | 未收录 | YAML-driven, multi-GPU-first with FSDP/DeepSpeed out of the box; favored for reproducible production runs. LlamaFactory adds a web UI and broader zero-code surface. |
| torchtune | 未收录 | Lean, native-PyTorch recipes you own end-to-end; less batteries-included, no web UI. |
| HF TRL | 未收录 | The lower-level SFT/DPO/PPO library LlamaFactory itself builds on; more control, more wiring. |
| Swift (ModelScope) | 未收录 | Comparable broad-coverage tuning framework from the ModelScope ecosystem; overlapping scope. |

## Tech stack

- **Language:** Python (≈99% per repo).
- **Core:** Hugging Face `transformers`, `peft`, `trl`, `accelerate`, `datasets`, `torch`.
- **UI/API:** Gradio (LlamaBoard web UI); OpenAI-compatible HTTP API server.
- **Acceleration:** FlashAttention-2, optional Unsloth kernels, optional quantization (bitsandbytes / GPTQ / AWQ), DeepSpeed & FSDP for distributed training, vLLM / SGLang for inference.
- **Methods:** pre-training, SFT, reward modeling, PPO, DPO, KTO, ORPO, SimPO; full / freeze / LoRA / QLoRA / OFT / QOFT.
- **Tracking:** Weights & Biases, SwanLab, TensorBoard.

## Dependencies

- **Runtime:** Python ≥ 3.11; PyTorch ≥ 2.0 (2.6 recommended). CUDA GPU for any real training (CPU only for trivial smoke tests); Ascend NPU supported.
- **Required Python deps (v0.9.5):** `transformers` ≥ 4.49, `peft` ≥ 0.14, `trl` ≥ 0.8.6, `accelerate` ≥ 0.34, `datasets` ≥ 2.16, `torchvision` ≥ 0.15 (versions per PyPI metadata, recommended pins higher).
- **Optional groups:** `deepspeed`, `bitsandbytes`, `vllm`, `flash-attn`, `galore`, `badam`, `awq`/`gptq`, metrics/tracking extras — installed via pip extras (`pip install "llamafactory[...]"`).
- **Install:** `pip install llamafactory`, or the official Docker image `hiyouga/llamafactory`.

## Ops difficulty

**Low-to-medium.** For the happy path — a single GPU, a supported model, LoRA/QLoRA via LlamaBoard or one CLI command — it's among the easiest ways to get a fine-tune running, and the Docker image removes most environment pain. Difficulty rises to **medium** with multi-GPU/distributed setups (DeepSpeed ZeRO stage / FSDP / Ray config interacts with library versions and VRAM, a common source of incompatibility issues), custom chat templates or non-standard dataset formats, and the usual CUDA/flash-attn/bitsandbytes version-matching friction inherent to the PyTorch training ecosystem.

## Caveats (unverified)

- [未验证] Reported v0.9.5 release date May 30, 2026; star count ~72.5k as of 2026-06 — GitHub stars in this ecosystem are unreliable and date-sensitive; treat as indicative only.
- [未验证] Specific throughput/VRAM comparisons vs Unsloth/axolotl/torchtune come from third-party blog benchmarks and vary heavily with config, model, and hardware; no first-party guarantee.
- [推断] The exact set of supported models/methods shifts release-to-release; "100+ models" is the project's own framing — verify a specific model's support against the current repo before relying on it.
