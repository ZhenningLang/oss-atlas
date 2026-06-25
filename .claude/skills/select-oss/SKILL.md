---
name: select-oss
description: 当收到一个任务、需要从开源项目里选型(选一个库/工具/系统)时使用；用本仓库的三级自然语言索引导航，按「何时不用」对照任务硬约束，产出带决定性 tradeoff 的 shortlist。不用于添加新条目(用 add-project)或刷新过期条目(用 sync-entry)。
argument-hint: <要解决的任务 / 选型需求>
---

# select-oss

This index exists so an agent can pick OSS for a task **fast and honestly**. Don't grep — descend the route.

## Procedure

1. **Frame the selection** from the task. Write down the hard constraints up front — these are
   what kill candidates:
   - scale / throughput expectations
   - deployment & ops budget (can the user run a DB? a GPU? a server?)
   - license constraints
   - language / ecosystem fit
   - must-have vs nice-to-have features

2. **Level 1 — category.** Read `INDEX.md`. Match the task to one or more categories by their
   "use when". If nothing fits, say so — the index may not cover this domain yet.

3. **Level 2 — shortlist.** For each candidate category, read `categories/<cat>/INDEX.md`.
   Use the one-liners + comparison matrix to pick 1–3 candidates.

4. **Level 3 — decide.** Read each candidate's `<slug>.md`. The decisive section is usually
   **`## When NOT to use`**: check it against the hard constraints from step 1. Then weigh
   `## Ops difficulty` and `## Dependencies` against the user's budget.

5. **Recommend** with the *tradeoff that decided it*, not just a name. Format:

   ```md
   ## Recommendation
   - **Pick: <project>** — <one-line why it fits this task>
   - Decisive tradeoff: <the when-not / ops / dep fact that ruled out the runner-up>
   - Runner-up: <project> — <why second>
   - Not chosen: <project> — <the disqualifying constraint>
   ```

## Honesty rules

- If the best fit is named in a `## Comparison` but marked `未收录` (not yet indexed), **say
  so** and recommend it anyway with a caveat — do not pretend the index is complete.
- Respect `last_verified`: if a candidate page is stale (lint warns), flag that its facts may
  be outdated and consider running `sync-entry` before relying on it.
- Surface `[未验证]` / `[推断]` labels from the page — don't launder them into confident facts.
- If two candidates are genuinely tied, present both with their tradeoffs instead of forcing a
  single pick.

## Anti-patterns

- Picking by star count or popularity instead of fit-to-constraints.
- Ignoring `## When NOT to use` because the positive scenario looked good.
- Recommending a project whose `## Dependencies` exceed the user's stated ops budget.
