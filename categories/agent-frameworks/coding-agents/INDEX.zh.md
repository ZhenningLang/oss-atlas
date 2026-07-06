# coding-agents

> 分类节点。终端、IDE 与助手侧编码 agent，以及用于切换或评审它们的控制平面。
> ← 返回 [agent-frameworks](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Claude Octopus** | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 | C（6/6） | [→](claude-octopus.zh.md) |
| **oh-my-claudecode** | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 | B（5/6） | [→](oh-my-claudecode.zh.md) |
| **Kilo Code** | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 | B（6/6） | [→](kilocode.zh.md) |
| **Open Interpreter** | 当你想要一个 Codex-fork 的终端编码 agent、带为低成本 / 开源模型（DeepSeek、Kimi、Qwen）调过的可切换 harness 时用它——不是老的 Python REPL（那个已迁到社区 fork），而且它是几周大的 0.0.x 重写、会执行代码。 | A（6/6） | [→](open-interpreter.zh.md) |
| **Codex** | 当你想要一个轻量级、由 OpenAI 支持的终端编码智能体，能编辑文件、运行测试并提交变更时用它——但需要 OpenAI API 访问权限和网络连接。 | ?（0/6） | [→](codex.zh.md) |
| **OpenCode** | 可自托管、审计和扩展的开源终端编码智能体；极其年轻（2025-04 创建），无 Lindy 记录。 | ?（0/6） | [→](opencode.zh.md) |
| **Gemini CLI** | 基于 Google Gemini 模型的开源终端 AI 智能体，带免费层、内置工具和 MCP 支持；非常年轻（2025-04 创建）且仅限 Google 模型。 | ?（0/6） | [→](gemini-cli.zh.md) |
| **CC Switch** | 当你同时使用多种 AI 编码智能体（Claude Code、Codex、Gemini CLI、OpenClaw、OpenCode、Hermes Agent）并希望有一个统一的桌面控制平面进行提供商路由和 MCP 支持时用它——但它不足一岁，且为单人维护。 | ?（0/6） | [→](cc-switch.zh.md) |
| **RTK** | 当你使用基于 CLI 的 AI 编码智能体，想在常见 shell 命令上减少 60–90% 的 LLM token 消耗时用它——但它仅约 6 个月大，且 star 数高得可疑。 | ?（0/6） | [→](rtk.zh.md) |
| **aider** | aider is AI pair programming in your terminal | ?（0/6） | [→](aider.zh.md) |
| **Cline** | Autonomous coding agent as an SDK, IDE extension, or CLI assistant. | ?（0/6） | [→](cline.zh.md) |
| **SWE-agent** | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] | ?（0/6） | [→](swe-agent.zh.md) |
| **OpenHands** | 🙌 OpenHands: AI-Driven Development | ?（0/6） | [→](openhands.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Claude Octopus](claude-octopus.zh.md) | ✅ | C（6/6） | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 |
| [oh-my-claudecode](oh-my-claudecode.zh.md) | ✅ | B（5/6） | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 |
| [Kilo Code](kilocode.zh.md) | ✅ | B（6/6） | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | A（6/6） | 当你想要一个 Codex-fork 的终端编码 agent、带为低成本 / 开源模型（DeepSeek、Kimi、Qwen）调过的可切换 harness 时用它——不是老的 Python REPL（那个已迁到社区 fork），而且它是几周大的 0.0.x 重写、会执行代码。 |
| [Codex](codex.zh.md) | ✅ | ?（0/6） | 当你想要一个轻量级、由 OpenAI 支持的终端编码智能体，能编辑文件、运行测试并提交变更时用它——但需要 OpenAI API 访问权限和网络连接。 |
| [OpenCode](opencode.zh.md) | ✅ | ?（0/6） | 可自托管、审计和扩展的开源终端编码智能体；极其年轻（2025-04 创建），无 Lindy 记录。 |
| [Gemini CLI](gemini-cli.zh.md) | ✅ | ?（0/6） | 基于 Google Gemini 模型的开源终端 AI 智能体，带免费层、内置工具和 MCP 支持；非常年轻（2025-04 创建）且仅限 Google 模型。 |
| [CC Switch](cc-switch.zh.md) | ✅ | ?（0/6） | 当你同时使用多种 AI 编码智能体（Claude Code、Codex、Gemini CLI、OpenClaw、OpenCode、Hermes Agent）并希望有一个统一的桌面控制平面进行提供商路由和 MCP 支持时用它——但它不足一岁，且为单人维护。 |
| [RTK](rtk.zh.md) | ✅ | ?（0/6） | 当你使用基于 CLI 的 AI 编码智能体，想在常见 shell 命令上减少 60–90% 的 LLM token 消耗时用它——但它仅约 6 个月大，且 star 数高得可疑。 |

## 什么该放这里

终端、IDE 与助手侧编码 agent，以及用于切换或评审它们的控制平面。
