# media-download

> Category node. Download video/audio from streaming sites via CLI or library.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **youtube-dl** | Use it when you need a battle-tested CLI/library to download video & audio from YouTube and 1000+ sites — but prefer the active yt-dlp fork for hot sites. | [→](youtube-dl.md) |
| **you-get** | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. | [→](you-get.md) |
| **cobalt** | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. | [→](cobalt.md) |
| **lux** | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. | [→](lux.md) |
| **youtube-transcript-api** | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. | [→](youtube-transcript-api.md) |
| **bulk-downloader-for-reddit** | Use it when you want a scriptable, reproducible Reddit archive of files plus metadata via OAuth — but Reddit's ~1000-post listing cap is unbypassable, and releases have stalled since early 2023 (GPL-3.0). | [→](bulk-downloader-for-reddit.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [youtube-dl](youtube-dl.md) | ✅ | Battle-tested extractor for 1000+ sites; upstream has slowed, so treat yt-dlp as the live fork for YouTube. |
| [you-get](you-get.md) | ✅ | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. |
| [cobalt](cobalt.md) | ✅ | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. |
| [lux](lux.md) | ✅ | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. |
| [youtube-transcript-api](youtube-transcript-api.md) | ✅ | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. |
| [bulk-downloader-for-reddit](bulk-downloader-for-reddit.md) | ✅ | Use it when you want a scriptable, reproducible Reddit archive of files plus metadata via OAuth — but Reddit's ~1000-post listing cap is unbypassable, and releases have stalled since early 2023 (GPL-3.0). |
| yt-dlp / gallery-dl | 未收录 | More-active forks and alternative downloaders named across the pages. |

## What belongs here

Tools whose primary job is **fetching media from streaming/hosting sites** (extractors, downloaders). Not media transcoding/encoding (see `media-processing`), not generic file servers (see `document-management`).
