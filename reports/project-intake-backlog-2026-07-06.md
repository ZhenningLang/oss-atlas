# Project Intake Backlog — 2026-07-06

This is a maintainer backlog for expanding `oss-atlas`. It is not a canonical selection page and does not claim the candidates are fully verified.

## Source Summary

| Source | Result | Notes |
|---|---:|---|
| Existing canonical English pages with `未收录` comparison rows | 878 rows / 754 unique alternatives | Full raw export: [`unindexed-project-mentions-2026-07-06.csv`](unindexed-project-mentions-2026-07-06.csv). English pages were used to avoid EN/ZH duplication. |
| Candidate collection pass: AI / agent / LLM categories | 35 candidates | Read-only collection; each candidate still needs `add-project` live verification before writing pages. |
| Candidate collection pass: general engineering categories | 40 candidates | Read-only collection; each candidate still needs `add-project` live verification before writing pages. |

## Intake Rules

- Use `add-project` for each checked item before creating canonical pages.
- Verify that the unit is a real, non-empty open-source git repository.
- Reject hosted SaaS, articles, docs-only pages, closed-source products, and generic patterns.
- If a row names multiple alternatives, split it into one repo per task before intake.
- Re-check duplicates against current `categories/**/<slug>.md` immediately before adding.
- Treat all repo URLs below as candidates until verified live during intake.

## P0 — Repeated Existing Mentions

These appear repeatedly in current comparison tables, so adding them should immediately improve existing horizontal comparisons.

| Todo | Candidate | Suggested category | Type | Evidence in current pages | Intake note |
|---|---|---|---|---|---|
| [ ] | Text Generation Inference (TGI) | `llm-inference` | service | 6 mentions | Verify archived/maintenance status first; if still archived, page should lead with the maintenance caveat. |
| [ ] | CrewAI | `agent-frameworks/agent-runtimes` | framework | 5 mentions | Role/crew-based multi-agent runtime; compare against AgentScope, AutoGen, LangGraph. |
| [ ] | SvelteKit | `web-ui` | framework | 5 mentions | Split from generic Svelte; compare against Next.js, Nuxt, Astro. |
| [ ] | trafilatura | `web-scraping` | library | 5 mentions | Modern article extraction; compare against newspaper, readability, boilerpipe. |
| [ ] | gallery-dl | `media-download` | tool | 4 mentions | Multi-site media downloader; compare against yt-dlp, you-get, lux. |
| [ ] | Hugging Face TRL | `llm-training` | library | 4 mentions | Foundational SFT/DPO/PPO/GRPO training library; many higher-level tools compare to it. |
| [ ] | LangGraph | `agent-frameworks/agent-runtimes` | framework | 4 mentions | Graph/state-machine orchestration; likely a core missing page. |
| [ ] | Pandoc | `markdown-tools` | tool | 4 mentions | Universal document converter; bridges Markdown, DOCX, LaTeX, HTML, PDF. |
| [ ] | Argo Workflows | `workflow-orchestration` | service | 3 mentions | Kubernetes-native workflow engine; compare against Airflow, Dagster, Prefect. |
| [ ] | browser-use | `web-automation` | framework | 3 mentions | Python browser agent loop; compare against Playwright, Agent Browser, page-agent. |
| [ ] | Goldmark | `markdown-tools` | library | 3 mentions | Go Markdown parser; compare against commonmark, micromark, markdown-it. |
| [ ] | GPT Researcher | `deep-research` | app | 3 mentions | Deep research agent; compare against current `deep-research` and Local Deep Research. |
| [ ] | Letta (MemGPT) | `agent-memory` | service | 3 mentions | Stateful memory/runtime; compare against Mem0, Zep, LangMem. |
| [ ] | LibreChat | `llm-chat-ui` | app | 3 mentions | Full multi-user chat platform; compare against NextChat and Lobe Chat. |
| [ ] | LlamaIndex | `agent-frameworks/workflow-builders` or `rag-retrieval` | framework | 3 mentions | Decide primary category before intake: agent workflow/data framework vs RAG retrieval. |
| [ ] | Marker | `document-parsing` | tool | 3 mentions | PDF-to-Markdown/document parsing; compare against Docling, MarkItDown, olmOCR. |
| [ ] | mitmproxy | `debugging-proxy` | tool | 3 mentions | Python-scriptable HTTP(S) proxy; compare against AnyProxy, Charles-like GUI tools. |
| [ ] | Playwright | `web-automation` | library | 3 mentions | Modern deterministic browser automation; likely a foundational missing page. |
| [ ] | Reactour | `web-ui` | library | 3 mentions | React product-tour component; split from `react-joyride` unless one page intentionally compares both. |
| [ ] | react-joyride | `web-ui` | library | 3 mentions | React product-tour component; compare against Intro.js, Driver.js, Shepherd.js. |
| [ ] | Sourcegraph | `rag-retrieval` or `dev-utilities` | app | 3 mentions | Code intelligence/search platform; verify open-core boundaries before adding. |
| [ ] | SCIP | `rag-retrieval` or `dev-utilities` | tool | 3 mentions | Code intelligence index format/tooling; likely separate from Sourcegraph app. |
| [ ] | torchtune | `llm-training` | library | 3 mentions | PyTorch-native fine-tuning recipes; compare against TRL, Axolotl, LlamaFactory. |

