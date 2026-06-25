# agent-tooling

> Level 2 of 3. Infrastructure for AI coding agents — task/work tracking, persistent memory,
> agent state. 为 AI agent 选「任务/记忆/状态」基建。
> ← back to [category route](../../INDEX.md)

## Projects in this category

| Project | Use when (一句话) | License | Page |
|---|---|---|---|
| **beads** | An agent (or small fleet) needs durable, dependency-aware task memory across sessions and branches, version-controlled with the code. agent 需要跨会话、可随代码版本化的依赖式任务记忆。 | MIT | [→](beads.md) |

## Comparison matrix

Substitutes named in the project pages but **not yet indexed** (`未收录`). They are candidates
for future entries — see [add-project](../../.claude/skills/add-project/SKILL.md).

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [beads](beads.md) | ✅ | Dependency-aware, version-controlled (Dolt) task graph; agent-native, offline-first — but alpha, single-writer in embedded mode, no human web UI. |
| Plain `MEMORY.md` / `TODO.md` | 未收录 | Zero deps, human-readable — but unstructured (no graph, no ready-detection, no merge-safe IDs). |
| GitHub Issues (+ `gh`) | 未收录 | Mature hosted tracker with UI/notifications — but online-first, not version-controlled with the code, not agent-native. |
| Taskwarrior | 未收录 | Battle-tested offline CLI task manager — but no SQL/version-control backend, weaker multi-agent merge. |
| Linear / Jira | 未收录 | Best for human teams — but heavyweight, online-only, not agent-native. |

## What belongs here

Tools whose primary job is to support an AI coding agent's *operation*: task/work graphs,
persistent memory, agent state stores, multi-agent coordination. Not end-user apps that merely
*use* an LLM.
