---
name: project-harvester
version: 1.0.0
category: oss-atlas-maintainer
metadata:
  internal: true
  description: >
    Manually-triggered batch harvester for GitHub repositories. One trigger = one wave.
    Collects a batch of GitHub repos via search API, deduplicates against existing index,
    filters for quality signals, infers categories, and (optionally) creates full bilingual
    project pages for selected candidates. Designed to be run via a manual cron job.
---

# Project Harvester — Batch Discovery Skill

> One trigger = one wave. Collect → dedupe → filter → infer category → report → create.

## Purpose

When the oss-atlas index needs new entries, this skill automates the heavy lifting of
finding GitHub repos that are **not already indexed**, filtering out noise, and surfacing
candidates with enough metadata to decide whether to add them.

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth status` passes), OR a `GITHUB_TOKEN` env var.
- Python 3.9+ with standard library only (no pip deps needed for the harvester core).
- The oss-atlas repo checked out locally at `{workspace}`.

## Trigger Modes

| Mode | What it does | When to use |
|------|-------------|-------------|
| **Search mode** (default) | GitHub Search API with configurable query | You have a domain/keyword in mind |
| **Trending mode** | GitHub Trending (daily/weekly) for a language | You want to see what's organically hot |
| **Backfill mode** | Read a list of repos from a file, batch-score | You have a curated candidate list from another source (e.g., Awesome list, Reddit thread) |

## Wave Workflow (Search Mode — default)

### Step 1: Configure the wave

Decide the search parameters. Default for a "general quality" wave:

```yaml
query_template: "language:{lang} stars:>1000 pushed:>2026-01-01 sort:stars"
per_page: 20           # GitHub API max = 100
lang_rotation:         # Rotate through languages to get diversity
  - python
  - rust
  - typescript
  - go
  - ""
min_stars: 100
exclude_forks: true
exclude_archived: true
```

### Step 2: Collect raw candidates

Run the harvester core script:

```bash
cd {workspace}
python3 tools/harvest.py search \
  --query "language:python stars:>1000 pushed:>2026-01-01 sort:stars" \
  --per-page 20 \
  --output /tmp/harvest-wave-N.json
```

The script calls GitHub Search API (REST), returns a JSON array of repo stubs:

```json
[
  {
    "repo": "calesthio/OpenMontage",
    "html_url": "https://github.com/calesthio/OpenMontage",
    "stars": 28813,
    "forks": 3218,
    "language": "Python",
    "license": "AGPL-3.0",
    "description": "World's first open-source, agentic video production system...",
    "pushed_at": "2026-06-29T21:55:03Z",
    "created_at": "2026-03-29T15:23:22Z",
    "topics": ["ai-video", "video-production", "remotion"]
  }
]
```

### Step 3: Deduplicate against existing index

The harvester reads **all** existing `.md` files under `categories/`, extracts `repo:` from YAML frontmatter, and builds a dedup set. It then filters the candidate list:

```bash
python3 tools/harvest.py dedupe \
  --input /tmp/harvest-wave-N.json \
  --index-root categories/ \
  --output /tmp/harvest-wave-N-new.json
```

Output: only repos not already in the index.

### Step 4: Quality filter & tier-zero scoring

Apply a lightweight gate (no health.py yet — that comes later when creating the page):

```bash
python3 tools/harvest.py filter \
  --input /tmp/harvest-wave-N-new.json \
  --min-stars 100 \
  --require-license \
  --exclude-archived \
  --output /tmp/harvest-wave-N-filtered.json
```

Quality signals checked at this stage (cheap, no extra API calls):
- `stars >= min_stars`
- `license != null` (GitHub detects one)
- `archived == false`
- `fork == false` (optional)
- `description` is non-empty

### Step 5: Agent semantic classification (no keyword matching)

**This is the key step where a coding agent (LLM) performs classification, not an algorithm.**

The harvester generates a `classify-task.md` report containing:
- All candidate repos with their descriptions and topics
- All existing category definitions ("What belongs here")
- 1-3 example projects from each category

The agent reads the report, compares each repo to the category definitions by **semantic meaning**, and assigns the best fit. The agent can also read the full `categories/{cat}/INDEX.md` for deeper context.

```bash
python3 tools/harvest.py classify \
  --input /tmp/harvest-wave-N-filtered.json \
  --category-index categories/ \
  --output /tmp/harvest-wave-N-classify-task.md
