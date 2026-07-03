---
name: Clash Verge Rev
slug: clash-verge-rev
repo: https://github.com/clash-verge-rev/clash-verge-rev
category: dev-utilities
tags: [proxy, clash, gui, tauri, cross-platform]
language: TypeScript
license: GPL-3.0
maturity: v1.x, active, 129k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T03:54:53Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T11:22:04Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.8
        qualifying_issues: 29
        band: relaxed_solo
        window_offset_days: 8
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 955
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 50
        top1_share: 0.536
        top3_share: 0.861
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: C
      raw:
        spdx_id: GPL-3.0
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: ambiguous }
---

# Clash Verge Rev

A modern cross-platform GUI proxy client based on Tauri, running on Windows, macOS, and Linux with the built-in mihomo (Clash Meta) kernel.

![Clash Verge Rev — health radar](../../assets/health/clash-verge-rev.svg)

## When to use

You're a developer or power user who needs a flexible, rule-based proxy client on your desktop. You've considered the original Clash for Windows, but that project is archived and no longer maintained. You manage multiple proxy subscriptions and want a clean, modern GUI to switch between them, edit rules, and monitor traffic. You need system-level proxy integration (system proxy and TUN mode) and want to run the mihomo kernel without command-line configuration. You reach for Clash Verge Rev because it is the actively maintained continuation of the Clash Verge project, built with Rust/Tauri for a native-feeling desktop app rather than an Electron-based alternative. Pick Clash Verge Rev over ClashX or ClashX Pro when you need a cross-platform client for Windows, macOS, and Linux rather than a macOS-only solution; pick it over sing-box when you want deeper Clash ecosystem compatibility and familiar rule syntax rather than a next-gen protocol-flexible platform.


## When NOT to use

- **Mobile-only users.** If you need an iOS or Android proxy client, use Shadowrocket or Surge instead of Clash Verge Rev, because this is a desktop-only application.
- **Simple one-proxy setups.** If you only need a single proxy and never switch rules, use the mihomo CLI directly or v2rayN instead of Clash Verge Rev, because the GUI overhead is unnecessary for a static configuration.
- **Enterprise MDM environments.** If you need a proxy client for corporate deployment with a permissive license, use sing-box or v2rayN instead of Clash Verge Rev, because GPL-3.0 copyleft may conflict with corporate software distribution policies. [未验证]
- **Users unfamiliar with proxy concepts.** If you want a beginner-friendly proxy with guided setup, use a commercial client like Surge instead of Clash Verge Rev, because the app assumes knowledge of Clash rules, proxy groups, and subscription URLs.


## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Clash for Windows | 未收录 | The original Windows Clash GUI (archived). | The original Clash for Windows project is archived; Clash Verge Rev is the active continuation with a modern Tauri stack. |
| ClashX / ClashX Pro | 未收录 | macOS-native Clash clients. | ClashX is macOS-specific; Clash Verge Rev is cross-platform and actively maintained. |
| Shadowrocket / Surge | 未收录 | Commercial proxy clients. | Shadowrocket (iOS) and Surge (macOS/iOS) are paid, closed-source apps with broader platform support. |
| sing-box | 未收录 | Next-gen proxy platform with a GUI. | sing-box is more protocol-flexible but Clash Verge Rev has deeper Clash ecosystem compatibility. |
| Proxifier | 未收录 | Commercial per-app proxy routing. | Proxifier is a paid tool for routing specific apps; Clash Verge Rev is a system-level proxy client with rule-based routing. |

## Tech stack

- **TypeScript** — frontend UI logic
- **Rust** — Tauri runtime and system integration
- **Tauri 2** — cross-platform desktop framework
- **mihomo (Clash Meta)** — built-in proxy kernel

## Dependencies

- Windows (x64/x86), Linux (x64/arm64), or macOS 11+ (Intel/Apple Silicon)
- No server infrastructure required; runs entirely on the local machine
- Optional: WebDav for configuration backup and sync

## Ops difficulty

**Low**. It is a desktop application with an installer. The main ongoing tasks are updating the app, updating the built-in kernel, and managing subscription URLs. No server or network infrastructure is required.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Grade A — median first-response time 0.8 hours across 33 qualifying issues/PRs.
- **Adoption**: Cannot be scored — unknown.
- **Longevity**: Grade B — 954 days old.
- **Governance**: Grade B — top-3 contributor share 86.1% (?).
- **Risk / License**: Grade C — GPL-3.0 license.
## Caveats (unverified)

- [未验证] The original Clash project and its Windows GUI were archived; the long-term stability of this continuation fork depends on ongoing community support.
- [未验证] The regulatory environment around proxy tools in certain jurisdictions may affect project availability and updates.
- [未验证] The GPL-3.0 license terms may conflict with enterprise software distribution policies; verify before corporate deployment.
