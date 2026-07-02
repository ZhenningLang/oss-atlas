# agent-skill-collections

> 分类节点。成体系的 agent 技能、提示词、subagent 人设与 harness 配置合集——按用途领域拆分。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类（按领域）

| 叶子 | 里面是什么 | 路由 |
|---|---|---|
| **engineering** | 代码质量、Web 性能、测试与科研/工程工作流。 | [→](engineering/INDEX.zh.md) |
| **design** | 设计审美 / UI-UX 判断——critique、反 AI 味、视觉生成。 | [→](design/INDEX.zh.md) |
| **writing** | 翻译、去 AI 味、编辑腔调。 | [→](writing/INDEX.zh.md) |
| **security** | 安全评审、威胁建模、网络安全 playbook。 | [→](security/INDEX.zh.md) |
| **context-engineering** | 组织、压缩、路由 agent 所读的内容。 | [→](context-engineering/INDEX.zh.md) |
| **vendor-collections** | 官方 / 厂商发布的第一方技能与插件捆绑包。 | [→](vendor-collections/INDEX.zh.md) |
| **subagent-collections** | 成套现成的 subagent 定义 / 人设，直接塞进 harness。 | [→](subagent-collections/INDEX.zh.md) |
| **personal-collections** | 长尾：某个作者策展的技能、subagent 或 harness 配置。 | [→](personal-collections/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **book-to-skill** | 当你想把技术书籍 PDF（及其他文档格式）转成可安装的 agent 技能以用于 Claude Code、Copilot CLI 或 Amp 时用它。 | ?（0/6） | [→](book-to-skill.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [book-to-skill](book-to-skill.zh.md) | ✅ | ?（0/6） | 将技术书籍和文档转成可安装的 agent 技能；批处理工具，不是 live RAG 系统。 |
| [Docling](../document-parsing/docling.zh.md) | ✅ | A（5/6） | 面向 RAG 流水线的通用文档解析器；book-to-skill 是专门针对 agent harness 的技能生成器。 |
| [NotebookLM Claude Code Skill](context-engineering/notebooklm-skill.zh.md) | ✅ | C（4/6） | 查询外部 Google 服务；book-to-skill 处理本地 PDF，无外部依赖。 |
| LlamaIndex / RAG 管线 | 未收录 | — | 带嵌入和动态检索的完整 RAG；基础设施比静态技能生成器更重。 |

## 什么该放这里

一个刻意拥挤的领域——agent **技能 / 提示词 / subagent 人设 / harness 配置**的合集，没有哪一个是唯一答案。
按用途领域组织（长尾再按来源：厂商 vs 个人），让 agent 能按任务和出处挑捆绑包。自平衡：某叶子超出 fanout 就继续拆。
