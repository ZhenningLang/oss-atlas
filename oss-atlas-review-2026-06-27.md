# oss-atlas Review - 2026-06-27

## 仓库定位

这是一个给 coding agent 读的 OSS 选型知识库，不是应用项目。它的“查询 API”就是 Markdown 目录树：agent 从 `INDEX.md` 进入分类，再读分类 `INDEX.md` 的 one-liner / comparison matrix，最后读项目页里的 `When NOT to use`、`Dependencies`、`Ops difficulty` 来做取舍。

已验证：

```bash
python3 tools/lint.py
```

输出：

```text
29 category nodes, 101 EN + 101 ZH pages, 0 errors, 0 warnings.
```

这说明当前结构性 lint 通过。但本 review 的重点是：lint clean 不等于机制契约和知识质量都没有问题。

## 总体判断

机制层：方向清楚，`AGENTS.md`、`tools/schema.md`、`tools/lint.py` 形成了一个很适合 agent 维护的弱索引系统；主要问题是“契约写得比 lint 覆盖得多”，已有实际漏检。

知识层：大多数项目页比普通 README 更适合选型，尤其是 `When NOT to use` 普遍有实质取舍。但当前内容明显偏向 agent / skill / LLM 生态，且很多单项目类别的分类级 comparison matrix 信息量不足，对“先短名单、再读页面”的流程帮助有限。

## 1. 机制 Review

### High: 双语 frontmatter 一致性是契约，但 lint 没检查，且已有真实漂移

证据：

`tools/schema.md:48-50` 写明：

```text
Frontmatter is byte-identical across the pair
```

`AGENTS.md:56` 写明：

```text
Required frontmatter (identical in both files)
```

但 `tools/lint.py:180-182` 只检查 sibling 是否存在：

```python
sibling = category_dir / (base + (".md" if zh else ZH_SUFFIX))
if not sibling.exists():
    rep.error(path, f"missing {'English' if zh else 'Chinese'} sibling: {sibling.name}")
```

实际漂移：

`categories/llm-training/unsloth.md:9`

```yaml
maturity: "Beta releases (v0.1.x-beta line, 2026-06); very active"
```

`categories/llm-training/unsloth.zh.md:9`

```yaml
maturity: "Beta 发布（v0.1.x-beta 线，2026-06）；非常活跃"
```

影响：[推断] facts 层在英文和中文路径会给 agent 不同事实。更糟的是 lint 仍显示 `0 errors, 0 warnings`，维护者会误以为此类问题被 gate 覆盖。

建议：在 linter 加 pair-level frontmatter raw block 比较；先修 `unsloth` 这处漂移。如果想允许 `maturity` 本地化，那就要改 schema，不要继续写 “byte-identical”。

### High: 递归遍历以 `INDEX.md` 为入口，会漏掉“缺英文 INDEX”的目录

证据：

`tools/lint.py:275`

```python
top_categories = sorted(d for d in categories_dir.iterdir() if d.is_dir() and (d / INDEX_EN).exists())
```

`tools/lint.py:213`

```python
subcats = sorted(d for d in catdir.iterdir() if d.is_dir() and (d / INDEX_EN).exists())
```

同时 `walk_category()` 里的 missing `INDEX.md` 检查只有在目录已被遍历时才执行，见 `tools/lint.py:191-196`。

影响：[推断] 如果新增目录里只有 `INDEX.zh.md`、只有页面文件，或英文 `INDEX.md` 被误删，这个子树可能不进入 lint 检查。对这个 repo 来说，英文 canonical route 是关键路径，这个漏检风险偏高。

建议：扫描 `categories/**/` 下所有含页面、含任一 `INDEX`、或含子目录的目录，再统一检查 EN/ZH `INDEX` 是否成对存在。

### Medium: `add-project` 收录门槛和仓库主契约不一致

证据：

`AGENTS.md:80-82`：

```text
Add any real open-source repo, across any domain
```

`tools/schema.md:112-115` 也写没有领域限制、不要求已有替代品。

但 `.claude/skills/add-project/SKILL.md:15-16`：

```text
only add if you actually evaluated it AND a real selection question exists (substitutes worth comparing)
```

影响：[推断] 维护 agent 可能拒绝 schema/AGENTS 明确允许的长尾 repo，和 “Breadth is the goal” 冲突。

建议：统一到一个标准。更适合当前仓库目标的是保留宽口径：真实开源 git repo、非重复、非空即可；comparison 不足时标注未收录替代品或说明边界，不要拒绝收录。

### Medium: 根路由仍有固定三级表述，和递归树契约冲突

证据：

`INDEX.md:3-4`：

```text
Level 1 of 3
```

`tools/schema.md:128`：

```text
recursive tree, not a fixed 3 levels
```

`AGENTS.md:38-39`：

```text
the tree can be deep
```

影响：[推断] agent 读根索引时可能建立“最多三层”的错误导航模型，后续分类继续拆深时容易提前停止。

建议：把 `INDEX.md` / `INDEX.zh.md` 的 “Level 1 of 3 / 三级路由” 改为“recursive route root / 递归路由根层”。

