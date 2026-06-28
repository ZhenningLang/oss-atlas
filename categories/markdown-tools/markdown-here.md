---
name: Markdown Here
slug: markdown-here
repo: https://github.com/adam-p/markdown-here
category: markdown-tools
tags: [inline]
language: JavaScript
license: MIT
maturity: "v2.16.0, low-cadence/effectively stale, ~60.2k stars (last pushed 2025-08)"
last_verified: 2026-06-28
type: tool
---

# Markdown Here

A Chrome/Firefox/Thunderbird browser extension that converts Markdown you type into a supported email or web textarea into rendered HTML in place — one click before you hit send.

## When to use

You're an engineer who writes a lot of email — code review notes, incident summaries, "here's how to reproduce it" walkthroughs — and your webmail compose box gives you a bare textarea with a clumsy WYSIWYG toolbar. You want a bulleted list, a fenced code block with syntax highlighting, a table, and a couple of links, and hand-formatting all of that with the toolbar is slow and ugly. You install Markdown Here, type the message in plain Markdown the way you'd write a `README`, and when it's ready you hit the toggle (or a hotkey): the extension parses the Markdown in that field and replaces it with rendered HTML right inside the compose area, so the recipient sees a properly formatted message in any mail client. If you got something wrong you can toggle back to the Markdown source, fix it, and re-render. It also lights up in a number of non-mail web textareas (Google Groups, some blogging/forum compose fields), so the same muscle memory works beyond email.

It earns its place precisely because it's *inline and on-demand* in fields you don't control: you're not exporting a file or running a build, you're turning the text already in the compose box into HTML at the moment you send. For the narrow job of "write this one email in Markdown," it's far lighter than drafting in an external editor and pasting.

## When NOT to use

- **Maintenance / longevity risk — the sharpest reason.** The original repo is widely treated as low-maintenance/effectively stale: high star count, but slow release cadence and a long backlog. [推断] Don't build a workflow that *depends* on it receiving timely fixes.
- **Browser-extension viability under Manifest V3.** It's a content-script extension living inside Chrome's MV3 migration; an unmaintained MV3 extension can be delisted or broken by a browser update, which is an availability risk outside your control. [未验证]
- **It only converts on demand, in *supported* fields.** It's not a universal "Markdown everywhere" layer — it works in the mail clients and textareas it has integrations for, and only when you trigger the toggle. If your target field isn't supported, it does nothing.
- **You need a Markdown *renderer/library* for a program.** This is a UI convenience, not an API. To parse Markdown to HTML in code (a site, a docs build, a server), use a parsing library like marked — Markdown Here is not embeddable.
- **Docs / publishing pipelines.** For a static site, knowledge base, or CI-rendered docs you want a deterministic build step and a real renderer, not a browser extension toggling one compose box at a time.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| marked | 未收录 | A Markdown→HTML *parsing library* you call from JavaScript; the right tool when you need rendering inside an app or pipeline — but it's not a browser UI, you wire up the editor/compose integration yourself. |
| Browser-native rich-text compose (Gmail/Outlook toolbars) | 未收录 | Built into the mail client, nothing to install; but it's WYSIWYG-by-toolbar with no Markdown and weak code-block/table support — exactly the friction Markdown Here removes. |
| Obsidian / editor Markdown plugins | 未收录 | First-class Markdown authoring with live preview, but inside a *document editor*, not your webmail compose box; you'd draft there and paste, losing the in-field, at-send-time conversion. |
| Markdown Here Revival (fork/successor) | 未收录 | A community fork aimed at keeping the idea alive (notably for Thunderbird), as the original stalled; hosting and its own maintenance status should be verified before relying on it (see Caveats). |

## Tech stack

- **Language:** JavaScript — a browser/WebExtension content-script extension (the compose-field code runs in the page, the conversion logic is bundled with the extension).
- **Markdown rendering:** Markdown is parsed to HTML and code blocks get syntax highlighting; the project bundles its own JS rendering/highlighting rather than calling out to a service (see Caveats).
- **Targets:** packaged for Chrome (and Chromium/Opera), Firefox, and Thunderbird, plus integrations for a set of webmail and web-textarea compose surfaces.

## Dependencies

- **Runtime:** a supported browser (Chrome/Chromium/Opera, Firefox) or Thunderbird — there is no server, account, or backend; everything runs client-side in the extension.
- **Distribution:** installed from the browser/add-on store or loaded as an unpacked/packaged extension; subject to that store's review and Manifest-version requirements.
- **Build:** to build from source you need a Node/JS toolchain; the exact versions are governed by the repo's tooling at build time.

## Ops difficulty

**Low.** There is nothing to operate — no service, datastore, or deployment. For an end user it's an install-and-toggle extension. The real "ops" cost is *longevity*, not running it: because the original project moves slowly, the practical risk is that a future browser change (especially in the MV3 transition) breaks or delists it and no timely fix lands, at which point you'd migrate to a maintained fork or a different approach. Treat it as a convenience you can lose, not infrastructure you depend on.

## Caveats (unverified)

- [未验证] ~60.2k GitHub stars and v2.16.0 with a last push around 2025-08 (per the repo, 2026-06); star counts and dates are time-sensitive and indicative only — re-check against the current repo.
- [推断] "Low-maintenance / effectively stale" is inferred from the slow release cadence and large open backlog relative to the star count, not from any deprecation notice in the README — the README does not declare the project dead.
- [未验证] Manifest V3 status and whether the extension is currently listed/installable in each browser's store shift over time; verify in the target browser before relying on it.
- [未验证] The exact set of supported mail clients and web textareas, and how each integration holds up, varies and may have regressed — confirm your specific compose surface works.
- [未验证] "Markdown Here Revival" exists as a community fork/successor (notably for Thunderbird) but its canonical hosting and current maintenance status were not confirmed here — verify before adopting it.
