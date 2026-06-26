# AGENTS.md — oss-atlas

> This repo is read **primarily by coding agents** (and secondarily by humans). It is a
> curated, natural-language knowledge base for **OSS selection** (选型): when an agent gets a
> task, it reads this index to choose the right open-source project — weighing *when NOT to
> use* each option, not just what it does.
>
> The index is deliberately **weak**: no database, no search engine, no embeddings. Just
> Markdown an agent reads and reasons over. The structure below is the only "query API".

## What this is (and is not)

- **Is**: a selection-decision corpus. Each project page is the *opposite of a README* — it
  leads with positive scenarios, negative scenarios, horizontal comparison, tech stack,
  dependencies, and ops difficulty.
- **Is not**: a tutorial site, a marketing collection, or a dump of non-repos (SaaS pages,
  articles). It collects real open-source **repositories** broadly, across any domain, and
  organizes them for selection. See "Inclusion criteria" below.

## READ ROUTE — how an agent navigates (recursive tree)

`categories/` is a **recursive tree** (≥3 levels; large categories split into sub-categories).
Descend by `INDEX`; do not grep blindly.

```
INDEX.md                              ← root: top-level category route (中文: INDEX.zh.md)
categories/<cat>/INDEX.md             ← a category node: its project pages + child sub-categories
categories/<cat>/<subcat>/INDEX.md    ← deeper nodes, as the tree grows
…/<slug>.md                           ← a leaf: the English selection page (中文 sibling <slug>.zh.md)
```

English (`*.md` / `INDEX.md`) is the **canonical path you read by default**. The `.zh.md` /
`INDEX.zh.md` files are the monolingual Chinese mirror.

Procedure when you have a task and need to pick a project:

1. Read `INDEX.md`; follow the category that matches your task.
2. Keep **descending** through sub-category `INDEX.md` files (the tree can be deep) until you reach
   project pages; scan their one-liners + the comparison matrix to shortlist 1–3.
3. Read each shortlisted `<slug>.md`. The decisive section is usually **`## When NOT to use`**:
   check it against the task's hard constraints (scale, deps, ops budget, license).
4. Recommend with the *tradeoff that decided it*. If the best fit is named in a `## Comparison`
   but is **not yet indexed** (`未收录`), say so — do not pretend the index is complete.

There is a skill for this: `.claude/skills/select-oss/`.

## WRITE CONTRACT — how to add or update an entry

The schema is the contract: **`tools/schema.md`**. In short:

- A project is a **bilingual pair** in the same dir: `categories/<category>/<slug>.md` (English,
  canonical) + `categories/<category>/<slug>.zh.md` (Chinese). Both = YAML frontmatter (**facts**)
  + Markdown body (**judgment**). Keep facts and judgment separate.
- Required frontmatter (identical in both files): `name, slug, repo, category, tags, language, license, maturity, last_verified, type`.
- `type` ∈ `tool | library | app | framework | service | model | skill-pack` and decides which body
  sections are required.
- Required body sections — **all types**: `When to use`, `When NOT to use`, `Comparison` (Chinese:
  `何时使用`, `何时不用`, `横向对比`). **Non-`skill-pack` types also require**: `Tech stack`,
  `Dependencies`, `Ops difficulty` (`技术栈`, `依赖`, `运维难度`). A `skill-pack` (prompt/skill
  collection) omits those three — don't pad them with "N/A".
- **Bilingual**: the two files are monolingual mirrors — do NOT mix languages inside one file.
- **Truth labeling**: anything not confirmed from a source is `[未验证]` / `[推断]`. Date your
  facts (`maturity`, `last_verified`). Never assert opinion as fact — an agent will act on it.
- After writing, update its category `INDEX.md` + `INDEX.zh.md` (and parent/root `INDEX` files for a
  new category), then run the linter. If a category overflows (lint WARNs), run `refactor-index`.

Skills: `.claude/skills/add-project/` (author a new entry), `.claude/skills/sync-entry/`
(re-verify a stale entry), `.claude/skills/refactor-index/` (rebalance the tree — split overflowing
categories into sub-categories, merge thin/overlapping ones).

## Inclusion criteria

**The unit of inclusion is a git repository.** Add any real open-source **repo**, across any domain —
no domain restriction, and no requirement that an in-index substitute already exists (comparisons may
cite `未收录` alternatives). Breadth is the goal: whatever task an agent gets, it should find guidance.

Do **not** add: things that aren't a repository (hosted SaaS, landing pages, articles, docs sites,
ads); an exact duplicate of an already-indexed repo; or an empty/contentless repo. That's the whole
bar — crowded fields are handled by the self-balancing tree (split into sub-categories), not by
dropping entries.

## Lint (the only gate — no tests)

This is a content repo with no runtime logic, so there are **no unit tests**. The structural
linter is the quality gate:

```bash
python3 tools/lint.py
```

ERROR = exit non-zero (CI fails). WARNING = printed (e.g. an entry is stale). Run it before
committing. CI runs it on every PR (`.github/workflows/lint.yml`).

## Conventions

- Slugs are kebab-case; `slug` in frontmatter MUST equal the **base** filename (`beads` for both
  `beads.md` and `beads.zh.md`).
- `category` in frontmatter MUST equal the **immediate** parent directory name (the leaf category),
  at any depth in the tree.
- Internal links are relative and must resolve (the linter checks this).
- One project = one bilingual page pair = one leaf category. Cross-cutting belongs in `tags`.
