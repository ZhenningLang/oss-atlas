# debugging-proxy

> 分类节点。HTTP(S)/WebSocket 调试代理——抓取、检查、改写并 mock 流量。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **whistle** | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 | [→](whistle.zh.md) |
| **AnyProxy** | 一个用 Node.js 写的完全可配置 HTTP/HTTPS 中间人代理：把你机器（或移动设备）的流量路由穿过它，在 web UI 里检视、录制，并用 JS 规则文件改写请求/响应。阿里背书——但 master 分支自 2020 年中起就没动过。 | [→](anyproxy.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [whistle](whistle.zh.md) | ✅ | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 |
| [AnyProxy](anyproxy.zh.md) | ✅ | 一个用 Node.js 写的完全可配置 HTTP/HTTPS 中间人代理：把你机器（或移动设备）的流量路由穿过它，在 web UI 里检视、录制，并用 JS 规则文件改写请求/响应。阿里背书——但 master 分支自 2020 年中起就没动过。 |
| Charles / Fiddler / mitmproxy / anyproxy | 未收录 | 各页对比里点到的其他调试代理。 |

## 什么该放这里

主要职责是为开发与调试**抓取、检查、改写并 mock** HTTP(S)/WebSocket 流量的代理。不含生产 API/AI 网关(见 `api-gateway`)，不含爬虫代理池(见 `proxy-pool`)。
