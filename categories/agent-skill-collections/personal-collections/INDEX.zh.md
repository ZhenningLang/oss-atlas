# personal-collections

> [agent-skill-collections](../INDEX.zh.md) 的叶子。长尾：某个作者策展的技能、subagent 或 harness 配置。
> ← 上层 [agent-skill-collections](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 页面 |
|---|---|---|
| **antfu/skills** | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 | [→](antfu-skills.zh.md) |
| **claude-code-harness** | 一套个人化的 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环（spec 优先契约、TDD 门控执行、独立 review），并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 | [→](claude-code-harness.zh.md) |
| **dbskill** | 一套个人精选的中文 agent 技能包（约 21 个 /dbs-* 命令），聚焦商业模式诊断、内容创作与个人决策，可安装进 Claude Code 等 harness。 | [→](dbskill.zh.md) |
| **Dimillian Skills** | 某开发者个人精选的 16 个自包含 Codex skill，重心压在 Apple 平台（SwiftUI/iOS/macOS），外加几个通用评审/重构 swarm。 | [→](dimillian-skills.zh.md) |
| **gstack** | Garry Tan 的私人 Claude Code 配置：约 23 个带强烈主张的 slash-command 技能，扮演一支虚拟工程团队（CEO 复盘、设计师、工程经理、QA、安全官），驱动「规划→构建→评审→发布→复盘」闭环。 | [→](gstack.zh.md) |
| **andrej-karpathy-skills** | 一个行为准则包——单个 CLAUDE.md（加 Cursor 变体和一层薄技能包装），把 Karpathy 关于 LLM 编码陷阱的四条原则（先想后写、简单优先、外科式改动、目标驱动执行）注入 Claude Code / Cursor。 | [→](karpathy-skills.zh.md) |
| **Khazix Skills** | 数字生命卡兹克（Khazix）的个人精选合集，含五个 SKILL.md 标准格式、以中文为主的 Agent Skill：磁盘清理、AI 资讯查询、文档/记忆同步、长文研究报告、公众号风格写作。 | [→](khazix-skills.zh.md) |
| **ljg-skills** | 李继刚的个人 Claude Code 技能合集（20+ 个 skill），面向中文知识工作——读论文/拆书、概念分析、大白话改写、把内容渲染成 PNG 卡片，通过 skills CLI 安装。 | [→](ljg-skills.zh.md) |
| **PUA** | 一个高能动性人设 skill 包：把 coding agent 设定成「被放进 30 天 PIP 的 P8 工程师」，用职场 PUA/PIP 话术逼它穷尽排查手段而非早早放弃。 | [→](pua.zh.md) |
| **Qiushi-Skill** | 一套方法论 skill 包，用「实事求是」加九个唯物辩证法思维工具（矛盾分析、调查研究、实践认识论等）武装编程 agent，并通过 npx 安装器跨 Claude Code/Cursor/Codex/OpenCode 落地。 | [→](qiushi-skill.zh.md) |
| **shaping-skills** | Ryan Singer 的个人 Claude Code 技能包，把 Shape Up 的「shaping」流程（框定问题、breadboarding、产出 framing/kickoff 文档）带进 coding agent，让 AI 在写代码前先帮你想清楚「要做什么」。 | [→](shaping-skills.zh.md) |
| **TÂCHES CC Resources** | TÂCHES（glittercowboy）的个人化 Claude Code 扩展合集：约 27 个 slash 命令、9 个 skill（多为生成新命令/skill/subagent/hook/MCP server 的元生成器）、3 个审计 subagent 及 hook，作为单个 marketplace 插件安装。 | [→](taches-cc-resources.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [antfu/skills](antfu-skills.zh.md) | ✅ | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 |
| [claude-code-harness](claude-code-harness.zh.md) | ✅ | 一套个人化的 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环（spec 优先契约、TDD 门控执行、独立 review），并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 |
| [dbskill](dbskill.zh.md) | ✅ | 一套个人精选的中文 agent 技能包（约 21 个 /dbs-* 命令），聚焦商业模式诊断、内容创作与个人决策，可安装进 Claude Code 等 harness。 |
| [Dimillian Skills](dimillian-skills.zh.md) | ✅ | 某开发者个人精选的 16 个自包含 Codex skill，重心压在 Apple 平台（SwiftUI/iOS/macOS），外加几个通用评审/重构 swarm。 |
| [gstack](gstack.zh.md) | ✅ | Garry Tan 的私人 Claude Code 配置：约 23 个带强烈主张的 slash-command 技能，扮演一支虚拟工程团队（CEO 复盘、设计师、工程经理、QA、安全官），驱动「规划→构建→评审→发布→复盘」闭环。 |
| [andrej-karpathy-skills](karpathy-skills.zh.md) | ✅ | 一个行为准则包——单个 CLAUDE.md（加 Cursor 变体和一层薄技能包装），把 Karpathy 关于 LLM 编码陷阱的四条原则（先想后写、简单优先、外科式改动、目标驱动执行）注入 Claude Code / Cursor。 |
| [Khazix Skills](khazix-skills.zh.md) | ✅ | 数字生命卡兹克（Khazix）的个人精选合集，含五个 SKILL.md 标准格式、以中文为主的 Agent Skill：磁盘清理、AI 资讯查询、文档/记忆同步、长文研究报告、公众号风格写作。 |
| [ljg-skills](ljg-skills.zh.md) | ✅ | 李继刚的个人 Claude Code 技能合集（20+ 个 skill），面向中文知识工作——读论文/拆书、概念分析、大白话改写、把内容渲染成 PNG 卡片，通过 skills CLI 安装。 |
| [PUA](pua.zh.md) | ✅ | 一个高能动性人设 skill 包：把 coding agent 设定成「被放进 30 天 PIP 的 P8 工程师」，用职场 PUA/PIP 话术逼它穷尽排查手段而非早早放弃。 |
| [Qiushi-Skill](qiushi-skill.zh.md) | ✅ | 一套方法论 skill 包，用「实事求是」加九个唯物辩证法思维工具（矛盾分析、调查研究、实践认识论等）武装编程 agent，并通过 npx 安装器跨 Claude Code/Cursor/Codex/OpenCode 落地。 |
| [shaping-skills](shaping-skills.zh.md) | ✅ | Ryan Singer 的个人 Claude Code 技能包，把 Shape Up 的「shaping」流程（框定问题、breadboarding、产出 framing/kickoff 文档）带进 coding agent，让 AI 在写代码前先帮你想清楚「要做什么」。 |
| [TÂCHES CC Resources](taches-cc-resources.zh.md) | ✅ | TÂCHES（glittercowboy）的个人化 Claude Code 扩展合集：约 27 个 slash 命令、9 个 skill（多为生成新命令/skill/subagent/hook/MCP server 的元生成器）、3 个审计 subagent 及 hook，作为单个 marketplace 插件安装。 |

## 什么该放这里

**个人策展**的合集——某作者的技能、subagent 或 harness 配置。按作者领域与活跃度挑。
