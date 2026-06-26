---
name: Cua
slug: cua
repo: https://github.com/trycua/cua
category: web-automation
tags: [computer-use, desktop-automation, vm-sandbox, gui-agent, vision, litellm, osworld, screenspot, macos, windows, linux]
language: Python (HTML/Rust/Swift/TypeScript in repo)
license: MIT
maturity: multi-package monorepo; cua-agent v0.8.4, cua-sandbox v0.1.17, cua-cloud v0.1.1, cua-driver-rs v0.6.8 (pre-release), all updated 2026-06; active, trycua-maintained
last_verified: 2026-06-26
type: framework
---

# Cua

面向 **Computer-Use Agent（计算机操作智能体）** 的开源基础设施：提供 VM/容器沙箱、视觉驱动的 Agent SDK、驱动层和评测基准，让 AI agent 通过“看屏幕、点击”来操作*整台桌面*（macOS、Windows、Linux、Android），而不是靠脚本操纵 DOM。

## 何时使用

你在做一个自动化产品，需要驱动**任意桌面应用**而不仅仅是网页——比如一个流程要打开某个 macOS 原生应用、把数据粘进一个老旧的 Windows 安装程序、再到浏览器里提交。基于选择器的 web 工具一旦任务离开页面就失效，而你又不想自己手工拼装一套 VM + 截图管线 + 模型循环。你还需要每次运行都**隔离且可丢弃**，这样 agent 误点一下也碰不到你的真机或别的租户的数据。

于是你选了 **Cua**。一行异步调用拉起临时沙箱——`Sandbox.ephemeral(Image.macos())` 或 `.linux()` / `.windows()` / `.android()`——交给一个 `ComputerAgent`，它从截图出发驱动桌面，无论底层是哪个 OS 或 runtime，API 都一样。因为 agent 层基于 liteLLM，你可以指向自己已经在付费的、具备 computer-use 能力的模型（Anthropic、OpenAI 等），不被单一厂商绑死。在 Apple Silicon 上可以用 Lume/Lumier 本地跑 macOS 客户机；要规模化就把同一份代码推到 Cua Cloud。需要证明效果时，Cua-Bench 在 OSWorld / ScreenSpot / Windows Arena 上给你的 agent 打分，还能导出轨迹用于训练。

## 何时不用

- **你只需要自动化一个网页。** 为了填个表单或抓个站，动用一整台桌面 VM + 截图循环属于杀鸡用牛刀——用页面内或浏览器级工具（[page-agent](page-agent.zh.md)、Playwright、browser-use），有 DOM 访问会更快、更便宜、更确定。
- **你要求每步低延迟 / 高吞吐。** 视觉 agent 每一步都要截图、调模型、再操作，相比 DOM/选择器自动化又慢又费 token，不适合紧凑实时循环或预算有限的大规模并行。
- **你跑不了 VM/容器。** 这是重型基础设施：VM、驱动、computer-server。macOS 客户机实际上需要 Apple Silicon（Virtualization.framework）；Linux 的 Cua Drivers 标注为 pre-release。
- **你想要一个 API 冻结的稳定单一 SDK。** 它是一个快速迭代的 monorepo，包含多个独立版本号的包（agent、sandbox、computer-server、cli、bench、train、cloud），大多停在 `v0.x`——会有 churn 和破坏性变更。
- **闭环像素级可靠性比覆盖面更重要。** computer-use 模型仍会误点、对 UI 状态产生幻觉；对合规关键或不可逆操作，你需要框架本身并不替你提供的护栏。
- **数据外发敏感。** 桌面截图会被发送到你选择的模型厂商——指向机密应用前请先做隐私/合规评估，并注意每张截图的 token 成本。

## 横向对比

