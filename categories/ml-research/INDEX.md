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
| **LSTM Neural Network for Time Series Prediction** | A compact, article-companion codebase showing how to build a Keras LSTM to predict time-series sequences — demoed on a sine wave and S&P 500 data — built to teach the technique, not to ship as a forecasting library. | [→](lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | A Chinese-language research project (ECNU) that builds an agricultural knowledge graph end-to-end — crawlers, entity recognition, relation extraction, a Neo4j store, and a Django demo with retrieval and Q&A — published as a reference, and explicitly no longer maintained. | [→](agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | Baidu's open-source sentiment-analysis toolkit built on SKEP — a sentiment-knowledge-enhanced pretraining method (ACL 2020) — shipping Chinese/English pretrained models and a one-line prediction tool, all on the PaddlePaddle 1.x framework. | [→](senta.md) |
| **Depth Anything V2** | A foundation model for monocular depth estimation (NeurIPS 2024): one image in, a dense depth map out — four ViT-based model sizes, faster and sharper than V1 and SD-based depth models, with a small PyTorch inference repo around the released checkpoints. | [→](depth-anything-v2.md) |
| **pymoo** | A Python framework for single- and multi-objective optimization: NSGA-II/III, MOEA/D, GA, DE, CMA-ES, PSO and more, plus test problems, constraint handling, visualization, and decision-making tools — built on NumPy/SciPy with optional compiled speedups. | [→](pymoo.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [autoresearch](autoresearch.md) | ✅ | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. |
| [llm-circuit-finder](llm-circuit-finder.md) | ✅ | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. |
| [CLIP](clip.md) | ✅ | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. |
| [TaskMatrix](taskmatrix.md) | ✅ | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. |
| [PyTorch-GAN](pytorch-gan.md) | ✅ | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.md) | ✅ | A compact, article-companion codebase showing how to build a Keras LSTM to predict time-series sequences — demoed on a sine wave and S&P 500 data — built to teach the technique, not to ship as a forecasting library. |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.md) | ✅ | A Chinese-language research project (ECNU) that builds an agricultural knowledge graph end-to-end — crawlers, entity recognition, relation extraction, a Neo4j store, and a Django demo with retrieval and Q&A — published as a reference, and explicitly no longer maintained. |
| [Senta (SKEP)](senta.md) | ✅ | Baidu's open-source sentiment-analysis toolkit built on SKEP — a sentiment-knowledge-enhanced pretraining method (ACL 2020) — shipping Chinese/English pretrained models and a one-line prediction tool, all on the PaddlePaddle 1.x framework. |
| [Depth Anything V2](depth-anything-v2.md) | ✅ | A foundation model for monocular depth estimation (NeurIPS 2024): one image in, a dense depth map out — four ViT-based model sizes, faster and sharper than V1 and SD-based depth models, with a small PyTorch inference repo around the released checkpoints. |
| [pymoo](pymoo.md) | ✅ | A Python framework for single- and multi-objective optimization: NSGA-II/III, MOEA/D, GA, DE, CMA-ES, PSO and more, plus test problems, constraint handling, visualization, and decision-making tools — built on NumPy/SciPy with optional compiled speedups. |
| nanoGPT / TransformerLens / minGPT | 未收录 | Other research demos / interpretability libs named across the pages. |

## What belongs here

Small, self-contained **ML research demos** and reference implementations meant to read and learn from, not to productionize. Not training frameworks (see `llm-training`).
