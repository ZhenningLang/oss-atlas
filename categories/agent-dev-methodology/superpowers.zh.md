---
name: Superpowers
slug: superpowers
repo: https://github.com/obra/superpowers
category: agent-dev-methodology
tags: [skills, sdlc, tdd, subagent-driven-development, brainstorming, git-worktrees, claude-code, plugin]
language: Shell
license: MIT
maturity: v6.0.3, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# Superpowers

一套可组合的 skills 库,以插件形式把完整的 SDLC 方法论——头脑风暴 → 写计划 → TDD → subagent 驱动执行 → 验证——装进你的编程 agent。

## 何时使用

你是一名开发者,在用 Claude Code(或 Codex、Cursor、Gemini CLI、OpenCode、Kimi、Droid…),反复撞上同一个失败模式:agent 上来就写代码,跳过先写失败测试,靠猜来"修" bug,然后没真正验证就宣布完成。你希望它像一名有纪律的资深工程师那样干活——先追问你到底想做什么、把计划写下来、做真正的 red-green-refactor、在 git worktree 上隔离改动、并在声称完成前跑一遍验证。Superpowers 正好把这些做成即插即用的插件:一组精心编排的 skills(`brainstorming`、`writing-plans`、`test-driven-development`、`systematic-debugging`、`subagent-driven-development`、`verification-before-completion`、`using-git-worktrees` 等),agent 按需加载并逐步执行。

当你想要一套有主张、经实战检验的工作流,而不是从零搭自己的 skill 栈时,就该用它——尤其是当你希望同一套方法论能跨 harness 跟着你走。仓库自带各 agent 的插件清单(Claude `.claude-plugin`、Codex、Cursor、Kimi、OpenCode、Pi),因此无论今天的任务跑在 Claude Code 还是 Codex CLI,头脑风暴-计划-TDD-验证这条主轴都保持一致。通过你 agent 的 marketplace 安装一次,方法论就会经由各平台原生的 skill 加载机制激活。

## 何时不用

- **你已经有一套自己信任的 skill/command 体系。** Superpowers 有强主张、强约束(强制先写失败测试、写代码前先 brainstorm)。把它叠在现有方法论栈之上,容易产生指令冲突和重复路由——只选一个事实源。
- **你不在受支持的 agent harness 上。** 它靠各平台的 skill 加载机制激活(Claude `Skill` 工具,Codex/Cursor/Kimi/Gemini/OpenCode 插件)。在不受支持或自研的 agent 上没有加载器去调用这些 skill,单凭 markdown 不会自动触发。
- **一次性脚本、抛弃式 spike、非代码任务。** 当你只想要一行 shell 或改个配置时,完整的 brainstorm→plan→TDD→verify 仪式就是负担;这套方法论假设的是真实的软件改动循环。
- **你想要的是运行时/库/CLI。** 这里没有可 `import` 或独立运行的东西——没有依赖、没有 API、没有服务。它只塑造 agent 的行为;离开支持它的 agent 就什么都不做。
- **上游迭代快、主张强。** 单维护者项目,已到 v6.x,发版频繁,行为固化在 prompt 里;一次版本升级就可能改变 skill 的路由方式或它强制的内容。需要稳定就锁版本,升级后重新核对。[推断]

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| [SuperClaude Framework](superclaude.zh.md) | ✅ | 面向 persona/命令/MCP 的 Claude Code 配置框架;命令和 agent 面更丰富,安装更重。Superpowers 更精简,主轴是 TDD/SDLC 纪律而非 persona 体系。 |
| [get-shit-done](get-shit-done.zh.md) | ✅ | 面向交付的工作流/命令包;"驱动 agent 走流程"的目标有重叠,但流程形态不同。Superpowers 以 brainstorm-then-TDD 加 subagent 分派为主线。 |
| [Compound Engineering](compound-engineering.zh.md) | ✅ | 围绕复利/自动化模式构建的方法论插件;同源理念,基元不同。按哪条工作流主轴贴合你的团队来选。 |
| [ECC](ecc.zh.md) | ✅ | 本类目下另一套 agent 开发方法论;对比点在于各自真正强制 vs 仅建议哪些生命周期阶段。 |
| [12-Factor Agents](12-factor-agents.zh.md) | ✅ | 用于构建 agent *应用* 的原则/方法论文档,而非装进编程 agent 的插件式 skill 包——消费单位不同。 |
| Anthropic 官方 skills / 内置 slash 命令 | 未收录 | 平台自带的 skill 生态;Superpowers 是叠在其上的第三方精选包,因此可能与原生 skill 冲突或重复。 |

## 存疑（未验证）

- [未验证] 最新发布记为 v6.0.3(2026-06-18 发布),仓库最近 push 于 2026-06-25;截至 2026-06-26,GitHub 元数据显示 license 为 MIT、主语言为 Shell——依赖某具体版本行为前请重新核实。
- [未验证] star 数(2026-06-26 GitHub 显示约 23.9 万)不可靠且对时间敏感,仅供参考,不作为质量信号。
- [未验证] 受支持 agent 列表(Claude Code、Codex App/CLI、Cursor、Factory Droid、Gemini CLI、GitHub Copilot CLI、Kimi Code、OpenCode、Pi、Antigravity)来自项目 README;各 harness 实际激活的保真度不一,此处未独立确认。
- [推断] 因为行为存在于 agent 加载的 prompt/markdown skill 中,约束是建议性的——agent 仍可能偏离;"强制"步骤是 prompt 层指令,而非硬保证。
- [推断] skill 集合(本次核查为 13 个)和路由随版本变动;请核对当前 `skills/` 目录,而非依赖此列表。
