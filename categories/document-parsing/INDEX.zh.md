# document-parsing

> 分类节点。把文档（PDF/DOCX/…）解析/转换成结构化 Markdown/JSON，供 gen-AI 消费。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | [→](docling.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Docling](docling.zh.md) | ✅ | 富文档解析（版面 + 表格）成结构化 Markdown/JSON；模型依赖比纯文本提取更重。 |
| [PageIndex](../rag-retrieval/pageindex.zh.md) | ✅ | 在长结构化文档上建检索索引——位于解析之后，本身不是解析器。 |
| unstructured.io / LlamaParse / Marker / PyMuPDF | 未收录 | 各页对比里点到的其他文档解析/提取器。 |

## 什么该放这里

主要职责是把**文档解析/转换成结构化表示**供 gen-AI/RAG 用的库。不含检索/索引本身（见 `rag-retrieval`），不含文档归档/检索（见 `document-management`），不含纯 OCR（见 `ocr`）。
