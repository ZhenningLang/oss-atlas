---
name: bulk-downloader-for-reddit
slug: bulk-downloader-for-reddit
repo: https://github.com/Serene-Arc/bulk-downloader-for-reddit
category: media-download
tags: [reddit, downloader, archiver, scraping, yt-dlp, python, cli]
language: Python
license: GPL-3.0
maturity: v2.6.2 (2023-01), commits ongoing to 2026-04, ~2.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
---

# bulk-downloader-for-reddit

A command-line tool (BDFR) that downloads media and/or archives metadata from Reddit — subreddits, multireddits, users, saved/upvoted posts, or direct links — via the official Reddit OAuth API.

## When to use

You're archiving a subreddit before it goes private, or backing up your own saved/upvoted posts, or building a personal dataset of images and videos from a handful of communities. You don't want to click through hundreds of threads, and you want both the *files* (images, galleries, Redgifs/Imgur/YouTube-hosted clips) and the *context* (post titles, scores, comment trees) on disk in a predictable folder layout. You register a Reddit API app for OAuth credentials, then run `bdfr download ./out --subreddit pics --limit 200 --sort top`, or `bdfr clone ./out --user me --upvoted` to grab both files and metadata. BDFR resolves each submission's link through its own resolvers plus yt-dlp, names files by a template you control, dedupes by hash, and keeps a log so re-runs are incremental rather than re-downloading everything.

It's the right reach when you want a *scriptable, reproducible* Reddit archive — three modes (`download` files-only, `archive` metadata-only, `clone` both), YAML config for repeatable jobs, and a folder/naming scheme you can pin down — rather than a one-off browser extension grab.

## When NOT to use

- **You expect to pull more than ~1000 posts from a single source.** This is a hard Reddit API ceiling (listings cap at ~1000), and the README states plainly: "We cannot bypass this." For deep historical archives you need a different approach (e.g. Pushshift-style dumps, where still available).
- **You want a faithful, browsable clone of Reddit.** `clone` retrieves raw data, not a navigable replica — no rendered site, no guaranteed completeness of comment trees.
- **You can't / won't register Reddit API credentials.** Authenticated access uses OAuth2; without an API app many operations won't work.
- **You need a maintained, frequently-released tool.** The last tagged release (v2.6.2) is from early 2023; commits continue but the release cadence has effectively stalled — you may be running from `master` rather than a blessed version (see Health).
- **Content on sites BDFR/yt-dlp can't resolve.** It handles Imgur, Redgifs, galleries, YouTube, and "anything yt-dlp supports," but an unsupported or newly-changed host will simply fail for those links. [推断]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| gallery-dl | 未收录 | Broad multi-site media downloader (Reddit among many); strong for *files* across the web, but weaker at Reddit-specific metadata/comment archiving and the three-mode download/archive/clone model. |
| redditdownloader (shadowmoose) | 未收录 | Another dedicated Reddit downloader with a web UI; more approachable for non-CLI users, but BDFR's scriptable CLI + YAML config suits automation better. [未验证] |
| Pushshift dumps / PRAW scripts | 未收录 | Going straight to data dumps or the API yourself bypasses tooling and the ~1000 cap (dumps) but is roll-your-own — BDFR packages resolvers, dedup, naming, and logging for you. |
| yt-dlp (directly) | 未收录 | BDFR *uses* yt-dlp under the hood for hosted media; calling yt-dlp directly works for individual links but lacks Reddit-source enumeration, metadata archiving, and dedup. |

## Tech stack

- **Language:** Python 3.9+.
- **Reddit access:** the official Reddit API over OAuth2 (PRAW-style client) for enumerating submissions and metadata.
- **Media resolution:** built-in per-site resolvers (Imgur, Redgifs, Reddit galleries/video, Vidble, Erome, …) plus **yt-dlp** as the general fallback.
- **Output:** templated file naming, hash-based dedup, structured logs; YAML config for repeatable runs; three modes (download / archive / clone).

## Dependencies

- **Runtime:** Python 3.9+, installed via `pip install bdfr` / pipx (AUR package on Arch).
- **Credentials:** a Reddit API application (OAuth2 client) for authenticated access.
- **Bundled libs:** yt-dlp and per-site resolver code; Reddit API client. [推断]
- **No database / no services** — it writes files and a log to local disk; state is the on-disk output + log.

## Ops difficulty

**Low.** It's a `pip`/pipx install plus a one-time Reddit API app registration, then a CLI invocation (or a cron'd YAML job). There's no server, datastore, or queue to operate; the incremental log makes re-runs cheap and idempotent-ish. The realistic friction is operational, not infrastructural: respecting the ~1000-post ceiling, occasional resolver breakage when a host changes, and the fact that you may be running unreleased `master` code so you own keeping it current and verifying it still works.

## Health & viability

- **Maintenance (2026-06).** Last push 2026-04, so the repo is **not abandoned** — but the last *tagged release* (v2.6.2) is from 2023-01, so the release cadence has effectively stalled even as commits trickle in. Treat it as "maintained but unreleased," a yellow flag. Not archived.
- **Governance / bus factor.** A small contributor group (project changed hands from the original author aliparlakci to Serene-Arc and others). Real bus-factor risk: a handful of maintainers, no foundation backing. [推断]
- **Age & Lindy verdict.** ~8 years old (created 2018-06) but with a stalled release line ⇒ Lindy is **mixed**: long-lived and still committed-to, yet the lack of recent releases tempers the "still-active" half of age × still-active.
- **Adoption.** ~2.6k stars and an AUR package indicate a real user base for Reddit archiving, though smaller than general-purpose downloaders. [未验证]
- **Risk flags.** GPL-3.0 (copyleft — relevant if you embed it). The standing risks are the stalled releases, the hard ~1000-post API ceiling, and resolver fragility against changing host APIs — not licensing surprises.

## Caveats (unverified)

- [未验证] ~2.6k stars as of 2026-06 and v2.6.2 (2023-01) as the last tag — figures are date-sensitive; commit activity to 2026-04 is from the API but the "maintained but unreleased" read is a judgment.
- [未验证] Exact Reddit-API client (PRAW vs custom OAuth client) and the precise current resolver list are inferred from the README, not confirmed against the manifest in this pass.
- [推断] OAuth credential requirement for most operations is the standard Reddit-API posture; the precise set of features that work unauthenticated is not verified here.
- [推断] Per-host failure on unsupported/changed sites is inferred from the resolver+yt-dlp architecture, not a tested enumeration.
