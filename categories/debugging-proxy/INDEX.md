# debugging-proxy

> Category node. HTTP(S)/WebSocket debugging proxies — capture, inspect, rewrite, and mock traffic.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **whistle** | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. | [→](whistle.md) |
| **AnyProxy** | A fully configurable HTTP/HTTPS man-in-the-middle proxy in Node.js: route your machine's (or a mobile device's) traffic through it to inspect it in a web UI, record it, and rewrite requests/responses with JS rule files. Alibaba-backed — but the master branch hasn't moved since mid-2020. | [→](anyproxy.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [whistle](whistle.md) | ✅ | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. |
| [AnyProxy](anyproxy.md) | ✅ | A fully configurable HTTP/HTTPS man-in-the-middle proxy in Node.js: route your machine's (or a mobile device's) traffic through it to inspect it in a web UI, record it, and rewrite requests/responses with JS rule files. Alibaba-backed — but the master branch hasn't moved since mid-2020. |
| Charles / Fiddler / mitmproxy / anyproxy | 未收录 | Other debugging proxies named across the pages. |

## What belongs here

Proxies whose primary job is **capturing, inspecting, rewriting, and mocking** HTTP(S)/WebSocket traffic for development and debugging. Not production API/AI gateways (see `api-gateway`), not scraping proxy pools (see `proxy-pool`).
