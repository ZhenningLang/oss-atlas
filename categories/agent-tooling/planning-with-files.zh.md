---
name: Planning with Files
slug: planning-with-files
repo: https://github.com/OthmanAdi/planning-with-files
category: agent-tooling
tags: [agent-skill, planning, persistent-memory, context-engineering, completion-gate, multi-agent, claude-code, skill-md]
language: Python/Shell/PowerShell
license: MIT
maturity: v3.1.3 (2026-06-16), active; installs across 60+ agents via the SKILL.md standard
last_verified: 2026-06-26
type: skill-pack
---

# Planning with Files

一个遵循 SKILL.md 标准的 skill，让编码 agent 把 `task_plan.md` / `findings.md` / `progress.md` 写到磁盘上，从而在 `/clear`、上下文压缩和崩溃中存活——Manus 风格的文件化规划，带一个可选的完成闸（completion gate），外加各 IDE 的生命周期 hook。

## 何时使用

你正驱动一个编码 agent 跑一个又长又多步的任务——一次迁移、一次跨十几个文件的重构、或者一段「先调研再实现」的流程——而上下文窗口一次次坑你。Agent 填满后自动压缩，或者你手动 `/clear`，它回来时已经忘了计划：把做完的阶段重做一遍、丢掉那条「迁移落地后再修这个」的备注、或者提前三步就宣布完工。你试过手动把 TODO 列表再贴回去，但下一次压缩之后什么都留不住。

于是你装上 Planning with Files（`npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`）。现在 agent 把阶段写进 `task_plan.md`、把发现写进 `findings.md`、把运行日志写进 `progress.md`，而随包提供的生命周期 hook 会在每一轮开始时重新注入计划（在 Claude Code / Codex / Cursor 等支持的 IDE 上，还会在工具调用前注入），让状态活在磁盘上而不只在窗口里。`/clear` 之后，session-catchup hook 会根据文件上次被改动的时间，把这之后发生的事重建出来。对于自主运行，你可以选 `--gated` 模式：Stop-hook 完成闸会拦住 agent，直到计划里的阶段真正做完——而一个 append-only 的 JSONL 运行账本（run ledger）会用固定形状的摘要取代原来对 `progress.md` 末尾的裸读取。因为它讲的是 SKILL.md / Agent-Skills 标准，同一个 skill 可以落进 Claude Code、Cursor、Codex、Copilot、Gemini CLI、Kiro、OpenCode 等 60+ 个 agent。

## 何时不用

- **你想要一个可查询、带依赖关系的任务图，而不是扁平 markdown。** 这就是三个 append 风格的 `.md` 文件，agent 读写它们——没有 `bd ready` 那种「未被阻塞的工作」查询，没有由数据存储强制的依赖边，也没有 merge 安全的 hash ID。需要真正的任务图，请看 [beads](beads.zh.md)。
- **你的 agent / IDE 没有生命周期 hook。** 「在上下文丢失中存活」的魔法靠的是 hook（UserPromptSubmit / PreToolUse / PostToolUse / Stop / PreCompact）。在一个没有 hook 支持的纯 Agent-Skills 安装上，你拿到的是模板和约定，但没有自动重注入或完成闸——行为退化成「模型被告知要用这些文件」。
- **你不信任一个快速迭代、单一作者的项目去跑无人值守的自主运行。** 版本翻动很快（短时间内 v2.x → v3.1.3，其间有多次针对 YAML frontmatter 损坏和 hook 标志漂移的 hotfix）。gated/autonomous 模式是新东西（v3.0+），其安全主张是「仅仅计划没做完，永远不会拦住一次 stop」——在让它去看管无人值守 agent 之前，先验证这个闸是否如你所料。
- **你需要把完成闸当成硬保证。** 这个闸只在五个条件同时成立时才拦住一次 Stop，并且带有 block 次数上限和「账本必须有进展」的检查，正是为了让它不会把会话困死——也就是说，它在设计上是 advisory（建议性）的，不是绝对的「不做完就不停」的锁。
- **你只做短的、单轮的任务。** 如果你的活儿能塞进一个上下文窗口、从不压缩，那这些计划文件和 hook 就是几乎没有回报的额外开销。
- **你想要厂商中立、零 Claude/Manus 叙事的底层管道。** 这个 skill、文档和默认配置都重度以 Claude Code 为先（plugin + 斜杠命令 `/plan`、`/plan-goal`、`/plan-loop`）；其它 IDE 受支持，但 parity 会逐版本落后。

## 横向对比

| 替代方案 | 已收录 | 取舍 |
|---|---|---|
| [beads](beads.zh.md) | ✅ | 依赖感知、版本化的任务*图*（Dolt 后端、`bd` 二进制），带 merge 安全 ID 和 ready 检测；相比这三个 agent 直接编辑的纯 markdown 文件，它更重、是个真正的数据存储。 |
| [Context Mode](context-mode.zh.md) | ✅ | 同类别的 agent 上下文方案；目标（让 agent 保持定向）有重叠，机制不同——按你的 IDE 直接对照两页选。 |
| [Ralph](ralph-claude-code.zh.md) | ✅ | 面向 Claude Code 的长时自主循环 harness；它编排「跑」这件事，而 Planning with Files 提供这个循环要读写的持久计划/状态。 |
| 你手工维护的 `task_plan.md` / `TODO.md` | 未收录 | 零安装、完全归你，但没有生命周期 hook、没有 `/clear` 后自动重注入、没有完成闸、没有 session 续接——正是这个 skill 要自动化掉的手工流程。 |
| 原生 agent 记忆（`CLAUDE.md`、Cursor rules、Codex `AGENTS.md`） | 未收录 | 内置、总是被加载、无需额外安装——但那是一个静态指令文件，不是带进度日志和 stop 闸、逐任务演进的计划。 |
| Manus / 托管自主 agent 产品 | 未收录 | 这个 skill 模仿的商业范式（「work like Manus」）；托管且更丰富，但是托管产品，不是开源、IDE 本地、可随仓库提交的 skill。 |

## 存疑（未验证）

- [未验证] Star 数在 2026-06 显示约 23,968；该生态里的 GitHub star 不可靠且对日期敏感——只当参考。
- [未验证]「96.7% 通过率（v2.21.0、sonnet-4-6、30 条断言）」与「3/3 盲测 A/B 胜出」是项目自己的 evals（`docs/evals.md`），未经独立复现。
- [未验证]「通过 SKILL.md 安装到 60+ agent / 17+ 平台」是项目自己的说法；README 列出约 17 个具名 IDE 加一条通用 Agent-Skills 路径。各 IDE 的 hook parity 会逐版本落后（changelog 反复 backport 落后的变体），所以某个 IDE 的实际行为应对照其自己的 setup 文档验证。
- [推断] 把它归为 `skill-pack`（markdown 模板 + hook 脚本，无独立运行时）而非 `tool`，是从它的 SKILL.md 打包方式和 `npx skills add` 分发推出的；但仓库确实附带可执行的 shell/PowerShell/Python hook 脚本，所以这条界线不是完全干净。
- [未验证] SHA-256 attestation（「锁定 `task_plan.md`；被篡改时 hook 拦截注入」，v2.37+）以及 v3 gated/autonomous 模式语义，均来自 README/changelog 描述，未经独立测试。
- [推断]「在崩溃 / 上下文丢失中存活」完全取决于宿主 IDE 是否真的触发了相关生命周期 hook；在不触发某个事件的运行时上（有些 hook 被标注为在那里是 dormant），该保证不成立。
