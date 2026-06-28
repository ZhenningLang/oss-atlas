# api-gateway

> 分类节点。路由、保护、限流并治理服务与 LLM 流量的 API / AI 网关。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Kong Gateway** | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 | [→](kong.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Kong Gateway](kong.zh.md) | ✅ | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 |
| Tyk / KrakenD / Envoy / APISIX | 未收录 | 页面里点到的其他 API 网关。 |

## 什么该放这里

挡在服务或 LLM 前面、做路由/鉴权/限流/可观测的 **API / AI 网关**。不含 agent 框架（见 `agent-frameworks`）。
