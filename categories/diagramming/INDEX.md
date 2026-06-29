# diagramming

> Category node. Generate diagrams from text (diagrams-as-code) for Markdown, docs, and the web.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mermaid** | Use it when you want diagrams as version-controlled plain text (flowchart/sequence/ER) rendered in Markdown and docs — not pixel-precise layouts. | A (6/6) | [→](mermaid.md) |
| **flowchart.js** | Use it when you want simple flowcharts authored as git-diffable text and rendered to SVG in the browser — but it only renders, depends on aging Raphael.js, and chokes on complex diagrams. | B (5/6) | [→](flowchart-js.md) |
| **bpmn-js** | Use it when business analysts must author or view standards-correct BPMN 2.0 diagrams inside your web app — but its license mandates a non-removable bpmn.io watermark, so confirm terms before white-labeling. | B (5/6) | [→](bpmn-js.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mermaid](mermaid.md) | ✅ | A (6/6) | Plain-text diagrams rendered everywhere; trades layout control for portability. |
| [flowchart.js](flowchart-js.md) | ✅ | B (5/6) | Use it when you want simple flowcharts authored as git-diffable text and rendered to SVG in the browser — but it only renders, depends on aging Raphael.js, and chokes on complex diagrams. |
| [bpmn-js](bpmn-js.md) | ✅ | B (5/6) | Use it when business analysts must author or view standards-correct BPMN 2.0 diagrams inside your web app — but its license mandates a non-removable bpmn.io watermark, so confirm terms before white-labeling. |
| Graphviz / PlantUML / D2 / draw.io / Excalidraw | 未收录 | — | Other diagram engines / editors named across the pages (more layout control or WYSIWYG). |

## What belongs here

Libraries/tools whose primary job is **turning text into diagrams** (diagrams-as-code) or rendering them. Not freeform whiteboard apps as the main use case, not UI animation (see `frontend-animation`).
