# agent-tooling

> 三级路由的第 2 级。为 AI 编码 agent 选「任务/工作追踪、持久记忆、agent 状态」基建。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 许可证 | 页面 |
|---|---|---|---|
| **beads** | agent（或一小队 agent）需要跨会话、跨分支、可随代码版本化的依赖式任务记忆。 | MIT | [→](beads.zh.md) |

## 对比矩阵

项目页里点到、但**尚未收录**（`未收录`）的替代方案，是未来候选条目——见
[add-project](../../.claude/skills/add-project/SKILL.md)。

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [beads](beads.zh.md) | ✅ | 依赖感知、可版本控制（Dolt）的任务图；agent 原生、离线优先——但仍 alpha，嵌入模式单写入，无人类 web UI。 |
| Plain `MEMORY.md` / `TODO.md` | 未收录 | 零依赖、人类可读——但非结构化（无图、无 ready 检测、无可安全合并的 ID）。 |
| GitHub Issues (+ `gh`) | 未收录 | 成熟托管 tracker，带 UI/通知——但在线优先、不随代码版本控制、非 agent 原生。 |
| Taskwarrior | 未收录 | 久经考验的离线 CLI 任务管理器——但无 SQL/版本控制后端，多 agent 合并较弱。 |
| Linear / Jira | 未收录 | 面向人类团队最佳——但重量级、仅在线、非 agent 原生。 |

## 什么该放这里

主要职责是支撑 AI 编码 agent *运行*的工具：任务/工作图、持久记忆、agent 状态存储、多 agent 协调。
不包括只是*调用* LLM 的终端用户应用。
