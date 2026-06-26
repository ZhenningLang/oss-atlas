# agent-memory

> Category node. Persistent, LLM-agnostic memory an agent reads/writes across sessions.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Mem0** | Use it when your LLM agent must remember users across sessions without bloating the prompt context. | [→](mem0.md) |
| **Memori** | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. | [→](memori.md) |
| **Claude Subconscious** | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. | [→](claude-subconscious.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Mem0](mem0.md) | ✅ | Use it when your LLM agent must remember users across sessions without bloating the prompt context. |
| [Memori](memori.md) | ✅ | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. |
| [Claude Subconscious](claude-subconscious.md) | ✅ | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. |
| Letta (MemGPT) / Zep / Cognee | 未收录 | Other agent-memory layers named across the pages. |

## What belongs here

Infrastructure whose primary job is to **store and recall** agent memory across sessions, independent of the model. Not task/issue tracking (see `agent-tooling`), not RAG document retrieval (see `rag-retrieval`).
