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
  computed_at: 2026-07-02T08:32:19Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 87.1
        qualifying_issues: 18
        band: relaxed_solo
        window_offset_days: 8
    adoption:
      grade: D
      raw:
        registry: conda-forge.org
        canonical_package: ripgrep
        dependent_repos_count: 86
        downloads_last_month: 13080989
        graph_tier: D
        volume_tier: "?"
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 3765
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 9
        top1_share: 0.892
        top3_share: 0.931
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Unlicense
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# ripgrep

面向行的搜索工具，递归搜索目录中的正则模式，默认自动遵守 gitignore 规则并跳过隐藏文件与二进制文件。

![ripgrep — 健康度雷达](../../assets/health/ripgrep.zh.svg)

## 何时使用

你正在选择日常代码搜索工具，需要在大型代码库中快速、智能地搜索。你选 ripgrep 而不是 `grep`，因为想要一个默认自动遵守 `.gitignore`、跳过隐藏文件和二进制文件的工具，且在 Windows、macOS 和 Linux 上行为一致，每次发布都带预编译二进制。你选 ripgrep 而不是 The Silver Searcher（ag），因为 ripgrep 通常更快、Unicode 支持更好、维护更活跃。你需要支持 Unicode 的正则搜索、可选的多行匹配，以及按特定文件类型搜索的能力——全部快到可以交互式运行而无需等待。

## 何时不用

- 如果你需要跨行搜索复杂的多行模式，请使用 `pcregrep` 或 `ack` 而不是 ripgrep，因为 ripgrep 的设计面向行，其多行模式（`-U`）对复杂跨行匹配不如前者自然。
- 如果你需要在二进制文件内搜索，请使用 `grep` 或 `strings` 而不是 ripgrep，因为 ripgrep 默认跳过二进制文件。
- 如果你在无法安装新二进制文件的系统上工作，请使用 `grep` 而不是 ripgrep，因为 ripgrep 不像 `grep` 那样普遍预装，在最小容器或受限系统上 `grep` 可能是唯一选择。
- 如果你需要 POSIX 标准工具，保证存在于每个 Unix 系统，请使用 `grep` 而不是 ripgrep，因为 ripgrep 是现代替代，但不是可移植标准。
- 如果你需要搜索压缩文件（`.gz`、`.zip`、`.tar`），请使用 `zgrep` 或带适当插件的 `ag` 而不是 ripgrep，因为 ripgrep 默认不搜索归档内部。

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
