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

# AutoGPT

A platform to create, deploy, and manage continuous AI agents that automate complex workflows — self-host for free or join the cloud-hosted beta.

![AutoGPT — health radar](../../assets/health/autogpt.svg)

## When to use

You're a developer or team that needs to automate complex, multi-step tasks with AI agents that run continuously without human intervention. You want to build agents that can research topics, write code, manage files, and interact with APIs on a schedule. You need the flexibility to self-host for free on your own infrastructure, or you want a managed cloud option. AutoGPT provides a full platform with a web UI for building and monitoring agents, rather than just a library.

## When NOT to use

- **If you need a simple, reliable script** — AutoGPT agents are non-deterministic and can fail or loop unexpectedly. For deterministic automation, use traditional scripting or workflow tools.
- **If you need low-resource edge deployment** — Minimum requirements are 4 CPU cores and 8GB RAM; the platform is not lightweight.
- **If you need a coding-specific agent** — AutoGPT is a general-purpose autonomous agent platform; for software engineering, use Claude Code, Open Interpreter, or Kilo Code.
- **If you need enterprise support guarantees** — Significant Gravitas is a community organization, not an enterprise vendor. There is no SLA or formal support.
- **If you want a mature, stable API** — The platform is still evolving rapidly; the cloud-hosted beta is not yet publicly available.

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
- **FastAPI** — backend API framework (inferred)
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

- **Maintenance**: Active — pushed daily as of 2026-07, 185k stars, 454 open issues. The project has been through significant pivots since its 2023 launch.
- **Governance**: Owned by Significant Gravitas, a community organization. Bus factor is unclear.
- **Backing**: No major corporate backing; funded by community donations and a waitlist for cloud hosting.
- **Adoption**: Very high star count (185k) but created in 2023, so only ~3 years old. The project had a famous hype cycle in 2023 and has since pivoted toward a platform model.
- **Longevity**: ~3 years old with active maintenance, but the project's direction has shifted significantly from the original "autonomous GPT" demo to a full platform.
- **Risk flags**: The project has no declared license (`NOASSERTION`), which is a legal risk for commercial use. The cloud-hosted offering is still in closed beta. The original hype-driven growth may not reflect sustained production use.

## Caveats (unverified)

- [未验证] The repository has no declared license (`NOASSERTION`), which creates legal uncertainty for commercial use or redistribution.
- [未验证] The cloud-hosted beta waitlist has been open for an extended period; the public release timeline is unclear.
- [推断] The 185k star count was largely driven by the 2023 hype cycle around "autonomous GPT"; current production adoption may be significantly lower than the star count suggests.
- [未验证] The hardware requirements (4+ cores, 16GB RAM recommended) are for the full platform; lighter usage may be possible but is not officially documented.
