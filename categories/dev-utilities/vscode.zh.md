---
name: VS Code
slug: vscode
repo: https://github.com/microsoft/vscode
category: dev-utilities
tags: [code-editor, ide, electron, extensible, microsoft]
language: TypeScript
license: MIT
maturity: v1.x, active, 187k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-01T10:34:32Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: A
  overall_score: 4.0
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
    responsiveness:
      grade: ?
      raw: {}
    adoption:
      grade: A
      raw:
        stars: 186885
    longevity:
      grade: A
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# VS Code

Visual Studio Code——一款轻量但强大的代码编辑器，兼具编辑器的简洁与 IDE 的能力，基于 Electron 构建，可通过丰富的扩展市场进行扩展。

![VS Code — health radar](../../assets/health/vscode.zh.svg)

## 何时使用

你是一位开发者，需要一款快速、跨平台的代码编辑器，开箱即支持数十种语言，并具备智能代码补全、调试与 Git 集成。你想要一款能随需求成长的编辑器——从简单的 markdown 与配置文件文本编辑器，到搭配扩展后成为 TypeScript、Python 或 Rust 的完整 IDE。你需要在 macOS、Windows 和 Linux 上都能使用，且快捷键与设置可跨机器同步。VS Code 是数百万开发者的默认选择，因为它精准命中了这个平衡点。

## 何时不用

- **如果你想要完全开源、无品牌烙印的构建**——微软分发的 VS Code 包含专有遥测与扩展市场。如需完全开源的构建，请使用 "Code - OSS" 或 VSCodium。
- **如果你需要纯终端编辑器**——VS Code 是 GUI 应用；纯终端环境请用 Vim、Neovim 或 Emacs。
- **如果你需要绝对最快的编辑器**——基于 Electron 的应用比 Sublime Text 或 Zed 等原生编辑器内存占用更高、启动更慢。在老机器上，VS Code 可能感觉迟钝。
- **如果你想要完全 MIT 许可的分发版**——分发版 VS Code 二进制文件适用微软产品许可；源代码（Code - OSS）才是 MIT 许可。
- **如果你需要深度集成的 JetBrains 风格 IDE**——对于重度 Java、Kotlin 或 Android 工作，IntelliJ IDEA 提供了比 VS Code 扩展更深的语言专用工具链。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| Zed | 未收录 | 高性能原生代码编辑器，支持多人协作。 | Zed 更快、Rust 原生，但生态更小；VS Code 拥有最大的扩展市场。 |
| Sublime Text | 未收录 | 快速、轻量的专有编辑器。 | Sublime 更快更轻，但专有且收费；VS Code 免费开源。 |
| Neovim | 未收录 | 带现代 Lua 配置的模态终端编辑器。 | Neovim 仅限终端，学习曲线陡峭；VS Code 以 GUI 优先，对新手友好。 |
| IntelliJ IDEA | 未收录 | 面向 JVM/Android 的深度语言专用 IDE。 | IntelliJ 更重、聚焦 JVM；VS Code 更轻、语言无关。 |
| VSCodium | 未收录 | 移除微软遥测的完全开源 VS Code 构建。 | VSCodium 去掉了遥测，但缺少微软扩展市场及部分专有功能。 |

## 技术栈

- **TypeScript**——编辑器核心与扩展的主要语言
- **Electron**——桌面外壳与跨平台运行时
- **Monaco Editor**——底层编辑器组件（也用于 Azure DevOps 与 GitHub）
- **Node.js**——扩展主机运行时

## 依赖

- 现代桌面操作系统（macOS、Windows、Linux）
- 充足内存（最低 8GB，大项目推荐 16GB）
- 支持 Electron 的图形栈（绝大多数现代桌面）

## 运维难度

**终端用户无运维负担**。VS Code 是消费级桌面应用——安装与更新由内置更新器或操作系统包管理器处理。对组织而言，主要关注点是管理扩展、设置同步与遥测策略。

## 健康度与可持续性

- **维护**：极其活跃——微软按月发布迭代计划、公开路线图、定期推送更新。187k star，18,939 个开放 issue。
- **治理**：由微软所有，全球最大的科技公司之一。路线图公开，项目资金充足。
- **背书**：微软是坚定的厂商，在开发者工具长期投入方面有良好记录。
- **采用**：全球采用最广泛的代码编辑器之一。扩展生态极其庞大。
- **长期性**：2015 年创建，约 11 年历史且持续活跃开发。强劲的 Lindy 信号。
- **风险旗标**：微软控制专有分发版与扩展市场。分发版中的遥测对部分用户是隐私顾虑。无 relicense 担忧，但 open-core 模式（免费编辑器 + 付费服务）存在。

## 存疑（未验证）

- [未验证] 分发版 VS Code 二进制文件附带的微软产品许可可能包含超出源代码仓库 MIT 许可的条款。
- [未验证] 扩展市场中部分热门扩展是专有的，或自带独立许可条款。
- [推断] 随着微软集成更多 AI 功能（Copilot），未来 VS Code 版本可能越来越倾向于推动微软付费服务。
