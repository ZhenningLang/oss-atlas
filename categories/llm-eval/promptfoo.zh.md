---
name: promptfoo
slug: promptfoo
repo: https://github.com/promptfoo/promptfoo
category: llm-eval
tags: [llm-eval, red-teaming, prompt-testing, ci-cd, rag, vulnerability-scanning, cli, local-first]
language: TypeScript
license: MIT
maturity: v0.121.x, active (2026-06)
last_verified: 2026-06-26
type: tool
---

# promptfoo

一个 local-first 的 CLI + 库,把 prompt/模型/RAG/agent 的评测变成声明式 YAML 测试套件,内置红队/漏洞扫描器,并能接进 CI/CD。

## 何时使用

你是在做 LLM 功能交付的工程师——一个客服 agent、一个 RAG 回答接口、一个分类 prompt——你已经厌倦了在 playground 里肉眼看输出、觉得"差不多能用"就上线。你想要一套回归测试:固定的一组输入、能在 prompt 改动让质量下降时真正让构建失败的断言,以及一个跨 GPT、Claude、Gemini 和本地 Ollama 模型的并排视图,这样你是凭证据而不是凭感觉选型。promptfoo 用一份 `promptfooconfig.yaml` 解决这个问题:把整套评测——prompt、provider、测试用例、断言(精确匹配、JSON schema、向量相似度,或 LLM 当裁判的 `llm-rubric`)——写进配置,然后本地跑 `npx promptfoo eval`,再用 `promptfoo view` 在浏览器里看结果矩阵。把同一条命令接进 CI,质量回归就会让 PR 失败。

当安全评审来问"这个 agent 会不会被越狱 / 会不会泄露 system prompt / 会不会以错误方式处理 PII"时,你也会用它。`redteam` 这一侧会针对你的线上接口生成对抗性探针(prompt 注入、越狱、有害内容、PII,以及 OWASP-LLM 风格的若干类别),并报告哪些攻击得手——把临时的渗透测试变成每次发版前都能重复跑的扫描。因为评测在你本机、用你自己的 provider key 运行,你的 prompt 和测试数据不必离开你的环境。

## 何时不用

- **你要的是开箱即用、面向团队的托管评测平台**(自带托管看板、RBAC、历史趋势存储)。promptfoo 是 local-first;云端分享/团队功能存在,但有 SLA、带治理的平台是商业版 Promptfoo,而非开源 CLI。需要交钥匙 SaaS 时,可权衡 LangSmith / Braintrust / Langfuse。
- **你不在 Node 工具链里、也不想引入它。** 它是 TypeScript/Node 包(Node `^20.20.0 || >=22.22.0`);虽然有 `pip install promptfoo` 包装,但引擎是 Node。如果你的栈和团队纯 Python、想要原生 fixture,DeepEval(未收录)/ Python 原生 harness 更顺手。
- **你要做严谨的学术基准测试**(MMLU/HELM 式排行榜、统计报告,几百个标准任务)。promptfoo 是为*你自己应用的*测试用例而建,不是跑标准基准电池——那种场景用 lm-evaluation-harness / HELM。
- **你指望红队扫描器当合规保证。** 它给出的是*发现项*,且攻击覆盖随版本变化;通过一次扫描是证据,不是安全的证明。把结果当成会变动的信号,而非认证。
- **你想要零配置、一个魔法分数。** 价值在于写出好的断言和测试用例;如果没人维护评测集,你得到的只是一个意义不大的绿勾。

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| DeepEval | 未收录 | Python 原生评测框架(pytest 风格,G-Eval/faithfulness 等指标);更适合 Python 团队和 RAG 指标深度。promptfoo 胜在语言无关的 YAML 配置、并排模型矩阵和集成红队。 |
| Langfuse | 未收录 | 追踪/可观测性 + 评测平台(可自托管,带 UI 和数据集后端);强在生产监控和趋势历史。promptfoo 更轻、CLI 优先、偏红队,而非可观测性后端。 |
| LangSmith | 未收录 | 托管的 LangChain 评测/可观测性 SaaS;LangChain 集成深、看板托管,但闭源、以云为中心。promptfoo 开源、local-first、框架无关。 |
| Braintrust | 未收录 | 商业评测/实验平台,托管打分与日志;团队 UX 打磨好。promptfoo 用开放、自跑的 CLI 换掉这套托管平台。 |
| Garak | 未收录 | 专门的 LLM 漏洞扫描器(只做红队,Python)。与 promptfoo 的 `redteam` 范围重叠,但不是通用评测/断言 harness。 |
| Giskard | 未收录 | 面向 ML+LLM 的开源测试/红队,扫描-报告模式;ML 范围更广、以 Python 为中心。promptfoo 更聚焦 prompt/CI 工作流。 |

