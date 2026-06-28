# diagramming

> 分类节点。从文本生成图表(diagrams-as-code)，用于 Markdown、文档和 Web。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Mermaid** | 当你想把图表写成可进版本库的纯文本(流程图/时序图/ER)，在 Markdown 和文档里渲染时用它——不适合像素级精确排版。 | [→](mermaid.zh.md) |
| **flowchart.js** | 一个很小的 JavaScript 库，把一段小型文本 DSL 在浏览器里渲染成 SVG 流程图——把节点和连线写成文本，得到一张画好的图。 | [→](flowchart-js.zh.md) |
| **bpmn-js** | 面向浏览器的 BPMN 2.0 渲染与建模工具包——导入 BPMN XML、渲染成可交互的图、并就地编辑，由 Camunda 旗下 bpmn.io 团队打造。 | [→](bpmn-js.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Mermaid](mermaid.zh.md) | ✅ | 处处可渲染的纯文本图表；以布局控制力换取可移植性。 |
| [flowchart.js](flowchart-js.zh.md) | ✅ | 一个很小的 JavaScript 库，把一段小型文本 DSL 在浏览器里渲染成 SVG 流程图——把节点和连线写成文本，得到一张画好的图。 |
| [bpmn-js](bpmn-js.zh.md) | ✅ | 面向浏览器的 BPMN 2.0 渲染与建模工具包——导入 BPMN XML、渲染成可交互的图、并就地编辑，由 Camunda 旗下 bpmn.io 团队打造。 |
| Graphviz / PlantUML / D2 / draw.io / Excalidraw | 未收录 | 各页对比里点到的其他图引擎/编辑器(布局更可控或所见即所得)。 |

## 什么该放这里

主要职责是**把文本变成图表**(diagrams-as-code)或渲染图表的库/工具。不含以自由白板为主用途的应用，不含 UI 动画(见 `frontend-animation`)。
