# de-ai-writing

> [agent-skills](../INDEX.zh.md) 的叶子。去 AI 味、消除机器腔、让文本更像真人写作。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根[路由](../../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本叶子集合

| 集合 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Humanizer-zh** | 一个简体中文 Claude Code 单技能，按约 24 条清单改写掉文本里的 AI 痕迹，是 blader/humanizer 的本地化版。 | C（4/6） | [→](humanizer-zh.zh.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | 去 AI 味提示词和作家增强 skill。 | ?（0/6） | [→](de-ai-prompt-enhancer-writer-booster-skill.zh.md) |
| **shuorenhua** | 中文优先的去 AI 味改写 skill，面向 Codex / Claude Code / Cursor / ChatGPT。 | ?（0/6） | [→](shuorenhua.zh.md) |
| **ai-flavor-remover** | 作者标注只在 Gemini 2.5 Pro 上测试过的 AI 味去除 skill。 | ?（0/6） | [→](ai-flavor-remover.zh.md) |
| **humanizer** | 移除英文文本中 AI 写作痕迹的 Claude Code skill。 | ?（0/6） | [→](humanizer.zh.md) |
| **stop-slop** | 用于移除 prose 中 AI 痕迹的 skill 文件。 | ?（0/6） | [→](stop-slop.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Humanizer-zh](humanizer-zh.zh.md) | ✅ | C（4/6） | 中文优先的去 AI 味 skill；作为当前索引里的基线使用。 |
| [Baoyu Skills](../writing/baoyu-skills.zh.md) | ✅ | B（4/6） | 更宽的中文内容 / 发布套件；Humanizer-zh 更窄，聚焦去 AI 味改写。 |
| 自写 voice guide | 未收录 | — | 更适合一个私有作者或品牌 voice；但不如公共 skill 可复用。 |
| [De-AI-Prompt-Enhancer-Writer-Booster-SKILL](de-ai-prompt-enhancer-writer-booster-skill.zh.md) | ✅ | ?（0/6） | 去 AI 味提示词和作家增强 skill。 |
| [shuorenhua](shuorenhua.zh.md) | ✅ | ?（0/6） | 中文优先的去 AI 味改写 skill；中文文案清理时和 Humanizer-zh 对比。 |
| [ai-flavor-remover](ai-flavor-remover.zh.md) | ✅ | ?（0/6） | 轻量去 AI 味 writing skill；使用前核验上游运行环境和示例。 |
| [humanizer](humanizer.zh.md) | ✅ | ?（0/6） | 英文上游风格的 AI 写作 humanizer；中文场景优先看 Humanizer-zh。 |
| [stop-slop](stop-slop.zh.md) | ✅ | ?（0/6） | 极简去机器腔 skill；需要完整流程时再对比更宽的写作套件。 |


## 什么该放这里

主要职责是**去除 AI 写作痕迹**、让文本更像真人、保事实改 voice，或执行真人编辑风格规则的 agent skill。
