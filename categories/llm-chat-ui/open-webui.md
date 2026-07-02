---
name: Open WebUI
slug: open-webui
repo: https://github.com/open-webui/open-webui
category: llm-chat-ui
tags: [self-hosted, ai-chat, ollama, rag, openai, mcp]
language: Python
license: NOASSERTION
maturity: v0.x, active, 144k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-01T08:41:05Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:28:38Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 11
        band: relaxed_solo
        window_offset_days: 2
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: open-webui
        dependent_repos_count: 0
        downloads_last_month: 1635855
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.0
    longevity:
      grade: B
      raw:
        repo_age_days: 999
        last_commit_age_days: 1
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 160
        top1_share: 0.705
        top3_share: 0.837
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Open WebUI

An extensible, feature-rich, user-friendly self-hosted AI platform that operates entirely offline and supports Ollama, OpenAI-compatible APIs, and built-in RAG.

![Open WebUI — health radar](../../assets/health/open-webui.svg)

## When to use

You're a privacy-conscious developer or small team who wants a self-hosted chat interface for local and remote LLMs. You run Ollama on your own hardware and need a polished web UI that supports multiple models, document upload for RAG, and conversation history without sending data to third-party cloud services. You want something that works out of the box with Docker, has a modern UI, and supports community plugins for extensibility.

## When NOT to use

- **Multi-user team admin** — Open WebUI is single-user-shaped by default; advanced RBAC and team quotas are not its core strength.
- **Zero self-hosting burden** — You must run and maintain the Docker container, manage model files, and keep the app updated.
- **Enterprise SSO/compliance** — While it supports OAuth, enterprise-grade admin dashboards, audit trails, and SLA guarantees are absent.
- **Mobile-native experience** — The primary interface is web-based; mobile app experience is through the browser.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [NextChat](nextchat.md) | ✅ | Lightweight self-deployable chat UI. | NextChat is simpler and faster to deploy; Open WebUI is heavier but has built-in RAG and more features. |
| [HiveChat](../team-chat/hivechat.md) | ✅ | Admin-managed team chat with quotas. | HiveChat is for RBAC team admin; Open WebUI is for personal/small-group use. |
| LibreChat | 未收录 | Another self-hosted chat UI. | LibreChat has a broader plugin ecosystem but is not indexed here. |
| Lobe Chat | 未收录 | Design-focused chat UI. | Lobe Chat emphasizes visual polish and plugin market; Open WebUI emphasizes offline operation. |
| ChatGPT / Claude web apps | 未收录 | Closed-source cloud chat. | Proprietary and require cloud; Open WebUI is self-hosted and works offline. |

## Tech stack

- **Python** — backend and API layer
- **SvelteKit** — frontend framework
- **Docker** — primary deployment method
- **Ollama** — local LLM runtime integration

## Dependencies

- Docker runtime for deployment
- Ollama (for local models) or OpenAI-compatible API keys (for remote models)
- A device or server to host the application
- Optional: vector store for RAG document ingestion

## Ops difficulty

**Low to medium**. A single Docker container handles the core app. The main burden is keeping Ollama model files updated (large downloads) and managing document uploads for RAG. For a single user, it is straightforward; for a small team, you may need to configure authentication and manage resource usage.

## Health & viability

- **Maintenance**: Very active — pushed daily as of 2026-07, with a responsive issue tracker (242 open issues). [推断]
- **Governance**: Owned by the open-webui organization; appears to have a dedicated team with reasonable bus factor.
- **Backing**: No major corporate backing visible; community-driven with active Discord and sponsor program. [未验证]
- **Adoption**: Very high star count (144k) and fork volume (20k+) for a project created in late 2023. The ~3-year track record is positive but star count may include hype. [推断]
- **Risk flags**: The `NOASSERTION` license metadata needs clarification for commercial use. The project is relatively young (created 2023-10) and the high star count warrants caution about organic vs. hype-driven adoption. [未验证]

## Caveats (unverified)

- [未验证] The GitHub API reports `NOASSERTION` as the license; the actual license terms must be verified before commercial use.
- [未验证] The exact enterprise features and their availability in the open-source edition vs. a potential paid tier are not confirmed.
- [推断] The 144k star count on a ~3-year-old repo may include significant hype-driven growth; verify production adoption in your target environment.
