---
name: OpenClaw
slug: openclaw
repo: https://github.com/openclaw/openclaw
category: agent-frameworks
tags: [personal-ai, assistant, multi-channel, self-hosted]
language: TypeScript
license: MIT
maturity: v0.x, active, 381k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-01T10:37:46Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:42:43Z
  overall: B
  overall_score: 3.25
  scored_axes: 4
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
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: openclaw
        dependent_repos_count: 0
        downloads_last_month: 14326323
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: C
      raw:
        repo_age_days: 220
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 487
        top1_share: 0.528
        top3_share: 0.753
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    risk_license: { reason: license_unparsed }
---

# OpenClaw

A personal AI assistant that runs on your own devices and answers you across 20+ messaging channels — the "lobster way" of owning your data.

![OpenClaw — health radar](../../assets/health/openclaw.svg)

## When to use

You're a privacy-conscious professional who wants a single AI assistant that follows you across all your devices and messaging apps. You don't want to trust cloud-only services with your conversations, and you need the assistant to be reachable on WhatsApp, Telegram, Slack, Discord, iMessage, WeChat, and more without switching between different bots. You install OpenClaw on your own hardware, connect it to your preferred LLM provider, and it becomes a persistent personal agent that answers you on the channels you already use.

## When NOT to use

- **Multi-user or team scenarios** — OpenClaw is designed as a single-user personal assistant, not a team-shared platform with RBAC.
- **Zero-setup SaaS preference** — Self-hosting requires managing Node.js runtime, LLM credentials, and channel configurations.
- **Enterprise compliance needs** — No admin dashboards, audit logs, or enterprise SSO; this is a personal tool.
- **Coding-specific agent work** — OpenClaw is a general-purpose conversational assistant, not a software development agent like Codex or Claude Code.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Hermes Agent](hermes-agent.md) | ✅ | Similar personal-agent angle with a learning loop. | Hermes has built-in self-improvement and skill creation; OpenClaw focuses on multi-channel ubiquity. |
| [AutoGPT](autogpt.md) | ✅ | Complex workflow-automation platform. | AutoGPT targets autonomous task execution and deployment; OpenClaw is a conversational assistant. |
| [Open Interpreter](open-interpreter.md) | ✅ | Terminal-first coding agent with swappable harnesses. | Open Interpreter is for coding in the terminal; OpenClaw is a chatbot across messaging apps. |
| LangChain | 未收录 | Lower-level library for building custom agents. | LangChain is a framework to build from scratch; OpenClaw is a ready-to-run personal assistant. |
| Claude / ChatGPT native apps | 未收录 | Closed-source cloud-only assistants. | Proprietary and require internet; OpenClaw is self-hosted and channel-agnostic. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — runtime for the gateway/control plane
- **Cross-platform** — macOS, iOS, Android, and server OS support

## Dependencies

- An LLM provider (OpenAI API, Anthropic API, or a local model endpoint)
- Node.js runtime for the gateway
- A device or server to host the assistant

## Ops difficulty

**Low**. The gateway is a single control plane; installation is straightforward for users comfortable with running Node.js apps. The main ongoing burden is configuring messaging channels and rotating LLM credentials.

## Health & viability

- **Maintenance**: Very active — pushed daily as of 2026-07, with a large open-issue volume (6,749) indicating engaged community.
- **Governance**: Owned by the OpenClaw organization; reasonable bus factor but the project is young (created 2025-11).
- **Backing**: No major corporate backing visible; community-driven with an active Discord.
- **Adoption**: Extremely high star count (381k) but very young (under 8 months). The star count signals hype rather than proven longevity.
- **Risk flags**: The project is extremely young with no Lindy track record. The `NOASSERTION` license metadata vs MIT badge on README needs clarification. [未验证]

## Caveats (unverified)

- [未验证] The `NOASSERTION` license in GitHub metadata may differ from the MIT badge shown in the README; verify before commercial use.
- [推断] With 381k stars on a repo created in late 2025, the star count may be inflated by hype rather than organic production adoption.
- [未验证] The "20+ messaging channels" list includes platforms like WeChat and QQ that may have unstable or unofficial integration APIs.
