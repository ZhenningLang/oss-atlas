# proxy-pool

> Category node. Self-hosted rotating proxy-IP pools for web scraping.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **proxy_pool** | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. | [→](proxy-pool.md) |
| **ProxyBroker** | Use it when you need a throwaway pool of free public proxies for a low-stakes prototype via a single rotating local endpoint — but it's effectively frozen since ~2018 and widely breaks on modern Python without pinning. | [→](proxybroker.md) |
| **Scylla** | Use it when you want an always-on, self-hosted free-proxy pool with a JSON API, quality scoring, and dashboard via one Docker command — but its forward proxy can't do HTTPS, and releases stalled since 2022. | [→](scylla.md) |
| **haipproxy** | Use it when you genuinely need a distributed, high-availability free-proxy pool for large multi-machine crawls on Scrapy+Redis — but it's dormant since 2022, runs 2018-era Py2/3 code, and is the heaviest pool to operate. | [→](haipproxy.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [proxy_pool](proxy-pool.md) | ✅ | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. |
| [ProxyBroker](proxybroker.md) | ✅ | Use it when you need a throwaway pool of free public proxies for a low-stakes prototype via a single rotating local endpoint — but it's effectively frozen since ~2018 and widely breaks on modern Python without pinning. |
| [Scylla](scylla.md) | ✅ | Use it when you want an always-on, self-hosted free-proxy pool with a JSON API, quality scoring, and dashboard via one Docker command — but its forward proxy can't do HTTPS, and releases stalled since 2022. |
| [haipproxy](haipproxy.md) | ✅ | Use it when you genuinely need a distributed, high-availability free-proxy pool for large multi-machine crawls on Scrapy+Redis — but it's dormant since 2022, runs 2018-era Py2/3 code, and is the heaviest pool to operate. |
| ProxyBroker / scylla / paid residential proxies | 未收录 | Other proxy pools & paid proxy services named across the pages. |

## What belongs here

Self-hosted **rotating proxy-IP pools** for web scraping. Not scraping frameworks themselves, not web/browser automation (see `web-automation`).
