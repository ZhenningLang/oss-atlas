---
name: wondershaper
slug: wondershaper
repo: https://github.com/magnific0/wondershaper
category: networking
tags: [traffic-shaping, bandwidth, qos, tc, htb, linux, shell]
language: Shell
license: GPL-2.0
maturity: stable, low activity (last push 2024-07), ~1.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
health:
  schema: 1
  computed_at: 2026-06-29T10:07:01Z
  overall: D
  overall_score: 0.5
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1718
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: E
      raw:
        repo_age_days: 5039
        last_commit_age_days: 1718
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: C
      raw:
        spdx_id: GPL-2.0
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# wondershaper

A single Bash script that wraps Linux `tc` (traffic control) to cap the up/download bandwidth of a network adapter with one command — `wondershaper -a eth0 -d 8192 -u 2048` instead of a wall of HTB queueing-discipline incantations.

![wondershaper — health radar](../../assets/health/wondershaper.svg)

## When to use

You're on a Linux box — a home server seeding torrents, a CI runner, a shared dev machine, an embedded gateway — and one process is saturating your link, starving everything else (SSH gets laggy, video calls stutter). You don't want to learn the full `tc` qdisc/class/filter DSL just to say "don't let this NIC exceed 8 Mbit down / 2 Mbit up." You install wondershaper (it's one script), run `sudo wondershaper -a eth0 -d 8192 -u 2048`, and it builds the HTB traffic-shaping rules for you; `wondershaper -c -a eth0` clears them again. For a persistent cap you drop in the provided systemd unit and a small config file so the limit re-applies on boot. It's the fastest path from "this link needs a ceiling" to a working shaped adapter without hand-writing `tc`.

It fits ad-hoc and lightweight-persistent QoS on a *single host's* adapter: throttle a backup job, keep a downloader from eating the whole pipe, or give a low-powered router a simple upload/download ceiling.

## When NOT to use

- **You need real multi-class QoS / per-flow prioritization.** wondershaper sets a simple overall up/down ceiling (with some prioritization heuristics); for fine-grained per-application/per-IP traffic classes, write `tc`/`nftables` rules directly or use a router OS (OpenWrt's SQM/`cake`).
- **You want modern bufferbloat-aware shaping.** The script's lineage is HTB-based; for latency-under-load, **`cake`** / `fq_codel` (often via SQM) is the current best practice — verify what qdisc this version applies before relying on it for bufferbloat control. [未验证]
- **You're not on Linux with `tc`.** It's a Bash wrapper around `iproute2`'s `tc`; no Windows/macOS, and it needs `iproute2` present. Containers/network namespaces add caveats.
- **You need shaping across many hosts centrally.** It's a per-host CLI, not a fleet/SDN controller — no central policy, no coordination between machines.
- **You require active upstream support.** Last repo push is **2024-07** and it's an old, thin script; it works, but treat it as stable-but-coasting, and test on your kernel/`iproute2` version. [未验证]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| raw `tc` (iproute2) | 未收录 | Full control over qdiscs/classes/filters (HTB, HFSC, cake, fq_codel) — maximally flexible, but a steep DSL; wondershaper is just a friendly wrapper over it. |
| `cake` / SQM (OpenWrt) | 未收录 | Modern bufferbloat-killing shaper; best latency-under-load, but typically lives on a router/OpenWrt, not a quick per-host script. |
| `tcconfig` (Python) | 未收录 | Python CLI/lib over tc with richer rules (per-IP/port, netem loss/delay) — more featureful and scriptable, but a Python dependency vs one Bash file. |
| `trickle` | 未收录 | Userspace per-process bandwidth limiter (LD_PRELOAD) — shapes a single command without root/tc, but per-process and not a NIC-wide cap. |
| Linux `tc` + `fq_codel` by hand | 未收录 | Same engine, current qdiscs, no wrapper — more correct for bufferbloat but more to write. |

## Tech stack

- **Language:** Bash (a single shell script) — no compilation.
- **Engine:** Linux **`tc`** from **`iproute2`**, applying **HTB** (Hierarchical Token Bucket) shaping (upgraded from the original CBQ; ingress handling improved in later versions).
- **Persistence:** an optional **systemd** service unit + config file to re-apply limits at boot.

## Dependencies

- **Runtime:** a Linux kernel with traffic-control support and **`iproute2`** (`tc`, `ip`) installed; **root/sudo** to apply rules. Optionally **systemd** for the persistent service.
- **External services:** none — it's purely local kernel queueing configuration.
- **Install:** clone the repo / `make install`, or distro packages where available; it's just a script + optional unit file. [推断]

## Ops difficulty

**Low.** One script, one command to apply, one to clear; the systemd unit makes a persistent cap a copy-config-and-enable job. The real care is conceptual, not operational: pick the right interface, get the rate units right (rates are in **Kbps/kilobits**, easy to confuse with kilobytes), remember it needs root and that rules are kernel state that vanish on reboot unless persisted. Verifying the cap actually holds (and doesn't add latency) means an `iperf`/ping test before and after. There's no daemon to babysit — it sets kernel qdiscs and exits.

## Health & viability

- **Maintenance (2026-06).** Last repo push **2024-07**; no GitHub tagged releases here. Effectively **stable / low-activity** — a small mature script that rarely needs changes, but not actively developed. Not archived. [未验证]
- **Governance / bus factor.** Owner type **User** (magnific0, ~20 commits) with a few minor contributors — a **single-maintainer** small utility; bus factor is thin but the surface is tiny. [推断]
- **Age & Lindy verdict.** Created **2012** (and itself a continuation of the much older Wondershaper lineage from the Linux Advanced Routing HOWTO) — ~14 years; old **but quiet**, so Lindy is *moderate*: long-lived and still works, yet HTB-era design is dated next to modern `cake`/`fq_codel`. [推断]
- **Adoption.** ~1.9k stars and a long history as the go-to "simple bandwidth limit" script in Linux how-tos; widely copied. [未验证]
- **Risk flags.** **GPL-2.0** (copyleft — fine for use, relevant if you redistribute modified versions). The technical risk is staleness vs modern bufferbloat-aware shaping, not licensing or abandonment of a tiny script. [推断]

## Caveats (unverified)

- [未验证] ~1.9k stars / ~277 forks as of 2026-06 — date-sensitive, indicative only.
- [未验证] No GitHub releases are tagged; versioning/changelog lives in the script/README — verify the version and qdisc behavior of what you install.
- [推断] Exact qdisc applied by the current version (HTB vs anything newer) and its bufferbloat behavior are not verified here — test on your kernel.
- [推断] Install path (make/package/manual) depends on your distro; the repo is essentially one script plus an optional systemd unit.
- [未验证] Behavior inside containers / network namespaces and on non-systemd inits is not verified.
