# web-scraping

> 分类节点。从网页抓取并提取内容/结构——文章正文提取与 HTML 解析。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **newspaper** | 用来从新闻 URL 批量提取正文、作者和元数据——但原版（newspaper3k）已陈旧，活跃路径是 newspaper4k 分叉。 | [→](newspaper.zh.md) |
| **requests-html** | 可作为小型 requests + HTML 解析脚本参考——基本停更（~2 年没动），JS 渲染路径脆弱；新项目优先 Playwright + parsel。 | [→](requests-html.zh.md) |
| **Readability.js** | 当你需要用 Firefox 阅读视图那套久经考验的引擎，把网页剥离成纯文章（标题、作者、正文）时用它——但它只解析你传入的 DOM，不会抓取 URL，也不会渲染重 JS 的 SPA。 | [→](readability-js.zh.md) |
| **python-readability** | 当你的 Python 流水线需要从已抓取的 HTML 中用 lxml 快速抽取正文、不依赖浏览器或 Node 时用它——但它单人维护、更新缓慢，而 trafilatura 在抽取基准上往往得分更高。 | [→](python-readability.zh.md) |
| **dragnet** | 当你有标注数据、想要一个可训练、还能把正文与用户评论分离的 ML 抽取器时用它——但它近乎停滞，依赖锁死老旧（scikit-learn<0.21、ftfy<5），在现代技术栈上安装会很痛苦。 | [→](dragnet.zh.md) |
| **boilerpipe** | 当你确实需要一个 JVM 原生、依赖轻量、基于经典算法的正文抽取器时用它——但仓库实际上已废弃（末次提交 2018-01），内置依赖陈旧，且不会再有安全修复。 | [→](boilerpipe.zh.md) |
| **fuck-login** | 当你想读 2016 年代「如何脚本化登录（CSRF／RSA／验证码）」的示例代码时用它——但它自 2018 年起已废弃、无许可证，脚本如今基本失效。 | [→](fuck-login.zh.md) |
| **gopup** | 当你想一行代码把中国公开数据（搜索指数、CPI、Shibor）拉进 pandas DataFrame 做学术研究时用它——但它自 2023 年起停更、无许可证，源站一变接口就失效。 | [→](gopup.zh.md) |
| **PRAW** | 当你的数据源就是 Reddit、想走官方 OAuth 合规路径并自带限速处理时用它——但真正的边界是 Reddit 自家的 API 条款、配额与定价，而非这个库。 | [→](praw.zh.md) |
| **Scrapyd** | 当你需要把本地 Scrapy 爬虫部署到服务器、通过 HTTP API 做定时与多版本调度时用它——但它只能跑 Scrapy 且默认无鉴权，暴露 6800 端口前务必先加认证。 | [→](scrapyd.zh.md) |
| **SpiderKeeper** | 当运行 Scrapyd 的小团队想要最简单的浏览器面板来部署和定时调度爬虫时用它——但它自 2023 年已停更且默认 admin/admin 鉴权，切勿暴露在不可信网络。 | [→](spiderkeeper.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [newspaper](newspaper.zh.md) | ✅ | 用来从新闻 URL 批量提取正文、作者和元数据——但原版（newspaper3k）已陈旧，活跃路径是 newspaper4k 分叉。 |
| [requests-html](requests-html.zh.md) | ✅ | 可作为小型 requests + HTML 解析脚本参考——基本停更（~2 年没动），JS 渲染路径脆弱；新项目优先 Playwright + parsel。 |
| [Readability.js](readability-js.zh.md) | ✅ | 当你需要用 Firefox 阅读视图那套久经考验的引擎，把网页剥离成纯文章（标题、作者、正文）时用它——但它只解析你传入的 DOM，不会抓取 URL，也不会渲染重 JS 的 SPA。 |
| [python-readability](python-readability.zh.md) | ✅ | 当你的 Python 流水线需要从已抓取的 HTML 中用 lxml 快速抽取正文、不依赖浏览器或 Node 时用它——但它单人维护、更新缓慢，而 trafilatura 在抽取基准上往往得分更高。 |
| [dragnet](dragnet.zh.md) | ✅ | 当你有标注数据、想要一个可训练、还能把正文与用户评论分离的 ML 抽取器时用它——但它近乎停滞，依赖锁死老旧（scikit-learn<0.21、ftfy<5），在现代技术栈上安装会很痛苦。 |
| [boilerpipe](boilerpipe.zh.md) | ✅ | 当你确实需要一个 JVM 原生、依赖轻量、基于经典算法的正文抽取器时用它——但仓库实际上已废弃（末次提交 2018-01），内置依赖陈旧，且不会再有安全修复。 |
| [fuck-login](fuck-login.zh.md) | ✅ | 当你想读 2016 年代「如何脚本化登录（CSRF／RSA／验证码）」的示例代码时用它——但它自 2018 年起已废弃、无许可证，脚本如今基本失效。 |
| [gopup](gopup.zh.md) | ✅ | 当你想一行代码把中国公开数据（搜索指数、CPI、Shibor）拉进 pandas DataFrame 做学术研究时用它——但它自 2023 年起停更、无许可证，源站一变接口就失效。 |
| [PRAW](praw.zh.md) | ✅ | 当你的数据源就是 Reddit、想走官方 OAuth 合规路径并自带限速处理时用它——但真正的边界是 Reddit 自家的 API 条款、配额与定价，而非这个库。 |
| [Scrapyd](scrapyd.zh.md) | ✅ | 当你需要把本地 Scrapy 爬虫部署到服务器、通过 HTTP API 做定时与多版本调度时用它——但它只能跑 Scrapy 且默认无鉴权，暴露 6800 端口前务必先加认证。 |
| [SpiderKeeper](spiderkeeper.zh.md) | ✅ | 当运行 Scrapyd 的小团队想要最简单的浏览器面板来部署和定时调度爬虫时用它——但它自 2023 年已停更且默认 admin/admin 鉴权，切勿暴露在不可信网络。 |
| Scrapy / trafilatura / httpx + BeautifulSoup / Playwright | 未收录 | 各页对比里点到的其他抓取/提取工具。 |

## 什么该放这里

主要职责是**抓取网页并提取内容/结构**的工具——文章正文提取与 HTML 解析。不含浏览器驱动自动化（见 `web-automation`），不含爬虫代理池（见 `proxy-pool`）。
