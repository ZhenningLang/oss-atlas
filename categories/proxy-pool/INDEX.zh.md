# proxy-pool

> 分类节点。面向网络爬虫的自托管轮换代理 IP 池。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **proxy_pool** | 当爬虫需要一个走简单 API 的轮换免费代理 IP 池时用它——前提是接受免费代理不稳定、不安全。 | [→](proxy-pool.zh.md) |
| **ProxyBroker** | 一个异步 Python 工具，从约 50 个来源找公开代理、检查它们（类型、匿名度、延迟、国家、DNSBL），并能作为一个自轮换的代理服务器挡在你的流量前面。 | [→](proxybroker.zh.md) |
| **Scylla** | 一个自托管的「智能代理池」应用，持续爬取公开代理、校验并打分（延迟、稳定性、匿名度），再经网页 UI、JSON API 和内置正向代理服务器把它们暴露出来。 | [→](scylla.zh.md) |
| **haipproxy** | 一个基于 Scrapy + Redis 的分布式高可用 IP 代理池——爬虫收割公开代理，校验器给它们打分，消费者经一个 Python 客户端或 Squid 集成拉取低延迟代理。 | [→](haipproxy.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [proxy_pool](proxy-pool.zh.md) | ✅ | 当爬虫需要一个走简单 API 的轮换免费代理 IP 池时用它——前提是接受免费代理不稳定、不安全。 |
| [ProxyBroker](proxybroker.zh.md) | ✅ | 一个异步 Python 工具，从约 50 个来源找公开代理、检查它们（类型、匿名度、延迟、国家、DNSBL），并能作为一个自轮换的代理服务器挡在你的流量前面。 |
| [Scylla](scylla.zh.md) | ✅ | 一个自托管的「智能代理池」应用，持续爬取公开代理、校验并打分（延迟、稳定性、匿名度），再经网页 UI、JSON API 和内置正向代理服务器把它们暴露出来。 |
| [haipproxy](haipproxy.zh.md) | ✅ | 一个基于 Scrapy + Redis 的分布式高可用 IP 代理池——爬虫收割公开代理，校验器给它们打分，消费者经一个 Python 客户端或 Squid 集成拉取低延迟代理。 |
| ProxyBroker / scylla / paid residential proxies | 未收录 | 各页对比里点到的其他代理池与付费代理服务。 |

## 什么该放这里

面向网络爬虫的自托管**轮换代理 IP 池**。不含爬虫框架本身，不含 Web/浏览器自动化(见 `web-automation`)。
