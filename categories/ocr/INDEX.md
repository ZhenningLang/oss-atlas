# ocr

> Category node. Optical character recognition engines — image/scan to text.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Tesseract** | Use it when you need offline, embeddable OCR over clean printed text in 100+ languages — not wild photos or handwriting. | A (5/6) | [→](tesseract.md) |
| **LaTeX-OCR (pix2tex)** | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. | C (3/6) | [→](latex-ocr.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Tesseract](tesseract.md) | ✅ | A (5/6) | Mature offline OCR engine for clean printed text; weak on layout, handwriting, in-the-wild photos. |
| [LaTeX-OCR (pix2tex)](latex-ocr.md) | ✅ | C (3/6) | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. |
| PaddleOCR / EasyOCR / TrOCR / Cloud Vision / Textract | 未收录 | — | Deep-learning / cloud OCR named across the pages (better on messy inputs). |

## What belongs here

Engines/libraries whose primary job is **recognizing text in images/scans**. Not document layout-and-table parsing for gen-AI (see `document-parsing`), not document archiving/search (see `document-management`).
