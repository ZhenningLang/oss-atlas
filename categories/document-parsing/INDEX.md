# document-parsing

> Category node. Parse/convert documents (PDF/DOCX/…) into structured Markdown/JSON for gen-AI ingestion.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | A (5/6) | [→](docling.md) |
| **MarkItDown** | Use it when you need a lightweight Python library to convert various office documents and files to Markdown for LLM ingestion — simpler than Docling but less layout-aware. | ? (0/6) | [→](markitdown.md) |
| **olmOCR** | Use it when you must convert complex PDFs with equations, tables, handwriting, and multi-column layouts into clean Markdown for LLM training datasets — requires a GPU. | ? (0/6) | [→](olmocr.md) |
| **Marker** | Convert PDF to markdown + JSON quickly with high accuracy | ? (0/6) | [→](marker.md) |
| **unstructured** | Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding. | ? (0/6) | [→](unstructured.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Docling](docling.md) | ✅ | A (5/6) | Rich-document parsing (layout + tables) to structured Markdown/JSON; heavier model deps than plain text extraction. |
| [MarkItDown](markitdown.md) | ✅ | ? (0/6) | Lightweight Python library converting office documents and files to Markdown for LLM ingestion; simpler than Docling but less layout-aware. |
| [olmOCR](olmocr.md) | ✅ | ? (0/6) | VLM-based PDF linearization for LLM datasets; handles equations, tables, and handwriting but requires GPU. |
| [PageIndex](../rag-retrieval/pageindex.md) | ✅ | B (5/6) | Builds a retrieval index over long structured docs — downstream of parsing, not a parser. |
| unstructured.io / LlamaParse / Marker / PyMuPDF | 未收录 | — | Other document parsers/extractors named across the pages. |

## What belongs here

Libraries whose primary job is **parsing/converting documents into structured representations** for gen-AI/RAG. Not retrieval/indexing itself (see `rag-retrieval`), not document archiving/search (see `document-management`), not raw OCR (see `ocr`).
