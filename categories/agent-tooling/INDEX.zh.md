# agent-tooling

> 分类节点。面向 AI 编码 agent 的基础设施——任务/工作追踪、持久记忆、agent 状态。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **beads** | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 | [→](beads.zh.md) |
| **CCPM** | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 | [→](ccpm.zh.md) |
| **Entire** | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 | [→](entire-cli.zh.md) |
| **Ralph for Claude Code** | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 | [→](ralph-claude-code.zh.md) |
| **Context Mode** | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 | [→](context-mode.zh.md) |
| **Planning with Files** | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 | [→](planning-with-files.zh.md) |
| **Vercel Skills** | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 | [→](vercel-skills.zh.md) |
| **OpenSandbox** | 当 agent 需要在隔离的 Docker/K8s 沙箱里运行不可信的生成代码时用它——非常年轻的高星项目，采用度宜谨慎看待。 | [→](opensandbox.zh.md) |
| **AgentsView** | 当你想对自己的编码 agent 会话做本地优先的搜索、分析与 token 成本洞察时用它。 | [→](agentsview.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [beads](beads.zh.md) | ✅ | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 |
| [CCPM](ccpm.zh.md) | ✅ | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 |
| [Entire](entire-cli.zh.md) | ✅ | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 |
| [Ralph for Claude Code](ralph-claude-code.zh.md) | ✅ | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 |
| [Context Mode](context-mode.zh.md) | ✅ | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 |
| [Planning with Files](planning-with-files.zh.md) | ✅ | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 |
| [Vercel Skills](vercel-skills.zh.md) | ✅ | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 |
| [OpenSandbox](opensandbox.zh.md) | ✅ | 当 agent 需要在隔离的 Docker/K8s 沙箱里运行不可信的生成代码时用它——非常年轻的高星项目，采用度宜谨慎看待。 |
| [AgentsView](agentsview.zh.md) | ✅ | 当你想对自己的编码 agent 会话做本地优先的搜索、分析与 token 成本洞察时用它。 |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | 各页对比里点到的其他 agent 任务/工作追踪后端。 |

## 什么该放这里

AI **编码 agent** 用来追踪工作、承载状态的基础设施——任务/issue 图、会话捕获、规划/上下文管线。不含与 LLM 无关的记忆库(见 `agent-memory`)，不含 agent 运行时(见 `agent-frameworks`)。
