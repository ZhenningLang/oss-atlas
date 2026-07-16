# de-ai-writing

> Leaf of [agent-skills](../INDEX.md). Humanizing AI text, removing AI tells, and enforcing human-sounding prose.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **Humanizer-zh** | A single Chinese Claude Code skill that rewrites text to strip ~24 tell-tale AI-writing patterns; a localization of blader/humanizer. | C (4/6) | [→](humanizer-zh.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | 去AI味提示词-作家增强-SKILL | ? (0/6) | [→](de-ai-prompt-enhancer-writer-booster-skill.md) |
| **shuorenhua** | Chinese-first rewrite skill for Codex / Claude Code / Cursor / ChatGPT that removes AI tone and preserves facts. | ? (0/6) | [→](shuorenhua.md) |
| **ai-flavor-remover** | AI-flavor removal skill tested by its author on Gemini 2.5 Pro. | ? (0/6) | [→](ai-flavor-remover.md) |
| **humanizer** | Claude Code skill that removes signs of AI-generated writing from text. | ? (0/6) | [→](humanizer.md) |
| **stop-slop** | A skill file for removing AI tells from prose. | ? (0/6) | [→](stop-slop.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Humanizer-zh](humanizer-zh.md) | ✅ | C (4/6) | Chinese-first AI-text humanizing skill; use it as the current in-index baseline. |
| [Baoyu Skills](../writing/baoyu-skills.md) | ✅ | B (4/6) | Broader Chinese content/publishing bundle; Humanizer-zh is narrower and focused on de-AI rewriting. |
| Custom voice guide | 未收录 | — | Better for one private author or brand voice; less reusable than a public skill. |
| [De-AI-Prompt-Enhancer-Writer-Booster-SKILL](de-ai-prompt-enhancer-writer-booster-skill.md) | ✅ | ? (0/6) | 去AI味提示词-作家增强-SKILL |
| [shuorenhua](shuorenhua.md) | ✅ | ? (0/6) | Chinese-first de-AI rewrite skill; compare against Humanizer-zh for Chinese prose cleanup. |
| [ai-flavor-remover](ai-flavor-remover.md) | ✅ | ? (0/6) | Lightweight de-AI writing skill; verify upstream runtime and examples before use. |
| [humanizer](humanizer.md) | ✅ | ? (0/6) | English upstream-style AI-writing humanizer; use Humanizer-zh for Chinese. |
| [stop-slop](stop-slop.md) | ✅ | ? (0/6) | Minimal prose de-slop skill; compare against broader writing bundles when workflow matters. |


## What belongs here

Agent skills whose primary job is to **remove AI writing tells**, humanize prose, preserve facts while changing voice, or enforce human-sounding editorial style.