### Medium: `skill-pack` 应省略三类章节，但 lint 只是不要求，没有禁止误加

证据：

`tools/schema.md:67-70` 说 `skill-pack` 省略 `Tech stack / Dependencies / Ops difficulty`，不是填 N/A。

`tools/lint.py:120-123`：

```python
return core + ([] if ptype in NO_EXTRA_TYPES else extra)
```

影响：[推断] `skill-pack` 页面误加普通软件章节时 lint 仍会通过，破坏 type-adaptive 页面形态。

建议：对 `skill-pack` 增加 forbidden-section check；出现 `## Tech stack`、`## Dependencies`、`## Ops difficulty` 或中文对应标题时报 ERROR。

### Medium: `refactor-index` 里的统计命令在 macOS 不可用

证据：

`.claude/skills/refactor-index/SKILL.md:42-45` 使用：

```bash
find categories -name '*.md' ! -name 'INDEX*' ! -name '*.zh.md' -printf '%h\n' | sort | uniq -c | sort -rn
```

当前环境是 macOS，BSD `find` 不支持 `-printf`。

影响：[推断] 本地维护分类重平衡时，agent 或人照文档运行会失败。

建议：改成 Python stdlib 片段，或把 fanout report 做成 `tools/lint.py --report-fanout`。

### Low: README / AGENTS 把 lint 说成唯一 gate，但语义质量大量不在 lint 覆盖范围内

证据：

`AGENTS.md:89-99` 和 `README.md:323-325` 强调 lint 是唯一 gate。

但 schema 里的这些要求没有被 lint 覆盖：

`tools/schema.md:52-55`：H1 和 TL;DR。

`tools/schema.md:78-90`：`When to use` 必须是 User Story。

`tools/schema.md:92-97`：Comparison 要比较真实替代项目。

`tools/schema.md:45-50`：双语 monolingual mirror。

影响：[推断] 贡献者容易把 `lint clean` 理解成内容质量也通过。

建议：文档里明确 “lint is structural gate, not semantic review”。低成本可补：H1、TL;DR、Comparison table、Caveats bullet list、双语 frontmatter 一致性。

## 2. 知识 Review

### High: 内容覆盖明显偏向 agent / LLM / skill 生态，作为“任意 OSS 选型库”的广度还不成立

证据：本地统计 101 个英文项目页，类型分布：

```text
skill-pack: 41
tool: 25
app: 14
framework: 13
library: 6
service: 1
model: 1
```

Top tags：

```text
44 claude-code
16 skills
15 mcp
12 agent-skills
9 plugin
8 self-hosted
7 skill-pack
7 slash-commands
7 multi-agent
7 codex
```

同时单页类别包括：

```text
api-gateway: 1
captcha: 1
frontend-animation: 1
geospatial: 1
llm-eval: 1
team-chat: 1
```

影响：[推断] 如果 agent 拿这个库去做一般 OSS 选型，会很擅长 agent tooling / skill 生态，但在数据库、后端框架、认证、队列、搜索、监控、前端基础库、移动端、数据工程等常见工程领域上覆盖不足。

建议：如果目标仍是“whatever task an agent gets”，下一阶段不要继续主要加 agent skill collections；优先补高频工程选型域，比如 database、auth、queue、observability、search、backend-frameworks、frontend-ui、data-pipeline、testing、infra-as-code。

### High: 很多单项目类别的分类级 comparison matrix 信息量不足，无法承担 shortlist 功能

证据：

`categories/geospatial/INDEX.md:16-17`

```md
| [QGIS](qgis.md) | ✅ | Full-featured ... |
| ArcGIS / GRASS GIS / gvSIG | 未收录 | Other GIS platforms named on the page. |
```

`categories/api-gateway/INDEX.md:16-17`

```md
| [Kong Gateway](kong.md) | ✅ | OpenResty/Nginx API gateway ... |
| Tyk / KrakenD / Envoy / APISIX | 未收录 | Other API gateways named on the page. |
```

同类模式在 `categories/captcha/INDEX.md:16-17`、`categories/frontend-animation/INDEX.md:16-17`、`categories/llm-eval/INDEX.md:16-17`、`categories/team-chat/INDEX.md:16-17` 等 16 处出现。

影响：[推断] `select-oss` 要求先读分类 INDEX 的 one-liners + comparison matrix 选 1-3 个候选，但这种“多个替代品合并一行 + Other named on page”无法让 agent 在分类层做初筛，只能打开单页再读。

建议：即使替代品未收录，也应拆成独立行，并写真实 tradeoff。例如 api-gateway 应拆 `APISIX`、`Tyk`、`Envoy`、`KrakenD`；frontend-animation 应拆 `GSAP`、`Motion`、`Theatre.js`。这比马上新增完整页面便宜，但会显著提升路由质量。

### Medium: `agent-skill-collections/personal-collections` 达到 `MAX_FANOUT=12` 的边界，且长尾内部差异很大

证据：统计显示：

