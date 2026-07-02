---
name: MarkItDown
slug: markitdown
repo: https://github.com/microsoft/markitdown
category: document-parsing
tags: [document-conversion, markdown, pdf, office, llm-ingestion, python]
language: Python
license: MIT
maturity: v0.x, active, 162k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-06-24T15:32:46Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
    responsiveness:
      grade: ?
      raw: {}
    adoption:
      grade: A
      raw:
        stars: 162226
    longevity:
      grade: D
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# MarkItDown

A lightweight Python library for converting various files and office documents to Markdown, designed for LLM ingestion and text-analysis pipelines rather than high-fidelity human consumption.

![MarkItDown — health radar](../../assets/health/markitdown.svg)

## When to use

You're building a RAG pipeline, a document QA system, or an agent that needs to consume PDFs, Word documents, PowerPoint slides, Excel sheets, images, audio files, and HTML pages as structured text. You want a single Python library that turns these heterogeneous formats into clean Markdown — preserving headings, lists, tables, and links — so your LLM can process them without being overwhelmed by binary noise or proprietary formatting. You install MarkItDown via pip, call `convert()` on a file path, and get back Markdown text you can chunk, embed, or feed directly into a prompt. It is purpose-built for machine consumption, not pixel-perfect document reproduction.

## When NOT to use

- **High-fidelity document conversion for human reading.** The output is optimized for text-analysis tools; it may drop advanced formatting, flatten complex layouts, or simplify tables in ways that make the result less presentable for human readers. If you need a Word-to-PDF or PDF-to-Word converter for publishing, look elsewhere.
- **Document editing or round-tripping.** MarkItDown is one-way conversion (file → Markdown). It does not edit, modify, or write back to the original format.
- **Complex table and layout preservation.** While it attempts to retain tables and structure, heavily formatted documents with nested layouts, merged cells, or precise positioning will lose fidelity in the Markdown output. [未验证]
- **Production use without input sanitization.** The library performs I/O with the privileges of the current process and can access any resource the process can reach. In untrusted environments, sanitize inputs and call the narrowest `convert_*` function for your use case. [未验证]
- **OCR as a primary use case.** It can extract EXIF metadata and perform OCR on images, but dedicated OCR libraries (e.g., Tesseract) are more mature and configurable for pure text-extraction tasks.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Docling](docling.md) | ✅ | Rich-document parsing with layout + tables to structured Markdown/JSON. | Docling is heavier with model dependencies and focuses on structured output; MarkItDown is lighter and simpler, built for LLM ingestion. |
| unstructured.io | 未收录 | Enterprise-grade document parsing with chunking and embedding pipelines. | More mature ecosystem and cloud offerings; heavier dependencies and potential licensing costs for enterprise features. |
| LlamaParse | 未收录 | Parsing service from LlamaIndex with a hosted API. | Cloud-based, API-key required, good for complex PDFs; MarkItDown is local, free, and open-source. |
| Marker | 未收录 | Fast PDF-to-Markdown converter optimized for academic papers. | Specializes in PDF and claims high accuracy on research papers; MarkItDown covers more formats (Office, audio, HTML, etc.). |
| PyMuPDF | 未收录 | Low-level Python PDF library for extraction and manipulation. | A library for direct PDF page manipulation, not a high-level Markdown converter; more powerful but requires more code. |
| textract | 未收录 | Python library for extracting text from many formats. | Older project with broader format support but less focus on Markdown structure preservation for LLMs. |

## Tech stack

- **Python** — primary implementation language
- **Modular converter architecture** — separate converters per format (PDF, DOCX, PPTX, XLSX, images, audio, HTML, etc.)
- **Markdown output** — unified target format for all conversions

## Dependencies

- **Python 3.9+** — runtime environment
- **Optional format-specific dependencies** — some converters require additional packages (e.g., for OCR, audio transcription, or advanced PDF parsing)
- **No service or database** — pure library; runs in-process

## Ops difficulty

**Low.** `pip install markitdown` and import. The library is stateless and runs in-process; there is no service to deploy, no database to manage, and no persistent infrastructure. The main operational concern is keeping the Python environment and optional dependencies current, plus the input-sanitization discipline mentioned in the security notes.

## Health & viability

- **Maintenance**: Active — last push 2026-06-24, indicating recent development. The project is young but has Microsoft's AutoGen team behind it, which suggests organizational commitment to continued development. [未验证]
- **Governance**: Owned by Microsoft (`microsoft` organization). This provides strong backing and a low bus-factor risk compared to single-maintainer projects. Roadmap alignment with Microsoft's broader AI tooling ecosystem is plausible. [推断]
- **Backing**: Microsoft / AutoGen team. A major corporate backing is a significant positive signal for longevity and maintenance, though it also means the roadmap may align with Microsoft's product priorities.
- **Adoption**: Extremely high star count (162k) for a project created in late 2024. The popularity reflects both genuine demand for document-to-LLM pipelines and the visibility boost from the Microsoft brand. [推断]
- **Age & Lindy**: Created 2024-11 (~8 months old at verification). This is extremely young with no meaningful Lindy track record. The Microsoft backing partially offsets the age risk, but breaking changes in a v0.x project should be expected.
- **Risk flags**: MIT license is clean and permissive. The main risk is the project's youth — APIs, converter quality, and supported formats may shift significantly. Also, being a Microsoft project means it could be deprioritized if it no longer serves strategic goals, though the AutoGen tie-in suggests it has a concrete use case.

## Caveats (unverified)

- [未验证] The Microsoft AutoGen team authorship is stated in the README badge; the exact team structure and long-term maintenance commitment are not publicly documented.
- [未验证] Output quality varies significantly by format and document complexity; the "Markdown is optimized for LLMs" disclaimer means human readability is explicitly a secondary goal.
- [未验证] The security note about I/O privileges and input sanitization should be treated as a real operational concern in multi-tenant or untrusted-input environments.
- [推断] The 162k star count on an 8-month-old project is likely amplified by the Microsoft brand and the 2024–2025 LLM-tooling hype cycle.
- [未验证] Support for audio transcription and image OCR may require additional external dependencies (e.g., Whisper, Tesseract) that are not bundled by default.
