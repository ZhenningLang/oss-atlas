# document-parsing

> 分类节点。把文档（PDF/DOCX/…）解析/转换成结构化 Markdown/JSON，供 gen-AI 消费。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | A（5/6） | [→](docling.zh.md) |
| **MarkItDown** | 当你需要一个轻量级 Python 库把各类办公文档和文件转成 Markdown 以喂给 LLM 时用它——比 Docling 更简单，但对版面感知较弱。 | ?（0/6） | [→](markitdown.zh.md) |
| **olmOCR** | 当你需要把带公式、表格、手写体和多栏版面的复杂 PDF 转成干净 Markdown 以用于 LLM 训练数据集时用它——需要 GPU。 | ?（0/6） | [→](olmocr.zh.md) |
| **Marker** | Convert PDF to markdown + JSON quickly with high accuracy | ?（0/6） | [→](marker.zh.md) |
| **unstructured** | Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding. | ?（0/6） | [→](unstructured.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Docling](docling.zh.md) | ✅ | A（5/6） | 富文档解析（版面 + 表格）成结构化 Markdown/JSON；模型依赖比纯文本提取更重。 |
| [MarkItDown](markitdown.zh.md) | ✅ | ?（0/6） | 轻量级 Python 库，将办公文档和文件转换为 Markdown 供 LLM 摄入；比 Docling 更简单，但版面感知较弱。 |
| [olmOCR](olmocr.zh.md) | ✅ | ?（0/6） | 基于 VLM 的 PDF 线性化，面向 LLM 数据集；支持公式、表格和手写体，但需要 GPU。 |
| [PageIndex](../rag-retrieval/pageindex.zh.md) | ✅ | B（5/6） | 在长结构化文档上建检索索引——位于解析之后，本身不是解析器。 |
| unstructured.io / LlamaParse / Marker / PyMuPDF | 未收录 | — | 各页对比里点到的其他文档解析/提取器。 |

## 什么该放这里

主要职责是把**文档解析/转换成结构化表示**供 gen-AI/RAG 用的库。不含检索/索引本身（见 `rag-retrieval`），不含文档归档/检索（见 `document-management`），不含纯 OCR（见 `ocr`）。
