---
name: beads
slug: beads
repo: https://github.com/gastownhall/beads
category: agent-tooling
tags: [ai-agents, task-graph, agent-memory, dolt, versioned-sql, dependency-graph, cli, go, long-horizon-tasks, multi-agent]
language: Go
license: MIT
maturity: v1.x line, active as of 2026-06; author still self-describes as "alpha" (see caveats)
last_verified: 2026-06-26
---

# beads

A dependency-aware, version-controlled task/issue graph that gives AI coding agents persistent structured memory — backed by Dolt (versioned SQL), shipped as a single Go binary (`bd`). Started by Steve Yegge; repo moved from `steveyegge/beads` to the `gastownhall` org.

## When to use

Use it when an AI coding agent (or a small fleet of them) needs durable, structured, dependency-aware task memory **across sessions and branches** — long-horizon work where the agent otherwise loses task context across sessions/compactions, silently drops discovered bugs to save context, or takes token-budget shortcuts.

It fits agent-native, offline-first workflows where you want task state version-controlled and merge-able alongside the code (hash IDs avoid collisions across parallel branches/agents), `bd ready` to auto-surface unblocked work, and `bd remember`/`bd prime` as a replacement for ad-hoc `MEMORY.md` scratch files. Good for solo developers or single-repo teams supervising agents who prefer a git-style, branchable task graph over a hosted tracker.

## When NOT to use

- **Stability / maturity signal** — despite a v1.x release line, the author's launch post described it as "alpha" software and the FAQ admits "command flags and data formats can evolve" `[未验证]` (whether maintainers still consider 1.x alpha as of 2026-06 is unconfirmed). It explicitly says *not* for "mission-critical production systems without a tested backup/restore plan" or "large enterprise deployments that need formal compatibility guarantees."
- **Human-team trackers** — no web UI, cross-repo dashboards, notifications, or non-engineer access. By design (it trades those for agent-native APIs).
- **Cross-project work** — each database is isolated; issues cannot reference issues in another project. A monorepo-of-services or portfolio view needs multiple DBs + custom glue.
- **Multi-writer at scale** — embedded mode is single-writer (file lock); concurrent agents require an external Dolt server plus a "claim work" convention (a user-defined "who's working on what" protocol so two agents don't race the same task) — real ops overhead.
- **Very large backlogs** — `[未验证]` the project's own FAQ reportedly suggests filtering exports or splitting into multiple databases past ~100k issues (its guidance, not independently benchmarked).
- **Migration / lock-in** — `[未验证]` export appears to be JSONL-only with no built-in importers from GitHub Issues/Jira/Linear found, so migrating *out* would need custom scripting; either way you inherit Dolt as the storage format.
- **Backend churn** — `[未验证]` documented SQLite→Dolt and 0.x→1.0 migrations with schema-repair steps; upgrades are not always painless.
- **DB fragility** — `[未验证]` per the project's own docs/warnings, agents have at times run destructive operations on the DB (e.g. `DROP TABLE`); treat it as not "set and forget" and keep backups.
- **Bus-factor** — `[未验证]` young, reportedly largely AI-built ("a tool that AI has built for itself"), under an org renamed from `steveyegge` to `gastownhall`; treat single-maintainer / abandonment risk as non-trivial, especially for mission-critical agent workflows you can't afford to re-tool.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| Plain markdown `MEMORY.md` / `TODO.md` | 未收录 | Zero deps and human-readable, but no dependency graph, no ready-detection, no merge-safe IDs — exactly the unstructured approach beads replaces. |
| GitHub Issues (+ `gh` CLI) | 未收录 | Mature hosted tracker with web UI/notifications/cross-repo views, but online-first, not branch-scoped/version-controlled, no native dependency-graph + auto-ready for agents. |
| Taskwarrior | 未收录 | Battle-tested offline CLI task manager with rich filtering, but no SQL/version-control backend, weaker multi-agent merge story, not built around agent JSON workflows. |
| Linear / Jira | 未收录 | Best-in-class for human teams (workflows, dashboards, guarantees), but heavyweight, online-only, not version-controlled with the code, not agent-native. |
| Dolt directly (raw versioned SQL) | 未收录 | Same versioned-SQL superpowers without an opinionated schema, but you build the issue schema, dependency logic, ready-detection and agent ergonomics yourself — beads is that opinionated layer. |

## Tech stack

- Go (~95%)
- Dolt — version-controlled SQL backend, embedded in-process via CGO
- JSONL — export / migration format
- CLI binary `bd`
- Distribution via Homebrew / npm (`@beads/bd`) / shell install script

## Dependencies

- **Dolt backend** — embedded in-process in the default prebuilt binary (no separate Dolt install for embedded mode). A `CGO_ENABLED=0` build is server-mode-only and needs an external `dolt sql-server`.
- **Server (multi-writer) mode** — an external Dolt SQL server process plus host/port/credential config.
- **Optional** — a git remote to sync the `.beads` database alongside the repo (`bd dolt push/pull`).

## Ops difficulty

**Medium.** Single-binary embedded mode is genuinely low-friction (`bd init` and go; Dolt runs in-process; data in `.beads/embeddeddolt/`). Difficulty rises because: embedded mode is single-writer (file lock), so any real multi-agent/multi-writer setup means standing up and operating an external Dolt SQL server with credentials; the Dolt database must be backed up and synced deliberately (no managed service); there is documented schema-migration churn (SQLite-era and v0.63→v1.0 upgrades needing repair steps); and the author warns agents have historically been destructive toward the DB, so backup/restore hygiene is on you.

## Caveats (unverified)

- **Stars** — repo page surfaced ~24.8k while a third-party article cited 18.7k; not reconciled. `[未验证]`
- **Release dates** — WebFetch returned 1.0.x releases dated to 2024, which conflicts with active development in 2026; the years are almost certainly misread. Treat specific release dates and the "bi-weekly cadence" claim as `[未验证]`.
- **Distribution** — whether Dolt is bundled in *every* installer (brew/npm/script) vs only the CGO-enabled prebuilt binary is inferred, not confirmed. `[未验证]`
- **"Alpha" label** — comes from the author's launch blog post; whether maintainers still consider 1.0.x alpha as of 2026-06 is unconfirmed. `[未验证]`
- **Performance / scale claims** — sub-100ms for thousands of issues and 100k+ guidance are the project's own FAQ claims, not independently benchmarked. `[未验证]`
- An independent third-party critique (starlog.is) could not be fetched (HTTP 403), so the tradeoffs above lean on the project's own README/FAQ/blog plus secondary summaries. `[未验证]`
