# terminal-ui

> Category node. Terminal/CLI UI libraries — colors, TUIs, ASCII art, terminal rendering.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **colorama** | Use it when a Python CLI needs ANSI colored output that also works on legacy Windows consoles — but it's only a color/style shim (no tables, TUI, or guaranteed truecolor) and largely a no-op on modern terminals. | [→](colorama.md) |
| **asciimatics** | Use it when you need a cross-platform full-screen Python TUI plus an ASCII animation engine on Linux/macOS/Windows — but the widget set is spartan, the API older-style, and it's single-maintainer. | [→](asciimatics.md) |
| **Terminal Markdown Viewer (mdv)** | Use it when you want one-shot read-only Markdown rendered with color/syntax-highlighting in a plain terminal over SSH — but it's low-activity (0.x, 2024-05) and glow/mdcat are the modern defaults. | [→](terminal-markdown-viewer.md) |
| **ART** | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. | [→](art.md) |
| **asciify** | Use it as a minimal, legible copy-paste reference for the image-to-ASCII algorithm — but it ships NO license (all rights reserved), is unmaintained since 2022, so never vendor it into a product. | [→](asciify.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [colorama](colorama.md) | ✅ | Use it when a Python CLI needs ANSI colored output that also works on legacy Windows consoles — but it's only a color/style shim (no tables, TUI, or guaranteed truecolor) and largely a no-op on modern terminals. |
| [asciimatics](asciimatics.md) | ✅ | Use it when you need a cross-platform full-screen Python TUI plus an ASCII animation engine on Linux/macOS/Windows — but the widget set is spartan, the API older-style, and it's single-maintainer. |
| [Terminal Markdown Viewer (mdv)](terminal-markdown-viewer.md) | ✅ | Use it when you want one-shot read-only Markdown rendered with color/syntax-highlighting in a plain terminal over SSH — but it's low-activity (0.x, 2024-05) and glow/mdcat are the modern defaults. |
| [ART](art.md) | ✅ | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. |
| [asciify](asciify.md) | ✅ | Use it as a minimal, legible copy-paste reference for the image-to-ASCII algorithm — but it ships NO license (all rights reserved), is unmaintained since 2022, so never vendor it into a product. |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries that **render UI in the terminal** — colors, TUIs, ASCII art, styled output.
