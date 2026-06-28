# oss-atlas

**A natural-language, agent-first index for open-source *selection* (选型).**
When a coding agent gets a task, it reads this index to pick the right OSS project —
weighing *when NOT to use* each option, not just what it does.

> 中文版 README：[README.zh.md](README.zh.md)

## Install

Install the **`select-oss`** skill into your coding agent — one skill that teaches the agent to
navigate this index and pick OSS for a task. It reads the public index over HTTP (no local copy
needed) and works in a clone too.

**Any agent, via [skills.sh](https://skills.sh)** (Claude Code, Codex, Cursor, OpenCode, Droid,
Kilo, Gemini CLI, Copilot, and ~70 more — the CLI knows each agent's skills path):

```bash
# Global (all your projects); drop -g for project-local. Pick agents with -a, e.g. -a claude-code
npx skills add ZhenningLang/oss-atlas -g
```

**Manual** (no Node) — copy the skill folder into your agent's skills dir, e.g. Claude Code:

```bash
git clone https://github.com/ZhenningLang/oss-atlas
cp -r oss-atlas/skills/select-oss ~/.claude/skills/
```

The skill fetches pages from `raw.githubusercontent.com/ZhenningLang/oss-atlas/main/`; only the
single `SKILL.md` is installed, so it stays tiny and always reads the latest index. For agents
without web access, the skill falls back to a local clone.

## Projects

The complete index, grouped by category. Each project has an English page (`<slug>.md`) and a Chinese sibling (`<slug>.zh.md`) — click straight through. Browse interactively from [INDEX.md](INDEX.md); agents start at [AGENTS.md](AGENTS.md).

### agent-tooling

| Project | Use when | License | Page |
|---|---|---|---|
| **beads** | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. | MIT | [EN](categories/agent-tooling/beads.md) · [中](categories/agent-tooling/beads.zh.md) |
| **CCPM** | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. | MIT | [EN](categories/agent-tooling/ccpm.md) · [中](categories/agent-tooling/ccpm.zh.md) |
| **Entire** | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. | MIT | [EN](categories/agent-tooling/entire-cli.md) · [中](categories/agent-tooling/entire-cli.zh.md) |
| **Ralph for Claude Code** | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. | MIT | [EN](categories/agent-tooling/ralph-claude-code.md) · [中](categories/agent-tooling/ralph-claude-code.zh.md) |
| **Context Mode** | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. | Elastic-2.0 | [EN](categories/agent-tooling/context-mode.md) · [中](categories/agent-tooling/context-mode.zh.md) |
| **Planning with Files** | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. | MIT | [EN](categories/agent-tooling/planning-with-files.md) · [中](categories/agent-tooling/planning-with-files.zh.md) |
| **Vercel Skills** | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. | MIT | [EN](categories/agent-tooling/vercel-skills.md) · [中](categories/agent-tooling/vercel-skills.zh.md) |
| **OpenSandbox** | Use it when you must self-host isolated sandboxes to run untrusted agent-generated code at K8s scale with egress controls and a credential vault — but the repo is only months old (created 2025-12), so its API and Lindy track record are unproven. | Apache-2.0 | [EN](categories/agent-tooling/opensandbox.md) · [中](categories/agent-tooling/opensandbox.zh.md) |
| **AgentsView** | Use it when you run several coding agents and want local-first cross-agent session search and token/cost analytics — but it's months-old and pre-1.0, expect churn. | MIT | [EN](categories/agent-tooling/agentsview.md) · [中](categories/agent-tooling/agentsview.zh.md) |
### document-management

| Project | Use when | License | Page |
|---|---|---|---|
| **paperless-ngx** | Use it when you want to self-host OCR + tagging + full-text search over scanned paperwork. | GPL-3.0 | [EN](categories/document-management/paperless-ngx.md) · [中](categories/document-management/paperless-ngx.zh.md) |
| **copyparty** | Use it when you need a single-file portable file server with resumable uploads, dedup, and multi-protocol access — not OCR document search. | MIT | [EN](categories/document-management/copyparty.md) · [中](categories/document-management/copyparty.zh.md) |
| **Twake Drive** | Use it when you want a self-hosted Google-Drive-style file network drive inside the Twake/Cozy stack, not OCR archiving. | AGPL-3.0 | [EN](categories/document-management/twake-drive.md) · [中](categories/document-management/twake-drive.zh.md) |

### on-device-ml

| Project | Use when | License | Page |
|---|---|---|---|
| **LiteRT-LM** | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). | Apache-2.0 | [EN](categories/on-device-ml/litert-lm.md) · [中](categories/on-device-ml/litert-lm.zh.md) |
| **BitNet** | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. | MIT | [EN](categories/on-device-ml/bitnet.md) · [中](categories/on-device-ml/bitnet.zh.md) |
| **Google AI Edge Gallery** | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. | Apache-2.0 | [EN](categories/on-device-ml/ai-edge-gallery.md) · [中](categories/on-device-ml/ai-edge-gallery.zh.md) |
| **TimesFM** | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. | Apache-2.0 | [EN](categories/on-device-ml/timesfm.md) · [中](categories/on-device-ml/timesfm.zh.md) |
| **MiniCPM-V** | Use it when you need efficient on-device/edge multimodal (image+video) understanding with a small footprint — verify the per-weight license. | Apache-2.0 | [EN](categories/on-device-ml/minicpm-v.md) · [中](categories/on-device-ml/minicpm-v.zh.md) |

### web-automation

