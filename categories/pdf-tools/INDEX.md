# pdf-tools

> Category node. Render, read, and manipulate PDF files.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **PDF.js** | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. | A (6/6) | [→](pdfjs.md) |
| **pdf-lib** | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. | — | [→](pdf-lib.md) |
| **jsPDF** | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. | — | [→](jspdf.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.md) | ✅ | A (6/6) | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. |
| [pdf-lib](pdf-lib.md) | ✅ | — | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. |
| [jsPDF](jspdf.md) | ✅ | — | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. |
| PyMuPDF / pdfplumber | 未收录 | — | Server-side PDF text/table extraction and rendering tools; named across the pages. |

## What belongs here

Tools whose primary job is to **render, read, or manipulate PDF files** — viewers, parsers, generators, and editors. Not parsing documents into structured Markdown/JSON for gen-AI (see `document-parsing`), not OCR engines (see `ocr`).
