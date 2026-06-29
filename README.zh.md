# oss-atlas

**一个面向 coding agent 的开源项目「选型」自然语言索引。**
agent 收到任务时读这个索引来挑开源项目——重点是衡量每个候选*何时不该用*，而不只是它能干什么。

> English README: [README.md](README.md)

## 安装

把 **`select-oss`** 这一个 skill 装进你的 coding agent —— 它教 agent 导航本索引、为任务选型。
默认通过 HTTP 读取公开索引（无需本地副本），在 clone 内也能直接读本地。

**任意 agent，经 [skills.sh](https://skills.sh)**（Claude Code、Codex、Cursor、OpenCode、Droid、
Kilo、Gemini CLI、Copilot 等 ~70 个 —— CLI 内置了每个 agent 的 skills 路径）：

```bash
# -g 装到全局（所有项目）；去掉 -g 则装到当前项目。用 -a 指定 agent，如 -a claude-code
npx skills add ZhenningLang/oss-atlas -g
```

**手动**（无 Node）—— 把 skill 目录拷进你 agent 的 skills 目录，以 Claude Code 为例：

```bash
git clone https://github.com/ZhenningLang/oss-atlas
cp -r oss-atlas/skills/select-oss ~/.claude/skills/
```

skill 从 `raw.githubusercontent.com/ZhenningLang/oss-atlas/main/` 拉取页面；只安装单个 `SKILL.md`，
因此体积极小、永远读到最新索引。对没有联网能力的 agent，skill 会回退到本地 clone。

## 项目总表

完整索引，按分类分组。每个项目有一份英文页（`<slug>.md`）和一份中文页（`<slug>.zh.md`），点击直达。交互式浏览见 [INDEX.zh.md](INDEX.zh.md)；agent 从 [AGENTS.md](AGENTS.md) 开始。

### agent-tooling

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **beads** | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 | MIT | [中](categories/agent-tooling/beads.zh.md) · [EN](categories/agent-tooling/beads.md) |
| **CCPM** | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 | MIT | [中](categories/agent-tooling/ccpm.zh.md) · [EN](categories/agent-tooling/ccpm.md) |
| **Entire** | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 | MIT | [中](categories/agent-tooling/entire-cli.zh.md) · [EN](categories/agent-tooling/entire-cli.md) |
| **Ralph for Claude Code** | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 | MIT | [中](categories/agent-tooling/ralph-claude-code.zh.md) · [EN](categories/agent-tooling/ralph-claude-code.md) |
| **Context Mode** | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 | Elastic-2.0 | [中](categories/agent-tooling/context-mode.zh.md) · [EN](categories/agent-tooling/context-mode.md) |
| **Planning with Files** | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 | MIT | [中](categories/agent-tooling/planning-with-files.zh.md) · [EN](categories/agent-tooling/planning-with-files.md) |
| **Vercel Skills** | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 | MIT | [中](categories/agent-tooling/vercel-skills.zh.md) · [EN](categories/agent-tooling/vercel-skills.md) |
| **OpenSandbox** | 当你需要自托管隔离沙箱、在 K8s 规模上运行不可信的 agent 生成代码（带出口管控和凭证保险库）时用它——但仓库仅数月之龄（2025-12 创建），其 API 与 Lindy 长期记录尚未经检验。 | Apache-2.0 | [中](categories/agent-tooling/opensandbox.zh.md) · [EN](categories/agent-tooling/opensandbox.md) |
| **AgentsView** | 当你同时跑多个编码 agent、想要本地优先的跨 agent 会话搜索与 token／成本分析时用它——但它问世仅数月、尚未到 1.0，要预期频繁变动。 | MIT | [中](categories/agent-tooling/agentsview.zh.md) · [EN](categories/agent-tooling/agentsview.md) |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI／review／冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | Apache-2.0 | [中](categories/agent-tooling/agent-orchestrator.zh.md) · [EN](categories/agent-tooling/agent-orchestrator.md) |
### document-management

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **paperless-ngx** | 想自托管对扫描纸质资料做 OCR + 打标签 + 全文检索时用它。 | GPL-3.0 | [中](categories/document-management/paperless-ngx.zh.md) · [EN](categories/document-management/paperless-ngx.md) |
| **copyparty** | 需要单文件便携、带断点续传/去重/多协议访问的文件服务器时用它——但它不做 OCR 文档检索。 | MIT | [中](categories/document-management/copyparty.zh.md) · [EN](categories/document-management/copyparty.md) |
| **Twake Drive** | 当你想在 Twake/Cozy 栈里要一个 Google-Drive 形态的自托管文件网盘（而非 OCR 归档）时用它。 | AGPL-3.0 | [中](categories/document-management/twake-drive.zh.md) · [EN](categories/document-management/twake-drive.md) |

### on-device-ml

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | Apache-2.0 | [中](categories/on-device-ml/litert-lm.zh.md) · [EN](categories/on-device-ml/litert-lm.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | MIT | [中](categories/on-device-ml/bitnet.zh.md) · [EN](categories/on-device-ml/bitnet.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | Apache-2.0 | [中](categories/on-device-ml/ai-edge-gallery.zh.md) · [EN](categories/on-device-ml/ai-edge-gallery.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | Apache-2.0 | [中](categories/on-device-ml/timesfm.zh.md) · [EN](categories/on-device-ml/timesfm.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | Apache-2.0 | [中](categories/on-device-ml/minicpm-v.zh.md) · [EN](categories/on-device-ml/minicpm-v.md) |

### web-automation

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | MIT | [中](categories/web-automation/page-agent.zh.md) · [EN](categories/web-automation/page-agent.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 | Apache-2.0 | [中](categories/web-automation/chrome-devtools-mcp.zh.md) · [EN](categories/web-automation/chrome-devtools-mcp.md) |
| **Cua** | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 | MIT | [中](categories/web-automation/cua.zh.md) · [EN](categories/web-automation/cua.md) |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | Apache-2.0 | [中](categories/web-automation/agent-browser.zh.md) · [EN](categories/web-automation/agent-browser.md) |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | Apache-2.0 | [中](categories/web-automation/selenium.zh.md) · [EN](categories/web-automation/selenium.md) |
| **PhantomJS** | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 | BSD-3-Clause | [中](categories/web-automation/phantomjs.zh.md) · [EN](categories/web-automation/phantomjs.md) |
| **Selenium Wire** | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 | MIT | [中](categories/web-automation/selenium-wire.zh.md) · [EN](categories/web-automation/selenium-wire.md) |
### llm-training

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **LlamaFactory** | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 | Apache-2.0 | [中](categories/llm-training/llamafactory.zh.md) · [EN](categories/llm-training/llamafactory.md) |
| **Unsloth** | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 | Apache-2.0 | [中](categories/llm-training/unsloth.zh.md) · [EN](categories/llm-training/unsloth.md) |
| **ART (Agent Reinforcement Trainer)** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | Apache-2.0 | [中](categories/llm-training/art.zh.md) · [EN](categories/llm-training/art.md) |
| **Agent Lightning** | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 | MIT | [中](categories/llm-training/agent-lightning.zh.md) · [EN](categories/llm-training/agent-lightning.md) |
| **Colossal-AI** | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 | Apache-2.0 | [中](categories/llm-training/colossalai.zh.md) · [EN](categories/llm-training/colossalai.md) |

### agent-frameworks

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | MIT | [中](categories/agent-frameworks/dspy.zh.md) · [EN](categories/agent-frameworks/dspy.md) |
| **AgentScope** | 要把多智能体 LLM 应用作为生产服务交付，需要沙箱工具、权限闸门、tracing 和人工介入时。 | Apache-2.0 | [中](categories/agent-frameworks/agentscope.zh.md) · [EN](categories/agent-frameworks/agentscope.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | Apache-2.0 OR MIT | [中](categories/agent-frameworks/openfang.zh.md) · [EN](categories/agent-frameworks/openfang.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | Apache-2.0 | [中](categories/agent-frameworks/symphony.zh.md) · [EN](categories/agent-frameworks/symphony.md) |
| **Claude Octopus** | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 | MIT | [中](categories/agent-frameworks/claude-octopus.zh.md) · [EN](categories/agent-frameworks/claude-octopus.md) |
| **oh-my-claudecode** | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 | MIT | [中](categories/agent-frameworks/oh-my-claudecode.zh.md) · [EN](categories/agent-frameworks/oh-my-claudecode.md) |
| **smolagents** | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 | Apache-2.0 | [中](categories/agent-frameworks/smolagents.zh.md) · [EN](categories/agent-frameworks/smolagents.md) |
| **Kilo Code** | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 | MIT | [中](categories/agent-frameworks/kilocode.zh.md) · [EN](categories/agent-frameworks/kilocode.md) |
| **Parlant** | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 | Apache-2.0 | [中](categories/agent-frameworks/parlant.zh.md) · [EN](categories/agent-frameworks/parlant.md) |
| **SkillOpt** | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 | MIT | [中](categories/agent-frameworks/skillopt.zh.md) · [EN](categories/agent-frameworks/skillopt.md) |
| **Open Interpreter** | 当你想要一个 Codex-fork 的终端编码 agent、带为低成本／开源模型（DeepSeek、Kimi、Qwen）调过的可切换 harness 时用它——不是老的 Python REPL（那个已迁到社区 fork），而且它是几周大的 0.0.x 重写、会执行代码。 | Apache-2.0 | [中](categories/agent-frameworks/open-interpreter.zh.md) · [EN](categories/agent-frameworks/open-interpreter.md) |
### agent-memory

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Mem0** | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 | Apache-2.0 | [中](categories/agent-memory/mem0.zh.md) · [EN](categories/agent-memory/mem0.md) |
| **Memori** | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 | Apache-2.0 | [中](categories/agent-memory/memori.zh.md) · [EN](categories/agent-memory/memori.md) |
| **Claude Subconscious** | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用（仅 demo，非生产）。 | MIT | [中](categories/agent-memory/claude-subconscious.zh.md) · [EN](categories/agent-memory/claude-subconscious.md) |
| **claude-mem** | 当你的编码 agent 跨会话丢失上下文、你想要本地 hook/MCP 捕获并压缩后再注入的记忆时用它（star 数存疑）。 | Apache-2.0 | [中](categories/agent-memory/claude-mem.zh.md) · [EN](categories/agent-memory/claude-mem.md) |

### deep-research

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **deep-research** | 想要一个极简可读、约 500 行的 TypeScript 深度研究 agent 作为 fork 底座时用它。 | MIT | [中](categories/deep-research/deep-research.zh.md) · [EN](categories/deep-research/deep-research.md) |
| **Vane** | 想要一个自托管、注重隐私的「Perplexity 式」带引用应答引擎，接你自己的 SearxNG 和自选 LLM 时用它。 | MIT | [中](categories/deep-research/vane.zh.md) · [EN](categories/deep-research/vane.md) |
| **Local Deep Research** | 当你需要一个自托管、可纯本地运行的深度研究 agent、把敏感查询留在自己机器上时用它。 | MIT | [中](categories/deep-research/local-deep-research.zh.md) · [EN](categories/deep-research/local-deep-research.md) |
| **Agent-Reach** | 当你的 agent 需要免付费 API 地读取和搜索网页与社交平台内容时用它。 | MIT | [中](categories/deep-research/agent-reach.zh.md) · [EN](categories/deep-research/agent-reach.md) |
| **MiroThinker** | 当你想要一个可在自有 GPU 上研究改造的自托管开源深研 Agent 时用它——但它要 GPU 集群加付费外部 API，且不到一岁、毫无 Lindy 沉淀。 | Apache-2.0 | [中](categories/deep-research/mirothinker.zh.md) · [EN](categories/deep-research/mirothinker.md) |
### ai-code-review

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Open Code Review** | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 | Apache-2.0 | [中](categories/ai-code-review/open-code-review.zh.md) · [EN](categories/ai-code-review/open-code-review.md) |
| **Claude Code Security Review** | 当你想用 Claude 在可信 PR 上做上下文感知的安全审查、且接受按 token 计费与非确定性结果时使用。 | MIT | [中](categories/ai-code-review/claude-code-security-review.zh.md) · [EN](categories/ai-code-review/claude-code-security-review.md) |
| **React Doctor** | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 | LicenseRef-Modified-MIT | [中](categories/ai-code-review/react-doctor.zh.md) · [EN](categories/ai-code-review/react-doctor.md) |

### rag-retrieval

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **FalkorDB** | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 | SSPL-1.0 | [中](categories/rag-retrieval/falkordb.zh.md) · [EN](categories/rag-retrieval/falkordb.md) |
| **graphify** | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 | MIT | [中](categories/rag-retrieval/graphify.zh.md) · [EN](categories/rag-retrieval/graphify.md) |
| **code-review-graph** | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及（blast-radius）的文件时用它。 | MIT | [中](categories/rag-retrieval/code-review-graph.zh.md) · [EN](categories/rag-retrieval/code-review-graph.md) |
| **PageIndex** | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 | MIT | [中](categories/rag-retrieval/pageindex.zh.md) · [EN](categories/rag-retrieval/pageindex.md) |
| **Understand-Anything** | 当你想把任意代码库变成可探索、可提问的知识图谱给 agent 用时用它——比 graphify 更年轻、未经检验。 | MIT | [中](categories/rag-retrieval/understand-anything.zh.md) · [EN](categories/rag-retrieval/understand-anything.md) |
| **FAISS** | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 | MIT | [中](categories/rag-retrieval/faiss.zh.md) · [EN](categories/rag-retrieval/faiss.md) |
| **text2vec** | 当你要为中文语义检索或 FAQ 匹配快速拿到句向量、只想一行 pip 装好时用它——它只是编码器，向量索引（FAISS／Milvus）得自己配。 | Apache-2.0 | [中](categories/rag-retrieval/text2vec.zh.md) · [EN](categories/rag-retrieval/text2vec.md) |
### llm-eval

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | MIT | [中](categories/llm-eval/promptfoo.zh.md) · [EN](categories/llm-eval/promptfoo.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | Apache-2.0 | [中](categories/llm-eval/pezzo.zh.md) · [EN](categories/llm-eval/pezzo.md) |
### agent-dev-methodology

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **12-Factor Agents** | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 | CC-BY-SA-4.0 (content) / Apache-2.0 (code examples) | [中](categories/agent-dev-methodology/12-factor-agents.zh.md) · [EN](categories/agent-dev-methodology/12-factor-agents.md) |
| **Superpowers** | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 | MIT | [中](categories/agent-dev-methodology/superpowers.zh.md) · [EN](categories/agent-dev-methodology/superpowers.md) |
| **SuperClaude Framework** | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 | MIT | [中](categories/agent-dev-methodology/superclaude.zh.md) · [EN](categories/agent-dev-methodology/superclaude.md) |
| **Get Shit Done (GSD)** | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 | MIT | [中](categories/agent-dev-methodology/get-shit-done.zh.md) · [EN](categories/agent-dev-methodology/get-shit-done.md) |
| **Compound Engineering** | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 | MIT | [中](categories/agent-dev-methodology/compound-engineering.zh.md) · [EN](categories/agent-dev-methodology/compound-engineering.md) |
| **ECC** | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 | MIT | [中](categories/agent-dev-methodology/ecc.zh.md) · [EN](categories/agent-dev-methodology/ecc.md) |

### ai-design-generation

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **HTML Anything** | 当你本机已登录某个 coding-agent CLI、想要零 API key、local-first 地把 Markdown 变成可交付 HTML 并一键导出微信/X/知乎时用它。 | Apache-2.0 | [中](categories/ai-design-generation/html-anything.zh.md) · [EN](categories/ai-design-generation/html-anything.md) |
| **Open Design** | 想要一个 local-first、BYOK 的桌面 studio，让编码 agent 产出 HTML 原型、deck、图像和 HTML→MP4 动效时用它。 | Apache-2.0 | [中](categories/ai-design-generation/open-design.zh.md) · [EN](categories/ai-design-generation/open-design.md) |
| **Impeccable** | 当你的 AI agent 总是产出同质化前端「AI 味」、需要确定性检测加设计 critique 时使用。 | Apache-2.0 | [中](categories/ai-design-generation/impeccable.zh.md) · [EN](categories/ai-design-generation/impeccable.md) |
| **ian-xiaohei-illustrations** | 当你要为中文文章批量生成风格一致、带小黑 IP 的手绘 16:9 正文配图时用它。 | MIT | [中](categories/ai-design-generation/ian-illustrations.zh.md) · [EN](categories/ai-design-generation/ian-illustrations.md) |
| **Guizang PPT Skill** | 当你想让 agent 把文章变成有设计感的单文件 HTML 翻页 PPT（杂志风或瑞士风）时用它。 | AGPL-3.0-only | [中](categories/ai-design-generation/guizang-ppt.zh.md) · [EN](categories/ai-design-generation/guizang-ppt.md) |
| **Guizang Social Card Skill** | 当你在 Claude Code/Codex 里想让 agent 用锁定的编辑风/瑞士风生成小红书图文或公众号封面对（单文件 HTML 渲染成 PNG）时使用。 | AGPL-3.0-only | [中](categories/ai-design-generation/guizang-social-card.zh.md) · [EN](categories/ai-design-generation/guizang-social-card.md) |
| **SdPaint** | 当你已在跑 AUTOMATIC1111＋ControlNet、想要一个实时草图转图的绘画循环时用它——但它自 2024 年起停滞，且自身不带任何模型。 | MIT | [中](categories/ai-design-generation/sdpaint.zh.md) · [EN](categories/ai-design-generation/sdpaint.md) |
### dev-utilities

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **DevToys** | 想把 Base64/JSON/哈希/diff 等开发小工具离线本地化、收进一个跨平台桌面应用、不再用不可信在线网站时，用它。 | MIT | [中](categories/dev-utilities/devtoys.zh.md) · [EN](categories/dev-utilities/devtoys.md) |
| **CyberChef** | 当你需要在浏览器里离线串联编解码、加解密、压缩和数据分析变换、且数据不能外发时用它。 | Apache-2.0 | [中](categories/dev-utilities/cyberchef.zh.md) · [EN](categories/dev-utilities/cyberchef.md) |
| **Cockpit** | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 | LGPL-2.1-or-later | [中](categories/dev-utilities/cockpit.zh.md) · [EN](categories/dev-utilities/cockpit.md) |
| **Telegraf** | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 | MIT | [中](categories/dev-utilities/telegraf.zh.md) · [EN](categories/dev-utilities/telegraf.md) |
| **OpenZL** | 当你要把 TB 级的某种高度结构化/数值格式压得比通用 zstd 更狠时使用。 | BSD-3-Clause | [中](categories/dev-utilities/openzl.zh.md) · [EN](categories/dev-utilities/openzl.md) |
| **Certbot** | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 | Apache-2.0 | [中](categories/dev-utilities/certbot.zh.md) · [EN](categories/dev-utilities/certbot.md) |
| **tqdm** | 当你想给 Python 循环/CLI/notebook 加一个快速、低开销的进度条时用它。 | MPL-2.0 AND MIT | [中](categories/dev-utilities/tqdm.zh.md) · [EN](categories/dev-utilities/tqdm.md) |
| **SlimToolkit** | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 | Apache-2.0 | [中](categories/dev-utilities/slim.zh.md) · [EN](categories/dev-utilities/slim.md) |
| **Faker (faker-js)** | 当你需要在 JS/TS 里生成逼真的假/mock 数据（姓名、地址、金融…）用于测试和填充时用它。 | MIT | [中](categories/dev-utilities/faker-js.zh.md) · [EN](categories/dev-utilities/faker-js.md) |
| **fontTools** | 当你需要对字体做程序化处理——子集化网页字体、转格式、查改表——时用它——但它只编辑字体文件，不绘制字形也不做文字排版。 | MIT | [中](categories/dev-utilities/fonttools.zh.md) · [EN](categories/dev-utilities/fonttools.md) |
| **Flashlight** | 当你在维护一台 10.10–10.15 的老 macOS、想给 Spotlight 加插件时用它——但它自 2020 年起已弃，且需关闭 SIP，日常机器上别碰。 | MIT AND GPL-2.0-only (component split) | [中](categories/dev-utilities/flashlight.zh.md) · [EN](categories/dev-utilities/flashlight.md) |
| **IdeaVim** | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 | MIT | [中](categories/dev-utilities/ideavim.zh.md) · [EN](categories/dev-utilities/ideavim.md) |
### frontend-animation

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Anime.js** | 零依赖的 JS 动画引擎：统一 animate() API 驱动 CSS、SVG、DOM 属性和 JS 对象，内置时间线、错峰、弹簧缓动和滚动联动。 | MIT | [中](categories/frontend-animation/anime.zh.md) · [EN](categories/frontend-animation/anime.md) |

### api-gateway

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Kong Gateway** | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 | Apache-2.0 | [中](categories/api-gateway/kong.zh.md) · [EN](categories/api-gateway/kong.md) |

### geospatial

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **QGIS** | 功能完整、跨平台的桌面 GIS(Qt/C++)：浏览、编辑、分析、发布矢量/栅格/网格/点云空间数据，带 PyQGIS 插件和无界面 Server。 | GPL-2.0-or-later | [中](categories/geospatial/qgis.zh.md) · [EN](categories/geospatial/qgis.md) |

### team-chat

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **HiveChat** | 可自托管、管理员统管的中小团队 AI 聊天：管理员配好多家大模型，团队据此聊天，按分组控制可见模型与 token 配额。 | Apache-2.0 | [中](categories/team-chat/hivechat.zh.md) · [EN](categories/team-chat/hivechat.md) |

### captcha

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Cap** | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 | Apache-2.0 | [中](categories/captcha/capjs.zh.md) · [EN](categories/captcha/capjs.md) |
| **Text_select_captcha** | 当要自动识别中文文字点选验证码（YOLO＋孪生网络，纯 CPU）时用它——仓库无 LICENSE 文件，默认保留所有权利，合法性是决定性门槛。 | NONE (no LICENSE file — all rights reserved) | [中](categories/captcha/text-select-captcha.zh.md) · [EN](categories/captcha/text-select-captcha.md) |
| **pytorch-captcha-recognition** | 当需要定长图片验证码（多头 CNN）的可读教学基线时用它——这是 2020 年冻结的教程，要预期改造过时的 PyTorch API。 | Apache-2.0 | [中](categories/captcha/pytorch-captcha-recognition.zh.md) · [EN](categories/captcha/pytorch-captcha-recognition.md) |
| **captcha (lepture)** | 当 Python 表单需要自托管、无第三方调用的图片／音频验证码渲染器时用它——它只渲染且抵不住现代 OCR，只能当 UX 减速带，而非安全控制。 | BSD-3-Clause | [中](categories/captcha/lepture-captcha.zh.md) · [EN](categories/captcha/lepture-captcha.md) |
### ml-research

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **autoresearch** | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 | MIT | [中](categories/ml-research/autoresearch.zh.md) · [EN](categories/ml-research/autoresearch.md) |
| **llm-circuit-finder** | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制（不训练、不改权重），再用内置探针验证效果。 | MIT | [中](categories/ml-research/llm-circuit-finder.zh.md) · [EN](categories/ml-research/llm-circuit-finder.md) |
| **CLIP** | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 | MIT | [中](categories/ml-research/clip.zh.md) · [EN](categories/ml-research/clip.md) |
| **TaskMatrix** | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 | MIT | [中](categories/ml-research/taskmatrix.zh.md) · [EN](categories/ml-research/taskmatrix.md) |
| **PyTorch-GAN** | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 | MIT | [中](categories/ml-research/pytorch-gan.zh.md) · [EN](categories/ml-research/pytorch-gan.md) |
| **LSTM Neural Network for Time Series Prediction** | 当需要可读的配套示例学习 Keras LSTM 时序预测时用它——它锁定 EOL 的 TF1／Python 3.5 且为 AGPL-3.0，应照文章重写而非直接引入。 | AGPL-3.0 | [中](categories/ml-research/lstm-time-series.zh.md) · [EN](categories/ml-research/lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 当需要中文领域知识图谱完整蓝图与现成数据集（NER、关系抽取、Neo4j、Django）时用它——作者声明已停止维护、技术栈陈旧且 GPL-3.0，应借鉴方法而非照搬代码。 | GPL-3.0 | [中](categories/ml-research/agriculture-knowledge-graph.zh.md) · [EN](categories/ml-research/agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | 当身处 PaddlePaddle／ERNIE 生态、需要带论文方法的 SKEP 情感分析 checkpoint 时用它——它锁定 EOL 的 PaddlePaddle 1.6.3，环境复原难以避免。 | Apache-2.0 | [中](categories/ml-research/senta.zh.md) · [EN](categories/ml-research/senta.md) |
| **Depth Anything V2** | 当需要当下默认的单目深度基础模型从单张图估深度（PyTorch／Transformers）时用它——仅 Small 权重为 Apache-2.0，Base／Large／Giant 是 CC-BY-NC-4.0（非商用）。 | Apache-2.0 | [中](categories/ml-research/depth-anything-v2.zh.md) · [EN](categories/ml-research/depth-anything-v2.md) |
| **pymoo** | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 | Apache-2.0 | [中](categories/ml-research/pymoo.zh.md) · [EN](categories/ml-research/pymoo.md) |
### agent-skill-collections

#### agent-skill-collections / engineering

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Agent Skills (addyosmani)** | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 | MIT | [中](categories/agent-skill-collections/engineering/addyosmani-agent-skills.zh.md) · [EN](categories/agent-skill-collections/engineering/addyosmani-agent-skills.md) |
| **web-quality-skills** | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 | MIT | [中](categories/agent-skill-collections/engineering/addyosmani-web-quality.zh.md) · [EN](categories/agent-skill-collections/engineering/addyosmani-web-quality.md) |
| **Scientific Agent Skills** | 一个大型 skill 包（约 147 个 skill），把 coding agent 变成生物、化学、医学、药物发现领域的科研助手——每个 skill 用一份带文档的 SKILL.md 封装一个科学 Python 库或数据库，按需加载。 | MIT | [中](categories/agent-skill-collections/engineering/scientific-agent-skills.zh.md) · [EN](categories/agent-skill-collections/engineering/scientific-agent-skills.md) |
| **Vercel Agent Skills** | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 | MIT | [中](categories/agent-skill-collections/engineering/vercel-agent-skills.zh.md) · [EN](categories/agent-skill-collections/engineering/vercel-agent-skills.md) |
| **Waza** | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 | MIT | [中](categories/agent-skill-collections/engineering/waza.zh.md) · [EN](categories/agent-skill-collections/engineering/waza.md) |

#### agent-skill-collections / design

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Designer Skills** | 覆盖面很广的设计实践 skill pack——9 个 plugin 下共 97 个 skill、30 个 command（研究、设计系统、UX 策略、UI、交互、原型/测试、design ops、工具箱、视觉批评），适用于 Claude Code 和 Gemini CLI。 | MIT | [中](categories/agent-skill-collections/design/designer-skills.zh.md) · [EN](categories/agent-skill-collections/design/designer-skills.md) |
| **make-interfaces-feel-better** | 一个单一、聚焦的 agent skill，把约 16 条具体的 UI 打磨原则（同心圆角、可中断过渡、等宽数字、入场/出场动画）注入 coding agent，让界面「感觉」做完了，而不只是功能正确。 | MIT | [中](categories/agent-skill-collections/design/make-interfaces-feel-better.zh.md) · [EN](categories/agent-skill-collections/design/make-interfaces-feel-better.md) |
| **Stitch Skills** | 一套遵循 Agent Skills 开放标准的技能库，驱动 Google 的 Stitch MCP server 生成 UI 屏幕、在代码与设计间双向转换、抽取 DESIGN.md，并导出 React/React Native/shadcn 组件。 | Apache-2.0 | [中](categories/agent-skill-collections/design/stitch-skills.zh.md) · [EN](categories/agent-skill-collections/design/stitch-skills.md) |
| **Taste-Skill** | 一套可移植、与框架无关的 agent skill 包，给 coding agent 注入审美，阻止千篇一律的 AI-slop 前端，转而产出有意图的布局、排版、动效与留白。 | MIT | [中](categories/agent-skill-collections/design/taste-skill.zh.md) · [EN](categories/agent-skill-collections/design/taste-skill.md) |
| **UI UX Pro Max Skill** | 一个设计智能 skill pack，通过本地 CSV 检索引擎（风格/配色/字体/规则数据库）和交付前可访问性清单给 coding agent 注入 UI/UX 品味，可装入多种 agent harness。 | MIT | [中](categories/agent-skill-collections/design/ui-ux-pro-max.zh.md) · [EN](categories/agent-skill-collections/design/ui-ux-pro-max.md) |

#### agent-skill-collections / writing

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Baoyu Skills** | 宝玉出品的 20+ 个 coding agent 技能合集（翻译、markdown/HTML 排版、字幕与网页抓取、图片/图表/幻灯片生成），可装入 Claude Code、Codex 等支持 skill 的 harness。 | MIT | [中](categories/agent-skill-collections/writing/baoyu-skills.zh.md) · [EN](categories/agent-skill-collections/writing/baoyu-skills.md) |
| **Humanizer-zh** | 一个简体中文 Claude Code 单技能，按约 24 条清单改写掉文本里的 AI 痕迹，是 blader/humanizer 的本地化版。 | MIT | [中](categories/agent-skill-collections/writing/humanizer-zh.zh.md) · [EN](categories/agent-skill-collections/writing/humanizer-zh.md) |

#### agent-skill-collections / security

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Anthropic Cybersecurity Skills** | 一个大型网络安全技能包（约 817 个技能），由对齐 MITRE ATT&CK、NIST CSF、ATLAS、D3FEND、NIST AI RMF、MITRE F3 的 SKILL.md runbook 组成，按需加载进 coding agent。 | Apache-2.0 | [中](categories/agent-skill-collections/security/anthropic-cybersecurity-skills.zh.md) · [EN](categories/agent-skill-collections/security/anthropic-cybersecurity-skills.md) |

#### agent-skill-collections / context-engineering

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Agent Skills for Context Engineering** | 一个 15 个 skill 的 Claude Code 插件包，灌输上下文工程纪律：基础原理、退化、压缩、多 agent 协同、记忆、工具设计、评估与 harness 工程。 | MIT | [中](categories/agent-skill-collections/context-engineering/context-engineering-skills.zh.md) · [EN](categories/agent-skill-collections/context-engineering/context-engineering-skills.md) |
| **NotebookLM Claude Code Skill** | 一个 Claude Code skill：用真实 Chrome 驱动查询你的 Google NotebookLM 笔记本，从你自己上传的文档取回有来源依据、带引用的答案，而非逐文件读取或凭空编造。 | MIT | [中](categories/agent-skill-collections/context-engineering/notebooklm-skill.zh.md) · [EN](categories/agent-skill-collections/context-engineering/notebooklm-skill.md) |

#### agent-skill-collections / vendor-collections

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Anthropic Skills** | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 | Apache-2.0 | [中](categories/agent-skill-collections/vendor-collections/anthropic-skills.zh.md) · [EN](categories/agent-skill-collections/vendor-collections/anthropic-skills.md) |
| **Agent Plugins for AWS** | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 | Apache-2.0 | [中](categories/agent-skill-collections/vendor-collections/aws-agent-plugins.zh.md) · [EN](categories/agent-skill-collections/vendor-collections/aws-agent-plugins.md) |
| **Claude Plugins (Official)** | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 | Apache-2.0 | [中](categories/agent-skill-collections/vendor-collections/claude-plugins-official.zh.md) · [EN](categories/agent-skill-collections/vendor-collections/claude-plugins-official.md) |
| **MiniMax Skills** | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 | MIT | [中](categories/agent-skill-collections/vendor-collections/minimax-skills.zh.md) · [EN](categories/agent-skill-collections/vendor-collections/minimax-skills.md) |
| **Anthropic Knowledge Work Plugins** | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 | Apache-2.0 | [中](categories/agent-skill-collections/vendor-collections/knowledge-work-plugins.zh.md) · [EN](categories/agent-skill-collections/vendor-collections/knowledge-work-plugins.md) |

#### agent-skill-collections / subagent-collections

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Agency-Agents** | 约 232 个专业 subagent 人格的精选集合（markdown），覆盖 16 个职能部门，附 install/convert 脚本，可部署到 Claude Code 及另外约 11 个 agent harness。 | MIT | [中](categories/agent-skill-collections/subagent-collections/agency-agents.zh.md) · [EN](categories/agent-skill-collections/subagent-collections/agency-agents.md) |
| **awesome-claude-code-subagents** | 一套精选的 100+ 个 Claude Code subagent 定义合集（每个角色一个 markdown persona），丢进 ~/.claude/agents/ 后 Claude Code 就能把活委派给对应领域专家。 | MIT | [中](categories/agent-skill-collections/subagent-collections/awesome-claude-code-subagents.zh.md) · [EN](categories/agent-skill-collections/subagent-collections/awesome-claude-code-subagents.md) |
| **wshobson/agents** | 单人维护的大型多 harness 插件市场（约 194 个 subagent、158 个 skill、106 个 command、16 个 orchestrator），用一份 Markdown 源生成各 harness 原生产物，覆盖 Claude Code、Codex CLI、Cursor、OpenCode、Gemini CLI 与 Copilot。 | MIT | [中](categories/agent-skill-collections/subagent-collections/wshobson-agents.zh.md) · [EN](categories/agent-skill-collections/subagent-collections/wshobson-agents.md) |

#### agent-skill-collections / personal-collections

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **antfu/skills** | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 | MIT | [中](categories/agent-skill-collections/personal-collections/antfu-skills.zh.md) · [EN](categories/agent-skill-collections/personal-collections/antfu-skills.md) |
| **claude-code-harness** | 一套个人化的 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环（spec 优先契约、TDD 门控执行、独立 review），并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 | MIT | [中](categories/agent-skill-collections/personal-collections/claude-code-harness.zh.md) · [EN](categories/agent-skill-collections/personal-collections/claude-code-harness.md) |
| **dbskill** | 一套个人精选的中文 agent 技能包（约 21 个 /dbs-* 命令），聚焦商业模式诊断、内容创作与个人决策，可安装进 Claude Code 等 harness。 | CC-BY-NC-4.0 | [中](categories/agent-skill-collections/personal-collections/dbskill.zh.md) · [EN](categories/agent-skill-collections/personal-collections/dbskill.md) |
| **Dimillian Skills** | 某开发者个人精选的 16 个自包含 Codex skill，重心压在 Apple 平台（SwiftUI/iOS/macOS），外加几个通用评审/重构 swarm。 | MIT | [中](categories/agent-skill-collections/personal-collections/dimillian-skills.zh.md) · [EN](categories/agent-skill-collections/personal-collections/dimillian-skills.md) |
| **gstack** | Garry Tan 的私人 Claude Code 配置：约 23 个带强烈主张的 slash-command 技能，扮演一支虚拟工程团队（CEO 复盘、设计师、工程经理、QA、安全官），驱动「规划→构建→评审→发布→复盘」闭环。 | MIT | [中](categories/agent-skill-collections/personal-collections/gstack.zh.md) · [EN](categories/agent-skill-collections/personal-collections/gstack.md) |
| **andrej-karpathy-skills** | 一个行为准则包——单个 CLAUDE.md（加 Cursor 变体和一层薄技能包装），把 Karpathy 关于 LLM 编码陷阱的四条原则（先想后写、简单优先、外科式改动、目标驱动执行）注入 Claude Code / Cursor。 | MIT | [中](categories/agent-skill-collections/personal-collections/karpathy-skills.zh.md) · [EN](categories/agent-skill-collections/personal-collections/karpathy-skills.md) |
| **Khazix Skills** | 数字生命卡兹克（Khazix）的个人精选合集，含五个 SKILL.md 标准格式、以中文为主的 Agent Skill：磁盘清理、AI 资讯查询、文档/记忆同步、长文研究报告、公众号风格写作。 | MIT | [中](categories/agent-skill-collections/personal-collections/khazix-skills.zh.md) · [EN](categories/agent-skill-collections/personal-collections/khazix-skills.md) |
| **ljg-skills** | 李继刚的个人 Claude Code 技能合集（20+ 个 skill），面向中文知识工作——读论文/拆书、概念分析、大白话改写、把内容渲染成 PNG 卡片，通过 skills CLI 安装。 | NOASSERTION | [中](categories/agent-skill-collections/personal-collections/ljg-skills.zh.md) · [EN](categories/agent-skill-collections/personal-collections/ljg-skills.md) |
| **PUA** | 一个高能动性人设 skill 包：把 coding agent 设定成「被放进 30 天 PIP 的 P8 工程师」，用职场 PUA/PIP 话术逼它穷尽排查手段而非早早放弃。 | MIT | [中](categories/agent-skill-collections/personal-collections/pua.zh.md) · [EN](categories/agent-skill-collections/personal-collections/pua.md) |
| **Qiushi-Skill** | 一套方法论 skill 包，用「实事求是」加九个唯物辩证法思维工具（矛盾分析、调查研究、实践认识论等）武装编程 agent，并通过 npx 安装器跨 Claude Code/Cursor/Codex/OpenCode 落地。 | MIT | [中](categories/agent-skill-collections/personal-collections/qiushi-skill.zh.md) · [EN](categories/agent-skill-collections/personal-collections/qiushi-skill.md) |
| **shaping-skills** | Ryan Singer 的个人 Claude Code 技能包，把 Shape Up 的「shaping」流程（框定问题、breadboarding、产出 framing/kickoff 文档）带进 coding agent，让 AI 在写代码前先帮你想清楚「要做什么」。 | NOASSERTION | [中](categories/agent-skill-collections/personal-collections/shaping-skills.zh.md) · [EN](categories/agent-skill-collections/personal-collections/shaping-skills.md) |
| **TÂCHES CC Resources** | TÂCHES（glittercowboy）的个人化 Claude Code 扩展合集：约 27 个 slash 命令、9 个 skill（多为生成新命令/skill/subagent/hook/MCP server 的元生成器）、3 个审计 subagent 及 hook，作为单个 marketplace 插件安装。 | MIT | [中](categories/agent-skill-collections/personal-collections/taches-cc-resources.zh.md) · [EN](categories/agent-skill-collections/personal-collections/taches-cc-resources.md) |

### observability

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Grafana** | 当你需要在 Prometheus/Loki/Elasticsearch 等多数据源之上加一层统一看板和告警时用它——它做可视化，不做存储。 | AGPL-3.0 | [中](categories/observability/grafana.zh.md) · [EN](categories/observability/grafana.md) |

### data-visualization

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Apache Superset** | 当你想要在数据仓库之上自托管 SQL BI 看板与探索时用它——不是基础设施指标/可观测性。 | Apache-2.0 | [中](categories/data-visualization/superset.zh.md) · [EN](categories/data-visualization/superset.md) |

### ocr

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Tesseract** | 当你需要离线、可嵌入、覆盖 100+ 语言、面向清晰印刷文本的 OCR 时用它——不适合野外照片或手写。 | Apache-2.0 | [中](categories/ocr/tesseract.zh.md) · [EN](categories/ocr/tesseract.md) |
| **LaTeX-OCR (pix2tex)** | 当你要把数学公式图片转成 LaTeX（pix2tex）时用它——只管公式、已放缓，VLM 可能更强。 | MIT | [中](categories/ocr/latex-ocr.zh.md) · [EN](categories/ocr/latex-ocr.md) |

### document-parsing

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | MIT | [中](categories/document-parsing/docling.zh.md) · [EN](categories/document-parsing/docling.md) |

### diagramming

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Mermaid** | 当你想把图表写成可进版本库的纯文本（流程图/时序图/ER），在 Markdown 和文档里渲染时用它——不适合像素级精确排版。 | MIT | [中](categories/diagramming/mermaid.zh.md) · [EN](categories/diagramming/mermaid.md) |
| **flowchart.js** | 当你想把简单流程图写成可 git diff 的文本、在浏览器里渲成 SVG 时用它——它只渲染不编辑，依赖老旧的 Raphael.js，复杂图会力不从心。 | MIT | [中](categories/diagramming/flowchart-js.zh.md) · [EN](categories/diagramming/flowchart-js.md) |
| **bpmn-js** | 当业务分析师需要在你的 Web 应用里编辑或查看合规的 BPMN 2.0 流程图时用它——但其许可证强制保留不可移除的 bpmn.io 水印，白标前务必先确认条款。 | MIT + bpmn.io watermark clause | [中](categories/diagramming/bpmn-js.zh.md) · [EN](categories/diagramming/bpmn-js.md) |
### media-download

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **youtube-dl** | 当你需要一个久经考验的 CLI/库从 YouTube 和 1000+ 站点下载音视频时用它——但热门站点优先用更活跃的 yt-dlp 分叉。 | Unlicense | [中](categories/media-download/youtube-dl.zh.md) · [EN](categories/media-download/youtube-dl.md) |
| **you-get** | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 | MIT | [中](categories/media-download/you-get.zh.md) · [EN](categories/media-download/you-get.md) |
| **cobalt** | 当你想要一个干净、可自托管、带 Web UI 和 API、无广告无追踪的媒体下载器时用它——不是可脚本化的 CLI。 | AGPL-3.0 | [中](categories/media-download/cobalt.zh.md) · [EN](categories/media-download/cobalt.md) |
| **lux** | 当你想要一个快速的单二进制 Go 下载器、对中文视频站点支持好时用它——站点覆盖与更新都不如 yt-dlp。 | MIT | [中](categories/media-download/lux.zh.md) · [EN](categories/media-download/lux.md) |
| **youtube-transcript-api** | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 | MIT | [中](categories/media-download/youtube-transcript-api.zh.md) · [EN](categories/media-download/youtube-transcript-api.md) |
| **bulk-downloader-for-reddit** | 当你想通过 OAuth 做可脚本化、可复现的 Reddit 文件加元数据归档时用它——但 Reddit 约 1000 帖的列表上限无法绕过，且发布自 2023 年初已停滞（GPL-3.0）。 | GPL-3.0 | [中](categories/media-download/bulk-downloader-for-reddit.zh.md) · [EN](categories/media-download/bulk-downloader-for-reddit.md) |
### media-processing

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **FFmpeg** | 当你需要在管线里解码/编码/转码/滤镜处理几乎任何音视频时用它——注意 LGPL→GPL 的构建授权陷阱。 | LGPL-2.1-or-later | [中](categories/media-processing/ffmpeg.zh.md) · [EN](categories/media-processing/ffmpeg.md) |
| **ffmpeg-python** | 当你想用 Python 编排复杂的 FFmpeg 滤镜图、把不可读的 -filter_complex 字符串换成可读的 DAG 代码时用它——但它自 2024 年起停更、仅单人维护，且仍依赖系统已装 ffmpeg 二进制。 | Apache-2.0 | [中](categories/media-processing/ffmpeg-python.zh.md) · [EN](categories/media-processing/ffmpeg-python.md) |
| **VMAF** | 当你在调编码档位、需要用业界通用的 0—100 感知分对比编解码器与预设时用它——但它只支持全参考，且选错模型会悄悄让跨版本对比失效。 | BSD-2-Clause-Patent | [中](categories/media-processing/vmaf.zh.md) · [EN](categories/media-processing/vmaf.md) |
| **m3u8** | 当你需要把 HLS 的 .m3u8 清单当作带类型的对象模型来解析或改写、而非正则硬抠时用它——但它仅限 Python 与 HLS，且自 2025 年起沉寂，最新的 rfc8216bis 标签可能滞后。 | MIT | [中](categories/media-processing/m3u8.zh.md) · [EN](categories/media-processing/m3u8.md) |
| **ffsubsync** | 当字幕整体存在恒定偏移、你想用一条命令做 FFT 音频对齐而不手动设同步点时用它——但它修不了内容内部的逐行／变动漂移，且仅单人维护。 | MIT | [中](categories/media-processing/ffsubsync.zh.md) · [EN](categories/media-processing/ffsubsync.md) |
### llm-chat-ui

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **NextChat** | 当你想要一个私有、可自部署、跨 web/桌面/移动 的多 provider AI 聊天前端时用它——不是多用户 RBAC 团队平台。 | MIT | [中](categories/llm-chat-ui/nextchat.zh.md) · [EN](categories/llm-chat-ui/nextchat.md) |

### markdown-tools

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Markdown Here** | 当你想用浏览器/Thunderbird 扩展把邮件用 Markdown 写好、发送前渲染成 HTML 时用它——注意维护已放缓。 | MIT | [中](categories/markdown-tools/markdown-here.zh.md) · [EN](categories/markdown-tools/markdown-here.md) |
| **marked** | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 | MIT | [中](categories/markdown-tools/marked.zh.md) · [EN](categories/markdown-tools/marked.md) |

### pdf-tools

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | Apache-2.0 | [中](categories/pdf-tools/pdfjs.zh.md) · [EN](categories/pdf-tools/pdfjs.md) |

### workflow-orchestration

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Apache Airflow** | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 | Apache-2.0 | [中](categories/workflow-orchestration/airflow.zh.md) · [EN](categories/workflow-orchestration/airflow.md) |
| **Gaia** | 当作只读参考研究「流水线即编译插件」设计时用它——仓库已归档废弃，绝不可用于新的生产部署。 | Apache-2.0 | [中](categories/workflow-orchestration/gaia.zh.md) · [EN](categories/workflow-orchestration/gaia.md) |
| **Airflow Maintenance DAGs** | 当自管 Airflow 需要现成 DAG 清理元数据库行和陈旧日志时用它——它执行依赖版本内部结构的破坏性删除，先 dry-run 并备份。 | Apache-2.0 | [中](categories/workflow-orchestration/airflow-maintenance-dags.zh.md) · [EN](categories/workflow-orchestration/airflow-maintenance-dags.md) |
### llm-inference

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | Apache-2.0 (mixed) | [中](categories/llm-inference/modular.zh.md) · [EN](categories/llm-inference/modular.md) |
| **omlx** | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 | Apache-2.0 | [中](categories/llm-inference/omlx.zh.md) · [EN](categories/llm-inference/omlx.md) |

### task-queue

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **XXL-JOB** | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 | GPL-3.0 | [中](categories/task-queue/xxl-job.zh.md) · [EN](categories/task-queue/xxl-job.md) |
| **Celery** | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 | BSD-3-Clause | [中](categories/task-queue/celery.zh.md) · [EN](categories/task-queue/celery.md) |
| **Kombu** | 当 Python 服务要在可替换 broker（RabbitMQ、Redis、SQS）间收发消息时用它——虚拟 transport 对 AMQP 的模拟并不完整，换 URL 不等于行为一致。 | BSD-3-Clause | [中](categories/task-queue/kombu.zh.md) · [EN](categories/task-queue/kombu.md) |
| **Flower** | 当生产 Celery 集群需要实时面板查看、控制 worker 并导出 Prometheus 指标时用它——它能撤销任务，绝不能无鉴权暴露。 | BSD-3-Clause | [中](categories/task-queue/flower.zh.md) · [EN](categories/task-queue/flower.md) |
### im-automation

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **ItChat** | 仅作为旧版微信机器人代码学习——已停更，且其依赖的网页协议已失效，基本不可用。 | MIT | [中](categories/im-automation/itchat.zh.md) · [EN](categories/im-automation/itchat.md) |
| **WeChatPlugin-MacOS** | 当前微信别用——一个 patch macOS 微信客户端二进制的小助手，每次微信更新就失效、已 ~2 年没动；有封号与安全风险。 | MIT | [中](categories/im-automation/wechatplugin-macos.zh.md) · [EN](categories/im-automation/wechatplugin-macos.md) |
| **wxpy** | 仅作为旧版微信机器人代码学习——2019 年起已归档，且基于已失效的微信网页协议，基本不可用。 | MIT | [中](categories/im-automation/wxpy.zh.md) · [EN](categories/im-automation/wxpy.md) |
| **wxappUnpacker** | 当你需要把自有的微信小程序 .wxapkg 包反编译回可读源码时用它——但本仓库已被清空成墓碑，请改用仍存活的 fork。 | GPL-3.0-or-later | [中](categories/im-automation/wxappunpacker.zh.md) · [EN](categories/im-automation/wxappunpacker.md) |
| **Douyin-Bot** | 仅当你想要一份 ADB 屏幕坐标手机自动化的历史示例时用它——切勿部署，2018 年的硬编码坐标与失效的腾讯人脸 API 意味着它早已跑不通。 | MIT | [中](categories/im-automation/douyin-bot.zh.md) · [EN](categories/im-automation/douyin-bot.md) |
### web-ui

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Driver.js** | 当你想在网页上加一个极简、无依赖的产品引导/功能高亮时用它——不是完整的 onboarding 平台。 | MIT | [中](categories/web-ui/driver-js.zh.md) · [EN](categories/web-ui/driver-js.md) |

### proxy-pool

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **proxy_pool** | 当爬虫需要一个走简单 API 的轮换免费代理 IP 池时用它——前提是接受免费代理不稳定、不安全。 | MIT | [中](categories/proxy-pool/proxy-pool.zh.md) · [EN](categories/proxy-pool/proxy-pool.md) |
| **ProxyBroker** | 当你想为低风险原型用一个本地轮换端点临时凑一批免费公共代理时用它——但它自约 2018 年起实质冻结，在新版 Python 上不锁版本普遍跑不起来。 | Apache-2.0 | [中](categories/proxy-pool/proxybroker.zh.md) · [EN](categories/proxy-pool/proxybroker.md) |
| **Scylla** | 当你想用一条 Docker 命令跑一个常驻自托管、带 JSON API、质量打分与面板的免费代理池时用它——但其正向代理不支持 HTTPS，且发布自 2022 年起停滞。 | Apache-2.0 | [中](categories/proxy-pool/scylla.zh.md) · [EN](categories/proxy-pool/scylla.md) |
| **haipproxy** | 当你确实需要为多机大规模爬取搭一个基于 Scrapy＋Redis 的分布式高可用免费代理池时用它——但它自 2022 年起休眠、跑的是 2018 年代 Py2／3 代码，且是最难运维的代理池。 | MIT | [中](categories/proxy-pool/haipproxy.zh.md) · [EN](categories/proxy-pool/haipproxy.md) |
### debugging-proxy

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **whistle** | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 | MIT | [中](categories/debugging-proxy/whistle.zh.md) · [EN](categories/debugging-proxy/whistle.md) |
| **AnyProxy** | 当你想用纯 JS 规则脚本化地拦截并改写 HTTP/HTTPS 流量、需要一个 Node.js MITM 代理时用它——但 master 自 2020 年已冻结，新项目请优先选 whistle。 | Apache-2.0 | [中](categories/debugging-proxy/anyproxy.zh.md) · [EN](categories/debugging-proxy/anyproxy.md) |
### web-scraping

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **newspaper** | 用来从新闻 URL 批量提取正文、作者和元数据——但原版（newspaper3k）已陈旧，活跃路径是 newspaper4k 分叉。 | MIT | [中](categories/web-scraping/newspaper.zh.md) · [EN](categories/web-scraping/newspaper.md) |
| **requests-html** | 可作为小型 requests + HTML 解析脚本参考——基本停更（~2 年没动），JS 渲染路径脆弱；新项目优先 Playwright + parsel。 | MIT | [中](categories/web-scraping/requests-html.zh.md) · [EN](categories/web-scraping/requests-html.md) |


### auth

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Authomatic** | 当需要框架无关的 Python 应用通过 OAuth1／OAuth2／OpenID 实现轻量「用 X 登录」、且会话持久化自己负责时用它——但它迭代缓慢，而认证库修复迟缓本身就是安全风险。 | MIT | [中](categories/auth/authomatic.zh.md) · [EN](categories/auth/authomatic.md) |
| **django-rules** | 当 Django 的对象级权限是由逻辑（谓词）计算得出、而非存储授权、且不想加数据库表时用它——但若管理员需在运行时为单个对象分配权限，则应改用 django-guardian。 | MIT | [中](categories/auth/django-rules.zh.md) · [EN](categories/auth/django-rules.md) |

### databases

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **PikiwiDB** | 当大规模 Redis 数据集撑爆内存、内存成本成为主要负担时用它——RocksDB 落盘、兼容 Redis 协议，单节点可存数百 GB；但它以延迟换容量，若每次操作都要微秒级则不合适。 | BSD-3-Clause | [中](categories/databases/pikiwidb.zh.md) · [EN](categories/databases/pikiwidb.md) |
| **elasticsearch-dsl-py** | 当你维护仍锁定独立 elasticsearch-dsl 包的旧 Python 代码时才用它——任何新项目它都已归档，请改装 elasticsearch>=8.18 并使用 elasticsearch.dsl。 | Apache-2.0 | [中](categories/databases/elasticsearch-dsl-py.zh.md) · [EN](categories/databases/elasticsearch-dsl-py.md) |
| **elasticsearch-sql** | 当熟悉 SQL 的团队想免学 JSON Query DSL 直接查 Elasticsearch 时用它——但 Elastic 官方的 SQL／ES\|QL 已与之重叠，能覆盖你的需求时优先用官方特性。 | Apache-2.0 | [中](categories/databases/elasticsearch-sql.zh.md) · [EN](categories/databases/elasticsearch-sql.md) |
| **go-mysql-elasticsearch** | 当你想用单个 Go 二进制 tail MySQL binlog、单向中等规模同步到 Elasticsearch 时用它——但它自 2023 年起无人维护、无任何发布，请当作 fork 自管的项目对待。 | MIT | [中](categories/databases/go-mysql-elasticsearch.zh.md) · [EN](categories/databases/go-mysql-elasticsearch.md) |
| **python-mysql-replication** | 当你想用纯 Python 原语把 MySQL binlog 流式解析成带类型的事件、自建可控 CDC 循环时用它——但 checkpoint、去重和精确一次投递全得你自己负责。 | Apache-2.0 | [中](categories/databases/python-mysql-replication.zh.md) · [EN](categories/databases/python-mysql-replication.md) |
| **PrettyZoo** | 当你在开发或故障排查时想用友好的桌面 GUI 浏览并轻量编辑 ZooKeeper znode 树时用它——但它自 2023 年起已归档，新 JDK／macOS 可能跑不起来且无上游修复。 | Apache-2.0 | [中](categories/databases/prettyzoo.zh.md) · [EN](categories/databases/prettyzoo.md) |
| **RDR** | 当 Redis 触发 maxmemory 告警、需要离线快速按前缀分析 RDB 快照时用它——但内存数字是近似值，且项目已停滞（v0.0.1，2019 年）。 | Apache-2.0 | [中](categories/databases/rdr.zh.md) · [EN](categories/databases/rdr.md) |

### desktop-automation

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **PyAutoGUI** | 当你要在 Windows／macOS／Linux 上脚本化操控没有 API 的桌面应用时用它——但基于坐标和像素的自动化会因分辨率、DPI 或主题变化静默失效，且自 2024 年起已停滞维护。 | BSD-3-Clause | [中](categories/desktop-automation/pyautogui.zh.md) · [EN](categories/desktop-automation/pyautogui.md) |

### game-dev

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **pygame** | 当你想学做或交付一个带简单游戏循环的小型 2D Python 游戏时用它——但做 3D 或性能敏感的项目它会成瓶颈，请另寻它路。 | LGPL-2.1 | [中](categories/game-dev/pygame.zh.md) · [EN](categories/game-dev/pygame.md) |

### kafka-tools

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **UI for Apache Kafka (provectus/kafka-ui)** | 当你想用一条 docker run 起一个浏览 Kafka broker、topic 和消费组 lag 的 Web 面板时用它——但 provectus 上游已停摆（末次发布 2024-04），应改用仍在维护的 kafbat/kafka-ui 分叉。 | Apache-2.0 | [中](categories/kafka-tools/kafka-ui.zh.md) · [EN](categories/kafka-tools/kafka-ui.md) |
| **kafka-python** | 当你想要一个纯 Python、pip install 即装、无需编译 librdkafka 的 Kafka 客户端时用它——但纯 Python 客户端的吞吐追不上 confluent-kafka，且对最新 broker 特性可能滞后支持。 | Apache-2.0 | [中](categories/kafka-tools/kafka-python.zh.md) · [EN](categories/kafka-tools/kafka-python.md) |

### networking

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Paramiko** | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 | LGPL-2.1 | [中](categories/networking/paramiko.zh.md) · [EN](categories/networking/paramiko.md) |
| **sshtunnel** | 当 Python 脚本需要以上下文管理器方式打通到堡垒机后服务的 SSH 端口转发时用它——但它无自动重连，且活跃度低（0.4.0，2021 年）。 | MIT | [中](categories/networking/sshtunnel.zh.md) · [EN](categories/networking/sshtunnel.md) |
| **dnspython** | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 | ISC | [中](categories/networking/dnspython.zh.md) · [EN](categories/networking/dnspython.md) |
| **wondershaper** | 当某块 Linux 网卡需要快速设置上／下行带宽上限、又不想手写 tc 规则时用它——但它基于老式 HTB（不像 cake／fq_codel 那样应对 bufferbloat），仅限 Linux，自 2024 年 7 月起停滞。 | GPL-2.0 | [中](categories/networking/wondershaper.zh.md) · [EN](categories/networking/wondershaper.md) |
| **ThriftPy** | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 | MIT | [中](categories/networking/thriftpy.zh.md) · [EN](categories/networking/thriftpy.md) |

### nginx-modules

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **lua-nginx-module (ngx_lua)** | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 | BSD-2-Clause | [中](categories/nginx-modules/lua-nginx-module.zh.md) · [EN](categories/nginx-modules/lua-nginx-module.md) |
| **lua-resty-redis** | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 | BSD-2-Clause | [中](categories/nginx-modules/lua-resty-redis.zh.md) · [EN](categories/nginx-modules/lua-resty-redis.md) |
| **nginx-upload-module** | 当你想让 NGINX 把大文件 multipart 上传直接落盘、只把文件元数据交给后端时用它——但你在编译一个老化、单人维护的 C 分叉（末次提交 2024-07），如今直传 S3 预签名上传往往更优。 | BSD-3-Clause | [中](categories/nginx-modules/nginx-upload-module.zh.md) · [EN](categories/nginx-modules/nginx-upload-module.md) |

### python-tooling

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **Cython** | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 | Apache-2.0 | [中](categories/python-tooling/cython.zh.md) · [EN](categories/python-tooling/cython.md) |
| **pyrasite** | 当你必须向一个无法重启、卡死或泄漏的运行中 Python 进程注入诊断代码时用它——但注入可能让目标崩溃，只当救火工具用。 | GPL-3.0 | [中](categories/python-tooling/pyrasite.zh.md) · [EN](categories/python-tooling/pyrasite.md) |
| **gophernotes** | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 | MIT | [中](categories/python-tooling/gophernotes.zh.md) · [EN](categories/python-tooling/gophernotes.md) |
| **GRequests** | 当你想用 `map()` 以最小改动让现有同步 `requests` 代码并发时用它——但 gevent 会猴补丁标准库，可能与你的技术栈冲突。 | BSD-2-Clause | [中](categories/python-tooling/grequests.zh.md) · [EN](categories/python-tooling/grequests.md) |
| **memory-analyzer** | 当你需要经 GDB 对一个活的 Python 3 进程做一次性按类型内存快照时用它——但 Meta 已归档它（代码停在 2021，目标是 EOL 的 3.6／3.7），优先选 memray／tracemalloc 这类有维护的工具。 | MIT | [中](categories/python-tooling/memory-analyzer.zh.md) · [EN](categories/python-tooling/memory-analyzer.md) |

### reading-tools

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **NetNewsWire** | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 | MIT | [中](categories/reading-tools/netnewswire.zh.md) · [EN](categories/reading-tools/netnewswire.md) |
| **Just Read** | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 | Unlicensed (EULA) | [中](categories/reading-tools/just-read.zh.md) · [EN](categories/reading-tools/just-read.md) |

### speech

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **SpeechBrain** | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 | Apache-2.0 | [中](categories/speech/speechbrain.zh.md) · [EN](categories/speech/speechbrain.md) |

### terminal-ui

| 项目 | 何时用 | 许可 | 页面 |
|---|---|---|---|
| **colorama** | 当 Python 命令行需要在旧版 Windows 控制台也能正确显示 ANSI 彩色输出时用它——但它只是颜色／样式适配层（不提供表格、TUI 或真彩保证），在现代终端上基本是空操作。 | BSD-3-Clause | [中](categories/terminal-ui/colorama.zh.md) · [EN](categories/terminal-ui/colorama.md) |
| **asciimatics** | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 | Apache-2.0 | [中](categories/terminal-ui/asciimatics.zh.md) · [EN](categories/terminal-ui/asciimatics.md) |
| **Terminal Markdown Viewer (mdv)** | 当你想在 SSH 下的纯终端里一次性、只读地渲染带彩色与语法高亮的 Markdown 时用它——但它活跃度低（0.x，2024 年 5 月），glow／mdcat 已是更现代的默认选择。 | BSD-3-Clause | [中](categories/terminal-ui/terminal-markdown-viewer.zh.md) · [EN](categories/terminal-ui/terminal-markdown-viewer.md) |
| **ART** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | MIT | [中](categories/terminal-ui/art.zh.md) · [EN](categories/terminal-ui/art.md) |
| **asciify** | 当你只想要一份极简易读、可复制粘贴的图片转 ASCII 算法参考时用它——但它没有任何许可证（默认保留所有权利），自 2022 年起无人维护，切勿将其并入产品。 | NONE | [中](categories/terminal-ui/asciify.zh.md) · [EN](categories/terminal-ui/asciify.md) |

分类顺序见 [INDEX.zh.md](INDEX.zh.md)。
| **Readability.js** | 当你需要用 Firefox 阅读视图那套久经考验的引擎，把网页剥离成纯文章（标题、作者、正文）时用它——但它只解析你传入的 DOM，不会抓取 URL，也不会渲染重 JS 的 SPA。 | Apache-2.0 | [中](categories/web-scraping/readability-js.zh.md) · [EN](categories/web-scraping/readability-js.md) |
| **python-readability** | 当你的 Python 流水线需要从已抓取的 HTML 中用 lxml 快速抽取正文、不依赖浏览器或 Node 时用它——但它单人维护、更新缓慢，而 trafilatura 在抽取基准上往往得分更高。 | Apache-2.0 | [中](categories/web-scraping/python-readability.zh.md) · [EN](categories/web-scraping/python-readability.md) |
| **dragnet** | 当你有标注数据、想要一个可训练、还能把正文与用户评论分离的 ML 抽取器时用它——但它近乎停滞，依赖锁死老旧（scikit-learn<0.21、ftfy<5），在现代技术栈上安装会很痛苦。 | MIT | [中](categories/web-scraping/dragnet.zh.md) · [EN](categories/web-scraping/dragnet.md) |
| **boilerpipe** | 当你确实需要一个 JVM 原生、依赖轻量、基于经典算法的正文抽取器时用它——但仓库实际上已废弃（末次提交 2018-01），内置依赖陈旧，且不会再有安全修复。 | Apache-2.0 | [中](categories/web-scraping/boilerpipe.zh.md) · [EN](categories/web-scraping/boilerpipe.md) |
| **fuck-login** | 当你想读 2016 年代「如何脚本化登录（CSRF／RSA／验证码）」的示例代码时用它——但它自 2018 年起已废弃、无许可证，脚本如今基本失效。 | NONE | [中](categories/web-scraping/fuck-login.zh.md) · [EN](categories/web-scraping/fuck-login.md) |
| **gopup** | 当你想一行代码把中国公开数据（搜索指数、CPI、Shibor）拉进 pandas DataFrame 做学术研究时用它——但它自 2023 年起停更、无许可证，源站一变接口就失效。 | NONE | [中](categories/web-scraping/gopup.zh.md) · [EN](categories/web-scraping/gopup.md) |
| **PRAW** | 当你的数据源就是 Reddit、想走官方 OAuth 合规路径并自带限速处理时用它——但真正的边界是 Reddit 自家的 API 条款、配额与定价，而非这个库。 | BSD-2-Clause | [中](categories/web-scraping/praw.zh.md) · [EN](categories/web-scraping/praw.md) |
| **Scrapyd** | 当你需要把本地 Scrapy 爬虫部署到服务器、通过 HTTP API 做定时与多版本调度时用它——但它只能跑 Scrapy 且默认无鉴权，暴露 6800 端口前务必先加认证。 | BSD-3-Clause | [中](categories/web-scraping/scrapyd.zh.md) · [EN](categories/web-scraping/scrapyd.md) |
| **SpiderKeeper** | 当运行 Scrapyd 的小团队想要最简单的浏览器面板来部署和定时调度爬虫时用它——但它自 2023 年已停更且默认 admin/admin 鉴权，切勿暴露在不可信网络。 | MIT | [中](categories/web-scraping/spiderkeeper.zh.md) · [EN](categories/web-scraping/spiderkeeper.md) |
## 为什么做这个

多数开源 README 是营销：讲它能干啥、为啥好，却**不**告诉你何时*不该*用、和替代怎么比、运维成本多少。
做选型的 agent 恰恰需要这片「负空间」。oss-atlas 把 README 这个体裁反转成**决策支持**体裁。

索引刻意做得「弱」——没有数据库、没有搜索、没有 embedding，就是给 agent 读和推理的 Markdown。
目录结构本身就是「查询 API」。

## 选型信号与启发式

选开源是在赌未来，不只是匹配功能。每页都带一个 **`健康度与可持续性`** 小节——一段有日期、带标注的
判断：维护节奏、治理与 bus factor、背书方、采用度与生态，以及风险旗标（relicense 史、open-core
阉割、CVE）。它要和 `何时不用` 一起看。

有一条先验值得点名——**林迪效应（Lindy effect）**：对非易逝之物（软件、格式、工具），预期*剩余*寿命
随当前年龄增长。一个**持续活跃**了 12 年的项目，比一个半年内爆火的项目更适合长期押注。把它当先验、
不是定律，且永远按 **年龄 × 仍活跃** 一起用：它既给「年轻但被炒作」的仓库降权（star 离谱、未经检验），
也**救不了**「老但已弃」的仓库（光有年龄 ≠ 还活着）；遇到范式更替时还可能误导。每页都记录项目**年龄**，
让这条先验可核查。[推断：林迪只是启发式，不构成对任何具体项目存续的保证。]

## 结构（递归树，双语）

```
INDEX.md / INDEX.zh.md                        # 根：分类路由（英 / 中）
categories/<分类>/INDEX.md / INDEX.zh.md      # 一个分类节点：项目页 + 子分类
categories/<分类>/<子类>/INDEX.md …           # 更深的节点 —— 树随增长自平衡
…/<slug>.md  +  …/<slug>.zh.md                # 一个叶子：英文选型页 + 它的中文兄弟页
```

`categories/` 是一棵**递归、自平衡的树**：某个分类项目过多时会拆成子分类（linter 告警，
`refactor-index` 执行拆分）。英文是 agent 默认读取的 canonical 路径，`.zh.md` 是同一内容的中文版。

### 一个项目页的结构

每页 = **YAML frontmatter（事实，带日期）** + **正文（判断）**。两者刻意分开：事实会过期、需要
重新核验（`last_verified`）；判断是观点，要带标注（`[未验证]` / `[推断]`），绝不当成永恒真理断言。

**Frontmatter**（中英成对、逐字一致——事实与语言无关）：
`name · slug · repo · category · tags · language · license · maturity`（带日期）· `last_verified` · `type`
（`tool | library | app | framework | service | model | skill-pack`）。

**正文小节**（确切集合随 `type` 而定）：

| 小节（英 / 中） | 必需于 | 承载什么 |
|---|---|---|
| `When to use` / `何时使用` | 所有类型 | 一个 **User Story**——具体的第二人称场景，不是功能清单 |
| `When NOT to use` / `何时不用` | 所有类型 | 决定性筛子：反模式、规模天花板、锁定、维护风险 |
| `Comparison` / `横向对比` | 所有类型 | 与真实替代品的对比表（替代品尚未收录则标 `未收录`） |
| `Tech stack` / `技术栈` | 非 `skill-pack` | 它构建于哪些语言、框架、数据存储 |
| `Dependencies` / `依赖` | 非 `skill-pack` | 你必须自己跑的运行时/基建（数据库、服务、硬件） |
| `Ops difficulty` / `运维难度` | 非 `skill-pack` | 低 / 中 / 高 + 原因 |
| `Health & viability` / `健康度与可持续性` | 所有类型 | 带日期的可持续性判断——维护、治理与 bus factor、背书方、**年龄 × Lindy**、采用度、风险旗标 |
| `Caveats (unverified)` / `存疑（未验证）` | 所有类型 | 不确定性账本——每条未验证事实一个 `[未验证]`/`[推断]` 条目 |

完整契约见 [tools/schema.md](tools/schema.md)；linter（[tools/lint.py](tools/lint.py)）强制这套形状
（小节、中英对齐、中文全角标点、README 对齐）。

## 新鲜度

事实会过期。每页记 `last_verified`。超过 90 天 linter 会告警；`sync-entry` 技能负责对照线上仓库
重核。把任何事实都当作**时点快照**，并按真话纪律标注（`[未验证]` / `[推断]`）。

## 贡献

策展，而非求全。一个项目只有在**确实被评估过**、**且存在真实选型问题**（有值得对比的替代）时才进。
见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [tools/schema.md](tools/schema.md)。

```bash
python3 tools/lint.py    # 唯一的门；没有单元测试（这是内容仓库）
```

## 许可证

- **工具**（代码，如 `tools/lint.py`）：MIT——见 [LICENSE](LICENSE)。
- **内容**（`categories/` 下的散文、路由页、文档）：CC BY 4.0——见 [LICENSE-CONTENT](LICENSE-CONTENT)。

各项目页描述的是第三方项目，其归属与许可证由各自作者决定；CC BY 4.0 仅覆盖这里的原创分析。
