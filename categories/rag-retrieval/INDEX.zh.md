# rag-retrieval

> 分类节点。面向 RAG 的文档索引、代码智能图与图数据库。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **FalkorDB** | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 | [→](falkordb.zh.md) |
| **graphify** | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 | [→](graphify.zh.md) |
| **code-review-graph** | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及(blast-radius)的文件时用它。 | [→](code-review-graph.zh.md) |
| **PageIndex** | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 | [→](pageindex.zh.md) |
| **Understand-Anything** | 当你想把任意代码库变成可探索、可提问的知识图谱给 agent 用时用它——比 graphify 更年轻、未经检验。 | [→](understand-anything.zh.md) |
| **FAISS** | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 | [→](faiss.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [FalkorDB](falkordb.zh.md) | ✅ | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 |
| [graphify](graphify.zh.md) | ✅ | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 |
| [code-review-graph](code-review-graph.zh.md) | ✅ | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及(blast-radius)的文件时用它。 |
| [PageIndex](pageindex.zh.md) | ✅ | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 |
| [Understand-Anything](understand-anything.zh.md) | ✅ | 把代码变成 agent 可查询的可探索知识图谱；比 graphify 年轻，star 数与数据外发边界均存疑。 |
| [FAISS](faiss.zh.md) | ✅ | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 |
| Neo4j / LlamaIndex / LightRAG / Weaviate | 未收录 | 各页对比里点到的其他图 / RAG 检索方案。 |

## 什么该放这里

主要职责是为 RAG **索引与检索**上下文的基础设施——文档索引、代码图、图数据库。不含 agent 记忆(见 `agent-memory`)，不含研究 agent(见 `deep-research`)。
