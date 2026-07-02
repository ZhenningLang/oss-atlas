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

A personal AI assistant you run on your own devices. It answers you on the messaging channels you already use — WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, WeChat, QQ, and WebChat — and can speak and listen on macOS, iOS, and Android with a live Canvas you control.

![OpenClaw — health radar](../../assets/health/openclaw.svg)

## When to use

You're a privacy-conscious professional who wants a single AI assistant that follows you across all your devices and messaging apps. You don't want to trust cloud-only services with your conversations, and you need the assistant to be reachable on WhatsApp, Telegram, Slack, Discord, iMessage, WeChat, and more without switching between different bots. You install OpenClaw on your own hardware, connect it to your preferred LLM provider, and it becomes a persistent personal agent that answers you on the channels you already use.

## When NOT to use

- **Multi-user or team scenarios** — OpenClaw is designed as a single-user personal assistant. There is no RBAC, team workspace, or shared admin dashboard.
- **Zero-setup SaaS preference** — Self-hosting requires managing a Node.js runtime, LLM API credentials, and per-channel configuration. There is no managed cloud option.
- **Enterprise compliance needs** — No audit logs, enterprise SSO, or formal security certifications. This is a personal tool, not a governed enterprise platform.
- **Coding-specific agent work** — OpenClaw is a general-purpose conversational assistant. For software engineering tasks like code generation and refactoring, use Claude Code, OpenCode, or Open Interpreter.

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
- **Node.js** — runtime for the gateway and control plane
- **Cross-platform** — macOS, iOS, Android, and server OS support

## Dependencies

- An LLM provider (OpenAI API, Anthropic API, or a local model endpoint)
- Node.js runtime for the gateway
- A device or server to host the assistant

## Ops difficulty

**Low**. The gateway is a single control plane; installation is straightforward for users comfortable with running Node.js apps. The main ongoing burden is configuring messaging channels and rotating LLM credentials.

## Health & viability

- **Maintenance**: Grade A — pushed daily as of 2026-07, with 13 active weeks out of 13 and a large open-issue volume (6,749) indicating engaged community.
- **Governance**: Grade B — owned by the OpenClaw organization with 487 active maintainers in the past 12 months. The top maintainer holds 52.8% of commits, which is a concentration risk.
- **Longevity**: Grade C — only 220 days old (created 2025-11). No Lindy track record; the project is extremely young despite its high visibility.
- **Adoption**: Grade A — 381k GitHub stars and 14.3M monthly npm downloads per the health radar.
- **Risk flags**: GitHub metadata shows `NOASSERTION` license while the README displays an MIT badge — a discrepancy that needs clarification before commercial use.

## Caveats (unverified)

- [未验证] The `NOASSERTION` license in GitHub metadata may differ from the MIT badge shown in the README; verify before commercial use.
- [推断] With 381k stars on a repo created in late 2025, the star count may be inflated by hype rather than organic production adoption.
- [未验证] The "20+ messaging channels" list includes platforms like WeChat and QQ that may have unstable or unofficial integration APIs.
- [推断] The health radar shows volume tier A but graph tier E, which may indicate most npm downloads are direct installs rather than transitive dependencies, suggesting individual exploration rather than embedded production use.
