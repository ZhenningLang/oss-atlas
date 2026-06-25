---
name: sync-entry
description: 当要刷新已有选型条目、对抗事实过期时使用；手动触发，按 last_verified 与今天的 delta 门控(超过阈值才真去联网重核),重核事实、更新变化项、bump last_verified,并对疑似废弃项目显著标注。不用于新增条目(用 add-project)或选型(用 select-oss)。
argument-hint: <项目 slug | 分类 | --all | --report>
---

# sync-entry

Facts in this index are point-in-time snapshots. They rot. This skill is the **manual,
delta-gated** refresh: it only spends effort re-verifying entries that are actually stale.

## Staleness model

- Each page has `last_verified` (ISO date).
- `delta = today - last_verified`. Threshold = `STALE_DAYS`, default **90**
  (override via env `OSS_ATLAS_STALE_DAYS`; the linter uses the same value).
- `python3 tools/lint.py` already prints a **WARNING** for every entry past threshold — use that
  as the worklist.

## Modes

- **`--report`** — list entries sorted by `last_verified` (oldest first) with their delta.
  Run `python3 tools/lint.py` and read the staleness WARNINGs; or scan frontmatter dates.
  This is read-only; no fetching.
- **`<slug>` / `<category>` / `--all`** — re-verify the named scope. **Skip any entry whose
  delta ≤ STALE_DAYS** unless explicitly forced — do not waste a fetch on fresh entries.

## Re-verify procedure (per stale entry)

1. **Refetch the source of truth**: GitHub repo page, latest release, README, last-commit date.
2. **Diff the facts** against frontmatter + body:
   - license, primary language, latest version / `maturity`, dependencies, tech stack.
   - star count (informational; not a gate).
3. **Update only what changed.** Keep the fact/judgment split; re-label `[未验证]` items if now
   confirmable (or vice versa).
4. **Abandonment check** — flag prominently in `## When NOT to use` if any hold:
   - archived / read-only repo, or no commits in ~12 months,
   - latest release far behind a moved-on ecosystem,
   - maintainer notice of deprecation.
   Treat single-maintainer / young projects as higher abandonment risk.
5. **Re-judge if facts moved materially.** A new major version can invalidate "when not to use"
   (e.g. a missing feature now exists). Don't just bump the date over stale judgment.
6. **Bump `last_verified` to today.** Only after actually re-checking — never bump blindly.
7. **Lint**: `python3 tools/lint.py`.

## Discipline

- The date is a claim that *you verified the facts today*. Do not bump it without doing step 1–5.
- If a source is unreachable, leave the old date, add a `[未验证]` note on what couldn't be
  checked, and report it — don't fabricate a refresh.
- Report what changed: "synced N entries, M facts updated, K flagged as abandonment-risk."
