---
name: Bun
slug: bun
repo: https://github.com/oven-sh/bun
category: dev-utilities
tags: [javascript, typescript, runtime, bundler, test-runner, package-manager]
language: Rust
license: NOASSERTION
maturity: v1.x, stable, 93.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T10:36:14Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:43:05Z
  overall: A
  overall_score: 4.0
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.2
        qualifying_issues: 46
        band: relaxed_solo
        window_offset_days: 0
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: bun-types
        dependent_repos_count: 3705
        downloads_last_month: 29288304
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.28
    longevity:
      grade: A
      raw:
        repo_age_days: 1905
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 65
        top1_share: 0.36
        top3_share: 0.73
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Bun

An incredibly fast all-in-one toolkit for JavaScript and TypeScript apps — runtime, bundler, test runner, and package manager in a single binary.

![Bun — health radar](../../assets/health/bun.svg)

## When to use

You're building a JavaScript or TypeScript application and you're frustrated with the sprawl of Node.js tooling: one tool for the runtime, another for bundling, another for testing, and yet another for package management. You want a single, fast binary that handles everything. You run `bun run` to execute TypeScript without pre-compilation, `bun test` for built-in testing, `bun build` for bundling, and `bun install` for dependency management — all significantly faster than their Node.js equivalents. You also value the JavaScriptCore engine's fast startup times and lower memory footprint compared to V8-based alternatives.

## When NOT to use

- **You rely on native Node.js addons or complex C++ bindings.** Bun aims for Node.js compatibility, but some native modules and `node-gyp` dependencies may not work without modification.
- **You need mature ecosystem tooling.** Bun is younger than Node.js and Deno; some npm packages, especially those with post-install scripts or deep Node.js internals, may behave unexpectedly.
- **You require a fully governed open-source license.** Bun is released under a custom license (NOASSERTION), not a standard OSI-approved license like MIT or Apache-2.0. Verify compliance before commercial use.
- **You are already deeply invested in Node.js tooling.** If your CI/CD, Docker images, and team expertise are all Node-native, the migration cost may outweigh the performance gains.
- **You need WebAssembly-first runtime.** While Bun supports Wasm, Deno has stronger WebAssembly integration and first-class Wasm module support.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Node.js | 未收录 | The incumbent JS/TS runtime with the largest ecosystem. | Node.js has the deepest ecosystem and broadest hosting support; Bun is faster but younger and less proven. |
| [Deno](deno.md) | ✅ | Modern JS/TS runtime with secure defaults and built-in toolchain. | Deno is more mature and has a standard OSI license; Bun is faster and bundles more tools, but its license is ambiguous. |
| [Tauri](tauri.md) | ✅ | Not a runtime comparison, but both are Rust-based dev tools. | Tauri builds desktop apps; Bun runs JS/TS. Complementary, not competing. |
| pnpm / Yarn | 未收录 | Dedicated package managers with mature workspaces. | pnpm and Yarn have deep workspace and monorepo features; Bun's package manager is fast but may lack some advanced features. |

## Tech stack

- **Rust** — core runtime and bundler implementation
- **JavaScriptCore (JSC)** — JavaScript engine powering Bun, known for fast startup
- **TypeScript** — first-class language support (transpiled internally)
- **Zig** — parts of the low-level system implementation
- **SQLite** — embedded for package management metadata

## Dependencies

- Bun binary (single executable, no external runtime needed)
- macOS, Linux, or Windows (x64/ARM64)
- For npm compatibility: existing `package.json` and `node_modules` can be used
- No backend or database server required for typical usage

## Ops difficulty

**Low.** Bun is a single binary installed via shell script, npm, or package manager. There is no server to maintain. The operational burden is in keeping the binary updated and verifying npm compatibility for your specific dependency tree. For CI/CD, replacing `node` with `bun` is usually straightforward, but test for edge cases in native modules.

## Health & viability

- **Maintenance**: Active — pushed daily as of 2026-07, with frequent releases and a responsive issue tracker (6,817 open issues). [推断]
- **Governance**: Owned by the `oven-sh` organization, with Jarred Sumner as the visible lead and a growing team of contributors. The bus factor is improving but still centered on a small core team.
- **Backing**: Backed by Oven (the company), which has raised venture funding. The commercial model and long-term roadmap are not fully transparent. [未验证]
- **Adoption**: Strong adoption with ~93.5k stars and ~4,742 forks, created in 2021 (5-year track record). Used in production by teams seeking faster build times. [推断]
- **Risk flags**: The license is NOASSERTION (not a standard OSI license), which introduces legal uncertainty for commercial redistribution. The venture-backed model may lead to open-core gating or license changes in the future. [推断]

## Caveats (unverified)

- [未验证] Bun's exact license terms are ambiguous; it is not tagged with a standard SPDX license and may have usage restrictions for commercial or embedded deployments.
- [推断] Native Node.js addon compatibility is improving but may still break with complex `node-gyp` dependencies.
- [未验证] The exact number of production deployments and enterprise users has not been verified from primary sources.
- [推断] Oven's venture funding and business model may influence the open-source roadmap; monitor for commercial-tier features or relicensing.
