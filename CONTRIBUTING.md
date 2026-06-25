# Contributing to oss-atlas

This is a **curated, agent-first** selection index. Quality and honesty matter more than
coverage. Read [AGENTS.md](AGENTS.md) and [tools/schema.md](tools/schema.md) first.

## Inclusion criteria

Add a project **only if both** hold:

1. You actually evaluated it (not catalogued from a list).
2. A real selection question exists — there are substitutes worth comparing.

Keeping the index small is a feature. If a project has no credible alternative, or you haven't
looked at it, don't add it.

## Adding a project

The fastest path is the `add-project` skill (`.claude/skills/add-project/`). By hand:

1. Pick the **primary** category (one project = one page = one category; cross-cutting goes in
   `tags`). New category only if it genuinely doesn't fit — then add a row to `INDEX.md`.
2. Create `categories/<category>/<slug>.md` following [tools/schema.md](tools/schema.md):
   frontmatter (facts, dated) + the seven required sections.
3. Write the body in **English**; include a Simplified-Chinese `## 中文摘要`.
4. **Separate facts from judgment.** Label anything unverified `[未验证]` / `[推断]`. The most
   valuable section is `## When NOT to use` — be concrete and honest, not nice.
5. In `## Comparison`, name real substitutes. Mark ones not in the index `未收录`; link ones
   that are.
6. Add the project to its category `INDEX.md` (one-liner + comparison-matrix row).
7. Set `last_verified` to today.

## Updating / de-staling

Use the `sync-entry` skill (`.claude/skills/sync-entry/`): it re-verifies facts against the
live repo when an entry is older than the staleness threshold, and flags abandoned projects.

## Before you commit

```bash
python3 tools/lint.py
```

Fix every ERROR. WARNINGs (e.g. staleness) should be addressed or explained. CI runs the same
linter on every PR.

## Tone

Write for an agent that will *act* on what you say. No marketing. Date your facts. When you
don't know, say `[未验证]` — never guess in a way that reads as fact.
