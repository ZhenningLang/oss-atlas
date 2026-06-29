# agent-frameworks

> Category node. Build and run multi-step or multi-agent systems — agent frameworks and agent operating systems.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **DSPy** | You have eval data and a metric and want optimizers to compile prompts instead of hand-tuning them. | [→](dspy.md) |
| **AgentScope** | Shipping a production multi-agent LLM service needing sandboxed tools, permissions, tracing, and human-in-the-loop. | [→](agentscope.md) |
| **OpenFang** | You want autonomous agents that run on a schedule from one self-hosted Rust binary. | [→](openfang.md) |
| **Symphony** | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. | [→](symphony.md) |
| **Claude Octopus** | You live in Claude Code and want other AI models to cross-review tasks for blindspots before shipping. | [→](claude-octopus.md) |
| **oh-my-claudecode** | You live in Claude Code and need staged multi-agent teams with model routing and tmux parallelism. | [→](oh-my-claudecode.md) |
| **smolagents** | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. | [→](smolagents.md) |
| **Kilo Code** | Use it when you want an open, BYOK in-IDE (VS Code) coding agent with planning and modes — an end-user tool, not a library to build agents. | [→](kilocode.md) |
| **Parlant** | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. | [→](parlant.md) |
| **SkillOpt** | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. | [→](skillopt.md) |
| **Open Interpreter** | Use it when you want a Codex-fork terminal coding agent with swappable harnesses tuned for low-cost/open models (DeepSeek, Kimi, Qwen) — not the old Python REPL (that moved to a community fork), and it's a weeks-old 0.0.x rewrite that executes code. | [→](open-interpreter.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [DSPy](dspy.md) | ✅ | Optimizer layer compiles prompts/weights against a metric — unique here; needs eval data, not a workflow engine. |
| [AgentScope](agentscope.md) | ✅ | Production multi-agent runtime: sandboxed tools, permission gates, tracing, human-in-the-loop. |
| [OpenFang](openfang.md) | ✅ | Self-hosted Rust "agent OS" for scheduled, autonomous 24×7 runs. |
| [Symphony](symphony.md) | ✅ | Self-hosted orchestrator running isolated per-issue autonomous implementation runs (Linear + Codex). |
| [Claude Octopus](claude-octopus.md) | ✅ | Cross-model blindspot-review layer that lives inside Claude Code. |
| [oh-my-claudecode](oh-my-claudecode.md) | ✅ | Staged multi-agent teams with model routing + tmux parallelism for Claude Code. |
| [smolagents](smolagents.md) | ✅ | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. |
| [Kilo Code](kilocode.md) | ✅ | Use it when you want an open, BYOK in-IDE (VS Code) coding agent with planning and modes — an end-user tool, not a library to build agents. |
| [Parlant](parlant.md) | ✅ | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. |
| [SkillOpt](skillopt.md) | ✅ | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. |
| [Open Interpreter](open-interpreter.md) | ✅ | OpenAI Codex-fork terminal coding agent with runtime-swappable harnesses for low-cost/open models; weeks-old 0.0.x Rust rewrite that runs code in an OS sandbox — not the discontinued Python REPL. |
| LangChain / LlamaIndex / CrewAI / AutoGen | 未收录 | Broader build/run agent ecosystems named across the pages' comparisons. |

## What belongs here

Frameworks and runtimes whose primary job is to **build, orchestrate, or autonomously run** multi-step
or multi-agent systems. Not LLM fine-tuning (see `llm-training`), not standalone agent memory
(see `agent-memory`), not inference runtimes (see `on-device-ml`).
