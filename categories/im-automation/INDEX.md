# im-automation

> Category node. Instant-messaging bots & automation (WeChat and other IM platforms).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ItChat** | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. | C (4/6) | [→](itchat.md) |
| **WeChatPlugin-MacOS** | Avoid for current WeChat — a macOS WeChat.app binary tweak that breaks on every WeChat update and is ~2y idle; account-ban & security risk. | D (3/6) | [→](wechatplugin-macos.md) |
| **wxpy** | Study it only as legacy WeChat-bot code — archived since 2019 and built on the now-defunct WeChat web protocol, so it mostly doesn't work. | D (5/6) | [→](wxpy.md) |
| **wxappUnpacker** | Use it when you must decompile a WeChat .wxapkg bundle you own back into readable source — but this exact repo is an empty tombstone, so grab a live fork instead. | E (4/6) | [→](wxappunpacker.md) |
| **Douyin-Bot** | Use it only as a historical reference for ADB screen-coordinate phone automation — never deploy it, its 2018 coordinates and dead Tencent face API mean it no longer works. | D (3/6) | [→](douyin-bot.md) |
| **WeChat Bot** | Use it for a maintained multi-channel Node.js CLI with many LLM backends and local chat analysis, only if you accept that its unofficial personal-WeChat path can trigger warnings or bans. | B (5/6) | [→](wechat-bot.md) |
| **ChatGPT-wechat-bot** | Use it only as a compact 2022–2023 Wechaty/ChatGPT reference; it is stale, hard-codes an old model path, and exposes a personal WeChat account to unofficial-puppet risk. | D (3/6) | [→](chatgpt-wechat-bot.md) |
| **OpeniLink Hub** | Use it when several iLink-connected WeChat bots need a self-hosted control plane, persistence, tracing, and Apps; it is young and explicitly not affiliated with or endorsed by iLink's official team. | B (5/6) | [→](openilink-hub.md) |
| **Dify Enterprise WeChat Bot** | Use it only for an isolated Windows prototype pinned to a specific Enterprise WeChat client; the message path includes a closed binary, Workflow support is unfinished, and the project is stale. | C (3/6) | [→](dify-enterprise-wechat-bot.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [ItChat](itchat.md) | ✅ | C (4/6) | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. |
| [WeChatPlugin-MacOS](wechatplugin-macos.md) | ✅ | D (3/6) | Avoid for current WeChat — a macOS WeChat.app binary tweak that breaks on every WeChat update and is ~2y idle; account-ban & security risk. |
| [wxpy](wxpy.md) | ✅ | D (5/6) | Study it only as legacy WeChat-bot code — archived since 2019 and built on the now-defunct WeChat web protocol, so it mostly doesn't work. |
| [wxappUnpacker](wxappunpacker.md) | ✅ | E (4/6) | Use it when you must decompile a WeChat .wxapkg bundle you own back into readable source — but this exact repo is an empty tombstone, so grab a live fork instead. |
| [Douyin-Bot](douyin-bot.md) | ✅ | D (3/6) | Use it only as a historical reference for ADB screen-coordinate phone automation — never deploy it, its 2018 coordinates and dead Tencent face API mean it no longer works. |
| [WeChat Bot](wechat-bot.md) | ✅ | B (5/6) | Maintained multi-channel CLI and model adapters, but the unofficial personal-WeChat route carries warning and ban risk. |
| [ChatGPT-wechat-bot](chatgpt-wechat-bot.md) | ✅ | D (3/6) | Small historical Wechaty/ChatGPT example, now stale and still dependent on an unsupported personal-account path. |
| [OpeniLink Hub](openilink-hub.md) | ✅ | B (5/6) | Young multi-bot control plane with persistence, tracing, and Apps, without official iLink affiliation or endorsement. |
| [Dify Enterprise WeChat Bot](dify-enterprise-wechat-bot.md) | ✅ | C (3/6) | Fixed-version Windows Enterprise WeChat bridge to Dify whose helper is a closed binary and whose Workflow path is unfinished. |
| Wechaty / WeCom official APIs / CowAgent / WeChatFerry / Dify-on-WeChat / OpeniLink SDKs | 未收录 | — | Framework, official-channel, client-injection, and focused SDK alternatives named across the pages. |

## What belongs here

Bots and automation for **instant-messaging platforms** (WeChat and other IM). Not web/browser automation (see `web-automation`), not team-chat apps (see `team-chat`).
