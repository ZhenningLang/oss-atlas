# databases

> Category node. Databases and database tooling — clients, GUIs, sync, and Redis/ES-compatible stores.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **PikiwiDB** | Use it when a large Redis dataset has blown past RAM and memory cost dominates — RocksDB-backed, Redis-protocol, so one node holds hundreds of GB; but it trades latency for capacity, wrong if every op must be microsecond-fast. | [→](pikiwidb.md) |
| **elasticsearch-dsl-py** | Use it when you maintain legacy Python code pinned to the standalone elasticsearch-dsl package — for any new project it's archived, so install elasticsearch>=8.18 and use elasticsearch.dsl instead. | [→](elasticsearch-dsl-py.md) |
| **elasticsearch-sql** | Use it when a SQL-fluent team needs to query Elasticsearch without learning the JSON Query DSL — but Elastic's first-party SQL/ES\|QL now overlaps it, so prefer the vendor feature when it covers you. | [→](elasticsearch-sql.md) |
| **go-mysql-elasticsearch** | Use it when you want a single Go binary to tail MySQL binlog and sync one direction into Elasticsearch at modest scale — but it's unmaintained since 2023 with no releases, so treat it as fork-and-own. | [→](go-mysql-elasticsearch.md) |
| **python-mysql-replication** | Use it when you want a pure-Python primitive to stream MySQL binlog as typed events and build a custom CDC loop with full control — but checkpointing, dedup and exactly-once delivery are entirely on you. | [→](python-mysql-replication.md) |
| **PrettyZoo** | Use it when you need a friendly desktop GUI to browse and lightly edit a ZooKeeper znode tree during dev or incident triage — but it's archived since 2023, so new JDK/macOS may break it with no upstream fix. | [→](prettyzoo.md) |
| **RDR** | Use it when a Redis instance trips its maxmemory alarm and you need offline, fast per-prefix analysis of an RDB snapshot — but figures are approximate and the tool is coasting (v0.0.1, 2019). | [→](rdr.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [PikiwiDB](pikiwidb.md) | ✅ | Use it when a large Redis dataset has blown past RAM and memory cost dominates — RocksDB-backed, Redis-protocol, so one node holds hundreds of GB; but it trades latency for capacity, wrong if every op must be microsecond-fast. |
| [elasticsearch-dsl-py](elasticsearch-dsl-py.md) | ✅ | Use it when you maintain legacy Python code pinned to the standalone elasticsearch-dsl package — for any new project it's archived, so install elasticsearch>=8.18 and use elasticsearch.dsl instead. |
| [elasticsearch-sql](elasticsearch-sql.md) | ✅ | Use it when a SQL-fluent team needs to query Elasticsearch without learning the JSON Query DSL — but Elastic's first-party SQL/ES\|QL now overlaps it, so prefer the vendor feature when it covers you. |
| [go-mysql-elasticsearch](go-mysql-elasticsearch.md) | ✅ | Use it when you want a single Go binary to tail MySQL binlog and sync one direction into Elasticsearch at modest scale — but it's unmaintained since 2023 with no releases, so treat it as fork-and-own. |
| [python-mysql-replication](python-mysql-replication.md) | ✅ | Use it when you want a pure-Python primitive to stream MySQL binlog as typed events and build a custom CDC loop with full control — but checkpointing, dedup and exactly-once delivery are entirely on you. |
| [PrettyZoo](prettyzoo.md) | ✅ | Use it when you need a friendly desktop GUI to browse and lightly edit a ZooKeeper znode tree during dev or incident triage — but it's archived since 2023, so new JDK/macOS may break it with no upstream fix. |
| [RDR](rdr.md) | ✅ | Use it when a Redis instance trips its maxmemory alarm and you need offline, fast per-prefix analysis of an RDB snapshot — but figures are approximate and the tool is coasting (v0.0.1, 2019). |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

Databases and the **tooling around them** — clients, admin GUIs, sync/replication, RDB analysis. Not RAG vector stores (see `rag-retrieval`).
