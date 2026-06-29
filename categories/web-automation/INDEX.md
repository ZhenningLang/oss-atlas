# web-automation

> Category node. Drive or automate a web UI — browser automation, or an in-page natural-language GUI agent.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | B (6/6) | [→](page-agent.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | A (6/6) | [→](chrome-devtools-mcp.md) |
| **Cua** | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. | B (6/6) | [→](cua.md) |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | B (6/6) | [→](agent-browser.md) |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | B (6/6) | [→](selenium.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | D (5/6) | [→](phantomjs.md) |
| **Selenium Wire** | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. | D (5/6) | [→](selenium-wire.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [page-agent](page-agent.md) | ✅ | B (6/6) | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | A (6/6) | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. |
| [Cua](cua.md) | ✅ | B (6/6) | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. |
| [Agent Browser](agent-browser.md) | ✅ | B (6/6) | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. |
| [Selenium](selenium.md) | ✅ | B (6/6) | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. |
| [PhantomJS](phantomjs.md) | ✅ | D (5/6) | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. |
| [Selenium Wire](selenium-wire.md) | ✅ | D (5/6) | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. |
| Playwright / Puppeteer | 未收录 | — | Lower-level browser automation libraries named across the pages. |

## What belongs here

Tools that **drive or automate a web/browser (or computer) GUI** — headless browser automation, computer-use, or in-page GUI agents. Not server-side scraping frameworks; not enterprise desktop-only RPA.
