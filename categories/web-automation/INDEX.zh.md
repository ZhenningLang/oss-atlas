# web-automation

> 三级路由的第 2 级。驱动/自动化 Web 界面——以编程方式或自然语言（浏览器自动化、页内 GUI agent）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 许可证 | 页面 |
|---|---|---|---|
| **page-agent** | 给已有 Web 应用（ERP/CRM/后台）用自然语言、在页内、无需后端改造地加一个能操作 UI 的 AI copilot。 | MIT | [→](page-agent.zh.md) |

## 对比矩阵

项目页里点到、但**尚未收录**的替代方案。

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [page-agent](page-agent.zh.md) | ✅ | 页内、DOM 当文本读、复用登录态、无后端/headless、LLM 无关——但只读文本（无视觉）、仅客户端、会把 DOM 发给外部 LLM。 |
| browser-use | 未收录 | 服务端、具视觉能力的 Python 浏览器 agent——能超越 DOM 文本、不依赖客户端，但基建更重（需真实/headless 浏览器）。 |
| Playwright / Puppeteer | 未收录 | 更底层、代码驱动、支持 headless——确定性强且强大，但基于选择器/脚本（非自然语言）、对 DOM 变化脆弱。 |
| Selenium | 未收录 | 成熟、普及的跨浏览器自动化——但纯手工、冗长、无自然语言层。 |
| Computer-use agents（Anthropic / OpenAI Operator） | 未收录 | 基于视觉、驱动任意像素 UI——但更慢、更贵，需要受控浏览器/VM。 |

## 什么该放这里

主要职责是**驱动 Web 界面**的工具——浏览器自动化框架与页内/GUI agent。不包括 HTTP/API 客户端、
无交互的纯爬虫、headless 渲染服务。
