---
name: DSPy
slug: dspy
repo: https://github.com/stanfordnlp/dspy
category: agent-frameworks
tags: [llm-programming, prompt-optimization, modules, signatures, rag, agents]
language: Python
license: MIT
maturity: v3.2.1, active (2026-06)
last_verified: 2026-06-26
type: framework
---

# DSPy

A framework for *programming* (not prompting) language models: you declare typed input→output `Signature`s, compose `Module`s, and let optimizers compile the actual prompts (and optionally weights) for you against a metric.

## When to use

You're an applied ML or platform engineer building an LLM pipeline — say a RAG system or a multi-step classification/extraction flow — and you're tired of hand-tuning megaprompts that silently break every time you swap the model or the data drifts. You've got a few dozen labeled examples and a metric you actually care about (exact-match, F1, an LLM judge), but no good way to systematically turn "this prompt feels better" into "this prompt measurably scores higher." DSPy resolves this by letting you write the *logic* declaratively: you define a `Signature` like `question -> answer`, wrap it in a `Module` (`Predict`, `ChainOfThought`, `ReAct`), and then hand the whole program plus your metric to an optimizer. The optimizer (BootstrapFewShot, MIPROv2, GEPA, BootstrapFinetune) searches over demonstrations, instructions, or finetuned weights to maximize your metric — so the prompt becomes a compiled artifact instead of a hand-edited string.

It's also a good fit when you expect to swap models often. Because DSPy routes calls through LiteLLM, the same program runs across OpenAI, Anthropic, local vLLM/Ollama, and others, and you can re-compile when you change backends rather than rewriting prompts per provider. If your value is in *structure that survives model churn* — and you have data and a metric to optimize against — that's DSPy's sweet spot.

## When NOT to use

- **You have no metric and no eval data.** DSPy's whole payoff is optimization against a measurable objective. With zero labeled examples and no scoring function, the optimizers have nothing to climb, and you're left with a heavier, more abstract way to write a single prompt — use a thin SDK or a template library instead.
- **You want a visual/low-code agent builder or a big tool/integration catalog.** DSPy is a Python programming model, not a drag-and-drop canvas or an integrations marketplace. For document loaders, vector-store connectors, and prebuilt chains, LangChain / LlamaIndex cover more surface out of the box.
- **You need a thin, fully-transparent prompt you can read and ship verbatim.** DSPy *generates* the final prompt; what the model sees is an artifact of compilation, not a string you wrote. Teams that need every token auditable and version-controlled by hand may find the indirection unwelcome.
- **Hard latency/cost budgets during development.** Optimizers (especially MIPROv2/GEPA) issue many LM calls to search the space; a compile run can be slow and token-expensive [未验证]. Production inference is cheap, but the optimize loop is not free.
- **You want long-term API stability.** DSPy has moved fast and renamed core surfaces across versions (teleprompters → optimizers, `dspy.Predict` ergonomics, signature syntax) [推断]; pin a version and expect migration work on upgrades.
- **Pure orchestration of deterministic multi-agent workflows** (queues, schedulers, durable state) — DSPy optimizes LM programs; it is not a workflow engine.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [AgentScope](agentscope.md) | ✅ | Multi-agent runtime/messaging platform; focuses on agent orchestration & coordination, not compiling/optimizing single LM programs against a metric. |
| [Symphony](symphony.md) | ✅ | Agent framework with a different orchestration model; DSPy's distinctive feature is the optimizer layer, which most agent frameworks don't have. |
| LangChain | not indexed | Far broader integration/chain/agent catalog and ecosystem; prompts stay hand-authored. DSPy trades breadth for systematic prompt/weight optimization. |
| LlamaIndex | not indexed | RAG/data-framework heavyweight with rich connectors and indices; DSPy is lighter on data plumbing but optimizes the reasoning program itself. |
| TextGrad | not indexed | Also optimizes LM pipelines, via "textual gradients" / backprop-through-text; narrower module model than DSPy's signatures+optimizers. |
| AdalFlow (LightRAG) | not indexed | "PyTorch-like" library for building & auto-optimizing LM apps; closest in philosophy (optimize, don't hand-prompt), smaller ecosystem. |

## Tech stack

- **Language:** Python (`>=3.10, <3.15` per pyproject).
- **Core abstractions:** `Signature` (typed I/O spec), `Module` (`Predict`, `ChainOfThought`, `ReAct`, `ProgramOfThought`, etc.), and optimizers / "teleprompters" (`BootstrapFewShot`, `MIPROv2`, `GEPA`, `BootstrapFinetune`, `COPRO`, `SIMBA`) [推断 — exact set varies by release].
- **LM gateway:** LiteLLM, giving provider-agnostic access (OpenAI, Anthropic, local vLLM/Ollama, etc.).
- **Validation/serialization:** Pydantic v2, orjson, json-repair (for coercing model output into typed fields).
- **Caching/robustness:** diskcache + cachetools (LM response caching), tenacity (retries), cloudpickle (program serialization).
- **Optimization helper:** `gepa` package (pinned dependency) for the GEPA optimizer.

## Dependencies

- **Runtime:** Python ≥ 3.10 and < 3.15. No GPU required for the framework itself (you call hosted or local LMs); finetune-based optimizers need whatever the target finetuning backend requires.
- **Required Python deps (v3.2.1, per pyproject):** `litellm` ≥ 1.64.0, `openai` ≥ 0.28.1, `pydantic` ≥ 2.0, `regex`, `orjson`, `tqdm`, `requests` ≥ 2.31, `diskcache` ≥ 5.6, `json-repair`, `tenacity`, `anyio`, `cachetools` ≥ 5.5, `cloudpickle` ≥ 3.1.2, `gepa[dspy]` ==0.1.1.
- **External services:** at least one LM provider/endpoint (API key for a hosted model, or a local server like Ollama/vLLM). Optional: a vector store/retriever for RAG, and tracking/observability backends.
- **Install:** `pip install dspy` (formerly `dspy-ai`).

## Ops difficulty

**Low-to-medium.** As a library it's `pip install` and run — no servers, no datastore, no cluster to operate; the framework just makes LM calls through LiteLLM. The medium-tier friction is conceptual and economic rather than infrastructural: you must build an eval set and metric to get value, optimizer runs can be slow and token-costly so you'll want LM caching and budget controls, and the fast-moving API means upgrades can require migration. Production *serving* of a compiled DSPy program is light (it's just code + saved prompts/state); the cost and care concentrate in the compile/optimize loop and in keeping pinned versions stable.

## Caveats (unverified)

- [未验证] Star count ~35.4k as of 2026-06 (from `gh repo view`) — GitHub stars in this ecosystem are unreliable and date-sensitive; indicative only.
- [未验证] Latest release 3.2.1 dated 2026-05-05 (per GitHub release metadata); a newer version may exist by the time you read this.
- [未验证] Optimizer compile runs being slow / token-expensive is a general characteristic of search-based prompt optimization; exact cost depends entirely on optimizer choice, program size, model, and dataset — no first-party number is asserted here.
- [推断] The exact set of available optimizers/modules (and their names) shifts release-to-release; the lists above reflect commonly documented components — verify against the installed version before relying on a specific one.
- [推断] API churn / renames across major versions (teleprompter→optimizer terminology, signature ergonomics) is inferred from DSPy's release history and community reports, not confirmed against a specific changelog here; treat upgrade-migration cost as a risk to check.
- [未验证] LiteLLM enabling specific providers (Anthropic, vLLM, Ollama) is per DSPy/LiteLLM documentation; confirm the exact provider/model is supported for your version before depending on it.
