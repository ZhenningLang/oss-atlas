# oss-atlas — 分类路由

> 三级路由的第 1 级。Agent 先读这张总表，按「何时进这个分类」选分类，再进分类的 `INDEX.zh.md`，
> 最后看项目页。
> English index: [INDEX.md](INDEX.md) · 完整读取流程见 [AGENTS.md](AGENTS.md)

## 分类

| 分类 | 何时进来 | 路由 |
|---|---|---|
| **agent-tooling** | 为 AI 编码 agent 选「任务/工作追踪、持久记忆、agent 状态」基建。 | [→](categories/agent-tooling/INDEX.zh.md) |
| **document-management** | 选「文档归档/OCR/打标签/全文检索」系统。 | [→](categories/document-management/INDEX.zh.md) |
| **on-device-ml** | 选「在端侧/边缘设备（手机、笔记本、IoT）本地跑模型」的运行时。 | [→](categories/on-device-ml/INDEX.zh.md) |
| **web-automation** | 选「驱动/自动化 Web 界面」的工具——浏览器自动化，或页内自然语言 GUI agent。 | [→](categories/web-automation/INDEX.zh.md) |
| **llm-training** | 微调或强化训练 LLM 与多步 agent。 | [→](categories/llm-training/INDEX.zh.md) |
| **agent-frameworks** | 构建与运行多步 / 多智能体系统——agent 框架与 agent 操作系统。 | [→](categories/agent-frameworks/INDEX.zh.md) |
| **agent-memory** | 面向 agent、与 LLM 无关的跨会话持久记忆基础设施。 | [→](categories/agent-memory/INDEX.zh.md) |
| **deep-research** | 迭代式多源研究 agent:搜索、抓取、综合成报告。 | [→](categories/deep-research/INDEX.zh.md) |
| **ai-code-review** | LLM 辅助的代码评审:对 diff 或仓库产出行级问题。 | [→](categories/ai-code-review/INDEX.zh.md) |
| **rag-retrieval** | 面向 RAG 的文档索引、代码智能图与图数据库。 | [→](categories/rag-retrieval/INDEX.zh.md) |
| **llm-eval** | 对提示词、agent 与 RAG 做测试、基准与安全红队扫描。 | [→](categories/llm-eval/INDEX.zh.md) |

## 如何新增分类

新分类 = `categories/` 下一个新目录，自带 `INDEX.md` **和** `INDEX.zh.md`，并在本表和
[INDEX.md](INDEX.md) 各加一行。只有当一个项目确实放不进现有分类时才新建。详见
[tools/schema.md](tools/schema.md) 与 `add-project` 技能。
