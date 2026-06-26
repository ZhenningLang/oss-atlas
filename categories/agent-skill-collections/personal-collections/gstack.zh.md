---
name: gstack
slug: gstack
repo: https://github.com/garrytan/gstack
category: personal-collections
tags: [claude-code, slash-commands, subagent-personas, sdlc-workflow, harness-config]
language: TypeScript
license: MIT
maturity: no tagged release, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# gstack

Garry Tan 的私人 Claude Code 配置：约 23 个带强烈个人主张的 slash-command 技能，扮演一支虚拟工程团队（CEO 复盘、设计师、工程经理、发布经理、文档工程师、QA、安全官），驱动「规划 → 构建 → 评审 → 发布 → 复盘」的闭环。

## 何时使用

你是一名长期泡在 Claude Code 里的独立开发者或小团队成员，平时把「团队」该做的活儿全在脑子里走一遍：判断一个功能值不值得做、写代码前先锁架构、过一遍设计、自己给自己做 QA，再写发布说明、上线。你希望把这整条流水线变成有名字、可重复的步骤，而不是每个 session 重打一遍临时 prompt。你把 gstack 克隆进 `~/.claude/skills/`、跑它的 `./setup`，于是就有了 `/office-hours`（产品拷问）、`/plan-eng-review`（锁架构）、`/review`、`/qa`、`/cso`（安全审计）、`/ship`、`/document-release`、`/retro` 这些 slash 命令——每一个都是从某个角色视角审视当前工作的 persona。

当你宁愿整套搬来一个人久经实战的端到端 harness，也不想自己一条条命令攒技能栈时，就用它。它明确就是「Garry Tan 本人的做法」——他每天在用的、带主张的软件工厂工作流——所以价值在于这 23 条命令里沉淀的*品味与编排顺序*，而不是一个通用工具箱。装一次后，命令通过 Claude Code 原生的技能加载机制激活；`setup` 还能把同一批命令分发到它检测到的其它 agent（Codex CLI、OpenCode、Cursor、Droid 等）[未验证]。

## 何时不用

- **你已经有一套自己信任的命令/技能体系。** gstack 主张强、人格化（一个会质疑你路线图的 CEO、一个会锁架构的工程经理）。把它叠在已有工作流之上会产生互相打架的 slash 命令和双重路由——只能留一个事实源。
- **你想要可 import 的运行时/库/CLI。** 它的交付物是一袋 prompt 定义的技能，不是 API 或服务。脱离支持它的 agent harness，这些 markdown 什么都不做。
- **你不在被支持的 harness 上。** 它靠 Claude Code 的技能加载器激活（并声称能自动检测约 10 个其它 agent）。在自制或不被支持的 agent 上，没有加载器来触发这些命令。
- **你不想要这套安装足迹。** setup 会克隆进 `~/.claude/skills/`、按技能建符号链接目录、可能写 `.gstack/` 状态，还会自启一个「browse 守护进程」；team 模式会把 `.claude/` 与 `CLAUDE.md` 提交进你的仓库。这比丢几个 `.md` 文件重得多。
- **单一维护者、一个人的品味。** 这是某位创始人的私人配置，没有打 tag 的发布；命令及其行为可能随任意一次 push 变动，且工作流编码的是他的偏好，不是社区标准。
- **是建议而非强制。** 这里的「评审」「锁定」都是 prompt 级指令，agent 仍可忽略；没有任何一项是 CI 里的硬闸门。

## 横向对比

| 替代方案 | 是否已收录 | 取舍 |
|---|---|---|
| [Superpowers](../../agent-dev-methodology/superpowers.zh.md) | ✅ | 可组合的 SDLC 技能库（brainstorm → plan → TDD → verify），以跨 harness 插件形式分发。更偏 TDD/测试先行的纪律，且走 marketplace 安装；gstack 是某位创始人*基于角色*的命令集（CEO/设计师/QA 等 persona），为他每天的工厂量身调过，而非通用方法论。 |
| antfu/skills | 未收录 | 另一份私人 Claude Code 技能集；按各自作者编排了什么工作流、对你环境假设多少来比较。 |
| Dimillian/Skills | 未收录 | 私人技能集；按作者品味与命令的路由方式来选。 |
| wshobson/agents | 未收录 | 体量较大的 subagent/persona 集合；目录更广，对比 gstack 更聚焦的创始人主张工厂闭环。 |
| 自己从零写命令 | 未收录 | 贴合度最高、零 lock-in，但每个 persona 和编排顺序都得你自己写、自己维护。 |

## 存疑（未验证）

- [未验证] 截至 2026-06-26，GitHub 元数据显示 license 为 MIT、主语言 TypeScript；仓库最近一次 push 在 2026-06-25；未报告任何 GitHub release/tag（`latestRelease: null`），因此没有可固定的稳定版本——依赖具体命令行为前请重新核验。
- [未验证] Star 数（2026-06-26 GitHub 约 11.6 万）不可靠且对日期敏感，仅作参考，不代表质量。
- [未验证] 「23 个工具」/命令列表（如 `/office-hours`、`/plan-eng-review`、`/review`、`/qa`、`/cso`、`/ship`、`/document-release`、`/retro`）取自项目 README；确切集合与命名会随仓库变化，应以当前 `skills/` 目录为准，而非本页。
- [未验证] 声称通过 `./setup --host` 自动检测支持约 10 个 AI 编码 agent（Codex CLI、OpenCode、Cursor、Factory Droid、Slate、Kiro、Hermes、GBrain 等），来自 README；各 agent 的实际激活保真度未在此独立确认。
- [未验证] 安装/运行要求（Git、Bun v1.0+、Windows 下可选 Node、自启的「browse 守护进程」、记忆功能可选用 Supabase/PGLite）取自 README，未通过实际运行 setup 验证。
- [推断] 由于行为存在于 agent 加载的 prompt/markdown 技能中，每个「评审」「锁定」「闸门」都是建议性的——agent 可以偏离；请当作指引，而非强制控制。
- [推断] 作为某人无发布版本的私人配置，破坏性变更可能在任意一次 push 落地；若需稳定，请固化你测试过的版本。
