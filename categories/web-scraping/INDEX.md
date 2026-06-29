# web-scraping

> Category node. Fetch and extract content/structure from web pages — article extraction and HTML parsing.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **newspaper** | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. | B (5/6) | [→](newspaper.md) |
| **requests-html** | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. | D (3/6) | [→](requests-html.md) |
| **Readability.js** | Use it when you need to strip a web page down to just the article (title, byline, body) using Firefox Reader View's battle-tested engine — but it parses a DOM you supply; it won't fetch URLs or render JS-heavy SPAs. | B (4/6) | [→](readability-js.md) |
| **python-readability** | Use it when your Python pipeline needs fast lxml article extraction from already-fetched HTML with no browser or Node — but it's single-maintainer and slow-cadence, and trafilatura often scores better on extraction benchmarks. | B (3/6) | [→](python-readability.md) |
| **dragnet** | Use it when you have labeled data and want a trainable ML extractor that also separates article from user comments — but it's near-dormant with aging pins (`scikit-learn<0.21`, `ftfy<5`) that make installing on modern stacks painful. | D (4/6) | [→](dragnet.md) |
| **boilerpipe** | Use it when you specifically need a JVM-native, dependency-light classic-algorithm article extractor — but the repo is effectively abandoned (last push 2018-01) with aged vendored deps and no security fixes coming. | ? (2/6) | [→](boilerpipe.md) |
| **fuck-login** | Use it when you want to read 2016-era examples of how site logins (CSRF/RSA/captcha) were scripted — but it's abandoned since 2018, unlicensed, and the scripts are broken today. | E (5/6) | [→](fuck-login.md) |
| **gopup** | Use it when you need a quick one-line pull of Chinese public data (search indices, CPI, Shibor) into a pandas DataFrame for academic research — but it's coasting since 2023, unlicensed, and scrapers rot as sources change. | E (3/6) | [→](gopup.md) |
| **PRAW** | Use it when your data source is Reddit and you want the official OAuth-compliant path with rate-limit handling built in — but Reddit's own API terms, quotas, and pricing bound what you can do, not the library. | B (6/6) | [→](praw.md) |
| **Scrapyd** | Use it when you need to deploy local Scrapy spiders to a server and drive scheduled, versioned crawls over an HTTP API — but it only runs Scrapy and ships unauthenticated, so add auth before exposing port 6800. | B (5/6) | [→](scrapyd.md) |
| **SpiderKeeper** | Use it when a small team running Scrapyd wants the simplest browser dashboard to deploy and cron-schedule spiders — but it's stale since 2023 with default admin/admin auth, so don't expose it untrusted. | E (3/6) | [→](spiderkeeper.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [newspaper](newspaper.md) | ✅ | B (5/6) | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. |
| [requests-html](requests-html.md) | ✅ | D (3/6) | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. |
| [Readability.js](readability-js.md) | ✅ | B (4/6) | Use it when you need to strip a web page down to just the article (title, byline, body) using Firefox Reader View's battle-tested engine — but it parses a DOM you supply; it won't fetch URLs or render JS-heavy SPAs. |
| [python-readability](python-readability.md) | ✅ | B (3/6) | Use it when your Python pipeline needs fast lxml article extraction from already-fetched HTML with no browser or Node — but it's single-maintainer and slow-cadence, and trafilatura often scores better on extraction benchmarks. |
| [dragnet](dragnet.md) | ✅ | D (4/6) | Use it when you have labeled data and want a trainable ML extractor that also separates article from user comments — but it's near-dormant with aging pins (`scikit-learn<0.21`, `ftfy<5`) that make installing on modern stacks painful. |
| [boilerpipe](boilerpipe.md) | ✅ | ? (2/6) | Use it when you specifically need a JVM-native, dependency-light classic-algorithm article extractor — but the repo is effectively abandoned (last push 2018-01) with aged vendored deps and no security fixes coming. |
| [fuck-login](fuck-login.md) | ✅ | E (5/6) | Use it when you want to read 2016-era examples of how site logins (CSRF/RSA/captcha) were scripted — but it's abandoned since 2018, unlicensed, and the scripts are broken today. |
| [gopup](gopup.md) | ✅ | E (3/6) | Use it when you need a quick one-line pull of Chinese public data (search indices, CPI, Shibor) into a pandas DataFrame for academic research — but it's coasting since 2023, unlicensed, and scrapers rot as sources change. |
| [PRAW](praw.md) | ✅ | B (6/6) | Use it when your data source is Reddit and you want the official OAuth-compliant path with rate-limit handling built in — but Reddit's own API terms, quotas, and pricing bound what you can do, not the library. |
| [Scrapyd](scrapyd.md) | ✅ | B (5/6) | Use it when you need to deploy local Scrapy spiders to a server and drive scheduled, versioned crawls over an HTTP API — but it only runs Scrapy and ships unauthenticated, so add auth before exposing port 6800. |
| [SpiderKeeper](spiderkeeper.md) | ✅ | E (3/6) | Use it when a small team running Scrapyd wants the simplest browser dashboard to deploy and cron-schedule spiders — but it's stale since 2023 with default admin/admin auth, so don't expose it untrusted. |
| Scrapy / trafilatura / httpx + BeautifulSoup / Playwright | 未收录 | — | Other scraping/extraction tools named across the pages. |

## What belongs here

Tools whose primary job is **fetching web pages and extracting content/structure** — article-text extraction and HTML parsing. Not browser-driving automation (see `web-automation`), not scraping proxy pools (see `proxy-pool`).
