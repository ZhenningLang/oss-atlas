# oss-atlas

**A natural-language, agent-first index for open-source *selection* (选型).**
When a coding agent gets a task, it reads this index to pick the right OSS project —
weighing *when NOT to use* each option, not just what it does.

> 中文版 README：[README.zh.md](README.zh.md)

## Projects

The complete index. Each project has a clean English page (`<slug>.md`) and a Chinese page
(`<slug>.zh.md`). Click straight through:

| Category | Project | What it is | Don't reach for it when | License | Page |
|---|---|---|---|---|---|
| `agent-tooling` | **beads** | Dependency-aware, version-controlled task/issue graph giving AI agents persistent structured memory (Dolt-backed Go binary). | You need a human web UI, cross-repo views, or production-grade stability (it's alpha, single-writer embedded). | MIT | [EN](categories/agent-tooling/beads.md) · [中](categories/agent-tooling/beads.zh.md) |
| `document-management` | **paperless-ngx** | Self-hosted DMS: OCR + tag + full-text-search for scanned paperwork (Django/Angular + Postgres). | You need encryption at rest, strict multi-tenant permissions, or an enterprise approval / EDMS workflow. | GPL-3.0 | [EN](categories/document-management/paperless-ngx.md) · [中](categories/document-management/paperless-ngx.zh.md) |
| `on-device-ml` | **LiteRT-LM** | Google's on-device LLM runtime atop LiteRT — run Gemma/etc on phone/laptop/edge via CPU/GPU/NPU. | You need many non-Gemma models, cloud-grade latency, a frozen API, or tiny-RAM devices. | Apache-2.0 | [EN](categories/on-device-ml/litert-lm.md) · [中](categories/on-device-ml/litert-lm.zh.md) |
| `web-automation` | **page-agent** | In-page GUI agent: control a web UI with natural language via direct DOM read/write, no backend. | You need vision/multimodal, server-side automation, high concurrency, or can't send DOM to an external LLM. | MIT | [EN](categories/web-automation/page-agent.md) · [中](categories/web-automation/page-agent.zh.md) |

Browse by category from [INDEX.md](INDEX.md); agents should start at [AGENTS.md](AGENTS.md).

## Why this exists

Most OSS READMEs are marketing: they tell you what a project does and why it's great. They do
**not** tell you when *not* to use it, how it compares to alternatives, or what it costs to
operate. An agent doing selection needs exactly that negative space. oss-atlas inverts the
README genre into a **decision-support** genre.

The index is deliberately **weak** — no database, no search, no embeddings. Just Markdown that
an agent reads and reasons over. The directory structure *is* the query API.

## Structure (recursive tree, bilingual)

```
INDEX.md / INDEX.zh.md                        # root: category route (EN / 中)
categories/<cat>/INDEX.md / INDEX.zh.md       # a category node: pages + sub-categories
categories/<cat>/<subcat>/INDEX.md …          # deeper nodes — the tree self-balances as it grows
…/<slug>.md  +  …/<slug>.zh.md                # a leaf: the EN selection page + its 中文 sibling
```

`categories/` is a **recursive, self-balancing tree**: when a category gets too many projects it
splits into sub-categories (the linter WARNs; `refactor-index` does the split). Each project page =
YAML frontmatter (**facts**, dated) + Markdown body (**judgment**). Required sections depend on
`type`: all entries have `When to use / When NOT to use / Comparison` and close with a
`Caveats (unverified)` uncertainty ledger; software (non-`skill-pack`) entries also have
`Tech stack / Dependencies / Ops difficulty`. English is the agent-canonical path;
the `.zh.md` sibling is the same content in Chinese.

## Freshness

Facts go stale. Every page records `last_verified`. The linter warns when an entry is older
than 90 days; the `sync-entry` skill re-verifies it against the live repo. Treat any fact as a
**point-in-time** snapshot, labeled per the truth discipline (`[未验证]` / `[推断]`).

## Contributing

The unit of inclusion is a **git repository** — any real open-source repo, across any domain. Not
added: non-repos (hosted SaaS, landing pages, articles), exact duplicates, empty repos. See
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
