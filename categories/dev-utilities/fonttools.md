---
name: fontTools
slug: fonttools
repo: https://github.com/fonttools/fonttools
category: dev-utilities
tags: [fonts, typography, opentype, truetype, woff, python, font-manipulation]
language: Python
license: MIT
maturity: v4.63.0, active (2026-06)
last_verified: 2026-06-28
type: library
---

# fontTools

A Python library (plus a set of command-line tools) to read, write, and manipulate font files — TrueType/OpenType, WOFF/WOFF2, AFM, and more — the de-facto foundation of the open-source font tooling stack.

## When to use

You're building a font pipeline: maybe you're a type designer's engineer turning a UFO/glyph source into shippable `.otf`/`.ttf`/`.woff2`, or a frontend platform team that needs to **subset** webfonts down to the glyphs a page actually uses so the download is a few KB instead of hundreds. You don't want to parse the binary `sfnt`/`glyf`/`GPOS` tables by hand, and you don't trust a one-off script to round-trip a font without corrupting its tables. You `pip install fonttools`, then either call the library — `TTFont("in.ttf")` gives you a navigable object model of every table you can read, edit, and save — or run the bundled CLIs: `ttx` to dump a font to editable XML and recompile it, `pyftsubset` to cut a font down to a glyph set, `ttx`/`fontTools.ttLib` to merge, instance a variable font, or fix metadata. It's the library that other font tools (and most webfont build steps) are built on.

You reach for it whenever the task is *programmatic font surgery*: subsetting for the web, converting formats, inspecting/patching tables, instancing variable fonts to static cuts, or feeding a larger build system (it's a dependency of matplotlib, of many designer toolchains, and of webfont services). [未验证]

## When NOT to use

- **You want to *design* glyphs or draw outlines.** fontTools manipulates font *files and tables*; it is not a font editor. For drawing/editing use Glyphs, FontForge, or RoboFont — fontTools is the engine behind/around them, not the canvas.
- **You need rich text shaping / rendering.** Turning text + a font into positioned glyphs (complex scripts, ligatures, bidi) is HarfBuzz's job; fontTools reads the GSUB/GPOS tables but doesn't shape or rasterize.
- **You only need to subset once via a GUI/CLI and never script it.** That's fine, but then a wrapper tool may be simpler than the library API.
- **Hard real-time or memory-tight embedded contexts.** It's a pure-Python object model that loads tables into memory; for constrained runtime font handling a C library (FreeType, HarfBuzz) is the right layer.
- **You expect every niche table to be fully supported / round-trip-perfect.** Coverage is broad but the format is vast; exotic or vendor tables may be passed through opaquely rather than modeled — verify the specific table you depend on. [未验证]

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| FontForge | 未收录 | Full GUI/scriptable font editor (design + production); much broader feature surface but heavier, C-based, and a different (editor) workflow than a clean Python library. |
| HarfBuzz | 未收录 | Text shaping engine (text → positioned glyphs); complementary, not a substitute — fontTools edits the font, HarfBuzz uses it to shape. |
| FreeType | 未收录 | C rasterizer/loader for rendering glyphs at runtime; about drawing pixels, not editing font files. |
| Glyphs / RoboFont | 未收录 | Commercial macOS type-design apps; for drawing typefaces, often *use* fontTools under the hood for export. |
| `woff2`/`sfnt2woff` CLIs | 未收录 | Single-purpose format converters; fontTools covers the same conversions plus full table manipulation and subsetting. |

## Tech stack

- **Language:** Python (pure-Python core; optional C-accelerated and native deps for specific features).
- **Model:** `TTFont` object model over `sfnt`-based formats — per-table classes for `cmap`, `glyf`, `GPOS`/`GSUB`, `name`, `head`, etc.; XML round-trip via `ttx`.
- **CLIs:** `ttx` (font ↔ XML), `pyftsubset` (subsetting), `pyftmerge` (merge), `fonttools` entry point exposing subcommands (instancer for variable fonts, etc.).
- **Formats:** TrueType/OpenType (`.ttf`/`.otf`), WOFF/WOFF2, AFM, T1/CFF, and more.

## Dependencies

- **Runtime:** Python; the base library is pure-Python with **no required external services**. Optional extras pull native deps — e.g. WOFF2 (`brotli`), unicode data, faster XML (`lxml`), graphite, plotting — installed via `pip install fonttools[woff,unicode,...]`. [未验证]
- **Services/infra:** none — it's an in-process library/CLI; no datastore or daemon.
- **Build:** standard Python packaging; optional native extras need their respective build prerequisites.

## Ops difficulty

**Low.** `pip install fonttools` (add extras like `[woff]` for WOFF2) and you're done — no services, no datastore, no daemon. It runs in-process or as a CLI step in a build. The only real friction is choosing the right optional extras for the formats you touch (WOFF2 needs brotli) and the inherent complexity of the font format itself when you do deep table surgery — that's domain difficulty, not ops.

## Health & viability

- **Maintenance (2026-06).** Very active: v4.63.0 released 2026-05, last push 2026-06, on a steady frequent minor-release cadence. Not archived — clearly maintained, not coasting. [推断]
- **Governance / bus factor.** Lives under the `fonttools` **GitHub organization** with a long contributor history led by Behdad Esfahbod and Cosimo Lupo (anthrotype) among hundreds of contributors — multi-maintainer, not a single point of failure; healthier bus factor than most font tools. [推断]
- **Age & Lindy.** Created 2013 on GitHub but the codebase's lineage (Just van Rossum's TTX/fontTools) predates that by years; ~13+ years here and **still actively shipping** ⇒ a **strong Lindy** signal — it is the established standard, not a newcomer. [推断]
- **Adoption.** Foundational: a dependency of matplotlib and a backbone of the open-source font/webfont toolchain; broad real-world use. ~400+ open issues are consistent with a large surface and active triage, not a red flag on their own. [未验证]
- **Risk flags.** None notable — permissive MIT, no relicense history found, diversified maintainership. The main caveat is format breadth (not every exotic table is deeply modeled), not project health. [推断]

## Caveats (unverified)

- [未验证] ~5.1k GitHub stars and ~400 open issues as of 2026-06; star/issue counts are date-sensitive and indicative only.
- [未验证] v4.63.0 dated 2026-05; release cadence and exact version shift over time — verify against the current releases page.
- [未验证] The set of optional extras (brotli for WOFF2, lxml, unicodedata2, etc.) and which features they gate is taken from packaging metadata/README and may change; check current `pyproject` extras.
- [推断] "Foundation of the font tooling stack" and specific downstream dependents (matplotlib, designer toolchains) are inferred from ecosystem knowledge; the exact current dependency set is not enumerated here.
- [推断] Per-table coverage and round-trip fidelity for exotic/vendor tables is an inference from the format's breadth, not a measured claim about any specific table.
