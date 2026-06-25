# oss-atlas

**A natural-language, agent-first index for open-source *selection* (选型).**
When a coding agent gets a task, it reads this index to pick the right OSS project —
weighing *when NOT to use* each option, not just what it does.

> 一个面向 coding agent 的开源项目**选型**知识库。每个项目页是「反 README」：先讲正面场景、
> 反面场景、横向对比、技术栈、依赖、运维难度——帮 agent 在收到任务时快速选型。人也能看，但
> **主要读者是 agent**。

## Why this exists

Most OSS READMEs are marketing: they tell you what a project does and why it's great. They do
**not** tell you when *not* to use it, how it compares to alternatives, or what it costs to
operate. An agent doing selection needs exactly that negative space. oss-atlas inverts the
README genre into a **decision-support** genre.

The index is deliberately **weak** — no database, no search, no embeddings. Just Markdown that
an agent reads and reasons over. The directory structure *is* the query API.

## Structure (3 levels)

```
INDEX.md                          # level 1: category route
categories/<category>/INDEX.md    # level 2: projects in a category + comparison matrix
categories/<category>/<slug>.md   # level 3: one project's selection page
```

Each project page = YAML frontmatter (**facts**, dated) + Markdown body (**judgment**) with
seven required sections: `中文摘要 / When to use / When NOT to use / Comparison / Tech stack /
Dependencies / Ops difficulty`.

- **For agents**: start at [AGENTS.md](AGENTS.md) — it has the read route and the write contract.
- **For humans**: browse from [INDEX.md](INDEX.md).

## Freshness

Facts go stale. Every page records `last_verified`. The linter warns when an entry is older
than 90 days; the `sync-entry` skill re-verifies it against the live repo. Treat any fact as a
**point-in-time** snapshot, labeled per the project's truth discipline (`[未验证]` / `[推断]`).

## Contributing

Curated, not comprehensive. A project earns a page only if it was actually evaluated **and** a
real selection question exists (there are substitutes worth comparing). See
[CONTRIBUTING.md](CONTRIBUTING.md) and [tools/schema.md](tools/schema.md).

```bash
python3 tools/lint.py    # the only gate; no unit tests (it's a content repo)
```

## License

- **Tooling** (code, e.g. `tools/lint.py`): MIT — see [LICENSE](LICENSE).
- **Content** (prose under `categories/`, routing pages, docs): CC BY 4.0 — see
  [LICENSE-CONTENT](LICENSE-CONTENT).

Profiles describe third-party projects owned by their respective authors and governed by their
own licenses; the CC BY 4.0 grant covers only the original analysis here.
