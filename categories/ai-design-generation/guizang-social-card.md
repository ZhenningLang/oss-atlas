---
name: Guizang Social Card Skill
slug: guizang-social-card
repo: https://github.com/op7418/guizang-social-card-skill
category: ai-design-generation
tags: [skill, social-cards, xiaohongshu, wechat, editorial-design, swiss-design, claude-code, codex]
language: HTML
license: AGPL-3.0-only
maturity: no tagged release, active (last push 2026-05)
last_verified: 2026-06-26
type: skill-pack
---

# Guizang Social Card Skill

An agent skill that turns a topic and a few images into Xiaohongshu carousels (1080×1440) and WeChat 21:9 + 1:1 cover pairs — single-file HTML rendered to PNG via Playwright, driven by two locked visual systems (editorial-magazine and Swiss international).

## When to use

You're an indie maker, content creator, or domain expert who lives in Claude Code or Codex and needs a batch of social images that look art-directed rather than canva-templated. You've got a half-written Xiaohongshu post about a trip, a product teardown, or a reading list, plus a folder of phone photos, and you do not want to hand-place text boxes or fight a design tool. You drop this skill in, say "做一套小红书图文" or "公众号 21:9 + 1:1 封面对," and the agent runs a fixed 7-step flow: it collects platform/style/content, picks Editorial (Monocle/Kinfolk-style, for narrative/lifestyle/travel) or Swiss (grid + single anchor color, for product reviews/data/tutorials), chooses from 28 named layouts and 10 theme presets, sources and locally caches your images (writing a `SOURCES.md` attribution file), clones a seed `.html`, and renders to PNG with `node render.mjs`.

It fits best when you want a strong, opinionated aesthetic baked in and an artifact you fully control. Because each deck is one self-contained `.html` file, the agent can edit it as text, diff it, and re-render without a build chain — and an optional Playwright validator (`validate-social-deck.mjs`) measures the real DOM for overflow, type-cap violations, footer collisions, and Swiss font-weight breaches before you ship. You get a constrained, agent-legible design system with the exact canvas sizes the platforms expect (`.poster.xhs` 1080×1440, `.poster.wide` 2100×900, `.poster.square` 1080×1080) instead of a blank canvas.

## When NOT to use

- **You need horizontal-swipe slide decks, not cards.** This skill is scoped to single social cards and covers; the README routes deck work to its sibling [guizang-ppt](guizang-ppt.md) instead.
- **You're not in a file-system + browser agent.** It assumes an agent that reads/writes files and runs shell with Node + Playwright/Chromium installed (Claude Code, Codex, Cursor). A plain chatbot with no filesystem, no Node, or no headless browser cannot render the PNGs.
- **You want full color/brand control.** Themes are preset-only — no custom hex is allowed (a deliberate constraint to protect aesthetic consistency). If you must hit exact brand colors, you'll be fighting the system.
- **Photo-retouching, OOTD photosets, film-grain or "real skin test" content.** The README explicitly puts these outside scope; it composes layouts and type, it does not edit or retouch your photos.
- **AGPL-3.0 matters to you.** The skill, templates, and scripts are AGPL-3.0-licensed; vendoring parts into a service or product you ship triggers copyleft (including network-served derivatives) — read the terms first.
- **You need a stable, long-stable contract.** It's a young, fast-moving single-maintainer skill with no tagged release yet (last push 2026-05); layout names, theme presets, and the brief flow can shift without versioned notice. [推断]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [guizang-ppt](guizang-ppt.md) | ✅ | Same author's sibling skill, scoped to full multi-page horizontal-swipe decks rather than single cards/covers; overlapping visual rules, different output artifact. |
| [html-anything](html-anything.md) | ✅ | General agent-driven HTML artifact generation; broader and unopinionated, so it lacks the locked card layouts, Swiss validator, platform canvas sizes, and image-sourcing workflow this skill ships. |
| [open-design](open-design.md) | ✅ | Aimed at broader UI/design generation; not a social-card specialist with platform-exact poster sizes and a render-to-PNG pipeline. |
| [Impeccable](impeccable.md) | ✅ | Design-quality oriented generation; different surface — not a single-file-HTML card workflow with a Playwright validator. |
| Canva / 稿定设计 | 未收录 | Hosted template SaaS, not a repo — easier for non-agents and richer asset libraries, but closed, no local agent control, no single-file HTML artifact, and far less opinionated visual rigor. |
| Figma + plugins | 未收录 | Full design control and collaboration, but manual; no agent-driven 7-step flow, no auto image sourcing, and not a repo you can vendor. |

## Health & viability

- **Maintenance (2026-06):** [推断] active but thin — last push 2026-05-27, **no tagged release at all** (pins to a moving `main`), open-issue count ~5. For a one-person skill pack that means layout names, presets, and the brief flow can shift without any versioned notice.
- **Governance & bus factor:** [推断] **single-maintainer, `User`-owned (`op7418`), ~4k stars** — a bus-factor flag, though milder than its sibling `guizang-ppt` (~19k) since the audience is smaller. No org or co-maintainer backstop; this is the same author's sibling to `guizang-ppt` and shares its sustainability profile. Mitigant: each card is a self-contained `.html` you own outright, so abandonment only stops future updates.
- **Age & Lindy:** [未验证] repo created ~2026-05, ~1 month old as of 2026-06 — **brand-new; zero Lindy prior.** No release line, fast-moving — treat the contract (28 layouts, 10 presets, canvas sizes) as unstable and verify against the current repo.
- **Risk flags:** [未验证] **AGPL-3.0-only** copyleft (including network-served derivatives) if you vendor it; render/validator scripts need Node + Playwright/Chromium; the image-sourcing fallback chain depends on third-party providers (Unsplash/Pexels/Flickr/Wallhaven) that may need keys/network. No CVEs relevant to a static-HTML generator.

## Caveats (unverified)

- [未验证] License read as AGPL-3.0-only from the GitHub `licenseInfo` API and the `LICENSE` file (2026-06-26); confirm the exact SPDX/edition against the repo before relying on copyleft scope.
- [未验证] No tagged GitHub release exists (`latestRelease` is null per the API on 2026-06-26); last push 2026-05-27; star count ~4.0k — GitHub stars are unreliable and date-sensitive, treat as indicative only.
- [未验证] The render (`render.mjs`) and validator (`validate-social-deck.mjs`) are Node + Playwright scripts; their exact dependency versions and rule coverage were read from the README description, not by running them. Playwright pulls a Chromium download on install.
- [推断] "28 layouts" (Editorial M01–M16, Swiss S01–S12), "10 theme presets," and the 11 Xiaohongshu category routings are the project's own framing from the README; precise counts/names may shift release-to-release.
- [推断] The image-sourcing fallback chain (user → AI generation → Unsplash → Pexels → Flickr CC → Wallhaven) and MapLibre/OSM travel maps are described in the README; whether each provider/API works in a given environment is not verified and may need keys or network access.
- [推断] Specific fonts cited (Editorial: Playfair Display + Noto Serif; Swiss: Inter + Helvetica) and canvas sizes are from the README; verify against the current templates before relying on exact rendering.