| 替代方案 | 是否已收录 | 取舍 |
|---|---|---|
| [page-agent](page-agent.zh.md) | ✅ | 页面内 JS GUI agent，在用户自己的浏览器里把 DOM 当文本操作——无 VM、无视觉，远更便宜更快，但仅限 web、碰不到原生桌面应用。 |
| [Chrome DevTools MCP](chrome-devtools-mcp.zh.md) | ✅ | 通过 MCP 用 DevTools 协议暴露真实 Chrome——擅长浏览器调试/自动化，但范围限于 Chrome，不是整桌面沙箱。 |
| [Agent Browser](agent-browser.zh.md) | ✅ | 面向 agent 的无头浏览器自动化 CLI——轻量的 web 任务执行器；无 OS 级控制、无 VM 隔离。 |
| OpenAI Operator / Anthropic computer use | 未收录 | 托管的视觉 computer-use agent——开箱即用但闭源、绑定单一模型厂商；Cua 是可自托管的开源基础设施层（且能通过 liteLLM *运行*这些模型）。 |
| OSWorld / WebArena（评测基准） | 未收录 | Cua-Bench 对接的评测环境——它们给 agent 打分；Cua 提供被打分的可运行沙箱 + agent。 |
| E2B / Daytona（开发沙箱） | 未收录 | 面向 agent 的代码执行沙箱——在 VM 隔离上有重叠，但定位是跑代码，不是截图驱动 GUI 桌面。 |

## 技术栈

- **语言：** Python（Agent/Sandbox SDK、computer-server）、Rust（`cua-driver-rs` 驱动）、Swift（Lume——Apple `Virtualization.framework`），仓库内还有 HTML/TypeScript。
- **Agent 层：** `cua-agent`——由截图（视觉）驱动的 `ComputerAgent` 循环，集成 **liteLLM** 做模型路由。
- **沙箱：** `cua-sandbox` SDK，底层基于 Lume/Lumier（Apple Silicon 上的 macOS/Linux VM）、Linux 容器、本地 QEMU 后端，以及 Cua Cloud（cua.ai）。
- **驱动：** `cua-driver-rs` / Cua Drivers——后台桌面自动化，也以 MCP server 形式暴露。
- **评测/训练：** `cua-bench`（OSWorld、ScreenSpot、Windows Arena、自定义任务；轨迹导出）、`cua-train`。
- **第三方：** Kasm（MIT）、OmniParser（CC-BY-4.0）、可选 ultralytics（AGPL-3.0）——注意这个 AGPL 可选依赖。

## 依赖

- **运行时：** SDK 需 Python ≥ 3.11（`pip install cua`）。一个 liteLLM 可用的模型端点（如 Anthropic / OpenAI 具备 computer-use 能力的模型）+ API key。
- **沙箱宿主：** 本地 macOS 客户机需 **Apple Silicon Mac**（通过 Lume 用 Virtualization.framework）；Linux 客户机用容器或 QEMU；Windows/Android 客户机见文档。Cua Cloud 可去掉本地宿主要求。
- **驱动：** 通过 bash（macOS/Linux）/ PowerShell（Windows）脚本安装；Linux 驱动支持为 pre-release。
- **Bench：** `cua-bench` 用 `uv tool install`。

## 运维难度

**中到高。** Cloud 路线（cua.ai）是轻松入口——托管沙箱，无需照看本地 VM。自托管更重：你要运维 VM/容器、computer-server 和驱动，在 Apple Silicon 上还要管理 Lume/Lumier 客户机镜像。跨多个 `v0.x` 包你得跟踪好几条独立版本线，视觉 agent 循环还带来持续的**每张截图的模型成本/延迟**，以及把桌面截图发给模型厂商的数据治理问题。Linux 驱动尚为 pre-release，意味着各平台覆盖仍不均衡。

## 存疑（未验证）

- [未验证] star 数约 19.0k（gh 快照 2026-06-26）——GitHub star 不可靠且随时间变化，仅作参考。
- [未验证] 各包版本（cua-agent v0.8.4、cua-sandbox v0.1.17、cua-cloud v0.1.1、cua-driver-rs v0.6.8、cua-bench v0.2.11）取自 2026-06-24/26 的发布列表；确切数字按快照时点看待。
- [推断] 具体支持的模型字符串（如 Anthropic Claude / OpenAI computer-use-preview / UI-TARS / OmniParser 等 loop）是从已记载的 liteLLM 集成与视觉设计推断的，并非逐字引用自当前的 supported-models 表——依赖某个模型前请对照文档核实。
- [推断] “无论 OS 或 runtime API 都一样”及 `Sandbox.ephemeral(Image.macos())` 风格代码片段是对 README 自述措辞的转述；当前确切 API 表面应对照 SDK 核实。
- [未验证] 对比中的替代方案（Operator、OSWorld/WebArena、E2B/Daytona）部分为基于仓库 + 二手背景的推断定位，并非全部经第一方确认。
- [推断] 可选依赖 ultralytics 为 AGPL-3.0——在为部署假定“仅 MIT”许可前，确认你的使用路径是否会引入它。
