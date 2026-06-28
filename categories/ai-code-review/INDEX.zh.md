# ai-code-review

> 分类节点。LLM 辅助的代码评审：对 diff 或仓库产出行级问题。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Open Code Review** | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 | [→](open-code-review.zh.md) |
| **Claude Code Security Review** | 当你想用 Claude 在可信 PR 上做上下文感知的安全审查、且接受按 token 计费与非确定性结果时使用。 | [→](claude-code-security-review.zh.md) |
| **React Doctor** | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 | [→](react-doctor.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Open Code Review](open-code-review.zh.md) | ✅ | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 |
| [Claude Code Security Review](claude-code-security-review.zh.md) | ✅ | 当你想用 Claude 在可信 PR 上做上下文感知的安全审查、且接受按 token 计费与非确定性结果时使用。 |
| [React Doctor](react-doctor.zh.md) | ✅ | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 |
| CodeRabbit / PR-Agent (Qodo) / Greptile | 未收录 | 各页对比里点到的其他 LLM 代码评审工具。 |

## 什么该放这里

主要职责是**LLM 辅助代码/安全评审**、产出行级问题的工具。不含通用 agent 框架，不含无 LLM 的传统 linter。
