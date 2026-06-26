---
name: Guizang PPT Skill
slug: guizang-ppt
repo: https://github.com/op7418/guizang-ppt-skill
category: ai-design-generation
tags: [skill, html-deck, presentation, slides, swiss-design, claude-code, codex]
language: HTML
license: AGPL-3.0-only
maturity: v1.1.0, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# Guizang PPT Skill

An agent skill that turns an article or outline into a single-file HTML horizontal-swipe slide deck — plus matching deck images and multi-platform covers — using two locked visual systems (editorial-magazine and Swiss international).

## When to use

You're a founder, indie maker, or domain expert prepping a talk for an offline meetup, a private salon, or a product demo day, and you want a deck that looks designed rather than templated. You have an article or a pile of Markdown notes, you live in Claude Code or Codex, and you don't want to fight slide software or hand-place every box. You drop the skill in, say "make me a 7-page Swiss-style deck with 2–3 images," and the agent walks a fixed workflow — pick a style, answer a 7-question brief, copy the template, fill named layouts, optionally generate images, self-check against a checklist, open the result in a browser. Because the output is one self-contained `.html` file, you can present it, send it, or screenshot it with no build step and no server.

It fits best when you want a strong personal aesthetic baked in: Style A (electronic-magazine × e-ink) leans narrative and opinionated; Style B (Swiss international) enforces a 16-column grid, a single high-saturation anchor color, hairline rules, and 22 named layouts (`S01`–`S22`) with a validator script that rejects centered titles, improvised page structures, and text baked into SVG. You get a constrained, agent-legible design system instead of a blank canvas.

## When NOT to use

- **You need editable, collaborative slides.** Output is static single-file HTML; there's no PowerPoint/Google Slides export and no multi-author co-editing. If colleagues must edit in a familiar tool, this is the wrong artifact.
- **Dense data, tables, or training material.** The README explicitly calls out big tables and high-density courseware as a poor fit — the layouts optimize for sparse, statement-driven slides, not spreadsheets.
- **You're not in a file-system + browser agent.** It assumes an agent that can read/write files and run shell (Claude Code, Codex, Cursor). A plain chatbot with no filesystem or preview can't reliably produce a full deck.
- **You want provider-neutral image generation.** The optional image pipeline is described around Codex + GPT-Image / GPT-M models; if you can't use those, you lose the integrated image step and must source visuals yourself. [推断]
- **AGPL-3.0 matters to you.** The skill (and its templates/scripts) is AGPL-3.0-licensed; if you embed parts into a service or product you ship, the copyleft terms apply — read them before vendoring.
- **You need a stable, long-stable contract.** It's a young, fast-moving single-maintainer skill (latest release 2026-05); layout names, theme presets, and the brief flow can shift between versions.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [guizang-social-card](guizang-social-card.md) | ✅ | Same author's sibling skill, but scoped to single social cards / covers rather than full multi-page decks; overlapping visual rules, narrower output. |
| [html-anything](html-anything.md) | ✅ | General agent-driven HTML artifact generation; broader and unopinionated, so it lacks the locked deck layouts, Swiss validator, and cover/image workflow this skill ships. |
| [open-design](open-design.md) | ✅ | Aimed at broader UI/design generation; not a presentation-deck specialist with horizontal-swipe runtime and named slide layouts. |
| [Impeccable](impeccable.md) | ✅ | Design-quality oriented generation; different surface — not a single-file HTML deck workflow. |
| Slidev | 未收录 | Developer-grade Markdown→HTML deck framework with build tooling, themes, and a dev server; more powerful/long-stable but not agent-driven and not opinionated about Swiss/editorial aesthetics. |
| Marp | 未收录 | Markdown→slides (HTML/PDF/PPTX) with a clean ecosystem and exports this skill lacks; far less visual flexibility per slide. |
| Gamma / Tome | 未收录 | Hosted AI deck SaaS, not a repo — easier for non-agents, but closed, no single-file HTML artifact, no local agent control. |

## Caveats (unverified)

- [未验证] License read as AGPL-3.0-only from the GitHub `licenseInfo` API and the `LICENSE` file (2026-06-26); confirm the exact SPDX/edition against the repo before relying on copyleft scope.
- [未验证] Latest release v1.1.0 (published 2026-05-15) and last push 2026-06-02 per the GitHub API on 2026-06-26; star count ~19k — GitHub stars are unreliable and date-sensitive, treat as indicative only.
- [推断] The optional image-generation step is tied to Codex + GPT-Image 2.0 / GPT-M 2.0 in the README; whether equivalent generation works on other agents/providers is not stated — verify before relying on it.
- [推断] "22 named Swiss layouts (S01–S22)" and "Style A 10 layouts" are the project's own framing from the README; the precise counts and names may shift release-to-release.
- [未验证] The Swiss validator (`scripts/validate-swiss-deck.mjs`) is a Node script; its exact rule coverage was read from the README description, not by running it.
