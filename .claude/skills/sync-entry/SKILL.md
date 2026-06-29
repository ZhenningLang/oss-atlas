---
name: sync-entry
description: 当要刷新已有选型条目、对抗事实过期时使用；手动触发，按 last_verified 与今天的 delta 门控(超过阈值才真去联网重核),重核事实、更新变化项、bump last_verified,并对疑似废弃项目显著标注。不用于新增条目(用 add-project)或选型(用 select-oss)。
argument-hint: <项目 slug | 分类 | --all | --report>
metadata:
  internal: true
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
  delta ≤ STALE_DAYS** unless explicitly forced — do not waste a fetch on fresh entries. For stale
  entries, first run the cheap upstream probe below; only do the full reread when upstream changed.

## Cheap upstream probe for stale entries

For a stale page, do not immediately reread the whole repo. First compare today's upstream repo state
with the last recorded snapshot in the page frontmatter:

```yaml
upstream:
  pushed_at: 2026-06-29T00:00:00Z
  default_branch: main
  default_branch_sha: abc123
  archived: false
```

- If `upstream` is missing, do a full re-verify and write it.
- If `archived`, `default_branch`, or `default_branch_sha` changed, do a full re-verify.
- Treat `pushed_at` as a cheap hint, not the sole gate: GitHub updates it for non-default-branch
  pushes and tag/bot activity. The default-branch SHA is the stronger reread trigger.
- If the cheap probe matches the stored snapshot, skip the full reread and report `unchanged_upstream`;
  do not silently bump `last_verified` as if prose/facts were reread.

Use the read-only compare mode for the probe:

```bash
python3 tools/upstream_snapshot.py --page categories/<cat>/<slug>.md --check
```

It prints `unchanged_upstream` or `changed_upstream`, writes nothing, exits `0` when unchanged and
`1` when changed. Only after a full re-verify should you refresh the stored snapshot with
`--apply --yes`.

## Re-verify procedure (per stale entry)

> **Bilingual:** each entry is a pair (`<slug>.md` + `<slug>.zh.md`) with **identical
> frontmatter**. Apply every fact/frontmatter change to both files, and update both bodies if a
> material fact moved. `last_verified` must match across the pair.

1. **Cheap upstream probe**: compare `upstream` frontmatter against GitHub repo state. Stop here if
   the stale entry is unchanged upstream.
2. **Refetch the source of truth**: GitHub repo page, latest release, README, last-commit date.
3. **Diff the facts** against frontmatter + body:
   - license, primary language, latest version / `maturity`, dependencies, tech stack.
   - star count (informational; not a gate).
4. **Update only what changed.** Keep the fact/judgment split; re-label `[未验证]` items if now
   confirmable (or vice versa).
5. **Abandonment check** — flag prominently in `## When NOT to use` if any hold:
   - archived / read-only repo, or no commits in ~12 months,
   - latest release far behind a moved-on ecosystem,
   - maintainer notice of deprecation.
   Treat single-maintainer / young projects as higher abandonment risk.
6. **Re-judge if facts moved materially.** A new major version can invalidate "when not to use"
   (e.g. a missing feature now exists). Don't just bump the date over stale judgment.
7. **Update `upstream` and bump `last_verified` to today.** Only after actually re-checking — never
   bump blindly.
8. **Re-score the health radar.** Health grades go stale like any
   fact — re-run the scorer when you re-verify:
   `python3 tools/health.py --page <page> --write && python3 tools/health_card.py <page>`
   This recomputes the 6 axes from live data, rewrites the identical `health:` block into both
   siblings (bumping its `computed_at`), and regenerates the card. See `docs/health-rubric.md`.
9. **Lint**: `python3 tools/lint.py`.

## Discipline

- The date is a claim that *you verified the facts today*. Do not bump it without doing step 1–5.
- If a source is unreachable, leave the old date, add a `[未验证]` note on what couldn't be
  checked, and report it — don't fabricate a refresh.
- Report what changed: "synced N entries, U unchanged upstream, M facts updated, K flagged as abandonment-risk."
