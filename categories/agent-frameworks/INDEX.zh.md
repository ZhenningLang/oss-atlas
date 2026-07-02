# agent-frameworks

> 分类节点。构建与运行多步 / 多智能体系统——agent 框架与 agent 操作系统。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | A（6/6） | [→](dspy.zh.md) |
| **AgentScope** | 要把多智能体 LLM 应用作为生产服务交付，需要沙箱工具、权限闸门、tracing 和人工介入时。 | B（6/6） | [→](agentscope.zh.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | B（5/6） | [→](openfang.zh.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | B（5/6） | [→](symphony.zh.md) |
| **Claude Octopus** | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 | C（6/6） | [→](claude-octopus.zh.md) |
| **oh-my-claudecode** | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 | B（5/6） | [→](oh-my-claudecode.zh.md) |
| **smolagents** | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 | B（6/6） | [→](smolagents.zh.md) |
| **Kilo Code** | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 | B（6/6） | [→](kilocode.zh.md) |
| **Parlant** | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 | B（6/6） | [→](parlant.zh.md) |
| **SkillOpt** | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 | B（6/6） | [→](skillopt.zh.md) |
| **Open Interpreter** | 当你想要一个 Codex-fork 的终端编码 agent、带为低成本 / 开源模型（DeepSeek、Kimi、Qwen）调过的可切换 harness 时用它——不是老的 Python REPL（那个已迁到社区 fork），而且它是几周大的 0.0.x 重写、会执行代码。 | A（6/6） | [→](open-interpreter.zh.md) |
| **Codex** | 当你想要一个轻量级、由 OpenAI 支持的终端编码智能体，能编辑文件、运行测试并提交变更时用它——但需要 OpenAI API 访问权限和网络连接。 | ?（0/6） | [→](codex.zh.md) |
| **OpenClaw** | 当你想要一款在自有设备上运行、跨 20 余条消息渠道应答你的个人 AI 助手时用它——但它极其年轻，毫无 Lindy 记录。 | ?（0/6） | [→](openclaw.zh.md) |
| **CC Switch** | 当你同时使用多种 AI 编码智能体（Claude Code、Codex、Gemini CLI、OpenClaw、OpenCode、Hermes Agent）并希望有一个统一的桌面控制平面进行提供商路由和 MCP 支持时用它——但它不足一岁，且为单人维护。 | ?（0/6） | [→](cc-switch.zh.md) |
| **Hermes Agent** | 当你想要一个带学习循环、能从经验中创建技能、可在 5 美元 VPS 上运行的自我改进 AI 智能体时用它——但它不足一岁，学习循环的稳定性未经检验。 | ?（0/6） | [→](hermes-agent.zh.md) |
| **AutoGPT** | 当你需要一个用于创建、部署和管理持续运行 AI 智能体以自动化复杂工作流的平台时用它——但它未声明许可，且自托管需要大量资源。 | ?（0/6） | [→](autogpt.zh.md) |
| **Dify** | 当你想要一个生产就绪的、用于构建 agentic 工作流的低代码可视化平台，内置 RAG 与 MCP 支持时用它——但商用前请核实许可。 | ?（0/6） | [→](dify.zh.md) |
| **LangChain** | 当你需要一个代码优先的框架来组合 LLM agent、工具与记忆，并拥有庞大的集成生态时用它——但简单单 prompt 应用别用它。 | ?（0/6） | [→](langchain.zh.md) |
| **RTK** | 当你使用基于 CLI 的 AI 编码智能体，想在常见 shell 命令上减少 60–90% 的 LLM token 消耗时用它——但它仅约 6 个月大，且 star 数高得可疑。 | ?（0/6） | [→](rtk.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [DSPy](dspy.zh.md) | ✅ | A（6/6） | 优化器层按指标编译提示词/权重——本类独有；需评测数据，非工作流引擎。 |
| [AgentScope](agentscope.zh.md) | ✅ | B（6/6） | 生产级多智能体运行时：沙箱工具、权限闸门、tracing、人工介入。 |
| [OpenFang](openfang.zh.md) | ✅ | B（5/6） | 自托管 Rust「agent OS」，按计划 7×24 自治运行。 |
| [Symphony](symphony.zh.md) | ✅ | B（5/6） | 自托管编排器，按 issue 跑隔离自治实现运行（Linear + Codex）。 |
| [Claude Octopus](claude-octopus.zh.md) | ✅ | C（6/6） | Claude Code 内的跨模型盲点评审层。 |
| [oh-my-claudecode](oh-my-claudecode.zh.md) | ✅ | B（5/6） | Claude Code 的多阶段 agent 团队 + 模型路由 + tmux 并行。 |
| [smolagents](smolagents.zh.md) | ✅ | B（6/6） | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 |
| [Kilo Code](kilocode.zh.md) | ✅ | B（6/6） | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 |
| [Parlant](parlant.zh.md) | ✅ | B（6/6） | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 |
| [SkillOpt](skillopt.zh.md) | ✅ | B（6/6） | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | A（6/6） | OpenAI Codex-fork 的终端编码 agent，带运行时可切换、为低成本 / 开源模型调过的 harness；几周大的 0.0.x Rust 重写、在 OS 沙箱里执行代码——不是已停更的 Python REPL。 |
| [Codex](codex.zh.md) | ✅ | ?（0/6） | 轻量级 OpenAI 终端编码智能体，带沙箱代码执行；仅限 OpenAI，极其年轻（2025-04 创建），且需要 API 额度。 |
| [OpenClaw](openclaw.zh.md) | ✅ | ?（0/6） | 在自有设备上跨 20 余条消息渠道运行的个人 AI 助手；极其年轻（2025-11 创建），无 Lindy 记录。 |
| [CC Switch](cc-switch.zh.md) | ✅ | ?（0/6） | 跨平台桌面管理器，统一管理多个 AI 编码智能体（Claude Code、Codex、Gemini CLI 等），支持提供商路由和 MCP；不足一岁，单人维护，bus factor 为 1。 |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | ?（0/6） | Nous Research 出品的自我改进 AI 智能体，带学习循环；能从经验中创建技能，但不足一岁，学习循环稳定性未经检验。 |
| [AutoGPT](autogpt.zh.md) | ✅ | ?（0/6） | 用于创建、部署和管理持续运行 AI 智能体的平台；未声明许可、资源占用高，且云端测试版尚未公开。 |
| [Dify](dify.zh.md) | ✅ | ?（0/6） | 生产就绪的低代码可视化 agentic 工作流平台，内置 RAG 与 MCP；商用前请核实许可。 |
| [LangChain](langchain.zh.md) | ✅ | ?（0/6） | 代码优先的 LLM agent、工具与记忆组合框架，集成生态庞大；简单单 prompt 应用别用它。 |
| [RTK](rtk.zh.md) | ✅ | ?（0/6） | 在 shell 输出到达 AI 智能体前进行压缩的 CLI 代理，可减少 60–90% 的 token 成本；极其年轻（6 个月），star 数高得可疑。 |
| [OpenCode](opencode.zh.md) | ✅ | ?（0/6） | 可自托管、审计和扩展的开源终端编码智能体；极其年轻（2025-04 创建），无 Lindy 记录。 |
| [Langflow](langflow.zh.md) | ✅ | ?（0/6） | 可视化拖拽平台，用于构建和部署 LLM 工作流与智能体，内置 API 和 MCP 服务器；可视化流比代码更难做 diff/审查。 |
| [Gemini CLI](gemini-cli.zh.md) | ✅ | ?（0/6） | 基于 Google Gemini 模型的开源终端 AI 智能体，带免费层、内置工具和 MCP 支持；非常年轻（2025-04 创建）且仅限 Google 模型。 |

## 什么该放这里

主要职责是**构建、编排或自治运行**多步 / 多智能体系统的框架与运行时。
不含 LLM 微调（见 `llm-training`）、不含单纯的 agent 记忆（见 `agent-memory`）、
不含推理运行时（见 `on-device-ml`）。
