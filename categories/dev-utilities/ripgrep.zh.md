---
name: ripgrep
slug: ripgrep
repo: https://github.com/BurntSushi/ripgrep
category: dev-utilities
tags: [search, grep, regex, cli, rust, gitignore]
language: Rust
license: Unlicense
maturity: v14.x, active, 66k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-06-21T12:48:16Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: B
  overall_score: 3.2
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
        stars: 65651
    longevity:
      grade: A
      raw: {}
    governance:
      grade: C
      raw:
        owner_type: User
    risk_license:
      grade: A
      raw:
        spdx_id: Unlicense
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# ripgrep

面向行的搜索工具，递归搜索目录中的正则模式，默认自动遵守 gitignore 规则并跳过隐藏文件与二进制文件。

![ripgrep — 健康度雷达](../../assets/health/ripgrep.zh.svg)

## 何时使用

你是一位每天搜索大型代码库的开发者，想要一个默认就快速、智能且尊重项目结构的工具。你厌倦了 `grep -r` 从 `.git`、`node_modules` 和构建产物中返回噪音。你想要一个在 Windows、macOS 和 Linux 上行为一致、每次发布都带预编译二进制文件的工具。你需要支持 Unicode 的正则搜索、可选的多行匹配，以及按特定文件类型搜索的能力。你想要一个快到可以交互式运行而无需等待的工具。

## 何时不用

- **如果你需要跨行搜索复杂的多行模式**——ripgrep 的设计面向行。虽然它有多行模式（`-U`），但对复杂跨行匹配不如 `pcregrep` 或 `ack` 自然。
- **如果你需要在二进制文件内搜索**——ripgrep 默认跳过二进制文件。如需在编译二进制或图像内搜索，请用 `grep` 或 `strings`。
- **如果你在无法安装新二进制文件的系统上**——ripgrep 不像 `grep` 那样普遍预装。在最小容器或受限系统上，`grep` 可能是唯一选择。
- **如果你需要 POSIX 标准工具**——`grep` 是 POSIX 标准，保证存在于每个 Unix 系统。ripgrep 是现代替代，但不是可移植标准。
- **如果你需要搜索压缩文件**——ripgrep 默认不搜索 `.gz`、`.zip` 或 `.tar` 归档内部。请用 `zgrep` 或带适当插件的 `ag`。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| grep | 未收录 | 标准 POSIX 搜索工具，到处可用。 | grep 通用且标准，但更慢、更 noisy；ripgrep 更快、更智能，默认遵守 gitignore。 |
| The Silver Searcher (ag) | 未收录 | 用 C 编写、支持 gitignore 的快速 grep 替代。 | ag 成熟且快；ripgrep 通常更快，Unicode 支持更好，维护更活跃。 |
| ack | 未收录 | 面向程序员优化的基于 Perl 的搜索工具。 | ack 更慢且需要 Perl；ripgrep 更快、Rust 原生，平台支持更广。 |
| git grep | 未收录 | 使用 git 自身索引在跟踪文件中搜索。 | git grep 对跟踪文件很快，但只在 Git 仓库内工作；ripgrep 随处可用，也搜索未跟踪文件。 |

## 技术栈

- **Rust**——主要实现语言，追求性能与安全
- **regex crate**——Rust 标准正则引擎，带 SIMD 优化
- **内存映射 I/O**——在受支持平台上高效读取文件

## 依赖

- 受支持的平台（Windows、macOS、Linux；x86_64、ARM64 等）
- 无运行时依赖——自包含静态二进制
- 可选：PCRE2 支持高级正则特性（若启用 PCRE2 编译，则需要 PCRE2 库）

## 运维难度

**无**。ripgrep 是单一静态二进制。通过包管理器安装、release 下载或 `cargo install` 即可。无需配置、无需守护进程、无需维护。

## 健康度与可持续性

- **维护**：活跃且稳定——定期发布，issue 跟踪管理良好。作者（BurntSushi）响应极快，对范围把控严格。
- **治理**：主要由 Andrew Gallant（BurntSushi）维护，Rust 社区中备受尊敬的成员。这是一个单人维护项目，但长期可靠性记录出色。
- **背书**：无企业背书——这是个人开源项目。维护者通过社区 goodwill 与偶尔赞助，已持续多年。
- **采用**：极其广泛——默认预装于许多开发者环境，被主流框架推荐，在全球 CI 流水线中使用。66k star、2.6k fork。
- **长期性**：约 10 年（2016 年创建）。持续维护，无断档。强劲的 Lindy 信号——一个单人维护项目，比许多资金充裕的替代品活得更久。
- **风险旗标**：MIT 或 Unlicense 双许可——两者都宽松且安全。单人维护的 bus factor 是顾虑，但代码库已成熟，维护者已证明长期承诺。无 relicense 风险。

## 存疑（未验证）

- [未验证] 与 grep 和 ag 的确切性能对比取决于具体查询、文件系统和硬件；基准测试会有差异。
- [未验证] PCRE2 支持是可选编译时特性；预编译二进制是否包含它取决于具体 release。
