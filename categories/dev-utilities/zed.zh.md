---
name: Zed
slug: zed
repo: https://github.com/zed-industries/zed
category: dev-utilities
tags: [code-editor, text-editor, rust, collaborative, gpui]
language: Rust
license: NOASSERTION
maturity: v0.x, active, 86k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T10:35:36Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: A
  overall_score: 3.4
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
      grade: B
      raw:
        stars: 86334
    longevity:
      grade: B
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: B
      raw:
        spdx_id: NOASSERTION
        permissiveness: ?
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Zed

由 Atom 和 Tree-sitter 的创作者用 Rust 构建的高性能多人协作代码编辑器，提供原生速度体验与实时协作。

![Zed — 健康度雷达](../../assets/health/zed.zh.svg)

## 何时使用

你是一位重视编辑原生性能、想要现代原生代码编辑器的开发者，希望它瞬间启动、在大代码库上依然保持响应。你在团队中工作，实时协作编辑——看到队友的光标和实时修改——能加速结对编程与代码评审。你受够了基于 Electron 的编辑器的内存膨胀，想要一个像 Sublime Text 一样快、却具备现代语言服务器支持和 AI 助手集成的工具。你在 macOS、Linux 或 Windows 上，想要一致的原生体验。

## 何时不用

- **如果你需要最大的扩展市场**——Zed 的扩展生态还很年轻，远小于 VS Code 的 5 万余个扩展。许多小众语言支持和工具尚缺。
- **如果你依赖 VS Code 特有的扩展或设置**——Zed 不是直接替代品。你的 `.vscode/settings.json`、快捷键和扩展工作流无法直接迁移。
- **如果你需要纯终端编辑器**——Zed 是 GUI 应用。对于远程 SSH 或纯终端环境，请用 Neovim 或 Vim。
- **如果你需要完全开源、无品牌烙印的构建**——Zed 主体为 GPL-3.0-or-later，部分组件为 Apache-2.0，但项目由 Zed Industries 所有，长期许可策略尚不完全清晰（GitHub 上标记为 NOASSERTION）。
- **如果你在老旧的或低配置机器上工作**——虽然 Zed 比 Electron 编辑器更快，但其 GPU 加速的 GPUI 框架需要现代图形栈。老旧集成显卡可能吃力。
- **如果你需要开箱即用的深度 IDE 功能**——Zed 是编辑器，不是完整 IDE。对于重度 Java/Android 开发，内置调试、分析和项目管理，JetBrains IDE 仍更优。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| VS Code | 已收录 | 最流行的代码编辑器，拥有最大的扩展生态。 | VS Code 的扩展与微软背书无可匹敌，但基于 Electron 且较慢；Zed 原生更快，但更年轻、扩展更少。 |
| Sublime Text | 未收录 | 快速、轻量的专有编辑器，历史悠久。 | Sublime 更快更成熟，但专有且收费；Zed 开源免费，并内置多人协作。 |
| Neovim | 未收录 | 带现代 Lua 插件生态的模态终端编辑器。 | Neovim 仅限终端，高度可定制；Zed 以 GUI 优先，内置协作。 |
| IntelliJ IDEA | 未收录 | 面向 JVM 与 Android 的深度语言专用 IDE。 | IntelliJ 更重、语言更聚焦；Zed 更轻、语言无关，但缺少深度 IDE 功能。 |

## 技术栈

- **Rust**——编辑器核心与 GPUI 框架的主要语言
- **GPUI**——Zed 自研的 GPU 加速 UI 框架（非 Electron）
- **Tree-sitter**——增量解析，用于语法高亮与代码智能（Zed 的创作者也是 Tree-sitter 的创作者）
- **Language Server Protocol (LSP)**——跨语言 IDE 功能支持

## 依赖

- 现代桌面操作系统（macOS、Linux、Windows）
- 支持 GPUI 的 GPU 与图形栈（绝大多数现代桌面）
- 充足内存（最低推荐 8GB）

## 运维难度

**终端用户无运维负担**。Zed 是消费级桌面应用，支持自动更新。对组织而言，主要关注点是管理团队设置、协作权限与扩展治理。

## 健康度与可持续性

- **维护**：非常活跃——每日提交、频繁发布、响应及时的 issue 跟踪。86k star、9.3k fork。
- **治理**：由 Zed Industries 所有，公司由 Atom 和 Tree-sitter 的创作者创立。团队在编辑器技术方面底蕴深厚。
- **背书**：Zed Industries 是一家获得风投支持的初创公司。公司完全专注于 Zed，这是积极信号，但相比多元化基金会，也存在集中风险。
- **采用**：在开发者社区增长迅速，尤其在 Rust 和注重性能的开发者中。市场份额仍仅为 VS Code 的一小部分。
- **长期性**：约 4 年（2021 年创建）。团队有 Atom 的强记录，但 Atom 本身被 GitHub 终止。Zed 是同一愿景的第二次尝试，这改善了 Lindy 信号，但并未消除单厂商编辑器的风险。
- **风险旗标**：GitHub 许可标记为 NOASSERTION，尽管 README 声明 GPL-3.0-or-later。公司的长期可持续性取决于能否找到可行商业模式。需留意潜在的 open-core 阉割或商业协作功能。

## 存疑（未验证）

- [未验证] GPUI 在老旧集成显卡上的确切 GPU 要求尚未在所有平台上测试。
- [未验证] 多人协作功能的网络需求与安全模型尚未经独立审计。
- [推断] 随着产品成熟，Zed Industries 可能会为企业协作引入商业许可或功能层级。
