# document-management

> Level 2 of 3. Ingest, OCR, tag, and search scanned documents / paperwork.
> 选「文档归档/OCR/全文检索」系统。
> ← back to [category route](../../INDEX.md)

## Projects in this category

| Project | Use when (一句话) | License | Page |
|---|---|---|---|
| **paperless-ngx** | Self-host a searchable archive of scanned paperwork (invoices, bills, letters) on a trusted home server / NAS, with OCR + auto-tagging. 在可信内网自托管「扫描件归档+OCR+检索」。 | GPL-3.0 | [→](paperless-ngx.md) |

## Comparison matrix

Substitutes named in the project page but **not yet indexed** (`未收录`).

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [paperless-ngx](paperless-ngx.md) | ✅ | Best-momentum self-hosted DMS for personal/small-team scan archives; great OCR + auto-tagging — but no encryption at rest, weak multi-tenant permissions, not an enterprise EDMS. |
| Mayan EDMS | 未收录 | Heavier enterprise EDMS: real workflow engine, versioning, granular permissions (Apache-2.0) — but far steeper to operate, overkill for a personal archive. |
| Docspell | 未收录 | Strong email ingestion + metadata extraction — but Scala/JVM stack, heavier memory, smaller community. |
| Teedy / sismics docs | 未收录 | Lightweight Java DMS, clean UI, modest resources — but weaker OCR/auto-tagging, smaller momentum. |
| Self-built (Tesseract + Meilisearch + object storage) | 未收录 | Full control over encryption/schema — but you build and maintain the whole pipeline. |

## What belongs here

Systems whose primary job is to **ingest, OCR, organize, and retrieve** documents. Not general
file sync (Nextcloud), not note-taking, not collaborative authoring.
