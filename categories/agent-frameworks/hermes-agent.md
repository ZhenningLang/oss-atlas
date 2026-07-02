---
name: Hermes Agent
slug: hermes-agent
repo: https://github.com/NousResearch/hermes-agent
category: agent-frameworks
tags: [ai-agent, learning-loop, self-improving, multi-channel]
language: Python
license: MIT
maturity: v0.x, active, 207k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T10:37:26Z
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

# Hermes Agent

The self-improving AI agent built by Nous Research — it creates skills from experience, improves them during use, and builds a deepening model of who you are across sessions.

![Hermes Agent — health radar](../../assets/health/hermes-agent.svg)

## When to use

You're a solo developer or small team running AI agents on a $5 VPS or a GPU cluster, and you need an agent that gets better over time without manual prompt engineering. You want an agent that can search its own past conversations, persist knowledge across sessions, and create new skills from real experience. You also want to talk to it from Telegram while it works on a cloud VM, using any LLM provider you choose. Hermes Agent gives you a learning loop that few other agents offer.

## When NOT to use

- **If you need a deterministic, repeatable system** — The learning loop means behavior changes over time, which can make outputs non-deterministic and harder to debug.
- **If you want a simple, stateless chatbot** — Hermes is overkill for one-off Q&A; the value is in accumulated memory and skill evolution.
- **If you need enterprise security compliance** — Nous Research is an AI research lab, not an enterprise vendor; there are no SOC 2, SSO, or audit-trail guarantees.
- **If you need a coding-only agent** — Hermes is a general-purpose agent framework, not optimized for software engineering tasks like Claude Code or Open Interpreter.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [OpenClaw](openclaw.md) | ✅ | Personal assistant focused on multi-channel ubiquity. | OpenClaw is a ready-to-run assistant; Hermes is a learning framework you extend. |
| [AutoGPT](autogpt.md) | ✅ | Autonomous workflow platform with deployment focus. | AutoGPT targets autonomous task execution; Hermes targets self-improvement through learning. |
| [Open Interpreter](open-interpreter.md) | ✅ | Terminal coding agent tuned for low-cost/open models. | Open Interpreter is for coding; Hermes is a general conversational agent with a learning loop. |
| LangChain | 未收录 | Lower-level library for building custom agent pipelines. | LangChain is a toolkit; Hermes is a higher-level agent with built-in memory and skill synthesis. |
| CrewAI | 未收录 | Multi-agent orchestration framework. | CrewAI focuses on multi-agent teams; Hermes focuses on single-agent self-improvement. |

## Tech stack

- **Python** — primary implementation language
- **CLI tooling** — interactive shell, setup wizard, migration tools
- **Gateway** — messaging gateway for Telegram, Discord, etc.

## Dependencies

- Python runtime (3.10+ recommended)
- An LLM provider (OpenAI, Anthropic, or local models)
- A server or VPS (can run on a $5 VPS)
- Messaging app credentials if using gateway features

## Ops difficulty

**Low to medium**. Installation is straightforward via CLI; the agent can run on minimal hardware. The learning loop and skill persistence add some operational complexity — you need to manage the knowledge store and monitor skill quality over time.

## Health & viability

- **Maintenance**: Very active — pushed daily as of 2026-07, 207k stars, 24,601 open issues indicate a large, engaged community.
- **Governance**: Owned by Nous Research organization; backed by an established AI research lab.
- **Backing**: Nous Research is a known AI research organization with a track record in open-source model training.
- **Adoption**: Very high star count (207k) but young (created 2025-07). The rapid growth suggests hype but also genuine interest.
- **Risk flags**: Extremely young with no Lindy track record. The learning-loop features are novel and their long-term stability is unproven. [推断]

## Caveats (unverified)

- [推断] With 207k stars in under a year, the star count may reflect hype rather than verified production adoption.
- [未验证] The "learning loop" that creates skills from experience may produce low-quality or unexpected skills; human review of generated skills may be necessary.
- [未验证] The $5 VPS claim is likely for minimal usage; production workloads with large models may require significantly more resources.
