---
name: ComfyUI
slug: comfyui
repo: https://github.com/Comfy-Org/ComfyUI
category: on-device-ml
tags: [diffusion, stable-diffusion, image-generation, nodes, pytorch, gui, local-inference, workflow]
language: Python
license: GPL-3.0
maturity: active, ~119k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T10:06:22Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T00:00:00Z
  overall: "?"
  overall_score: 0.0
  scored_axes: 0
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
---

# ComfyUI

最强大、最模块化的扩散模型 GUI 与后端，通过图/节点界面创建复杂的图像生成工作流，无需写代码。

![ComfyUI — 健康度雷达](../../assets/health/comfyui.zh.svg)

## 何时使用

你是数字艺术家或 AI 研究者，想在自有硬件上用 Stable Diffusion 和其他扩散模型生成、编辑和超分图像。你不满足于一键提示框：你想把采样器、VAE、ControlNet、IP-Adapter 和自定义模型串成可复用的工作流。你在画布上拖拽节点，像可视化着色器图一样连线，然后在本地 GPU 上跑管线。ComfyUI 支持 SD 1.x、SDXL、SD3、Flux 以及数十种 checkpoint 和 LoRA，节点生态意味着社区不断加入新能力——从图像修复到视频生成——不用等官方发布。

## 何时不用

- **你没有 NVIDIA GPU 或显存不足。** ComfyUI 依赖 GPU 才能达到可接受的速度；纯 CPU 推理可行，但慢得令人痛苦。4–6 GB 显存的配置必须开启优化，仍可能爆显存。[未验证]
- **你想要简单的一键式图像生成器。** 节点图很强大，但学习曲线陡峭；如果你只想输入提示词拿图，请用 Stable Diffusion WebUI 或云 API。
- **你需要商业支持或托管云服务。** ComfyUI 是自托管工具，无官方 SLA；生产管线可能需要自己封装或使用商业推理平台。
- **GPL-3.0 与你们项目不兼容。** 许可为 GPL-3.0，可能与专有集成或分发计划冲突。
- **你需要跨版本稳定、可复现的工作流。** 节点定义和自定义扩展可能在版本间变动；分享 workflow JSON 并不能保证在另一台装了不同自定义节点的机器上完全一致地运行。[推断]
- **你的主要需求是视频或音频生成。** 虽然 ComfyUI 有视频节点，但其核心优势是图像生成；专用视频工具可能更成熟。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Stable Diffusion WebUI](stable-diffusion-webui.zh.md) | ✅ | 当前页用于它的主场景；如果更看重「更简单、更传统的 Stable Diffusion Web UI」，再选 Stable Diffusion WebUI。 | 更简单、更传统的 Stable Diffusion 标签页式 Web UI，带内置扩展；对初学者更友好，但模块化程度不如 ComfyUI 的节点图。 |
| AUTOMATIC1111 WebUI | 未收录 | 当前页用于它的主场景；如果更看重「经典、文档最丰富的 Stable Diffusion Web 界面」，再选 AUTOMATIC1111。 | 最经典、文档最丰富的 Stable Diffusion Web UI；扩展生态庞大，但比 ComfyUI 更单体化。 |
| InvokeAI | 未收录 | 当前页用于它的主场景；如果更看重「面向艺术家的精致画布，统一生成与编辑」，再选 InvokeAI。 | 面向艺术家的精致画布，生成与编辑在同一视图；UX 更流畅，但开放度与可定制性不如 ComfyUI。 |
| Fooocus | 未收录 | 当前页用于它的主场景；如果更看重「类 Midjourney 的极简本地提示词生图体验」，再选 Fooocus。 | 受 Midjourney 启发的极简提示词生图 UI；快速出图不错，但灵活度远不如 ComfyUI 的节点图。 |
| Diffusers（Hugging Face） | 未收录 | 当前页用于它的主场景；如果更看重「用 Python 库程序化编排扩散管线，不需要 GUI」，再选 Diffusers。 | 用于程序化编写扩散管线的 Python 库；无 GUI，面向开发自己工具的人。 |

## 技术栈