| Project | Use when | License | Page |
|---|---|---|---|
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | MIT | [EN](categories/web-automation/page-agent.md) · [中](categories/web-automation/page-agent.zh.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | Apache-2.0 | [EN](categories/web-automation/chrome-devtools-mcp.md) · [中](categories/web-automation/chrome-devtools-mcp.zh.md) |
| **Cua** | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. | MIT | [EN](categories/web-automation/cua.md) · [中](categories/web-automation/cua.zh.md) |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | Apache-2.0 | [EN](categories/web-automation/agent-browser.md) · [中](categories/web-automation/agent-browser.zh.md) |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | Apache-2.0 | [EN](categories/web-automation/selenium.md) · [中](categories/web-automation/selenium.zh.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | BSD-3-Clause | [EN](categories/web-automation/phantomjs.md) · [中](categories/web-automation/phantomjs.zh.md) |
| **Selenium Wire** | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. | MIT | [EN](categories/web-automation/selenium-wire.md) · [中](categories/web-automation/selenium-wire.zh.md) |
### llm-training

| Project | Use when | License | Page |
|---|---|---|---|
| **LlamaFactory** | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. | Apache-2.0 | [EN](categories/llm-training/llamafactory.md) · [中](categories/llm-training/llamafactory.zh.md) |
| **Unsloth** | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. | Apache-2.0 | [EN](categories/llm-training/unsloth.md) · [中](categories/llm-training/unsloth.zh.md) |
| **ART (Agent Reinforcement Trainer)** | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. | Apache-2.0 | [EN](categories/llm-training/art.md) · [中](categories/llm-training/art.zh.md) |
| **Agent Lightning** | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. | MIT | [EN](categories/llm-training/agent-lightning.md) · [中](categories/llm-training/agent-lightning.zh.md) |
| **Colossal-AI** | Use it when you must train/fine-tune large models across many GPUs with tensor/pipeline/ZeRO parallelism — overkill for single-GPU LoRA. | Apache-2.0 | [EN](categories/llm-training/colossalai.md) · [中](categories/llm-training/colossalai.zh.md) |

### agent-frameworks

| Project | Use when | License | Page |
|---|---|---|---|
| **DSPy** | You have eval data and a metric and want optimizers to compile prompts instead of hand-tuning them. | MIT | [EN](categories/agent-frameworks/dspy.md) · [中](categories/agent-frameworks/dspy.zh.md) |
| **AgentScope** | Shipping a production multi-agent LLM service needing sandboxed tools, permissions, tracing, and human-in-the-loop. | Apache-2.0 | [EN](categories/agent-frameworks/agentscope.md) · [中](categories/agent-frameworks/agentscope.zh.md) |
| **OpenFang** | You want autonomous agents that run on a schedule from one self-hosted Rust binary. | Apache-2.0 OR MIT | [EN](categories/agent-frameworks/openfang.md) · [中](categories/agent-frameworks/openfang.zh.md) |
| **Symphony** | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. | Apache-2.0 | [EN](categories/agent-frameworks/symphony.md) · [中](categories/agent-frameworks/symphony.zh.md) |
| **Claude Octopus** | You live in Claude Code and want other AI models to cross-review tasks for blindspots before shipping. | MIT | [EN](categories/agent-frameworks/claude-octopus.md) · [中](categories/agent-frameworks/claude-octopus.zh.md) |
| **oh-my-claudecode** | You live in Claude Code and need staged multi-agent teams with model routing and tmux parallelism. | MIT | [EN](categories/agent-frameworks/oh-my-claudecode.md) · [中](categories/agent-frameworks/oh-my-claudecode.zh.md) |
| **smolagents** | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. | Apache-2.0 | [EN](categories/agent-frameworks/smolagents.md) · [中](categories/agent-frameworks/smolagents.zh.md) |
| **Kilo Code** | Use it when you want an open, BYOK in-IDE (VS Code) coding agent with planning and modes — an end-user tool, not a library to build agents. | MIT | [EN](categories/agent-frameworks/kilocode.md) · [中](categories/agent-frameworks/kilocode.zh.md) |
| **Parlant** | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. | Apache-2.0 | [EN](categories/agent-frameworks/parlant.md) · [中](categories/agent-frameworks/parlant.zh.md) |
| **SkillOpt** | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. | MIT | [EN](categories/agent-frameworks/skillopt.md) · [中](categories/agent-frameworks/skillopt.zh.md) |
### agent-memory

| Project | Use when | License | Page |
|---|---|---|---|
| **Mem0** | Use it when your LLM agent must remember users across sessions without bloating the prompt context. | Apache-2.0 | [EN](categories/agent-memory/mem0.md) · [中](categories/agent-memory/mem0.zh.md) |
| **Memori** | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. | Apache-2.0 | [EN](categories/agent-memory/memori.md) · [中](categories/agent-memory/memori.zh.md) |
| **Claude Subconscious** | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. | MIT | [EN](categories/agent-memory/claude-subconscious.md) · [中](categories/agent-memory/claude-subconscious.zh.md) |
| **claude-mem** | Use it when your coding agent loses context across sessions and you want local hook/MCP-captured memory compressed and injected back in. | Apache-2.0 | [EN](categories/agent-memory/claude-mem.md) · [中](categories/agent-memory/claude-mem.zh.md) |

### deep-research

| Project | Use when | License | Page |
|---|---|---|---|
| **deep-research** | Use it when you want a minimal, readable ~500-LOC TypeScript reference deep-research agent to fork and adapt. | MIT | [EN](categories/deep-research/deep-research.md) · [中](categories/deep-research/deep-research.zh.md) |
| **Vane** | Use it when you want a self-hosted, privacy-focused Perplexity-style cited answer engine over your own SearxNG and chosen LLM. | MIT | [EN](categories/deep-research/vane.md) · [中](categories/deep-research/vane.zh.md) |
| **Local Deep Research** | Use it when you need a self-hosted, fully-local deep-research agent that keeps sensitive queries on your own machine. | MIT | [EN](categories/deep-research/local-deep-research.md) · [中](categories/deep-research/local-deep-research.zh.md) |
| **Agent-Reach** | Use it when your agent needs to read and search web plus social platforms without paid APIs. | MIT | [EN](categories/deep-research/agent-reach.md) · [中](categories/deep-research/agent-reach.zh.md) |
| **MiroThinker** | Use it when you want a self-hosted, open-weights deep-research agent you can study and extend on your own GPUs — but it needs a GPU cluster plus paid external APIs and is under a year old with no Lindy. | Apache-2.0 | [EN](categories/deep-research/mirothinker.md) · [中](categories/deep-research/mirothinker.zh.md) |
### ai-code-review

| Project | Use when | License | Page |
|---|---|---|---|
| **Open Code Review** | Use it when you want precise, line-level LLM review comments on Git diffs in CI without PR noise. | Apache-2.0 | [EN](categories/ai-code-review/open-code-review.md) · [中](categories/ai-code-review/open-code-review.zh.md) |
| **Claude Code Security Review** | Use it when you want LLM-driven, context-aware security review on trusted PRs via a GitHub Action. | MIT | [EN](categories/ai-code-review/claude-code-security-review.md) · [中](categories/ai-code-review/claude-code-security-review.zh.md) |
| **React Doctor** | Use it when a coding agent writes React and you want deterministic, repeatable checks for React-specific anti-patterns. | LicenseRef-Modified-MIT | [EN](categories/ai-code-review/react-doctor.md) · [中](categories/ai-code-review/react-doctor.zh.md) |

### rag-retrieval

| Project | Use when | License | Page |
|---|---|---|---|
| **FalkorDB** | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. | SSPL-1.0 | [EN](categories/rag-retrieval/falkordb.md) · [中](categories/rag-retrieval/falkordb.zh.md) |
| **graphify** | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. | MIT | [EN](categories/rag-retrieval/graphify.md) · [中](categories/rag-retrieval/graphify.zh.md) |
| **code-review-graph** | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. | MIT | [EN](categories/rag-retrieval/code-review-graph.md) · [中](categories/rag-retrieval/code-review-graph.zh.md) |
| **PageIndex** | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. | MIT | [EN](categories/rag-retrieval/pageindex.md) · [中](categories/rag-retrieval/pageindex.zh.md) |
| **Understand-Anything** | Use it when you want any codebase turned into an explorable, queryable knowledge graph for an agent — younger and less proven than graphify. | MIT | [EN](categories/rag-retrieval/understand-anything.md) · [中](categories/rag-retrieval/understand-anything.zh.md) |
| **FAISS** | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. | MIT | [EN](categories/rag-retrieval/faiss.md) · [中](categories/rag-retrieval/faiss.zh.md) |
| **text2vec** | Use it when you need Chinese-first sentence embeddings for semantic search or FAQ matching from a single pip install — it's only the encoder, so bring your own vector index (FAISS/Milvus). | Apache-2.0 | [EN](categories/rag-retrieval/text2vec.md) · [中](categories/rag-retrieval/text2vec.zh.md) |
### llm-eval

| Project | Use when | License | Page |
|---|---|---|---|
| **promptfoo** | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. | MIT | [EN](categories/llm-eval/promptfoo.md) · [中](categories/llm-eval/promptfoo.zh.md) |
| **Pezzo** | Use it when a small team wants one self-hosted control plane for prompt versioning plus cost/latency observability — but it looks stalled since mid-2025, so assume you'll maintain it yourself. | Apache-2.0 | [EN](categories/llm-eval/pezzo.md) · [中](categories/llm-eval/pezzo.zh.md) |
### agent-dev-methodology

| Project | Use when | License | Page |
|---|---|---|---|
| **12-Factor Agents** | Use it when you want production-agent design principles to guide a hand-rolled or thinly-framed agent. | CC-BY-SA-4.0 (content) / Apache-2.0 (code examples) | [EN](categories/agent-dev-methodology/12-factor-agents.md) · [中](categories/agent-dev-methodology/12-factor-agents.zh.md) |
| **Superpowers** | Use it when you want a drop-in brainstorm→plan→TDD→verify SDLC methodology installed into your coding agent. | MIT | [EN](categories/agent-dev-methodology/superpowers.md) · [中](categories/agent-dev-methodology/superpowers.zh.md) |
| **SuperClaude Framework** | Use it when you live in Claude Code and want a ready-made command, agent, and behavioral-mode framework installed at once. | MIT | [EN](categories/agent-dev-methodology/superclaude.md) · [中](categories/agent-dev-methodology/superclaude.zh.md) |
| **Get Shit Done (GSD)** | Use it when you build through a coding agent and want a spec-driven, fresh-context phase pipeline that fights context rot. | MIT | [EN](categories/agent-dev-methodology/get-shit-done.md) · [中](categories/agent-dev-methodology/get-shit-done.zh.md) |
| **Compound Engineering** | Use it when you want a turnkey brainstorm→plan→work→review→compound loop that persists learnings across coding-agent sessions. | MIT | [EN](categories/agent-dev-methodology/compound-engineering.md) · [中](categories/agent-dev-methodology/compound-engineering.zh.md) |
| **ECC** | Use it when you want a maintained, batteries-included Claude Code harness of skills, agents, hooks, memory, and a security scanner. | MIT | [EN](categories/agent-dev-methodology/ecc.md) · [中](categories/agent-dev-methodology/ecc.zh.md) |

### ai-design-generation

| Project | Use when | License | Page |
|---|---|---|---|
| **HTML Anything** | Use it when you already run a logged-in coding-agent CLI and want local-first, key-free Markdown-to-shippable-HTML generation with one-click WeChat/X/Zhihu export. | Apache-2.0 | [EN](categories/ai-design-generation/html-anything.md) · [中](categories/ai-design-generation/html-anything.zh.md) |
| **Open Design** | Use it when you want a local-first, BYOK desktop studio that makes your coding agent generate HTML prototypes, decks, images and HTML→MP4. | Apache-2.0 | [EN](categories/ai-design-generation/open-design.md) · [中](categories/ai-design-generation/open-design.zh.md) |
| **Impeccable** | Use it when your AI agent keeps shipping same-looking frontend slop and you want deterministic detection plus design critique. | Apache-2.0 | [EN](categories/ai-design-generation/impeccable.md) · [中](categories/ai-design-generation/impeccable.zh.md) |
| **ian-xiaohei-illustrations** | Use it when you need consistent hand-drawn 16:9 Chinese article illustrations with a fixed IP. | MIT | [EN](categories/ai-design-generation/ian-illustrations.md) · [中](categories/ai-design-generation/ian-illustrations.zh.md) |
| **Guizang PPT Skill** | Use it when you want an agent to turn an article into a designed single-file HTML swipe deck. | AGPL-3.0-only | [EN](categories/ai-design-generation/guizang-ppt.md) · [中](categories/ai-design-generation/guizang-ppt.zh.md) |
| **Guizang Social Card Skill** | Use it when a coding agent needs art-directed Xiaohongshu carousels or WeChat cover pairs as single-file HTML rendered to PNG. | AGPL-3.0-only | [EN](categories/ai-design-generation/guizang-social-card.md) · [中](categories/ai-design-generation/guizang-social-card.zh.md) |
| **SdPaint** | Use it when you already run AUTOMATIC1111 + ControlNet and want a live sketch-to-image painting loop — but it's stalled since 2024 and provides no model of its own. | MIT | [EN](categories/ai-design-generation/sdpaint.md) · [中](categories/ai-design-generation/sdpaint.zh.md) |
### dev-utilities

| Project | Use when | License | Page |
|---|---|---|---|
| **DevToys** | Use it when you want offline, local-only dev utilities (Base64/JSON/hash/diff) in one cross-platform desktop app instead of untrusted online tools. | MIT | [EN](categories/dev-utilities/devtoys.md) · [中](categories/dev-utilities/devtoys.zh.md) |
| **CyberChef** | Use it when you need to chain encode/decode, crypto, compression and data-analysis transforms offline in your browser. | Apache-2.0 | [EN](categories/dev-utilities/cyberchef.md) · [中](categories/dev-utilities/cyberchef.zh.md) |
| **Cockpit** | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. | LGPL-2.1-or-later | [EN](categories/dev-utilities/cockpit.md) · [中](categories/dev-utilities/cockpit.zh.md) |
| **Telegraf** | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. | MIT | [EN](categories/dev-utilities/telegraf.md) · [中](categories/dev-utilities/telegraf.zh.md) |
| **OpenZL** | Use it when you must squeeze terabytes of one highly structured/numeric format better than generic zstd. | BSD-3-Clause | [EN](categories/dev-utilities/openzl.md) · [中](categories/dev-utilities/openzl.zh.md) |
| **Certbot** | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. | Apache-2.0 | [EN](categories/dev-utilities/certbot.md) · [中](categories/dev-utilities/certbot.zh.md) |
| **tqdm** | Use it when you want a fast, low-overhead progress bar for Python loops/CLI/notebooks. | MPL-2.0 AND MIT | [EN](categories/dev-utilities/tqdm.md) · [中](categories/dev-utilities/tqdm.zh.md) |
| **SlimToolkit** | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. | Apache-2.0 | [EN](categories/dev-utilities/slim.md) · [中](categories/dev-utilities/slim.zh.md) |
| **Faker (faker-js)** | Use it when you need realistic fake/mock data (names, addresses, finance…) for tests and seeding in JS/TS. | MIT | [EN](categories/dev-utilities/faker-js.md) · [中](categories/dev-utilities/faker-js.zh.md) |
| **fontTools** | Use it when you need programmatic font surgery — subset webfonts, convert formats, inspect/patch tables — but it edits font files, it won't design glyphs or shape text. | MIT | [EN](categories/dev-utilities/fonttools.md) · [中](categories/dev-utilities/fonttools.zh.md) |
| **Flashlight** | Use it when you're keeping a vintage macOS 10.10–10.15 machine and want Spotlight plugins — but it's abandoned since 2020 and requires disabling SIP, avoid on real machines. | MIT AND GPL-2.0-only (component split) | [EN](categories/dev-utilities/flashlight.md) · [中](categories/dev-utilities/flashlight.zh.md) |
| **IdeaVim** | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. | MIT | [EN](categories/dev-utilities/ideavim.md) · [中](categories/dev-utilities/ideavim.zh.md) |
### frontend-animation

| Project | Use when | License | Page |
|---|---|---|---|
| **Anime.js** | Dependency-free JS animation engine: CSS, SVG, DOM attrs and JS objects through one animate() API, with timeline, stagger, spring easings, and scroll-linked playback. | MIT | [EN](categories/frontend-animation/anime.md) · [中](categories/frontend-animation/anime.zh.md) |

### api-gateway

| Project | Use when | License | Page |
|---|---|---|---|
| **Kong Gateway** | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. | Apache-2.0 | [EN](categories/api-gateway/kong.md) · [中](categories/api-gateway/kong.zh.md) |

### geospatial

| Project | Use when | License | Page |
|---|---|---|---|
| **QGIS** | Full-featured cross-platform desktop GIS (Qt/C++) to view, edit, analyze and publish vector/raster/mesh/point-cloud spatial data, with PyQGIS plugins and a headless server. | GPL-2.0-or-later | [EN](categories/geospatial/qgis.md) · [中](categories/geospatial/qgis.zh.md) |

### team-chat

| Project | Use when | License | Page |
|---|---|---|---|
| **HiveChat** | Self-hostable, admin-managed AI chat for small/medium teams: one admin wires many LLM providers; the team chats with per-group model access and token quotas. | Apache-2.0 | [EN](categories/team-chat/hivechat.md) · [中](categories/team-chat/hivechat.zh.md) |

### captcha

| Project | Use when | License | Page |
|---|---|---|---|
| **Cap** | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. | Apache-2.0 | [EN](categories/captcha/capjs.md) · [中](categories/captcha/capjs.zh.md) |
| **Text_select_captcha** | Use it when automating Chinese click-to-select-text CAPTCHAs (YOLO + Siamese, CPU-only) — there's no LICENSE file, so all rights reserved and legality is the decisive filter. | NONE (no LICENSE file — all rights reserved) | [EN](categories/captcha/text-select-captcha.md) · [中](categories/captcha/text-select-captcha.zh.md) |
| **pytorch-captcha-recognition** | Use it as a readable teaching baseline for fixed-length text-in-image CAPTCHAs via a multi-head CNN — it's a frozen 2020 tutorial, expect to modernize the dated PyTorch APIs. | Apache-2.0 | [EN](categories/captcha/pytorch-captcha-recognition.md) · [中](categories/captcha/pytorch-captcha-recognition.zh.md) |
| **captcha (lepture)** | Use it when a Python web form needs a self-hosted image/audio CAPTCHA renderer with no third-party call — it's render-only and weak against modern OCR, treat it as a UX speed-bump, not security. | BSD-3-Clause | [EN](categories/captcha/lepture-captcha.md) · [中](categories/captcha/lepture-captcha.zh.md) |
### ml-research

| Project | Use when | License | Page |
|---|---|---|---|
| **autoresearch** | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. | MIT | [EN](categories/ml-research/autoresearch.md) · [中](categories/ml-research/autoresearch.zh.md) |
| **llm-circuit-finder** | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. | MIT | [EN](categories/ml-research/llm-circuit-finder.md) · [中](categories/ml-research/llm-circuit-finder.zh.md) |
| **CLIP** | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. | MIT | [EN](categories/ml-research/clip.md) · [中](categories/ml-research/clip.zh.md) |
| **TaskMatrix** | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. | MIT | [EN](categories/ml-research/taskmatrix.md) · [中](categories/ml-research/taskmatrix.zh.md) |
| **PyTorch-GAN** | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. | MIT | [EN](categories/ml-research/pytorch-gan.md) · [中](categories/ml-research/pytorch-gan.zh.md) |
| **LSTM Neural Network for Time Series Prediction** | Use it as a readable article-companion example for learning Keras LSTM time-series forecasting — pinned to EOL TF1/Python 3.5 and AGPL-3.0, re-implement from the article rather than vendoring. | AGPL-3.0 | [EN](categories/ml-research/lstm-time-series.md) · [中](categories/ml-research/lstm-time-series.zh.md) |
| **Agriculture Knowledge Graph (AgriKG)** | Use it as a complete blueprint and bundled datasets for a Chinese domain knowledge-graph pipeline (NER, RE, Neo4j, Django) — author-declared unmaintained on a dated GPL-3.0 stack, lift techniques not code. | GPL-3.0 | [EN](categories/ml-research/agriculture-knowledge-graph.md) · [中](categories/ml-research/agriculture-knowledge-graph.zh.md) |
| **Senta (SKEP)** | Use it when working inside PaddlePaddle/ERNIE and needing SKEP sentiment checkpoints with a published method — pinned to EOL PaddlePaddle 1.6.3, so environment archaeology is unavoidable. | Apache-2.0 | [EN](categories/ml-research/senta.md) · [中](categories/ml-research/senta.zh.md) |
| **Depth Anything V2** | Use it as the current default monocular-depth foundation model for single-image depth in PyTorch/Transformers — only the Small weights are Apache-2.0; Base/Large/Giant are CC-BY-NC-4.0 (non-commercial). | Apache-2.0 | [EN](categories/ml-research/depth-anything-v2.md) · [中](categories/ml-research/depth-anything-v2.zh.md) |
| **pymoo** | Use it as the de-facto Python library for evolutionary multi-objective optimization (NSGA-II/III, MOEA/D) to find Pareto fronts — for convex/linear/single-objective problems an LP/gradient solver is far faster. | Apache-2.0 | [EN](categories/ml-research/pymoo.md) · [中](categories/ml-research/pymoo.zh.md) |
### agent-skill-collections

#### agent-skill-collections / engineering

| Project | Use when | License | Page |
|---|---|---|---|
| **Agent Skills (addyosmani)** | A curated pack of ~24 production-engineering skills (quality, security, web-perf, API, ship) installed into your coding agent and routed through ~8 SDLC slash commands. | MIT | [EN](categories/agent-skill-collections/engineering/addyosmani-agent-skills.md) · [中](categories/agent-skill-collections/engineering/addyosmani-agent-skills.zh.md) |
| **web-quality-skills** | A six-skill agent pack encoding Lighthouse / Core Web Vitals / WCAG / SEO best practices as on-demand instruction sets so a coding agent can audit and fix web-quality issues; advisory, not a measurement tool. | MIT | [EN](categories/agent-skill-collections/engineering/addyosmani-web-quality.md) · [中](categories/agent-skill-collections/engineering/addyosmani-web-quality.zh.md) |
| **Scientific Agent Skills** | A large skill pack (~147 skills) that turns a coding agent into a research assistant for biology, chemistry, medicine, and drug discovery — each skill wraps a scientific Python library or database with a documented SKILL.md loaded on demand. | MIT | [EN](categories/agent-skill-collections/engineering/scientific-agent-skills.md) · [中](categories/agent-skill-collections/engineering/scientific-agent-skills.zh.md) |
| **Vercel Agent Skills** | Vercel's official agent-skill pack — install-on-demand React/Next.js/Vercel deploy, web-design, and docs audit guides in the agentskills.io/skills.sh format. | MIT | [EN](categories/agent-skill-collections/engineering/vercel-agent-skills.md) · [中](categories/agent-skill-collections/engineering/vercel-agent-skills.zh.md) |
| **Waza** | A compact collection of eight "engineering habit" skills (plan, design, review, debug, write, research, read, audit) a coding agent loads on demand across Claude Code, Codex, and Cursor. | MIT | [EN](categories/agent-skill-collections/engineering/waza.md) · [中](categories/agent-skill-collections/engineering/waza.zh.md) |

#### agent-skill-collections / design

| Project | Use when | License | Page |
|---|---|---|---|
| **Designer Skills** | A broad design-practice skill pack — 97 skills and 30 commands across 9 plugins (research, design systems, UX strategy, UI, interaction, prototyping/testing, design ops, toolkit, visual critique) for Claude Code and Gemini CLI. | MIT | [EN](categories/agent-skill-collections/design/designer-skills.md) · [中](categories/agent-skill-collections/design/designer-skills.zh.md) |
| **make-interfaces-feel-better** | A single, focused agent skill that injects ~16 concrete UI-polish principles (concentric radius, interruptible transitions, tabular numbers, enter/exit animation) so a coding agent ships interfaces that feel finished, not merely correct. | MIT | [EN](categories/agent-skill-collections/design/make-interfaces-feel-better.md) · [中](categories/agent-skill-collections/design/make-interfaces-feel-better.zh.md) |
| **Stitch Skills** | A library of Agent Skills (open standard) that drive Google's Stitch MCP server to generate UI screens, convert code↔design, extract DESIGN.md, and export React/React Native/shadcn components. | Apache-2.0 | [EN](categories/agent-skill-collections/design/stitch-skills.md) · [中](categories/agent-skill-collections/design/stitch-skills.zh.md) |
| **Taste-Skill** | A portable, framework-agnostic agent skill pack that gives coding agents visual taste — stopping generic AI-slop frontends and pushing intentional layout, typography, motion, and spacing. | MIT | [EN](categories/agent-skill-collections/design/taste-skill.md) · [中](categories/agent-skill-collections/design/taste-skill.zh.md) |
| **UI UX Pro Max Skill** | A design-intelligence skill pack that gives a coding agent UI/UX taste via a local CSV-backed retrieval engine (style/palette/font/rule databases) plus a pre-delivery accessibility checklist, installed across many agent harnesses. | MIT | [EN](categories/agent-skill-collections/design/ui-ux-pro-max.md) · [中](categories/agent-skill-collections/design/ui-ux-pro-max.zh.md) |

#### agent-skill-collections / writing

| Project | Use when | License | Page |
|---|---|---|---|
| **Baoyu Skills** | A 20+ skill pack for coding agents (translation, markdown/HTML formatting, transcript/URL capture, image/diagram/slide generation), installable into Claude Code, Codex, and other skill-capable harnesses. | MIT | [EN](categories/agent-skill-collections/writing/baoyu-skills.md) · [中](categories/agent-skill-collections/writing/baoyu-skills.zh.md) |
| **Humanizer-zh** | A single Chinese Claude Code skill that rewrites text to strip ~24 tell-tale AI-writing patterns; a localization of blader/humanizer. | MIT | [EN](categories/agent-skill-collections/writing/humanizer-zh.md) · [中](categories/agent-skill-collections/writing/humanizer-zh.zh.md) |

#### agent-skill-collections / security

| Project | Use when | License | Page |
|---|---|---|---|
| **Anthropic Cybersecurity Skills** | A large (~817 skill) cybersecurity skill pack of SKILL.md runbooks cross-mapped to MITRE ATT&CK, NIST CSF, ATLAS, D3FEND, NIST AI RMF and MITRE F3, loaded on demand into a coding agent. | Apache-2.0 | [EN](categories/agent-skill-collections/security/anthropic-cybersecurity-skills.md) · [中](categories/agent-skill-collections/security/anthropic-cybersecurity-skills.zh.md) |

#### agent-skill-collections / context-engineering

| Project | Use when | License | Page |
|---|---|---|---|
| **Agent Skills for Context Engineering** | A 15-skill Claude Code plugin pack teaching context-engineering discipline: fundamentals, degradation, compression, multi-agent coordination, memory, tool design, evaluation, and harness engineering. | MIT | [EN](categories/agent-skill-collections/context-engineering/context-engineering-skills.md) · [中](categories/agent-skill-collections/context-engineering/context-engineering-skills.zh.md) |
| **NotebookLM Claude Code Skill** | A Claude Code skill that drives real Chrome to query your Google NotebookLM notebooks, returning source-grounded, citation-backed answers from your own docs instead of file-reading or hallucinating. | MIT | [EN](categories/agent-skill-collections/context-engineering/notebooklm-skill.md) · [中](categories/agent-skill-collections/context-engineering/notebooklm-skill.zh.md) |

#### agent-skill-collections / vendor-collections

| Project | Use when | License | Page |
|---|---|---|---|
| **Anthropic Skills** | Anthropic's official public collection of Agent Skills — self-contained SKILL.md folders (document editing, design, MCP/skill authoring, comms) installable into Claude Code, Claude.ai, or the Claude API. | Apache-2.0 | [EN](categories/agent-skill-collections/vendor-collections/anthropic-skills.md) · [中](categories/agent-skill-collections/vendor-collections/anthropic-skills.zh.md) |
| **Agent Plugins for AWS** | AWS Labs' official collection of nine agent plugins (serverless, Amplify, SageMaker, migration, databases, deploy/cost-estimate, etc.) that teach Claude Code / Cursor / Codex to architect, deploy, and operate on AWS via marketplace-installed, trigger-phrase skills wired to AWS MCP servers. | Apache-2.0 | [EN](categories/agent-skill-collections/vendor-collections/aws-agent-plugins.md) · [中](categories/agent-skill-collections/vendor-collections/aws-agent-plugins.zh.md) |
| **Claude Plugins (Official)** | Anthropic's first-party Claude Code plugin marketplace: a curated directory of installable plugins (commands, agents, skills, MCP servers) installed by name via the native /plugin system. | Apache-2.0 | [EN](categories/agent-skill-collections/vendor-collections/claude-plugins-official.md) · [中](categories/agent-skill-collections/vendor-collections/claude-plugins-official.zh.md) |
| **MiniMax Skills** | MiniMax's official ~16-skill Agent Skills bundle (frontend/mobile/shader dev plus pdf/docx/xlsx/pptx, music & multimodal generation), installable into Claude Code and other coding agents via plugin marketplace. | MIT | [EN](categories/agent-skill-collections/vendor-collections/minimax-skills.md) · [中](categories/agent-skill-collections/vendor-collections/minimax-skills.zh.md) |
| **Anthropic Knowledge Work Plugins** | Use it when you want Anthropic's official open-source plugins aimed at knowledge work (docs, comms, research) for Claude — very young. | Apache-2.0 | [EN](categories/agent-skill-collections/vendor-collections/knowledge-work-plugins.md) · [中](categories/agent-skill-collections/vendor-collections/knowledge-work-plugins.zh.md) |

#### agent-skill-collections / subagent-collections

| Project | Use when | License | Page |
|---|---|---|---|
| **Agency-Agents** | A curated collection of ~232 specialized subagent personas (markdown) across 16 functional divisions, with install/convert scripts that deploy them into Claude Code and ~11 other agent harnesses. | MIT | [EN](categories/agent-skill-collections/subagent-collections/agency-agents.md) · [中](categories/agent-skill-collections/subagent-collections/agency-agents.zh.md) |
| **awesome-claude-code-subagents** | A curated bundle of 100+ specialized Claude Code subagent definitions (one markdown persona per role) you drop into ~/.claude/agents/ so Claude Code can delegate to a domain expert. | MIT | [EN](categories/agent-skill-collections/subagent-collections/awesome-claude-code-subagents.md) · [中](categories/agent-skill-collections/subagent-collections/awesome-claude-code-subagents.zh.md) |
| **wshobson/agents** | Large single-maintainer multi-harness plugin marketplace (~194 subagents, ~158 skills, ~106 commands, ~16 orchestrators) authored once in Markdown and generated into harness-native artifacts for Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI and Copilot. | MIT | [EN](categories/agent-skill-collections/subagent-collections/wshobson-agents.md) · [中](categories/agent-skill-collections/subagent-collections/wshobson-agents.zh.md) |

#### agent-skill-collections / personal-collections

| Project | Use when | License | Page |
|---|---|---|---|
| **antfu/skills** | Anthony Fu's personal curated agent-skill collection for the Vue/Vite/Nuxt stack (his ESLint/pnpm/Vitest/UnoCSS prefs + generated/vendored framework skills), installed via the skills CLI. | MIT | [EN](categories/agent-skill-collections/personal-collections/antfu-skills.md) · [中](categories/agent-skill-collections/personal-collections/antfu-skills.zh.md) |
| **claude-code-harness** | A personal Claude Code harness that installs a governed plan → work → review → release loop (spec-first contracts, TDD-gated execution, independent review) as a plugin, with a Go-native doctor CLI for diagnosing plugin-cache and skill drift. | MIT | [EN](categories/agent-skill-collections/personal-collections/claude-code-harness.md) · [中](categories/agent-skill-collections/personal-collections/claude-code-harness.zh.md) |
| **dbskill** | A personal, curated pack of ~21 Chinese-language agent skills (/dbs-*) for business-model diagnosis, content creation, and personal decision-making, installable into Claude Code and other harnesses. | CC-BY-NC-4.0 | [EN](categories/agent-skill-collections/personal-collections/dbskill.md) · [中](categories/agent-skill-collections/personal-collections/dbskill.zh.md) |
| **Dimillian Skills** | One developer's personal collection of 16 self-contained Codex skills, heavily focused on Apple-platform work (SwiftUI/iOS/macOS) plus generic review/refactor swarms. | MIT | [EN](categories/agent-skill-collections/personal-collections/dimillian-skills.md) · [中](categories/agent-skill-collections/personal-collections/dimillian-skills.zh.md) |
| **gstack** | Garry Tan's personal Claude Code setup: ~23 opinionated slash-command skills that role-play a virtual engineering team (CEO review, designer, eng-manager, QA, security officer) across a plan-build-review-ship-retro loop. | MIT | [EN](categories/agent-skill-collections/personal-collections/gstack.md) · [中](categories/agent-skill-collections/personal-collections/gstack.zh.md) |
| **andrej-karpathy-skills** | A single behavioral-guidelines pack — one CLAUDE.md (plus a Cursor variant and a thin skills wrapper) distilling Karpathy's four LLM-coding principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) into Claude Code / Cursor. | MIT | [EN](categories/agent-skill-collections/personal-collections/karpathy-skills.md) · [中](categories/agent-skill-collections/personal-collections/karpathy-skills.zh.md) |
| **Khazix Skills** | A small personal collection of five SKILL.md-format Agent Skills from 数字生命卡兹克 (Khazix) — disk cleanup, AI-news lookup, doc/memory reconciliation, long-form research reports, and WeChat-style writing — for SKILL.md-capable agents. | MIT | [EN](categories/agent-skill-collections/personal-collections/khazix-skills.md) · [中](categories/agent-skill-collections/personal-collections/khazix-skills.zh.md) |
| **ljg-skills** | Li Jigang's personal Claude Code skill collection (20+ skills) for Chinese knowledge work — reading, paper/book deconstruction, concept analysis, plain-language rewriting, and rendering content into visual PNG cards, installed via the skills CLI. | NOASSERTION | [EN](categories/agent-skill-collections/personal-collections/ljg-skills.md) · [中](categories/agent-skill-collections/personal-collections/ljg-skills.zh.md) |
| **PUA** | A high-agency persona skill pack that frames your coding agent as a P8 engineer on a 30-day PIP, using corporate-PUA/PIP rhetoric to push it to exhaust debugging approaches instead of giving up early. | MIT | [EN](categories/agent-skill-collections/personal-collections/pua.md) · [中](categories/agent-skill-collections/personal-collections/pua.zh.md) |
| **Qiushi-Skill** | A methodology skill pack arming a coding agent with "seek truth from facts" plus nine dialectical-materialist thinking tools (contradiction analysis, investigation-first, practice-cognition, etc.), installable across Claude Code/Cursor/Codex/OpenCode via an npx installer. | MIT | [EN](categories/agent-skill-collections/personal-collections/qiushi-skill.md) · [中](categories/agent-skill-collections/personal-collections/qiushi-skill.zh.md) |
| **shaping-skills** | Ryan Singer's personal Claude Code skill pack that brings Shape Up "shaping" — problem framing, breadboarding, and framing/kickoff docs — into your coding agent so the AI helps define what to build before any code is written. | NOASSERTION | [EN](categories/agent-skill-collections/personal-collections/shaping-skills.md) · [中](categories/agent-skill-collections/personal-collections/shaping-skills.zh.md) |
| **TÂCHES CC Resources** | A personal, opinionated Claude Code bundle from TÂCHES (glittercowboy): ~27 slash commands, 9 skills (mostly meta-generators for building new commands/skills/subagents/hooks/MCP servers), 3 auditor subagents, and hooks — installable as one marketplace plugin. | MIT | [EN](categories/agent-skill-collections/personal-collections/taches-cc-resources.md) · [中](categories/agent-skill-collections/personal-collections/taches-cc-resources.zh.md) |

### observability

| Project | Use when | License | Page |
|---|---|---|---|
| **Grafana** | Use it when you need one dashboard + alerting layer over Prometheus/Loki/Elasticsearch and other sources — it visualizes, it doesn't store. | AGPL-3.0 | [EN](categories/observability/grafana.md) · [中](categories/observability/grafana.zh.md) |

### data-visualization

| Project | Use when | License | Page |
|---|---|---|---|
| **Apache Superset** | Use it when you want self-hosted SQL BI dashboards and exploration over a warehouse — not infra metrics/observability. | Apache-2.0 | [EN](categories/data-visualization/superset.md) · [中](categories/data-visualization/superset.zh.md) |

### ocr

| Project | Use when | License | Page |
|---|---|---|---|
| **Tesseract** | Use it when you need offline, embeddable OCR over clean printed text in 100+ languages — not wild photos or handwriting. | Apache-2.0 | [EN](categories/ocr/tesseract.md) · [中](categories/ocr/tesseract.zh.md) |
| **LaTeX-OCR (pix2tex)** | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. | MIT | [EN](categories/ocr/latex-ocr.md) · [中](categories/ocr/latex-ocr.zh.md) |

### document-parsing

| Project | Use when | License | Page |
|---|---|---|---|
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | MIT | [EN](categories/document-parsing/docling.md) · [中](categories/document-parsing/docling.zh.md) |

### diagramming

| Project | Use when | License | Page |
|---|---|---|---|
| **Mermaid** | Use it when you want diagrams as version-controlled plain text (flowchart/sequence/ER) rendered in Markdown and docs — not pixel-precise layouts. | MIT | [EN](categories/diagramming/mermaid.md) · [中](categories/diagramming/mermaid.zh.md) |
| **flowchart.js** | Use it when you want simple flowcharts authored as git-diffable text and rendered to SVG in the browser — but it only renders, depends on aging Raphael.js, and chokes on complex diagrams. | MIT | [EN](categories/diagramming/flowchart-js.md) · [中](categories/diagramming/flowchart-js.zh.md) |
| **bpmn-js** | Use it when business analysts must author or view standards-correct BPMN 2.0 diagrams inside your web app — but its license mandates a non-removable bpmn.io watermark, so confirm terms before white-labeling. | MIT + bpmn.io watermark clause | [EN](categories/diagramming/bpmn-js.md) · [中](categories/diagramming/bpmn-js.zh.md) |
### media-download

| Project | Use when | License | Page |
|---|---|---|---|
| **youtube-dl** | Use it when you need a battle-tested CLI/library to download video & audio from YouTube and 1000+ sites — but prefer the active yt-dlp fork for hot sites. | Unlicense | [EN](categories/media-download/youtube-dl.md) · [中](categories/media-download/youtube-dl.zh.md) |
| **you-get** | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. | MIT | [EN](categories/media-download/you-get.md) · [中](categories/media-download/you-get.zh.md) |
| **cobalt** | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. | AGPL-3.0 | [EN](categories/media-download/cobalt.md) · [中](categories/media-download/cobalt.zh.md) |
| **lux** | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. | MIT | [EN](categories/media-download/lux.md) · [中](categories/media-download/lux.zh.md) |
| **youtube-transcript-api** | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. | MIT | [EN](categories/media-download/youtube-transcript-api.md) · [中](categories/media-download/youtube-transcript-api.zh.md) |
| **bulk-downloader-for-reddit** | Use it when you want a scriptable, reproducible Reddit archive of files plus metadata via OAuth — but Reddit's ~1000-post listing cap is unbypassable, and releases have stalled since early 2023 (GPL-3.0). | GPL-3.0 | [EN](categories/media-download/bulk-downloader-for-reddit.md) · [中](categories/media-download/bulk-downloader-for-reddit.zh.md) |
### media-processing

| Project | Use when | License | Page |
|---|---|---|---|
| **FFmpeg** | Use it when you must decode/encode/transcode/filter virtually any audio or video in a pipeline — mind the LGPL→GPL build trap. | LGPL-2.1-or-later | [EN](categories/media-processing/ffmpeg.md) · [中](categories/media-processing/ffmpeg.zh.md) |
| **ffmpeg-python** | Use it when you're scripting complex FFmpeg filter graphs in Python and want readable DAG code instead of write-only -filter_complex strings — but it's coasting since 2024, single-maintainer, and still needs the ffmpeg binary installed. | Apache-2.0 | [EN](categories/media-processing/ffmpeg-python.md) · [中](categories/media-processing/ffmpeg-python.zh.md) |
| **VMAF** | Use it when you're tuning an encoding ladder and need a perceptual 0-100 score to compare codecs/presets the way the industry does — but it's full-reference only, and picking the wrong model silently invalidates cross-version comparisons. | BSD-2-Clause-Patent | [EN](categories/media-processing/vmaf.md) · [中](categories/media-processing/vmaf.zh.md) |
| **m3u8** | Use it when you must parse or rewrite HLS .m3u8 manifests programmatically as a typed object model rather than regex — but it's Python-only, HLS-specific, and quiet since 2025 so the newest rfc8216bis tags may lag. | MIT | [EN](categories/media-processing/m3u8.md) · [中](categories/media-processing/m3u8.zh.md) |
| **ffsubsync** | Use it when a subtitle file is off by a constant global offset and you want one-command FFT audio-sync without manual sync points — but it can't fix per-line/variable drift inside the content, and it's single-maintainer. | MIT | [EN](categories/media-processing/ffsubsync.md) · [中](categories/media-processing/ffsubsync.zh.md) |
### llm-chat-ui

| Project | Use when | License | Page |
|---|---|---|---|
| **NextChat** | Use it when you want a private, self-deployable multi-provider AI chat UI across web/desktop/mobile — not a multi-user RBAC team platform. | MIT | [EN](categories/llm-chat-ui/nextchat.md) · [中](categories/llm-chat-ui/nextchat.zh.md) |

### markdown-tools

| Project | Use when | License | Page |
|---|---|---|---|
| **Markdown Here** | Use it when you want to write email in Markdown and render it before sending via a browser/Thunderbird extension — mind its slow maintenance. | MIT | [EN](categories/markdown-tools/markdown-here.md) · [中](categories/markdown-tools/markdown-here.zh.md) |
| **marked** | Use it when you need a fast, low-level Markdown→HTML parser in JS — but you must sanitize the output yourself and don't need strict CommonMark. | MIT | [EN](categories/markdown-tools/marked.md) · [中](categories/markdown-tools/marked.zh.md) |

### pdf-tools

| Project | Use when | License | Page |
|---|---|---|---|
| **PDF.js** | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. | Apache-2.0 | [EN](categories/pdf-tools/pdfjs.md) · [中](categories/pdf-tools/pdfjs.zh.md) |

### workflow-orchestration

| Project | Use when | License | Page |
|---|---|---|---|
| **Apache Airflow** | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. | Apache-2.0 | [EN](categories/workflow-orchestration/airflow.md) · [中](categories/workflow-orchestration/airflow.zh.md) |
| **Gaia** | Use it when studying the "pipelines-as-compiled-plugins" design as a read-only reference — the repo is archived and abandoned, never pick it for new production work. | Apache-2.0 | [EN](categories/workflow-orchestration/gaia.md) · [中](categories/workflow-orchestration/gaia.zh.md) |
| **Airflow Maintenance DAGs** | Use it when self-managed Airflow needs proven copy-in DAGs to clean metadata-DB rows and stale logs — they run destructive DELETEs tied to version-specific internals, so dry-run and back up first. | Apache-2.0 | [EN](categories/workflow-orchestration/airflow-maintenance-dags.md) · [中](categories/workflow-orchestration/airflow-maintenance-dags.zh.md) |
### llm-inference

| Project | Use when | License | Page |
|---|---|---|---|
| **Modular Platform (MAX + Mojo)** | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. | Apache-2.0 (mixed) | [EN](categories/llm-inference/modular.md) · [中](categories/llm-inference/modular.zh.md) |
| **omlx** | Use it when you want a Mac (Apple Silicon) local LLM inference server on MLX with SSD-tiered KV caching — a young single-maintainer repo with a suspicious star count. | Apache-2.0 | [EN](categories/llm-inference/omlx.md) · [中](categories/llm-inference/omlx.zh.md) |

### task-queue

| Project | Use when | License | Page |
|---|---|---|---|
| **XXL-JOB** | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. | GPL-3.0 | [EN](categories/task-queue/xxl-job.md) · [中](categories/task-queue/xxl-job.zh.md) |
| **Celery** | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. | BSD-3-Clause | [EN](categories/task-queue/celery.md) · [中](categories/task-queue/celery.zh.md) |
| **Kombu** | Use it when a Python service must publish/consume messages across swappable brokers (RabbitMQ, Redis, SQS) — virtual transports emulate AMQP imperfectly, so "swap the URL" is not identical behavior. | BSD-3-Clause | [EN](categories/task-queue/kombu.md) · [中](categories/task-queue/kombu.zh.md) |
| **Flower** | Use it when a production Celery cluster needs a live dashboard to inspect and control workers and export Prometheus metrics — it can revoke tasks, so never expose it unauthenticated. | BSD-3-Clause | [EN](categories/task-queue/flower.md) · [中](categories/task-queue/flower.zh.md) |
### im-automation

| Project | Use when | License | Page |
|---|---|---|---|
| **ItChat** | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. | MIT | [EN](categories/im-automation/itchat.md) · [中](categories/im-automation/itchat.zh.md) |
| **WeChatPlugin-MacOS** | Avoid for current WeChat — a macOS WeChat.app binary tweak that breaks on every WeChat update and is ~2y idle; account-ban & security risk. | MIT | [EN](categories/im-automation/wechatplugin-macos.md) · [中](categories/im-automation/wechatplugin-macos.zh.md) |
| **wxpy** | Study it only as legacy WeChat-bot code — archived since 2019 and built on the now-defunct WeChat web protocol, so it mostly doesn't work. | MIT | [EN](categories/im-automation/wxpy.md) · [中](categories/im-automation/wxpy.zh.md) |
| **wxappUnpacker** | Use it when you must decompile a WeChat .wxapkg bundle you own back into readable source — but this exact repo is an empty tombstone, so grab a live fork instead. | GPL-3.0-or-later | [EN](categories/im-automation/wxappunpacker.md) · [中](categories/im-automation/wxappunpacker.zh.md) |
| **Douyin-Bot** | Use it only as a historical reference for ADB screen-coordinate phone automation — never deploy it, its 2018 coordinates and dead Tencent face API mean it no longer works. | MIT | [EN](categories/im-automation/douyin-bot.md) · [中](categories/im-automation/douyin-bot.zh.md) |
### web-ui

| Project | Use when | License | Page |
|---|---|---|---|
| **Driver.js** | Use it when you want a tiny, dependency-free product tour / feature-spotlight on a web page — not a full onboarding platform. | MIT | [EN](categories/web-ui/driver-js.md) · [中](categories/web-ui/driver-js.zh.md) |

### proxy-pool

| Project | Use when | License | Page |
|---|---|---|---|
| **proxy_pool** | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. | MIT | [EN](categories/proxy-pool/proxy-pool.md) · [中](categories/proxy-pool/proxy-pool.zh.md) |
| **ProxyBroker** | Use it when you need a throwaway pool of free public proxies for a low-stakes prototype via a single rotating local endpoint — but it's effectively frozen since ~2018 and widely breaks on modern Python without pinning. | Apache-2.0 | [EN](categories/proxy-pool/proxybroker.md) · [中](categories/proxy-pool/proxybroker.zh.md) |
| **Scylla** | Use it when you want an always-on, self-hosted free-proxy pool with a JSON API, quality scoring, and dashboard via one Docker command — but its forward proxy can't do HTTPS, and releases stalled since 2022. | Apache-2.0 | [EN](categories/proxy-pool/scylla.md) · [中](categories/proxy-pool/scylla.zh.md) |
| **haipproxy** | Use it when you genuinely need a distributed, high-availability free-proxy pool for large multi-machine crawls on Scrapy+Redis — but it's dormant since 2022, runs 2018-era Py2/3 code, and is the heaviest pool to operate. | MIT | [EN](categories/proxy-pool/haipproxy.md) · [中](categories/proxy-pool/haipproxy.zh.md) |
### debugging-proxy

| Project | Use when | License | Page |
|---|---|---|---|
| **whistle** | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. | MIT | [EN](categories/debugging-proxy/whistle.md) · [中](categories/debugging-proxy/whistle.zh.md) |
| **AnyProxy** | Use it when you want a scriptable Node.js MITM proxy to inspect and rewrite HTTP/HTTPS traffic in plain JS rules — but master is frozen since 2020, so prefer whistle for new work. | Apache-2.0 | [EN](categories/debugging-proxy/anyproxy.md) · [中](categories/debugging-proxy/anyproxy.zh.md) |
### web-scraping

| Project | Use when | License | Page |
|---|---|---|---|
| **newspaper** | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. | MIT | [EN](categories/web-scraping/newspaper.md) · [中](categories/web-scraping/newspaper.zh.md) |
| **requests-html** | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. | MIT | [EN](categories/web-scraping/requests-html.md) · [中](categories/web-scraping/requests-html.zh.md) |


### auth

| Project | Use when | License | Page |
|---|---|---|---|
| **Authomatic** | Use it when a framework-agnostic Python app needs thin "sign in with X" via OAuth1/OAuth2/OpenID, leaving session persistence to you — but it's low-velocity and an auth lib's slow fix cadence is a security risk. | MIT | [EN](categories/auth/authomatic.md) · [中](categories/auth/authomatic.zh.md) |
| **django-rules** | Use it when Django object-level permissions are computed from logic (predicates), not stored grants, with no DB tables — but if admins must assign per-object permissions at runtime you need django-guardian instead. | MIT | [EN](categories/auth/django-rules.md) · [中](categories/auth/django-rules.zh.md) |

### databases

| Project | Use when | License | Page |
|---|---|---|---|
| **PikiwiDB** | Use it when a large Redis dataset has blown past RAM and memory cost dominates — RocksDB-backed, Redis-protocol, so one node holds hundreds of GB; but it trades latency for capacity, wrong if every op must be microsecond-fast. | BSD-3-Clause | [EN](categories/databases/pikiwidb.md) · [中](categories/databases/pikiwidb.zh.md) |
| **elasticsearch-dsl-py** | Use it when you maintain legacy Python code pinned to the standalone elasticsearch-dsl package — for any new project it's archived, so install elasticsearch>=8.18 and use elasticsearch.dsl instead. | Apache-2.0 | [EN](categories/databases/elasticsearch-dsl-py.md) · [中](categories/databases/elasticsearch-dsl-py.zh.md) |
| **elasticsearch-sql** | Use it when a SQL-fluent team needs to query Elasticsearch without learning the JSON Query DSL — but Elastic's first-party SQL/ES\|QL now overlaps it, so prefer the vendor feature when it covers you. | Apache-2.0 | [EN](categories/databases/elasticsearch-sql.md) · [中](categories/databases/elasticsearch-sql.zh.md) |
| **go-mysql-elasticsearch** | Use it when you want a single Go binary to tail MySQL binlog and sync one direction into Elasticsearch at modest scale — but it's unmaintained since 2023 with no releases, so treat it as fork-and-own. | MIT | [EN](categories/databases/go-mysql-elasticsearch.md) · [中](categories/databases/go-mysql-elasticsearch.zh.md) |
| **python-mysql-replication** | Use it when you want a pure-Python primitive to stream MySQL binlog as typed events and build a custom CDC loop with full control — but checkpointing, dedup and exactly-once delivery are entirely on you. | Apache-2.0 | [EN](categories/databases/python-mysql-replication.md) · [中](categories/databases/python-mysql-replication.zh.md) |
| **PrettyZoo** | Use it when you need a friendly desktop GUI to browse and lightly edit a ZooKeeper znode tree during dev or incident triage — but it's archived since 2023, so new JDK/macOS may break it with no upstream fix. | Apache-2.0 | [EN](categories/databases/prettyzoo.md) · [中](categories/databases/prettyzoo.zh.md) |
| **RDR** | Use it when a Redis instance trips its maxmemory alarm and you need offline, fast per-prefix analysis of an RDB snapshot — but figures are approximate and the tool is coasting (v0.0.1, 2019). | Apache-2.0 | [EN](categories/databases/rdr.md) · [中](categories/databases/rdr.zh.md) |

### desktop-automation

| Project | Use when | License | Page |
|---|---|---|---|
| **PyAutoGUI** | Use it when you must script a desktop app with no API across Windows/macOS/Linux — but coordinate/pixel automation breaks silently on resolution, DPI, or theme changes, and dev has coasted since 2024. | BSD-3-Clause | [EN](categories/desktop-automation/pyautogui.md) · [中](categories/desktop-automation/pyautogui.zh.md) |

### game-dev

| Project | Use when | License | Page |
|---|---|---|---|
| **pygame** | Use it when you want to learn or ship a small 2D Python game with a simple loop — but for 3D or performance-critical work it bottlenecks, look elsewhere. | LGPL-2.1 | [EN](categories/game-dev/pygame.md) · [中](categories/game-dev/pygame.zh.md) |

### kafka-tools

| Project | Use when | License | Page |
|---|---|---|---|
| **UI for Apache Kafka (provectus/kafka-ui)** | Use it when you want a one-`docker run` web dashboard to browse Kafka brokers, topics, and consumer-group lag — but this `provectus` upstream is stalled (last release 2024-04); deploy the maintained `kafbat/kafka-ui` fork instead. | Apache-2.0 | [EN](categories/kafka-tools/kafka-ui.md) · [中](categories/kafka-tools/kafka-ui.zh.md) |
| **kafka-python** | Use it when you want a pure-Python Kafka client that just `pip install`s with no librdkafka to compile — but a pure-Python client can't match `confluent-kafka`'s throughput and may trail the newest broker features. | Apache-2.0 | [EN](categories/kafka-tools/kafka-python.md) · [中](categories/kafka-tools/kafka-python.zh.md) |

### networking

| Project | Use when | License | Page |
|---|---|---|---|
| **Paramiko** | Use it when Python code must open SSH/SFTP connections and run remote commands programmatically — but it's pure-Python (slower than OpenSSH), threading-only, and LGPL-2.1. | LGPL-2.1 | [EN](categories/networking/paramiko.md) · [中](categories/networking/paramiko.zh.md) |
| **sshtunnel** | Use it when a Python script needs a clean context-managed SSH port-forward to a service behind a bastion — but it has no auto-reconnect and is low-activity (0.4.0, 2021). | MIT | [EN](categories/networking/sshtunnel.md) · [中](categories/networking/sshtunnel.zh.md) |
| **dnspython** | Use it when Python needs arbitrary record types, custom resolvers, zone transfers, DNSSEC, or DoH/DoT — but it bypasses /etc/hosts and the OS resolver, requires Python 3.10+, and is a library not a CLI. | ISC | [EN](categories/networking/dnspython.md) · [中](categories/networking/dnspython.zh.md) |
| **wondershaper** | Use it when one Linux NIC needs a quick up/down bandwidth ceiling without hand-writing tc rules — but it's HTB-era (not bufferbloat-aware like cake/fq_codel) and Linux-only, coasting since 2024-07. | GPL-2.0 | [EN](categories/networking/wondershaper.md) · [中](categories/networking/wondershaper.zh.md) |
| **ThriftPy** | Use it only to understand a legacy service still importing thriftpy before migrating — the repo is archived and deprecated, so all new Thrift work should go to the maintained thriftpy2. | MIT | [EN](categories/networking/thriftpy.md) · [中](categories/networking/thriftpy.zh.md) |

### nginx-modules

| Project | Use when | License | Page |
|---|---|---|---|
| **lua-nginx-module (ngx_lua)** | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. | BSD-2-Clause | [EN](categories/nginx-modules/lua-nginx-module.md) · [中](categories/nginx-modules/lua-nginx-module.zh.md) |
| **lua-resty-redis** | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. | BSD-2-Clause | [EN](categories/nginx-modules/lua-resty-redis.md) · [中](categories/nginx-modules/lua-resty-redis.zh.md) |
| **nginx-upload-module** | Use it when you want NGINX to stream large multipart uploads to disk and hand your backend just file metadata — but you're compiling an aging, single-maintainer C fork (last push 2024-07); direct-to-S3 presigned uploads often beat it now. | BSD-3-Clause | [EN](categories/nginx-modules/nginx-upload-module.md) · [中](categories/nginx-modules/nginx-upload-module.zh.md) |

### python-tooling

| Project | Use when | License | Page |
|---|---|---|---|
| **Cython** | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. | Apache-2.0 | [EN](categories/python-tooling/cython.md) · [中](categories/python-tooling/cython.zh.md) |
| **pyrasite** | Use it when you must inject diagnostic code into a stuck or leaking live Python process you can't restart — but injection can crash the target, treat it as incident-only. | GPL-3.0 | [EN](categories/python-tooling/pyrasite.md) · [中](categories/python-tooling/pyrasite.zh.md) |
| **gophernotes** | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. | MIT | [EN](categories/python-tooling/gophernotes.md) · [中](categories/python-tooling/gophernotes.zh.md) |
| **GRequests** | Use it when you want to make existing synchronous `requests` code concurrent with minimal diff via `map()` — but gevent monkeypatches the stdlib and can collide with your stack. | BSD-2-Clause | [EN](categories/python-tooling/grequests.md) · [中](categories/python-tooling/grequests.zh.md) |

### reading-tools

| Project | Use when | License | Page |
|---|---|---|---|
| **NetNewsWire** | Use it when you read many feeds on Mac/iPhone and want a fast, ad-free native RSS client you own — but only on Apple platforms, never elsewhere. | MIT | [EN](categories/reading-tools/netnewswire.md) · [中](categories/reading-tools/netnewswire.zh.md) |
| **Just Read** | Use it when you want to strip ads and clutter from an article in-browser, your way, with per-site selectors — but it's EULA-licensed source, not real OSS. | Unlicensed (EULA) | [EN](categories/reading-tools/just-read.md) · [中](categories/reading-tools/just-read.zh.md) |

### speech

| Project | Use when | License | Page |
|---|---|---|---|
| **SpeechBrain** | Use it when you need to train and adapt speech models (ASR, speaker ID, separation) on one coherent PyTorch recipe codebase — but it's research-and-training-first, so production serving and cross-version API stability are your job. | Apache-2.0 | [EN](categories/speech/speechbrain.md) · [中](categories/speech/speechbrain.zh.md) |

### terminal-ui

| Project | Use when | License | Page |
|---|---|---|---|
| **colorama** | Use it when a Python CLI needs ANSI colored output that also works on legacy Windows consoles — but it's only a color/style shim (no tables, TUI, or guaranteed truecolor) and largely a no-op on modern terminals. | BSD-3-Clause | [EN](categories/terminal-ui/colorama.md) · [中](categories/terminal-ui/colorama.zh.md) |
| **asciimatics** | Use it when you need a cross-platform full-screen Python TUI plus an ASCII animation engine on Linux/macOS/Windows — but the widget set is spartan, the API older-style, and it's single-maintainer. | Apache-2.0 | [EN](categories/terminal-ui/asciimatics.md) · [中](categories/terminal-ui/asciimatics.zh.md) |
| **Terminal Markdown Viewer (mdv)** | Use it when you want one-shot read-only Markdown rendered with color/syntax-highlighting in a plain terminal over SSH — but it's low-activity (0.x, 2024-05) and glow/mdcat are the modern defaults. | BSD-3-Clause | [EN](categories/terminal-ui/terminal-markdown-viewer.md) · [中](categories/terminal-ui/terminal-markdown-viewer.zh.md) |
| **ART** | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. | MIT | [EN](categories/terminal-ui/art.md) · [中](categories/terminal-ui/art.zh.md) |
| **asciify** | Use it as a minimal, legible copy-paste reference for the image-to-ASCII algorithm — but it ships NO license (all rights reserved), is unmaintained since 2022, so never vendor it into a product. | NONE | [EN](categories/terminal-ui/asciify.md) · [中](categories/terminal-ui/asciify.zh.md) |

Categories follow the tree in [INDEX.md](INDEX.md).
| **Readability.js** | Use it when you need to strip a web page down to just the article (title, byline, body) using Firefox Reader View's battle-tested engine — but it parses a DOM you supply; it won't fetch URLs or render JS-heavy SPAs. | Apache-2.0 | [EN](categories/web-scraping/readability-js.md) · [中](categories/web-scraping/readability-js.zh.md) |
| **python-readability** | Use it when your Python pipeline needs fast lxml article extraction from already-fetched HTML with no browser or Node — but it's single-maintainer and slow-cadence, and trafilatura often scores better on extraction benchmarks. | Apache-2.0 | [EN](categories/web-scraping/python-readability.md) · [中](categories/web-scraping/python-readability.zh.md) |
| **dragnet** | Use it when you have labeled data and want a trainable ML extractor that also separates article from user comments — but it's near-dormant with aging pins (`scikit-learn<0.21`, `ftfy<5`) that make installing on modern stacks painful. | MIT | [EN](categories/web-scraping/dragnet.md) · [中](categories/web-scraping/dragnet.zh.md) |
| **boilerpipe** | Use it when you specifically need a JVM-native, dependency-light classic-algorithm article extractor — but the repo is effectively abandoned (last push 2018-01) with aged vendored deps and no security fixes coming. | Apache-2.0 | [EN](categories/web-scraping/boilerpipe.md) · [中](categories/web-scraping/boilerpipe.zh.md) |
| **fuck-login** | Use it when you want to read 2016-era examples of how site logins (CSRF/RSA/captcha) were scripted — but it's abandoned since 2018, unlicensed, and the scripts are broken today. | NONE | [EN](categories/web-scraping/fuck-login.md) · [中](categories/web-scraping/fuck-login.zh.md) |
| **gopup** | Use it when you need a quick one-line pull of Chinese public data (search indices, CPI, Shibor) into a pandas DataFrame for academic research — but it's coasting since 2023, unlicensed, and scrapers rot as sources change. | NONE | [EN](categories/web-scraping/gopup.md) · [中](categories/web-scraping/gopup.zh.md) |
| **PRAW** | Use it when your data source is Reddit and you want the official OAuth-compliant path with rate-limit handling built in — but Reddit's own API terms, quotas, and pricing bound what you can do, not the library. | BSD-2-Clause | [EN](categories/web-scraping/praw.md) · [中](categories/web-scraping/praw.zh.md) |
| **Scrapyd** | Use it when you need to deploy local Scrapy spiders to a server and drive scheduled, versioned crawls over an HTTP API — but it only runs Scrapy and ships unauthenticated, so add auth before exposing port 6800. | BSD-3-Clause | [EN](categories/web-scraping/scrapyd.md) · [中](categories/web-scraping/scrapyd.zh.md) |
| **SpiderKeeper** | Use it when a small team running Scrapyd wants the simplest browser dashboard to deploy and cron-schedule spiders — but it's stale since 2023 with default admin/admin auth, so don't expose it untrusted. | MIT | [EN](categories/web-scraping/spiderkeeper.md) · [中](categories/web-scraping/spiderkeeper.zh.md) |
## Why this exists

Most OSS READMEs are marketing: they tell you what a project does and why it's great. They do
**not** tell you when *not* to use it, how it compares to alternatives, or what it costs to
operate. An agent doing selection needs exactly that negative space. oss-atlas inverts the
README genre into a **decision-support** genre.

The index is deliberately **weak** — no database, no search, no embeddings. Just Markdown that
an agent reads and reasons over. The directory structure *is* the query API.

## Selection signals & heuristics

Choosing OSS is a bet on the future, not just a feature match. Every page carries a
**`Health & viability`** section — a dated, labeled verdict on whether the project is worth betting
on: maintenance cadence, governance & bus factor, backing org, adoption/ecosystem, and risk flags
(relicense history, open-core gating, CVEs). Read it alongside `When NOT to use`.

One prior deserves a name — the **Lindy effect**: for non-perishable things (software, formats,
tools), expected *remaining* life grows with current age. A project **actively maintained** for 12
years is a safer long-term bet than one that exploded in 6 months. Treat it as a prior, not a law,
and always as **age × still-active**: it discounts young-but-hyped repos (suspicious stars, unproven)
and does **not** rescue old **abandoned** ones (age alone ≠ alive); it can also mislead across
paradigm shifts. Pages record the project's **age** so the prior is checkable. [推断: the Lindy
framing is a heuristic, not a guarantee of any specific project's survival.]

## Structure (recursive tree, bilingual)

```
INDEX.md / INDEX.zh.md                        # root: category route (EN / 中)
categories/<cat>/INDEX.md / INDEX.zh.md       # a category node: pages + sub-categories
categories/<cat>/<subcat>/INDEX.md …          # deeper nodes — the tree self-balances as it grows
…/<slug>.md  +  …/<slug>.zh.md                # a leaf: the EN selection page + its 中文 sibling
```

`categories/` is a **recursive, self-balancing tree**: when a category gets too many projects it
splits into sub-categories (the linter WARNs; `refactor-index` does the split). English is the
agent-canonical path; the `.zh.md` sibling is the same content in Chinese.

### Anatomy of a project page

Each page = **YAML frontmatter (facts, dated)** + **Markdown body (judgment)**. The two are kept
apart on purpose: facts go stale and get re-verified (`last_verified`); judgment is opinion and is
labeled (`[未验证]` / `[推断]`), never asserted as eternal truth.

**Frontmatter** (identical across the EN/中 pair — facts are language-neutral):
`name · slug · repo · category · tags · language · license · maturity` (dated) · `last_verified` · `type`
(`tool | library | app | framework | service | model | skill-pack`).

**Body sections** (the exact set depends on `type`):

| Section (EN / 中) | Required for | What it carries |
|---|---|---|
| `When to use` / `何时使用` | all types | a **User Story** — a concrete second-person scenario, not a feature list |
| `When NOT to use` / `何时不用` | all types | the decisive filter: anti-patterns, scale ceilings, lock-in, maintenance risk |
| `Comparison` / `横向对比` | all types | a table vs real substitutes (`未收录` when an alternative isn't indexed yet) |
| `Tech stack` / `技术栈` | non-`skill-pack` | languages, frameworks, datastores it's built on |
| `Dependencies` / `依赖` | non-`skill-pack` | runtime/infra you must run (db, services, hardware) |
| `Ops difficulty` / `运维难度` | non-`skill-pack` | low / medium / high + why |
| `Health & viability` / `健康度与可持续性` | all types | dated viability verdict — maintenance, governance/bus-factor, backing, **age × Lindy**, adoption, risk flags |
| `Caveats (unverified)` / `存疑（未验证）` | all types | the uncertainty ledger — one `[未验证]`/`[推断]` bullet per unverified fact |

The full contract is [tools/schema.md](tools/schema.md); the linter ([tools/lint.py](tools/lint.py))
enforces this shape (sections, bilingual parity, fullwidth Chinese punctuation, README parity).

## Freshness

Facts go stale. Every page records `last_verified`. The linter warns when an entry is older
than 90 days; the `sync-entry` skill re-verifies it against the live repo. Treat any fact as a
**point-in-time** snapshot, labeled per the truth discipline (`[未验证]` / `[推断]`).

## Contributing

The unit of inclusion is a **git repository** — any real open-source repo, across any domain. Not
added: non-repos (hosted SaaS, landing pages, articles), exact duplicates, empty repos. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [tools/schema.md](tools/schema.md).

```bash
python3 tools/lint.py    # the structural gate; no unit tests (it's a content repo)
```

Lint is a **structural** gate (frontmatter keys + bilingual parity, required/forbidden sections per
`type`, H1, links, Caveats ledger, fanout) — not a **semantic** one. `lint clean` means the shape is
right, not that the prose was reviewed for accuracy or selection quality.

## License

- **Tooling** (code, e.g. `tools/lint.py`): MIT — see [LICENSE](LICENSE).
- **Content** (prose under `categories/`, routing pages, docs): CC BY 4.0 — see
  [LICENSE-CONTENT](LICENSE-CONTENT).

Profiles describe third-party projects owned by their respective authors and governed by their
own licenses; the CC BY 4.0 grant covers only the original analysis here.
