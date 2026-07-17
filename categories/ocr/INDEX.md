# ocr

> Category node. Optical character recognition engines — image/scan to text.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Tesseract** | Use it when you need offline, embeddable OCR over clean printed text in 100+ languages — not wild photos or handwriting. | A (5/6) | [→](tesseract.md) |
| **LaTeX-OCR (pix2tex)** | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. | C (3/6) | [→](latex-ocr.md) |
| **Laravel OCR** | Use it when an existing Laravel application needs one wrapper for Tesseract and cloud OCR plus template/regex extraction and persistence; not for multi-page scanned PDFs or layout-aware OCR, and the repository lacks a license file. | D (5/6) | [→](laravel-ocr.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Tesseract](tesseract.md) | ✅ | A (5/6) | Mature offline OCR engine for clean printed text; weak on layout, handwriting, in-the-wild photos. |
| [LaTeX-OCR (pix2tex)](latex-ocr.md) | ✅ | C (3/6) | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. |
| [Laravel OCR](laravel-ocr.md) | ✅ | D (5/6) | Laravel-native OCR driver switching plus template/regex business extraction; saves application plumbing but has shallow PDF/layout handling, incomplete workflows, and no repository license text. |
| PaddleOCR / EasyOCR / TrOCR / Cloud Vision / Textract | 未收录 | — | Deep-learning / cloud OCR named across the pages (better on messy inputs). |

## What belongs here

Engines/libraries whose primary job is **recognizing text in images/scans**. Not document layout-and-table parsing for gen-AI (see `document-parsing`), not document archiving/search (see `document-management`).
