---
name: Superpowers
slug: superpowers
repo: https://github.com/obra/superpowers
category: agent-dev-methodology
tags: [skills, sdlc, tdd, subagent-driven-development, brainstorming, git-worktrees, claude-code, plugin]
language: Shell
license: MIT
maturity: v6.0.3, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# Superpowers

A composable skills library that installs a full SDLC methodology — brainstorm → plan → TDD → subagent-driven execution → verify — into your coding agent as a plugin.

## When to use

You're a developer running Claude Code (or Codex, Cursor, Gemini CLI, OpenCode, Kimi, Droid…) and you keep hitting the same failure mode: the agent jumps straight to code, skips writing a failing test first, "fixes" a bug by guessing, and declares victory without actually verifying anything. You want it to behave like a disciplined senior engineer — interrogate what you're really trying to build, write the plan down, do real red-green-refactor, isolate work on a git worktree, and run a verification pass before claiming done. Superpowers gives you exactly that as a drop-in plugin: a curated set of skills (`brainstorming`, `writing-plans`, `test-driven-development`, `systematic-debugging`, `subagent-driven-development`, `verification-before-completion`, `using-git-worktrees`, and more) that the agent loads on demand and follows step by step.

You reach for it when you want an opinionated, battle-tested workflow rather than building your own skill stack from scratch — and especially when you want that same methodology to follow you across harnesses. The repo ships per-agent plugin manifests (Claude `.claude-plugin`, Codex, Cursor, Kimi, OpenCode, Pi), so the brainstorm-plan-TDD-verify spine stays consistent whether today's task runs in Claude Code or Codex CLI. Install once via your agent's marketplace, and the methodology activates through the platform's native skill-loading mechanism.

## When NOT to use

- **You already have a curated skill/command system you trust.** Superpowers is opinionated and prescriptive (mandatory failing-test-first, brainstorm-before-code). Layering it on top of an existing methodology stack invites conflicting instructions and double-routing — pick one source of truth.
- **You're not on a supported agent harness.** It activates through each platform's skill-loading mechanism (Claude `Skill` tool, Codex/Cursor/Kimi/Gemini/OpenCode plugins). On an unsupported or bespoke agent there's no loader to invoke the skills, and the markdown alone won't auto-fire.
- **One-off scripts, throwaway spikes, non-code tasks.** The full brainstorm→plan→TDD→verify ceremony is overhead when you just want a quick shell one-liner or a config tweak; the methodology assumes a real software-change loop.
- **You want a runtime/library/CLI.** There's nothing to `import` or run standalone — no deps, no API, no service. It only shapes an agent's behavior; outside a supporting agent it does nothing.
- **Fast-moving, opinionated upstream.** Single-maintainer project at v6.x with frequent releases and behavior baked into prompts; a version bump can shift how skills route or what they enforce. Pin a version if you need stability, and re-check after upgrades. [推断]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [SuperClaude Framework](superclaude.md) | ✅ | Persona/command/MCP-oriented configuration framework for Claude Code; richer command + agent surface, heavier install. Superpowers is leaner and centers a TDD/SDLC discipline rather than a persona system. |
| [get-shit-done](get-shit-done.md) | ✅ | Workflow/command pack aimed at shipping; overlapping "drive the agent through a process" goal, different process shape. Superpowers leads with brainstorm-then-TDD and subagent dispatch. |
| [Compound Engineering](compound-engineering.md) | ✅ | Methodology plugin built around compounding/automation patterns; sibling philosophy, different primitives. Pick by which workflow spine matches your team. |
| [ECC](ecc.md) | ✅ | Another agent-dev methodology in this category; compare on which lifecycle stages each actually enforces vs. suggests. |
| [12-Factor Agents](12-factor-agents.md) | ✅ | Principles/methodology doc for building agent *applications*, not a plug-in skill pack you install into a coding agent — different unit of consumption. |
| Anthropic's official skills / built-in slash commands | 未收录 | The platform's own skill ecosystem; Superpowers is a third-party curated bundle layered on top, so it can conflict with or duplicate native skills. |

## Health & viability

- **Maintenance (2026-06):** actively maintained — last pushed 2026-06-25, latest release v6.0.3 (2026-06-18), not archived. Frequent releases on a v6.x line = a live, fast-iterating project (the page already flags "fast-moving, opinionated upstream").
- **Governance & bus factor:** the repo is **User-owned** (obra / Jesse Vincent) — a single-maintainer project. The ~240k-star headline against one-person stewardship is a **bus-factor flag**, not a durability signal; the roadmap and "mandatory" prompt-level rules are one author's opinionated line. [未验证] No co-maintainer/foundation governance published.
- **Age & Lindy (2026-06):** created 2025-10, ~8 months old, already at v6.x — frequent major bumps imply the skill set and routing churn release-to-release. Lindy verdict: **unproven by age** — high mindshare is not longevity; adopt for current value, pin versions, re-check skill routing after upgrades.
- **Risk flags:** MIT (no relicense). Enforcement is **advisory** — behavior lives in prompt/markdown skills the agent can still deviate from, so "mandatory failing-test-first" is a prompt instruction, not a hard gate. Single-maintainer abandonment is the main long-term exposure. [未验证] No CVEs reviewed.

## Caveats (unverified)

- [未验证] Latest release reported as v6.0.3 (published 2026-06-18) with the repo last pushed 2026-06-25; license MIT and primary language Shell per GitHub metadata as of 2026-06-26 — re-verify before relying on a specific version's behavior.
- [未验证] Star count (~239k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not as a quality signal.
- [未验证] The supported-agent list (Claude Code, Codex App/CLI, Cursor, Factory Droid, Gemini CLI, GitHub Copilot CLI, Kimi Code, OpenCode, Pi, Antigravity) is from the project README; actual activation fidelity varies per harness and is not independently confirmed here.
- [推断] Because behavior lives in prompt/markdown skills loaded by the agent, enforcement is advisory — the agent can still deviate; "mandatory" steps are prompt-level instructions, not hard guarantees.
- [推断] The skill set (13 skills as of this check) and routing change release-to-release; verify the current `skills/` directory rather than relying on this list.
