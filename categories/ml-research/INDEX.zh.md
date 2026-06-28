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
| **LSTM Neural Network for Time Series Prediction** | 一份配套文章的精简代码库，演示如何用 Keras 搭一个 LSTM 来预测时间序列——以正弦波和标普 500 数据为例——它是用来讲明白这个技术的，不是用来当预测库交付的。 | [→](lstm-time-series.zh.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 一个中文研究项目（华师大），端到端构建农业知识图谱——爬虫、实体识别、关系抽取、Neo4j 存储，外加一个带检索与问答的 Django demo——作为参考发布，且作者已明确不再维护。 | [→](agriculture-knowledge-graph.zh.md) |
| **Senta (SKEP)** | 百度开源的情感分析工具包，基于 SKEP——一种情感知识增强的预训练方法（ACL 2020）——提供中英文预训练模型和一键预测工具，全部跑在 PaddlePaddle 1.x 框架上。 | [→](senta.zh.md) |
| **Depth Anything V2** | 一个单目深度估计的基础模型（NeurIPS 2024）：输入一张图，输出稠密深度图——四种基于 ViT 的模型规模，比 V1 和基于 SD 的深度模型更快更锐，围绕已发布 checkpoint 配了一个小巧的 PyTorch 推理仓库。 | [→](depth-anything-v2.zh.md) |
| **pymoo** | 一个做单目标与多目标优化的 Python 框架：NSGA-II/III、MOEA/D、GA、DE、CMA-ES、PSO 等等，外加测试问题、约束处理、可视化和决策工具——建立在 NumPy/SciPy 之上，并有可选的编译加速。 | [→](pymoo.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [autoresearch](autoresearch.zh.md) | ✅ | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 |
| [llm-circuit-finder](llm-circuit-finder.zh.md) | ✅ | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制(不训练、不改权重)，再用内置探针验证效果。 |
| [CLIP](clip.zh.md) | ✅ | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 |
| [TaskMatrix](taskmatrix.zh.md) | ✅ | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 |
| [PyTorch-GAN](pytorch-gan.zh.md) | ✅ | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.zh.md) | ✅ | 一份配套文章的精简代码库，演示如何用 Keras 搭一个 LSTM 来预测时间序列——以正弦波和标普 500 数据为例——它是用来讲明白这个技术的，不是用来当预测库交付的。 |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.zh.md) | ✅ | 一个中文研究项目（华师大），端到端构建农业知识图谱——爬虫、实体识别、关系抽取、Neo4j 存储，外加一个带检索与问答的 Django demo——作为参考发布，且作者已明确不再维护。 |
| [Senta (SKEP)](senta.zh.md) | ✅ | 百度开源的情感分析工具包，基于 SKEP——一种情感知识增强的预训练方法（ACL 2020）——提供中英文预训练模型和一键预测工具，全部跑在 PaddlePaddle 1.x 框架上。 |
| [Depth Anything V2](depth-anything-v2.zh.md) | ✅ | 一个单目深度估计的基础模型（NeurIPS 2024）：输入一张图，输出稠密深度图——四种基于 ViT 的模型规模，比 V1 和基于 SD 的深度模型更快更锐，围绕已发布 checkpoint 配了一个小巧的 PyTorch 推理仓库。 |
| [pymoo](pymoo.zh.md) | ✅ | 一个做单目标与多目标优化的 Python 框架：NSGA-II/III、MOEA/D、GA、DE、CMA-ES、PSO 等等，外加测试问题、约束处理、可视化和决策工具——建立在 NumPy/SciPy 之上，并有可选的编译加速。 |
| nanoGPT / TransformerLens / minGPT | 未收录 | 各页对比里点到的其他研究 demo / 可解释性库。 |

## 什么该放这里

小而自洽、用于研读学习而非投产的 **ML 研究 demo** 与参考实现。不含训练框架(见 `llm-training`)。
