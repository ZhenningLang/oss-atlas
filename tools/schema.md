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

## 2. Files — a bilingual pair

Each project is **two files** in the same category dir:

- `<slug>.md` — the **English** page (canonical; what an agent reads by default)
- `<slug>.zh.md` — the **Chinese** page (same content, monolingual)

The linter requires both to exist (parity). Frontmatter is byte-identical across the pair
(facts are language-neutral); only the body language differs. `slug` in frontmatter is the
project slug for **both** files (e.g. `beads`), even though the Chinese file is `beads.zh.md`.

### Required body sections (exact H2 headings)

Both pages start with `# <name>` and a one-line TL;DR (in that page's language). Then six
required `##` sections, in this order:

| English page (`<slug>.md`) | Chinese page (`<slug>.zh.md`) | What goes here |
|---|---|---|
| `## When to use` | `## 何时使用` | a **User Story** (see below) — a concrete second-person scenario, not a feature list |
| `## When NOT to use` | `## 何时不用` | anti-patterns, scale ceilings, lock-in, maintenance risk — **the most valuable section** |
| `## Comparison` | `## 横向对比` | horizontal table vs real substitutes (see below) |
| `## Tech stack` | `## 技术栈` | languages, frameworks, datastores it is built on |
| `## Dependencies` | `## 依赖` | runtime/infra a user must run (db, services, hardware) |
| `## Ops difficulty` | `## 运维难度` | low / medium / high + why; deploy + maintain burden |

An optional final `## Caveats (unverified)` / `## 存疑（未验证）` section is encouraged to collect
`[未验证]` facts.

### "When to use" is a User Story

Write this section as a **User Story**, not a feature list — a concrete, second-person scenario:

- WHO you are (a believable role / persona)
- WHAT you're working on (the real task / context)
- the PROBLEM / pain you hit
- HOW you reach for this tool and what it does to resolve it

English uses "You're a …"; Chinese uses "你是…". 1–2 tight paragraphs. The persona/scenario is
illustrative, but the tool's role in it must be accurate — never invent capabilities the page
doesn't otherwise support. "When NOT to use" stays a sharp bulleted list (it's the decisive
filter); only "When to use" is narrative.

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
