# Entry Schema — the single source of truth

> 中文：本文件是**项目选型页的契约**。`tools/lint.py` 按本文件校验，所有 `categories/<cat>/<slug>.md` 必须遵守。改这里 = 改契约，必须同步改 linter。

A project page lives at `categories/<category-slug>/<project-slug>.md`. It has two parts:

1. **YAML frontmatter** — the *facts* (verifiable, dated). Machine-checkable.
2. **Markdown body** — the *judgment* (when to use, when not, comparison). Agent-readable prose.

This fact/judgment split is deliberate: facts go stale and must be re-verified (see `last_verified`); judgment is opinion and must be labeled, never asserted as eternal truth.

## 1. Frontmatter (required keys)

```yaml
---
name: Beads                         # display name
slug: beads                         # MUST equal the filename without .md
repo: https://github.com/owner/repo # canonical repo URL
category: agent-tooling             # MUST equal the parent directory name
tags: [task-graph, agent-memory]    # inline list, >=1 tag
language: Go                        # primary implementation language
license: Apache-2.0                 # SPDX id where possible
maturity: v0.x, active, NN.Nk stars (as of YYYY-MM)   # one line, DATED
last_verified: 2026-06-26           # ISO date YYYY-MM-DD — when facts were last checked
---
```

Optional keys: `homepage`, `stars`, `aka` (alternate names).

Rules enforced by the linter:

- All required keys present.
- `slug` == filename (without `.md`).
- `category` == parent directory name.
- `tags` is a non-empty inline list.
- `last_verified` parses as `YYYY-MM-DD`.
- **Staleness**: if `today - last_verified > STALE_DAYS` (default 90), the linter prints a **WARNING** (not an error). Run the `sync-entry` skill to re-verify and bump the date.

## 2. Body — required sections (exact H2 headings)

Every page MUST contain these seven `##` headings, in this order:

| Heading | What goes here | 中文 |
|---|---|---|
| `## 中文摘要` | One paragraph, Simplified Chinese: 是什么 / 最适合 / 何时别用 | 中文速览 |
| `## When to use` | User stories / positive scenarios — concrete, not marketing | 正面场景 |
| `## When NOT to use` | Anti-patterns, scale ceilings, lock-in, maintenance risk — **the most valuable section** | 反面场景 |
| `## Comparison` | Horizontal table vs real substitutes (see below) | 横向对比 |
| `## Tech stack` | Languages, frameworks, datastores it is built on | 技术栈 |
| `## Dependencies` | Runtime/infra a user must run (db, services, hardware) | 依赖 |
| `## Ops difficulty` | low / medium / high + why; deploy + maintain burden | 运维难度 |

The page starts with `# <name>` and a one-line English TL;DR before `## 中文摘要`.

### Comparison rules

- The `## Comparison` table compares against **real** substitute projects.
- A row may reference a project **not yet indexed** — mark it `未收录` / `not indexed`. This is allowed and expected (the index grows over time); it keeps comparisons honest instead of dangling.
- When a substitute *is* indexed, link it relatively: `[name](../<category>/<slug>.md)`.

## 3. Truth labeling (inherited discipline)

In the body, any claim you could not verify from a source must carry `[未验证]` (unverified) or `[推断]` (inferred). Facts in frontmatter must be dated via `maturity` / `last_verified`. Never present opinion as fact — an agent reading this will act on it.

## 4. Inclusion criteria (what earns a page)

This is a **curated** index, not a complete directory. A project earns a page only if:

- it was actually evaluated (not catalogued from a list), AND
- a real selection question exists (there are substitutes worth comparing).

If those do not hold, do not add it. Preventing sprawl is a feature.
