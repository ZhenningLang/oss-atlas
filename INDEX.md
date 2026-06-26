# oss-atlas — category route

> Level 1 of 3. The master map an agent reads first. Pick a category by its "use when",
> then open that category's `INDEX.md`, then a project page.
> 中文索引：[INDEX.zh.md](INDEX.zh.md) · Full reading procedure: [AGENTS.md](AGENTS.md)

## Categories

| Category | Use when | Route |
|---|---|---|
| **agent-tooling** | Infrastructure for AI coding agents — task/work tracking, persistent memory, agent state. | [→](categories/agent-tooling/INDEX.md) |
| **document-management** | Ingest, OCR, tag, and full-text-search scanned documents / paperwork. | [→](categories/document-management/INDEX.md) |
| **on-device-ml** | Run ML / LLM inference locally on edge devices (phone, laptop, IoT) instead of in the cloud. | [→](categories/on-device-ml/INDEX.md) |
| **web-automation** | Drive or automate a web UI — browser automation, or an in-page natural-language GUI agent. | [→](categories/web-automation/INDEX.md) |
| **llm-training** | Fine-tune or reinforcement-train LLMs and multi-step agents. | [→](categories/llm-training/INDEX.md) |
| **agent-frameworks** | Build and run multi-step or multi-agent systems — agent frameworks and agent operating systems. | [→](categories/agent-frameworks/INDEX.md) |

## How to add a category

A new category = a new directory under `categories/` with its own `INDEX.md` **and** `INDEX.zh.md`,
plus a row here and in [INDEX.zh.md](INDEX.zh.md). Only create one when a project genuinely doesn't
fit the existing categories. See [tools/schema.md](tools/schema.md) and the `add-project` skill.