## P1 — High-Value Existing Mentions

These are lower-frequency but clean enough to become direct intake tasks after live verification.

| Todo | Candidate | Suggested category | Type | Current evidence | Intake note |
|---|---|---|---|---|---|
| [ ] | Prefect | `workflow-orchestration` | framework | 2 mentions | Pythonic dynamic flows; compare against Airflow and Dagster. |
| [ ] | Dagster | `workflow-orchestration` | framework | 1+ mentions | Asset-oriented data orchestration; high selection value even if fewer mentions. |
| [ ] | Temporal | `workflow-orchestration` | service | 1+ mentions | Durable execution, not batch DAG scheduling; must explain category boundary. |
| [ ] | Material UI (MUI) | `web-ui` | library | 2 mentions | React Material component library; compare against Ant Design, Chakra, shadcn/ui. |
| [ ] | Chakra UI | `web-ui` | library | 2 mentions | React component library; verify current project health and maintainer direction. |
| [ ] | Radix UI Primitives | `web-ui` | library | 2 mentions | Headless primitives; compare against Headless UI and shadcn/ui. |
| [ ] | Nuxt | `web-ui` | framework | 2 mentions | Vue meta-framework; compare against Vue, Next.js, SvelteKit. |
| [ ] | Astro | `web-ui` | framework | 1 mention | Content-focused islands framework; strong contrast to Next.js. |
| [ ] | Puppeteer | `web-automation` | library | 2 mentions | Chrome/CDP automation; compare against Playwright and Chrome DevTools MCP. |
| [ ] | PyMuPDF | `pdf-tools` | library | 2 mentions | Python PDF extraction/manipulation; compare against pdfplumber and pdf.js. |
| [ ] | pdfplumber | `pdf-tools` | library | 1+ mentions | PDF text/table extraction; compare against PyMuPDF and Docling. |
| [ ] | unstructured | `document-parsing` | library | 2 mentions | Document ingestion/parsing pipeline; verify OSS/commercial boundary. |
| [ ] | OCRmyPDF | `pdf-tools` | tool | 1+ mentions | Adds OCR layer to scanned PDFs; compare against Tesseract and document parsers. |
| [ ] | Milvus | `rag-retrieval` | service | 2 mentions | Distributed vector DB; compare against FAISS and graph/vector DBs. |
| [ ] | Zep | `agent-memory` | service | 2 mentions | Temporal/graph memory; compare against Mem0 and Letta. |
| [ ] | Graphiti | `agent-memory` | library | 2 mentions | Knowledge-graph memory library; could be separate or paired with Zep after verification. |
| [ ] | LangMem | `agent-memory` | library | 2 mentions | LangChain/LangGraph memory utilities; category fit is clear. |
| [ ] | Langfuse | `llm-eval` | app | 2 mentions | LLM observability/eval/prompt management; compare against Pezzo and promptfoo. |
| [ ] | DeepEval | `llm-eval` | library | Existing INDEX mention | Python/pytest-style LLM eval; compare against promptfoo and Ragas. |
| [ ] | Ragas | `llm-eval` | library | Existing INDEX mention | RAG eval metrics; narrower than general prompt/agent eval. |
| [ ] | garak | `llm-eval` | tool | Existing mention | LLM vulnerability scanner; emphasize security vs quality eval. |
| [ ] | Giskard OSS | `llm-eval` | library | Existing mention | ML/LLM testing; verify repo/license naming before intake. |
| [ ] | Axolotl | `llm-training` | tool | Existing mentions | YAML-driven fine-tuning; compare against LlamaFactory, Unsloth, torchtune. |
| [ ] | verl | `llm-training` | framework | 2 mentions | Distributed RL post-training; compare against ART and Agent Lightning. |
| [ ] | llama.cpp | `llm-inference` or `on-device-ml` | library | Existing mentions | Decide primary category: local inference engine vs on-device ML. |
| [ ] | Ollama | `llm-inference` or `on-device-ml` | app | 2 mentions | Local model runner; compare against LM Studio, llama.cpp, vLLM. |
| [ ] | LM Studio | `llm-inference` or `on-device-ml` | app | 2 mentions | Verify open-source status before adding; may be non-eligible if not a repo. |
| [ ] | MLX / mlx-lm | `on-device-ml` | library | 2 mentions | Apple-silicon local inference/training; split MLX framework from mlx-lm if needed. |

