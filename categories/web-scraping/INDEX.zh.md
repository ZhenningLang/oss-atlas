# web-scraping

> 分类节点。从网页抓取并提取内容/结构——文章正文提取与 HTML 解析。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **newspaper** | 用来从新闻 URL 批量提取正文、作者和元数据——但原版(newspaper3k)已陈旧，活跃路径是 newspaper4k 分叉。 | [→](newspaper.zh.md) |
| **requests-html** | 可作为小型 requests + HTML 解析脚本参考——基本停更(~2 年没动)，JS 渲染路径脆弱；新项目优先 Playwright + parsel。 | [→](requests-html.zh.md) |
| **Readability.js** | Firefox Reader View 背后那个 readability 库的独立版本——给它一个 DOM document，拿回文章的标题、作者署名和清理过的正文，导航、广告和样板内容都被剥掉。 | [→](readability-js.zh.md) |
| **python-readability** | 一个快速、基于 lxml 的 arc90 Readability Python 移植——递给它一个 HTML 文档，它返回清理过的正文（`summary()`）和标题（`title()`），剥掉导航、广告和样板。 | [→](python-readability.zh.md) |
| **dragnet** | 一种用机器学习做网页正文抽取的方法——训练好的模型从页面 HTML 里拉出正文（可选连用户评论一起），靠多样的文本/标记特征而非手调启发式。 | [→](dragnet.zh.md) |
| **boilerpipe** | 一个用于从 HTML 做样板移除和全文抽取的 Java 库——经典的、算法驱动的路子（浅层文本特征、链接密度、标签比率），把文章抽出来、丢掉导航、广告和周边杂物。 | [→](boilerpipe.zh.md) |
| **fuck-login** | 一批约 20 个 Python 脚本，逐个复刻知名网站（多为中文站：知乎、微博、百度、京东、B 站、GitHub、豆瓣）的登录流程，让你把拿到的会话 cookie 带进爬虫。这是一个 2016 年的教学仓库，作者已明确**不再维护**。 | [→](fuck-login.zh.md) |
| **gopup** | 一个 Python 库，把一大堆（多为中文的）公开数据源封装成返回 pandas DataFrame 的单行调用——百度/微博/谷歌搜索指数、中国宏观指标（CPI/PPI/PMI、货币供应量、汇率）、Shibor/LPR 利率、独角兽公司名单、影视票房和疫情数据等等。 | [→](gopup.zh.md) |
| **PRAW** | “Python Reddit API Wrapper”——一个 Python 包，在 Reddit 官方 OAuth API 之上给你类型化、Pythonic 的对象（Submission、Comment、Subreddit、Redditor），并替你处理限速合规，让你不必在代码里到处撒 `sleep`。 | [→](praw.zh.md) |
| **Scrapyd** | 一个通过 JSON HTTP API 部署并运行 Scrapy 爬虫的服务守护进程——把 Scrapy 项目打成 egg、上传，然后远程调度/取消/监控抓取作业。它是 Scrapy 官方组织出品、把"在生产里跑 Scrapy"这件事标准化的守护进程。 | [→](scrapyd.zh.md) |
| **SpiderKeeper** | 一个基于 Flask、叠在 Scrapyd 之上的 Scrapy 爬虫管理 web UI / 看板——在浏览器里部署项目、调度周期作业、查看运行统计。它自己什么都不抓；它是覆盖在一个或多个 Scrapyd 服务器之上的管理层。轻量、流行，且大体已陈旧。 | [→](spiderkeeper.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [newspaper](newspaper.zh.md) | ✅ | 用来从新闻 URL 批量提取正文、作者和元数据——但原版(newspaper3k)已陈旧，活跃路径是 newspaper4k 分叉。 |
| [requests-html](requests-html.zh.md) | ✅ | 可作为小型 requests + HTML 解析脚本参考——基本停更(~2 年没动)，JS 渲染路径脆弱；新项目优先 Playwright + parsel。 |
| [Readability.js](readability-js.zh.md) | ✅ | Firefox Reader View 背后那个 readability 库的独立版本——给它一个 DOM document，拿回文章的标题、作者署名和清理过的正文，导航、广告和样板内容都被剥掉。 |
| [python-readability](python-readability.zh.md) | ✅ | 一个快速、基于 lxml 的 arc90 Readability Python 移植——递给它一个 HTML 文档，它返回清理过的正文（`summary()`）和标题（`title()`），剥掉导航、广告和样板。 |
| [dragnet](dragnet.zh.md) | ✅ | 一种用机器学习做网页正文抽取的方法——训练好的模型从页面 HTML 里拉出正文（可选连用户评论一起），靠多样的文本/标记特征而非手调启发式。 |
| [boilerpipe](boilerpipe.zh.md) | ✅ | 一个用于从 HTML 做样板移除和全文抽取的 Java 库——经典的、算法驱动的路子（浅层文本特征、链接密度、标签比率），把文章抽出来、丢掉导航、广告和周边杂物。 |
| [fuck-login](fuck-login.zh.md) | ✅ | 一批约 20 个 Python 脚本，逐个复刻知名网站（多为中文站：知乎、微博、百度、京东、B 站、GitHub、豆瓣）的登录流程，让你把拿到的会话 cookie 带进爬虫。这是一个 2016 年的教学仓库，作者已明确**不再维护**。 |
| [gopup](gopup.zh.md) | ✅ | 一个 Python 库，把一大堆（多为中文的）公开数据源封装成返回 pandas DataFrame 的单行调用——百度/微博/谷歌搜索指数、中国宏观指标（CPI/PPI/PMI、货币供应量、汇率）、Shibor/LPR 利率、独角兽公司名单、影视票房和疫情数据等等。 |
| [PRAW](praw.zh.md) | ✅ | “Python Reddit API Wrapper”——一个 Python 包，在 Reddit 官方 OAuth API 之上给你类型化、Pythonic 的对象（Submission、Comment、Subreddit、Redditor），并替你处理限速合规，让你不必在代码里到处撒 `sleep`。 |
| [Scrapyd](scrapyd.zh.md) | ✅ | 一个通过 JSON HTTP API 部署并运行 Scrapy 爬虫的服务守护进程——把 Scrapy 项目打成 egg、上传，然后远程调度/取消/监控抓取作业。它是 Scrapy 官方组织出品、把"在生产里跑 Scrapy"这件事标准化的守护进程。 |
| [SpiderKeeper](spiderkeeper.zh.md) | ✅ | 一个基于 Flask、叠在 Scrapyd 之上的 Scrapy 爬虫管理 web UI / 看板——在浏览器里部署项目、调度周期作业、查看运行统计。它自己什么都不抓；它是覆盖在一个或多个 Scrapyd 服务器之上的管理层。轻量、流行，且大体已陈旧。 |
| Scrapy / trafilatura / httpx + BeautifulSoup / Playwright | 未收录 | 各页对比里点到的其他抓取/提取工具。 |

## 什么该放这里

主要职责是**抓取网页并提取内容/结构**的工具——文章正文提取与 HTML 解析。不含浏览器驱动自动化(见 `web-automation`)，不含爬虫代理池(见 `proxy-pool`)。
