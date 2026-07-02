# dev-utilities

> Category node. Standalone devtools, data-wrangling swiss-army-knives, and self-hostable infrastructure.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **DevToys** | Use it when you want offline, local-only dev utilities (Base64/JSON/hash/diff) in one cross-platform desktop app instead of untrusted online tools. | B (4/6) | [→](devtoys.md) |
| **CyberChef** | Use it when you need to chain encode/decode, crypto, compression and data-analysis transforms offline in your browser. | B (6/6) | [→](cyberchef.md) |
| **Cockpit** | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. | D (5/6) | [→](cockpit.md) |
| **Telegraf** | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. | A (5/6) | [→](telegraf.md) |
| **OpenZL** | Use it when you must squeeze terabytes of one highly structured/numeric format better than generic zstd. | B (4/6) | [→](openzl.md) |
| **Certbot** | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. | A (5/6) | [→](certbot.md) |
| **tqdm** | Use it when you want a fast, low-overhead progress bar for Python loops/CLI/notebooks. | B (5/6) | [→](tqdm.md) |
| **SlimToolkit** | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. | B (5/6) | [→](slim.md) |
| **Faker (faker-js)** | Use it when you need realistic fake/mock data (names, addresses, finance…) for tests and seeding in JS/TS. | A (5/6) | [→](faker-js.md) |
| **fontTools** | Use it when you need programmatic font surgery — subset webfonts, convert formats, inspect/patch tables — but it edits font files, it won't design glyphs or shape text. | A (6/6) | [→](fonttools.md) |
| **Flashlight** | Use it when you're keeping a vintage macOS 10.10–10.15 machine and want Spotlight plugins — but it's abandoned since 2020 and requires disabling SIP, avoid on real machines. | E (3/6) | [→](flashlight.md) |
| **IdeaVim** | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. | B (5/6) | [→](ideavim.md) |
| **VS Code** | Use it when you need a fast, cross-platform code editor with intelligent completion, debugging, and the largest extension marketplace — but it's Electron-based and the distributed build includes Microsoft telemetry. | ? (0/6) | [→](vscode.md) |
| **Clash Verge Rev** | Use it when you want a modern cross-platform GUI proxy client with rule-based routing, built-in mihomo kernel, and TUN mode — but it's desktop-only and GPL-3.0 licensed. | ? (0/6) | [→](clash-verge-rev.md) |
| **RustDesk** | Use it when you need an open-source, self-hosted remote desktop for your own machines across platforms — but it requires managing your own relay server or accepting P2P limitations. | ? (0/6) | [→](rustdesk.md) |
| **Tauri** | Use it when you want to build small, fast, secure cross-platform desktop and mobile apps with a web frontend using Rust and native OS webviews instead of Electron. | ? (0/6) | [→](tauri.md) |
| **Deno** | Use it when you want a modern JavaScript/TypeScript runtime with secure defaults, built-in tooling, and native TypeScript support without node_modules. | ? (0/6) | [→](deno.md) |
| **Vaultwarden** | Use it when you want a self-hosted, Bitwarden-compatible password manager in Rust — but it is unofficial, AGPL-3.0, and the core maintainer is a single user. | ? (0/6) | [→](vaultwarden.md) |

| **Bun** | Use it when you want an all-in-one, incredibly fast JavaScript/TypeScript toolkit (runtime, bundler, test runner, package manager) in a single binary — but verify the license before commercial use. | ? (0/6) | [→](bun.md) |
| **Zed** | Use it when you want a high-performance, native code editor with real-time multiplayer collaboration — but its extension ecosystem is far smaller than VS Code's and it's only ~4 years old. | ? (0/6) | [→](zed.md) |
| **ripgrep** | Use it when you need a fast, smart, cross-platform search tool that respects gitignore by default and works identically on Windows, macOS, and Linux. | ? (0/6) | [→](ripgrep.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [DevToys](devtoys.md) | ✅ | B (4/6) | Use it when you want offline, local-only dev utilities (Base64/JSON/hash/diff) in one cross-platform desktop app instead of untrusted online tools. |
| [CyberChef](cyberchef.md) | ✅ | B (6/6) | Use it when you need to chain encode/decode, crypto, compression and data-analysis transforms offline in your browser. |
| [Cockpit](cockpit.md) | ✅ | D (5/6) | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. |
| [Telegraf](telegraf.md) | ✅ | A (5/6) | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. |
| [OpenZL](openzl.md) | ✅ | B (4/6) | Use it when you must squeeze terabytes of one highly structured/numeric format better than generic zstd. |
| [Certbot](certbot.md) | ✅ | A (5/6) | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. |
| [tqdm](tqdm.md) | ✅ | B (5/6) | Use it when you want a fast, low-overhead progress bar for Python loops/CLI/notebooks. |
| [SlimToolkit](slim.md) | ✅ | B (5/6) | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. |
| [Faker (faker-js)](faker-js.md) | ✅ | A (5/6) | Use it when you need realistic fake/mock data (names, addresses, finance…) for tests and seeding in JS/TS. |
| [fontTools](fonttools.md) | ✅ | A (6/6) | Use it when you need programmatic font surgery — subset webfonts, convert formats, inspect/patch tables — but it edits font files, it won't design glyphs or shape text. |
| [Flashlight](flashlight.md) | ✅ | E (3/6) | Use it when you're keeping a vintage macOS 10.10–10.15 machine and want Spotlight plugins — but it's abandoned since 2020 and requires disabling SIP, avoid on real machines. |
| [IdeaVim](ideavim.md) | ✅ | B (5/6) | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. |
| [VS Code](vscode.md) | ✅ | ? (0/6) | Lightweight but powerful cross-platform code editor with the largest extension marketplace; Electron-based, and the Microsoft distribution includes telemetry. |
| [Clash Verge Rev](clash-verge-rev.md) | ✅ | ? (0/6) | Modern cross-platform GUI proxy client with rule-based routing and built-in mihomo kernel; desktop-only and GPL-3.0 licensed. |
| [RustDesk](rustdesk.md) | ✅ | ? (0/6) | Open-source, self-hosted remote desktop across platforms; requires managing your own relay server or accepting P2P limitations. |
| [Tauri](tauri.md) | ✅ | ? (0/6) | Build small, fast, secure cross-platform desktop and mobile apps with web frontend; Rust + native OS webview alternative to Electron. |
| [Deno](deno.md) | ✅ | ? (0/6) | Modern JS/TS runtime with secure defaults, built-in tooling, and native TypeScript; no node_modules, but smaller ecosystem than Node.js. |
| [Vaultwarden](vaultwarden.md) | ✅ | ? (0/6) | Self-hosted, Bitwarden-compatible password manager in Rust; unofficial, AGPL-3.0, single-core-maintainer model. |
| [Zed](zed.md) | ✅ | ? (0/6) | High-performance native code editor with real-time multiplayer collaboration from the creators of Atom; far smaller extension ecosystem than VS Code and only ~4 years old. |
| [ripgrep](ripgrep.md) | ✅ | ? (0/6) | Fast, gitignore-aware line-oriented search tool with first-class cross-platform support; 10 years old with strong Lindy signal and single-maintainer reliability. |
| [Bun](bun.md) | ✅ | ? (0/6) | Incredibly fast all-in-one JS/TS toolkit (runtime, bundler, test runner, package manager); single binary, but custom license (NOASSERTION) and younger than Node.js/Deno. |

## What belongs here

Broadly useful **standalone developer tools and self-hostable infra** that don't fit a narrower AI/agent category — encoders, admin UIs, collectors, compressors. A deliberately wide catch-all; rebalanced into sub-categories if it overflows.
