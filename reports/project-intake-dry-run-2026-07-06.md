# Project Intake Dry Run — 2026-07-06

This dry-run validates the 91 high-value backlog items before writing canonical selection pages.

## Summary

| Metric | Count |
|---|---:|
| Backlog items | 91 |
| GitHub repo verified | 90 |
| Blocked | 1 |
| Archived repos | 2 |
| License missing / NOASSERTION from GitHub API | 9 |
| Split / mixed candidates | 1 |

## Blocked Or Risky Items

| ID | Candidate | Repo | Status | Reasons |
|---:|---|---|---|---|
| 1 | Text Generation Inference (TGI) | https://github.com/huggingface/text-generation-inference | verified | github_repo_archived |
| 21 | Sourcegraph | https://github.com/sourcegraph/sourcegraph-public-snapshot | verified | license_missing_or_noassertion, github_repo_archived |
| 31 | Astro | https://github.com/withastro/astro | verified | license_missing_or_noassertion |
| 41 | Langfuse | https://github.com/langfuse/langfuse | verified | license_missing_or_noassertion |
| 50 | LM Studio | — | blocked | missing_open_source_repo_url, likely_not_open_source_repo |
| 51 | MLX / mlx-lm | https://github.com/ml-explore/mlx-lm | verified | split_mixed_candidate_review_needed |
| 55 | Flowise | https://github.com/FlowiseAI/Flowise | verified | license_missing_or_noassertion |
| 58 | OpenHands | https://github.com/OpenHands/OpenHands | verified | license_missing_or_noassertion |
| 66 | OpenReview | https://github.com/vercel-labs/openreview | verified | license_missing_or_noassertion |
| 71 | ImageMagick | https://github.com/ImageMagick/ImageMagick | verified | license_missing_or_noassertion |
| 78 | jq | https://github.com/jqlang/jq | verified | license_missing_or_noassertion |
| 87 | Metabase | https://github.com/metabase/metabase | verified | license_missing_or_noassertion |

## Verified Queue

