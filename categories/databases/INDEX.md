# databases

> Category node. Databases and database tooling — clients, GUIs, sync, and Redis/ES-compatible stores.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **PikiwiDB** | A Redis-protocol-compatible, disk-backed KV store (RocksDB engine) built by Qihoo360's infra team — keeps hot data in memory and persists the full dataset to disk so a single node can hold hundreds of GB the way Redis can't. (This repo is the home of the project historically known as **Pika**.) | [→](pikiwidb.md) |
| **elasticsearch-dsl-py** | A high-level, Pythonic DSL over the low-level Elasticsearch client — query objects, a Document ORM-style mapping layer, and chainable search builders instead of hand-writing query JSON. **Archived: as of v8.18.0 it lives inside the official `elasticsearch` Python client as `elasticsearch.dsl`.** | [→](elasticsearch-dsl-py.md) |
| **elasticsearch-sql** | Query Elasticsearch with SQL instead of its native JSON Query DSL — a community plugin (and library) that parses SQL and translates it into ES queries/aggregations, with version-matched releases tracking the ES major you run. | [→](elasticsearch-sql.md) |
| **go-mysql-elasticsearch** | A small Go service that syncs MySQL into Elasticsearch in real time: it does an initial dump, then tails the MySQL binlog as a fake replica and applies inserts/updates/deletes to ES indices per a mapping rule file. | [→](go-mysql-elasticsearch.md) |
| **python-mysql-replication** | A pure-Python implementation of the MySQL replication protocol (built on PyMySQL): connect as a fake replica, stream the binlog, and get parsed row/query/rotate events as Python objects — the building block under most Python CDC tooling for MySQL. | [→](python-mysql-replication.md) |
| **PrettyZoo** | A cross-platform desktop GUI for Apache ZooKeeper (Win/Mac/Linux) — browse the znode tree, view/edit node data, manage ACLs and connections, without dropping into the `zkCli.sh` shell. **Archived: the author publicly announced in 2023 that maintenance has stopped.** | [→](prettyzoo.md) |
| **RDR** | A fast, offline Redis RDB-file parser (written in Go despite the repo's reported language tag) that reveals which keys and key-prefixes are eating your memory — `rdr show` serves an HTML memory report on a local port, `rdr keys` dumps every key. | [→](rdr.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [PikiwiDB](pikiwidb.md) | ✅ | A Redis-protocol-compatible, disk-backed KV store (RocksDB engine) built by Qihoo360's infra team — keeps hot data in memory and persists the full dataset to disk so a single node can hold hundreds of GB the way Redis can't. (This repo is the home of the project historically known as **Pika**.) |
| [elasticsearch-dsl-py](elasticsearch-dsl-py.md) | ✅ | A high-level, Pythonic DSL over the low-level Elasticsearch client — query objects, a Document ORM-style mapping layer, and chainable search builders instead of hand-writing query JSON. **Archived: as of v8.18.0 it lives inside the official `elasticsearch` Python client as `elasticsearch.dsl`.** |
| [elasticsearch-sql](elasticsearch-sql.md) | ✅ | Query Elasticsearch with SQL instead of its native JSON Query DSL — a community plugin (and library) that parses SQL and translates it into ES queries/aggregations, with version-matched releases tracking the ES major you run. |
| [go-mysql-elasticsearch](go-mysql-elasticsearch.md) | ✅ | A small Go service that syncs MySQL into Elasticsearch in real time: it does an initial dump, then tails the MySQL binlog as a fake replica and applies inserts/updates/deletes to ES indices per a mapping rule file. |
| [python-mysql-replication](python-mysql-replication.md) | ✅ | A pure-Python implementation of the MySQL replication protocol (built on PyMySQL): connect as a fake replica, stream the binlog, and get parsed row/query/rotate events as Python objects — the building block under most Python CDC tooling for MySQL. |
| [PrettyZoo](prettyzoo.md) | ✅ | A cross-platform desktop GUI for Apache ZooKeeper (Win/Mac/Linux) — browse the znode tree, view/edit node data, manage ACLs and connections, without dropping into the `zkCli.sh` shell. **Archived: the author publicly announced in 2023 that maintenance has stopped.** |
| [RDR](rdr.md) | ✅ | A fast, offline Redis RDB-file parser (written in Go despite the repo's reported language tag) that reveals which keys and key-prefixes are eating your memory — `rdr show` serves an HTML memory report on a local port, `rdr keys` dumps every key. |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

Databases and the **tooling around them** — clients, admin GUIs, sync/replication, RDB analysis. Not RAG vector stores (see `rag-retrieval`).
