---
name: uv
slug: uv
repo: https://github.com/astral-sh/uv
category: python-tooling
tags: [python, packaging, dependency-manager, rust, cli]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 87k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T09:38:49Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: "?"
  overall_score: 0.0
  scored_axes: 0
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
---

# uv

An extremely fast Python package and project manager written in Rust, designed to replace pip, pip-tools, pipx, poetry, pyenv, and more with a single tool and a universal lockfile.

![uv — health radar](../../assets/health/uv.svg)

## When to use

You're a Python developer tired of waiting for `pip install` to resolve dependencies or juggling multiple tools — pip for installing, pip-tools for locking, pipx for CLI tools, pyenv for Python versions, poetry for project management. You want one tool that installs packages 10–100x faster than pip, manages Python versions, runs scripts with inline dependency metadata, and produces a universal lockfile you can check into Git. You're starting a new Python project or modernizing an existing one and want the fastest, most reliable packaging experience available.

## When NOT to use

- **If you need a mature, battle-tested ecosystem** — uv is relatively new (created 2023). While rapidly adopted, some edge cases in dependency resolution or platform-specific builds may still be rougher than pip or poetry.
- **If you rely on poetry-specific features** — Poetry's `pyproject.toml` extras, plugins, and build-backend ecosystem are not fully compatible. Migrating existing poetry projects may require manual adjustment.
- **If you need conda-forge or binary-scientific packages** — uv does not replace Conda/Mamba for scientific stacks that need precompiled binary distributions. It is a pip-replacement, not a Conda-replacement.
- **If you are on an exotic platform with no Rust toolchain** — uv provides prebuilt binaries for common platforms, but niche architectures may require building from source.
- **If your team is not ready to change workflows** — uv introduces new commands (`uv pip`, `uv run`, `uv lock`) that differ from standard pip/virtualenv workflows. The learning curve may not be worth the speed gain for stable legacy projects.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| pip | 未收录 | Python's default package installer. | pip is universal and stable but slow; uv is 10–100x faster with a modern resolver and lockfile. |
| Poetry | 未收录 | Python dependency management and packaging. | Poetry has mature project management and publish workflows; uv is faster but newer and still building feature parity. |
| pdm | 未收录 | Python package manager with PEP 582 support. | pdm is modern and spec-compliant; uv is faster but may lack some pdm-specific workflow features. |
| Conda | 未收录 | Cross-platform package manager for any language, especially scientific Python. | Conda handles binary scientific distributions; uv is Python-only and does not replace Conda's binary packaging. |

## Tech stack

- **Rust** — primary implementation language for performance and memory safety
- **PubGrub** — the dependency resolution algorithm (also used by cargo and dart)
- **PEP 517/518/621/660** — modern Python packaging standards support

## Dependencies

- A supported platform (macOS, Linux, Windows; x86_64 and ARM64)
- No Python runtime required for installation (self-contained Rust binary)
- A Python interpreter to manage (uv can install one for you)

## Ops difficulty

**Low**. A single static binary — install via `curl`, Homebrew, or PyPI. No daemon, no background service. For teams, the main cost is workflow migration and training.

## Health & viability

- **Maintenance**: Extremely active — daily commits, rapid releases. Created in 2023 but already one of the most starred Python tooling repos.
- **Governance**: Backed by Astral, a well-funded Python tooling company (also behind Ruff). Clear commercial backing with a strong Rust/Python team.
- **Backing**: Astral has demonstrated commitment through consistent investment in Ruff and uv. The company appears stable and focused on Python developer experience.
- **Adoption**: Rapidly growing — 87k stars, 3.2k forks, widely discussed in the Python community. Many projects are migrating from pip/poetry to uv.
- **Longevity**: Only ~3 years old (created 2023). While backed by a committed vendor, it lacks the Lindy track record of pip (20+ years). The risk is lower than a hobby project but higher than a foundation-backed tool.
- **Risk flags**: Apache-2.0 license is safe. Astral is a single-vendor company; if the business model fails, maintenance could slow. No relicense history yet, but watch for open-core/feature-gating as they build commercial offerings.

## Caveats (unverified)

- [未验证] The exact speedup factor varies by platform, cache state, and network conditions; 10–100x is the project's own benchmark claim.
- [未验证] Full feature parity with Poetry's build and publish workflows has not been achieved as of the verification date.
- [推断] Astral may introduce commercial tiers or feature-gating as the product matures, given the company's funding model.
