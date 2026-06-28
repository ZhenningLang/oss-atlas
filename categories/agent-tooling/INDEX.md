# agent-tooling

> Category node. Infrastructure for AI coding agents — task/work tracking, persistent memory, agent state.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **beads** | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. | [→](beads.md) |
| **CCPM** | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. | [→](ccpm.md) |
| **Entire** | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. | [→](entire-cli.md) |
| **Ralph for Claude Code** | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. | [→](ralph-claude-code.md) |
| **Context Mode** | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. | [→](context-mode.md) |
| **Planning with Files** | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. | [→](planning-with-files.md) |
| **Vercel Skills** | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. | [→](vercel-skills.md) |
| **OpenSandbox** | Use it when an agent must run untrusted, generated code in isolated Docker/K8s sandboxes — a very young high-star project, so weigh adoption claims with caution. | [→](opensandbox.md) |
| **AgentsView** | Use it when you want local-first search, analytics, and token-cost insight across your coding-agent sessions. | [→](agentsview.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [beads](beads.md) | ✅ | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. |
| [CCPM](ccpm.md) | ✅ | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. |
| [Entire](entire-cli.md) | ✅ | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. |
| [Ralph for Claude Code](ralph-claude-code.md) | ✅ | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. |
| [Context Mode](context-mode.md) | ✅ | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. |
| [Planning with Files](planning-with-files.md) | ✅ | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. |
| [Vercel Skills](vercel-skills.md) | ✅ | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. |
| [OpenSandbox](opensandbox.md) | ✅ | Use it when an agent must run untrusted, generated code in isolated Docker/K8s sandboxes — a very young high-star project, so weigh adoption claims with caution. |
| [AgentsView](agentsview.md) | ✅ | Use it when you want local-first search, analytics, and token-cost insight across your coding-agent sessions. |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | Other task/work-tracking backends for agents named across the pages. |

## What belongs here

Infrastructure an AI **coding agent** uses to track work and carry state — task/issue graphs, session capture, planning / context plumbing. Not LLM-agnostic memory libraries (see `agent-memory`), not agent runtimes (see `agent-frameworks`).
