# Project Intake Apply Summary — 2026-07-06

## Outcome

| Metric | Count |
|---|---:|
| Original high-value backlog items | 91 |
| Added as bilingual project pages | 90 |
| Blocked / not added | 1 |
| Added with explicit risk caveats | 11 |

## Blocked

| Candidate | Reason |
|---|---|
| LM Studio | missing_open_source_repo_url, likely_not_open_source_repo |

## Added With Explicit Caveats

| Candidate | Page | Reasons |
|---|---|---|
| Text Generation Inference (TGI) | `categories/llm-inference/text-generation-inference.md` | github_repo_archived |
| Sourcegraph | `categories/rag-retrieval/sourcegraph.md` | license_missing_or_noassertion, github_repo_archived |
| Astro | `categories/web-ui/astro.md` | license_missing_or_noassertion |
| Langfuse | `categories/llm-eval/langfuse.md` | license_missing_or_noassertion |
| MLX / mlx-lm | `categories/on-device-ml/mlx-mlx-lm.md` | split_mixed_candidate_review_needed |
| Flowise | `categories/agent-frameworks/workflow-builders/flowise.md` | license_missing_or_noassertion |
| OpenHands | `categories/agent-frameworks/coding-agents/openhands.md` | license_missing_or_noassertion |
| OpenReview | `categories/ai-code-review/openreview.md` | license_missing_or_noassertion |
| ImageMagick | `categories/media-processing/imagemagick.md` | license_missing_or_noassertion |
| jq | `categories/dev-utilities/data-tools/jq.md` | license_missing_or_noassertion |
| Metabase | `categories/data-visualization/metabase.md` | license_missing_or_noassertion |

## Fanout Follow-up

Final lint passes with 0 errors, but these category nodes exceed `MAX_FANOUT=12` and should be rebalanced with `refactor-index`:

- `categories/agent-frameworks/coding-agents`: 13 pages
- `categories/databases`: 13 pages
- `categories/media-processing`: 14 pages
- `categories/web-scraping`: 13 pages
- `categories/web-ui`: 19 pages

## Verification

- `python3 tools/lint.py`: 0 errors, 5 fanout warnings.
- `python3 tools/quality_scan.py --changed-only --fail-on-any-scoped`: 0 deterministic findings.
- `python3 tools/health_backfill.py --apply --yes --resume --sleep 1 --timeout 240 --retries 1`: completed remaining health blocks and SVG cards.

## Important Caveat

These are first-pass intake pages generated from verified GitHub metadata plus the backlog context. They pass structural gates, but semantic depth is intentionally marked in Caveats; future `sync-entry` passes should deepen individual pages before high-stakes recommendations.
