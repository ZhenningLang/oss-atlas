---
name: Codex
slug: codex
repo: https://github.com/openai/codex
category: agent-frameworks
tags: [coding-agent, terminal, ai-agent, openai, code-execution]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 94.8k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T09:13:07Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T00:00:00Z
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

# Codex

A lightweight coding agent from OpenAI that runs locally in your terminal. It can read files, execute shell commands, edit code, and ship changes — all through a natural-language interface.

![Codex — health radar](../../assets/health/codex.svg)

## When to use

You're a developer who wants an AI assistant that lives inside your terminal and can actually modify your codebase. You describe what you want — "refactor this function to use async/await" or "add error handling to this API route" — and Codex reads the relevant files, makes the edits, runs tests, and commits the changes. You prefer to keep your workflow local rather than relying on a cloud IDE, and you want the agent to have real shell access (with sandboxing) so it can verify its own changes. You install it with a single curl command or via npm, and it works with your existing Git setup.

## When NOT to use

- **You need multi-model flexibility.** Codex is optimized for OpenAI models. If you want to switch between DeepSeek, Anthropic, or local models frequently, use [Open Interpreter](open-interpreter.md) instead.
- **You are in a highly regulated environment.** Codex executes code in a sandbox, but it still runs arbitrary commands on your machine. If your security policy forbids AI agents with shell access, this is a non-starter.
- **You want a visual IDE experience.** Codex is terminal-only. If you prefer a GUI with click-to-edit, inline suggestions, and visual diffing, use an IDE plugin like GitHub Copilot or Cursor.
- **You need complex multi-agent orchestration.** Codex is a single-agent coding tool, not a multi-agent framework like LangChain or AutoGPT. For building workflows with multiple collaborating agents, look elsewhere.
- **You require offline operation.** Codex requires an internet connection to reach the OpenAI API; it does not support local model inference.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Open Interpreter](open-interpreter.md) | ✅ | Codex-fork with swappable harnesses for low-cost/open models. | Open Interpreter supports multiple providers and local models; Codex is OpenAI-only but has first-party integration and polish. |
| [OpenCode](opencode.md) | ✅ | Open-source terminal coding agent. | OpenCode is model-agnostic and community-driven; Codex is OpenAI-backed with tighter GPT integration. |
| [Gemini CLI](gemini-cli.md) | ✅ | Google's terminal AI agent. | Gemini CLI is Google-only with a free tier; Codex is OpenAI-only and may require API credits. |
| Claude Code | 未收录 | Official Anthropic terminal coding agent. | Closed-source, Anthropic-only; Codex is open-source and terminal-native but locked to OpenAI models. |
| GitHub Copilot | 未收录 | AI pair programmer IDE extension. | Copilot is IDE-integrated and subscription-based; Codex is terminal-first and standalone. |

## Tech stack

- **Rust** — core implementation for performance and safety
- **OpenAI API** — backend LLM provider (GPT-4o / GPT-4.5 class models)
- **Sandboxing** — OS-level sandbox for code execution on macOS, Linux, and Windows
- **Git** — built-in version control integration for committing changes
- **MCP (Model Context Protocol)** — extensibility for custom tools and integrations

## Dependencies

- OpenAI API key (or subscription)
- macOS, Linux, or Windows terminal
- Git repository (recommended, for change tracking)
- Internet connectivity (to reach OpenAI API)

## Ops difficulty

**Low.** Codex is installed via a shell script or npm and runs as a local CLI process. There is no server to maintain. The operational burden is managing your OpenAI API credentials and reviewing the agent's changes before accepting them. The sandboxing provides safety, but you should still audit executed commands.

## Health & viability

- **Maintenance**: Very active — pushed daily as of 2026-07, with rapid iteration and a large issue volume (8,147 open issues). [推断]
- **Governance**: Owned by OpenAI (`openai` GitHub org). The project has clear backing from OpenAI, but the roadmap is controlled by a single corporate entity. [未验证]
- **Backing**: Officially backed by OpenAI. The Apache-2.0 license is permissive, but OpenAI has not relicensed any major projects historically. [推断]
- **Adoption**: Explosive adoption with ~94.8k stars and ~14.1k forks, created in 2025-04. The OpenAI brand and terminal-native workflow drive rapid uptake. [推断]
- **Risk flags**: Very young (created 2025-04) with no Lindy track record. Tightly coupled to OpenAI's API and pricing, which can change without notice. The project's future depends on OpenAI's continued commitment to open-source terminal tools. [推断]

## Caveats (unverified)

- [未验证] Codex requires an OpenAI API key; the exact pricing and rate limits for heavy usage have not been verified.
- [推断] As an OpenAI project, the roadmap may prioritize features that drive API usage or OpenAI ecosystem lock-in.
- [未验证] The sandboxing mechanism's security guarantees against determined adversarial prompts have not been independently audited.
- [推断] The star count is extremely high for a project created in 2025-04; some inflation from OpenAI brand recognition is likely, but genuine adoption is also strong.
