---
name: MiniMax Skills
slug: minimax-skills
repo: https://github.com/MiniMax-AI/skills
category: vendor-collections
tags: [agent-skills, minimax, skill-pack, claude-code, plugin-marketplace, multimodal]
language: C#
license: MIT
maturity: no tagged releases, active, last pushed 2026-04 (12.8k stars [未验证])
last_verified: 2026-06-26
type: skill-pack
---

# MiniMax Skills

MiniMax's official public collection of ~16 Agent Skills — production-quality guidance for frontend / fullstack / Android / iOS / Flutter / React Native / shader dev, plus document & media generation (pdf/docx/xlsx/pptx, music, vision) — installable into Claude Code and other coding agents via a plugin marketplace.

## When to use

You're a developer running Claude Code (or Cursor / Codex / OpenCode) and you keep re-explaining the same procedural, domain-heavy tasks: "scaffold a production-grade React frontend", "build a native Android screen", "generate a .docx from this outline", "make a GIF sticker", "produce a PPTX deck". You want first-party, reference-quality recipes for these instead of hand-rolling prompts or trusting a random third-party bundle. MiniMax Skills is the vendor source: a `skills/` directory of self-contained skill folders (`frontend-dev`, `fullstack-dev`, `android-native-dev`, `ios-application-dev`, `flutter-dev`, `react-native-dev`, `shader-dev`, plus `minimax-docx`, `minimax-xlsx`, `pptx-generator`, `minimax-pdf`, `gif-sticker-maker`, `vision-analysis`, `minimax-multimodal-toolkit`, `minimax-music-gen`, and more), each loaded on demand when its description matches the task.

You reach for it when you want an opinionated, ready-made skill bundle covering both software-dev disciplines and MiniMax's media/document/multimodal capabilities, and you're on a supported harness. Install once via the marketplace (`claude plugin marketplace add MiniMax-AI/skills`, then install the bundle), or — on Cursor/Codex/OpenCode — clone the repo and point your agent at the per-harness manifest dirs (`.claude-plugin`, `.cursor-plugin`, `.codex`, `.opencode`). The methodology then activates through the platform's native skill-loading mechanism, not as something you `import`.

## When NOT to use

- **You already run a curated skill stack you trust.** This is a vendor-opinionated bundle; layering 16 skills on top of an existing methodology stack invites overlapping or conflicting routing — pick one source of truth.
- **You only need software-dev discipline, not media generation.** Much of the value here is MiniMax-specific media/document/multimodal skills (music gen, vision, GIF/PPTX/DOCX). If you only want dev workflow guidance, a focused dev-methodology pack is leaner than installing the whole bundle.
- **You're not on a supported harness.** Skills activate through each platform's loader (Claude Code marketplace; Cursor/Codex/OpenCode manifest dirs). On a bespoke or unsupported agent there's no loader to fire them, and the markdown alone won't auto-activate.
- **You need the latest, frequently-shipped vendor source.** No tagged releases and last pushed 2026-04 [未验证] — re-check freshness before depending on a specific skill's behavior; an unmaintained skill in a domain you care about is worse than none.
- **You expect hard guarantees.** Behavior lives in prompt/markdown skills the agent loads; "production-quality guidance" is advisory, not enforced — the agent can still deviate.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [Anthropic Skills](anthropic-skills.md) | ✅ | First-party Anthropic bundle (document editing, frontend/canvas, MCP/skill authoring). Tighter Claude-format fidelity; narrower domain. MiniMax adds mobile/shader dev + MiniMax-specific media/multimodal skills. |
| [Claude Plugins (official)](claude-plugins-official.md) | ✅ | Anthropic's official *plugin* marketplace (commands/agents/hooks/MCP, not just skills). Broader plugin surface, Claude-only. MiniMax is a skill-focused, multi-harness vendor bundle. |
| aws-agent-plugins | not indexed | Another vendor/official plugin collection; compare on which harnesses each targets and whether you need cloud-specific vs media/dev-generalist skills. |
| Building your own `skills/` folder | not indexed | Full control, zero lock-in, no maintenance bus-factor risk — but you write and curate every skill yourself. MiniMax trades that for a ready-made, vendor-maintained bundle. |

## Caveats (unverified)

- [未验证] License MIT and primary language C# (≈68.5%, with Python ≈24.3%) per GitHub metadata as of 2026-06-26; C# dominance is attributed to .NET/OpenXML helper code behind the document skills (e.g. `minimax-docx`) — confirm against the repo before assuming a build toolchain.
- [未验证] Last pushed 2026-04-18 with **no tagged releases** as of 2026-06-26; treat the bundle as a snapshot and re-verify freshness before relying on any specific skill.
- [未验证] Star count (~12.8k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not as a quality signal.
- [未验证] The skill list (~16 skills: frontend/fullstack/android/ios/flutter/react-native/shader dev, plus pdf/docx/xlsx/pptx, gif-sticker, vision, multimodal, music-gen/playlist, buddy-sings) is read from the README/`skills/` listing; verify the current `skills/` directory rather than relying on this enumeration.
- [未验证] Supported-harness claim (Claude Code marketplace; Cursor/Codex/OpenCode via cloned manifest dirs) is from the README; actual activation fidelity per harness is not independently confirmed here.
- [推断] Because behavior lives in prompt/markdown skills loaded by the agent, enforcement is advisory — "production-quality guidance" is a prompt-level instruction, not a hard guarantee, and the agent can deviate.
