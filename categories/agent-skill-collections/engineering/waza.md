---
name: Waza
slug: waza
repo: https://github.com/tw93/Waza
category: engineering
tags: [skills, claude-code, engineering-habits, debugging, code-review, multi-agent]
language: Python
license: MIT
maturity: v3.29.0, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# Waza

A compact collection of eight "engineering habit" skills — plan, design, review, debug, write, research, read, audit — packaged so a coding agent can load and run them on demand across Claude Code, Codex, and Cursor.

## When to use

You're an engineer working day-to-day inside Claude Code (or Codex / Cursor), and you notice the agent has no muscle memory for the disciplines you take for granted: it dives into code without thinking through the design, "fixes" bugs by guessing instead of finding the root cause, skips the diff review before declaring a release ready, and writes prose that reads like a robot. You don't want to assemble and maintain your own skill stack from scratch, and you want a small, opinionated set of habits rather than a sprawling framework. Waza drops in eight named skills you invoke directly — `/think` (pre-build planning and design validation), `/design` (frontend UI with aesthetic iteration), `/check` (post-task review / diff analysis / release verification), `/hunt` (systematic debugging and root-cause analysis), `/write` (natural English/Chinese prose editing), `/learn` (a six-phase research workflow), `/read` (URL and PDF extraction), and `/health` (agent config auditing across platforms).

You reach for it when you want a curated, ready-made habit pack that follows you across the three supported harnesses, installed in one command (`npx skills add tw93/Waza -a claude-code codex cursor -g -y`). Each skill folder ships reference docs, helper scripts, and gotchas, so the behavior is more than a bare prompt — but it still activates through the host platform's native skill-loading mechanism, not as a standalone program you run.

## When NOT to use

- **You already run a curated skill/command system.** Several Waza skills (`/think`, `/check`, `/hunt`, `/write`, `/health`, `/learn`, `/read`) overlap directly with common in-house planning/review/debug/research stacks. Layering them on top invites duplicate routing and conflicting instructions — pick one source of truth per habit.
- **Your agent isn't in the supported set.** Installation targets Claude Code, Codex, Cursor (plus Pi / Claude Desktop per the README). On an unsupported or bespoke harness there's no loader to fire the skills, and the markdown alone won't auto-activate. [推断]
- **You want enforcement, not suggestion.** Behavior lives in prompt/skill markdown that the agent loads; the "habits" are advisory and the agent can still deviate. They are not hard gates.
- **You only need one habit.** It's a bundle of eight; if you just want, say, a debugging routine, installing the whole pack pulls in seven skills you won't route to.
- **Single-maintainer, fast-moving upstream.** A v3.x project with frequent releases and behavior baked into prompts; a version bump can change how a skill routes or what it checks. Pin and re-verify after upgrades.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [Superpowers](../../agent-dev-methodology/superpowers.md) | ✅ | Larger, methodology-first skills library (brainstorm→plan→TDD→subagent→verify) targeting many harnesses; Waza is a smaller, habit-oriented bag of eight named commands, lighter to adopt but less of a full SDLC spine. |
| [SuperClaude Framework](../../agent-dev-methodology/superclaude.md) | ✅ | Persona/command/MCP configuration framework with a much larger surface and heavier install; Waza is leaner and centers concrete engineering routines rather than a persona system. |
| addyosmani/agent-skills | 未收录 | Sibling skill collection in this leaf; compare on which engineering habits each actually ships and harness coverage. |
| web-quality-skills (addyosmani) | 未收录 | Web-performance/quality-focused skills; narrower domain than Waza's general engineering habits. |
| vercel-labs/agent-skills | 未收录 | Vendor-curated skill collection; compare provenance and which agents it targets. |
| Anthropic's built-in skills / slash commands | 未收录 | The platform's native skill ecosystem; Waza is a third-party bundle layered on top and can duplicate or conflict with native commands. |

## Caveats (unverified)

- [未验证] Latest release reported as v3.29.0 ("Bridge", published 2026-06-19) with the repo last pushed 2026-06-24; license MIT and primary language Python (with Shell/Makefile) per GitHub metadata as of 2026-06-26 — re-verify before relying on a specific version's behavior.
- [未验证] Star count (~6.05k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not as a quality signal.
- [未验证] The eight skill names and their descriptions (`/think`, `/design`, `/check`, `/hunt`, `/write`, `/learn`, `/read`, `/health`) and the `skills/` directory layout are taken from the README and repo tree; the exact behavior, helper scripts, and per-skill contents were not exercised here.
- [未验证] The supported-agent list (Claude Code, Codex, Cursor, Pi, Claude Desktop) and the `npx skills add …` install path are from the project README; actual activation fidelity per harness is not independently confirmed.
- [推断] Because behavior lives in prompt/skill markdown loaded by the agent, enforcement is advisory — "habits" are prompt-level instructions, not hard guarantees, and the agent can deviate.
- [推断] As a single-maintainer v3.x project with frequent releases, skill set and routing can change release-to-release; check the current `skills/` directory rather than relying on this list.
