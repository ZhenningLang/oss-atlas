---
name: Taste-Skill
slug: taste-skill
repo: https://github.com/Leonxlnx/taste-skill
category: design
tags: [skills, design-taste, anti-slop, frontend, ui, claude-code, codex]
language: JavaScript
license: MIT
maturity: no tagged release, active, last push 2026-06 (51.2k stars [未验证])
last_verified: 2026-06-26
type: skill-pack
---

# Taste-Skill

A collection of portable, framework-agnostic agent skills whose single job is to give your coding agent visual taste — stopping it from emitting boring, generic "AI slop" frontends and pushing it toward intentional layout, typography, motion, and spacing.

## When to use

You're a developer or a vibe-coder using Claude Code, Codex, Cursor, or ChatGPT to scaffold a landing page or web app, and every time the agent produces a UI it looks the same: centered hero, three feature cards, a purple-to-blue gradient, default Tailwind spacing, zero motion. The output is technically correct but visually dead — it screams "an LLM made this." You don't want to hand-write a 2,000-word design brief every prompt, and you don't have a design system to point the agent at. You reach for Taste-Skill: you install it, and the agent loads a `SKILL.md` that injects an opinionated taste protocol — inferring a design direction from your brief, mapping it to a coherent design-system (color/type/spacing scale), laying in GSAP motion skeletons, and running anti-repetition checks so the next screen doesn't clone the last one.

It also ships tunable dials — `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY` on a 1–10 scale [未验证] — so you can dictate "loud and animated" vs. "calm and dense" without rewriting the prompt. Beyond the default frontend skill, the pack includes named aesthetic variants (`soft`, `minimalist`, `brutalist`), an `image-to-code` skill, a `redesign-existing-projects` skill, and image-generation skills (`imagegen-frontend-web/mobile`, `brandkit`) for producing reference visuals before you write code. Install once via `npx skills add` and the agent activates the right skill on demand.

## When NOT to use

- **You already run a design-taste / UI-critique skill you trust.** This overlaps heavily with sibling packs (designer-skills, stitch-skills, ui-ux-pro-max). Stacking two opinionated "make it look good" skills produces conflicting directives and double-routing — pick one taste source of truth.
- **You have a real design system or brand guide.** When colors, type scale, components, and tokens are already mandated, an inference-driven taste skill fights your constraints instead of serving them; encode the system directly (e.g. a `DESIGN.md`) and skip the guessing layer.
- **Backend, CLI, data, or non-visual work.** The pack only shapes frontend/visual output; it does nothing for an API, a migration, or a TUI.
- **Harness without a skill loader.** It activates through `SKILL.md` consumed by an agent (Claude Code, Codex, Cursor, ChatGPT); on a bespoke agent with no skill-loading mechanism the markdown won't auto-fire and you'd be pasting prompts by hand.
- **Advisory, not enforced.** Taste lives in prompt text the agent may ignore or dilute; "anti-slop protocol" is an instruction, not a lint gate. If you need deterministic enforcement, pair it with an artifact linter rather than relying on the skill alone.
- **Maintenance risk.** Single-author repo with no tagged releases; the v2 default is flagged experimental and skills get renamed/reorganized between pushes. Pin a commit if you need stability. [推断]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [designer-skills](designer-skills.md) | ✅ | Sibling design-taste pack; compare on which aesthetic variants and harnesses each covers and which one's protocol matches your output style. |
| [stitch-skills](stitch-skills.md) | ✅ | Sibling skill pack in the same design leaf; overlapping "improve agent UI output" goal, different skill primitives — pick by install target and variant coverage. |
| [ui-ux-pro-max](ui-ux-pro-max.md) | ✅ | Sibling pack leaning toward broader UI/UX guidance; Taste-Skill is narrower and centers anti-slop frontend generation with tunable variance/motion/density dials. |
| make-interfaces-feel-better | 未收录 | Listed as a leaf sibling but no page exists yet; compare on whether it enforces interaction polish vs. Taste-Skill's generation-time aesthetics. |
| Anthropic / built-in agent skills | 未收录 | Native skill ecosystem of the host harness; Taste-Skill is a third-party bundle layered on top and can duplicate or conflict with native design skills. |

## Health & viability

- **Maintenance (2026-06):** active — last push 2026-06, not archived, but no tagged releases at all, so "version" means a moving commit. Treat it as best-effort, not a versioned product.
- **Governance & bus factor:** single-author `User` repo (`Leonxlnx`) carrying ~52k stars — a textbook bus-factor flag: outsized adoption resting on one maintainer with no foundation/vendor backing.
- **Age & Lindy:** created 2026-02, so <1 year old as of 2026-06 — young and star-hyped, with a v2 default still flagged experimental and skills renamed/reorganized between pushes. Unproven on the Lindy axis; the star count says nothing about longevity.
- **Risk flags:** advisory-only enforcement (prompt/markdown, not a lint gate) + no semver + single maintainer ⇒ pin a commit if you need stable behavior.

## Caveats (unverified)

- [未验证] License MIT and primary language JavaScript per GitHub metadata as of 2026-06-26; repo last pushed 2026-06-20 with no tagged release (`latestRelease` null) — re-verify before relying on a specific version's behavior.
- [未验证] Star count (~51.2k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, never as a quality signal.
- [未验证] The skill inventory (taste-skill / taste-skill-v1 / gpt-tasteskill / image-to-code-skill / redesign-skill / soft / minimalist / brutalist / imagegen-frontend-web / imagegen-frontend-mobile / brandkit / stitch / output) is read from the README and `skills/` tree; install names and v2-experimental status may change between pushes — verify the current `skills/` directory.
- [未验证] The tunable dials (`DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`, 1–10) and GSAP-motion/design-system-mapping behavior are described in the README; their actual effect on output is not independently confirmed here.
- [未验证] Supported agents (ChatGPT, Codex, Cursor, Claude Code) and the `npx skills add` install path are from the project README; activation fidelity per harness is not verified.
- [推断] Because the taste protocol lives in prompt/markdown skills loaded by the agent, enforcement is advisory — the agent can still produce slop; "anti-slop" steps are prompt-level instructions, not hard guarantees.
