# rag-retrieval

> Category node. Document indexing, code-intelligence graphs, and graph DBs for retrieval-augmented generation.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **FalkorDB** | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. | [→](falkordb.md) |
| **graphify** | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. | [→](graphify.md) |
| **code-review-graph** | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. | [→](code-review-graph.md) |
| **PageIndex** | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. | [→](pageindex.md) |
| **Understand-Anything** | Use it when you want any codebase turned into an explorable, queryable knowledge graph for an agent — younger and less proven than graphify. | [→](understand-anything.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [FalkorDB](falkordb.md) | ✅ | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. |
| [graphify](graphify.md) | ✅ | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. |
| [code-review-graph](code-review-graph.md) | ✅ | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. |
| [PageIndex](pageindex.md) | ✅ | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. |
| [Understand-Anything](understand-anything.md) | ✅ | Code → explorable knowledge graph an agent can query; younger than graphify, with an unverified star count and egress boundary. |
| Neo4j / LlamaIndex / LightRAG / Weaviate | 未收录 | Other graph/RAG retrieval stacks named across the pages. |

## What belongs here

Infrastructure whose primary job is **indexing and retrieving** context for RAG — document indexes, code graphs, graph databases. Not agent memory (see `agent-memory`), not research agents (see `deep-research`).
