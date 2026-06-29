# web-automation

> 分类节点。驱动或自动化 Web 界面——浏览器自动化，或页内自然语言 GUI agent。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | B（6/6） | [→](page-agent.zh.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 | A（6/6） | [→](chrome-devtools-mcp.zh.md) |
| **Cua** | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 | B（6/6） | [→](cua.zh.md) |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | B（6/6） | [→](agent-browser.zh.md) |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | B（6/6） | [→](selenium.zh.md) |
| **PhantomJS** | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 | D（5/6） | [→](phantomjs.zh.md) |
| **Selenium Wire** | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 | D（5/6） | [→](selenium-wire.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [page-agent](page-agent.zh.md) | ✅ | B（6/6） | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 |
| [Chrome DevTools MCP](chrome-devtools-mcp.zh.md) | ✅ | A（6/6） | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 |
| [Cua](cua.zh.md) | ✅ | B（6/6） | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 |
| [Agent Browser](agent-browser.zh.md) | ✅ | B（6/6） | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 |
| [Selenium](selenium.zh.md) | ✅ | B（6/6） | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 |
| [PhantomJS](phantomjs.zh.md) | ✅ | D（5/6） | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 |
| [Selenium Wire](selenium-wire.zh.md) | ✅ | D（5/6） | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 |
| Playwright / Puppeteer | 未收录 | — | 各页对比里点到的更底层浏览器自动化库。 |

## 什么该放这里

**驱动或自动化 Web/浏览器（乃至计算机）GUI** 的工具——headless 浏览器自动化、computer-use，或页内 GUI agent。不含服务端爬虫框架，不含企业级纯桌面 RPA。
