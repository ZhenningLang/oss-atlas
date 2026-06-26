---
name: Claude Code Security Review
slug: claude-code-security-review
repo: https://github.com/anthropics/claude-code-security-review
category: ai-code-review
tags: [security, sast, github-action, claude, pr-review, slash-command]
language: Python
license: MIT
maturity: no tagged release, pinned via @main, active (2026-02)
last_verified: 2026-06-26
type: tool
---

# Claude Code Security Review

Anthropic 出的 AI 安全审查器:一个 GitHub Action(外加 Claude Code 的 `/security-review` 斜杠命令),用 Claude 读 PR diff,并在出问题的具体行上贴出漏洞 finding。

## 何时使用

你是一个中小型仓库的维护者,想要一道比正则/AST 模式匹配更进一步的 PR 安全闸门。传统 SAST 反复命中相同形状,却漏掉逻辑层面的 bug——比如一个 IDOR,它之所以成立是因为两个 handler 共享了 session;又比如一个注入,只有走某条特定代码路径才可达。你把这个 Action 加进 `.github/workflows/`,给它一个 Claude API key,之后每个 PR 它只分析改动过的文件、结合上下文推理 diff,并在它认为有漏洞的具体行留下带严重级别和修复建议的 review 评论。因为它"与语言无关"(本质是 Claude 在读代码,而非按语言写死规则集),同一套 workflow 就能覆盖你的 Python 服务、TypeScript 前端和 Terraform,无需分别配工具。

你也可能是一个日常用 Claude Code 的开发者,想在还没开 PR 之前就跑同样的检查。你对未提交的改动运行 `/security-review`,在本地拿到审查结果;还能把 `security-review.md` 拷进你仓库的 `.claude/commands/`,针对你的项目调 prompt。这个工具的整体卖点正是嘈杂扫描器的反面:一套有主张的误报过滤器,会丢掉 DoS/限流/开放重定向之类的 finding,让落地的评论都是值得动手处理的那些。

## 何时不用

- **你要审查不可信 / fork PR。** README 明确说它**未针对 prompt injection 做加固**,只应审查**可信 PR**;一个恶意 diff 可以尝试操纵审查器本身。对公开仓库,你必须把它挡在"维护者批准外部贡献者"之后——这是硬性运维约束,不是可选项。
- **你要免费或纯本地的扫描器。** 每次运行都调用 Claude API、按 token 计费(默认模型 `claude-opus-4-1-20250805`,单次默认 20 分钟超时)。PR 量大的仓库或开启 `run-every-commit: true` 会很贵——确定性的开源 SAST(Semgrep、CodeQL)没有按次 API 成本。
- **你需要确定性、可复现、合规级的结果。** LLM 审查器是非确定性的:同一份 diff 不同次运行可能浮现不同 finding。如果你需要稳定的规则 ID 集、抑制基线和审计可复现性,基于规则的 SAST 更合适。
- **你需要全代码库或定时深扫。** 它在设计上是 diff 感知的(只看 PR 改动文件),不是像一次完整 SAST 扫荡那样,在整个既有代码库里爬找潜在漏洞的爬虫。
- **你想要开箱即用的 SARIF / 第三方 security-tab 集成。** 输出是 PR 评论加一份结果 JSON 制品;[未验证] 没有文档化的原生 SARIF 导出,把 finding 接进 GitHub 的 code-scanning UI 不是一键的。
- **没有打 tag 的 release。** 用法 pin 的是 `@main`;没有 semver 发版线,所以你是用稳定性换"跟随一个未固定的移动分支"(或者自己 pin 某个 commit SHA)。

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| [open-code-review](open-code-review.zh.md) | ✅ | 阿里出的基于 LLM 的代码审查器,面向 GitLab / 编码风格 + 质量;本工具则是安全专用,且是 Claude/GitHub-Actions 原生。 |
| [react-doctor](react-doctor.zh.md) | ✅ | React 专用的性能/正确性诊断,不是安全审查器;完全是另一类问题。 |
| Semgrep | 未收录 | 确定性、基于规则的 SAST,带 SARIF 和庞大的社区规则集;快、免费、可复现——但被模式绑死,在逻辑/上下文型 bug 上更弱。 |
| GitHub CodeQL | 未收录 | 深度数据流/污点分析,原生 code-scanning UI,对公开仓库免费;按语言、配置更重,无 LLM 修复文字。 |
| Claude Code GitHub Action(通用版) | 未收录 | Anthropic 通用的 Claude Action,面向 PR/编码;并未专门做安全审计或 finding 过滤。 |
| Snyk Code | 未收录 | 商业 ML/SAST,带托管面板和依赖扫描;是托管 SaaS,而非单仓库开源 Action。 |

