---
name: marked
slug: marked
repo: https://github.com/markedjs/marked
category: markdown-tools
tags: [markdown, parser, compiler, html, javascript, gfm, commonmark]
language: JavaScript
license: MIT
maturity: v18.x, active (2026-06)
last_verified: 2026-06-28
type: library
---

# marked

A fast, low-level Markdown parser and compiler for JavaScript — turns Markdown into HTML in a single function call, with no required dependencies and a small API surface ("Built for speed").

## When to use

You're building a web app — a comment box, a docs viewer, a chat client, a README renderer — and you need to turn user- or author-written Markdown into HTML, in the browser or in Node, without pulling in a heavy toolchain. You want `import { marked } from 'marked'` and then `marked.parse(src)` to just give you an HTML string, fast, with sane GFM-leaning defaults (tables, fenced code, autolinks). You drop it in, wire the output into your DOM (after sanitizing — see below), and you're done; there's no AST to learn, no plugin manifest to assemble, no build step beyond your normal bundler.

It's the right reach when *throughput and simplicity* matter more than strict spec conformance: rendering many small Markdown snippets per page, server-side rendering a docs site, or any place where you'd otherwise hand-roll a regex and regret it. marked compiles to a compact bundle, runs the same in Node and the browser, and exposes just enough hooks (a `renderer`, a `walkTokens` pass, a lexer you can call directly) to customize output without adopting a whole pipeline.

## When NOT to use

- **You need 100% CommonMark conformance.** marked is fast and CommonMark/GFM-*leaning* but is **not** fully spec-compliant by default — edge cases diverge from the reference. If exact spec behavior is a hard requirement, use markdown-it (CommonMark-strict) or remark. [推断]
- **You're rendering untrusted Markdown without sanitizing.** marked does **not** sanitize its output HTML — raw HTML and crafted links pass straight through, so naive use is an XSS hole. You **must** run the output through DOMPurify (or equivalent) yourself; sanitization was deliberately removed from marked's own scope.
- **You want to transform Markdown as an AST / mdast pipeline.** marked's token model is for rendering, not a general document-transform toolchain. For linting, rewriting, MDX, or plugin-based AST passes, reach for remark / unified.
- **You depend on a large plugin ecosystem.** marked has extensions but nothing like markdown-it's plugin catalog. If you need footnotes, containers, KaTeX, task lists, etc. as off-the-shelf plugins, markdown-it or remark will have more ready-made parts.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| markdown-it | 未收录 | CommonMark-strict, pluggable architecture with a rich plugin ecosystem; heavier API and a touch slower than marked, but the choice when spec conformance and plugins matter. |
| remark / unified | 未收录 | Full mdast AST pipeline for parsing, transforming, linting, and serializing (Markdown, MDX); far more powerful and far heavier — a toolchain, not a one-call renderer. |
| micromark | 未收录 | The low-level CommonMark/GFM tokenizer underneath remark; correct and streaming-oriented, but you build the rendering layer yourself. |
| CommonMark reference (commonmark.js) | 未收录 | The spec's own reference implementation; the conformance yardstick, but fewer GFM niceties and not optimized as a production renderer. |

## Tech stack

- **Language:** JavaScript (the published source ships JS plus TypeScript type definitions; the repo also contains TS and HTML for tooling/docs). [推断]
- **Runtime targets:** runs in Node and in the browser; distributed as ESM and UMD/CJS builds and via CDN.
- **Architecture:** a lexer/tokenizer that turns Markdown into tokens, then a parser/renderer that emits HTML; customization via a `Renderer`, `Tokenizer`, `walkTokens` hook, and an extension API.
- **Flavors:** GFM-leaning defaults (tables, strikethrough, autolinks, fenced code) on top of a CommonMark-ish core.

## Dependencies

- **Runtime:** none required — marked is dependency-light by design and works standalone. [未验证]
- **Sanitizer (yours to add):** for any untrusted input you must pair it with DOMPurify or another HTML sanitizer — not bundled, deliberately your responsibility.
- **Install:** `npm install marked`, or load the prebuilt bundle from a CDN; also exposes a CLI (`marked`) for command-line conversion.

## Ops difficulty

**Low.** It's a library, not a service — there is nothing to deploy or operate beyond adding a dependency to your app. The only real operational concern is the security one: remember to sanitize output before injecting it into the DOM, and pin/track the major version since the API has changed across majors. No datastore, no runtime, no infra.

## Caveats (unverified)

- [未验证] ~36.9k GitHub stars and latest release in the v18.x line (v18.0.5, dated 2026-06-04) as of 2026-06; star counts and versions drift release-to-release — treat as indicative.
- [推断] "Not fully CommonMark-compliant by default" reflects marked's long-standing positioning as a speed-first, spec-leaning parser; exact divergences depend on the version and your config — verify against the current spec test suite if conformance is critical.
- [未验证] "No required runtime dependencies" is marked's own framing; confirm against the current `package.json` for your version, especially if you enable optional features.
- [推断] License is MIT (GitHub's auto-detection may show NOASSERTION for the repo); confirm via the repo's LICENSE file for your pinned version.
