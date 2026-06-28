# agent-memory

> 分类节点。面向 agent、与 LLM 无关的跨会话持久记忆基础设施。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Mem0** | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 | [→](mem0.zh.md) |
| **Memori** | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 | [→](memori.zh.md) |
| **Claude Subconscious** | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用(仅 demo,非生产)。 | [→](claude-subconscious.zh.md) |
| **claude-mem** | 当你的编码 agent 跨会话丢失上下文、你想要本地 hook/MCP 捕获并压缩后再注入的记忆时用它(star 数存疑)。 | [→](claude-mem.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Mem0](mem0.zh.md) | ✅ | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 |
| [Memori](memori.zh.md) | ✅ | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 |
| [Claude Subconscious](claude-subconscious.zh.md) | ✅ | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用(仅 demo,非生产)。 |
| [claude-mem](claude-mem.zh.md) | ✅ | 接进编码 agent 会话生命周期的 hook/MCP 记忆(非与模型无关的应用内记忆 API);所报 star 数存疑。 |
| Letta (MemGPT) / Zep / Cognee | 未收录 | 各页对比里点到的其他 agent 记忆层。 |

## 什么该放这里

主要职责是**跨会话存取** agent 记忆、且与具体模型无关的基础设施。不含任务/issue 跟踪(见 `agent-tooling`),不含 RAG 文档检索(见 `rag-retrieval`)。
