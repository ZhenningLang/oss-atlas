---
name: wshobson/agents
slug: wshobson-agents
repo: https://github.com/wshobson/agents
category: subagent-collections
tags: [claude-code, subagents, skills, slash-commands, multi-harness, marketplace, orchestrators]
language: Python
license: MIT
maturity: active, no tagged releases, ~37.2k stars (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# wshobson/agents

A large, single-maintainer multi-harness "plugin marketplace": ~194 domain subagents, ~158 skills, ~106 slash commands and ~16 multi-agent orchestrators, authored once in Markdown and generated into harness-native artifacts for Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI and Copilot.

## When to use

You're a developer who lives in Claude Code (or Codex CLI / Cursor / OpenCode / Gemini CLI), and you keep hitting tasks that sit outside your own comfort zone — a Rust performance regression, a Terraform module review, a SQL query plan, an incident post-mortem, a security pass on an auth flow. Hand-writing a good subagent persona or a focused skill for each of these is real work, and you'd rather pull a vetted one off the shelf. You open `/plugin marketplace add wshobson/agents`, then `/plugin install <plugin-name>`, and the relevant domain-expert subagents, skills and slash commands drop into your harness through its own loader. Instead of one bloated do-everything prompt, you get many narrow specialists the agent can delegate to by domain.

You reach for this specifically when you want *breadth* and *cross-harness portability* from one source. The repo is built from a single Markdown source and emits idiomatic per-harness artifacts via `make generate`, so the same "backend-architect" or "security-auditor" persona follows you whether today's task runs in Claude Code or Codex CLI. It is closer to a curated catalog than an opinionated methodology: pick the plugins for the domains you actually touch (Python, full-stack, ML, infra, security, data, docs, SEO, orchestration) and ignore the rest.

## When NOT to use

- **You already run a curated subagent/skill stack you trust.** ~194 agents plus ~158 skills is a lot of surface; layering it onto an existing methodology pack invites overlapping personas and double-routing (two "code reviewers", two "debuggers" competing for the same task). Pick one source of truth per concern.
- **Install path varies sharply by harness.** Claude Code installs natively via `/plugin`; Codex and Cursor pull from committed registries; Gemini CLI and OpenCode require cloning plus `make generate` (the transformed trees are gitignored), which needs `make`/`uv` and is not a one-command install. [推断]
- **You want a runtime, library or CLI for your app.** Apart from the `plugin-eval` quality tool, there is nothing to `import` into your own software — this configures an agent's behavior, not your application. Outside a supporting harness it does nothing.
- **You need pinned, reproducible behavior.** No tagged releases exist [未验证]; you install whatever is on `main`. A push can shift how a subagent routes or what a skill enforces. Vendor the files and pin your own copy if you need stability.
- **Enforcement is advisory, and breadth is unaudited.** Behavior lives in prompt/Markdown that the agent loads; "expert" personas are instructions, not guarantees, and 190+ personas means you cannot personally vet each one's quality before delegating real work to it.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [awesome-claude-code-subagents](awesome-claude-code-subagents.md) | ✅ | The other large Claude Code subagent collection in this leaf, but *subagents only* (drop into `~/.claude/agents/`). wshobson/agents bundles skills + commands + orchestrators too and generates per-harness; pick by whether you want persona breadth only vs. a multi-artifact, multi-harness catalog. |
| [gstack](../personal-collections/gstack.md) | ✅ | One founder's *role-based* command set (CEO/designer/QA personas) tuned to his daily factory. Far narrower and personal; wshobson/agents is a generic domain catalog, not a single operator's workflow. |
| Anthropic Claude Plugins (official marketplace) | 未收录 | First-party, Anthropic-curated `/plugin` marketplace with known provenance; narrower and Claude-Code-only. wshobson/agents is third-party and far broader, spanning multiple harnesses, at higher trust/vetting cost. |
| Hand-rolling your own subagents/skills | 未收录 | Maximum fit and zero conflict with your existing stack, but you author and maintain everything. This repo trades bespoke fit for ready-made breadth you must still vet. |

## Caveats (unverified)

- [未验证] License MIT, primary language Python, not archived, last pushed 2026-06-25, topics include `claude-code`/`agent-skills`/`opencode`/`codex-cli`/`mcp` per GitHub metadata as of 2026-06-26 — re-verify before relying on specifics.
- [未验证] No tagged release exists (`latestRelease` is null as of this check); installs track `main`, so behavior can change without a version bump.
- [未验证] Star count (~37.2k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] The inventory figures (~88 plugins, ~194 agents, ~158 skills, ~106 commands, ~16 orchestrators) are read from the README on 2026-06-26 and will drift; enumerate the current `plugins/` tree rather than trusting these counts.
- [未验证] The supported-harness list (Claude Code as source-of-truth, plus Codex CLI, Cursor, OpenCode, Gemini CLI, Copilot) and the per-harness install mechanics (native registry vs. clone + `make generate`) are from the README; actual generation/activation fidelity per harness is not independently confirmed here.
- [未验证] The `plugin-eval` quality framework (static analysis, LLM semantic scoring via Haiku/Sonnet, Monte Carlo validation; `uv run plugin-eval score`/`certify`) is described in the README and not independently exercised here.
- [推断] Single-maintainer project; maintenance cadence and long-term support are not guaranteed, and a large unversioned surface can regress between pushes.
- [推断] Because personas/skills activate through each harness's native loader, enforcement is advisory — the agent can deviate, and cross-harness portability depends on the generator, not a runtime contract.
