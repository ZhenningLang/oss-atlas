# web-automation

> Level 2 of 3. Drive or automate web UIs — programmatically or via natural language
> (browser automation, in-page GUI agents).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | License | Page |
|---|---|---|---|
| **page-agent** | Add an AI copilot that operates an existing web UI (ERP/CRM/admin) via natural language, in-page, with no backend rewrite. | MIT | [→](page-agent.md) |

## Comparison matrix

Substitutes named in the project page but **not yet indexed**.

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [page-agent](page-agent.md) | ✅ | In-page, DOM-as-text, reuses login session, no backend/headless, LLM-agnostic — but text-only (no vision), client-side only, sends DOM to an external LLM. |
| browser-use | not indexed | Server-side, vision-capable Python browser agent — works beyond DOM text and off the client, but heavier infra (real/headless browser). |
| Playwright / Puppeteer | not indexed | Lower-level, code-driven, headless-capable — deterministic and powerful, but selector/script-based (not NL) and brittle to DOM changes. |
| Selenium | not indexed | Mature, ubiquitous cross-browser automation — but DIY, verbose, no NL layer. |
| Computer-use agents (Anthropic / OpenAI Operator) | not indexed | Vision-based, drive any pixel UI — but slower, costlier, need a controlled browser/VM. |

## What belongs here

Tools whose primary job is to **drive a web UI** — browser automation frameworks and in-page/GUI
agents. Not HTTP/API clients, not scrapers-without-interaction, not headless-render services.
