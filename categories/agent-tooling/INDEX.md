# agent-tooling

> Level 2 of 3. Infrastructure for AI coding agents — task/work tracking, persistent memory,
> agent state.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | License | Page |
|---|---|---|---|
| **beads** | An agent (or small fleet) needs durable, dependency-aware task memory across sessions and branches, version-controlled with the code. | MIT | [→](beads.md) |

## Comparison matrix

Substitutes named in the project pages but **not yet indexed** (`未收录` / not indexed). They are
candidates for future entries — see [add-project](../../.claude/skills/add-project/SKILL.md).

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [beads](beads.md) | ✅ | Dependency-aware, version-controlled (Dolt) task graph; agent-native, offline-first — but alpha, single-writer in embedded mode, no human web UI. |
| Plain `MEMORY.md` / `TODO.md` | not indexed | Zero deps, human-readable — but unstructured (no graph, no ready-detection, no merge-safe IDs). |
| GitHub Issues (+ `gh`) | not indexed | Mature hosted tracker with UI/notifications — but online-first, not version-controlled with the code, not agent-native. |
| Taskwarrior | not indexed | Battle-tested offline CLI task manager — but no SQL/version-control backend, weaker multi-agent merge. |
| Linear / Jira | not indexed | Best for human teams — but heavyweight, online-only, not agent-native. |

## What belongs here

Tools whose primary job is to support an AI coding agent's *operation*: task/work graphs,
persistent memory, agent state stores, multi-agent coordination. Not end-user apps that merely
*use* an LLM.
