---
name: OpenCode
slug: opencode
repo: https://github.com/anomalyco/opencode
category: agent-frameworks
tags: [coding-agent, ai-agent, terminal, cli, typescript]
language: TypeScript
license: MIT
maturity: v0.x, active, 181k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T09:44:42Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:35:03Z
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: "@opencode-ai/cli-darwin-arm64"
        dependent_repos_count: 0
        downloads_last_month: 127913
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
    longevity:
      grade: C
      raw:
        repo_age_days: 428
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 475
        top1_share: 0.161
        top3_share: 0.451
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
---

# OpenCode

An open-source AI coding agent that runs in your terminal, edits files, executes commands, and works with your existing codebase. Install it via npm as `opencode-ai`.

![OpenCode — health radar](../../assets/health/opencode.svg)

## When to use

You're a developer who wants an AI coding agent you can run locally in your terminal, audit its source code, and extend when needed. You've outgrown copy-pasting into chat UIs and want the agent to read your project files, suggest edits across multiple files, run tests, and iterate on its own errors. You install OpenCode via npm (`npm install opencode-ai`), connect your LLM API key, and point it at a repo — it acts as a pair programmer that lives in your shell and understands your codebase context.

## When NOT to use

- **Non-technical users or terminal-averse teams** — OpenCode is a CLI-first tool. If your team lives in IDEs or web UIs and doesn't want to learn terminal commands, this is the wrong fit.
- **Enterprise compliance needs** — No built-in audit logs, RBAC, or admin dashboards. It's a personal developer tool, not a governed team platform.
- **Zero-setup SaaS preference** — You must bring your own LLM API key and manage a local Node.js runtime. There is no managed cloud offering.
- **Non-coding tasks** — OpenCode is purpose-built for software engineering workflows, not general chat, data analysis, or document generation.
- **Heavy IDE integration** — It does not ship as a VS Code or JetBrains extension. If you want in-IDE AI completion, look at Kilo Code or Copilot.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Open Interpreter](open-interpreter.md) | ✅ | Terminal coding agent with swappable harnesses for open models. | Open Interpreter is a Rust rewrite with OS sandbox execution; OpenCode is TypeScript/npm-based and younger. |
| [Hermes Agent](hermes-agent.md) | ✅ | Self-improving AI agent with a learning loop from Nous Research. | Hermes focuses on skill creation and personal growth across sessions; OpenCode is a focused coding agent. |
| [AutoGPT](autogpt.md) | ✅ | Platform for autonomous workflow automation. | AutoGPT targets complex multi-step autonomous tasks; OpenCode is a terminal pair-programmer for code. |
| Claude Code | 未收录 | Closed-source terminal coding agent from Anthropic. | Proprietary, no source access, subscription-bound; OpenCode is open-source and BYOK. |
| Gemini CLI | 未收录 | Google's open-source terminal AI agent. | Apache-2.0, backed by Google; OpenCode is MIT and community-driven. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — runtime environment
- **npm** — distribution via `npm install opencode-ai`
- **Monorepo** — packages for console app and core logic

## Dependencies

- **Node.js** runtime (check package requirements for version)
- **LLM API key** — OpenAI, Anthropic, or compatible provider
- **Terminal / shell** — primary interaction surface
- **Git** — for working with repositories

## Ops difficulty

**Low**. Installation is `npm install -g opencode-ai` or similar; the agent runs as a local process with no persistent service to manage. The ongoing burden is API key rotation and keeping the npm package updated.

## Health & viability

- **Maintenance**: Grade A — pushed daily as of 2026-07, with 13 active weeks out of 13. The 7,113 open issues indicate high community engagement.
- **Governance**: Grade A — owned by the `anomalyco` organization, with 475 active maintainers in the past 12 months. The top maintainer holds only 16.1% of commits and the top three hold 45.1%, indicating a well-distributed core team.
- **Longevity**: Grade C — 428 days old (created 2025-04). No Lindy track record; the project is young but has been active for over a year.
- **Adoption**: Grade C — 181k GitHub stars and 127k monthly npm downloads. The volume tier is C and graph tier is E, suggesting the project is still in early adoption.
- **Risk flags**: The project is extremely young with no proven Lindy track record. MIT license is clean, but the velocity of a v0.x project this young means breaking changes should be expected.

## Caveats (unverified)

- [推断] 181k GitHub stars on a repo created in April 2025 may be inflated by hype rather than organic production adoption.
- [未验证] The exact npm package name and installation path may change as the project is still in v0.x.
- [未验证] Multi-language README support (18+ languages listed) suggests global ambition, but the depth of non-English documentation quality is unverified.
- [未验证] The relationship between `anomalyco` and any commercial entity or monetization plan is not publicly documented.
