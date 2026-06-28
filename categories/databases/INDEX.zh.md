# databases

> 分类节点。数据库与数据库工具——客户端、GUI、同步，以及 Redis/ES 兼容存储。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **PikiwiDB** | 一个兼容 Redis 协议、落盘的 KV 存储（RocksDB 引擎），由 Qihoo360 基础架构团队打造——热数据留在内存，全量数据持久化到磁盘，于是单节点能装下 Redis 装不下的几百 GB。（本仓库就是历史上称为 **Pika** 的项目所在地。） | [→](pikiwidb.zh.md) |
| **elasticsearch-dsl-py** | 一层架在底层 Elasticsearch 客户端之上的高层、Pythonic DSL——用查询对象、类 ORM 的 Document 映射层和可链式的搜索构建器，取代手写查询 JSON。**已归档：自 v8.18.0 起，它已并入官方 `elasticsearch` Python 客户端，作为 `elasticsearch.dsl`。** | [→](elasticsearch-dsl-py.zh.md) |
| **elasticsearch-sql** | 用 SQL 而非原生 JSON Query DSL 查询 Elasticsearch——一个社区插件（兼库），把 SQL 解析并翻译成 ES 查询／聚合，发布版与你所跑的 ES 大版本对齐。 | [→](elasticsearch-sql.zh.md) |
| **go-mysql-elasticsearch** | 一个小巧的 Go 服务，实时把 MySQL 同步进 Elasticsearch：先做一次初始 dump，再以伪从库身份 tail MySQL binlog，按一份映射规则文件把 insert／update／delete 应用到 ES 索引。 | [→](go-mysql-elasticsearch.zh.md) |
| **python-mysql-replication** | MySQL 复制协议的纯 Python 实现（构建于 PyMySQL）：以伪从库身份连接、流式读取 binlog，把解析后的 row／query／rotate 事件作为 Python 对象交给你——大多数 Python MySQL CDC 工具底下的那块积木。 | [→](python-mysql-replication.zh.md) |
| **PrettyZoo** | 一个跨平台的 Apache ZooKeeper 桌面 GUI（Win／Mac／Linux）——浏览 znode 树、查看／编辑节点数据、管理 ACL 与连接，无需跌进 `zkCli.sh` shell。**已归档：作者于 2023 年公开宣布停止维护。** | [→](prettyzoo.zh.md) |
| **RDR** | 一个快速的离线 Redis RDB 文件解析器（尽管仓库标注语言为 JavaScript，核心其实是 Go 写的），用来揭示哪些 key 和 key 前缀在吃内存——`rdr show` 在本地端口起一个 HTML 内存报告，`rdr keys` 把所有 key 导出。 | [→](rdr.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [PikiwiDB](pikiwidb.zh.md) | ✅ | 一个兼容 Redis 协议、落盘的 KV 存储（RocksDB 引擎），由 Qihoo360 基础架构团队打造——热数据留在内存，全量数据持久化到磁盘，于是单节点能装下 Redis 装不下的几百 GB。（本仓库就是历史上称为 **Pika** 的项目所在地。） |
| [elasticsearch-dsl-py](elasticsearch-dsl-py.zh.md) | ✅ | 一层架在底层 Elasticsearch 客户端之上的高层、Pythonic DSL——用查询对象、类 ORM 的 Document 映射层和可链式的搜索构建器，取代手写查询 JSON。**已归档：自 v8.18.0 起，它已并入官方 `elasticsearch` Python 客户端，作为 `elasticsearch.dsl`。** |
| [elasticsearch-sql](elasticsearch-sql.zh.md) | ✅ | 用 SQL 而非原生 JSON Query DSL 查询 Elasticsearch——一个社区插件（兼库），把 SQL 解析并翻译成 ES 查询／聚合，发布版与你所跑的 ES 大版本对齐。 |
| [go-mysql-elasticsearch](go-mysql-elasticsearch.zh.md) | ✅ | 一个小巧的 Go 服务，实时把 MySQL 同步进 Elasticsearch：先做一次初始 dump，再以伪从库身份 tail MySQL binlog，按一份映射规则文件把 insert／update／delete 应用到 ES 索引。 |
| [python-mysql-replication](python-mysql-replication.zh.md) | ✅ | MySQL 复制协议的纯 Python 实现（构建于 PyMySQL）：以伪从库身份连接、流式读取 binlog，把解析后的 row／query／rotate 事件作为 Python 对象交给你——大多数 Python MySQL CDC 工具底下的那块积木。 |
| [PrettyZoo](prettyzoo.zh.md) | ✅ | 一个跨平台的 Apache ZooKeeper 桌面 GUI（Win／Mac／Linux）——浏览 znode 树、查看／编辑节点数据、管理 ACL 与连接，无需跌进 `zkCli.sh` shell。**已归档：作者于 2023 年公开宣布停止维护。** |
| [RDR](rdr.zh.md) | ✅ | 一个快速的离线 Redis RDB 文件解析器（尽管仓库标注语言为 JavaScript，核心其实是 Go 写的），用来揭示哪些 key 和 key 前缀在吃内存——`rdr show` 在本地端口起一个 HTML 内存报告，`rdr keys` 把所有 key 导出。 |
| (各页对比里点到的替代品) | 未收录 | 详见各页 Comparison。 |

## 什么该放这里

数据库及其**周边工具**——客户端、管理 GUI、同步/复制、RDB 分析。不含 RAG 向量库(见 `rag-retrieval`)。
