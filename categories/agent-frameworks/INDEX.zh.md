# agent-frameworks

> 分类节点。构建与运行多步 / 多智能体系统——agent 框架与 agent 操作系统。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | [→](dspy.zh.md) |
| **AgentScope** | 要把多智能体 LLM 应用作为生产服务交付,需要沙箱工具、权限闸门、tracing 和人工介入时。 | [→](agentscope.zh.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | [→](openfang.zh.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | [→](symphony.zh.md) |
| **Claude Octopus** | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 | [→](claude-octopus.zh.md) |
| **oh-my-claudecode** | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 | [→](oh-my-claudecode.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [DSPy](dspy.zh.md) | ✅ | 优化器层按指标编译提示词/权重——本类独有;需评测数据,非工作流引擎。 |
| [AgentScope](agentscope.zh.md) | ✅ | 生产级多智能体运行时:沙箱工具、权限闸门、tracing、人工介入。 |
| [OpenFang](openfang.zh.md) | ✅ | 自托管 Rust「agent OS」,按计划 7×24 自治运行。 |
| [Symphony](symphony.zh.md) | ✅ | 自托管编排器,按 issue 跑隔离自治实现运行(Linear + Codex)。 |
| [Claude Octopus](claude-octopus.zh.md) | ✅ | Claude Code 内的跨模型盲点评审层。 |
| [oh-my-claudecode](oh-my-claudecode.zh.md) | ✅ | Claude Code 的多阶段 agent 团队 + 模型路由 + tmux 并行。 |
| LangChain / LlamaIndex / CrewAI / AutoGen | 未收录 | 各页对比里点到的更广义 agent 构建/运行生态。 |

## 什么该放这里

主要职责是**构建、编排或自治运行**多步 / 多智能体系统的框架与运行时。
不含 LLM 微调(见 `llm-training`)、不含单纯的 agent 记忆(见 `agent-memory`)、
不含推理运行时(见 `on-device-ml`)。
