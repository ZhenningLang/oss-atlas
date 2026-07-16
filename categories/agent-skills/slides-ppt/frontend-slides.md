---
name: frontend-slides
slug: frontend-slides
repo: https://github.com/zarazhangrui/frontend-slides
category: slides-ppt
tags: [agent-skill, slides-ppt, frontend-slides, skill-pack]
language: JavaScript
license: NOASSERTION
maturity: active, ~25,713 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-06-23T20:08:19Z
  default_branch: main
  default_branch_sha: 9906a34d640d2111f724544cbc50f7f130569ae1
  archived: false
health:
  schema: 1
  computed_at: 2026-07-16T08:14:14Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 23
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 169
        last_commit_age_days: 23
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 7
        top1_share: 0.739
        top3_share: 0.826
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
---
# frontend-slides

Create beautiful slides on the web using a coding agent's frontend skills

![frontend-slides — health radar](../../../assets/health/frontend-slides.svg)

## When to use

You're evaluating a task in the `slides-ppt` area and want a real repository in the oss-atlas shortlist rather than an untracked name from a backlog. Reach for frontend-slides when the upstream description matches the job, when its license and maintenance profile are acceptable after verification, and when adopting a public project is preferable to writing a local one-off.

This is a first-pass intake page for a user-requested backlog item. Use it to route selection and compare nearby options, then reread the upstream README, license, examples, and release history before relying on it for high-stakes work.

## When NOT to use

- **You need a deeply reviewed atlas page today.** Prefer an older in-index page from the comparison table until this entry has had a full semantic review.
- **License is a hard constraint.** GitHub reported `NOASSERTION`; inspect the repository license files before commercial use, redistribution, or vendoring.
- **Maintenance risk is unacceptable.** If the project is young, single-maintainer, low-star, unversioned, or quiet, choose a more established substitute in the same category.
- **Your task needs a narrower substitute.** If another page's `When NOT to use` section names your exact constraint, prefer that page over this first-pass entry.
- **You cannot verify the upstream workflow.** Do not install, run, or vendor this repo before checking its README, scripts, dependencies, and any external API requirements.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Guizang PPT Skill](guizang-ppt.md) | ✅ | Choose Guizang PPT when a constrained single-file HTML deck with strong art direction is acceptable; choose this page when editable PowerPoint or a different deck workflow is the key constraint. | Guizang is opinionated and already reviewed; this entry expands the deck-skill surface but needs deeper review. |
| [HTML Anything](../../ai-design-generation/html-anything.md) | ✅ | Choose HTML Anything for broad Markdown-to-HTML artifacts; choose a slide-specific skill when the whole job is a presentation deck. | Broader artifact coverage vs narrower deck-specific constraints. |


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-06-23T20:08:19Z`.
- **Adoption snapshot:** ~25,713 GitHub stars as of 2026-07; this is a noisy signal and low-star projects are still included when the repository is real and relevant.
- **License snapshot:** `NOASSERTION` from GitHub metadata; manual license-file review remains required when license matters.
- **Lindy / governance:** not fully reviewed in this intake pass. Check age, owner type, contributor concentration, releases, and issue response before long-term adoption.
- **Risk flags:** first-pass page generated from the 2026-07-16 backlog; semantic comparison and dependency review are intentionally conservative.

## Caveats (unverified)

- [未验证] This page is generated from public GitHub metadata plus the user-provided intake list; upstream README, docs, examples, releases, and dependency manifests still need deeper review.
- [未验证] License, install commands, supported harnesses, and runtime requirements may differ from GitHub metadata; verify them in the repository before use.
- [推断] The comparison table starts from nearby atlas categories rather than a complete substitute survey; refine it after reading the full upstream project and adjacent alternatives.
