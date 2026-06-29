---
name: score-health
description: 当维护者要给某个选型页计算/重算「健康度雷达」、解释某轴档位为何如此、重试 ? 轴、或批量回填全索引时使用；封装 tools/health.py 评分引擎 + 卡片生成，按 docs/health-rubric.md 的客观阈值出分。不用于新增项目（用 add-project，它已内置评分）或刷新事实（用 sync-entry，它会顺带重算）。
argument-hint: <项目 slug | --explain <slug> | --retry <slug> | --backfill>
metadata:
  internal: true
---

# score-health

The maintainer hand-crank for the 6-axis **health radar**. The grades are **not** authored
by hand — they are computed deterministically by `tools/health.py` from GitHub + package
registries, against the objective thresholds in [`docs/health-rubric.md`](../../docs/health-rubric.md)
(same inputs → same grades). This skill wraps the engine so you don't memorize CLI flags.

> SSOT = the `health:` block in each page's frontmatter. Cards (`assets/health/<slug>.svg`
> + `<slug>.zh.svg`) are **derived** from it by `tools/health_card.py`. Never edit grades by hand;
> if a grade looks wrong, fix the rubric or the scorer, not the page.

Engine CLI (for reference): `python3 tools/health.py --page <path>.md [--write] [--evidence]`
(or `--repo owner/name --type <t>` for an ad-hoc score without a page). `--write` splices the
**identical** block into both the `.md` and `.zh.md` siblings.

## Modes

### 1. Score / re-score one project (default)
```bash
PAGE=categories/<cat>/<slug>.md
python3 tools/health.py --page "$PAGE" --write          # score live; write block to BOTH siblings
python3 tools/health_card.py "$PAGE" "${PAGE%.md}.zh.md" # regenerate EN + ZH cards from the block
python3 tools/lint.py                                    # must be 0 errors
```
Re-scoring bumps `computed_at`. Grades may legitimately move as live data shifts (e.g. an A/B
knife-edge on responsiveness) — that's real, not a bug.

### 2. Explain a grade (`--explain <slug>`)
Answer "why is axis X a D?" with evidence, not vibes:
```bash
python3 tools/health.py --page "$PAGE" --evidence        # prints per-axis raw measured values
```
Read the raw value against the matching threshold table in `docs/health-rubric.md` §2.<axis>
(e.g. maintenance `last_commit_age_days` / `active_weeks_13`; governance `top1_share`/`top3_share`;
adoption `dependent_repos_count` + `downloads_last_month`). Quote the number AND the threshold it
crossed. If the axis is `?`, name the reason code (§5.2 enums) — `?` means *unobtainable / N/A*,
never a low score.

### 3. Retry `?` axes (`--retry <slug>`)
Just re-run mode 1. The scorer **already retries transient `?`** (a `stats/*` cold-cache 202, a
rate-limited call, a moved repo) on every run. A `?` that persists is usually **structural** and
correct (e.g. adoption for an `app`/`skill-pack` that ships no package, governance for an archived
repo with zero in-window commits) — leave it `?`, don't force a grade.

### 4. Batch backfill the index (`--backfill`) — Phase 1
Use the operational runner, not a hand-written shell loop. It dry-runs by default, records a
checkpoint, prints progress/ETA, and keeps a failed set for retry:
```bash
python3 tools/health_backfill.py                         # dry-run: counts + samples, no writes
python3 tools/health_backfill.py --apply --yes --limit 5  # smoke apply on a bounded sample
python3 tools/health_backfill.py --apply --yes --resume   # full/resumed apply
```
State lives at `.health-backfill/state.json` by default. Use `--state <path>` for experiments,
`--sleep` to slow down under GitHub secondary rate limits, and `--timeout/--retries` for flaky
network calls. A GitHub token must be present (`gh auth status`); unauthenticated 60/hr dies early.

## Discipline
- **Machine SSOT, not hand-grades.** Don't touch the `health:` block or the SVGs by hand — re-run
  the scorer/generator. The pre-commit hook (`make install-hooks`) regenerates cards + lints, but
  verify lint is green yourself.
- **Both languages, every time.** After `--write`, regenerate **both** `<slug>.svg` and
  `<slug>.zh.svg` (cards are language-separated; never mix scripts on a card).
- **`?` is first-class.** Never coerce `?` to a grade or average it as 0/A.
- **Freshness.** Re-scoring updates `computed_at`. For broader fact rot (license, maturity, prose),
  that's [`sync-entry`](../sync-entry/SKILL.md)'s job — it calls this skill as one of its steps.

## Relationship to other skills
- `add-project` — runs this automatically when a new project is added (compute on add).
- `sync-entry` — re-scores as part of a staleness-gated refresh.
- `score-health` — the **direct** maintainer entry point: targeted re-score, explanation, retry, backfill.
