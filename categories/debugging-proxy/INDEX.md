# debugging-proxy

> Category node. HTTP(S)/WebSocket debugging proxies — capture, inspect, rewrite, and mock traffic.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **whistle** | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. | [→](whistle.md) |
| **AnyProxy** | Use it when you want a scriptable Node.js MITM proxy to inspect and rewrite HTTP/HTTPS traffic in plain JS rules — but master is frozen since 2020, so prefer whistle for new work. | [→](anyproxy.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [whistle](whistle.md) | ✅ | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. |
| [AnyProxy](anyproxy.md) | ✅ | Use it when you want a scriptable Node.js MITM proxy to inspect and rewrite HTTP/HTTPS traffic in plain JS rules — but master is frozen since 2020, so prefer whistle for new work. |
| Charles / Fiddler / mitmproxy / anyproxy | 未收录 | Other debugging proxies named across the pages. |

## What belongs here

Proxies whose primary job is **capturing, inspecting, rewriting, and mocking** HTTP(S)/WebSocket traffic for development and debugging. Not production API/AI gateways (see `api-gateway`), not scraping proxy pools (see `proxy-pool`).
