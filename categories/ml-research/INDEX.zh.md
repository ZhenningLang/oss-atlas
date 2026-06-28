# ml-research

> 分类节点。小而自洽的 ML 研究 demo 与参考实现。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **autoresearch** | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 | [→](autoresearch.zh.md) |
| **llm-circuit-finder** | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制(不训练、不改权重)，再用内置探针验证效果。 | [→](llm-circuit-finder.zh.md) |
| **CLIP** | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 | [→](clip.zh.md) |
| **TaskMatrix** | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 | [→](taskmatrix.zh.md) |
| **PyTorch-GAN** | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 | [→](pytorch-gan.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [autoresearch](autoresearch.zh.md) | ✅ | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 |
| [llm-circuit-finder](llm-circuit-finder.zh.md) | ✅ | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制(不训练、不改权重)，再用内置探针验证效果。 |
| [CLIP](clip.zh.md) | ✅ | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 |
| [TaskMatrix](taskmatrix.zh.md) | ✅ | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 |
| [PyTorch-GAN](pytorch-gan.zh.md) | ✅ | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 |
| nanoGPT / TransformerLens / minGPT | 未收录 | 各页对比里点到的其他研究 demo / 可解释性库。 |

## 什么该放这里

小而自洽、用于研读学习而非投产的 **ML 研究 demo** 与参考实现。不含训练框架(见 `llm-training`)。
