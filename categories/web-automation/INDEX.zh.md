# web-automation

> 分类节点。驱动或自动化 Web 界面——浏览器自动化，或页内自然语言 GUI agent。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | [→](page-agent.zh.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome(性能 trace、网络、控制台、堆内存)时使用。 | [→](chrome-devtools-mcp.zh.md) |
| **Cua** | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统(而非仅网页)时使用。 | [→](cua.zh.md) |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | [→](agent-browser.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [page-agent](page-agent.zh.md) | ✅ | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 |
| [Chrome DevTools MCP](chrome-devtools-mcp.zh.md) | ✅ | 当 agent 需要驱动并用 DevTools 检查真实 Chrome(性能 trace、网络、控制台、堆内存)时使用。 |
| [Cua](cua.zh.md) | ✅ | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统(而非仅网页)时使用。 |
| [Agent Browser](agent-browser.zh.md) | ✅ | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 |
| Playwright / Puppeteer / Selenium | 未收录 | 各页对比里点到的更底层浏览器自动化库。 |

## 什么该放这里

**驱动或自动化 Web/浏览器(乃至计算机)GUI** 的工具——headless 浏览器自动化、computer-use，或页内 GUI agent。不含服务端爬虫框架，不含企业级纯桌面 RPA。