```text
12 agent-skill-collections/personal-collections
```

`tools/lint.py` 的 overflow 条件是 `n_en_pages > MAX_FANOUT`，所以 12 不报警。`categories/agent-skill-collections/personal-collections/INDEX.md:10-21` 混合了 Vue 生态、Claude harness、中文知识工作、PIP persona、Shape Up、插件生成器等不同意图。

影响：[推断] 这个叶子现在没越线，但已经接近“agent 读一个叶子还要扫太多互不相似对象”的临界点。下一次再加个人 skill collection 就会触发 overflow warning。

建议：提前准备拆分轴，不要等 lint 报了再仓促拆。可考虑按 `engineering-stack`、`knowledge-work-writing`、`methodology-persona`、`harness-plugin` 拆，但是否拆要看后续新增方向。

### Medium: 部分 `Comparison matrix` 复用了 one-liner，没有形成“横向比较”

证据：

`categories/agent-skill-collections/personal-collections/INDEX.md:23-38` 的 `One-line tradeoff` 基本重复 `Collections in this leaf` 的 Use when 文案，例如 `antfu/skills` 在 `:10` 和 `:27` 高度相同，`claude-code-harness` 在 `:11` 和 `:28` 高度相同。

影响：[推断] agent 在分类层会看到两张实质重复的表，无法快速判断“同类之间到底差在哪里”。

建议：`Projects in this category` 可以保留“何时用”；`Comparison matrix` 应改成差异维度，比如 `provenance`、`scope`、`harness`、`strength`、`avoid when`，或者至少把 tradeoff 写成“比同类更偏 X，但牺牲 Y”。

### Medium: README 的“complete index”是手写大表，和 categories 树存在同步成本

证据：

`README.md:34-36` 写：

```text
The complete index, grouped by category.
```

实际同样的项也维护在 `INDEX.md`、各 `categories/**/INDEX.md` 和项目页中。

影响：[推断] 这是明显的重复信息源。现在未发现链接断裂，但新增/移动项目时必须同时改 README、root INDEX、category INDEX、双语 mirror，人工和 agent 都容易漏。lint 当前不检查 README 与 categories 同步。

建议：要么把 README 项目清单改成只指向 `INDEX.md`，要么生成 README 项目表并纳入 lint/脚本。当前 repo 规模 101 项，手写 complete index 会越来越贵。

### Low: 部分知识条目的质量很强，值得作为模板，但模板化经验没有被机制捕获

好例子：

`categories/llm-training/unsloth.md:24-31` 的 `When NOT to use` 清楚覆盖单卡边界、多卡争议、商业层、工作流复现、版本风险。

`categories/geospatial/qgis.md:24-31` 清楚区分 desktop GIS、web map front-end、server SDI、headless ETL、proprietary format、plugin 稳定性。

`categories/api-gateway/kong.md:24-31` 明确说明 PostgreSQL/DB-less、OSS/Enterprise plugin、service mesh、Lua PDK、小规模不值得、Cassandra 移除。

影响：[推断] 这些页面证明这个知识库的写作方向是对的，但新增 entry 可能不会稳定复制这种质量。

建议：在 `tools/schema.md` 或 maintainer skill 中加入一个 “golden examples” 列表，明确新条目可参考这几页的 negative-space 写法。

## 机制与知识的交叉问题

最核心的结构性问题是：这个 repo 的设计哲学依赖 agent “按路由读”，但当前若干路由层内容没有足够信息密度。

`skills/select-oss/SKILL.md:51-53` 要求：

```text
Use the one-liners + comparison matrix to pick 1-3 candidates.
```

但很多单项目分类的 matrix 只给“Other X named on the page”。这不是错误，但削弱了这个 skill 的核心路径。

建议优先级：

1. 先修机制漏检：frontmatter pair check、缺 INDEX 子树发现、skill-pack forbidden sections。
2. 再修分类级 matrix：把合并未收录替代品拆成独立 tradeoff 行。
3. 然后处理 README 重复 SSOT：生成或瘦身。
4. 最后扩领域覆盖：减少继续向 agent-skill 长尾倾斜。

## 验证证据

结构 lint：

```bash
python3 tools/lint.py
```

结果：

```text
29 category nodes, 101 EN + 101 ZH pages, 0 errors, 0 warnings.
```

本地统计确认：

```text
EN pages: 101
Category nodes with INDEX.md: 29
Frontmatter pair mismatches: categories/llm-training/unsloth.md ['maturity']
Largest leaf: agent-skill-collections/personal-collections = 12 pages
Types: skill-pack 41, tool 25, app 14, framework 13, library 6, service 1, model 1
```

## 结论

当前仓库已经是一个可用的 agent-first OSS 选型索引，且结构 lint clean。最值得立刻处理的不是新增内容，而是修“契约与 lint 的落差”：双语 facts 漂移已实际发生，递归目录漏检也是真风险。知识层则应优先提升分类 INDEX 的 shortlist 能力，否则 agent 仍会被迫打开每个页面才能比较，削弱“Markdown 树就是查询 API”的设计目标。
