---
name: Twake Drive
slug: twake-drive
repo: https://github.com/linagora/twake-drive
category: document-management
tags: [drive, file-manager, cozy, self-hosted, file-sharing, react, agpl, personal-cloud, google-drive-alternative]
language: JavaScript / TypeScript (React)
license: AGPL-3.0
maturity: Active, mature codebase; latest release 1.103.0 (2026-06-23), main at 1.105.0 (see caveats)
last_verified: 2026-06-26
type: app
---

# Twake Drive

A self-hostable "open-source alternative to Google Drive" — a React web app for storing, browsing, link-sharing and previewing files, running as a Cozy app on top of the cozy-stack backend (part of the Twake Workplace suite). It is a personal/team file drive, NOT an OCR document archiver.

## When to use

You're running Twake Workplace (or a Cozy server) for a small team and you want the file-storage piece of that suite — somewhere people drop documents, photos, ID scans, payslips and tax notices, browse them in a familiar file-tree UI, and share a folder with a colleague by link. You don't want yet another standalone server to babysit; you want the drive that plugs into the auth, sharing and connector model you already run. So you serve the Twake Drive web app from your cozy-stack, and your users get a clean React UI with upload, search-by-name, in-browser PDF/image preview, and "share this link" — plus the Cozy connectors that auto-pull bills and statements from utility/telecom providers into the drive. It's the "Google-Drive-shaped" front door to your self-hosted stack, not a records-management system.

This is the right pick when your real goal is *file storage and link-sharing inside the Twake/Cozy ecosystem*, and your "documents" are things people keep and occasionally retrieve by name or folder — not a corpus you need to OCR, auto-tag and full-text search the way a paperwork archive demands.

## When NOT to use

- **You actually want OCR / full-text search of scanned paperwork.** This is the category's anti-pattern for Twake Drive: it has no OCR, no content extraction, no auto-tagging, no full-text search of document *contents*. Search is name/metadata-based. If you're indexing scanned invoices, use [paperless-ngx](paperless-ngx.md) instead.
- **You want a single standalone DMS binary.** This repo is only the front-end web app; it requires a running **cozy-stack** backend (a separate Go project) and the surrounding Cozy/Twake infrastructure. It is not a one-container `docker run` document server.
- **You're not on the Cozy / Twake Workplace stack.** It's a Cozy app (`manifest.webapp`, served via `cozy-stack serve`, `cozy/cozy-app-dev`). Adopting it effectively means adopting cozy-stack and its data model — meaningful platform lock-in, not a drop-in DMS.
- **You need an enterprise EDMS** — versioned records, retention/lifecycle policies, multi-step approval workflows, e-signatures, granular per-document ACLs. None of that is the goal here.
- **You want a plain WebDAV/HTTP file server to expose a folder.** Twake Drive is heavyweight for that; a single-binary file server (e.g. [copyparty](copyparty.md)) is a far smaller surface.
- **AGPL-3.0 is a blocker.** Network-copyleft obligations apply if you offer it as a service and modify it — a problem for some commercial/proprietary deployments.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [paperless-ngx](paperless-ngx.md) | ✅ | A true OCR/DMS: ingests, OCRs, auto-tags and full-text-searches scanned paperwork. The right tool when "documents" means searchable scans. Twake Drive does none of that — it's a file drive, not an archiver. |
| [copyparty](copyparty.md) | ✅ | Single-binary file server with upload UI, WebDAV, sharing and (optional) media indexing; far lighter to run than Twake Drive's Cozy-stack dependency, but no suite/auth/connector ecosystem. |
| Nextcloud | 未收录 | The mainstream self-hosted Drive+groupware platform — files, sharing, collaborative office, huge app ecosystem; much heavier (PHP/DB stack) but standalone and not tied to cozy-stack. |
| Seafile | 未收录 | Sync-first self-hosted drive with strong delta-sync, versioning and (Pro) encryption; standalone server, weaker suite/groupware integration than Twake/Cozy. |
| Cozy Drive (upstream) | 未收录 | This *is* the upstream — Twake Drive is Linagora/Twake Workplace's fork/rebrand of `cozy/cozy-drive`. Same architecture; pick based on which ecosystem (Cozy Cloud vs Twake Workplace) you run. |

## Tech stack

- **Frontend:** React 18, Redux, React-Router, `react-dnd`, built with Rsbuild + Babel; Jest for tests.
- **Cozy libraries:** `cozy-client`, `cozy-ui` / `cozy-ui-plus`, `cozy-bar`, `cozy-sharing`, `cozy-search`, `cozy-realtime`, `cozy-harvest-lib` (connectors), `cozy-viewer`.
- **Viewers:** EmbedPDF / `react-pdf` (PDF), Excalidraw, Leaflet (map for geo-tagged items).
- **Backend (separate repo):** **cozy-stack** (Go) provides storage, auth, sharing and the data layer — not in this repository.
- **Languages:** JavaScript (~77%), TypeScript (~21%), Stylus.

## Dependencies

- **cozy-stack** — mandatory backend; you serve this app via `cozy-stack serve --appdir drive:…`. Without it the app does nothing.
- **Node.js 20** (`.nvmrc`) + **Yarn** to build/develop the web app.
- **CouchDB** is cozy-stack's datastore `[推断]` (cozy-stack's standard backing store; not configured from this repo).
- **MailHog / an SMTP server** for the share-by-email flow in dev.
- **Docker** image `cozy/cozy-app-dev` for the in-VM dev workflow; `docker-compose.e2e.yml` for E2E tests. Production deployment is via the Cozy/Twake Workplace platform, not a compose file in this repo.

## Ops difficulty

**Medium-to-high — but mostly inherited from cozy-stack, not this app.** Building the web app itself is a routine Node/Yarn workflow. The real operational burden is standing up and maintaining the **cozy-stack** backend and the surrounding Twake Workplace/Cozy platform (auth, sharing, connectors, datastore), which this repo assumes already exists. If you only want "a place to put files," that platform requirement makes Twake Drive a heavy choice; if you already run Twake Workplace, the drive is just another served app and ops is low.

## Caveats (unverified)

- [未验证] `gh` reports latest tagged release **1.103.0** (2026-06-23) while `package.json`/`manifest.webapp` on `main` show **1.105.0** — main is ahead of the latest tag; treat the exact "current version" as approximate.
- [未验证] Star count ~960 (gh, 2026-06-26). GitHub stars are unreliable and date-sensitive; indicative only.
- [推断] cozy-stack uses CouchDB as its datastore and provides the actual file storage/auth/sharing layer — inferred from the Cozy architecture, not from files in this repo (which is front-end only).
- [推断] "No OCR / no full-text content search / no auto-tagging" is inferred from the README feature list (file tree, upload, URL sharing, name search) and the absence of any OCR/index dependency; verify against current cozy-stack capabilities if content search matters.
- [未验证] Relationship to upstream `cozy/cozy-drive` (fork vs rebrand) is inferred from `manifest.webapp` `source`/`editor` fields and the `cozy-drive` package name; exact governance not confirmed this session.
- [未验证] Production deployment topology (containers, datastore, object storage) is not defined in this repo; it ships only an E2E compose file and a dev Docker image.
