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
  computed_at: 2026-07-02T12:56:32Z
  overall: "?"
  overall_score: null
  scored_axes: 1
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
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
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    maintenance: { reason: recency_unreadable }
    responsiveness: { reason: no_traffic }
    longevity: { reason: not_found }
    governance: { reason: empty_or_gated }
    risk_license: { reason: repo_unreachable }
---

# ripgrep

A line-oriented search tool that recursively searches directories for a regex pattern while automatically respecting gitignore rules and skipping hidden files and binary files by default.

![ripgrep — health radar](../../assets/health/ripgrep.svg)

## When to use

You're choosing a code search tool for daily use across large codebases and speed and smart defaults matter. You pick ripgrep over `grep` because you want a tool that automatically respects `.gitignore`, skips hidden files and binary files, and works identically on Windows, macOS, and Linux with prebuilt binaries for every release. You pick ripgrep over The Silver Searcher (ag) because ripgrep is generally faster, has better Unicode support, and more active maintenance. You need Unicode-aware regex search, optional multiline matching, and the ability to search specific file types — all fast enough to run interactively without waiting.

## When NOT to use

- If you need to search across lines with complex multiline patterns, use `pcregrep` or `ack` instead of ripgrep, because ripgrep is line-oriented by design and its multiline mode (`-U`) is not as natural for complex cross-line matching.
- If you need to search within binary files, use `grep` or `strings` instead of ripgrep, because ripgrep skips binary files by default.
- If you are on a system where you cannot install a new binary, use `grep` instead of ripgrep, because ripgrep is not universally preinstalled like `grep` and on minimal containers or restricted systems `grep` may be your only option.
- If you need a tool that is part of the POSIX standard and guaranteed on every Unix system, use `grep` instead of ripgrep, because ripgrep is a modern replacement but not a portable standard.
- If you need to search compressed files (`.gz`, `.zip`, `.tar`), use `zgrep` or `ag` with appropriate plugins instead of ripgrep, because ripgrep does not search inside archives by default.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| grep | 未收录 | The standard POSIX search utility, available everywhere. | grep is universal and standard but slower and noisier; ripgrep is faster, smarter, and respects gitignore by default. |
| The Silver Searcher (ag) | 未收录 | Fast grep replacement with gitignore support, written in C. | ag is mature and fast; ripgrep is generally faster, has better Unicode support, and more active maintenance. |
| ack | 未收录 | Perl-based search tool optimized for programmers. | ack is slower and requires Perl; ripgrep is faster, Rust-native, and has broader platform support. |
| git grep | 未收录 | Search within tracked files using git's own index. | git grep is fast for tracked files but only works inside Git repos; ripgrep works anywhere and searches untracked files too. |

## Tech stack

- **Rust** — primary implementation language for performance and safety
- **regex crate** — Rust's standard regex engine with SIMD optimizations
- **Memory-mapped I/O** — for efficient file reading on supported platforms

## Dependencies

- A supported platform (Windows, macOS, Linux; x86_64, ARM64, and others)
- No runtime dependencies — self-contained static binary
- Optional: PCRE2 support for advanced regex features (requires PCRE2 library if compiled with it)

## Ops difficulty

**None**. ripgrep is a single static binary. Install via package manager, download from releases, or `cargo install`. No configuration, no daemon, no maintenance.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance**: Active and stable — regular releases, well-managed issue tracker. The author (BurntSushi) is highly responsive and disciplined about scope.
- **Governance**: Primarily maintained by Andrew Gallant (BurntSushi), a respected Rust community member. This is a single-maintainer project with a long track record of reliability.
- **Backing**: No corporate backing — this is a personal open-source project. The maintainer has sustained it for years through community goodwill and occasional sponsorship.
- **Adoption**: Extremely widespread — installed by default in many developer environments, recommended by major frameworks, and used in CI pipelines worldwide. 66k stars, 2.6k forks.
- **Longevity**: ~10 years old (created 2016). Continuously maintained with no gaps. Strong Lindy signal — a single-maintainer project that has outlasted many well-funded alternatives.
- **Risk flags**: Dual-licensed under MIT or Unlicense — both are permissive and safe. The single-maintainer bus factor is a concern, but the codebase is mature and the maintainer has demonstrated long-term commitment. No relicense risk.

## Caveats (unverified)

- [未验证] The exact performance comparison against grep and ag depends on the specific query, filesystem, and hardware; benchmarks vary.
- [未验证] The PCRE2 support is an optional compile-time feature; the prebuilt binaries may or may not include it depending on the release.
