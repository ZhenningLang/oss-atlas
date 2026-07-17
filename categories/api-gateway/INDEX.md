# api-gateway

> Category node. API / AI gateways that route, secure, rate-limit, and govern service and LLM traffic.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Kong Gateway** | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. | A (5/6) | [→](kong.md) |
| **Funtool** | Use it only for the exact Windows + Claude Code + NVIDIA proxy path when a prebuilt tool matters more than auditability; the current release is binary-only and cannot be rebuilt from published source. | C (5/6) | [→](funtool.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Kong Gateway](kong.md) | ✅ | A (5/6) | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. |
| [Funtool](funtool.md) | ✅ | C (5/6) | Narrow Windows proxy for Claude Code and NVIDIA models whose current implementation is distributed as an opaque binary rather than auditable source. |
| Tyk / KrakenD / Envoy / APISIX / LiteLLM / claude-code-router / CLIProxyAPI / New API | 未收录 | — | General API gateways and source-available LLM or coding-agent routing alternatives named across the pages. |

## What belongs here

**API / AI gateways** that sit in front of services or LLMs to route, secure, rate-limit, and observe traffic. Not agent frameworks (see `agent-frameworks`).
