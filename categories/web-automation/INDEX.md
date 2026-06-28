# web-automation

> Category node. Drive or automate a web UI — browser automation, or an in-page natural-language GUI agent.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | [→](page-agent.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | [→](chrome-devtools-mcp.md) |
| **Cua** | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. | [→](cua.md) |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | [→](agent-browser.md) |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | [→](selenium.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | [→](phantomjs.md) |
| **Selenium Wire** | Extends Selenium's Python bindings so you can inspect and modify the browser's underlying HTTP/HTTPS traffic — by routing the browser through an internal MITM proxy. **The project is archived and explicitly no longer maintained.** | [→](selenium-wire.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [page-agent](page-agent.md) | ✅ | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. |
| [Cua](cua.md) | ✅ | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. |
| [Agent Browser](agent-browser.md) | ✅ | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. |
| [Selenium](selenium.md) | ✅ | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. |
| [PhantomJS](phantomjs.md) | ✅ | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. |
| [Selenium Wire](selenium-wire.md) | ✅ | Extends Selenium's Python bindings so you can inspect and modify the browser's underlying HTTP/HTTPS traffic — by routing the browser through an internal MITM proxy. **The project is archived and explicitly no longer maintained.** |
| Playwright / Puppeteer | 未收录 | Lower-level browser automation libraries named across the pages. |

## What belongs here

Tools that **drive or automate a web/browser (or computer) GUI** — headless browser automation, computer-use, or in-page GUI agents. Not server-side scraping frameworks; not enterprise desktop-only RPA.
