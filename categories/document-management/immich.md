---
name: Immich
slug: immich
repo: https://github.com/immich-app/immich
category: document-management
tags: [photo-management, video-management, self-hosted, backup, google-photos-alternative]
language: TypeScript
license: AGPL-3.0
maturity: v1.x, stable, 104.8k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-01T08:56:34Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:28:12Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 2.1
        qualifying_issues: 36
        band: relaxed_solo
        window_offset_days: 3
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: "@immich/cli"
        dependent_repos_count: 0
        downloads_last_month: 6496
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 1610
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 322
        top1_share: 0.107
        top3_share: 0.273
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: true
        content_license: null
---

# Immich

High performance self-hosted photo and video management solution. A direct alternative to Google Photos that keeps your media on your own hardware.

![Immich — health radar](../../assets/health/immich.svg)

## When to use

You're a privacy-conscious user with thousands of photos and videos scattered across phones, cameras, and cloud services. You want a single, searchable home for all your media that you control, not a Big Tech SaaS. You install Immich on a home server or NAS, set up the mobile app for automatic background backup, and watch your photos sync with face detection, EXIF-based maps, and AI-powered search. You share albums with family without sending data through a third party. Immich gives you the Google Photos experience — auto-backup, timeline, memories, and ML search — with full ownership of the stack.

## When NOT to use

- **Small photo collections** — If you have fewer than a few thousand photos, the server overhead (Postgres, Redis, ~4GB RAM) may not be worth it versus a simple NAS folder or a commercial cloud plan.
- **Zero-ops users** — Immich requires Docker or a Linux server, database setup, and periodic updates. If you don't want to think about backups, disk space, or container restarts, a managed service is simpler.
- **AGPL-3.0 sensitivity** — The AGPL-3.0 license requires sharing source code if you modify and network-serve the app. Verify this fits your organization's compliance posture before commercial or internal-network deployment.
- **RAW-only workflows** — While Immich supports RAW formats, it is primarily a photo/video management and sharing platform, not a darkroom or RAW development tool like darktable or Lightroom.
- **Multi-tenant public SaaS** — Immich is designed for single-family/small-team self-hosting, not as a public-facing multi-tenant photo service. The auth model and rate limits are not built for that scale.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Google Photos | 未收录 | The incumbent cloud photo service with unlimited storage (for compressed) and best-in-class ML search. | Google hosts your data and trains models on it; Immich keeps everything local but you run the hardware. |
| Nextcloud Photos | 未收录 | File-sync-first with a photo viewer; not a dedicated photo management app. | Nextcloud is a general file server with photo plugins; Immich is purpose-built for media with AI search and mobile auto-backup. |
| PhotoPrism | 未收录 | Self-hosted photo management with strong RAW support and a focus on privacy. | PhotoPrism has a more mature RAW pipeline and broader format support; Immich has a more modern mobile app and faster feature velocity. [推断] |
| LibrePhotos | 未收录 | Lightweight self-hosted photo manager with face recognition. | LibrePhotos is lighter on resources but has a smaller community and less polished mobile experience. [未验证] |

## Tech stack

- **TypeScript** — primary server and web UI language
- **NestJS** — server-side framework for the REST API
- **Svelte / SvelteKit** — web frontend
- **Flutter** — cross-platform mobile app (iOS/Android)
- **PostgreSQL** — primary data store (metadata, users, albums)
- **Redis** — job queue, caching, and session store
- **TensorFlow / ONNX** — ML models for face detection, CLIP-based search, and object recognition
- **FFmpeg** — video transcoding and thumbnail generation
- **Typesense** — fast typo-tolerant search engine for metadata and tags
- **Docker** — official deployment method

## Dependencies

- **Server**: Linux server or NAS with Docker; minimum 4GB RAM recommended, 8GB+ for ML features
- **Storage**: Enough disk for originals + generated thumbnails + transcoded videos; Immich does not deduplicate across users by default
- **PostgreSQL**: Required for metadata; must be backed up regularly alongside media
- **Redis**: Required for job queuing; can be co-located on the same host
- **Reverse proxy**: Nginx or Traefik for TLS termination if exposing to the internet
- **Backup strategy**: The 3-2-1 rule applies — Immich is not a backup, it is a live photo manager [推断]

## Ops difficulty

**Medium**. Immich ships as Docker Compose, but running it in production means:
- Keeping Postgres, Redis, and Immich containers updated in sync
- Managing storage growth (photos accumulate fast; plan for tiered storage or pruning)
- Monitoring ML job queues (face detection and CLIP embedding can be CPU/GPU intensive)
- Running backups of both the database and the media library
- The mobile app auto-backup works well on WiFi but can be battery-heavy on cellular if not restricted

## Health & viability

- **Maintenance**: Very active — daily pushes as of 2026-07, with a regular release cadence and a large, engaged community (104.8k stars, 669 open issues). [推断]
- **Governance**: Developed by the `immich-app` organization with multiple core maintainers. The project has a clear roadmap and transparent issue tracking. Bus factor is moderate. [推断]
- **Backing**: No large corporate backing visible; sustained by community contributions and likely donations/sponsorships. This is a strength for independence but a risk for long-term sustainability. [未验证]
- **Adoption**: Strong adoption with 104.8k stars, created in 2022 (4-year track record). A popular choice in the self-hosting and homelab communities. [推断]
- **Risk flags**: AGPL-3.0 license is strong copyleft — verify compatibility before commercial or internal-network use. No relicense history visible, but monitor for any future license changes. The project is young enough that long-term governance is still being proven. [未验证]

## Caveats (unverified)

- [未验证] The exact number of active production instances and the size of the largest known deployment have not been verified.
- [未验证] The project's exact funding model (donations, sponsorships, or commercial backing) has not been verified from primary sources.
- [推断] PhotoPrism may have broader RAW format support than Immich, but this has not been systematically compared.
- [推断] The ML model accuracy for face detection and CLIP search in non-English contexts may vary.
