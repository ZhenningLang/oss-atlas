# oss-atlas — category route

> Recursive route root. The master map an agent reads first. Pick a category by its "use when",
> then keep descending through each node's `INDEX.md` (the tree can be deep, not a fixed 3 levels)
> until you reach a project page.
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
| **agent-memory** | Persistent, LLM-agnostic memory an agent reads/writes across sessions. | [→](categories/agent-memory/INDEX.md) |
| **deep-research** | Iterative multi-source research agents that search, scrape, and synthesize. | [→](categories/deep-research/INDEX.md) |
| **ai-code-review** | LLM-assisted code review that produces line-level findings on a diff or repo. | [→](categories/ai-code-review/INDEX.md) |
| **rag-retrieval** | Document indexing, code-intelligence graphs, and graph DBs for retrieval-augmented generation. | [→](categories/rag-retrieval/INDEX.md) |
| **llm-eval** | Test, benchmark, and security-scan (red-team) prompts, agents, and RAG systems. | [→](categories/llm-eval/INDEX.md) |
| **agent-dev-methodology** | Frameworks and methodologies that shape *how* an agent builds software — spec-driven, context-engineering, persona/command systems. | [→](categories/agent-dev-methodology/INDEX.md) |
| **ai-design-generation** | Agent-driven generation of UI/design, slide decks, social cards, and HTML artifacts. | [→](categories/ai-design-generation/INDEX.md) |
| **dev-utilities** | Standalone devtools, data-wrangling swiss-army-knives, and self-hostable infrastructure. | [→](categories/dev-utilities/INDEX.md) |
| **frontend-animation** | JavaScript animation engines and motion libraries for the web. | [→](categories/frontend-animation/INDEX.md) |
| **api-gateway** | API / AI gateways that route, secure, rate-limit, and govern service and LLM traffic. | [→](categories/api-gateway/INDEX.md) |
| **geospatial** | Geographic information systems (GIS) — view, edit, and analyze spatial data. | [→](categories/geospatial/INDEX.md) |
| **team-chat** | Self-hostable team chat / multi-LLM chatbot applications. | [→](categories/team-chat/INDEX.md) |
| **captcha** | CAPTCHA / bot-detection challenges (proof-of-work, click, behavioral). | [→](categories/captcha/INDEX.md) |
| **ml-research** | Small, self-contained ML research demos and reference implementations. | [→](categories/ml-research/INDEX.md) |
| **agent-skill-collections** | Curated collections of agent skills, prompts, subagent personas, and harness configs — split by domain. | [→](categories/agent-skill-collections/INDEX.md) |

## How to add a category

A new category = a new directory under `categories/` with its own `INDEX.md` **and** `INDEX.zh.md`,
plus a row here and in [INDEX.zh.md](INDEX.zh.md). Only create one when a project genuinely doesn't
fit the existing categories. See [tools/schema.md](tools/schema.md) and the `add-project` skill.
