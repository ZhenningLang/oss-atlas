---
name: Vercel Agent Skills
slug: vercel-agent-skills
repo: https://github.com/vercel-labs/agent-skills
category: engineering
tags: [agent-skills, react, nextjs, vercel, web-performance, code-review, skills-sh]
language: JavaScript
license: MIT
maturity: no tagged releases, active (pushed 2026-06), ~28.3k stars (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# Vercel Agent Skills

Vercel's official collection of agent skills — install-on-demand audit/build guides for React, Next.js, Vercel deploys, web design, and docs — packaged in the [agentskills.io](https://agentskills.io/) / [skills.sh](https://skills.sh/) format.

## When to use

You're a frontend or full-stack engineer shipping a Next.js app on Vercel, working through a coding agent (Claude Code, Claude Desktop, or another harness that speaks the Agent Skills format). Your agent writes React that technically works but quietly regresses Core Web Vitals — request waterfalls, oversized bundles, needless re-renders — and you don't have Vercel's internal performance handbook memorized to catch it in review. Or your function bill crept up and you can't tell which routes are the cost drivers. You want the agent to apply Vercel Engineering's actual house rules instead of generic advice.

You run `npx skills add vercel-labs/agent-skills` and the agent gains a menu of on-demand skills it loads when the task matches: `react-best-practices` (40+ perf rules across 8 categories — waterfalls, bundle size, server-side perf), `composition-patterns` (avoid boolean-prop proliferation), `react-view-transitions`, `react-native-skills`, `web-design-guidelines` (100+ accessibility/UX rules), `writing-guidelines` (Vercel's writing handbook for docs review), `vercel-optimize` (pulls real Vercel metrics first, then audits only the routes those metrics flag for cost/caching/ISR/function issues), plus deploy helpers (`deploy-to-vercel`, `vercel-cli-with-tokens`). You reach for it when your stack *is* React + Vercel and you want the vendor's own opinionated guidance applied automatically rather than authoring those rule sets yourself.

## When NOT to use

- **You're not on React/Next.js/Vercel.** The bulk of the value is React perf rules, Next.js patterns, and Vercel-specific deploy/cost audits. On a Vue/Svelte/Astro or non-Vercel-hosted stack, most skills don't apply and the deploy/optimize skills assume the Vercel platform outright.
- **You already run a curated web-quality skill stack.** If you've installed another web-perf or accessibility skill pack, layering Vercel's on top risks conflicting rule sets and double-routing during review — pick one source of truth per concern.
- **Your harness doesn't speak the Agent Skills format.** These activate via the agentskills.io / skills.sh loading mechanism; on a harness with no such loader, the markdown won't auto-fire and you'd be copy-pasting prompts by hand.
- **You want enforcement, not advice.** Rules live in prompt/markdown the agent *should* follow; nothing blocks a merge or fails CI. It's advisory review guidance, not a gate.
- **You need version stability.** No tagged releases as of this check — you track a moving `main`, so rule sets and skill boundaries can shift between pulls. [推断]
- **You want a runnable library/CLI.** There's nothing to `import`; the helper scripts run *inside* a skill the agent invokes, not as a standalone tool you call yourself.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [Agent Skills (addyosmani)](addyosmani-agent-skills.md) | ✅ | Addy Osmani's personal engineering skill set; overlapping web-perf/quality focus but maintained by an individual and not Vercel-platform-coupled. Compare on which rule sources you trust and whether you're on Vercel. |
| [web-quality-skills](addyosmani-web-quality.md) | ✅ | Dedicated web-quality/perf/accessibility skills; narrower than Vercel's broader bundle (deploy + optimize + React patterns) but vendor-neutral, so it travels off Vercel. |
| [Waza](waza.md) | ✅ | Another engineering skill pack in this leaf; compare on domain coverage and which workflows each actually encodes. |
| [Scientific Agent Skills](scientific-agent-skills.md) | ✅ | Scientific/eng-workflow skills — different domain (research/data) than web/frontend engineering; complementary, not a substitute. |
| Anthropic / community official skills (e.g. superpowers) | 未收录 | General SDLC/methodology skill packs shape *how* the agent works (TDD, planning); Vercel's pack supplies *domain* rules for React/Vercel. Often run together, not either/or. |

## Caveats (unverified)

- [未验证] License is MIT per the repo README's `## License` section; the GitHub license API and a top-level `LICENSE` file both returned empty on 2026-06-26, so the SPDX id rests on the README declaration alone — confirm before relying on it.
- [未验证] Primary language reported as JavaScript by GitHub metadata (2026-06-26); the substance is markdown skill definitions plus helper scripts, so the language tag reflects tooling/scripts, not a runnable JS app.
- [未验证] No tagged releases / `latestRelease` is null as of 2026-06-26; "maturity" is inferred from last push (2026-06-10) and activity, not a semver.
- [未验证] Star count (~28.3k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] The skill inventory (vercel-optimize, react-best-practices, composition-patterns, react-view-transitions, react-native-skills, web-design-guidelines, writing-guidelines, deploy-to-vercel, vercel-cli-with-tokens) and rule counts (40+/100+/80+/16) are from the README and `skills/` listing on 2026-06-26; verify the live directory rather than trusting this snapshot, since it tracks an untagged `main`.
- [推断] Activation fidelity depends on each harness's Agent Skills loader; README names claude.ai/Claude Desktop explicitly, but behavior on other harnesses is not independently confirmed here.
- [推断] Because rules are prompt/markdown the agent loads, enforcement is advisory — the agent can deviate and nothing fails the build.
