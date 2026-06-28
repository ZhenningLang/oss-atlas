# media-download

> 分类节点。通过 CLI 或库从流媒体站点下载音视频。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **youtube-dl** | 当你需要一个久经考验的 CLI/库从 YouTube 和 1000+ 站点下载音视频时用它——但热门站点优先用更活跃的 yt-dlp 分叉。 | [→](youtube-dl.zh.md) |
| **you-get** | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 | [→](you-get.zh.md) |
| **cobalt** | 当你想要一个干净、可自托管、带 Web UI 和 API、无广告无追踪的媒体下载器时用它——不是可脚本化的 CLI。 | [→](cobalt.zh.md) |
| **lux** | 当你想要一个快速的单二进制 Go 下载器、对中文视频站点支持好时用它——站点覆盖与更新都不如 yt-dlp。 | [→](lux.zh.md) |
| **youtube-transcript-api** | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 | [→](youtube-transcript-api.zh.md) |
| **bulk-downloader-for-reddit** | 当你想通过 OAuth 做可脚本化、可复现的 Reddit 文件加元数据归档时用它——但 Reddit 约 1000 帖的列表上限无法绕过，且发布自 2023 年初已停滞（GPL-3.0）。 | [→](bulk-downloader-for-reddit.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [youtube-dl](youtube-dl.zh.md) | ✅ | 覆盖 1000+ 站点的老牌提取器；上游已放缓，YouTube 实际请用活跃分叉 yt-dlp。 |
| [you-get](you-get.zh.md) | ✅ | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 |
| [cobalt](cobalt.zh.md) | ✅ | 当你想要一个干净、可自托管、带 Web UI 和 API、无广告无追踪的媒体下载器时用它——不是可脚本化的 CLI。 |
| [lux](lux.zh.md) | ✅ | 当你想要一个快速的单二进制 Go 下载器、对中文视频站点支持好时用它——站点覆盖与更新都不如 yt-dlp。 |
| [youtube-transcript-api](youtube-transcript-api.zh.md) | ✅ | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 |
| [bulk-downloader-for-reddit](bulk-downloader-for-reddit.zh.md) | ✅ | 当你想通过 OAuth 做可脚本化、可复现的 Reddit 文件加元数据归档时用它——但 Reddit 约 1000 帖的列表上限无法绕过，且发布自 2023 年初已停滞（GPL-3.0）。 |
| yt-dlp / gallery-dl | 未收录 | 各页对比里点到的更活跃分叉与其他下载器。 |

## 什么该放这里

主要职责是**从流媒体/托管站点抓取媒体**的工具（提取器、下载器）。不含媒体转码/编码（见 `media-processing`），不含通用文件服务器（见 `document-management`）。
