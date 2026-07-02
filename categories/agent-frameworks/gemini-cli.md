---
name: Gemini CLI
slug: gemini-cli
repo: https://github.com/google-gemini/gemini-cli
category: agent-frameworks
tags: [ai-agent, cli, gemini, mcp-client, mcp-server, terminal]
language: TypeScript
license: Apache-2.0
maturity: v0.x, active, 105.7k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T01:49:23Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: A
  overall_score: 3.4
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
      grade: A
      raw:
        stars: 105703
    longevity:
      grade: D
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Gemini CLI

An open-source AI agent that brings the power of Gemini directly into your terminal. Provides lightweight access to Gemini models with built-in tools, MCP support, and a free tier for personal Google accounts.

![Gemini CLI — health radar](../../assets/health/gemini-cli.svg)

## When to use

You're a developer who lives in the terminal and wants an AI assistant that can reason about your codebase, run shell commands, search the web, and read files — all without leaving your command line. You prefer Google's Gemini models (especially the 1M token context window) and want a free tier with reasonable rate limits (60 req/min, 1,000 req/day). You install Gemini CLI via npm, authenticate with your Google account, and start delegating tasks: refactoring code, explaining APIs, generating tests, or fetching documentation. The MCP extensibility means you can wire it into your existing tool ecosystem.

## When NOT to use

- **Non-Gemini model preference** — Gemini CLI is tightly coupled to Google's Gemini API. If you need to switch between OpenAI, Anthropic, or local models frequently, this is not your tool.
- **No Google account policy** — The free tier requires a personal Google account; if your organization blocks Google authentication or you need enterprise SSO, this is a barrier.
- **Offline / air-gapped environments** — Gemini CLI requires internet access to reach the Gemini API; it does not support local model inference.
- **Complex multi-agent orchestration** — Gemini CLI is a single-agent CLI tool, not a multi-agent framework like LangChain or AutoGPT. For building workflows with multiple collaborating agents, look elsewhere.
- **Enterprise audit requirements** — No built-in audit logging, RBAC, or admin controls; it's a personal developer tool.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [OpenCode](opencode.md) | ✅ | Open-source terminal coding agent. | OpenCode is model-agnostic and self-hostable; Gemini CLI is Google-only but offers a generous free tier and deep Gemini integration. |
| [Open Interpreter](open-interpreter.md) | ✅ | Terminal coding agent with swappable harnesses for open models. | Open Interpreter supports multiple model providers and local models; Gemini CLI is Gemini-only but has stronger Google ecosystem integration. |
| Claude Code | 未收录 | Official Anthropic terminal coding agent. | Closed-source, Anthropic-only; Gemini CLI is open-source and free-tier friendly but locked to Google models. |
| [CC Switch](cc-switch.md) | ✅ | Desktop manager for multiple coding agents. | CC Switch can manage Gemini CLI alongside other agents; they are complementary, not competing. |
| GitHub Copilot CLI | 未收录 | AI-powered CLI from GitHub/Microsoft. | Copilot CLI is Copilot-subscription based and IDE-integrated; Gemini CLI is standalone and free-tier accessible. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — runtime environment
- **Gemini API** — backend LLM provider (Google)
- **MCP (Model Context Protocol)** — extensibility layer for custom integrations
- **Google Search** — built-in grounding tool

## Dependencies

- Node.js runtime (npm-installable)
- A Google account (for the free tier API access)
- Internet connectivity (to reach Gemini API endpoints)
- Terminal / shell environment

## Ops difficulty

**Low**. Gemini CLI is installed via npm and runs as a local Node.js process. There is no server to maintain. The operational burden is limited to keeping the CLI updated and managing your Google API credentials. The free tier has rate limits that may require upgrading for heavy usage, but there is no infrastructure to operate.

## Health & viability

- **Maintenance**: Active — pushed daily as of 2026-07, with a responsive issue tracker (1,347 open issues). [推断]
- **Governance**: Owned by the `google-gemini` organization, a Google-backed GitHub org. Bus factor is reasonable given Google's backing, but the project's future depends on Google's continued commitment to the open-source CLI. [未验证]
- **Backing**: Officially backed by Google (Gemini team). The Apache-2.0 license is permissive, but Google has a history of sunnsetting open-source projects. [推断]
- **Adoption**: Strong star count (105.7k) with a recent creation date (2025-04). The backing by Google and the generous free tier drive rapid adoption. [推断]
- **Risk flags**: Very young (created 2025-04) with no Lindy track record. Google's history of abandoning open-source projects (e.g., Google Reader, Google+) is a relevant prior, though the Gemini brand appears to be a strategic priority. [推断]

## Caveats (unverified)

- [未验证] The exact relationship between `google-gemini` and the broader Google DeepMind / Gemini product organization has not been verified.
- [推断] Google has a track record of launching and later deprecating open-source and consumer projects; the long-term commitment to Gemini CLI is unproven.
- [未验证] The free tier rate limits (60 req/min, 1,000 req/day) may be reduced or changed as the product matures.
- [未验证] The MCP server ecosystem and third-party integration quality are new and unverified.
