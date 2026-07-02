---
name: Alacritty
slug: alacritty
repo: https://github.com/alacritty/alacritty
category: terminal-ui
tags: [terminal, terminal-emulator, opengl, gpu, rust, cross-platform]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 65k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-06-22T14:16:02Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: A
  overall_score: 3.6
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
    responsiveness:
      grade: ?
      raw: {}
    adoption:
      grade: B
      raw:
        stars: 64725
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
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Alacritty

快速、跨平台、基于 OpenGL 的终端模拟器，具备合理的默认设置与广泛的配置能力，设计上与其他应用集成而非重新实现它们的功能。

![Alacritty — 健康度雷达](../../assets/health/alacritty.zh.svg)

## 何时使用

你是一位每天在终端里花数小时的开发者，想要最快、最响应的终端模拟器。你受够了在滚动大型日志文件或对多兆字节输出执行 `cat` 时 lag 的终端。你想要一个利用 GPU 渲染、把负载从 CPU 卸下的终端。你偏好极简、可配置的终端，不想让它充当窗口管理器或复用器——你已经用 tmux 或 screen 做那些事。你想要一个在 macOS、Linux、BSD 和 Windows 上配置一致、行为统一的工具。

## 何时不用

- **如果你需要内置终端复用器**——Alacritty 明确不包含标签页、分屏或会话管理。请配合 tmux、screen 或 Zellij 使用 Alacritty，或选择 WezTerm、iTerm2 等内置这些功能的终端。
- **如果你需要连字支持**——Alacritty 不支持字体连字（把 `!=` 合成单个字形）。如果连字对你的工作流至关重要，请用 WezTerm、Kitty 或打过补丁的字体。
- **如果你在不支持 OpenGL 3.3+ 的系统上**——Alacritty 需要现代 GPU 和显卡驱动。老旧系统、部分虚拟机以及远程 X11/VNC 场景可能无法运行。
- **如果你想要内置 AI 或 shell 集成的终端**——Alacritty 是纯粹的终端模拟器。如需 AI 功能、shell 建议或内置智能补全，请考虑 Warp 或 Fig。
- **如果你需要完全稳定、1.0 的产品**——Alacritty 自我定位为 beta 级软件。虽然许多人已将其作为日常工具，但仍有已知缺失功能和 bug。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| WezTerm | 未收录 | 现代 GPU 加速终端，支持标签页、分屏与连字。 | WezTerm 内置功能更多（标签页、连字、复用）；Alacritty 更快、更极简。 |
| Kitty | 未收录 | 基于 GPU 的终端，支持 kitten（插件）和图像等高级功能。 | Kitty 功能更多、有插件系统；Alacritty 更简单、更专注于原生性能。 |
| iTerm2 | 未收录 | 流行的 macOS 终端，功能丰富且集成度高。 | iTerm2 仅限 macOS、功能丰富；Alacritty 跨平台、极简。 |
| Windows Terminal | 未收录 | 微软为 Windows 打造的现代终端，支持标签页与 GPU 加速。 | Windows Terminal 仅限 Windows、集成 WSL；Alacritty 跨平台、更简单。 |
| Warp | 未收录 | 带 AI 功能的现代终端，含云端特性。 | Warp 有 AI 功能和现代 UI；Alacritty 朴素、快速、完全本地。 |

## 技术栈

- **Rust**——主要实现语言
- **OpenGL**——GPU 加速渲染，实现流畅滚动与大型输出
- **FreeType/FontConfig**——字体渲染与配置（平台相关）

## 依赖

- 现代桌面操作系统（macOS、Linux、BSD、Windows）
- 支持 OpenGL 3.3+ 的 GPU 与最新显卡驱动
- 自选的 shell（Alacritty 不捆绑 shell）

## 运维难度

**无**。Alacritty 是单一二进制。通过包管理器安装或 release 下载。配置为单个 YAML 文件。无需守护进程、无需后台服务。

## 健康度与可持续性

- **维护**：活跃——定期发布，维护者响应及时。65k star、3.5k fork。项目管理良好，issue 分类清晰。
- **治理**：由 alacritty 组织维护，有多位贡献者。原创建者（jwilm）已退居幕后，但项目已成功过渡到社区/组织维护。
- **背书**：无企业背书——alacritty GitHub 组织下的社区驱动项目。靠志愿贡献与社区 goodwill 维持。
- **采用**：在重视终端性能的开发者中非常广泛。常在 Rust 与开发者社区被推荐为默认快速终端。
- **长期性**：约 10 年（2016 年创建）。持续维护，无显著断档。对社区项目而言，Lindy 信号良好。
- **风险旗标**：Apache-2.0 安全。无 relicense 历史。项目对功能膨胀持保守态度，这保证了稳定，但可能让想要标签页、连字或内置复用的用户失望。原维护者过渡处理得当。

## 存疑（未验证）

- [未验证] 确切的 OpenGL 版本要求与 Linux 各发行版及硬件上的具体 GPU 驱动兼容性有所不同。
- [未验证] beta 级就绪声明是项目自我评估；许多用户报告日常使用稳定。
- [推断] 随着终端模拟器领域演进，Alacritty 的极简主义可能导致其用户流向 WezTerm 或 Warp 等功能更丰富的替代品，除非它能保持性能优势。
