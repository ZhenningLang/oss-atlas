---
name: add-project
description: 当要把一个新开源项目加进本选型索引时使用；联网调研该项目，按 tools/schema.md 产出合规的选型页(frontmatter 事实 + type 自适应小节 + Caveats 存疑账本)，归类、更新分类 INDEX、跑 lint。不用于选型(用 select-oss)或刷新已有过期条目(用 sync-entry)。
argument-hint: <项目名 或 GitHub URL>
metadata:
  internal: true
---

# add-project

Author one conformant selection page. The contract is `tools/schema.md`; read it first.

## Procedure

1. **Gate on inclusion criteria** (AGENTS.md / schema §4 — keep the bar wide). The unit is a
   **git repository**. Add it if it is a real, non-empty open-source repo and not an exact
   duplicate of one already indexed — **across any domain, with no requirement that a substitute
   already exists in the index** (the `## Comparison` may cite `未收录` alternatives). Do not
   reject a valid long-tail repo for lack of in-index peers. Only stop if it is a non-repo (hosted
   SaaS, landing page, article, docs site), an exact duplicate, or contentless.

2. **Research live** — follow the `read-repo` skill's methodology (read order, how deep, how to mine
   the negative space). Fetch repo metadata (`gh api repos/<o>/<r>`: `created_at` for age/Lindy,
   `pushed_at`, `archived`, releases cadence, contributors for bus factor, `owner.type`), README,
   docs, the dependency manifest, and governance/LICENSE files. Separate **facts** (stars, license,
   language, deps, latest version, age — each dated) from **judgment**. Anything you can't confirm
   from a source → label `[未验证]` / `[推断]`, never assert it.

3. **Classify.** Pick the single best **primary** category (= directory under `categories/`).
   Cross-cutting traits go in `tags`, not extra categories. Only create a new category if it
   genuinely doesn't fit — then also add a row to root `INDEX.md` **and** `INDEX.zh.md`.

4. **Write the bilingual pair** `categories/<category>/<slug>.md` (English) **and**
   `categories/<category>/<slug>.zh.md` (Chinese) per schema:
   - Frontmatter (identical in both): `name, slug(==base filename), repo, category(==leaf dir), tags,
     language, license, maturity(dated), last_verified(today), type`.
   - `type` ∈ `tool | library | app | framework | service | model | skill-pack` — it decides which
     sections are required.
   - `# <name>` + one-line TL;DR in that file's language.
   - Sections (all types): English `When to use / When NOT to use / Comparison`; Chinese
     `何时使用 / 何时不用 / 横向对比`. **Non-`skill-pack` also add**: `Tech stack / Dependencies /
     Ops difficulty` (`技术栈 / 依赖 / 运维难度`). A `skill-pack` omits those three. Each file is
     monolingual — no language mixing.
   - Write "When to use" / "何时使用" as a **User Story** (second-person scenario: who you are,
     what you're doing, the problem you hit, how this tool resolves it) — not a feature list.
     See `tools/schema.md`.
   - Make the "when NOT to use" section the strongest: concrete anti-patterns, scale ceilings,
     lock-in, maintenance/abandonment risk. This is the section agents most need.
   - **Health & viability** (`健康度与可持续性`) — required for **all types** (skill-pack included).
     A short dated, labeled verdict on whether it's worth betting on: maintenance/cadence,
     governance & bus factor, backing org, **age as a Lindy prior (age × still-active)**, adoption/
     ecosystem, risk flags (relicense/open-core/CVE). See `tools/schema.md` §7. Judgment, not a
     number dump — volatile numbers stay in `maturity`/Caveats.
   - In Comparison, name 3–5 real substitutes; `未收录` for ones not in the index, relative link
     for ones that are.
   - **Caveats ledger (all types):** end every page with `## Caveats (unverified)` /
     `## 存疑（未验证）` — one `[未验证]`/`[推断]` bullet per unverified fact. In the prose above,
     keep inline labels to the **load-bearing/contested few** (≤3; the linter WARNs above that);
     the full uncertainty list lives in this ledger, not sprinkled across the body.

   - **Chinese punctuation (`.zh.md`)**: use fullwidth `，；：！？（）`, never the ASCII forms next
     to Chinese characters (the classic slip is `,` between two 汉字 where it must be `，`). Code,
     link targets, URLs, and frontmatter stay ASCII. The linter ERRORs on violations.

5. **Wire it in.** Add the project to its `categories/<category>/INDEX.md` **and** `INDEX.zh.md`
   (one-liner + comparison-matrix row in each) **and to the README master listing** (`README.md` +
   `README.zh.md`). If new category, also add it to root `INDEX.md` + `INDEX.zh.md`. The linter
   ERRORs if a page is missing from its INDEX or from either README, so nothing drifts silently.

6. **Lint.** `python3 tools/lint.py` — fix every ERROR before finishing.

## Quality bar

- Facts dated; judgment labeled. No marketing tone — write for an agent that will *act* on it.
- The page must answer "when should I NOT reach for this?" better than the project's own README.
- If you couldn't verify the basics (license, language, maintenance status), say so explicitly
  rather than guessing — a confident wrong fact routes an agent into a wall.