## P1 — Collected New Candidates

These came from the collection pass, not necessarily from repeated current mentions.

| Todo | Candidate | Repo URL | Suggested category | Type | Why add | Main caveat to verify |
|---|---|---|---|---|---|---|
| [ ] | AutoGen | `https://github.com/microsoft/autogen` | `agent-frameworks/agent-runtimes` | framework | Mature Microsoft multi-agent framework and common comparison point. | Conversation-driven abstraction may be heavy for simple tool loops. |
| [ ] | Pydantic AI | `https://github.com/pydantic/pydantic-ai` | `agent-frameworks/agent-runtimes` | framework | Type/schema-centered agent framework; fills structured-output agent gap. | Python/Pydantic ecosystem binding. |
| [ ] | OpenAI Agents SDK | `https://github.com/openai/openai-agents-python` | `agent-frameworks/agent-runtimes` | library | Official OpenAI agent workflow SDK. | Vendor neutrality and API churn need live verification. |
| [ ] | Flowise | `https://github.com/FlowiseAI/Flowise` | `agent-frameworks/workflow-builders` | app | Visual LLM workflow builder; complements Langflow/Dify. | Visual flows are harder to diff/review than code. |
| [ ] | aider | `https://github.com/Aider-AI/aider` | `agent-frameworks/coding-agents` | tool | Mature terminal pair-programming coding agent. | Not an autonomous issue-runner/control plane. |
| [ ] | Cline | `https://github.com/cline/cline` | `agent-frameworks/coding-agents` | tool | Important VS Code coding-agent lineage for Kilo/Roo comparisons. | Editor lock-in and extension lifecycle. |
| [ ] | OpenHands | `https://github.com/OpenHands/OpenHands` | `agent-frameworks/coding-agents` | app | Autonomous software engineering platform. | Heavier platform/sandbox/permission surface. |
| [ ] | SWE-agent | `https://github.com/SWE-agent/SWE-agent` | `agent-frameworks/coding-agents` | tool | GitHub issue / SWE-bench style autonomous repair agent. | Needs strict sandboxing and review gates. |
| [ ] | Cognee | `https://github.com/topoteretes/cognee` | `agent-memory` | service | Self-hosted knowledge-graph memory candidate. | Graph memory value and ops cost need sample-based verification. |
| [ ] | Open Deep Research | `https://github.com/langchain-ai/open_deep_research` | `deep-research` | app | LangChain/LangGraph deep research implementation. | Ecosystem binding. |
| [ ] | STORM | `https://github.com/stanford-oval/storm` | `deep-research` | app | Long-form cited report generation workflow. | More report-generation than lightweight Q&A. |
| [ ] | node-DeepResearch | `https://github.com/jina-ai/node-DeepResearch` | `deep-research` | tool | Node/Jina deep research agent route. | Token/search budget and result quality need verification. |
| [ ] | PR-Agent | `https://github.com/The-PR-Agent/pr-agent` | `ai-code-review` | app | Open-source PR reviewer bot; important code-review category gap. | Permission/noise governance for PR comments. |
| [ ] | Metis | `https://github.com/arm/metis` | `ai-code-review` | tool | AI-assisted security code review candidate. | Security findings require human confirmation; scope may be narrow. |
| [ ] | OpenReview | `https://github.com/vercel-labs/openreview` | `ai-code-review` | app | Self-hosted AI code review bot candidate. | License and maintenance must be verified first. |
| [ ] | BentoML | `https://github.com/bentoml/BentoML` | `llm-inference` | service | General AI/model serving framework. | Not optimized only for single-model LLM token throughput. |
| [ ] | LMDeploy | `https://github.com/InternLM/lmdeploy` | `llm-inference` | tool | LLM deployment/compression/serving toolchain. | Model compatibility and ecosystem fit need verification. |
| [ ] | qpdf | `https://github.com/qpdf/qpdf` | `pdf-tools` | tool | PDF structure repair, encryption, split/merge, linearization. | Low-level PDF operations, not content understanding. |
| [ ] | markdownlint | `https://github.com/DavidAnson/markdownlint` | `markdown-tools` | library | Markdown style linting quality gate. | Rule preferences can conflict with prose style. |
| [ ] | ImageMagick | `https://github.com/ImageMagick/ImageMagick` | `media-processing` | tool | Image conversion/composition batch processing. | Untrusted image parsing needs sandbox/security caveats. |
| [ ] | sharp | `https://github.com/lovell/sharp` | `media-processing` | library | High-performance Node image processing via libvips. | Native dependency/deployment compatibility. |
| [ ] | DuckDB | `https://github.com/duckdb/duckdb` | `databases` | service | Embedded OLAP database for local analytics. | Not a high-concurrency OLTP primary database. |
| [ ] | ClickHouse | `https://github.com/ClickHouse/ClickHouse` | `databases` | service | Columnar OLAP database for logs/events/analytics. | Operational/modeling cost for clusters and MergeTree. |
| [ ] | DBeaver | `https://github.com/dbeaver/dbeaver` | `databases` | app | Universal database GUI client. | Credential exposure and GUI operational boundaries. |
| [ ] | Debezium | `https://github.com/debezium/debezium` | `databases` | service | CDC/binlog platform candidate. | Kafka Connect and connector ops complexity. |
| [ ] | Valkey | `https://github.com/valkey-io/valkey` | `databases` | service | Redis-compatible open governance fork. | Cloud/provider Redis feature compatibility. |
| [ ] | jq | `https://github.com/jqlang/jq` | `dev-utilities/data-tools` | tool | JSON CLI processing standard. | DSL readability for complex transforms. |
| [ ] | fzf | `https://github.com/junegunn/fzf` | `dev-utilities/data-tools` | tool | Interactive fuzzy finder used across shell/editor workflows. | Not for non-interactive batch processing. |
| [ ] | Keycloak | `https://github.com/keycloak/keycloak` | `auth` | service | Self-hosted IAM/SSO/OIDC/SAML anchor project. | Heavy ops and security responsibility. |
| [ ] | Casbin | `https://github.com/casbin/casbin` | `auth` | library | Policy-based authorization library. | Not identity/authentication; policy modeling risk. |
| [ ] | OpenFGA | `https://github.com/openfga/openfga` | `auth` | service | Zanzibar-style fine-grained authorization. | Complex relation modeling and consistency semantics. |
| [ ] | Prometheus | `https://github.com/prometheus/prometheus` | `observability` | service | Metrics/PromQL/alerting ecosystem anchor. | High-cardinality and long-term storage governance. |
| [ ] | OpenTelemetry Collector | `https://github.com/open-telemetry/opentelemetry-collector` | `observability` | service | Vendor-neutral metrics/logs/traces pipeline. | More complex than simple host metric agents. |
| [ ] | Loki | `https://github.com/grafana/loki` | `observability` | service | Grafana ecosystem log backend. | Label design and non-full-text search tradeoff. |
| [ ] | Jaeger | `https://github.com/jaegertracing/jaeger` | `observability` | service | Distributed tracing backend. | Requires app instrumentation and sampling decisions. |
| [ ] | Metabase | `https://github.com/metabase/metabase` | `data-visualization` | app | Easy self-hosted BI/dashboard app. | Enterprise governance/deep semantic layer limitations. |
| [ ] | Evidence | `https://github.com/evidence-dev/evidence` | `data-visualization` | framework | Markdown/SQL data apps and reports. | Developer-oriented, not no-code BI. |
| [ ] | Rich | `https://github.com/Textualize/rich` | `terminal-ui` | library | Python CLI rich text/tables/progress. | Not a full TUI application framework. |
| [ ] | Textual | `https://github.com/Textualize/textual` | `terminal-ui` | framework | Python full-screen TUI apps. | Heavier than simple CLI output formatting. |
| [ ] | FreshRSS | `https://github.com/FreshRSS/FreshRSS` | `reading-tools` | app | Self-hosted RSS server/web reader. | Requires server ops and backup/sync decisions. |

