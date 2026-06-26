# on-device-ml

> 三级路由的第 2 级。在端侧/边缘设备（手机、笔记本、IoT）本地跑 ML / LLM 推理，而非走云端。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 许可证 | 页面 |
|---|---|---|---|
| **LiteRT-LM** | 交付一个在端侧离线跑 LLM 的移动端/跨平台 App（尤其 Android 上跑 Gemma），带 CPU/GPU/NPU 加速。 | Apache-2.0 | [→](litert-lm.zh.md) |

## 对比矩阵

项目页里点到、但**尚未收录**的替代方案。

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [LiteRT-LM](litert-lm.zh.md) | ✅ | Google 维护，一套运行时横跨 Android/iOS/桌面/边缘，Gemma 甜点区，支持 NPU——但目录以 Gemma 为中心、pre-1.0 变动、Bazel/C++ 构建、`.litertlm` 锁定。 |
| llama.cpp | 未收录 | 模型/量化支持（GGUF）广泛得多、无处不在——但构建更复杂，没有单一官方移动 SDK。 |
| MLX / mlx-lm (Apple) | 未收录 | 在 Apple silicon 上快、体验干净——但仅限 Apple，无法跨平台。 |
| MediaPipe LLM Inference API | 未收录 | 更高层、即插即用（`.task` 模型）更易上手——但底层控制更少，与 LiteRT-LM 重叠/被取代。 |
| ONNX Runtime (+ GenAI/Mobile) | 未收录 | 厂商中立、众多格式/后端——但更重、对最新小型移动 LLM 调优不足。 |

## 什么该放这里

主要职责是在**边缘/消费级硬件上本地推理**的运行时与编排层。不包括云端推理（vLLM、TGI），不包括训练框架。
