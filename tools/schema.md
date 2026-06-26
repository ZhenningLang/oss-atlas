# Entry Schema — the single source of truth

> 中文：本文件是**项目选型页的契约**。`tools/lint.py` 按本文件校验，所有 `categories/<cat>/<slug>.md` 必须遵守。改这里 = 改契约，必须同步改 linter。

A project page lives in the **category tree** under `categories/…/<project-slug>.md` (the tree is recursive and self-balancing — see §5). It has two parts:

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
type: tool                          # tool | library | app | framework | service | model | skill-pack
---
```

Optional keys: `homepage`, `stars`, `aka` (alternate names).

Rules enforced by the linter:

- All required keys present.
- `slug` == filename (without `.md` / `.zh.md`).
- `category` == the **immediate** parent directory name (the leaf category), at any tree depth.
- `tags` is a non-empty inline list.
- `type` is one of `tool | library | app | framework | service | model | skill-pack`. It decides which body sections are required (§2).
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

Both pages start with `# <name>` and a one-line TL;DR (in that page's language). Then the
required `##` sections below — **which ones are required depends on `type`** (note after the table):

| English page (`<slug>.md`) | Chinese page (`<slug>.zh.md`) | Required for | What goes here |
|---|---|---|---|
| `## When to use` | `## 何时使用` | **all types** | a **User Story** (see below) — a concrete second-person scenario, not a feature list |
| `## When NOT to use` | `## 何时不用` | **all types** | anti-patterns, scale ceilings, lock-in, maintenance risk — **the most valuable section** |
| `## Comparison` | `## 横向对比` | **all types** | horizontal table vs real substitutes (see below) |
| `## Tech stack` | `## 技术栈` | non-`skill-pack` | languages, frameworks, datastores it is built on |
| `## Dependencies` | `## 依赖` | non-`skill-pack` | runtime/infra a user must run (db, services, hardware) |
| `## Ops difficulty` | `## 运维难度` | non-`skill-pack` | low / medium / high + why; deploy + maintain burden |
| `## Caveats (unverified)` | `## 存疑（未验证）` | **all types** | a bulleted **ledger**: one `[未验证]`/`[推断]` bullet per unverified fact — the page's single uncertainty list |

**Type-adaptive sections.** `skill-pack` entries (prompt/skill collections, harness configs) require
only the first three (`When to use / When NOT to use / Comparison`) — a bag of prompts has no
meaningful tech-stack / dependencies / ops, so those three are omitted rather than padded with
"N/A". All other types (`tool/library/app/framework/service/model`) require all six. The linter
enforces the right set per `type`.

**Caveats is required — it is the uncertainty ledger.** Every page ends with
`## Caveats (unverified)` (EN) / `## 存疑（未验证）` (ZH): a bulleted list where each unverified or
inferred fact gets one `[未验证]` / `[推断]` bullet. This is the single place uncertainty is collected;
the linter ERRORs if it is missing. See §3 for how it interacts with inline labels.

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

**Inline density.** Don't sprinkle `[未验证]` on every claim in the prose. In the body sections
(When to use / NOT / Comparison / Tech stack / Dependencies / Ops difficulty), label inline only the
**load-bearing or contested** points — e.g. a contradiction the reader must weigh in context — aiming
for **≤ `PROSE_LABEL_MAX` (default 3)** inline labels before the Caveats heading. Every unverified
fact, *including the ones you left unlabeled in prose*, still gets its own bullet in the
`## Caveats (unverified)` ledger. The linter WARNs when prose density exceeds the threshold; the ledger
is where the full uncertainty list lives.

## 4. Inclusion criteria (what earns a page)

**The unit of inclusion is a git repository.** This index collects and organizes open-source
**repositories** across any domain — there is **no domain restriction**, and a project does **not**
need an existing in-index substitute (comparisons may reference `未收录` alternatives). Breadth is
the point: whatever task an agent gets, it should find selection guidance.

Do **not** add:

- things that are **not a repository** — hosted SaaS, product landing pages, articles, docs sites, ads;
- an **exact duplicate** of an already-indexed repo (e.g. a vendor landing page for a repo already listed);
- an **empty / contentless** repo (no description, nothing to write a page from).

That's the whole bar. (Homogeneous fields still get organized via the self-balancing tree in §5, not
by dropping entries.)

## 5. The category tree (recursive + self-balancing)

`categories/` is a **recursive tree**, not a fixed 3 levels. A directory containing an `INDEX.md`
(+ `INDEX.zh.md`) is a **category node**; it may hold project pages, child sub-categories, or both.
Routing splits by language at every node: `INDEX.md` (EN) links `.md` pages and child `INDEX.md`;
`INDEX.zh.md` (ZH) links `.zh.md` pages and child `INDEX.zh.md`. The root `INDEX.md` /`INDEX.zh.md`
link the top-level categories.

**Self-balancing.** When a leaf category exceeds `MAX_FANOUT` project pages (default 12, env
`OSS_ATLAS_MAX_FANOUT`), the linter emits an **overflow WARNING** — the signal to split it into
sub-categories. When categories become too thin/overlapping, they should be merged. The
`refactor-index` skill performs these split/merge rebalances (`git mv`, additive-first, lint as the
gate). Detection is automatic (lint); the restructure is run via the skill, not silently.
