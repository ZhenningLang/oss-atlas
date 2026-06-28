---
name: newspaper
slug: newspaper
repo: https://github.com/codelucas/newspaper
category: web-scraping
tags: [article-extraction, news, web-scraping, nlp, content-extraction, metadata, python]
language: Python
license: MIT
maturity: "newspaper3k 0.2.8 (last PyPI 2018-09), codebase stale since ~2020; active fork newspaper4k — ~15.1k stars (as of 2026-06)"
last_verified: 2026-06-28
type: library
---

# newspaper

A Python library that takes a news/article URL, downloads it, and pulls out the clean article text, title, authors, publish date, top image, and (optionally) NLP keywords/summary — boilerplate stripped, no per-site scraping rules to write.

## When to use

You're a data engineer building a media-monitoring pipeline, and you have a list of thousands of news article URLs — press releases, newspaper stories, blog posts. You don't care about the nav bars, ad rails, comment widgets, or cookie banners; you want the *body text*, the headline, who wrote it, when, and the lead image, in a clean dict per URL. Writing a bespoke CSS/XPath extractor per outlet would be hundreds of brittle rules, so instead you point `newspaper` at each URL: `Article(url).download()`, `.parse()`, and read `.text`, `.title`, `.authors`, `.publish_date`, `.top_image`. Call `.nlp()` and you also get `.keywords` and a naive `.summary`. For one outlet you can build a `Source` to discover and batch its article URLs.

It shines when the input is *article-shaped* and you want one general extractor instead of N site-specific ones — the classic "give me the readable text behind this news link, at scale" job, where a roughly-right heuristic across many domains beats hand-tuning each.

## When NOT to use

- **The page isn't article-shaped.** It targets news/article layouts. On SPAs that render via JS, paywalled or login-walled pages, listing/search/home pages, product pages, or forums, it returns empty or garbage `.text` — it parses static HTML, it is not a headless browser.
- **You need high or guaranteed extraction accuracy.** Heuristic boilerplate removal varies a lot by site; expect missed paragraphs, wrong authors, or null dates on a meaningful fraction. Benchmark on *your* sources before trusting it. [未验证]
- **You're installing the original `newspaper3k`.** The upstream `codelucas/newspaper` is effectively stale (last PyPI release 2018, codebase quiet since ~2020). The maintained path is the community fork **newspaper4k** (`AndyTheFactory/newspaper4k`) — prefer it for new work. [未验证]
- **You need a crawler/scheduler.** It downloads and parses URLs you hand it; it is not a distributed crawler, queue, or scheduler. For large-scale crawling with retries/politeness/pipelines, use Scrapy.
- **You need arbitrary structured scraping.** For extracting tables, prices, or fields from non-article pages, a selector/extraction framework (Scrapy + parsel) or a generic readability extractor fits better than an article-text heuristic.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| trafilatura | 未收录 | Focused main-text + metadata extractor; generally stronger/cleaner extraction and active maintenance — often the better default today for "just the text". |
| readability-lxml | 未收录 | Port of Arc90 Readability; main-content extraction only (no authors/date/image/NLP), smaller surface, simpler. |
| boilerpipe | 未收录 | Older Java boilerplate-removal algorithm (with Python wrappers); historically influential, but JVM dependency and aging. |
| Scrapy + custom | 未收录 | Full crawling framework — you write extraction rules but get queuing, concurrency, retries, pipelines; the right tool when you need a *crawler*, not a one-URL extractor. |
| Goose3 | 未收录 | Python port of Goose article extractor; same niche as newspaper (text/metadata/top-image), different heuristics — a direct peer to benchmark against. |
| newspaper4k | 未收录 | The actively-maintained fork of this very project; same API lineage, bug fixes and Python-version updates — the recommended successor. |

## Tech stack

- **Language:** Python 3.
- **Parsing:** `lxml` for HTML parsing and the XPath/heuristic extraction of title/body/authors/date.
- **Fetching:** `requests` for HTTP downloads (static HTML only — no JS execution).
- **Imaging/NLP:** image handling for top-image detection; an optional NLP step (keywords + extractive summary) backed by NLTK corpora and a stopwords/POS approach.

## Dependencies

- **Runtime:** Python 3 plus `lxml` and `requests` (and their transitive C/HTTP deps).
- **NLP data:** the `.nlp()` path needs NLTK data (e.g. `punkt`) downloaded once; without it, `.text`/metadata still work but keyword/summary fails.
- **No services:** no database, server, or browser required — it's an in-process library you call per URL.

## Ops difficulty

**Low.** It's a `pip install` library with no infrastructure — no server, datastore, or browser to run. The real operational cost is *quality and robustness at scale*: pages that error or time out, sites that block scrapers, empty extractions you must detect and skip, and the one-time NLTK corpus download for the NLP features. You own concurrency, rate-limiting, and retry logic (the library does one URL at a time). Pin to the maintained fork (newspaper4k) to avoid running on a stale dependency. [未验证]

## Health & viability

- **Maintenance (dated 2026-06).** The upstream `codelucas/newspaper` (newspaper3k) is effectively stale: last PyPI release 0.2.8 was 2018-09 and the codebase has been quiet since ~2020. A "pushed 2026-05" repo timestamp, if present, looks like a trivial touch rather than revived development — treat the original as in maintenance-mode/abandoned, not actively evolving. [未验证]
- **Governance / bus factor.** A single-maintainer, `User`-owned repo (Lucas Ou-Yang) — classic bus-factor risk, and here the maintainer has largely moved on. The healthier path is the **community fork newspaper4k** by Andrei Paraschiv (`AndyTheFactory/newspaper4k`), which reports healthy maintenance and a regular release cadence. [未验证]
- **Age & Lindy verdict.** Created 2013-11 (~13 years) — the *concept* is durable and battle-tested, so Lindy on the idea is strong; but Lindy needs **age × still-active**, and the original is no longer active. The age signal transfers to newspaper4k, which keeps the lineage alive. [推断]
- **Adoption.** ~15.1k stars and very wide historical use in tutorials and pipelines indicate strong adoption and a large install base; much of that mindshare is now migrating toward newspaper4k and trafilatura. [未验证]
- **Risk flags.** Maintenance/currency is *the* flag — running the original on modern Python and modern sites risks unpatched bugs. License is permissive (MIT); no relicense or open-core concerns found. [推断]

## Caveats (unverified)

- [未验证] ~15.1k GitHub stars as of 2026-06 — star counts are unreliable and date-sensitive, treat as indicative only.
- [未验证] newspaper3k last PyPI release is 0.2.8 (2018-09) and the codebase is reported quiet since ~September 2020; any 2026 repo "pushed" timestamp was not confirmed to reflect substantive development.
- [未验证] newspaper4k (`AndyTheFactory/newspaper4k`) is reported as the actively-maintained community fork with healthy cadence; verify its current release/activity before depending on it.
- [未验证] Extraction-accuracy claims are inherently site-dependent; "accuracy varies" is a general property of heuristic extractors, not a measured number for any specific source.
- [未验证] The exact dependency set (lxml/requests/Pillow/NLTK and versions) and the NLP corpora required differ between newspaper3k and newspaper4k and across versions — confirm against the version you install.
- [推断] Created 2013-11 (~13 years) is stated as a Lindy/age signal for the concept; the durability inference applies to the article-extraction idea and the live fork, not to the stale original.
