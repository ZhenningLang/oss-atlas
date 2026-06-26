---
name: DevToys
slug: devtoys
repo: https://github.com/DevToys-app/DevToys
category: dev-utilities
tags: [developer-tools, offline, desktop, cross-platform, converters, encoders, formatters, extensible]
language: C#
license: MIT
maturity: v2.0.9.0 (prerelease, 2026-01), active (2026-06)
last_verified: 2026-06-26
type: app
---

# DevToys

An offline, cross-platform desktop "Swiss Army knife" that bundles ~30 small developer utilities (converters, encoders, formatters, generators, testers) behind one native GUI — plus a separate CLI for automation.

## When to use

You're a developer who, twenty times a day, needs to Base64-decode a token, pretty-print a blob of JSON, diff two strings, generate a UUID, convert JSON↔YAML, or hash a file — and you're tired of pasting potentially-sensitive payloads into random "json formatter online" sites whose ad-funded business model you don't trust. DevToys installs as a normal desktop app (Windows, macOS, or Linux), opens instantly, and runs every transformation locally with no network call, so a JWT or a config secret never leaves your machine. You get one searchable window with ~30 tools instead of thirty browser tabs, and a "Smart Detection" feature that guesses which tool you want from whatever you paste.

It also fits when you want the same conveniences in automation: DevToys ships a separate CLI app that exposes the tools for scripting and CI, and both the GUI and CLI are extensible — you can pull in community tools or write your own as a NuGet-distributed extension. So the personal scratchpad and the pipeline step can share the same tool implementations.

## When NOT to use

- **You live in the terminal and want a single binary, not a desktop app.** DevToys is GUI-first; the CLI is a separate companion. For a pure browser/CLI text-transform pipeline, [CyberChef](cyberchef.md) (browser, chainable "recipes") or plain `jq`/`xxd`/`openssl` are lighter weight.
- **You need to chain transforms into a reproducible recipe.** DevToys tools are mostly one-shot, single-tool screens; CyberChef's whole model is composing many operations into a saved, shareable pipeline. DevToys does not (as of v2) offer an equivalent recipe graph. [推断]
- **You need server/headless infrastructure or remote management.** This is a local devtools box, not a service. For host administration use [Cockpit](cockpit.md); for metrics collection use [Telegraf](telegraf.md).
- **You depend on a frozen, long-term-stable release.** The current cross-platform 2.x line is published as **prerelease** builds; the last non-prerelease GitHub release is the older Windows-only 1.0.13.0 (2023). If your org bars prerelease software, that's a real gate. [未验证] release-channel policy may change.
- **You need a tool DevToys doesn't have and can't justify an extension.** The built-in set is fixed (~30); anything beyond means finding or authoring an extension, with the maintenance/trust cost that implies.
- **Browser-embeddable / scriptable-in-JS use.** DevToys is a .NET desktop app; you can't drop it into a web page the way CyberChef (pure client-side JS) embeds.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [CyberChef](cyberchef.md) | ✅ | Browser-based, chainable "recipe" pipelines and crypto/forensics depth; runs anywhere with a browser. DevToys is a native desktop app with OS integration, a CLI companion, and an offline-by-default install, but mostly one-shot tools (no recipe graph). |
| [Cockpit](cockpit.md) | ✅ | Web server-administration UI for Linux hosts (services, logs, storage); a different job — remote host management vs local dev string-wrangling. |
| [Telegraf](telegraf.md) | ✅ | Metrics/event collection agent for observability pipelines; not an interactive devtools box. |
| It-Tools | 未收录 | Self-hostable web app with a very similar grab-bag of dev utilities; runs in any browser / Docker. DevToys is native desktop + offline + a CLI; It-Tools is zero-install over HTTP. |
| DevUtils (macOS) | 未收录 | Polished native macOS-only equivalent (paid); DevToys is free, MIT, and cross-platform. |
| `jq` / `xxd` / `openssl` (CLI) | 未收录 | Scriptable Unix primitives, no GUI; better for pipelines, worse for "I just need to eyeball this once." |

## Tech stack

- **Language:** C# (≈73% of the repo) on .NET; UI assets in HTML/SCSS/TypeScript (Blazor Hybrid front end). PowerShell for build/packaging. (percentages per GitHub language stats, 2026-06)
- **UI:** WinUI on Windows and a cross-platform shell rendering a Blazor Hybrid (WebView) UI on macOS/Linux; Fluent/Mica design language. (exact cross-platform host framework not re-confirmed from source this pass — see Caveats)
- **Form factors:** a GUI app and a separate CLI app, sharing the same tool/extension model.
- **Extensibility:** tools are plugins; community + first-party extensions are distributed as NuGet packages and discovered in-app.

## Dependencies

- **Runtime:** none for the user — DevToys ships as a self-contained desktop install per OS (Windows / macOS / Linux). No database, no server, no internet connection required to run the built-in tools.
- **Install:** OS-native installers / package managers (e.g. Microsoft Store / winget on Windows, and macOS/Linux packages); see the project's releases and site for the current channel (exact package-manager IDs not re-verified this pass — see Caveats).
- **Build-from-source:** .NET SDK toolchain (C#), plus the JS/TS asset pipeline for the Blazor UI.
- **Extensions:** optional; pulled as NuGet packages at the user's discretion.

## Ops difficulty

**Low.** For the end user it is a single desktop install with zero services to run, no config, and no network exposure — essentially "install and use," and uninstall is clean. The only ongoing burden is keeping up with prerelease 2.x builds if you want the cross-platform line, and vetting any third-party extension you add (an extension is arbitrary code from NuGet, so it inherits that trust/maintenance cost). There is no deployment, scaling, or backup story because there is no server.

## Caveats (unverified)

- [未验证] Latest release is v2.0.9.0 published 2026-01-08 and marked **prerelease**; the most recent non-prerelease GitHub release is v1.0.13.0 (2023-07-25, Windows-only 1.x). Repo `pushedAt` 2026-02-25, so development is ongoing — but "stable 2.0" status should be confirmed before relying on it.
- [未验证] Star count ~31.7k as of 2026-06 — GitHub stars are unreliable and date-sensitive; indicative only.
- [推断] Built-in tool count "~30" comes from the project's own "30 tools" framing for 2.0; the exact catalog shifts release-to-release — verify a specific tool exists in your installed build.
- [推断] Cross-platform UI is described as WinUI (Windows) + a Blazor Hybrid WebView shell elsewhere; the precise cross-platform host framework (Uno Platform vs custom) was not re-confirmed from source this pass.
- [未验证] Installation methods (winget / Store / brew / Linux packages) and the CLI's exact command surface were not exhaustively re-verified; check the official site/releases.
- [推断] CyberChef-style recipe chaining is absent in DevToys based on its single-tool UI model; not exhaustively confirmed against the current feature set.
