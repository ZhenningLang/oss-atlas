---
name: paperless-ngx
slug: paperless-ngx
repo: https://github.com/paperless-ngx/paperless-ngx
category: document-management
tags: [dms, ocr, self-hosted, django, angular, full-text-search, document-archive, homelab, tesseract, gplv3]
language: Python (backend) + TypeScript/Angular (frontend)
license: GPL-3.0
maturity: Mature, active; stable v2.20.x (2026-04), v3.0 in beta as of 2026-06 (see caveats)
last_verified: 2026-06-26
type: tool
---

# paperless-ngx

A self-hosted document management system (DMS) that OCRs, tags, indexes, and full-text-searches scanned paperwork — bills, invoices, letters — built on Django + Angular with PostgreSQL/Redis.

## When to use

You're the one unofficial "IT person" for a two-person accounting practice run out of a spare room, and the filing cabinet has finally won: years of invoices, utility bills, client letters, and receipts in paper folders, and every time a client asks "did you ever get my March statement?" you're flipping through binders for twenty minutes. You already have a little Linux box / NAS humming in the corner on the office network, and you want every scan to land in one place you can actually search.

So you stand up paperless-ngx with its Docker-first compose stack and point your scanner at the consume folder. Now you drop a batch of scans in, paperless OCRs them, and its matching rules auto-apply tags, the correspondent, and a document type — so that March statement is one full-text search away in the web UI instead of a cabinet dive. Because the box lives on your trusted internal office network and the corpus is personal-to-small-team scale, this is squarely the "scan, archive, and forget" job paperless is built for — you're not editing these documents or routing them for approval, just making a pile of finished paperwork findable.

## When NOT to use

