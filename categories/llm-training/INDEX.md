# llm-training

> Category node. Fine-tune or reinforcement-train LLMs and multi-step agents.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **LlamaFactory** | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. | [→](llamafactory.md) |
| **Unsloth** | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. | [→](unsloth.md) |
| **ART (Agent Reinforcement Trainer)** | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. | [→](art.md) |
| **Agent Lightning** | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. | [→](agent-lightning.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [LlamaFactory](llamafactory.md) | ✅ | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. |
| [Unsloth](unsloth.md) | ✅ | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. |
| [ART (Agent Reinforcement Trainer)](art.md) | ✅ | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. |
| [Agent Lightning](agent-lightning.md) | ✅ | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. |
| axolotl / torchtune / HF TRL / verl | 未收录 | other fine-tuning / RL trainers named in the pages |

## What belongs here

Tools and frameworks whose primary job is to **train, fine-tune, or RL-optimize** LLMs or agents.
Not inference runtimes (see `on-device-ml`), not agent build/run frameworks (see `agent-frameworks`).