```

The agent then reviews the task and applies classifications to the JSON file by setting `suggested_category` on each candidate. Possible answers:
- An existing category name (e.g., `agent-tooling`, `web-ui`, `dev-utilities`)
- `needs-new-category` — if no existing category fits
- `uncertain` — if the repo is too vague or niche to classify confidently

**Why agent-driven?** Keyword matching is unreliable — a project like "rust-lang/rust" (compiler) has no meaningful keywords in its description, and "tauri" (desktop framework with web frontend) could be miscategorized by any keyword heuristic. The agent understands *what the project actually does*.

### Step 6: Generate final report

After the agent has assigned categories, produce the final candidate report:

```bash
python3 tools/harvest.py finalize \
  --input /tmp/harvest-wave-N-classified.json \
  --output /tmp/harvest-wave-N-report.md
```

The report contains a table like:

| Repo | Stars | Lang | License | Suggested Category | Why |
|------|-------|------|---------|-------------------|-----|
| calesthio/OpenMontage | 28.8K | Python | AGPL-3.0 | video-production | AI video production, 12 pipelines, matches new category |
| ... | ... | ... | ... | ... | ... |

### Step 7: Human review (gate)

**STOP. The agent presents the report to the user.**

The user decides:
- **"Add all"** → proceed to Step 8 for all candidates
- **"Add #1, #3, #5"** → proceed for selected
- **"Skip this wave"** → discard, end
- **"Create a new category for #2"** → create category first, then proceed

### Step 8: Create full project pages (for selected candidates)

For each selected repo, spawn a **sub-agent** (or sequential in-conversation) to execute the `add-project` workflow:

```bash
# For each selected repo:
python3 tools/harvest.py create-page \
  --repo owner/repo \
  --category inferred-category \
  --index-root categories/ \
  --workspace {workspace}
```

This internal step:
1. Runs `tools/health.py --repo owner/repo --type inferred-type` to generate the health block
2. Runs `tools/health_card.py` to generate the SVG
3. Fetches the repo README via GitHub API for content reference
4. Uses LLM to write the bilingual body (When to use / When NOT / Comparison / Tech stack / Dependencies / Ops difficulty / Health & viability / Caveats)
5. Writes `categories/{cat}/{slug}.md` and `categories/{cat}/{slug}.zh.md`
6. Updates `categories/{cat}/INDEX.md` and `categories/{cat}/INDEX.zh.md`
7. Updates root `INDEX.md` and `INDEX.zh.md`
8. Updates `README.md` and `README.zh.md`

**Important:** The agent-generated body sections are **drafts**. The sub-agent must label unverified claims with `[未验证]` / `[推断]` and populate the `Caveats` ledger. Human review of the drafted pages is encouraged before final commit.

### Step 9: Verify

```bash
cd {workspace}
python3 tools/lint.py
```

Fix any errors (missing INDEX entries, missing README rows, broken links, ASCII punctuation in `.zh.md` bodies, etc.).

### Step 10: Commit

```bash
git add -A
git commit -m "harvest: wave N — add K projects from {search_query}"
```

---

## Wave Size & Rate Limit Budget

| Resource | Budget per wave | Notes |
|----------|----------------|-------|
| GitHub Search API | 1 call per 100 results | Unauth: 10/min; Auth: 30/min |
| GitHub REST API (repo detail) | 1 call per candidate | Auth: 5000/hr |
| `health.py` | ~7-8 calls per repo | Auth: 5000/hr |
| `health_card.py` | 0 calls (offline) | SVG generation is local |
| LLM calls for page drafting | 1 per repo | Depends on provider |

**Recommended wave size: 10-15 repos.** This fits comfortably in a single hour's GitHub API budget and a 30-minute cron conversation timeout. Larger waves should be split into multiple manual triggers.

---

## One-Command Shortcut (Power User)

For experienced maintainers who trust the defaults:

```bash
cd {workspace}
python3 tools/harvest.py wave \
  --query "language:python stars:>1000 pushed:>2026-01-01 sort:stars" \
  --per-page 15 \
  --auto-create \
  --git-commit
```

This runs Steps 1–10 in sequence, with `--auto-create` bypassing the human review gate (use with caution; `--git-commit` requires `git` configured).

---

## Caveats & Limits

- **Classification is heuristic.** The keyword-based category inference can misplace repos (e.g., a "Python CLI tool for video processing" might be mapped to `media-processing` or `python-tooling`). Always review the suggested category.
- **Health scoring is as good as the data.** `health.py` needs `gh` auth. If rate-limited, some axes will be `?` — the page is still valid, but re-run `sync-entry` later to fill gaps.
- **Page drafting is AI-generated.** The `When to use` / `When NOT` / `Comparison` sections are synthesized from the README and a web search. They may contain unverified claims. Always review the `Caveats` ledger before committing.
- **Language detection is GitHub's.** Repos with mixed languages or mis-detected primary language may get wrong `language` frontmatter. Verify.
- **No dependency analysis.** The harvester does not clone repos or run dependency scanners. `Dependencies` and `Tech stack` sections are inferred from README mentions and may be incomplete.