## 技术栈

- **语言:** TypeScript / Node.js(CLI 命令为 `promptfoo` 和 `pf`)。
- **核心库(依 package.json,v0.121.17):** `commander`(CLI)、`express` + `compression`/`cors`(本地 Web 查看器服务)、`drizzle-orm` + `@libsql/client`(本地 SQLite 评测存储)、`ajv`/`ajv-formats`(JSON-schema 断言)、`@anthropic-ai/sdk` 和 `ai` SDK 及众多 provider 客户端、`@opentelemetry/*`(追踪)、`chokidar`/`execa`/`chalk`(CLI 基建)。
- **配置面:** 声明式 `promptfooconfig.yaml`(prompts、providers、tests、assertions、`redteam`);也可作为库使用或接进 CI。
- **断言类型:** 确定性(equals/contains/regex/JSON-schema)、相似度(embeddings)、模型评分(`llm-rubric`,LLM 当裁判)。

## 依赖

- **运行时:** Node.js `^20.20.0 || >=22.22.0`(依 `engines`)。无需部署数据库——它用本地 libsql/SQLite 文件存评测历史。
- **安装:** `npm install -g promptfoo`、`brew install promptfoo`,或用 `npx promptfoo@latest` 零安装运行;另有 `pip install promptfoo` 包装(底层仍需 Node)。[推断]
- **外部服务:** 你要评测的 LLM provider——你自备 API key(OpenAI/Anthropic/Azure/Bedrock/Google/Ollama 等);本地模型经 Ollama 需自带运行时。
- **可选:** 相似度断言需要 embeddings provider;只有选用托管分享/团队功能时才需要云账号。

## 运维难度

**低。** 核心循环基本无需运维:安装或 `npx`、写一份 YAML、配好 provider 环境变量、跑 `eval` 和 `view`。状态是一个本地文件,Web UI 是一个按需启动的内置 Express 服务,CI 用法就是在 job 里跑同一条 CLI。难度升到**低到中**仅在于:为团队自托管分享、在 CI 里管理大量 provider 凭据/限流,或维护庞大的红队配置——而你的评测成本会变成真实的 provider API 花费,这才是要盯的,而非基础设施。

## 存疑（未验证）

- [未验证] 观测到 `promptfoo` 包最新版本为 0.121.17,发布于 2026-06-16(独立的 `code-scan-action` 单独发版,如 0.1.8)。发版节奏快,pin 之前请重新核实。
- [未验证] 截至 2026-06 star 约 22.6k——GitHub star 不可靠且对时间敏感,仅供参考。
- [未验证] README 称其"为服务 1000 万+ 生产用户的 LLM 应用提供支撑",并"被 OpenAI 和 Anthropic 使用"——这些是项目自身的营销表述,本页未独立证实。
- [推断] `pip install promptfoo` 这条路是 Node 包的薄包装;真正的引擎和 `engines` 约束都是 Node——若纯 Python 部署很关键,请对照当前文档确认。
- [推断] 具体红队攻击类别(OWASP-LLM 覆盖、越狱/PII 插件)和支持的 provider 列表随版本变动;依赖某具体攻击或 provider 前请核对当前文档。
- [未验证] 许可证依仓库元数据读作 MIT;对比表(DeepEval/Langfuse/LangSmith/Braintrust/Garak/Giskard 的定位)是基于通用认知的判断,非逐项实测对比。
