# agent-skill-collections

> Category node. Curated collections of agent skills, prompts, subagent personas, and harness configs — split by domain.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories (by domain)

| Leaf | What's inside | Route |
|---|---|---|
| **engineering** | Code quality, web performance, testing, and scientific/eng workflows. | [→](engineering/INDEX.md) |
| **design** | Design taste / UI-UX judgment — critique, anti-slop, visual generation. | [→](design/INDEX.md) |
| **writing** | Translation, humanizing AI text, editorial voice. | [→](writing/INDEX.md) |
| **security** | Security review, threat modeling, cybersecurity playbooks. | [→](security/INDEX.md) |
| **context-engineering** | Structuring, compressing, and routing what an agent reads. | [→](context-engineering/INDEX.md) |
| **vendor-collections** | Official / vendor-published first-party skill & plugin bundles. | [→](vendor-collections/INDEX.md) |
| **subagent-collections** | Ready-made subagent definitions / personas to drop into a harness. | [→](subagent-collections/INDEX.md) |
| **personal-collections** | The long tail: one author's curated skills, subagents, or harness config. | [→](personal-collections/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **book-to-skill** | Use it when you want to turn technical book PDFs (and other document formats) into installable agent skills for Claude Code, Copilot CLI, or Amp. | ? (0/6) | [→](book-to-skill.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [book-to-skill](book-to-skill.md) | ✅ | ? (0/6) | Converts technical books and documents into installable agent skills; batch tool, not a live RAG system. |
| [Docling](../document-parsing/docling.md) | ✅ | A (5/6) | General document parser for RAG pipelines; book-to-skill is specifically a skill-generator for agent harnesses. |
| [NotebookLM Claude Code Skill](context-engineering/notebooklm-skill.md) | ✅ | C (4/6) | Queries an external Google service; book-to-skill works on local PDFs with no external dependency. |
| LlamaIndex / RAG pipelines | 未收录 | — | Full RAG with embeddings and dynamic retrieval; more infrastructure than a static skill generator. |

## What belongs here

A deliberately crowded field — collections of agent **skills / prompts / subagent personas / harness
configs**, where no single one is "the" answer. Organized by domain (and, for the long tail, by source:
vendor vs personal) so an agent can pick a bundle by task and provenance. Self-balancing: a leaf that
outgrows the fanout splits further.