## P2 — Split Or Reject Before Intake

These appeared in `未收录` rows but are mixed, generic, non-repo, or likely need a stronger inclusion decision.

| Candidate text | Action |
|---|---|
| `Ollama / llama.cpp` | Split into `Ollama` and `llama.cpp`; choose primary categories independently. |
| `PyMuPDF / pdfplumber` | Split into separate pages. |
| `Playwright / Puppeteer` | Split into separate pages. |
| `Reactour / react-joyride` | Split unless one repo is clearly dominant for intake priority. |
| `Zep / Graphiti` | Split into service vs library, or explicitly decide a paired ecosystem page. |
| `BentoML / OpenLLM` | Split; verify OpenLLM maintenance/status before adding. |
| `MLX / mlx-lm` | Split framework vs model-serving package if both are eligible repos. |
| `Appcues / Userflow / Userpilot` | Reject for `oss-atlas` unless an actual open-source repo is identified; these are commercial onboarding platforms. |
| `Feedly / Inoreader`, `Reeder`, `Claude / ChatGPT native apps`, `GitHub Copilot`, `IntelliJ IDEA`, `Sublime Text`, `ArcGIS Pro` | Likely reject as closed-source/proprietary/non-OSS for this index. |
| `Anthropic "Building effective agents" guide`, `Heroku 12-Factor App` | Reject as methodology/article/non-repo unless a repo-backed project is identified. |
| Generic patterns like `Application framework upload handlers`, `Direct-to-S3 presigned uploads`, `ad-hoc if checks`, `write your own SKILL.md` | Keep only as comparison text, not project intake items. |

