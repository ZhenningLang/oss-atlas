---
name: Warp
slug: warp
repo: https://github.com/warpdotdev/warp
homepage: https://www.warp.dev
category: terminal-ui
tags: [terminal, ai-agent, coding-environment, rust, modern-shell]
language: Rust
license: AGPL-3.0
maturity: active, ~62k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T06:16:34Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: B
  overall_score: 3.0
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
        stars: 62664
    longevity:
      grade: C
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: C
      raw:
        spdx_id: AGPL-3.0
        permissiveness: copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Warp

A modern terminal built for coding with agents — **note: this GitHub repository is issues-only; the product itself is proprietary closed-source software.**

![Warp — health radar](../../assets/health/warp.svg)

## When to use

You're a developer who spends most of your day in a terminal and wants a modern, fast, IDE-like experience for the command line. You want features like command blocks (so you can navigate output like a document), AI-assisted command suggestions, and integrated coding agents. You use macOS or Linux and want a terminal that feels like it was built in 2026, not 1986. You install Warp, and it replaces your default terminal with a GPU-accelerated, Rust-powered shell that supports bash, zsh, and fish, with built-in AI agent "Oz" that can help write and debug commands, or you can run external CLI coding agents like Claude Code, Codex, or Gemini CLI inside it.

## When NOT to use

- **You require fully open-source software.** The GitHub repo is an issue tracker only. Warp's actual source code is proprietary and closed. The AGPL-3.0 license on the repo applies to the minimal issue-tracker code, not the product. If you need a terminal you can audit, modify, or self-host, choose Alacritty, iTerm2, or Tabby instead. [推断]
- **You need a lightweight, minimal terminal.** Warp is a feature-rich, Rust-based application with AI integrations, cloud features, and modern UI. If you want a 10MB terminal that starts in 50ms, this is not it.
- **You are on Windows.** As of mid-2026, Warp's primary support is macOS and Linux; Windows support is limited or unavailable. [未验证]
- **You don't want AI features or cloud connectivity.** Warp's value proposition is tightly coupled with AI assistance and cloud-backed features (collaboration, drive, etc.). If you want a terminal with zero network calls and no AI, traditional terminals are a better fit.
- **You need a terminal for remote/headless servers over SSH.** Warp's advanced features (blocks, AI, etc.) may not work well or at all in a plain SSH session; it's designed for local interactive use. [推断]
- **You object to proprietary telemetry or cloud accounts.** Warp requires a login for some features and is a closed-source product; you cannot fully audit what data is collected. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Alacritty | 未收录 | A fast, cross-platform, OpenGL terminal emulator — fully open source. | Fully open source and minimal, but no native AI features, no command blocks, and no built-in shell intelligence. |
| iTerm2 | 未收录 | The most popular macOS terminal with deep macOS integration. | macOS-only, not open source, but mature and feature-rich without the AI-centric design of Warp. |
| Tabby | 未收录 | A modern, open-source terminal with SSH client and serial support. | Open source and cross-platform, with some modern UI features, but less AI-native than Warp. |
| [asciimatics](asciimatics.md) | ✅ | A Python TUI library for building terminal UIs, not a terminal emulator. | This is a library for building TUIs, not a standalone terminal app — different category. |

## Tech stack

- **Rust** — the core terminal and rendering engine.
- **WASM** — used for some internal components and extensions.
- **GPU acceleration** — modern rendering pipeline for smooth scrolling and blocks.
- **Proprietary codebase** — the actual source is not open; the GitHub repo is an issue tracker only.

## Dependencies

- **Operating system:** macOS or Linux (primary platforms).
- **The Warp application:** downloaded from the official website or package manager.
- **Shell:** bash, zsh, or fish.
- **Optional:** LLM API keys if you want to use external coding agents inside Warp.
- **Account:** some features require a Warp account (free tier available).

## Ops difficulty

**Low.** Warp is an end-user desktop application. You download it, install it, and use it. The operational complexity is the same as any other desktop app: keeping it updated, managing any account/login requirements, and understanding that it's a closed-source product that receives updates on Warp's schedule (weekly, typically Thursdays). There is no server to run, no database to manage, and no self-hosting burden.

## Health & viability

- **Maintenance — active product development, but closed source.** Weekly releases (typically Thursdays) are claimed by the team. The GitHub repo receives frequent issue and feature-request activity, but this is not a proxy for code commits since the repo is issues-only. [推断]
- **Governance — vendor-controlled, single company.** Warp is a venture-backed company (Warp.dev) that owns the product entirely. The roadmap is decided by the company, not a community. The GitHub repo exists for transparency on issues, not for community governance. [推断]
- **Age & Lindy — ~4 years old, still evolving.** Created 2021-07. Four years is a moderate age for a dev tool; the terminal space is conservative, so a new entrant needs to keep proving itself. The "agentic terminal" angle is a recent pivot and its durability is unproven. [推断]
- **Adoption & ecosystem — growing mindshare, closed ecosystem.** ~62k stars on the issues-only repo signals strong interest. The ecosystem is limited by the closed-source nature — no plugins, no community forks, no independent audits. [未验证]
- **Risk flags — proprietary, closed-source, AGPL-3.0 on a repo that is not the product.** The AGPL-3.0 license on the issues-only repo is misleading if you expect it to cover the terminal. The company's ability to change pricing, terms, or discontinue features is unchecked by an open-source license. The "agentic" feature pivot is recent and may shift the product's focus. [推断]

## Caveats (unverified)

- [未验证] Repo facts as of 2026-07-01 via GitHub API: created 2021-07-08, last push 2026-07-01, not archived, ~62.7k stars, ~5.1k forks, AGPL-3.0, language reported as Rust, owner type Organization.
- [推断] The GitHub repository is explicitly described as "issues-only" in the README; the actual product is proprietary closed-source software. The AGPL-3.0 license applies only to the issue-tracker code.
- [未验证] Platform support claims (macOS, Linux) and Windows limitations are from the README and website; verify current availability for your OS.
- [未验证] "Weekly releases, typically on Thursdays" and the feature list (AI agent Oz, command blocks, Warp Drive, etc.) are from the README; actual release cadence and feature stability are not independently verified.
- [推断] The requirement for a Warp account and any telemetry/cloud data practices are based on the closed-source nature of the product and common patterns for similar tools; the exact data handling cannot be audited without source access.
- [未验证] Star count on an issues-only repo may reflect product interest rather than code quality or community contribution, since no code contributions are accepted.