- **Not a security / compliance store** — documents are stored in cleartext on disk and full text is stored plain in the database; filenames are not encrypted. Built-in document encryption was removed (paperless-ng 0.9, and again in v3), and `[未验证]` maintainers have reportedly indicated no plan to add encryption at rest. Disk-level encryption is on you.
- **Not on an untrusted/shared host** — the project explicitly warns against this.
- **Not for strict multi-tenant / per-document privacy** — the permission/ownership model has known gaps (e.g. documents ingested via the consume folder may get no owner and become visible to all users). It is not a hardened multi-user system.
- **Not an enterprise EDMS** — no built-in multi-step approval workflows, lifecycle/retention management, or e-signatures (use Mayan EDMS for that).
- **Not for collaborative authoring/editing** — it's an archive of *finished* documents, not a Google-Docs replacement.
- **Poor fit for large-scale OCR on weak hardware** — OCR and auto-matching are CPU/RAM-intensive; the docs themselves suggest cutting workers, processing only the first page, and disabling NLTK on constrained devices (Raspberry Pi etc.).
- **Windows is not supported** (Linux host required).
- **Upgrade lock-in / maintenance risk** — community-supported with no commercial backer; major versions ship significant breaking changes (v3 drops API v1, recreates migrations, changes pre/post-consume script arguments). Pin versions and read release notes before upgrading.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| Mayan EDMS | 未收录 | Also Python/Django, but a heavier enterprise EDMS with a real workflow engine, versioning and granular permissions; far steeper to operate and overkill for a personal scan archive. Apache-2.0 (more permissive than paperless's GPLv3). |
| Docspell | 未收录 | Inbox/metadata-extraction model with strong email ingestion; Scala/JVM stack means heavier memory footprint and a smaller community than paperless-ngx. |
| Teedy / sismics docs | 未收录 | Lightweight Java DMS with versioning, clean UI and modest resource needs; weaker automated OCR/auto-tagging and smaller momentum. |
| OpenDocMan | 未收录 | PHP/MySQL DMS for business file control + access rules; dated UI, no first-class OCR/auto-tagging — only if you need simple web access control on an existing PHP stack. |
| Self-built (Tesseract + Meilisearch/Elasticsearch + object storage) | 未收录 | Maximum flexibility and full control over encryption/schema, but you build and maintain the whole ingest/OCR/index/UI pipeline — worth it only when paperless's data model or security constraints are dealbreakers. |

## Tech stack

- Python, Django (backend); Angular, TypeScript (frontend)
- PostgreSQL (recommended); SQLite or MariaDB supported
- Redis / Valkey (message broker)
- Tesseract OCR, ImageMagick
- Apache Tika + Gotenberg (optional — Office/HTML formats)
- Whoosh (search, v2) → Tantivy (search, v3)
- Docker / docker-compose

## Dependencies

- **PostgreSQL** (recommended; SQLite or MariaDB also supported)
- **Redis or Valkey** (mandatory message broker)
- **Tesseract OCR** 4.0.0+ with language packs
- **ImageMagick** 6+
- **Apache Tika + Gotenberg** — only if ingesting Office/non-PDF formats
- **Docker + docker-compose** (recommended deployment)
- **Linux host** (Windows not supported); for bare-metal installs, Python 3.11–3.14 on the v3 line `[未验证]` (the v2.20.x stable line reportedly still supports Python 3.10+)

## Ops difficulty

**Medium.** Multi-container docker-compose stack (web + worker + Redis + DB, plus Tika/Gotenberg for Office docs). Day-to-day operation is low-touch once configured, but: OCR is CPU/RAM-heavy and slow on low-power hardware; you own backups of both the DB and the document/media volumes; and major upgrades carry breaking changes (v3 removes API v1, drops Python 3.10, recreates migrations, changes consume scripts), so upgrades require reading release notes. Must not be exposed on an untrusted host.

## Health & viability

- **Maintenance (2026-06).** Last pushed 2026-06; stable v2.20.x line plus a v3.0 beta in flight — **actively** developed, not archived. The strikingly low open-issue count (~6) suggests aggressive triage, not stagnation. [推断]
- **Governance / bus factor.** Community-maintained under the `paperless-ngx` org — itself the community continuation after the original `paperless`/`paperless-ng` lineage stalled, which is reassuring (the project has *already* survived one maintainer handoff) but it has **no commercial backer**; longevity rests on volunteer continuity. [推断]
- **Age & Lindy verdict.** ~4 years as `paperless-ngx` (created 2022-02), with deeper roots via its predecessors ⇒ a **moderate Lindy** signal — proven in the homelab/DMS niche, though younger than the underlying paperless idea. [推断]
- **Adoption & ecosystem.** Strong (~42k stars, the default self-hosted DMS recommendation, packaged for Docker-first deployment) — a healthy, widely-deployed project. [未验证]
- **Risk flags.** GPL-3.0 (no relicense found). The real flags are **upgrade lock-in / breaking changes** (v3 drops API v1, recreates migrations, changes consume scripts) and the security posture (cleartext at rest, permission-model gaps) — pin versions and read release notes before upgrading. [推断]

## Caveats (unverified)

- **Stars** — 42.5k from a single fetch of the GitHub repo page (2026-06), not cross-checked against the API. `[未验证]`
- **Release versions/dates** — v2.20.15 (~2026-04-27) and v3.0.0-beta.rc1 (~2026-05-05) come from search aggregators (releasebot/newreleases), not confirmed on the GitHub releases page this session. `[未验证]`
- **v3 feature list** — tantivy backend, local "Paperless AI", document versions, OCR plugin framework, API-v1 removal, Python 3.10 drop, consume-script changes — drawn from search summaries of the v3 beta, not the full release notes. `[未验证]`
- **Gotenberg** listed as an optional companion based on the `-tika` compose files; not explicitly confirmed in the extracted setup docs. `[未验证]`
- **Resource needs** — "CPU/RAM heavy" is a qualitative judgment from the docs' resource-saving guidance; no official min RAM/CPU spec is published. `[未验证]`
