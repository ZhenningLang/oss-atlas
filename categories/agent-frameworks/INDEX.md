# agent-frameworks

> Category node. Build and run multi-step or multi-agent systems — agent frameworks and agent operating systems.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **DSPy** | You have eval data and a metric and want optimizers to compile prompts instead of hand-tuning them. | A (6/6) | [→](dspy.md) |
| **AgentScope** | Shipping a production multi-agent LLM service needing sandboxed tools, permissions, tracing, and human-in-the-loop. | B (6/6) | [→](agentscope.md) |
| **OpenFang** | You want autonomous agents that run on a schedule from one self-hosted Rust binary. | B (5/6) | [→](openfang.md) |
| **Symphony** | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. | B (5/6) | [→](symphony.md) |
| **Claude Octopus** | You live in Claude Code and want other AI models to cross-review tasks for blindspots before shipping. | C (6/6) | [→](claude-octopus.md) |
| **oh-my-claudecode** | You live in Claude Code and need staged multi-agent teams with model routing and tmux parallelism. | B (5/6) | [→](oh-my-claudecode.md) |
| **smolagents** | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. | B (6/6) | [→](smolagents.md) |
| **Kilo Code** | Use it when you want an open, BYOK in-IDE (VS Code) coding agent with planning and modes — an end-user tool, not a library to build agents. | B (6/6) | [→](kilocode.md) |
| **Parlant** | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. | B (6/6) | [→](parlant.md) |
| **SkillOpt** | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. | B (6/6) | [→](skillopt.md) |
| **Open Interpreter** | Use it when you want a Codex-fork terminal coding agent with swappable harnesses tuned for low-cost/open models (DeepSeek, Kimi, Qwen) — not the old Python REPL (that moved to a community fork), and it's a weeks-old 0.0.x rewrite that executes code. | A (6/6) | [→](open-interpreter.md) |
| **Codex** | Use it when you want a lightweight OpenAI-backed coding agent that runs in your terminal and can edit files, run tests, and commit changes — but it requires OpenAI API access and an internet connection. | ? (0/6) | [→](codex.md) |
| **OpenClaw** | Use it when you want a personal AI assistant that runs on your own devices and answers you across 20+ messaging channels — but it's extremely young with no Lindy track record. | ? (0/6) | [→](openclaw.md) |
| **CC Switch** | Use it when you juggle multiple AI coding agents (Claude Code, Codex, Gemini CLI, OpenClaw, OpenCode, Hermes Agent) and want a single desktop control plane with provider routing and MCP support. | ? (0/6) | [→](cc-switch.md) |
| **Hermes Agent** | Use it when you want a self-improving AI agent with a learning loop that creates skills from experience and runs on a $5 VPS — but it's under a year old and the learning-loop stability is unproven. | ? (0/6) | [→](hermes-agent.md) |
| **AutoGPT** | Use it when you need a platform to create, deploy, and manage continuous AI agents that automate complex workflows — but it has no declared license and requires significant resources to self-host. | ? (0/6) | [→](autogpt.md) |
| **OpenCode** | Use it when you want an open-source terminal coding agent you can self-host, audit, and extend — but it's extremely young (created 2025-04) with no Lindy track record. | ? (0/6) | [→](opencode.md) |
| **Langflow** | Use it when you want a visual drag-and-drop platform to build and deploy LLM workflows and agents with built-in API and MCP servers — but visual flows are harder to diff/review than code. | ? (0/6) | [→](langflow.md) |
| **Dify** | Use it when you want a production-ready visual platform for building agentic workflows with low-code, RAG, and MCP support — but verify the license before commercial use. | ? (0/6) | [→](dify.md) |
| **LangChain** | Use it when you need a code-first framework to compose LLM agents, tools, and memory with a vast integration ecosystem — but avoid for simple single-prompt apps. | ? (0/6) | [→](langchain.md) |
| **RTK** | Use it when you use CLI-based AI coding agents and want to reduce LLM token consumption by 60–90% on common shell commands — but it's only ~6 months old and the star count is suspiciously high. | ? (0/6) | [→](rtk.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [DSPy](dspy.md) | ✅ | A (6/6) | Optimizer layer compiles prompts/weights against a metric — unique here; needs eval data, not a workflow engine. |
| [AgentScope](agentscope.md) | ✅ | B (6/6) | Production multi-agent runtime: sandboxed tools, permission gates, tracing, human-in-the-loop. |
| [OpenFang](openfang.md) | ✅ | B (5/6) | Self-hosted Rust "agent OS" for scheduled, autonomous 24×7 runs. |
| [Symphony](symphony.md) | ✅ | B (5/6) | Self-hosted orchestrator running isolated per-issue autonomous implementation runs (Linear + Codex). |
| [Claude Octopus](claude-octopus.md) | ✅ | C (6/6) | Cross-model blindspot-review layer that lives inside Claude Code. |
| [oh-my-claudecode](oh-my-claudecode.md) | ✅ | B (5/6) | Staged multi-agent teams with model routing + tmux parallelism for Claude Code. |
| [smolagents](smolagents.md) | ✅ | B (6/6) | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. |
| [Kilo Code](kilocode.md) | ✅ | B (6/6) | Use it when you want an open, BYOK in-IDE (VS Code) coding agent with planning and modes — an end-user tool, not a library to build agents. |
| [Parlant](parlant.md) | ✅ | B (6/6) | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. |
| [SkillOpt](skillopt.md) | ✅ | B (6/6) | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. |
| [Open Interpreter](open-interpreter.md) | ✅ | A (6/6) | OpenAI Codex-fork terminal coding agent with runtime-swappable harnesses for low-cost/open models; weeks-old 0.0.x Rust rewrite that runs code in an OS sandbox — not the discontinued Python REPL. |
| [Codex](codex.md) | ✅ | ? (0/6) | Lightweight OpenAI terminal coding agent with sandboxed code execution; OpenAI-only, very young (2025-04), and requires API credits. |
| [OpenClaw](openclaw.md) | ✅ | ? (0/6) | Personal AI assistant running on your own devices across 20+ messaging channels; extremely young (created 2025-11) with no Lindy track record. |
| [CC Switch](cc-switch.md) | ✅ | ? (0/6) | Cross-platform desktop manager for multiple AI coding agents with provider routing and MCP support; under a year old, single maintainer, bus factor of 1. |
| [Hermes Agent](hermes-agent.md) | ✅ | ? (0/6) | Self-improving AI agent with a learning loop from Nous Research; creates skills from experience, but under a year old and learning-loop stability is unproven. |
| [AutoGPT](autogpt.md) | ✅ | ? (0/6) | Platform to create, deploy, and manage continuous AI agents; no declared license, resource-heavy, and cloud beta is not yet public. |
| [Dify](dify.md) | ✅ | ? (0/6) | Production-ready visual platform for agentic workflows with low-code, RAG, and MCP; verify license before commercial use. |
| [LangChain](langchain.md) | ✅ | ? (0/6) | Code-first framework for composing LLM agents, tools, and memory with vast integrations; avoid for simple single-prompt apps. |
| [RTK](rtk.md) | ✅ | ? (0/6) | CLI proxy that compresses shell output before it reaches AI agents, reducing token costs by 60–90%; extremely young (6 months) with suspiciously high star count. |
| [OpenCode](opencode.md) | ✅ | ? (0/6) | Open-source terminal coding agent you can self-host, audit, and extend; extremely young (created 2025-04) with no Lindy track record. |
| [Langflow](langflow.md) | ✅ | ? (0/6) | Visual drag-and-drop platform for building and deploying LLM workflows and agents with built-in API and MCP servers; visual flows are harder to diff/review than code. |
| [Gemini CLI](gemini-cli.md) | ✅ | ? (0/6) | Open-source terminal AI agent powered by Google's Gemini models with free tier, built-in tools, and MCP support; very young (created 2025-04) and Google-only. |

## What belongs here

Frameworks and runtimes whose primary job is to **build, orchestrate, or autonomously run** multi-step
or multi-agent systems. Not LLM fine-tuning (see `llm-training`), not standalone agent memory
(see `agent-memory`), not inference runtimes (see `on-device-ml`).
