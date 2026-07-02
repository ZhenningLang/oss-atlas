---
name: yt-dlp
slug: yt-dlp
repo: https://github.com/yt-dlp/yt-dlp
category: media-download
tags: [video-downloader, audio-downloader, cli, youtube, python, extractor]
language: Python
license: Unlicense
maturity: active, 174k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T04:46:55Z
  default_branch: master
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T12:47:59Z
  overall: "?"
  overall_score: null
  scored_axes: 1
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: conda-forge.org
        canonical_package: yt-dlp
        dependent_repos_count: 0
        downloads_last_month: 138250
        graph_tier: E
        volume_tier: "?"
        cross_check_divergence: null
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    maintenance: { reason: recency_unreadable }
    responsiveness: { reason: no_traffic }
    longevity: { reason: not_found }
    governance: { reason: empty_or_gated }
    risk_license: { reason: repo_unreachable }
---

# yt-dlp

A feature-rich command-line audio/video downloader and the actively maintained successor fork of youtube-dl, supporting thousands of sites with faster extractor fixes and modern features.

![yt-dlp — health radar](../../assets/health/yt-dlp.svg)

## When to use

You're building a media pipeline, archiving content, or need to grab a video or audio track from a streaming site for local processing. You want a single CLI tool that understands hundreds of sites out of the box, can select the best quality stream, merge formats, embed subtitles, skip sponsor segments, and run as a cron job or inside a Python script. You reach for yt-dlp instead of youtube-dl because the original upstream has slowed to a crawl on extractor fixes; you pick it over lux because lux is a single-binary Go tool with a narrower site list and slower extractor updates; you choose it over you-get because you-get's extractor catalog is smaller and its maintenance cadence is lower. One pip install, one command, and yt-dlp resolves the URL, picks the formats, and writes the file with a predictable filename template.

## When NOT to use

- **DRM-protected content.** If you need to decrypt Widevine, PlayReady, or FairPlay DRM, use a licensed streaming service or a dedicated DRM tool instead of yt-dlp, because it cannot decrypt protected streams and will fail or return only unencrypted portions.
- **Bulk commercial or ToS-violating use.** If you need a product-grade media-saver service with a web UI, use [cobalt](cobalt.md) instead of yt-dlp, because many sites prohibit downloading in their Terms of Service and youtube-dl itself was subject to a 2020 DMCA takedown (later reinstated).
- **JS-heavy SPAs without an extractor.** If you need to execute arbitrary page JavaScript to reach media, use a headless browser scraper like Puppeteer or Playwright instead of yt-dlp, because it does not run client-side JavaScript and sites that gate media behind per-request token schemes without a written extractor will fail.
- **Geo-restricted or login-walled content at scale.** If you need CAPTCHA solving, identity rotation, or anti-bot protection, use a dedicated scraping platform like [Firecrawl](https://firecrawl.dev) or a residential proxy service instead of yt-dlp, because yt-dlp can only pass cookies and proxies and will not shield you from IP bans.
- **You need a stable library API.** If you need a programmatic API with semver stability, use [youtube-dl](youtube-dl.md) as a more stable (but stale) library or write a dedicated scraper instead of yt-dlp, because yt-dlp's internal APIs and extractor behavior change without notice and are risky as a hard dependency in a shipped product.
- **Live stream capture or very high concurrency.** If you need reliable live HLS/DASH capture or massive parallel jobs, use FFmpeg directly or a dedicated streaming ingestion tool instead of yt-dlp, because its live capture and concurrency support are fragile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [youtube-dl](youtube-dl.md) | ✅ | The original upstream project. | youtube-dl is the legacy upstream with slowed releases; yt-dlp is the actively maintained fork with faster fixes and more features. For YouTube and hot sites, default to yt-dlp. |
| [you-get](you-get.md) | ✅ | Tiny Python CLI focused on Chinese sites. | Lighter and simpler than yt-dlp, but a smaller extractor catalog and less active maintenance. |
| [lux](lux.md) | ✅ | Fast single-binary Go downloader. | No Python runtime needed, but a narrower site list and slower extractor updates than yt-dlp. |
| [cobalt](cobalt.md) | ✅ | Self-hostable web-UI + API media saver. | Browser-friendly service, not a scriptable CLI for automation pipelines. |
| gallery-dl | 未收录 | Specialized in image and gallery sites. | Complementary rather than a substitute for video/audio extraction. |

## Tech stack

- **Python** — primary implementation language
- **Per-site extractor classes** — modular plugin architecture for different hosting sites
- **Format selection engine** — chooses best available streams based on user criteria
- **Post-processor pipeline** — shells out to external tools for remux, metadata embedding, and thumbnail conversion

## Dependencies

- **Python interpreter** — the only hard requirement for basic operation
- **Optional ffmpeg** — strongly recommended for audio extraction, format merging, and remuxing (`--extract-audio`, `--merge-output-format`)
- **Optional ffprobe** — for metadata and format probing
- **Network access** — outbound HTTP(S) to target sites; optionally a proxy or cookies file for login-gated content
- **No service to run** — executes and exits; no daemon or database

## Ops difficulty

**Low to run, medium to keep current.** Installation is trivial (`pip install yt-dlp` or a standalone binary). The real ops burden is extractor currency: streaming sites change frequently, and while yt-dlp updates much faster than youtube-dl, you still need to stay on a recent release. For one-off scripts this is fine; for a long-lived automation pipeline, budget for version pinning and periodic updates. The `--update` flag helps, but CI environments should pin and test new versions.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance**: Very active — pushed daily as of 2026-07, with a commit-activity badge showing sustained velocity. The fork has consistently outpaced the original upstream on extractor fixes.
- **Governance**: Owned by the `yt-dlp` organization; community-driven with multiple maintainers. The org structure provides reasonable bus factor compared to a single-maintainer project.
- **Backing**: No major corporate backing visible; funded by community donations and volunteer effort.
- **Adoption**: Extremely popular (174k stars) and widely regarded as the de-facto successor to youtube-dl for YouTube extraction. High production usage in scripts, pipelines, and downstream tools.
- **Age & Lindy**: Created 2020 as a fork (~6 years old), which is young but has already outlived many hype-cycle tools. The "fork of a long-lived tool" lineage gives it a partial Lindy pedigree through youtube-dl's 15+ year history.
- **Risk flags**: Unlicense (public domain) — no copyleft or relicense friction. The main risks are the same legal/ToS exposure that affects all downloaders, and the occasional upstream arms race with streaming sites that can break extractors for days.

## Caveats (unverified)

- The exact count of supported sites ("thousands") shifts over time; verify with `--list-extractors` for your specific target sites.
- SponsorBlock integration and other advanced features may require additional dependencies or configuration not enabled by default.
- [推断] The high star count (174k) reflects both genuine utility and the visibility boost from being the successor to the widely-known youtube-dl project.
- Some extractors for regional or niche sites may be community-contributed and less thoroughly tested than the core YouTube extractor.
