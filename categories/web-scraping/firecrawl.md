---
name: Firecrawl
slug: firecrawl
repo: https://github.com/firecrawl/firecrawl
category: web-scraping
tags: [web-scraping, ai-crawler, markdown, data-extraction, api]
language: TypeScript
license: AGPL-3.0
maturity: v1.x, active, 142k stars (as of 2026-07)
last_verified: 2026-07-01
type: service
upstream:
  pushed_at: 2026-07-01T07:40:07Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T12:44:29Z
  overall: "?"
  overall_score: null
  scored_axes: 1
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: firecrawl-py
        dependent_repos_count: 0
        downloads_last_month: 5804535
        graph_tier: E
        volume_tier: A
        cross_check_divergence: null
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    maintenance: { reason: recency_unreadable }
    responsiveness: { reason: no_traffic }
    longevity: { reason: not_found }
    governance: { reason: empty_or_gated }
    risk_license: { reason: repo_unreachable }
---

# Firecrawl

The API to search, scrape, and interact with the web at scale — turning raw web pages into clean Markdown or structured data your agents can ship with.

![Firecrawl — health radar](../../assets/health/firecrawl.svg)

## When to use

You're building an AI agent or data pipeline that needs to ingest web content at scale, and you want clean, structured output rather than raw HTML. You've looked at writing Scrapy spiders or Playwright scripts, but maintaining browser automation, handling anti-bot, and converting messy HTML into Markdown is not your core job. You reach for Firecrawl because it is an API-first service that handles search, scraping, and even browser interaction (click, navigate) for you, returning structured Markdown or JSON without you managing crawler infrastructure. Pick Firecrawl over [Scrapyd](scrapyd.md) or raw Scrapy when you want the extraction and conversion layer handled for you rather than scheduling spiders you wrote yourself; pick it over [newspaper](newspaper.md) or [Readability.js](readability-js.md) when you need general-purpose web scraping, search, and interaction at scale rather than single-page article extraction. If you need a hosted API with an AGPL-3.0 open-source self-host option, Firecrawl is the closer fit than proprietary alternatives.


## When NOT to use

- **Simple one-off scraping.** If you need a single page or occasional curl, use `curl` + `pandoc` or `trafilatura` instead of Firecrawl, because paying for or self-hosting a full crawling API is overkill for sporadic tasks.
- **Strict closed-source compliance.** If you need a permissive-license scraper without network-copyleft obligations, use [newspaper](newspaper.md) (MIT) or `trafilatura` (Apache-2.0) instead of Firecrawl, because AGPL-3.0 requires sharing source if you modify and distribute the service. [未验证]
- **Budget-constrained at scale.** If you need high-volume scraping without per-request pricing, use Scrapy or Playwright on your own infrastructure instead of Firecrawl's hosted service, because the API pricing becomes significant at scale and self-hosting Firecrawl still requires managing Node.js and browser automation.
- **Deep web / authenticated sites.** If you need complex login flows and session management across many sites, use custom Playwright scripts instead of Firecrawl, because while it supports interaction, complex multi-step authentication and stateful crawling are better handled by direct browser automation you control.


## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Scrapyd](scrapyd.md) | ✅ | Self-hosted Scrapy spider scheduler. | Scrapyd is for running Scrapy spiders you write; Firecrawl is an API that handles crawling and extraction for you. |
| [newspaper](newspaper.md) | ✅ | Article text extraction from news URLs. | newspaper is Python-only and article-focused; Firecrawl is a full-service API with search, scrape, and interaction. |
| [Readability.js](readability-js.md) | ✅ | Firefox Reader View article extraction. | Readability.js is a browser library for article extraction; Firecrawl is a scalable API with search and interaction. |
| [PRAW](praw.md) | ✅ | Reddit-specific API wrapper. | PRAW is Reddit-only; Firecrawl is general-purpose web scraping. |
| Scrapy / Playwright | 未收录 | Lower-level scraping frameworks. | Scrapy and Playwright give full control but require building and maintaining crawler infrastructure. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — API server runtime
- **Docker** — containerized deployment option
- **Playwright** — underlying browser automation for JS-rendered pages

## Dependencies

- For hosted API: API key and internet connectivity
- For self-hosted: Docker, Node.js runtime, and a server with sufficient bandwidth
- Optional: Redis for caching and queue management
- Browser dependencies (Chromium via Playwright) for dynamic content

## Ops difficulty

**Low (hosted) / Medium (self-hosted)**. The hosted API is a simple HTTP integration. Self-hosting requires managing a Node.js service, Playwright browser instances, and queue/caching infrastructure. Browser automation is resource-intensive and can consume significant memory.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance**: Very active — daily pushes as of 2026-07, with a responsive team (376 open issues). [推断]
- **Governance**: Owned by the Firecrawl organization; appears to be a dedicated company/org behind the project with reasonable bus factor.
- **Backing**: Firecrawl appears to be a venture-backed company offering both open-source and hosted services; the dual model provides sustainability but may shift roadmap toward paid features. [未验证]
- **Adoption**: High star count (142k) for a project created in 2024; the ~2-year track record is short but the active development cadence is positive. [推断]
- **Risk flags**: AGPL-3.0 copyleft license may limit commercial use without open-sourcing derivatives. The hosted service pricing and open-source feature parity are important to monitor. The project is young (created 2024-04) with no long-term Lindy track record. [未验证]

## Caveats (unverified)

- [未验证] The AGPL-3.0 license may require source disclosure for derivative works in a SaaS context; verify with legal counsel for your specific use case.
- [未验证] The exact feature parity between the open-source self-hosted version and the paid hosted API is not confirmed.
- [推断] The 142k star count on a ~2-year-old repo suggests significant hype; verify organic production adoption beyond the GitHub star metric.
