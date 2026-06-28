# pdf-tools

> 分类节点。渲染、读取与处理 PDF 文件。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | [→](pdfjs.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [PDF.js](pdfjs.zh.md) | ✅ | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 |
| pdf-lib / jsPDF / PyMuPDF / pdfplumber | 未收录 | 各页对比里点到的 PDF 生成/编辑与服务端提取工具。 |

## 什么该放这里

主要职责是**渲染、读取或处理 PDF 文件**的工具——查看器、解析器、生成器与编辑器。不含把文档解析成结构化 Markdown/JSON 供 gen-AI 消费(见 `document-parsing`)，不含 OCR 引擎(见 `ocr`)。