- **语言：** Python（后端推理引擎），前端为 React/TypeScript 的节点图画布。
- **ML 运行时：** 支持 CUDA 的 PyTorch；推理引擎通过在 GPU 上调度 PyTorch 运算来执行节点图。
- **节点系统：** 自定义节点架构，每个节点是一个 Python 类；社区通过往目录里丢 `custom_nodes` 来扩展功能。
- **前端：** 基于 Web 的画布 UI（React/TypeScript），将图序列化为 JSON 后发送给 Python 后端执行。
- **模型格式：** 支持 Safetensors、CKPT、Diffusers、ONNX 以及多种社区格式（LoRA、ControlNet、T2I-Adapter、IP-Adapter 等）。[未验证]

## 依赖

- **硬件：** 强烈建议 NVIDIA GPU + CUDA；跑 SD 1.5/SDXL 舒适需要 8 GB+ 显存，Flux 和更大模型需要 12 GB+。纯 CPU 可行但极慢。
- **软件：** Python 3.10+、带 CUDA 的 PyTorch，以及各类 Python 包（通过 pip 或便携包安装）。支持 Windows、Linux 和 macOS（macOS 走 Metal）。
- **模型：** 需要单独下载 checkpoint、VAE 和 LoRA；工具本身不携带模型。完整模型库很容易超过 100 GB 存储。
- **网络：** 纯本地使用可选，但许多工作流会从互联网下载自定义节点和模型；气隙环境需要手动传模型。

## 运维难度

**高。** ComfyUI 不是装完就能跑的工具。你需要：
- 管理 Python 环境，让 PyTorch + CUDA 与驱动版本对齐。
- 下载并整理数 GB 模型权重，按正确目录结构摆放。
- 保持自定义节点更新，并解决节点包与 ComfyUI 核心版本之间的冲突。
- 监控 GPU 显存占用；大工作流或高分辨率会在普通显卡上爆显存。
- 排查节点图出错时的晦涩报错，尤其是自定义节点损坏或模型不兼容时。
- 备份工作流和模型库；从头重装意味着全部重新下载。

## 健康度与可持续性

- **维护（2026-07）。** 最后 push 于 2026-07-01，每日提交活跃；项目处于快速开发期，发布频繁，Discord 社区活跃。[推断]
- **治理 / bus factor。** 现归属 `Comfy-Org`（独立 GitHub 组织），从原来的单作者 `comfyanonymous` 账号迁移而来——治理成熟度的好信号。核心团队与社区自定义节点生态共同分担维护。[推断]
- **年龄与 Lindy 判断。** 约 2.5 年（2023-01 创建），极其活跃。虽然年轻，但已成为开源扩散工作流工具的统治者；考虑到快速采用与生态增长，Lindy 信号为**中等偏强**。[推断]
- **采用度与生态。** 约 119k star，自定义节点生态庞大（数千个社区扩展）。`.json` 工作流格式已成为分享扩散管线的事实标准。[未验证]
- **风险标记。** GPL-3.0 许可可能限制商业使用和集成；变化节奏快，API 和节点接口可能在版本间破坏。从 `comfyanonymous` 迁到 `Comfy-Org` 是积极的治理步骤，但项目仍年轻，长期资金模式不明。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-07-01 约 119k GitHub star；star 数为近似值且对时间敏感。
- [未验证] 显存需求因工作流和模型而异；SD 1.5 在优化后可能跑在 4 GB，Flux 模型需要 12 GB+ 才能 reasonable 速度。请用目标模型测试。
- [未验证] 节点图 JSON 格式和自定义节点 API 可能在版本间变动；分享或导入工作流时请确认版本兼容性。
- [未验证] CPU 推理和 Apple Metal 支持可行，但性能远低于 CUDA；请在使用前确认硬件可行性。
- [推断] 自定义节点生态庞大但未经过审核；从社区管理器安装节点与安装未经审核的 Python 包风险相同。
- [推断] 模型权重管理完全由用户负责；没有内置模型注册表或版本管理，跟踪 checkpoint 和 LoRA 是手动负担。
