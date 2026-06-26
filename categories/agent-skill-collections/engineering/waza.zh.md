---
name: Waza
slug: waza
repo: https://github.com/tw93/Waza
category: engineering
tags: [skills, claude-code, engineering-habits, debugging, code-review, multi-agent]
language: Python
license: MIT
maturity: v3.29.0, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
---

# Waza

一套精简的八个「工程习惯」skill 集合——规划、设计、评审、调试、写作、调研、读取、审计——打包成 coding agent 可按需加载并运行的形式，覆盖 Claude Code、Codex、Cursor。

## 何时使用

你是一名日常在 Claude Code（或 Codex / Cursor）里干活的工程师，发现 agent 完全没有你视为本能的那些纪律：不先想清楚设计就埋头写代码、靠猜而不是找根因来「修」bug、发布前不审一遍 diff 就宣布完工、写出来的英文/中文一股机器腔。你不想从零搭建并维护自己的 skill 栈，又想要一套有主见的小习惯集合，而不是一个庞大的框架。Waza 直接塞进八个具名 skill，由你直接调用——`/think`（开工前规划与设计校验）、`/design`（带审美迭代的前端 UI）、`/check`（任务后评审 / diff 分析 / 发布验证）、`/hunt`（系统化调试与根因定位）、`/write`（自然的中英文文稿润色）、`/learn`（六阶段调研工作流）、`/read`（URL 与 PDF 内容提取）、`/health`（跨平台 agent 配置审计）。

当你想要一套现成、有主见、能跨三个受支持 harness 跟着你走的习惯包，且一条命令装好（`npx skills add tw93/Waza -a claude-code codex cursor -g -y`）时，就会用到它。每个 skill 文件夹附带参考文档、辅助脚本和坑位说明，所以行为不止是一段裸 prompt——但它仍通过宿主平台原生的 skill 加载机制激活，而不是作为一个你自己运行的独立程序。

## 何时不用

- **你已有一套自建的 skill / 命令体系。** Waza 的多个 skill（`/think`、`/check`、`/hunt`、`/write`、`/health`、`/learn`、`/read`）与常见自建的规划/评审/调试/调研栈直接重叠。叠在上面会造成重复路由和指令冲突——每个习惯只保留一个事实源。
- **你的 agent 不在支持列表里。** 安装面向 Claude Code、Codex、Cursor（README 还列了 Pi / Claude Desktop）。在不受支持或自制 harness 上没有 loader 触发这些 skill，单凭 markdown 不会自动激活。[推断]
- **你要的是强制约束而非建议。** 行为存在于 agent 加载的 prompt/skill markdown 里；这些「习惯」是建议性的，agent 仍可偏离，并非硬闸门。
- **你只需要其中一个习惯。** 它是八合一的包；若只想要个调试套路，装整包会一并带进七个你不会路由到的 skill。
- **单维护者、快速迭代的上游。** v3.x 项目，发布频繁、行为内嵌在 prompt 里；一次版本升级就可能改变某个 skill 的路由或检查内容。升级后请锁版并重新核验。

## 横向对比

| 替代项 | 是否收录 | 取舍 |
|---|---|---|
| [Superpowers](../../agent-dev-methodology/superpowers.md) | ✅ | 更大、方法论优先的 skills 库（brainstorm→plan→TDD→subagent→verify），面向多 harness；Waza 是更小、面向习惯的八个具名命令的集合，更轻便上手，但不构成完整的 SDLC 主干。 |
| [SuperClaude Framework](../../agent-dev-methodology/superclaude.md) | ✅ | persona/命令/MCP 配置框架，面更大、安装更重；Waza 更精简，围绕具体工程套路而非 persona 体系。 |
| addyosmani/agent-skills | 未收录 | 本叶子里的同类 skill 集合；按各自实际提供的工程习惯与 harness 覆盖度比较。 |
| web-quality-skills（addyosmani） | 未收录 | 聚焦 web 性能/质量的 skill；领域比 Waza 的通用工程习惯更窄。 |
| vercel-labs/agent-skills | 未收录 | 厂商策划的 skill 集合；比较来源与所面向的 agent。 |
| Anthropic 内置 skill / 斜杠命令 | 未收录 | 平台原生 skill 生态；Waza 是叠在上面的第三方包，可能与原生命令重复或冲突。 |

## 存疑（未验证）

- [未验证] 最新发布标记为 v3.29.0（「Bridge」，2026-06-19 发布），仓库最后 push 于 2026-06-24；license MIT、主语言 Python（另含 Shell/Makefile），均据 2026-06-26 的 GitHub 元数据——依赖某具体版本行为前请重新核验。
- [未验证] star 数（2026-06-26 GitHub 显示约 6.05k）不可靠且对日期敏感；仅作参考，不作为质量信号。
- [未验证] 八个 skill 名称及描述（`/think`、`/design`、`/check`、`/hunt`、`/write`、`/learn`、`/read`、`/health`）与 `skills/` 目录结构取自 README 和仓库树；各 skill 的实际行为、辅助脚本和具体内容未在此实操验证。
- [未验证] 受支持 agent 列表（Claude Code、Codex、Cursor、Pi、Claude Desktop）与 `npx skills add …` 安装路径来自项目 README；各 harness 的实际激活保真度未独立确认。
- [推断] 由于行为存在于 agent 加载的 prompt/skill markdown，强制力是建议性的——「习惯」是 prompt 层指令而非硬保证，agent 可能偏离。
- [推断] 作为单维护者的 v3.x 项目、发布频繁，skill 集合与路由可能逐版本变化；请查当前 `skills/` 目录而非依赖此列表。
