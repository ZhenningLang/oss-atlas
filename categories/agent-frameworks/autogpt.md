---
name: AutoGPT
slug: autogpt
repo: https://github.com/Significant-Gravitas/AutoGPT
category: agent-frameworks
tags: [autonomous-agents, ai, workflow-automation, deployment]
language: Python
license: NOASSERTION
maturity: v0.x, active, 185k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T10:28:49Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:33:02Z
  overall: A
  overall_score: 3.5
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 7
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 48.1
        qualifying_issues: 27
        band: default
        window_offset_days: 5
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 1204
        last_commit_age_days: 7
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 18
        top1_share: 0.292
        top3_share: 0.562
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    adoption: { reason: ambiguous }
    risk_license: { reason: license_unparsed }
---

# AutoGPT

A platform to create, deploy, and manage continuous AI agents that automate complex workflows. You can self-host for free on your own infrastructure, or join the waitlist for the cloud-hosted beta.

![AutoGPT — health radar](../../assets/health/autogpt.svg)

## When to use

You're a developer or team that needs to automate complex, multi-step tasks with AI agents that run continuously without human intervention. You want to build agents that can research topics, write code, manage files, and interact with APIs on a schedule. You need the flexibility to self-host for free on your own infrastructure, or you want a managed cloud option. AutoGPT provides a full platform with a web UI for building and monitoring agents, rather than just a library.

## When NOT to use

- **Simple, reliable scripts** — AutoGPT agents are non-deterministic and can fail or loop unexpectedly. For deterministic automation, use traditional scripting or workflow tools like n8n.
- **Low-resource edge deployment** — The README specifies minimum requirements of 4 CPU cores, 8GB RAM (16GB recommended), and 10GB+ free storage. This is not a lightweight agent.
- **Coding-specific agents** — AutoGPT is a general-purpose autonomous agent platform; for software engineering, use Claude Code, Open Interpreter, or Kilo Code.
- **Enterprise support guarantees** — Significant Gravitas is a community organization, not an enterprise vendor. There is no SLA or formal support contract.
- **Mature, stable API** — The platform is still evolving rapidly; the cloud-hosted beta is not yet publicly available.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Hermes Agent](hermes-agent.md) | ✅ | Self-improving agent with a learning loop. | Hermes focuses on skill evolution and memory; AutoGPT focuses on workflow automation and deployment. |
| [OpenClaw](openclaw.md) | ✅ | Personal multi-channel assistant. | OpenClaw is a conversational assistant; AutoGPT is a task-automation platform. |
| [Open Interpreter](open-interpreter.md) | ✅ | Terminal coding agent for open models. | Open Interpreter is a coding tool; AutoGPT is a general-purpose agent framework. |
| LangChain | 未收录 | Lower-level framework for building agent pipelines. | LangChain is a library; AutoGPT is a higher-level platform with a UI and deployment model. |
| CrewAI | 未收录 | Multi-agent orchestration framework. | CrewAI focuses on multi-agent teams; AutoGPT focuses on single-agent continuous execution. |

## Tech stack

- **Python** — primary implementation language
- **FastAPI** — backend API framework
- **React / Next.js** — web UI for the platform
- **PostgreSQL** — database for agent state and metadata
- **Redis** — caching and message broker

## Dependencies

- **Hardware**: 4+ CPU cores, 8GB RAM minimum (16GB recommended), 10GB+ free storage
- **OS**: Linux (Ubuntu 20.04+ recommended), macOS, or Windows with WSL
- **Database**: PostgreSQL for agent state persistence
- **LLM provider**: OpenAI API or compatible endpoint
- **Docker**: Recommended for deployment

## Ops difficulty

**High**. Self-hosting the AutoGPT platform requires multiple services (backend, frontend, database, Redis), environment configuration, and ongoing monitoring. The system is resource-intensive and agents can fail in unexpected ways, requiring human oversight.

## Health & viability

- **Maintenance**: Grade A — pushed within the past 7 days as of 2026-07, with 13 active weeks out of 13. The 454 open issues suggest a focused, manageable community.
- **Governance**: Grade A — owned by Significant Gravitas, with 18 active maintainers in the past 12 months. The top maintainer holds 29.2% of commits and the top three hold 56.2%, indicating a distributed core team.
- **Longevity**: Grade B — 1,204 days old (created 2023-03), giving it a ~3.3-year track record. The project has pivoted from its original "autonomous GPT" demo to a full platform, demonstrating adaptability but also direction shifts.
- **Adoption**: Grade ? — the health radar could not score adoption due to ambiguous package data. The 185k GitHub stars are high but the project's actual package download footprint is unclear.
- **Risk flags**: The repository has no declared license (`NOASSERTION`), which creates legal uncertainty for commercial use or redistribution. The cloud-hosted beta is still in closed beta with a public release timeline that is not confirmed.

## Caveats (unverified)

- [未验证] The repository has no declared license (`NOASSERTION`), which creates legal uncertainty for commercial use or redistribution.
- [未验证] The cloud-hosted beta waitlist has been open for an extended period; the public release timeline is unclear.
- [推断] The 185k star count was largely driven by the 2023 hype cycle around "autonomous GPT"; current production adoption may be significantly lower than the star count suggests.
- [未验证] The hardware requirements (4+ cores, 16GB RAM recommended) are for the full platform; lighter usage may be possible but is not officially documented.
