---
name: ECC
slug: ecc
repo: https://github.com/affaan-m/ECC
category: agent-dev-methodology
tags: [claude-code, skills, agents, hooks, memory, security-scan, cross-harness, mcp]
language: JavaScript
license: MIT
maturity: v2.0.0, active (2026-06)
last_verified: 2026-06-26
type: framework
---

# ECC

A cross-harness "agent operating system" that installs hundreds of skills, agents, rules, hooks, memory/instinct learning, and a security scanner into Claude Code (and Codex/OpenCode/Cursor) from one repo.

## When to use

You're running Claude Code (or several harnesses — Codex, OpenCode, Cursor) day to day, and you've outgrown a hand-rolled `~/.claude` directory. You keep re-writing the same TDD / code-review / security-review workflows per project, your context gets blown out at session start, and nothing carries learnings forward. ECC resolves this by shipping an opinionated, batteries-included substrate as a Claude Code plugin: you run `/plugin install ecc@ecc`, and you get a large library of skills, specialized subagents (planner, architect, code-reviewer, language-specific reviewers), always-on rules, and Node-backed hooks that auto-save/load session context and extract "instincts" with confidence scoring. It's the right reach when you want a maintained, versioned harness stack instead of curating one yourself.

You're also a fit if you work across more than one agent runtime and want *one* source of truth: ECC ships harness-neutral session adapters and an MCP inventory so the same skills/rules/AGENTS.md conventions apply whether you're in Claude Code, Codex CLI, OpenCode, or Cursor, plus a `/security-scan` (AgentShield) pass that audits your agent config for injection risks, leaked secrets, and misconfigurations before you trust it.

## When NOT to use

- **You want a small, auditable, self-owned config.** ECC installs hundreds of skills/agents/rules and a hook runtime into `~/.claude`; if you prefer a handful of files you fully understand and version yourself, this is a large surface to inherit and reason about.
- **You're not on Claude Code / a supported harness.** The primary target is Claude Code; non-Claude harnesses use adapters of varying completeness. If your runtime isn't on the list, most value evaporates.
- **You distrust auto-loaded hooks / memory.** Hooks run Node on session events and persist data locally; the v2.0.0 notes themselves flag that "plugin hooks were silently no-ops on Node 21+" was a shipped bug — a reminder this is moving, behavior-bearing automation, not inert prompts.
- **You only need one workflow.** If you just want, say, a TDD loop or a security gate, lifting one pattern (or a single-purpose tool) beats adopting a whole operating-system layer and its update cadence.
- **Single-author velocity / lock-in risk.** Development is fast-moving and centered on one maintainer's repo; coupling your whole agent harness to its release rhythm and conventions is real lock-in. Maturity/abandonment is a bet you're making on one project.
- **You need provider-neutral methodology, not Claude-centric config.** ECC is heavily Claude-Code-shaped; for vendor-agnostic *principles* rather than installed config, a doc-only methodology fits better.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [SuperClaude Framework](superclaude.md) | ✅ | Also a Claude-focused config framework (personas, commands, MCP); narrower and lighter than ECC's hundreds-of-skills + hooks + security-scan + cross-harness substrate. |
| [Superpowers](superpowers.md) | ✅ | A curated skills/plugin collection for Claude Code; overlapping skill-library idea but without ECC's memory/instinct hooks, security scanner, and multi-harness adapters. |
| [Compound Engineering](compound-engineering.md) | ✅ | A plugin encoding a specific compounding-workflow methodology; far more opinionated-and-small vs ECC's broad OS-style bundle. |
| [get-shit-done](get-shit-done.md) | ✅ | Lightweight task-execution workflow pack; single-philosophy vs ECC's everything-included surface. |
| [12-Factor Agents](12-factor-agents.md) | ✅ | Provider-neutral *principles* for building agents (docs, not installed config); different layer than ECC's concrete Claude-Code harness. |
| dotfiles / hand-rolled `~/.claude` | 未收录 | Full control and minimal surface; you maintain every skill/hook/rule yourself instead of inheriting and updating a curated stack. |

## Tech stack

- **Language:** JavaScript / Node.js (per repo primary language) for hooks, scripts, and the install path; large amounts of Markdown (skills/agents/rules with YAML frontmatter) as the actual payload.
- **Tooling:** `install.sh` / `install.ps1` installers; npm packages `ecc-universal` (main) and `ecc-agentshield` (security auditor); Node's built-in test runner for the internal test suite.
- **Optional GUI:** a Python (Tkinter) dashboard (`ecc_dashboard.py`).
- **Integration surface:** Claude Code plugin format (`/plugin install`), `hooks.json` + Node hook scripts, `mcp-servers.json` for MCP wiring, and per-harness adapters (Codex `AGENTS.md`, OpenCode plugin hooks, Cursor, GitHub Copilot instruction files).

## Dependencies

- **Runtime:** Node.js (for hook execution and setup scripts). README states Claude Code CLI v2.1.0+ as the primary target [未验证]. v2.0.0 notes call out a Node 21+ hook regression that was fixed — version sensitivity is real.
- **Optional:** Python 3 for the dashboard GUI; PM2 for multi-agent orchestration; MCP servers (GitHub, Supabase, Vercel, Context7, Exa, Playwright, etc.) for the MCP features — each its own external dependency/credential.
- **Storage:** local only — memory/metrics persist under `~/.claude/session-data/`, `~/.claude/skills/learned/`, `~/.claude/metrics/`; no external backend.
- **Install:** `/plugin install ecc@ecc` (plugin path), or `npm install && ./install.sh --profile full` for manual setup.

## Ops difficulty

**Low to medium.** The plugin install path is one command and the system is purely client-side (no server to run), so getting started is easy. Difficulty rises because what you've installed is large and *active*: hundreds of skills/agents/rules plus Node hooks that fire on session events and mutate local memory. You inherit its update cadence, env-var tuning (`ECC_HOOK_PROFILE`, `ECC_SESSION_START_MAX_CHARS`, `ECC_AGENT_DATA_HOME`), Node-version sensitivity (the v2.0.0 Node 21+ hook fix), and cross-harness adapter quirks. Debugging an unexpected behavior means tracing through hook scripts and a big config tree rather than a few files you wrote.

## Caveats (unverified)

- [未验证] v2.0.0 publish date per GitHub release API is 2026-06-10; one secondary source rendered it as 2024 — treat the 2026-06 maturity line as the authoritative one and re-verify on the release page.
- [未验证] Skill/agent/command/rule counts vary by source and release (README cites ~271 skills / 67 agents; the v2.0.0 notes cite 261 skills / 64 agents / 84 commands). Counts shift release-to-release; verify against the current repo.
- [未验证] GitHub stars (~211.9k–221.9k as of 2026-06) — star counts in this ecosystem are unreliable and date-sensitive; indicative only.
- [未验证] npm package names (`ecc-universal`, `ecc-agentshield`), the Tkinter dashboard, PM2 orchestration, and AgentShield's "1,282 tests / 102 rules" come from the README and were not independently confirmed against published packages.
- [未验证] Claude Code CLI v2.1.0+ minimum and the exact set of supported non-Claude harnesses / adapter completeness are from project docs, not independently tested.
- [推断] Typed as `framework` (not `skill-pack`) because, beyond its prompt/skill payload, it ships real runtime tooling (Node hooks, installers, version-gated behavior, env-var config, local state) — i.e. it has genuine tech-stack/deps/ops. A reader who only wants the markdown payload may reasonably regard the prompt collection alone as skill-pack-like.