| ID | P | Candidate | Repo | Category | Type | Stars | License | Archived |
|---:|---|---|---|---|---|---:|---|---|
| 1 | P0 | Text Generation Inference (TGI) | https://github.com/huggingface/text-generation-inference | `categories/llm-inference` | service | 10867 | Apache-2.0 | True |
| 2 | P0 | CrewAI | https://github.com/crewAIInc/crewAI | `categories/agent-frameworks/agent-runtimes` | framework | 55016 | MIT | False |
| 3 | P0 | SvelteKit | https://github.com/sveltejs/kit | `categories/web-ui` | framework | 20647 | MIT | False |
| 4 | P0 | trafilatura | https://github.com/adbar/trafilatura | `categories/web-scraping` | library | 6239 | Apache-2.0 | False |
| 5 | P0 | gallery-dl | https://github.com/mikf/gallery-dl | `categories/media-download` | tool | 18759 | GPL-2.0 | False |
| 6 | P0 | Hugging Face TRL | https://github.com/huggingface/trl | `categories/llm-training` | library | 18778 | Apache-2.0 | False |
| 7 | P0 | LangGraph | https://github.com/langchain-ai/langgraph | `categories/agent-frameworks/agent-runtimes` | framework | 36628 | MIT | False |
| 8 | P0 | Pandoc | https://github.com/jgm/pandoc | `categories/markdown-tools` | tool | 45244 | GPL-2.0 | False |
| 9 | P0 | Argo Workflows | https://github.com/argoproj/argo-workflows | `categories/workflow-orchestration` | service | 16809 | Apache-2.0 | False |
| 10 | P0 | browser-use | https://github.com/browser-use/browser-use | `categories/web-automation` | framework | 103084 | MIT | False |
| 11 | P0 | Goldmark | https://github.com/yuin/goldmark | `categories/markdown-tools` | library | 4880 | MIT | False |
| 12 | P0 | GPT Researcher | https://github.com/assafelovic/gpt-researcher | `categories/deep-research` | app | 28109 | Apache-2.0 | False |
| 13 | P0 | Letta (MemGPT) | https://github.com/letta-ai/letta | `categories/agent-memory` | service | 23666 | Apache-2.0 | False |
| 14 | P0 | LibreChat | https://github.com/danny-avila/LibreChat | `categories/llm-chat-ui` | app | 40350 | MIT | False |
| 15 | P0 | LlamaIndex | https://github.com/run-llama/llama_index | `categories/agent-frameworks/workflow-builders` | framework | 50684 | MIT | False |
| 16 | P0 | Marker | https://github.com/datalab-to/marker | `categories/document-parsing` | tool | 37199 | GPL-3.0 | False |
| 17 | P0 | mitmproxy | https://github.com/mitmproxy/mitmproxy | `categories/debugging-proxy` | tool | 44183 | MIT | False |
| 18 | P0 | Playwright | https://github.com/microsoft/playwright | `categories/web-automation` | library | 92304 | Apache-2.0 | False |
| 19 | P0 | Reactour | https://github.com/elrumordelaluz/reactour | `categories/web-ui` | library | 4088 | MIT | False |
| 20 | P0 | react-joyride | https://github.com/gilbarbara/react-joyride | `categories/web-ui` | library | 7793 | MIT | False |
| 21 | P0 | Sourcegraph | https://github.com/sourcegraph/sourcegraph-public-snapshot | `categories/rag-retrieval` | app | 10291 | NOASSERTION | True |
| 22 | P0 | SCIP | https://github.com/scip-code/scip | `categories/rag-retrieval` | tool | 678 | Apache-2.0 | False |
| 23 | P0 | torchtune | https://github.com/meta-pytorch/torchtune | `categories/llm-training` | library | 5783 | BSD-3-Clause | False |
| 24 | P1 | Prefect | https://github.com/PrefectHQ/prefect | `categories/workflow-orchestration` | framework | 22774 | Apache-2.0 | False |
| 25 | P1 | Dagster | https://github.com/dagster-io/dagster | `categories/workflow-orchestration` | framework | 15793 | Apache-2.0 | False |
| 26 | P1 | Temporal | https://github.com/temporalio/temporal | `categories/workflow-orchestration` | service | 21447 | MIT | False |
| 27 | P1 | Material UI (MUI) | https://github.com/mui/material-ui | `categories/web-ui` | library | 98542 | MIT | False |
| 28 | P1 | Chakra UI | https://github.com/chakra-ui/chakra-ui | `categories/web-ui` | library | 40487 | MIT | False |
| 29 | P1 | Radix UI Primitives | https://github.com/radix-ui/primitives | `categories/web-ui` | library | 19028 | MIT | False |
| 30 | P1 | Nuxt | https://github.com/nuxt/nuxt | `categories/web-ui` | framework | 60557 | MIT | False |
| 31 | P1 | Astro | https://github.com/withastro/astro | `categories/web-ui` | framework | 60748 | NOASSERTION | False |
| 32 | P1 | Puppeteer | https://github.com/puppeteer/puppeteer | `categories/web-automation` | library | 95284 | Apache-2.0 | False |
| 33 | P1 | PyMuPDF | https://github.com/pymupdf/PyMuPDF | `categories/pdf-tools` | library | 10155 | AGPL-3.0 | False |
| 34 | P1 | pdfplumber | https://github.com/jsvine/pdfplumber | `categories/pdf-tools` | library | 10511 | MIT | False |
| 35 | P1 | unstructured | https://github.com/Unstructured-IO/unstructured | `categories/document-parsing` | library | 15078 | Apache-2.0 | False |
| 36 | P1 | OCRmyPDF | https://github.com/ocrmypdf/OCRmyPDF | `categories/pdf-tools` | tool | 34093 | MPL-2.0 | False |
| 37 | P1 | Milvus | https://github.com/milvus-io/milvus | `categories/rag-retrieval` | service | 45094 | Apache-2.0 | False |
| 38 | P1 | Zep | https://github.com/getzep/zep | `categories/agent-memory` | service | 4732 | Apache-2.0 | False |
| 39 | P1 | Graphiti | https://github.com/getzep/graphiti | `categories/agent-memory` | library | 28417 | Apache-2.0 | False |
| 40 | P1 | LangMem | https://github.com/langchain-ai/langmem | `categories/agent-memory` | library | 1541 | MIT | False |
| 41 | P1 | Langfuse | https://github.com/langfuse/langfuse | `categories/llm-eval` | app | 30539 | NOASSERTION | False |
| 42 | P1 | DeepEval | https://github.com/confident-ai/deepeval | `categories/llm-eval` | library | 16674 | Apache-2.0 | False |
| 43 | P1 | Ragas | https://github.com/vibrantlabsai/ragas | `categories/llm-eval` | library | 14686 | Apache-2.0 | False |
| 44 | P1 | garak | https://github.com/NVIDIA/garak | `categories/llm-eval` | tool | 8342 | Apache-2.0 | False |
| 45 | P1 | Giskard OSS | https://github.com/Giskard-AI/giskard-oss | `categories/llm-eval` | library | 5494 | Apache-2.0 | False |
| 46 | P1 | Axolotl | https://github.com/axolotl-ai-cloud/axolotl | `categories/llm-training` | tool | 12159 | Apache-2.0 | False |
| 47 | P1 | verl | https://github.com/verl-project/verl | `categories/llm-training` | framework | 22321 | Apache-2.0 | False |
| 48 | P1 | llama.cpp | https://github.com/ggml-org/llama.cpp | `categories/llm-inference` | library | 119451 | MIT | False |
| 49 | P1 | Ollama | https://github.com/ollama/ollama | `categories/llm-inference` | app | 175595 | MIT | False |
| 50 | P1 | LM Studio | — | `categories/llm-inference` | app |  | NOASSERTION |  |
| 51 | P1 | MLX / mlx-lm | https://github.com/ml-explore/mlx-lm | `categories/on-device-ml` | library | 6204 | MIT | False |
| 52 | P1 | AutoGen | https://github.com/microsoft/autogen | `categories/agent-frameworks/agent-runtimes` | framework | 59526 | CC-BY-4.0 | False |
| 53 | P1 | Pydantic AI | https://github.com/pydantic/pydantic-ai | `categories/agent-frameworks/agent-runtimes` | framework | 18243 | MIT | False |
| 54 | P1 | OpenAI Agents SDK | https://github.com/openai/openai-agents-python | `categories/agent-frameworks/agent-runtimes` | library | 27693 | MIT | False |
| 55 | P1 | Flowise | https://github.com/FlowiseAI/Flowise | `categories/agent-frameworks/workflow-builders` | app | 54327 | NOASSERTION | False |
| 56 | P1 | aider | https://github.com/Aider-AI/aider | `categories/agent-frameworks/coding-agents` | tool | 47110 | Apache-2.0 | False |
| 57 | P1 | Cline | https://github.com/cline/cline | `categories/agent-frameworks/coding-agents` | tool | 64347 | Apache-2.0 | False |
| 58 | P1 | OpenHands | https://github.com/OpenHands/OpenHands | `categories/agent-frameworks/coding-agents` | app | 79621 | NOASSERTION | False |
| 59 | P1 | SWE-agent | https://github.com/SWE-agent/SWE-agent | `categories/agent-frameworks/coding-agents` | tool | 19709 | MIT | False |
| 60 | P1 | Cognee | https://github.com/topoteretes/cognee | `categories/agent-memory` | service | 27221 | Apache-2.0 | False |
| 61 | P1 | Open Deep Research | https://github.com/langchain-ai/open_deep_research | `categories/deep-research` | app | 11944 | MIT | False |
| 62 | P1 | STORM | https://github.com/stanford-oval/storm | `categories/deep-research` | app | 29864 | MIT | False |
| 63 | P1 | node-DeepResearch | https://github.com/jina-ai/node-DeepResearch | `categories/deep-research` | tool | 5193 | Apache-2.0 | False |
| 64 | P1 | PR-Agent | https://github.com/The-PR-Agent/pr-agent | `categories/ai-code-review` | app | 11995 | Apache-2.0 | False |
| 65 | P1 | Metis | https://github.com/arm/metis | `categories/ai-code-review` | tool | 768 | Apache-2.0 | False |
| 66 | P1 | OpenReview | https://github.com/vercel-labs/openreview | `categories/ai-code-review` | app | 1450 | NOASSERTION | False |
| 67 | P1 | BentoML | https://github.com/bentoml/BentoML | `categories/llm-inference` | service | 8708 | Apache-2.0 | False |
| 68 | P1 | LMDeploy | https://github.com/InternLM/lmdeploy | `categories/llm-inference` | tool | 7943 | Apache-2.0 | False |
| 69 | P1 | qpdf | https://github.com/qpdf/qpdf | `categories/pdf-tools` | tool | 5204 | Apache-2.0 | False |
| 70 | P1 | markdownlint | https://github.com/DavidAnson/markdownlint | `categories/markdown-tools` | library | 6175 | MIT | False |
| 71 | P1 | ImageMagick | https://github.com/ImageMagick/ImageMagick | `categories/media-processing` | tool | 16892 | NOASSERTION | False |
| 72 | P1 | sharp | https://github.com/lovell/sharp | `categories/media-processing` | library | 32428 | Apache-2.0 | False |
| 73 | P1 | DuckDB | https://github.com/duckdb/duckdb | `categories/databases` | service | 39203 | MIT | False |
| 74 | P1 | ClickHouse | https://github.com/ClickHouse/ClickHouse | `categories/databases` | service | 48478 | Apache-2.0 | False |
| 75 | P1 | DBeaver | https://github.com/dbeaver/dbeaver | `categories/databases` | app | 50882 | Apache-2.0 | False |
| 76 | P1 | Debezium | https://github.com/debezium/debezium | `categories/databases` | service | 12876 | Apache-2.0 | False |
| 77 | P1 | Valkey | https://github.com/valkey-io/valkey | `categories/databases` | service | 26448 | BSD-3-Clause | False |
| 78 | P1 | jq | https://github.com/jqlang/jq | `categories/dev-utilities/data-tools` | tool | 35118 | NOASSERTION | False |
| 79 | P1 | fzf | https://github.com/junegunn/fzf | `categories/dev-utilities/data-tools` | tool | 81518 | MIT | False |
| 80 | P1 | Keycloak | https://github.com/keycloak/keycloak | `categories/auth` | service | 35514 | Apache-2.0 | False |
| 81 | P1 | Casbin | https://github.com/apache/casbin | `categories/auth` | library | 20226 | Apache-2.0 | False |
| 82 | P1 | OpenFGA | https://github.com/openfga/openfga | `categories/auth` | service | 5382 | Apache-2.0 | False |
| 83 | P1 | Prometheus | https://github.com/prometheus/prometheus | `categories/observability` | service | 64970 | Apache-2.0 | False |
| 84 | P1 | OpenTelemetry Collector | https://github.com/open-telemetry/opentelemetry-collector | `categories/observability` | service | 7211 | Apache-2.0 | False |
| 85 | P1 | Loki | https://github.com/grafana/loki | `categories/observability` | service | 28505 | AGPL-3.0 | False |
| 86 | P1 | Jaeger | https://github.com/jaegertracing/jaeger | `categories/observability` | service | 22972 | Apache-2.0 | False |
| 87 | P1 | Metabase | https://github.com/metabase/metabase | `categories/data-visualization` | app | 48067 | NOASSERTION | False |
| 88 | P1 | Evidence | https://github.com/evidence-dev/evidence | `categories/data-visualization` | framework | 6533 | MIT | False |
| 89 | P1 | Rich | https://github.com/Textualize/rich | `categories/terminal-ui` | library | 56788 | MIT | False |
| 90 | P1 | Textual | https://github.com/Textualize/textual | `categories/terminal-ui` | framework | 36491 | MIT | False |
| 91 | P1 | FreshRSS | https://github.com/FreshRSS/FreshRSS | `categories/reading-tools` | app | 15476 | AGPL-3.0 | False |

## Apply Decision

- `LM Studio` is blocked because no open-source repository URL was verified.
- Archived repos may still be added if the page leads with archival/maintenance risk instead of recommending them for new production use.
- `NOASSERTION` license rows can be added only with explicit Caveats and `license: NOASSERTION`; a later sync should replace it if a repository-level license is confirmed.
- `MLX / mlx-lm` is treated as `mlx-lm` for this queue; a separate MLX framework page can be added later if desired.
