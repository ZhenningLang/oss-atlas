---
name: Spec Kit
slug: spec-kit
repo: https://github.com/github/spec-kit
category: agent-dev-methodology
tags: [spec-driven, prd, methodology, ai-coding, copilot, agent-dev, development-process]
language: Python
license: MIT
maturity: active, ~116.8k stars (as of 2026-07)
last_verified: 2026-07-01
type: skill-pack
upstream:
  pushed_at: 2026-07-01T01:09:03Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
    responsiveness:
      grade: ?
      raw: {}
    adoption:
      grade: A
      raw:
        stars: 117269
    longevity:
      grade: E
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Spec Kit

An open-source toolkit from GitHub that helps you get started with Spec-Driven Development — focusing on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.

![Spec Kit — health radar](../../assets/health/spec-kit.svg)

## When to use

You're a developer or product manager who uses AI coding agents (Copilot, Claude Code, Codex, etc.) and you're tired of "vibe coding" — writing a vague prompt, getting code that almost works, and then iterating by feel. You want a structured methodology: write a spec first, define the scenario and expected outcomes, and let the agent build against that contract. You install Spec Kit and get CLI tooling (`specify`), PRD templates, role-based bundles, and AI-agent integrations that turn "build me a feature" into "here is the spec, implement it to these acceptance criteria." It is especially useful when you work on GitHub and want your coding agent to respect a disciplined development process rather than generating ad-hoc solutions.

You also reach for it when you want to standardize how your team uses AI agents. Spec Kit provides extensions, presets, and a documented process (brainstorm → plan → build → review → ship) that can be shared across team members, making agent-assisted development more predictable and reviewable.

## When NOT to use

- **You don't use AI coding agents.** Spec Kit is designed around the agent-assisted workflow; without Copilot, Claude Code, or a similar harness, the methodology loses its primary integration point and much of its value.
- **You prefer lightweight, ad-hoc coding without formal specs.** If your projects are small experiments, prototypes, or one-off scripts, the overhead of writing a PRD and running through a spec-driven phase pipeline may be slower than simply prompting the agent directly.
- **You need a mature, battle-tested methodology.** Spec Kit was created in 2025-08 and is less than a year old. While it is backed by GitHub, the spec-driven development practices it encodes are still evolving and have not been proven over multiple years or at massive scale. [推断]
- **You are not in the GitHub ecosystem.** While the methodology is portable, the tooling and integrations (Copilot-centric bundles, GitHub Pages docs) are optimized for GitHub users. Teams on GitLab or Bitbucket may find the integration surface thinner. [推断]
- **You need a comprehensive project-management platform.** Spec Kit is a methodology and CLI toolkit, not Jira or Linear. It does not track sprints, manage backlogs, or handle cross-team dependencies — it helps you write specs for agent-driven implementation, not manage the project lifecycle. [推断]
- **You want guaranteed outcome quality.** Spec-Driven Development improves predictability, but it does not eliminate the inherent uncertainty of AI-generated code. You still need human review, testing, and iteration.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [12-Factor Agents](12-factor-agents.md) | ✅ | Use this page for its stated niche; choose 12-Factor Agents when you want high-level design principles for production agents rather than a coding-phase spec methodology. | High-level design principles for production agent architecture; more abstract and less prescriptive about the day-to-day coding workflow than Spec Kit. |
| [Superpowers](superpowers.md) | ✅ | Use this page for its stated niche; choose Superpowers when you want a drop-in brainstorm→plan→TDD→verify SDLC methodology installed into your coding agent. | Drop-in brainstorm→plan→TDD→verify SDLC methodology for Claude Code; overlapping goals but different packaging (skill/plugin vs CLI toolkit). |
| [get-shit-done](get-shit-done.md) | ✅ | Use this page for its stated niche; choose get-shit-done when you want an opinionated phase pipeline that fights context rot with fresh contexts per stage. | Opinionated phase pipeline with fresh-context-per-stage discipline; narrower workflow focus vs Spec Kit's broader spec-driven development toolkit. |
| [Compound Engineering](compound-engineering.md) | ✅ | Use this page for its stated niche; choose Compound Engineering when you want a turnkey loop that persists learnings across coding-agent sessions. | Turnkey brainstorm→plan→work→review→compound loop with session-persistence; less about spec authoring and more about iterative improvement. |
| [ECC](ecc.md) | ✅ | Use this page for its stated niche; choose ECC when you want a batteries-included Claude Code harness with skills, agents, hooks, memory, and security scanning. | Batteries-included Claude Code harness with a broad feature set; the methodology layer is one part of a larger agent infrastructure. |

## Health & viability

- **Maintenance (2026-07).** Last pushed 2026-07-01 with active development; the project is not archived and receives updates from GitHub's team. [推断]
- **Governance / bus factor.** Owned by GitHub (Microsoft) — a **very strong backing** signal with virtually zero bus-factor risk from maintainer attrition. The roadmap is tied to GitHub's AI strategy, which is both a strength and a potential lock-in concern. [推断]
- **Age & Lindy verdict.** Less than a year old (created 2025-08) ⇒ **very weak Lindy** signal. It is a young, hype-backed project with massive star count but no proven long-term track record. The backing by GitHub improves longevity odds, but the methodology itself is unproven at scale. [推断]
- **Adoption & ecosystem.** ~116.8k stars (as of 2026-07) driven largely by GitHub branding and the AI-coding hype cycle; real production adoption and community ecosystem depth are unclear at this early stage. [未验证]
- **Risk flags.** MIT license is permissive. The primary risk is **vendor strategy coupling**: if GitHub shifts its AI agent roadmap, Spec Kit's maintenance and relevance could decline. The project is also extremely young, so the methodology may change significantly as it matures. [推断]

## Caveats (unverified)

- [未验证] ~116.8k GitHub stars as of 2026-07-01; the star count is heavily influenced by GitHub branding and AI hype, not necessarily organic production adoption.
- [未验证] The exact CLI commands (`specify`), bundle contents, and AI-agent integrations are evolving rapidly; verify the current release docs before adopting.
- [未验证] GitHub's long-term commitment to Spec Kit as a standalone open-source project (vs. an internal GitHub feature) is unclear; the project may pivot or be absorbed into Copilot workflows.
- [推断] Spec-Driven Development is a promising methodology, but its effectiveness with AI agents depends heavily on the quality of the spec writer and the capabilities of the agent harness; it is not a magic bullet.
- [推断] The project is extremely young (created 2025-08); expect API changes, CLI redesigns, and methodology shifts as it matures.
- [推断] "Predictable outcomes" is an aspirational goal, not a guaranteed property; AI-generated code still requires testing, review, and iteration regardless of how good the spec is.