## Suggested Intake Batches

| Batch | Focus | Items |
|---|---|---|
| Batch 1 | Foundational agent/runtime gaps | LangGraph, AutoGen, CrewAI, Pydantic AI, OpenAI Agents SDK, aider, Cline, OpenHands, SWE-agent |
| Batch 2 | Memory/eval/deep-research | Letta, Zep, Graphiti, LangMem, Cognee, DeepEval, Ragas, garak, Langfuse, GPT Researcher, Open Deep Research |
| Batch 3 | LLM training/inference | HF TRL, torchtune, Axolotl, verl, TGI, llama.cpp, Ollama, BentoML, LMDeploy |
| Batch 4 | Web UI/automation/workflows | Playwright, Puppeteer, browser-use, SvelteKit, Nuxt, Astro, MUI, Radix UI, Prefect, Dagster, Argo Workflows, Temporal |
| Batch 5 | Documents/Markdown/PDF/media | Pandoc, Goldmark, Marker, unstructured, PyMuPDF, pdfplumber, OCRmyPDF, qpdf, ImageMagick, sharp |
| Batch 6 | Core infra/devtools | DuckDB, ClickHouse, Debezium, Valkey, Keycloak, Casbin, OpenFGA, Prometheus, OpenTelemetry Collector, Loki, Jaeger |

## Verification Runbook For Each Item

- Run `add-project` for exactly one repo at a time.
- Fetch GitHub metadata, README, license, release/commit activity, dependency manifests, governance files, and package metadata when applicable.
- Write bilingual pages plus health radar and upstream snapshot.
- Update category `INDEX.md` / `INDEX.zh.md` and README listings.
- Run `python3 tools/lint.py`.
- Run `python3 tools/quality_scan.py --scope <en-page> --scope <zh-page> --fail-on-any-scoped`.

## Remaining Risks

- The CSV includes every `未收录` comparison row, including non-repos and closed products; do not bulk-convert it into pages.
- Some candidates have ambiguous primary categories, especially `LlamaIndex`, `llama.cpp`, `Ollama`, `MLX`, `Sourcegraph`, and `SCIP`.
- Collection-pass repo URLs were gathered in a read-only pass, but this report intentionally defers final fact verification to `add-project`.
