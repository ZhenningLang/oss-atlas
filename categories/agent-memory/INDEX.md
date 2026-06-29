# agent-memory

> Category node. Persistent, LLM-agnostic memory an agent reads/writes across sessions.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mem0** | Use it when your LLM agent must remember users across sessions without bloating the prompt context. | A (5/6) | [→](mem0.md) |
| **Memori** | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. | B (5/6) | [→](memori.md) |
| **Claude Subconscious** | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. | C (6/6) | [→](claude-subconscious.md) |
| **claude-mem** | Use it when your coding agent loses context across sessions and you want local hook/MCP-captured memory compressed and injected back in. | B (6/6) | [→](claude-mem.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mem0](mem0.md) | ✅ | A (5/6) | Use it when your LLM agent must remember users across sessions without bloating the prompt context. |
| [Memori](memori.md) | ✅ | B (5/6) | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. |
| [Claude Subconscious](claude-subconscious.md) | ✅ | C (6/6) | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. |
| [claude-mem](claude-mem.md) | ✅ | B (6/6) | Hook/MCP memory wired into a coding agent's session lifecycle (not a model-agnostic app memory API); reported star count is unverified. |
| Letta (MemGPT) / Zep / Cognee | 未收录 | — | Other agent-memory layers named across the pages. |

## What belongs here

Infrastructure whose primary job is to **store and recall** agent memory across sessions, independent of the model. Not task/issue tracking (see `agent-tooling`), not RAG document retrieval (see `rag-retrieval`).