## 技术栈

- **语言:** Python(按 GitHub 约 89.6%;另有少量 TypeScript/JavaScript 用于工具链)。[未验证] 百分比是语言条快照,会漂移。
- **运行时模型:** Claude(Claude Code)——默认 `claude-opus-4-1-20250805`,可通过 `claude-model` 输入配置。
- **交付方式:** 一个组合式 GitHub Action(`anthropics/claude-code-security-review@main`)外加一个 `/security-review` Claude Code 斜杠命令。
- **核心模块:** `github_action_audit.py`(主审计)、`prompts.py`(审计 prompt 模板)、`findings_filter.py`(误报过滤)、`claude_api_client.py`(API 客户端)、`json_parser.py`(健壮 JSON 解析)、`evals/`(评测工具)。
- **测试:** `pytest claudecode -v`。

## 依赖

- **必需:** 一个 Anthropic Claude API key(须同时对 Claude API 与 Claude Code 启用),以 `claude-api-key` / GitHub secret 提供。
- **平台:** 开启 Actions 的 GitHub 仓库(主路径);也可经 evals 框架在本地运行。
- **权限:** workflow 需要 `pull-requests: write`(发评论)与 `contents: read`。
- **Python 依赖:** `claudecode/requirements.txt` 很轻——`PyGithub>=1.59.0`、`requests>=2.28.0`、`anthropic>=0.39.0`(解析用 stdlib)。没有重型 ML 栈,因为推理在远端。
- **Claude CLI:** `claude` 命令行工具需单独安装(Action 会处理);分析是通过它驱动的,而不仅是裸 API。

## 运维难度

**低。** 走顺路径就是一个约 15 行的 workflow 文件加一个 secret——无服务器、无数据存储、无需自托管模型(推理是远端 Claude API)。日常维护主要两件事:成本控制(token 花费随 PR 量和 `run-every-commit` 增长,注意 20 分钟的 `claudecode-timeout`)和 prompt-injection 约束(你必须配置 fork/外部贡献者的批准闸门)。调误报过滤器或自定义扫描指令是可选的文件式配置。主要残余风险是运维而非基础设施:pin `@main` 意味着上游改动可能在没有版本号变化的情况下改变行为。

## 存疑（未验证）

- [未验证] `gh` 报告 `latestRelease: null`,star 约 5.37k(截至 2026-02,最近 push 2026-02-11);GitHub star 不可靠且对时间敏感——仅供参考。
- [未验证] 无文档化的原生 SARIF / GitHub code-scanning 导出;把 finding 接进 security tab 可能需要自定义胶水代码。
- [未验证] 仓库语言占比(约 89.6% Python / 7.2% TS / 3.2% JS)是 GitHub 快照,随时间变化。
- [推断] 默认模型 `claude-opus-4-1-20250805` 是写作时 README 的默认值,上游可能上调;依赖某具体模型/成本画像前请核实当前默认。
- [推断] 单次成本与延迟取决于 diff 大小、所选模型和 `run-every-commit`;此处未发布一方成本数字。
- [未验证] `claudecode/requirements.txt`(2026-06-26 核实)仅 pin 了 `PyGithub>=1.59.0`、`requests>=2.28.0`、`anthropic>=0.39.0`,并注明 `claude` CLI 需单独安装——上游后续可能新增依赖。
