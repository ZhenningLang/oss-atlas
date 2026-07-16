# Classification Task — Agent Semantic Review

> This report is for a coding agent (LLM) to perform semantic classification.
> Read each category definition, compare it to the candidate repos, and assign
> the most appropriate category by semantic fit. Do not rely on keyword matching.

## Candidate Repositories

| # | Repo | Stars | Lang | Description | Topics |
|---|------|-------|------|-------------|--------|
| 1 | public-apis/public-apis | 450,656 | Python | A collective list of free APIs | api, apis, dataset, development, free, list, lists, open-source, public, public- |
| 2 | EbookFoundation/free-programming-books | 392,242 | Python | :books: Freely available programming books | books, education, hacktoberfest, list, resource |
| 3 | donnemartin/system-design-primer | 357,818 | Python | Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards. | design, design-patterns, design-system, development, interview, interview-practi |
| 4 | vinta/awesome-python | 308,491 | Python | An opinionated list of Python frameworks, libraries, tools, and resources | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 5 | practical-tutorials/project-based-learning | 273,640 | Python | Curated list of project-based tutorials | beginner-project, cpp, golang, javascript, project, python, tutorial, webdevelop |
| 6 | TheAlgorithms/Python | 222,764 | Python | All Algorithms implemented in Python | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driv |
| 7 | huggingface/transformers | 162,657 | Python | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and  | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning |

## Available Categories

> Read the full `categories/{cat}/INDEX.md` for deeper context if needed.

### agent-dev-methodology
- **Definition:** Opinionated **methodologies and meta-frameworks** for agent-driven development — how to structure specs, context, skills, and workflow. Not runtime agent frameworks (see `agent-frameworks`), not raw s
- **Examples:** 12-Factor Agents, 12-Factor Agents, Compound Engineering
- **File:** `categories/agent-dev-methodology/INDEX.md`

### agent-frameworks
- **Definition:** Navigate by the kind of agent system you need: coding-agent tools, reusable agent runtimes, or workflow-building platforms.
- **Examples:** AgentScope, AgentScope, AutoGen
- **File:** `categories/agent-frameworks/INDEX.md`

### agent-governance
- **Definition:** Governance, policy enforcement, identity, sandboxing, reliability controls, and install-time security gates for AI agents.
- **Examples:** agent-governance-toolkit, agent-governance-toolkit, SkillSpector
- **File:** `categories/agent-governance/INDEX.md`

