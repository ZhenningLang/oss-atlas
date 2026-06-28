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

### llm-training

| Project | Use when | License | Page |
|---|---|---|---|
| **LlamaFactory** | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. | Apache-2.0 | [EN](categories/llm-training/llamafactory.md) · [中](categories/llm-training/llamafactory.zh.md) |
| **Unsloth** | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. | Apache-2.0 | [EN](categories/llm-training/unsloth.md) · [中](categories/llm-training/unsloth.zh.md) |
| **ART (Agent Reinforcement Trainer)** | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. | Apache-2.0 | [EN](categories/llm-training/art.md) · [中](categories/llm-training/art.zh.md) |
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

### llm-eval

| Project | Use when | License | Page |
|---|---|---|---|
| **promptfoo** | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. | MIT | [EN](categories/llm-eval/promptfoo.md) · [中](categories/llm-eval/promptfoo.zh.md) |

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

### ml-research

| Project | Use when | License | Page |
|---|---|---|---|
| **autoresearch** | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. | MIT | [EN](categories/ml-research/autoresearch.md) · [中](categories/ml-research/autoresearch.zh.md) |
| **llm-circuit-finder** | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. | MIT | [EN](categories/ml-research/llm-circuit-finder.md) · [中](categories/ml-research/llm-circuit-finder.zh.md) |
| **CLIP** | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. | MIT | [EN](categories/ml-research/clip.md) · [中](categories/ml-research/clip.zh.md) |
| **TaskMatrix** | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. | MIT | [EN](categories/ml-research/taskmatrix.md) · [中](categories/ml-research/taskmatrix.zh.md) |

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

### document-parsing

| Project | Use when | License | Page |
|---|---|---|---|
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | MIT | [EN](categories/document-parsing/docling.md) · [中](categories/document-parsing/docling.zh.md) |

### diagramming

| Project | Use when | License | Page |
|---|---|---|---|
| **Mermaid** | Use it when you want diagrams as version-controlled plain text (flowchart/sequence/ER) rendered in Markdown and docs — not pixel-precise layouts. | MIT | [EN](categories/diagramming/mermaid.md) · [中](categories/diagramming/mermaid.zh.md) |

### media-download

| Project | Use when | License | Page |
|---|---|---|---|
| **youtube-dl** | Use it when you need a battle-tested CLI/library to download video & audio from YouTube and 1000+ sites — but prefer the active yt-dlp fork for hot sites. | Unlicense | [EN](categories/media-download/youtube-dl.md) · [中](categories/media-download/youtube-dl.zh.md) |
| **you-get** | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. | MIT | [EN](categories/media-download/you-get.md) · [中](categories/media-download/you-get.zh.md) |
| **cobalt** | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. | AGPL-3.0 | [EN](categories/media-download/cobalt.md) · [中](categories/media-download/cobalt.zh.md) |
| **lux** | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. | MIT | [EN](categories/media-download/lux.md) · [中](categories/media-download/lux.zh.md) |

### media-processing

| Project | Use when | License | Page |
|---|---|---|---|
| **FFmpeg** | Use it when you must decode/encode/transcode/filter virtually any audio or video in a pipeline — mind the LGPL→GPL build trap. | LGPL-2.1-or-later | [EN](categories/media-processing/ffmpeg.md) · [中](categories/media-processing/ffmpeg.zh.md) |

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

### llm-inference

| Project | Use when | License | Page |
|---|---|---|---|
| **Modular Platform (MAX + Mojo)** | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. | Apache-2.0 (mixed) | [EN](categories/llm-inference/modular.md) · [中](categories/llm-inference/modular.zh.md) |

### task-queue

| Project | Use when | License | Page |
|---|---|---|---|
| **XXL-JOB** | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. | GPL-3.0 | [EN](categories/task-queue/xxl-job.md) · [中](categories/task-queue/xxl-job.zh.md) |
| **Celery** | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. | BSD-3-Clause | [EN](categories/task-queue/celery.md) · [中](categories/task-queue/celery.zh.md) |

### im-automation

| Project | Use when | License | Page |
|---|---|---|---|
| **ItChat** | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. | MIT | [EN](categories/im-automation/itchat.md) · [中](categories/im-automation/itchat.zh.md) |

### web-ui

| Project | Use when | License | Page |
|---|---|---|---|
| **Driver.js** | Use it when you want a tiny, dependency-free product tour / feature-spotlight on a web page — not a full onboarding platform. | MIT | [EN](categories/web-ui/driver-js.md) · [中](categories/web-ui/driver-js.zh.md) |

### proxy-pool

| Project | Use when | License | Page |
|---|---|---|---|
| **proxy_pool** | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. | MIT | [EN](categories/proxy-pool/proxy-pool.md) · [中](categories/proxy-pool/proxy-pool.zh.md) |


Categories follow the tree in [INDEX.md](INDEX.md).

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
