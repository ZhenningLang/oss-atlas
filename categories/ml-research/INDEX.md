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
| **LSTM Neural Network for Time Series Prediction** | Use it as a readable article-companion example for learning Keras LSTM time-series forecasting — pinned to EOL TF1/Python 3.5 and AGPL-3.0, re-implement from the article rather than vendoring. | [→](lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | Use it as a complete blueprint and bundled datasets for a Chinese domain knowledge-graph pipeline (NER, RE, Neo4j, Django) — author-declared unmaintained on a dated GPL-3.0 stack, lift techniques not code. | [→](agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | Use it when working inside PaddlePaddle/ERNIE and needing SKEP sentiment checkpoints with a published method — pinned to EOL PaddlePaddle 1.6.3, so environment archaeology is unavoidable. | [→](senta.md) |
| **Depth Anything V2** | Use it as the current default monocular-depth foundation model for single-image depth in PyTorch/Transformers — only the Small weights are Apache-2.0; Base/Large/Giant are CC-BY-NC-4.0 (non-commercial). | [→](depth-anything-v2.md) |
| **pymoo** | Use it as the de-facto Python library for evolutionary multi-objective optimization (NSGA-II/III, MOEA/D) to find Pareto fronts — for convex/linear/single-objective problems an LP/gradient solver is far faster. | [→](pymoo.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [autoresearch](autoresearch.md) | ✅ | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. |
| [llm-circuit-finder](llm-circuit-finder.md) | ✅ | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. |
| [CLIP](clip.md) | ✅ | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. |
| [TaskMatrix](taskmatrix.md) | ✅ | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. |
| [PyTorch-GAN](pytorch-gan.md) | ✅ | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.md) | ✅ | Use it as a readable article-companion example for learning Keras LSTM time-series forecasting — pinned to EOL TF1/Python 3.5 and AGPL-3.0, re-implement from the article rather than vendoring. |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.md) | ✅ | Use it as a complete blueprint and bundled datasets for a Chinese domain knowledge-graph pipeline (NER, RE, Neo4j, Django) — author-declared unmaintained on a dated GPL-3.0 stack, lift techniques not code. |
| [Senta (SKEP)](senta.md) | ✅ | Use it when working inside PaddlePaddle/ERNIE and needing SKEP sentiment checkpoints with a published method — pinned to EOL PaddlePaddle 1.6.3, so environment archaeology is unavoidable. |
| [Depth Anything V2](depth-anything-v2.md) | ✅ | Use it as the current default monocular-depth foundation model for single-image depth in PyTorch/Transformers — only the Small weights are Apache-2.0; Base/Large/Giant are CC-BY-NC-4.0 (non-commercial). |
| [pymoo](pymoo.md) | ✅ | Use it as the de-facto Python library for evolutionary multi-objective optimization (NSGA-II/III, MOEA/D) to find Pareto fronts — for convex/linear/single-objective problems an LP/gradient solver is far faster. |
| nanoGPT / TransformerLens / minGPT | 未收录 | Other research demos / interpretability libs named across the pages. |

## What belongs here

Small, self-contained **ML research demos** and reference implementations meant to read and learn from, not to productionize. Not training frameworks (see `llm-training`).