### agent-memory
- **Definition:** Infrastructure whose primary job is to **store and recall** agent memory across sessions, independent of the model. Not task/issue tracking (see `agent-tooling`), not RAG document retrieval (see `rag-
- **Examples:** ByteRover CLI, ByteRover CLI, claude-mem
- **File:** `categories/agent-memory/INDEX.md`

### agent-runtimes
- **Definition:** Reusable frameworks and runtimes for autonomous agents, multi-agent execution, or on-rails agent behavior.
- **Examples:** AgentScope, AgentScope, AutoGen
- **File:** `categories/agent-runtimes/INDEX.md`

### agent-skills
- **Definition:** A deliberately crowded field — agent **skills / prompts / subagent personas / harness configs**, where no
single one is "the" answer. Organize primary leaves by task when the job is clear (slides, vis
- **Examples:** book-to-skill, book-to-skill, cangjie-skill
- **File:** `categories/agent-skills/INDEX.md`

### agent-tooling
- **Definition:** Infrastructure an AI **coding agent** uses to track work and carry state — task/issue graphs, session capture, planning / context plumbing. Not LLM-agnostic memory libraries (see `agent-memory`), not 
- **Examples:** Agent Orchestrator, Agent Orchestrator, AgentsView
- **File:** `categories/agent-tooling/INDEX.md`

### ai-code-review
- **Definition:** Tools whose primary job is **LLM-assisted code / security review** producing line-level findings. Not general agent frameworks, not non-LLM linters.
- **Examples:** Claude Code Security Review, Claude Code Security Review, Metis
- **File:** `categories/ai-code-review/INDEX.md`

### ai-design-generation
- **Definition:** Tools and applications whose job is to **generate visual / design artifacts** — UI, HTML, images, decks, or cards — with an agent. Portable skill packs whose primary value is being installed into an a
- **Examples:** HTML Anything, HTML Anything, Impeccable
- **File:** `categories/ai-design-generation/INDEX.md`

### api-gateway
- **Definition:** **API / AI gateways** that sit in front of services or LLMs to route, secure, rate-limit, and observe traffic. Not agent frameworks (see `agent-frameworks`).
- **Examples:** Kong Gateway, Kong Gateway
- **File:** `categories/api-gateway/INDEX.md`

### article-extraction
- **Definition:** Article readability extraction, boilerplate removal, and content parsing.
- **Examples:** boilerpipe, boilerpipe, dragnet
- **File:** `categories/article-extraction/INDEX.md`

### auth
- **Definition:** Libraries whose primary job is **authentication or authorization** — login/OAuth providers, permission/rule engines.
- **Examples:** Authomatic, Authomatic, Casbin
- **File:** `categories/auth/INDEX.md`

### captcha
- **Definition:** **CAPTCHA / bot-detection** challenge systems — proof-of-work, click, or behavioral. A standalone domain in this broad index.
- **Examples:** Cap, Cap, captcha (lepture)
- **File:** `categories/captcha/INDEX.md`

### coding-agents
- **Definition:** Terminal, IDE, and assistant-facing coding agents plus control planes for switching or reviewing them.
- **Examples:** Cline, Cline, Kilo Code
- **File:** `categories/coding-agents/INDEX.md`

### component-libraries
- **Definition:** UI component libraries, primitives, and design-system building blocks.
- **Examples:** Ant Design, Ant Design, Chakra UI
- **File:** `categories/component-libraries/INDEX.md`

### context-engineering
- **Definition:** Skill collections focused on **context engineering** — structuring, compressing, and routing what an agent reads.
- **Examples:** cangjie-skill, cangjie-skill, Agent Skills for Context Engineering
- **File:** `categories/context-engineering/INDEX.md`

### crawling-tools
- **Definition:** Web crawling, scraping orchestration, site/API wrappers, and crawler deployment tools.
- **Examples:** Firecrawl, Firecrawl, fuck-login
- **File:** `categories/crawling-tools/INDEX.md`

### data-sync
- **Definition:** CDC, replication, and database-to-database sync tools.
- **Examples:** Debezium, Debezium, go-mysql-elasticsearch
- **File:** `categories/data-sync/INDEX.md`

### data-tools
- **Definition:** Offline data transforms, compression, test data, font tooling, progress indicators, and fast search utilities.
- **Examples:** CyberChef, CyberChef, DevToys
- **File:** `categories/data-tools/INDEX.md`

### data-visualization
- **Definition:** Tools whose primary job is **BI dashboards and data exploration over SQL warehouses** for analysts. Not infra metrics/observability (see `observability`), not document/graph retrieval (see `rag-retrie
- **Examples:** Evidence, Evidence, Metabase
- **File:** `categories/data-visualization/INDEX.md`

### database-clients
- **Definition:** Database clients, GUIs, query layers, and inspection tools.
- **Examples:** DBeaver, DBeaver, elasticsearch-dsl-py
- **File:** `categories/database-clients/INDEX.md`

### database-engines
- **Definition:** Database engines and self-hosted database services.
- **Examples:** ClickHouse, ClickHouse, DuckDB
- **File:** `categories/database-engines/INDEX.md`

### databases
- **Definition:** Databases and database tooling — clients, GUIs, sync, and Redis/ES-compatible stores.
- **Examples:** Debezium, Debezium, go-mysql-elasticsearch
- **File:** `categories/databases/INDEX.md`

### de-ai-writing
- **Definition:** Agent skills, prompt repos, or writing helpers whose primary job is to **remove AI writing tells**, humanize prose, preserve facts while changing voice, or enforce human-sounding editorial style.
- **Examples:** ai-flavor-remover, ai-flavor-remover, De-AI-Prompt-Enhancer-Writer-Booster-SKILL
- **File:** `categories/de-ai-writing/INDEX.md`

### debugging-proxy
- **Definition:** Proxies whose primary job is **capturing, inspecting, rewriting, and mocking** HTTP(S)/WebSocket traffic for development and debugging. Not production API/AI gateways (see `api-gateway`), not scraping
- **Examples:** AnyProxy, AnyProxy, mitmproxy
- **File:** `categories/debugging-proxy/INDEX.md`

### deep-research
- **Definition:** Agents whose primary job is **iterative web / multi-source research** — search, fetch, synthesize. Not single-shot RAG indexes (see `rag-retrieval`), not general agent frameworks (see `agent-framework
- **Examples:** Agent-Reach, Agent-Reach, deep-research
- **File:** `categories/deep-research/INDEX.md`

### design
- **Definition:** Skill collections that give an agent **design taste / UI-UX judgment** — critique, anti-slop, visual generation prompts.
- **Examples:** ai-website-cloner-template, ai-website-cloner-template, archify
- **File:** `categories/design/INDEX.md`

### desktop-automation
- **Definition:** Tools that **drive the desktop GUI** (mouse/keyboard/screen). Not web-page automation (see `web-automation`).
- **Examples:** PyAutoGUI, PyAutoGUI
- **File:** `categories/desktop-automation/INDEX.md`

### dev-utilities
- **Definition:** Navigate by utility class: data manipulation, operations infrastructure, or editors/runtimes.
- **Examples:** CyberChef, CyberChef, DevToys
- **File:** `categories/dev-utilities/INDEX.md`

### diagramming
- **Definition:** Libraries/tools whose primary job is **turning text into diagrams** (diagrams-as-code) or rendering them. Not freeform whiteboard apps as the main use case, not UI animation (see `frontend-animation`)
- **Examples:** bpmn-js, bpmn-js, Excalidraw
- **File:** `categories/diagramming/INDEX.md`

### document-management
- **Definition:** Self-hosted systems to **store, OCR, organize, and search documents** — DMS, file servers, paperless workflows. Not RAG indexes for LLMs (see `rag-retrieval`).
- **Examples:** copyparty, copyparty, Immich
- **File:** `categories/document-management/INDEX.md`

### document-parsing
- **Definition:** Libraries whose primary job is **parsing/converting documents into structured representations** for gen-AI/RAG. Not retrieval/indexing itself (see `rag-retrieval`), not document archiving/search (see 
- **Examples:** any2html, any2html, Docling
- **File:** `categories/document-parsing/INDEX.md`

### editors-and-runtimes
- **Definition:** Code editors, IDE extensions, app runtimes, and JavaScript/TypeScript toolchains.
- **Examples:** Bun, Bun, Deno
- **File:** `categories/editors-and-runtimes/INDEX.md`

### education-tutoring
- **Definition:** AI tutoring, learning assistants, and education-focused agent systems.
- **Examples:** DeepTutor, DeepTutor
- **File:** `categories/education-tutoring/INDEX.md`

### engineering
- **Definition:** Skill/prompt collections that make a coding agent better at **engineering tasks** — code review, performance, testing, scientific workflows.
- **Examples:** Agent Skills (addyosmani), Agent Skills (addyosmani), web-quality-skills
- **File:** `categories/engineering/INDEX.md`

### engineering-workflows
- **Definition:** Personal collections whose primary value is improving a coding agent's engineering workflow, review loop, architecture judgment, harness behavior, or coding persona.
- **Examples:** antfu/skills, antfu/skills, claude-code-harness
- **File:** `categories/engineering-workflows/INDEX.md`

### frameworks
- **Definition:** Front-end frameworks and meta-frameworks for building web applications.
- **Examples:** Angular, Angular, Astro
- **File:** `categories/frameworks/INDEX.md`

### frontend-animation
- **Definition:** Libraries that **animate web UI** — JS motion engines, timeline/tween systems. Not agent-driven design generation (see `ai-design-generation`).
- **Examples:** Anime.js, Anime.js
- **File:** `categories/frontend-animation/INDEX.md`

### game-dev
- **Definition:** Libraries/engines for **building games**.
- **Examples:** pygame, pygame
- **File:** `categories/game-dev/INDEX.md`

### geospatial
- **Definition:** **Geospatial / GIS** tools to view, edit, and analyze spatial data. A standalone domain in this broad index.
- **Examples:** QGIS, QGIS
- **File:** `categories/geospatial/INDEX.md`

### ide-agents
- **Definition:** IDE-integrated coding agents and editor extensions.
- **Examples:** Cline, Cline, Kilo Code
- **File:** `categories/ide-agents/INDEX.md`

### im-automation
- **Definition:** Bots and automation for **instant-messaging platforms** (WeChat and other IM). Not web/browser automation (see `web-automation`), not team-chat apps (see `team-chat`).
- **Examples:** Douyin-Bot, Douyin-Bot, ItChat
- **File:** `categories/im-automation/INDEX.md`

### image-processing
- **Definition:** Image processing, conversion, resizing, and format tooling.
- **Examples:** ImageMagick, ImageMagick, sharp
- **File:** `categories/image-processing/INDEX.md`

### investment-finance
- **Definition:** Quant finance, market-data, trading research, and investment-analysis tooling.
- **Examples:** awesome-deep-trading, awesome-deep-trading, backtrader
- **File:** `categories/investment-finance/INDEX.md`

### kafka-tools
- **Definition:** Clients and management UIs for **Apache Kafka**. General messaging libs may live in `task-queue`.
- **Examples:** kafka-python, kafka-python, UI for Apache Kafka (provectus/kafka-ui)
- **File:** `categories/kafka-tools/INDEX.md`

### knowledge-content
- **Definition:** Personal collections whose dominant use is knowledge work, writing/content production, business judgment, social publishing, or broad operator utility rather than coding-agent engineering process.
- **Examples:** canghe-skills, canghe-skills, dbskill
- **File:** `categories/knowledge-content/INDEX.md`

### llm-chat-ui
- **Definition:** Self-deployable **chat client front-ends** a single user (or small group) points at their own LLM provider keys. For admin-managed multi-user team chat with quotas see `team-chat`; for agent framework
- **Examples:** LibreChat, LibreChat, NextChat
- **File:** `categories/llm-chat-ui/INDEX.md`

### llm-eval
- **Definition:** Tools whose primary job is to **evaluate, benchmark, or red-team** LLM prompts/agents/RAG. Not code review (see `ai-code-review`), not training (see `llm-training`).
- **Examples:** chatgpt-comparison-detection, chatgpt-comparison-detection, DeepEval
- **File:** `categories/llm-eval/INDEX.md`

### llm-inference
- **Definition:** Engines and systems languages whose primary job is **high-performance LLM/model inference and serving**. Not on-device/edge runtimes (see `on-device-ml`), not LLM fine-tuning (see `llm-training`).
- **Examples:** BentoML, BentoML, llama.cpp
- **File:** `categories/llm-inference/INDEX.md`

### llm-training
- **Definition:** Tools and frameworks whose primary job is to **train, fine-tune, or RL-optimize** LLMs or agents.
Not inference runtimes (see `on-device-ml`), not agent build/run frameworks (see `agent-frameworks`).
- **Examples:** Agent Lightning, Agent Lightning, ART (Agent Reinforcement Trainer)
- **File:** `categories/llm-training/INDEX.md`

### markdown-tools
- **Definition:** Tools whose primary job is **parsing, rendering, or authoring Markdown** — parsers, converters, and editor extensions. Not document parsing into structured data for gen-AI (see `document-parsing`), no
- **Examples:** CommonMark, CommonMark, Goldmark
- **File:** `categories/markdown-tools/INDEX.md`

### media-download
- **Definition:** Tools whose primary job is **fetching media from streaming/hosting sites** (extractors, downloaders). Not media transcoding/encoding (see `media-processing`), not generic file servers (see `document-m
- **Examples:** bulk-downloader-for-reddit, bulk-downloader-for-reddit, cobalt
- **File:** `categories/media-download/INDEX.md`

### media-processing
- **Definition:** Decode, encode, transcode, filter, and score images, audio, and video.
- **Examples:** ImageMagick, ImageMagick, sharp
- **File:** `categories/media-processing/INDEX.md`

### ml-research
- **Definition:** Small, self-contained **ML research demos** and reference implementations meant to read and learn from, not to productionize. Not training frameworks (see `llm-training`).
- **Examples:** Agriculture Knowledge Graph (AgriKG), Agriculture Knowledge Graph (AgriKG), autoresearch
- **File:** `categories/ml-research/INDEX.md`

### networking
- **Definition:** Libraries/tools for **network protocols and links** — SSH, DNS, tunnels, RPC, bandwidth shaping.
- **Examples:** dnspython, dnspython, Paramiko
- **File:** `categories/networking/INDEX.md`

### nginx-modules
- **Definition:** **NGINX / OpenResty** extension modules. Full API gateways live in `api-gateway`.
- **Examples:** lua-nginx-module (ngx_lua), lua-nginx-module (ngx_lua), lua-resty-redis
- **File:** `categories/nginx-modules/INDEX.md`

### observability
- **Definition:** Tools whose primary job is **visualizing and alerting** on metrics/logs/traces from datasources you already run. Not collection agents (see `dev-utilities` → Telegraf), not SQL/BI analytics (see `data
- **Examples:** Grafana, Grafana, Jaeger
- **File:** `categories/observability/INDEX.md`

### ocr
- **Definition:** Engines/libraries whose primary job is **recognizing text in images/scans**. Not document layout-and-table parsing for gen-AI (see `document-parsing`), not document archiving/search (see `document-man
- **Examples:** LaTeX-OCR (pix2tex), LaTeX-OCR (pix2tex), Tesseract
- **File:** `categories/ocr/INDEX.md`

### on-device-ml
- **Definition:** Runtimes and models meant to **run inference locally / on-device** — phone, laptop, edge, CPU. Not cloud training (see `llm-training`), not RAG retrieval (see `rag-retrieval`).
- **Examples:** Google AI Edge Gallery, Google AI Edge Gallery, BitNet
- **File:** `categories/on-device-ml/INDEX.md`

### ops-infra
- **Definition:** Self-hostable infrastructure and operational tools for servers, metrics, TLS, images, proxying, remote access, and passwords.
- **Examples:** Certbot, Certbot, Clash Verge Rev
- **File:** `categories/ops-infra/INDEX.md`

### orchestration-and-review
- **Definition:** Coding-agent control planes, multi-agent runners, and review/automation wrappers.
- **Examples:** Background Agents (Open-Inspect), Background Agents (Open-Inspect), CC Switch
- **File:** `categories/orchestration-and-review/INDEX.md`

### pdf-tools
- **Definition:** Tools whose primary job is to **render, read, or manipulate PDF files** — viewers, parsers, generators, and editors. Not parsing documents into structured Markdown/JSON for gen-AI (see `document-parsi
- **Examples:** jsPDF, jsPDF, OCRmyPDF
- **File:** `categories/pdf-tools/INDEX.md`

### personal-collections
- **Definition:** Use this parent when the selection question is “whose personal skill collection should I install?” Descend into a child leaf by dominant task: coding workflow or knowledge/content/business work.
- **Examples:** antfu/skills, antfu/skills, claude-code-harness
- **File:** `categories/personal-collections/INDEX.md`

### product-tours
- **Definition:** Product tour, onboarding, spotlight, and guided-step UI libraries.
- **Examples:** Driver.js, Driver.js, Intro.js
- **File:** `categories/product-tours/INDEX.md`

### proxy-pool
- **Definition:** Self-hosted **rotating proxy-IP pools** for web scraping. Not scraping frameworks themselves, not web/browser automation (see `web-automation`).
- **Examples:** haipproxy, haipproxy, proxy_pool
- **File:** `categories/proxy-pool/INDEX.md`

### python-tooling
- **Definition:** Developer tooling for the **Python** ecosystem — compilers, debuggers/injection, kernels, HTTP helpers.
- **Examples:** Cython, Cython, gophernotes
- **File:** `categories/python-tooling/INDEX.md`

### quality-metrics
- **Definition:** Perceptual media quality metrics and benchmarking tools.
- **Examples:** SSIMULACRA2, SSIMULACRA2, VMAF
- **File:** `categories/quality-metrics/INDEX.md`

### rag-retrieval
- **Definition:** Infrastructure whose primary job is **indexing and retrieving** context for RAG — document indexes, code graphs, graph databases. Not agent memory (see `agent-memory`), not research agents (see `deep-
- **Examples:** code-review-graph, code-review-graph, FAISS
- **File:** `categories/rag-retrieval/INDEX.md`

### reading-tools
- **Definition:** End-user **reading** tools — reader-mode browser extensions, bilingual/immersive translation extensions, RSS/feed readers. Article-extraction libraries live in `web-scraping`.
- **Examples:** FluentRead, FluentRead, FreshRSS
- **File:** `categories/reading-tools/INDEX.md`

### security
- **Definition:** Skill collections for **security work** — review, threat modeling, cybersecurity playbooks.
- **Examples:** Anthropic Cybersecurity Skills, Anthropic Cybersecurity Skills
- **File:** `categories/security/INDEX.md`

### slides-ppt
- **Definition:** Agent skills whose primary output is a **presentation / slide deck**: HTML swipe decks, PPT-like decks, keynote-style decks, or slide-specific generation workflows.
- **Examples:** frontend-slides, frontend-slides, Guizang PPT Skill
- **File:** `categories/slides-ppt/INDEX.md`

### speech
- **Definition:** Toolkits for **speech** — recognition (ASR), synthesis (TTS), speaker/audio tasks.
- **Examples:** SpeechBrain, SpeechBrain
- **File:** `categories/speech/INDEX.md`

### subagent-collections
- **Definition:** Collections of ready-made **subagent definitions / agent personas** to install into a harness — pick by the role coverage you need.
- **Examples:** Agency-Agents, Agency-Agents, awesome-claude-code-subagents
- **File:** `categories/subagent-collections/INDEX.md`

### task-queue
- **Definition:** Systems whose primary job is **distributed background job execution** — task queues and job schedulers. Not workflow/DAG orchestrators (see `workflow-orchestration`), not agent runtimes (see `agent-fr
- **Examples:** Celery, Celery, Flower
- **File:** `categories/task-queue/INDEX.md`

### team-chat
- **Definition:** Self-hostable **chat / chatbot applications** for teams or individuals. Not agent runtimes (see `agent-frameworks`), not memory infra (see `agent-memory`).
- **Examples:** HiveChat, HiveChat
- **File:** `categories/team-chat/INDEX.md`

### terminal-agents
- **Definition:** Terminal-first coding agents and CLI pair programmers.
- **Examples:** aider, aider, Codex
- **File:** `categories/terminal-agents/INDEX.md`

### terminal-ui
- **Definition:** Libraries that **render UI in the terminal** — colors, TUIs, ASCII art, styled output.
- **Examples:** Alacritty, Alacritty, ART
- **File:** `categories/terminal-ui/INDEX.md`

### vendor-collections
- **Definition:** **Official or vendor-published** skill/plugin collections (Anthropic, AWS, MiniMax, …) — first-party bundles.
- **Examples:** Anthropic Skills, Anthropic Skills, Agent Plugins for AWS
- **File:** `categories/vendor-collections/INDEX.md`

### video-audio
- **Definition:** Audio/video decode, encode, transcode, mux, subtitle, and pipeline tools.
- **Examples:** claude-video, claude-video, ffmpeg-python
- **File:** `categories/video-audio/INDEX.md`

### video-production
- **Definition:** Tools and frameworks whose primary job is **agent-driven or AI-orchestrated video production** — end-to-end pipelines that go from prompt/idea to finished video through research, scripting, asset gene
- **Examples:** OpenMontage, OpenMontage
- **File:** `categories/video-production/INDEX.md`

### visual-content
- **Definition:** Agent skills whose primary output is **visual content for publishing**: social cards, covers, article illustrations, quote cards, and related rendered artifacts.
- **Examples:** Guizang Social Card Skill, Guizang Social Card Skill, ian-xiaohei-illustrations
- **File:** `categories/visual-content/INDEX.md`

### web-automation
- **Definition:** Tools that **drive or automate a web/browser (or computer) GUI** — headless browser automation, computer-use, or in-page GUI agents. Not server-side scraping frameworks; not enterprise desktop-only RP
- **Examples:** Agent Browser, Agent Browser, browser-use
- **File:** `categories/web-automation/INDEX.md`

### web-scraping
- **Definition:** Fetch, crawl, and extract content or structure from web pages and web APIs.
- **Examples:** boilerpipe, boilerpipe, dragnet
- **File:** `categories/web-scraping/INDEX.md`

### web-ui
- **Definition:** Front-end UI/UX libraries — frameworks, component systems, and onboarding widgets.
- **Examples:** Ant Design, Ant Design, Chakra UI
- **File:** `categories/web-ui/INDEX.md`

### workflow-builders
- **Definition:** Prompt optimizers and visual/code-first platforms for building LLM workflows and agentic applications.
- **Examples:** AutoGPT, AutoGPT, Dify
- **File:** `categories/workflow-builders/INDEX.md`

### workflow-orchestration
- **Definition:** Tools whose primary job is to **author, schedule, and monitor batch data/workflow pipelines** as DAGs. Not low-latency event/stream processing, not agent build/run frameworks (see `agent-frameworks`).
- **Examples:** Airflow Maintenance DAGs, Airflow Maintenance DAGs, Apache Airflow
- **File:** `categories/workflow-orchestration/INDEX.md`

### writing
- **Definition:** Skill collections for **writing tasks** — translation, long-form drafting, editorial workflow, publishing and marketing pipelines. Dedicated de-AI/humanizer skills belong in [de-ai-writing](../de-ai-w
- **Examples:** Baoyu Skills, Baoyu Skills, huashu-skills
- **File:** `categories/writing/INDEX.md`

## Agent Task

For each candidate repo, choose the **single most appropriate** category.
Consider the repo's description, topics, and what it actually does.

If the repo does not fit any existing category, answer `needs-new-category`.
If uncertain, answer `uncertain`.

Return your classification in this exact format (one per line):

```
1. tauri-apps/tauri → web-ui
2. rust-lang/rust → needs-new-category
```

After classifying, apply the results to the JSON file (set `suggested_category`),
then run the report step to generate the final candidate report.