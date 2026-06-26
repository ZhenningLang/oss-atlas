---
name: Open Design
slug: open-design
repo: https://github.com/nexu-io/open-design
category: ai-design-generation
tags: [ai-design, local-first, desktop-app, electron, byok, design-systems, prototyping, slides, mcp]
language: TypeScript
license: Apache-2.0
maturity: v0.11.0 "The Bazaar", active (2026-06)
last_verified: 2026-06-26
type: app
---

# Open Design

A local-first, BYOK Electron desktop app that turns a coding agent into a design studio — generating sandboxed HTML prototypes, magazine-style decks, brand-grade images and HTML→MP4 motion graphics, all driven by reusable Skills and `DESIGN.md` design systems.

## When to use

You're a product engineer or designer who already lives inside a coding agent (Claude Code, Codex, Cursor, Copilot, etc.) and you want it to *produce design artifacts*, not just code — a clickable mobile prototype, a pitch deck, a brand social card — without piping your prompts and assets through someone else's cloud. You care that everything runs on your own machine, that you bring your own model key, and that the output is plain HTML/PDF/PPTX/MP4 you can keep. Open Design gives you a desktop "Studio" where the agent reads a `DESIGN.md` design system, renders prototypes in a sandboxed iframe, and exports decks, images, dashboards and HyperFrames (HTML→MP4) — with a library of 100+ Skills and ~150 brand design systems (Linear, Stripe, Apple, Notion, etc.) as starting points.

It also fits when you want one design surface that plugs into *whatever* agent you already use. Rather than locking you to a single assistant, it exposes itself through an MCP server and BYOK proxy (any OpenAI-compatible endpoint), so the same prototypes/decks workflow is callable from 20+ CLIs. You prototype in the browser-like renderer, tweak Live Artifact parameters, then export the file and move on — no account, no per-seat SaaS.

## When NOT to use

- **You want a hosted, zero-setup SaaS.** This is a desktop app you install and run (Electron + a local Node daemon). If you'd rather log into a website and have a vendor manage everything, the proprietary Claude Design / similar hosted tools are a closer fit — this trades that convenience for local control.
- **You need true vector design / freeform canvas editing.** It generates *code-rendered* artifacts (HTML/PPTX/MP4), not an editable vector document. It is positioned as a "Figma alternative" for generation, but it is not a collaborative vector editor — for hand-pixel-pushing, real-time multiplayer, or precise vector work, Figma/Penpot remain the tools.
- **Early-stage maturity / churn.** It's pre-1.0 (v0.11.0) with rapid releases and an expanding plugin "Bazaar"; Skills, plugin formats and the agent-adapter surface are still moving. [推断] Lock-in risk is low (open formats, Apache-2.0), but breaking changes between minor versions are plausible.
- **No GPU/heavy video budget but you need lots of MP4.** HyperFrames (HTML→MP4) and video generation lean on local rendering plus your BYOK model spend; high-volume video is not free or instant.
- **You can't or won't manage a model key.** BYOK is the model — there is no built-in free inference. If you have no OpenAI-compatible endpoint/key, you can't generate.
- **Production design-system governance at team scale.** It's a single-user local studio; it has no built-in multiplayer, review workflow, or central asset governance.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [html-anything](html-anything.md) | ✅ | Sibling focused on turning prompts into standalone HTML artifacts; Open Design is the heavier full desktop studio (decks/video/design-systems/export) around that idea. |
| [Impeccable](impeccable.md) | ✅ | Sibling aimed at high-polish UI generation; Open Design is broader (slides, images, video, MP4) and ships as a local app rather than a narrower generator. |
| [guizang-ppt-skill](guizang-ppt.md) | ✅ | A single-purpose deck-generation Skill; Open Design includes deck generation as one of several artifact types plus its own runtime/export. |
| [guizang-social-card-skill](guizang-social-card.md) | ✅ | A focused social-card Skill; Open Design covers cards/images among many artifact types inside a packaged app. |
| Claude Design (Anthropic, hosted) | not indexed | The proprietary hosted product this clones; managed cloud + polish vs Open Design's local-first, BYOK, open-format stance. |
| v0 (Vercel) | not indexed | Hosted prompt-to-UI generator; cloud SaaS, narrower to web UI, vs Open Design's local multi-artifact studio. |
| Figma / Penpot | not indexed | True vector design editors with multiplayer; Open Design generates code-rendered artifacts, not editable vector docs. |

## Tech stack

- **Language:** TypeScript (primary, per repo).
- **Frontend/Studio:** Next.js 16 App Router + React 18. [未验证] exact framework versions are from the README and may shift release-to-release.
- **Local daemon:** Node 24 · Express · SSE streaming · `better-sqlite3` for project/conversation storage.
- **Desktop shell:** Electron with a sandboxed renderer; prototypes render in a sandboxed iframe / loopback-only preview server.
- **Integration:** MCP server + BYOK proxy for any OpenAI-compatible endpoint (with SSRF protection per release notes).
- **Content:** ~150 `DESIGN.md` design systems, 100+ Skills, 261 official plugins; deck templates/themes.
- **Export:** HTML, PDF, PPTX, MP4, ZIP, Markdown.

## Dependencies

- **Runtime:** Node ~24 and pnpm (README cites pnpm 10.33.x) for run-from-source; the packaged desktop builds (macOS / Windows / Linux AppImage) bundle their runtime, so no separate install is needed for those.
- **Models:** a BYOK key for an OpenAI-compatible endpoint — required for any generation; no bundled inference.
- **Datastore:** local SQLite (`better-sqlite3`); no external database/service required for core use.
- **Optional:** Docker Desktop (web/Docker deployment) or Vercel (web). [未验证] Video/HyperFrame export may pull additional local rendering deps — verify against current docs.

## Ops difficulty

**Low for desktop use, medium from source/web.** The fastest path is the pre-packaged desktop app: download, add a BYOK key, generate — close to zero ops, everything local. Running from source or self-hosting the web build is **medium**: you manage Node 24 / pnpm versions, the local daemon, and Docker/Vercel deployment, plus the usual Electron build friction across OSes. Because it's local-first and single-user there's no server fleet to maintain, but you do own model-key management, updates across fast minor releases, and any video/export toolchain on your machine.

## Caveats (unverified)

- [未验证] v0.11.0 ("The Bazaar") published 2026-06-17; repo last pushed 2026-06-26 — versions and dates per GitHub API/README and may move quickly given the rapid release cadence.
- [未验证] Star count ~71.3k as of 2026-06 — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [未验证] Counts cited (100+ Skills, ~150 design systems, 261 plugins, 22+ agents, 56 decks) are the project's own README/release framing and shift release-to-release; verify the current numbers before relying on a specific one.
- [未验证] Framework/runtime versions (Next.js 16, React 18, Node 24, Electron, pnpm 10.33.x) are from the README and not independently confirmed against the lockfile.
- [推断] HyperFrames are described as HTML→MP4 motion graphics built on an external framework; exact rendering pipeline and its system requirements are not fully verified here.
- [推断] "Figma alternative" / "Claude Design alternative" are the project's positioning claims, not a feature-parity guarantee.
