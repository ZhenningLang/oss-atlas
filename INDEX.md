# oss-atlas — category route

> Level 1 of 3. This is the master map an agent reads first. Pick a category by its
> "use when", then open that category's `INDEX.md`, then a project page.
> 一级路由：先按「何时进这个分类」选分类，再进分类的 `INDEX.md`，最后看项目页。

For the full reading procedure see [AGENTS.md](AGENTS.md).

## Categories

| Category | Use when (你在选什么) | Route |
|---|---|---|
| **agent-tooling** | You need infrastructure for AI coding agents — task/work tracking, persistent memory, agent state. 为 AI agent 选「任务/记忆/状态」基建。 | [→](categories/agent-tooling/INDEX.md) |
| **document-management** | You need to ingest, OCR, tag, and search scanned documents / paperwork. 选「文档归档/OCR/全文检索」系统。 | [→](categories/document-management/INDEX.md) |
| **on-device-ml** | You need to run ML / LLM inference locally on edge devices (phone, laptop, IoT) instead of in the cloud. 选「端侧/边缘跑模型」的运行时。 | [→](categories/on-device-ml/INDEX.md) |

## How to add a category

A new category = a new directory under `categories/` with its own `INDEX.md`, plus a row here.
Only create one when a project genuinely doesn't fit the existing categories. See
[tools/schema.md](tools/schema.md) and the `add-project` skill.
