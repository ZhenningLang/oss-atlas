# document-parsing

> Category node. Parse/convert documents (PDF/DOCX/…) into structured Markdown/JSON for gen-AI ingestion.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | [→](docling.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Docling](docling.md) | ✅ | Rich-document parsing (layout + tables) to structured Markdown/JSON; heavier model deps than plain text extraction. |
| [PageIndex](../rag-retrieval/pageindex.md) | ✅ | Builds a retrieval index over long structured docs — downstream of parsing, not a parser. |
| unstructured.io / LlamaParse / Marker / PyMuPDF | 未收录 | Other document parsers/extractors named across the pages. |

## What belongs here

Libraries whose primary job is **parsing/converting documents into structured representations** for gen-AI/RAG. Not retrieval/indexing itself (see `rag-retrieval`), not document archiving/search (see `document-management`), not raw OCR (see `ocr`).
