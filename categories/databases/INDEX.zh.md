# databases

> 分类节点。数据库与数据库工具——客户端、GUI、同步，以及 Redis/ES 兼容存储。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **PikiwiDB** | 当大规模 Redis 数据集撑爆内存、内存成本成为主要负担时用它——RocksDB 落盘、兼容 Redis 协议，单节点可存数百 GB；但它以延迟换容量，若每次操作都要微秒级则不合适。 | [→](pikiwidb.zh.md) |
| **elasticsearch-dsl-py** | 当你维护仍锁定独立 elasticsearch-dsl 包的旧 Python 代码时才用它——任何新项目它都已归档，请改装 elasticsearch>=8.18 并使用 elasticsearch.dsl。 | [→](elasticsearch-dsl-py.zh.md) |
| **elasticsearch-sql** | 当熟悉 SQL 的团队想免学 JSON Query DSL 直接查 Elasticsearch 时用它——但 Elastic 官方的 SQL／ES\|QL 已与之重叠，能覆盖你的需求时优先用官方特性。 | [→](elasticsearch-sql.zh.md) |
| **go-mysql-elasticsearch** | 当你想用单个 Go 二进制 tail MySQL binlog、单向中等规模同步到 Elasticsearch 时用它——但它自 2023 年起无人维护、无任何发布，请当作 fork 自管的项目对待。 | [→](go-mysql-elasticsearch.zh.md) |
| **python-mysql-replication** | 当你想用纯 Python 原语把 MySQL binlog 流式解析成带类型的事件、自建可控 CDC 循环时用它——但 checkpoint、去重和精确一次投递全得你自己负责。 | [→](python-mysql-replication.zh.md) |
| **PrettyZoo** | 当你在开发或故障排查时想用友好的桌面 GUI 浏览并轻量编辑 ZooKeeper znode 树时用它——但它自 2023 年起已归档，新 JDK／macOS 可能跑不起来且无上游修复。 | [→](prettyzoo.zh.md) |
| **RDR** | 当 Redis 触发 maxmemory 告警、需要离线快速按前缀分析 RDB 快照时用它——但内存数字是近似值，且项目已停滞（v0.0.1，2019 年）。 | [→](rdr.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [PikiwiDB](pikiwidb.zh.md) | ✅ | 当大规模 Redis 数据集撑爆内存、内存成本成为主要负担时用它——RocksDB 落盘、兼容 Redis 协议，单节点可存数百 GB；但它以延迟换容量，若每次操作都要微秒级则不合适。 |
| [elasticsearch-dsl-py](elasticsearch-dsl-py.zh.md) | ✅ | 当你维护仍锁定独立 elasticsearch-dsl 包的旧 Python 代码时才用它——任何新项目它都已归档，请改装 elasticsearch>=8.18 并使用 elasticsearch.dsl。 |
| [elasticsearch-sql](elasticsearch-sql.zh.md) | ✅ | 当熟悉 SQL 的团队想免学 JSON Query DSL 直接查 Elasticsearch 时用它——但 Elastic 官方的 SQL／ES\|QL 已与之重叠，能覆盖你的需求时优先用官方特性。 |
| [go-mysql-elasticsearch](go-mysql-elasticsearch.zh.md) | ✅ | 当你想用单个 Go 二进制 tail MySQL binlog、单向中等规模同步到 Elasticsearch 时用它——但它自 2023 年起无人维护、无任何发布，请当作 fork 自管的项目对待。 |
| [python-mysql-replication](python-mysql-replication.zh.md) | ✅ | 当你想用纯 Python 原语把 MySQL binlog 流式解析成带类型的事件、自建可控 CDC 循环时用它——但 checkpoint、去重和精确一次投递全得你自己负责。 |
| [PrettyZoo](prettyzoo.zh.md) | ✅ | 当你在开发或故障排查时想用友好的桌面 GUI 浏览并轻量编辑 ZooKeeper znode 树时用它——但它自 2023 年起已归档，新 JDK／macOS 可能跑不起来且无上游修复。 |
| [RDR](rdr.zh.md) | ✅ | 当 Redis 触发 maxmemory 告警、需要离线快速按前缀分析 RDB 快照时用它——但内存数字是近似值，且项目已停滞（v0.0.1，2019 年）。 |
| （各页对比里点到的替代品） | 未收录 | 详见各页 Comparison。 |

## 什么该放这里

数据库及其**周边工具**——客户端、管理 GUI、同步/复制、RDB 分析。不含 RAG 向量库（见 `rag-retrieval`）。
