# proxy-pool

> Category node. Self-hosted rotating proxy-IP pools for web scraping.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **proxy_pool** | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. | [→](proxy-pool.md) |
| **ProxyBroker** | An async Python tool that finds public proxies from ~50 sources, checks them (type, anonymity, latency, country, DNSBL), and can run as a self-rotating proxy server in front of your traffic. | [→](proxybroker.md) |
| **Scylla** | A self-hosted "intelligent proxy pool" app that continuously crawls public proxies, validates and scores them (latency, stability, anonymity), and exposes them via a web UI, a JSON API, and a built-in forward-proxy server. | [→](scylla.md) |
| **haipproxy** | A distributed, high-availability IP proxy pool built on Scrapy + Redis — crawlers harvest public proxies, validators score them, and consumers pull low-latency proxies via a Python client or a Squid integration. | [→](haipproxy.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [proxy_pool](proxy-pool.md) | ✅ | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. |
| [ProxyBroker](proxybroker.md) | ✅ | An async Python tool that finds public proxies from ~50 sources, checks them (type, anonymity, latency, country, DNSBL), and can run as a self-rotating proxy server in front of your traffic. |
| [Scylla](scylla.md) | ✅ | A self-hosted "intelligent proxy pool" app that continuously crawls public proxies, validates and scores them (latency, stability, anonymity), and exposes them via a web UI, a JSON API, and a built-in forward-proxy server. |
| [haipproxy](haipproxy.md) | ✅ | A distributed, high-availability IP proxy pool built on Scrapy + Redis — crawlers harvest public proxies, validators score them, and consumers pull low-latency proxies via a Python client or a Squid integration. |
| ProxyBroker / scylla / paid residential proxies | 未收录 | Other proxy pools & paid proxy services named across the pages. |

## What belongs here

Self-hosted **rotating proxy-IP pools** for web scraping. Not scraping frameworks themselves, not web/browser automation (see `web-automation`).
