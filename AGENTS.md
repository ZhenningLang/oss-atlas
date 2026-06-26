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
- **Is not**: a complete OSS directory, a tutorial site, or a marketing collection. It is
  curated and intentionally small. See "Inclusion criteria" below.

## READ ROUTE — how an agent navigates (3 levels)

Always descend in this order; do not grep blindly.

```
1. INDEX.md                          ← level 1: category route (English; 中文: INDEX.zh.md)
2. categories/<category>/INDEX.md    ← level 2: projects in that category + comparison matrix
3. categories/<category>/<slug>.md   ← level 3: the English selection page (canonical)
                                       Chinese sibling: <slug>.zh.md (same content, 中文)
```

English (`*.md` / `INDEX.md`) is the **canonical path you read by default**. The `.zh.md` /
`INDEX.zh.md` files are the monolingual Chinese mirror for human / Chinese-preference readers.

Procedure when you have a task and need to pick a project:

1. Read `INDEX.md`. Match the task to one or more **categories** by their one-line "use when".
2. For each candidate category, read its `INDEX.md`: scan the project one-liners and the
   comparison matrix to shortlist 1–3 projects.
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
- Required frontmatter (identical in both files): `name, slug, repo, category, tags, language, license, maturity, last_verified`.
- Required body sections — English page (exact H2): `When to use`, `When NOT to use`, `Comparison`,
  `Tech stack`, `Dependencies`, `Ops difficulty`. The Chinese page uses the Chinese headings:
  `何时使用`, `何时不用`, `横向对比`, `技术栈`, `依赖`, `运维难度`.
- **Bilingual**: the two files are monolingual mirrors — do NOT mix languages inside one file.
- **Truth labeling**: anything not confirmed from a source is `[未验证]` / `[推断]`. Date your
  facts (`maturity`, `last_verified`). Never assert opinion as fact — an agent will act on it.
- After writing, update the category `INDEX.md` + `INDEX.zh.md` (and the root `INDEX.md` +
  `INDEX.zh.md` if it's a new category), then run the linter.

Skills: `.claude/skills/add-project/` (author a new entry), `.claude/skills/sync-entry/`
(re-verify a stale entry), `.claude/skills/refactor-index/` (reorganize the taxonomy when the
directory gets chaotic — imbalanced/overlapping categories, miscategorized pages, tag drift).

## Inclusion criteria (anti-sprawl)

Add a project **only if** both hold:

1. it was actually evaluated (not catalogued from a list), and
2. a real selection question exists (there are substitutes worth comparing).

If a project has no credible alternative, or you have not actually looked at it, do not add it.
Keeping the index small is a feature, not a limitation.

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
- `category` in frontmatter MUST equal the parent directory name.
- Internal links are relative and must resolve (the linter checks this).
- One project = one bilingual page pair = one primary category. Cross-cutting belongs in `tags`.
