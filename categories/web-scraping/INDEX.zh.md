# web-scraping

> 分类节点。从网页抓取并提取内容/结构——文章正文提取与 HTML 解析。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **newspaper** | 用来从新闻 URL 批量提取正文、作者和元数据——但原版(newspaper3k)已陈旧，活跃路径是 newspaper4k 分叉。 | [→](newspaper.zh.md) |
| **requests-html** | 可作为小型 requests + HTML 解析脚本参考——基本停更(~2 年没动)，JS 渲染路径脆弱；新项目优先 Playwright + parsel。 | [→](requests-html.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [newspaper](newspaper.zh.md) | ✅ | 用来从新闻 URL 批量提取正文、作者和元数据——但原版(newspaper3k)已陈旧，活跃路径是 newspaper4k 分叉。 |
| [requests-html](requests-html.zh.md) | ✅ | 可作为小型 requests + HTML 解析脚本参考——基本停更(~2 年没动)，JS 渲染路径脆弱；新项目优先 Playwright + parsel。 |
| Scrapy / trafilatura / httpx + BeautifulSoup / Playwright | 未收录 | 各页对比里点到的其他抓取/提取工具。 |

## 什么该放这里

主要职责是**抓取网页并提取内容/结构**的工具——文章正文提取与 HTML 解析。不含浏览器驱动自动化(见 `web-automation`)，不含爬虫代理池(见 `proxy-pool`)。
