---
name: asciimatics
slug: asciimatics
repo: https://github.com/peterbrittain/asciimatics
category: terminal-ui
tags: [terminal-ui, tui, curses, ascii-art, animation, cross-platform, python, widgets]
language: Python
license: Apache-2.0
maturity: v1.15.x, active (2026-06)
last_verified: 2026-06-28
type: library
---

# asciimatics

A cross-platform Python library for full-screen text UIs — a single curses-like API plus a widget/forms toolkit and an ASCII animation/effects engine, working the same on Linux, macOS and Windows.

## When to use

You're a Python developer who needs a real full-screen terminal interface — an interactive form, a dashboard, a wizard — and you want it to behave identically on a colleague's Windows laptop, your Mac, and the Linux CI box. The stdlib `curses` module is Unix-only and famously fiddly, and you don't want to ship two code paths. You pull in asciimatics: it gives you one `Screen` abstraction that handles colour/styled text (including 256-colour and CJK unicode), cursor positioning, non-blocking keyboard and mouse input, and console-resize detection across all three platforms. On top of that it ships a `Frame`/widget layer — text boxes, lists, buttons, layouts — so you can assemble a form-driven TUI without hand-rolling the event loop.

You also reach for it when you want the *fun* layer: scrolling banners, sprites, particle effects, Conway's Life, transitions between scenes. asciimatics started as an animation toolkit (the name is a pun), so if you're building a splash screen, a retro demo, an ASCII-art intro, or a teaching visual, the `Effect`/`Scene`/`Renderer` model is purpose-built for it. It's the same library whether you want a serious data-entry screen or a credits-roll animation.

## When NOT to use

- **You only target Linux/macOS and want maximum control.** If cross-platform isn't a requirement, raw `curses` or a lower-level binding has no extra dependency and finer control — asciimatics' abstraction is a convenience layer you may not need.
- **You want a modern, reactive, richly-styled TUI framework.** Textual (CSS-like styling, async, mouse-first widgets) or `urwid` target richer app UIs; asciimatics' widget set is functional but more spartan and its API is older-style. Compare before committing to a large app.
- **You just want pretty static output, tables, progress bars, or markup.** `rich` is the better fit for styled non-fullscreen output — asciimatics takes over the whole screen and is overkill for log colouring or a progress bar.
- **You need ASCII-art text banners or image-to-ASCII only.** Use a focused library ([art](art.md) for figlet-style text, image-to-ASCII converters for pictures); asciimatics is a UI/animation engine, not a font/art generator.
- **Single-maintainer risk matters to you.** Development is driven primarily by one author; for a long-lived production dependency, weigh the bus-factor (see Health). [推断]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| Textual | 未收录 | Modern async, CSS-styled, mouse-first TUI framework (Textualize); much richer widget/styling model and active backing, but heavier and a different programming model than asciimatics' curses-like API. |
| urwid | 未收录 | Long-established Python console UI library with a flexible widget/layout system; Unix-focused (weaker Windows story) and no animation engine. |
| rich | 未收录 | Styled terminal *output* (tables, markup, progress, syntax) — not a full-screen UI/event loop; complementary, not a substitute for interactive screens. |
| blessed / curses (stdlib) | 未收录 | Lower-level terminal control; `curses` is Unix-only, `blessed` is a friendlier wrapper — neither ships widgets or an animation framework. |
| prompt_toolkit | 未收录 | Powerful for interactive prompts/REPLs and some full-screen apps; strong line-editing, but a different focus (input) and no ASCII-effects engine. |

## Tech stack

- **Language:** pure Python (supports current CPython versions; verify the exact minimum against the repo's `setup`/`pyproject` for your version). [未验证]
- **Core abstraction:** a `Screen` class wrapping platform-specific terminal back-ends — `curses` on Unix-likes, native console APIs on Windows — to present one cross-platform surface.
- **Widget layer:** `Frame`, `Layout`, and widgets (text, list, button, etc.) with a scene/effect model on top.
- **Animation engine:** `Scene` / `Effect` / `Renderer` primitives for sprites, particles, transitions and ASCII-art rendering.

## Dependencies

- **Runtime:** Python plus a small set of pip dependencies (e.g. a Windows console binding such as `pywin32`/`pyfiglet`-style helpers and `wcwidth`); install via `pip install asciimatics`. Exact dependency list is in the packaging metadata. [未验证]
- **Platform:** a terminal/console; on Windows it uses native console APIs rather than requiring a Unix `curses`.
- **No external services or datastore** — it's an in-process UI library.

## Ops difficulty

**Low.** It's a library, not a service — there's nothing to deploy or operate. The burden is purely development-time: it grabs the whole terminal, so you design around its event loop and scene model, and you test rendering across the terminals you actually target (colour support, resize behaviour, and CJK/unicode width handling differ between emulators). No datastore, no network, no runtime infra.

## Health & viability

- **Maintenance (2026-06).** Last pushed 2025-06; commits continue but cadence is modest. Releases are tagged (1.15.x line). Reads as **maintained but slow-moving**, not abandoned — not archived. [推断]
- **Governance / bus factor.** A single-maintainer project (Peter Brittain) on a personal account with a long tail of occasional contributors; roadmap depends largely on one person. That's the main governance risk for a long-term dependency. [推断]
- **Age & Lindy verdict.** ~11 years old (created 2015-04) and still receiving commits ⇒ a **strong Lindy** signal: a mature, stable library that has long since found its shape, not a hyped newcomer. [推断]
- **Adoption.** ~4.3k stars and broad use as the go-to cross-platform Python TUI/animation library; well-documented with examples. [未验证]
- **Risk flags.** Apache-2.0 (permissive, no relicense history found); the realistic risk is maintenance velocity/bus-factor, not licensing. [推断]

## Caveats (unverified)

- [未验证] ~4.3k GitHub stars and 1.15.x release line as of 2026-06; star counts and version numbers drift — treat as indicative only.
- [未验证] Exact Python version floor and the precise runtime dependency list are governed by the repo's packaging metadata and change across releases; not asserting specific values.
- [推断] "Maintained but slow-moving" is inferred from a 2025-06 last-push and modest commit cadence, not a measured release-frequency figure.
- [推断] Single-maintainer/bus-factor characterization is inferred from the contributor distribution and personal-account ownership, not a stated governance document.
- [推断] Textual/urwid being "richer" is a general characterization of their feature sets, not a feature-by-feature audit against asciimatics.
