# llm-training

> 分类节点。微调或强化训练 LLM 与多步 agent。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **LlamaFactory** | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 | [→](llamafactory.zh.md) |
| **Unsloth** | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 | [→](unsloth.zh.md) |
| **ART (Agent Reinforcement Trainer)** | 通过客户端-服务端循环用 GRPO 强化学习训练多步 LLM agent，并用 RULER（LLM 充当裁判）实现零标注奖励生成。 | [→](art.zh.md) |
| **Agent Lightning** | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 | [→](agent-lightning.zh.md) |
| **Colossal-AI** | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 | [→](colossalai.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [LlamaFactory](llamafactory.zh.md) | ✅ | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 |
| [Unsloth](unsloth.zh.md) | ✅ | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 |
| [ART (Agent Reinforcement Trainer)](art.zh.md) | ✅ | 通过客户端-服务端循环用 GRPO 强化学习训练多步 LLM agent，并用 RULER（LLM 充当裁判）实现零标注奖励生成。 |
| [Agent Lightning](agent-lightning.zh.md) | ✅ | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 |
| [Colossal-AI](colossalai.zh.md) | ✅ | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 |
| axolotl / torchtune / HF TRL / verl | 未收录 | 各页里点到的其他微调 / RL 训练器 |

## 什么该放这里

主要职责是**训练、微调或 RL 优化** LLM 或 agent 的工具与框架。
不含推理运行时（见 `on-device-ml`），不含 agent 构建/运行框架（见 `agent-frameworks`）。
