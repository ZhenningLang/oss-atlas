---
name: Anthropic Skills
slug: anthropic-skills
repo: https://github.com/anthropics/skills
category: vendor-collections
tags: [agent-skills, claude, skill-pack, anthropic, plugin-marketplace]
language: Python
license: Apache-2.0
maturity: no tagged releases, active, last pushed 2026-06 (155k+ stars [未验证])
last_verified: 2026-06-26
type: skill-pack
---

# Anthropic Skills

Anthropic's own public collection of Agent Skills — self-contained `SKILL.md` folders (document editing, frontend/canvas design, MCP/skill authoring, brand & comms) installable into Claude Code, Claude.ai, or the Claude API.

## When to use

You're a developer or team standing up Claude as an agent and you keep re-explaining the same procedural tasks — "extract the form fields from this PDF", "build a .docx from this outline", "scaffold a new MCP server", "spin up a frontend artifact". You want first-party, reference-quality implementations of those procedures rather than hand-rolling prompts or trusting a random third-party bundle. This repo is the vendor source: each skill is a folder with a `SKILL.md` (YAML `name` + `description`, then markdown instructions) plus any helper scripts/resources, following Anthropic's own Agent Skills format. You install via the plugin marketplace (`/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills` or `example-skills@anthropic-agent-skills`), and the skills load on demand when their description matches the task.

You reach for it specifically when you want (a) the document skills (`docx`, `pdf`, `pptx`, `xlsx`) that power Claude's file generation, (b) a canonical `skill-creator` / `mcp-builder` to learn the format and author your own, or (c) a curated starter set (`frontend-design`, `canvas-design`, `brand-guidelines`, `internal-comms`, `slack-gif-creator`, `webapp-testing`, `claude-api`, etc.) maintained by the platform vendor. The `spec/` and `template/` directories make it the reference for writing skills against Anthropic's implementation. Use it as the baseline you adopt or fork before building a bespoke skill stack.

## When NOT to use

- **You already run a curated skill/command system you trust.** These ship with their own descriptions and routing; layering them onto an existing methodology stack invites overlap and double-firing (e.g. a `frontend-design` skill colliding with your own UI conventions). Pick one source of truth per concern.
- **Mixed license — read before redistributing.** The example skills are Apache-2.0, but the document skills (`docx`, `pdf`, `pptx`, `xlsx`) are explicitly **source-available, not open source**. There is no repo-wide LICENSE; don't assume Apache-2.0 covers everything you vendor or ship. [未验证]
- **You're not on a Claude-family harness.** Installation paths are Claude Code, Claude.ai, and the Claude API. The `SKILL.md` markdown won't auto-fire on a non-Claude agent with no compatible skill loader; portability to other harnesses is not a goal here.
- **You want a runnable tool/CLI/library.** There's nothing to `import` or run standalone — it's skill definitions plus helper resources that shape an agent's behavior, not an application.
- **You need pinned, stable behavior.** No tagged releases; skills are markdown/scripts that change on `main`. A pull can shift what a skill does or routes to. Vendor a specific commit if you need stability and re-check after updates. [推断]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| Claude plugins (official) | 未收录 | Anthropic's broader official plugin/marketplace surface; this `skills` repo is specifically the Agent Skills collection (document + example skills), not the full plugin catalog. Compare on whether you want skills only or the wider plugin set. |
| AWS Labs agent plugins | 未收录 | Another vendor-published collection, AWS-ecosystem-flavored; pick by which cloud/tooling bias matches your stack. Format/loader compatibility differs. |
| MiniMax skills | 未收录 | A different vendor's skill collection; overlapping "official starter skills" goal but tied to that vendor's models/harness. Cross-check format compatibility before mixing. |
| Third-party community skill packs (e.g. Superpowers) | 未收录 | Opinionated SDLC/methodology bundles layered on top of an agent. This repo is narrower and first-party: reference task skills + the authoring spec, not a full workflow methodology. |
| Roll your own `SKILL.md` skills | n/a | Maximum fit and zero external dependency, but you forgo the vendor's tested document-generation skills and the canonical spec/template. Many users fork from here as the baseline. |

## Caveats (unverified)

- [未验证] No tagged releases and no repo-wide LICENSE file as of 2026-06-26; license is per-area — example skills Apache-2.0, document skills (`docx`/`pdf`/`pptx`/`xlsx`) source-available. The `Apache-2.0` in frontmatter reflects the example skills only; verify the specific skill's terms before redistribution.
- [未验证] Primary language reported as Python per GitHub metadata; the repo mixes Python helper scripts with Markdown skill definitions and other languages — language tag is indicative, not a build target.
- [未验证] Star count (~155k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as a popularity hint, not a quality signal.
- [未验证] Skill inventory observed (algorithmic-art, brand-guidelines, canvas-design, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx) is a snapshot of `skills/` on 2026-06-26; the set and routing change on `main` — read the live directory.
- [未验证] Install commands and marketplace identifiers (`anthropic-agent-skills`, `document-skills`, `example-skills`) are from the README; exact plugin names and activation behavior may change — confirm against current docs.
- [推断] Because behavior lives in markdown `SKILL.md` instructions loaded by the agent, enforcement is advisory — the agent can deviate; skills describe procedures, they do not hard-guarantee outcomes.
