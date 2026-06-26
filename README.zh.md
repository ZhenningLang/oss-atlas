# oss-atlas

**一个面向 coding agent 的开源项目「选型」自然语言索引。**
agent 收到任务时读这个索引来挑开源项目——重点是衡量每个候选*何时不该用*，而不只是它能干什么。

> English README: [README.md](README.md)

## 项目总表

完整索引。每个项目有一份干净的英文页（`<slug>.md`）和一份中文页（`<slug>.zh.md`），点击直达：

| 分类 | 项目 | 是什么 | 何时别选它 | 许可证 | 页面 |
|---|---|---|---|---|---|
| `agent-tooling` | **beads** | 依赖感知、可版本控制的任务/issue 图，给 AI agent 持久的结构化记忆（Dolt 支撑的 Go 二进制）。 | 你需要人类 web UI、跨仓视图，或生产级稳定性（它仍 alpha、嵌入模式单写入）。 | MIT | [中](categories/agent-tooling/beads.zh.md) · [EN](categories/agent-tooling/beads.md) |
| `document-management` | **paperless-ngx** | 自托管 DMS：对扫描件做 OCR + 打标签 + 全文检索（Django/Angular + Postgres）。 | 你需要静态加密、严格多租户权限，或企业级审批 / EDMS 工作流。 | GPL-3.0 | [中](categories/document-management/paperless-ngx.zh.md) · [EN](categories/document-management/paperless-ngx.md) |
| `on-device-ml` | **LiteRT-LM** | Google 架在 LiteRT 之上的端侧 LLM 运行时——在手机/笔记本/边缘经 CPU/GPU/NPU 跑 Gemma 等。 | 你需要大量非 Gemma 模型、云级延迟、冻结的 API，或在小内存设备上跑。 | Apache-2.0 | [中](categories/on-device-ml/litert-lm.zh.md) · [EN](categories/on-device-ml/litert-lm.md) |
| `web-automation` | **page-agent** | 页内 GUI agent：用自然语言、直接读写 DOM 来操作 Web UI，无需后端。 | 你需要视觉/多模态、服务端自动化、高并发，或不能把 DOM 发给外部 LLM。 | MIT | [中](categories/web-automation/page-agent.zh.md) · [EN](categories/web-automation/page-agent.md) |

按分类浏览见 [INDEX.zh.md](INDEX.zh.md)；agent 应从 [AGENTS.md](AGENTS.md) 开始（英文）。

## 为什么做这个

多数开源 README 是营销：讲它能干啥、为啥好，却**不**告诉你何时*不该*用、和替代怎么比、运维成本多少。
做选型的 agent 恰恰需要这片「负空间」。oss-atlas 把 README 这个体裁反转成**决策支持**体裁。

索引刻意做得「弱」——没有数据库、没有搜索、没有 embedding，就是给 agent 读和推理的 Markdown。
目录结构本身就是「查询 API」。

## 结构（三级，双语）

```
INDEX.md / INDEX.zh.md                       # 一级：分类路由（英 / 中）
categories/<分类>/INDEX.md / INDEX.zh.md     # 二级：项目 + 对比矩阵
categories/<分类>/<slug>.md                  # 三级：英文选型页（canonical）
categories/<分类>/<slug>.zh.md               # 三级：中文选型页
```

每个项目页 = YAML frontmatter（**事实**，带日期）+ 正文（**判断**），含六个必需小节：
`何时使用 / 何时不用 / 横向对比 / 技术栈 / 依赖 / 运维难度`（英文页用英文标题）。
英文是 agent 默认读取的 canonical 路径，`.zh.md` 是同一内容的中文版。

## 新鲜度

事实会过期。每页记 `last_verified`。超过 90 天 linter 会告警；`sync-entry` 技能负责对照线上仓库
重核。把任何事实都当作**时点快照**，并按真话纪律标注（`[未验证]` / `[推断]`）。

## 贡献

策展，而非求全。一个项目只有在**确实被评估过**、**且存在真实选型问题**（有值得对比的替代）时才进。
见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [tools/schema.md](tools/schema.md)。

```bash
python3 tools/lint.py    # 唯一的门；没有单元测试（这是内容仓库）
```

## 许可证

- **工具**（代码，如 `tools/lint.py`）：MIT——见 [LICENSE](LICENSE)。
- **内容**（`categories/` 下的散文、路由页、文档）：CC BY 4.0——见 [LICENSE-CONTENT](LICENSE-CONTENT)。

各项目页描述的是第三方项目，其归属与许可证由各自作者决定；CC BY 4.0 仅覆盖这里的原创分析。
