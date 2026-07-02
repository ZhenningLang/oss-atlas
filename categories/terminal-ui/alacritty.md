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

# Alacritty

A fast, cross-platform, OpenGL terminal emulator with sensible defaults and extensive configuration, designed to integrate with other applications rather than reimplement their functionality.

![Alacritty — health radar](../../assets/health/alacritty.svg)

## When to use

You're a developer who spends hours in the terminal every day and wants the fastest, most responsive terminal emulator available. You are frustrated with terminal emulators that lag when scrolling through large log files or running `cat` on multi-megabyte outputs. You want a terminal that uses your GPU for rendering, offloading work from the CPU. You prefer a minimal, configurable terminal that does not try to be a window manager or a multiplexer — you already use tmux or screen for that. You want something that works consistently across macOS, Linux, BSD, and Windows with the same configuration file.

## When NOT to use

- **If you need a built-in terminal multiplexer** — Alacritty explicitly does not include tabs, splits, or session management. Use tmux, screen, or Zellij alongside Alacritty, or choose a terminal like WezTerm or iTerm2 that includes these features.
- **If you need ligature support** — Alacritty does not support font ligatures (combining `!=` into a single glyph). Use WezTerm, Kitty, or a patched font if ligatures are essential to your workflow.
- **If you are on a system without OpenGL 3.3+ support** — Alacritty requires a modern GPU and graphics driver. Older systems, some VMs, and remote X11/VNC setups may not work.
- **If you want a terminal with built-in AI or shell integration** — Alacritty is a plain terminal emulator. For AI-powered features, shell suggestions, or smart completions built into the terminal, look at Warp or Fig.
- **If you need a fully stable, 1.0 product** — Alacritty is self-described as beta-level software. While widely used as a daily driver, there are known missing features and bugs.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| WezTerm | 未收录 | Modern GPU-accelerated terminal with tabs, splits, and ligatures. | WezTerm has more built-in features (tabs, ligatures, multiplexing); Alacritty is faster and more minimal. |
| Kitty | 未收录 | GPU-based terminal with advanced features like kittens (plugins) and image support. | Kitty has more features and a plugin system; Alacritty is simpler and more focused on raw performance. |
| iTerm2 | 未收录 | Popular macOS terminal with extensive features and integration. | iTerm2 is macOS-only and feature-rich; Alacritty is cross-platform and minimal. |
| Windows Terminal | 未收录 | Microsoft's modern terminal for Windows with tabs and GPU acceleration. | Windows Terminal is Windows-only and integrates with WSL; Alacritty is cross-platform and simpler. |
| Warp | 未收录 | AI-powered modern terminal with cloud features. | Warp has AI features and modern UI; Alacritty is plain, fast, and fully local. |

## Tech stack

- **Rust** — primary implementation language
- **OpenGL** — GPU-accelerated rendering for smooth scrolling and large output
- **FreeType/FontConfig** — font rendering and configuration (platform-dependent)

## Dependencies

- A modern desktop OS (macOS, Linux, BSD, Windows)
- A GPU with OpenGL 3.3+ support and up-to-date graphics drivers
- A shell of your choice (Alacritty does not bundle one)

## Ops difficulty

**None**. Alacritty is a single binary. Install via package manager or download from releases. Configuration is a single YAML file. No daemon, no background service.

## Health & viability

- **Maintenance**: Active — regular releases, responsive maintainers. 65k stars, 3.5k forks. The project is well-managed with clear issue triage.
- **Governance**: Maintained by the alacritty organization with multiple contributors. The original creator (jwilm) stepped back, but the project has successfully transitioned to community/organization maintenance.
- **Backing**: No corporate backing — a community-driven project under the alacritty GitHub organization. Sustained by volunteer contributions and community goodwill.
- **Adoption**: Very widely adopted among developers who prioritize terminal performance. Often recommended in Rust and developer communities as the default fast terminal.
- **Longevity**: ~10 years old (created 2016). Continuously maintained with no significant gaps. Good Lindy signal for a community project.
- **Risk flags**: Apache-2.0 is safe. No relicense history. The project is conservative about feature creep, which keeps it stable but may frustrate users wanting tabs, ligatures, or built-in multiplexing. The original maintainer transition was handled well.

## Caveats (unverified)

- [未验证] The exact OpenGL version requirement and compatibility with specific GPU drivers on Linux vary by distribution and hardware.
- [未验证] The beta-level readiness claim is self-assessed by the project; many users report stable daily use.
- [推断] As the terminal emulator landscape evolves, Alacritty's minimalism may cause it to lose users to feature-richer alternatives like WezTerm or Warp unless it finds a way to maintain its performance edge.
