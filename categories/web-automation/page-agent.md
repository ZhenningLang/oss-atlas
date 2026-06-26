---
name: page-agent
slug: page-agent
repo: https://github.com/alibaba/page-agent
category: web-automation
tags: [browser-automation, gui-agent, in-page, natural-language, dom, llm-agnostic, typescript, no-backend, web-copilot, byo-llm]
language: TypeScript (runs as browser JS; npm + CDN)
license: MIT
maturity: v1.10.0 (2026-06-15); ~33 releases, ~1061 commits, active; Alibaba-maintained
last_verified: 2026-06-26
---

# page-agent

A JavaScript **in-page GUI agent** from Alibaba: control a web interface with natural-language commands by reading and manipulating the DOM directly inside the user's existing browser session — no screenshots, no headless browser, no backend rewrite.

## 中文摘要

page-agent(PageAgent)是阿里开源的「页内 GUI agent」JS 库:把 AI agent 直接塞进网页,用自然语言命令读取并操作 DOM(读**可见页面**而非 CSS/XPath 选择器),复用浏览器**已有登录态**,无需后端改造、无需 headless/截图。BYO LLM(任意 OpenAI 兼容模型,示例用 Qwen/Dashscope)。**最适合**:给已有复杂 Web 应用(ERP/CRM/后台)几行代码加一个能真正操作 UI 的 AI copilot。**何时别用**:需要视觉/多模态推理(只读 DOM 文本,canvas/图像类页面不行)、服务端批量自动化(它活在浏览器里,服务端该用 Playwright/browser-use)、高并发 agent(客户端受浏览器限制)、或对把页面 DOM 文本发给外部 LLM 有数据合规顾虑时。`[未验证]` 星数等单源数据见 Caveats。

## When to use

You have an existing complex web app — ERP, CRM, admin dashboard — and want to add an **AI copilot that actually operates the UI** (fills forms, clicks through multi-step flows) with a few lines of JavaScript and no backend rewrite. It reuses the user's existing login/session, and because it reads the visible page as text, instructions like "click the submit-order button" are meant to survive HTML refactors (no brittle selectors). LLM-agnostic (bring your own OpenAI-compatible model). Good for in-product copilots, complex form/workflow automation, and natural-language / voice accessibility layers over web UIs.

## When NOT to use

- **No vision / multimodal** — it reads the DOM as text only. Canvas/WebGL/image-heavy UIs, pixel-precise interactions, or anything not expressed in the DOM won't work. `[推断]` shadow DOM and cross-origin iframes are likely weak spots.
- **Not server-side automation** — it lives in the browser. For headless/batch crawling, scraping, or CI automation use Playwright or browser-use instead.
- **Not for high concurrency** — client-side and bound by browser limits; it is not a fleet-of-agents backend.
- **No closed-loop visual verification** — it cannot "see" whether an action visually succeeded; verification must come from the DOM.
- **External-LLM dependency & data egress** — `[未验证]` you bring your own LLM, so quality/cost/latency are inherited, and page DOM text is sent to that model — a privacy/compliance review is warranted for sensitive apps.
- **Maturity** — active and at v1.x, but `[未验证]` long-term API stability and real-world coverage across arbitrary sites; the "survives HTML changes" robustness is the project's own claim, not independently benchmarked.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| browser-use | 未收录 | Python, server-side, vision-capable (screenshots) browser agent — heavier infra (a real/headless browser), but works beyond DOM text and off the client; page-agent cites it as inspiration. |
| Playwright / Puppeteer | 未收录 | Lower-level, code-driven, headless-capable automation — deterministic and powerful, but you write selectors/scripts (not natural language), and it breaks when the DOM changes. |
| Selenium | 未收录 | Mature, ubiquitous cross-browser automation — but DIY, verbose, selector-based, no NL layer. |
| UiPath / Automation Anywhere (RPA) | 未收录 | Enterprise desktop+web RPA with governance — but proprietary, costly, vendor lock-in, heavyweight vs a JS snippet. |
| Computer-use agents (Anthropic computer use / OpenAI Operator) | 未收录 | Vision-based agents that drive a real screen/browser — handle any pixel UI, but slower, costlier, and need a controlled browser/VM, not an in-page snippet. |

## Tech stack

- TypeScript / browser JavaScript — runs in-page; no Node.js / Python / headless browser required
- LLM-agnostic — bring your own model via an OpenAI-compatible API (examples: Qwen / Dashscope)
- Optional Chrome extension — multi-tab / cross-page tasks
- Optional MCP server — external control / orchestration
- Distribution — npm package + CDN (jsDelivr, npmmirror)

## Dependencies

- A modern **browser** (it runs client-side, inside the page)
- An **LLM endpoint you provide** (OpenAI-compatible API + key)
- **Optional** — the Chrome extension (multi-tab); an MCP server (external orchestration)

## Ops difficulty

**Low.** Drop-in browser library (npm/CDN, a few lines), no backend, no headless browser, no separate infra to operate. The real operational cost is the **BYO LLM endpoint** — API-key management, per-call cost and latency — plus the **data-governance** question of sending page DOM text to that model. `[推断]` token cost scales with DOM size, so large/complex pages can get expensive per action.

## Caveats (unverified)

- **Stars** — ~19.9k from a single snapshot (~2026-06-15), not cross-checked against the API. `[未验证]`
- **Substitute list** — browser-use as the cited "foundation", plus RPA and computer-use agents, is partly inferred from the repo page + secondary articles, not all confirmed. `[未验证]`
- **Positioning claims** — "survives HTML structure changes" and "no backend needed" are the project's own framing; real-world robustness across arbitrary sites is not independently verified. `[未验证]`
- **Qwen/Dashscope** — whether these are merely examples vs recommended defaults is inferred. `[推断]`
