---
name: add-project
description: 当要把一个新开源项目加进本选型索引时使用；联网调研该项目，按 tools/schema.md 产出合规的选型页(frontmatter 事实 + 7 个必需小节)，归类、更新分类 INDEX、跑 lint。不用于选型(用 select-oss)或刷新已有过期条目(用 sync-entry)。
argument-hint: <项目名 或 GitHub URL>
---

# add-project

Author one conformant selection page. The contract is `tools/schema.md`; read it first.

## Procedure

1. **Gate on inclusion criteria** (AGENTS.md): only add if you actually evaluated it AND a real
   selection question exists (substitutes worth comparing). If not, stop and say why.

2. **Research live.** Fetch the GitHub repo, README, releases, docs. Separate **facts**
   (stars, license, language, deps, latest version — each dated) from **judgment**. Anything you
   can't confirm from a source → label `[未验证]` / `[推断]`, never assert it.

3. **Classify.** Pick the single best **primary** category (= directory under `categories/`).
   Cross-cutting traits go in `tags`, not extra categories. Only create a new category if it
   genuinely doesn't fit — then also add a row to root `INDEX.md` **and** `INDEX.zh.md`.

4. **Write the bilingual pair** `categories/<category>/<slug>.md` (English) **and**
   `categories/<category>/<slug>.zh.md` (Chinese) per schema:
   - Frontmatter (identical in both): `name, slug(==base filename), repo, category(==dir), tags,
     language, license, maturity(dated), last_verified(today)`.
   - `# <name>` + one-line TL;DR in that file's language.
   - English page sections: `When to use / When NOT to use / Comparison / Tech stack /
     Dependencies / Ops difficulty`. Chinese page sections: `何时使用 / 何时不用 / 横向对比 /
     技术栈 / 依赖 / 运维难度`. Each file is monolingual — no language mixing.
   - Write "When to use" / "何时使用" as a **User Story** (second-person scenario: who you are,
     what you're doing, the problem you hit, how this tool resolves it) — not a feature list.
     See `tools/schema.md`.
   - Make the "when NOT to use" section the strongest: concrete anti-patterns, scale ceilings,
     lock-in, maintenance/abandonment risk. This is the section agents most need.
   - In Comparison, name 3–5 real substitutes; `未收录` for ones not in the index, relative link
     for ones that are.

5. **Wire it in.** Add the project to its `categories/<category>/INDEX.md` **and** `INDEX.zh.md`
   (one-liner + comparison-matrix row in each). If new category, add it to root `INDEX.md` +
   `INDEX.zh.md`.

6. **Lint.** `python3 tools/lint.py` — fix every ERROR before finishing.

## Quality bar

- Facts dated; judgment labeled. No marketing tone — write for an agent that will *act* on it.
- The page must answer "when should I NOT reach for this?" better than the project's own README.
- If you couldn't verify the basics (license, language, maintenance status), say so explicitly
  rather than guessing — a confident wrong fact routes an agent into a wall.
