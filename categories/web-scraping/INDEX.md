# web-scraping

> Category node. Fetch and extract content/structure from web pages — article extraction and HTML parsing.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **newspaper** | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. | [→](newspaper.md) |
| **requests-html** | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. | [→](requests-html.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [newspaper](newspaper.md) | ✅ | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. |
| [requests-html](requests-html.md) | ✅ | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. |
| Scrapy / trafilatura / httpx + BeautifulSoup / Playwright | 未收录 | Other scraping/extraction tools named across the pages. |

## What belongs here

Tools whose primary job is **fetching web pages and extracting content/structure** — article-text extraction and HTML parsing. Not browser-driving automation (see `web-automation`), not scraping proxy pools (see `proxy-pool`).
