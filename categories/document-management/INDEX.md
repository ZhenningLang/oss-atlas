# document-management

> Level 2 of 3. Ingest, OCR, tag, and full-text-search scanned documents / paperwork.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | License | Page |
|---|---|---|---|
| **paperless-ngx** | Self-host a searchable archive of scanned paperwork (invoices, bills, letters) on a trusted home server / NAS, with OCR + auto-tagging. | GPL-3.0 | [→](paperless-ngx.md) |

## Comparison matrix

Substitutes named in the project page but **not yet indexed**.

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [paperless-ngx](paperless-ngx.md) | ✅ | Best-momentum self-hosted DMS for personal/small-team scan archives; great OCR + auto-tagging — but no encryption at rest, weak multi-tenant permissions, not an enterprise EDMS. |
| Mayan EDMS | not indexed | Heavier enterprise EDMS: real workflow engine, versioning, granular permissions (Apache-2.0) — but far steeper to operate, overkill for a personal archive. |
| Docspell | not indexed | Strong email ingestion + metadata extraction — but Scala/JVM stack, heavier memory, smaller community. |
| Teedy / sismics docs | not indexed | Lightweight Java DMS, clean UI, modest resources — but weaker OCR/auto-tagging, smaller momentum. |
| Self-built (Tesseract + Meilisearch + object storage) | not indexed | Full control over encryption/schema — but you build and maintain the whole pipeline. |

## What belongs here

Systems whose primary job is to **ingest, OCR, organize, and retrieve** documents. Not general
file sync (Nextcloud), not note-taking, not collaborative authoring.
