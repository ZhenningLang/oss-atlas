# ml-research

> Category node. Small, self-contained ML research demos and reference implementations.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **autoresearch** | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. | [→](autoresearch.md) |
| **llm-circuit-finder** | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. | [→](llm-circuit-finder.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [autoresearch](autoresearch.md) | ✅ | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. |
| [llm-circuit-finder](llm-circuit-finder.md) | ✅ | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. |
| nanoGPT / TransformerLens / minGPT | 未收录 | Other research demos / interpretability libs named across the pages. |

## What belongs here

Small, self-contained **ML research demos** and reference implementations meant to read and learn from, not to productionize. Not training frameworks (see `llm-training`).
