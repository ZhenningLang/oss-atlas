# web-scraping

> Category node. Fetch and extract content/structure from web pages — article extraction and HTML parsing.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **newspaper** | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. | [→](newspaper.md) |
| **requests-html** | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. | [→](requests-html.md) |
| **Readability.js** | The standalone version of the readability library behind Firefox Reader View — give it a DOM document, get back the article's title, byline, and cleaned main content with the navigation, ads, and boilerplate stripped out. | [→](readability-js.md) |
| **python-readability** | A fast, lxml-based Python port of arc90's Readability — hand it an HTML document and it returns the cleaned main body (`summary()`) and the title (`title()`), stripping nav, ads, and boilerplate. | [→](python-readability.md) |
| **dragnet** | A machine-learning approach to web content extraction — trained models pull the main article (and optionally user comments) out of a page's HTML, using diverse text/markup features rather than hand-tuned heuristics. | [→](dragnet.md) |
| **boilerpipe** | A Java library for boilerplate removal and full-text extraction from HTML — the classic, algorithm-driven approach (shallow text features, link density, tag ratios) that pulls the article out and drops navigation, ads, and surrounding clutter. | [→](boilerpipe.md) |
| **fuck-login** | A collection of ~20 Python scripts that script the login flow of well-known (mostly Chinese) websites — Zhihu, Weibo, Baidu, JD, Bilibili, GitHub, Douban — so you can carry the resulting session cookies into a scraper. A 2016-era teaching repo, explicitly **no longer maintained**. | [→](fuck-login.md) |
| **gopup** | A Python library that wraps a grab-bag of (mostly Chinese) public data sources behind one-line calls returning pandas DataFrames — Baidu/Weibo/Google search indices, Chinese macro indicators (CPI/PPI/PMI, money supply, FX rates), Shibor/LPR rates, unicorn-company lists, box-office and epidemic data, and more. | [→](gopup.md) |
| **PRAW** | The "Python Reddit API Wrapper" — a Python package that gives you typed, Pythonic objects (Submission, Comment, Subreddit, Redditor) over Reddit's official OAuth API, and handles rate-limit compliance so you don't have to sprinkle `sleep` calls in your code. | [→](praw.md) |
| **Scrapyd** | A service daemon for deploying and running Scrapy spiders over a JSON HTTP API — eggify a Scrapy project, upload it, and schedule/cancel/monitor crawl jobs remotely. The canonical "run Scrapy in production" daemon, from the Scrapy org itself. | [→](scrapyd.md) |
| **SpiderKeeper** | A Flask-based admin web UI / dashboard for Scrapy spiders that sits on top of Scrapyd — deploy projects, schedule periodic jobs, and watch run stats from a browser. It crawls nothing itself; it's a management layer over one or more Scrapyd servers. Lightweight, popular, and largely stale. | [→](spiderkeeper.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [newspaper](newspaper.md) | ✅ | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. |
| [requests-html](requests-html.md) | ✅ | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. |
| [Readability.js](readability-js.md) | ✅ | The standalone version of the readability library behind Firefox Reader View — give it a DOM document, get back the article's title, byline, and cleaned main content with the navigation, ads, and boilerplate stripped out. |
| [python-readability](python-readability.md) | ✅ | A fast, lxml-based Python port of arc90's Readability — hand it an HTML document and it returns the cleaned main body (`summary()`) and the title (`title()`), stripping nav, ads, and boilerplate. |
| [dragnet](dragnet.md) | ✅ | A machine-learning approach to web content extraction — trained models pull the main article (and optionally user comments) out of a page's HTML, using diverse text/markup features rather than hand-tuned heuristics. |
| [boilerpipe](boilerpipe.md) | ✅ | A Java library for boilerplate removal and full-text extraction from HTML — the classic, algorithm-driven approach (shallow text features, link density, tag ratios) that pulls the article out and drops navigation, ads, and surrounding clutter. |
| [fuck-login](fuck-login.md) | ✅ | A collection of ~20 Python scripts that script the login flow of well-known (mostly Chinese) websites — Zhihu, Weibo, Baidu, JD, Bilibili, GitHub, Douban — so you can carry the resulting session cookies into a scraper. A 2016-era teaching repo, explicitly **no longer maintained**. |
| [gopup](gopup.md) | ✅ | A Python library that wraps a grab-bag of (mostly Chinese) public data sources behind one-line calls returning pandas DataFrames — Baidu/Weibo/Google search indices, Chinese macro indicators (CPI/PPI/PMI, money supply, FX rates), Shibor/LPR rates, unicorn-company lists, box-office and epidemic data, and more. |
| [PRAW](praw.md) | ✅ | The "Python Reddit API Wrapper" — a Python package that gives you typed, Pythonic objects (Submission, Comment, Subreddit, Redditor) over Reddit's official OAuth API, and handles rate-limit compliance so you don't have to sprinkle `sleep` calls in your code. |
| [Scrapyd](scrapyd.md) | ✅ | A service daemon for deploying and running Scrapy spiders over a JSON HTTP API — eggify a Scrapy project, upload it, and schedule/cancel/monitor crawl jobs remotely. The canonical "run Scrapy in production" daemon, from the Scrapy org itself. |
| [SpiderKeeper](spiderkeeper.md) | ✅ | A Flask-based admin web UI / dashboard for Scrapy spiders that sits on top of Scrapyd — deploy projects, schedule periodic jobs, and watch run stats from a browser. It crawls nothing itself; it's a management layer over one or more Scrapyd servers. Lightweight, popular, and largely stale. |
| Scrapy / trafilatura / httpx + BeautifulSoup / Playwright | 未收录 | Other scraping/extraction tools named across the pages. |

## What belongs here

Tools whose primary job is **fetching web pages and extracting content/structure** — article-text extraction and HTML parsing. Not browser-driving automation (see `web-automation`), not scraping proxy pools (see `proxy-pool`).
