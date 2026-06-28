# ml-research

> Category node. Small, self-contained ML research demos and reference implementations.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **autoresearch** | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. | [→](autoresearch.md) |
| **llm-circuit-finder** | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. | [→](llm-circuit-finder.md) |
| **CLIP** | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. | [→](clip.md) |
| **TaskMatrix** | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. | [→](taskmatrix.md) |
| **PyTorch-GAN** | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. | [→](pytorch-gan.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [autoresearch](autoresearch.md) | ✅ | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. |
| [llm-circuit-finder](llm-circuit-finder.md) | ✅ | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. |
| [CLIP](clip.md) | ✅ | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. |
| [TaskMatrix](taskmatrix.md) | ✅ | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. |
| [PyTorch-GAN](pytorch-gan.md) | ✅ | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. |
| nanoGPT / TransformerLens / minGPT | 未收录 | Other research demos / interpretability libs named across the pages. |

## What belongs here

Small, self-contained **ML research demos** and reference implementations meant to read and learn from, not to productionize. Not training frameworks (see `llm-training`).
