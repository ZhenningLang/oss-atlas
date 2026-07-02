---
name: Supabase
slug: supabase
repo: https://github.com/supabase/supabase
category: databases
tags: [postgres, firebase-alternative, auth, realtime, edge-functions, vector-database]
language: TypeScript
license: Apache-2.0
maturity: v2.x, stable, 105.0k stars (as of 2026-07)
last_verified: 2026-07-01
type: service
upstream:
  pushed_at: 2026-07-01T10:37:59Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: "?"
  overall_score: 0.0
  scored_axes: 0
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
---

# Supabase

The open-source Firebase alternative built on Postgres. Provides a dedicated PostgreSQL database, authentication, auto-generated APIs (REST, GraphQL, Realtime), edge functions, file storage, and an AI/vector toolkit — all in one platform.

![Supabase — health radar](../../assets/health/supabase.svg)

## When to use

You're building a web or mobile application and need a backend that handles auth, database, real-time subscriptions, and file storage without cobbling together multiple services. You want the power and familiarity of PostgreSQL (including extensions like `pgvector` and `postgis`) but don't want to manage the database, API layer, and auth system separately. You choose Supabase, create a project, and get an auto-generated REST API, a ready-to-use auth system with OAuth providers, and real-time WebSocket subscriptions straight from your Postgres tables. For AI features, you can store and query vector embeddings with `pgvector` without adding a separate vector database. You can self-host the entire stack or use the managed cloud with a generous free tier.

## When NOT to use

- **Heavy analytics / OLAP workloads** — Supabase is built on PostgreSQL, which is optimized for OLTP. For large-scale data warehousing or complex analytics, use a dedicated OLAP solution (BigQuery, ClickHouse, Snowflake).
- **Microservices with multiple databases** — Supabase is designed around a single Postgres instance per project. If your architecture requires many independent databases with separate lifecycles, the platform model may not fit.
- **No PostgreSQL familiarity** — While Supabase abstracts much of the database layer, you still write SQL for complex queries, migrations, and RLS policies. If your team avoids SQL entirely, the learning curve is real.
- **Extreme multi-region latency requirements** — Supabase supports read replicas but the primary write node is in a single region. If your application needs sub-10ms writes globally, you may need a different architecture.
- **Non-Postgres database requirement** — Supabase is deeply tied to PostgreSQL. If you need MongoDB, Cassandra, or a graph database as your primary store, Supabase is not the right choice.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Firebase | 未收录 | Google's managed backend-as-a-service (BaaS). | Firebase is fully managed and has a broader mobile SDK ecosystem, but it locks you into proprietary NoSQL (Firestore) and Google's platform. Supabase gives you open-source Postgres and avoids vendor lock-in. |
| Appwrite | 未收录 | Open-source Firebase alternative with broader language support. | Appwrite is also open-source and supports more client languages out of the box; Supabase has deeper Postgres integration and a more mature ecosystem. |
| Hasura | 未收录 | Auto-generated GraphQL API over Postgres. | Hasura is excellent for GraphQL-only APIs but lacks the built-in auth, storage, and edge functions that Supabase bundles. |
| [Deno](../dev-utilities/deno.md) | ✅ | Supabase uses Deno for edge functions. | Not a direct competitor — Deno is the runtime for Supabase edge functions, showing Supabase's production reliance on Deno. |
| Self-hosted Postgres + PostgREST + Keycloak | 未收录 | DIY stack matching Supabase's components. | More flexible and fully self-managed, but requires significantly more setup and ongoing maintenance than Supabase's integrated platform. |

## Tech stack

- **PostgreSQL** — core database with extensions (`pgvector`, `postgis`, `pg_graphql`)
- **PostgREST** — auto-generated REST API layer
- **Go** — realtime server, auth service, and storage API
- **TypeScript** — dashboard frontend and edge functions runtime
- **Deno** — edge functions execution environment
- **Kong / Kong Gateway** — API gateway and routing layer
- **Redis** — caching and realtime subscription state

## Dependencies

- PostgreSQL (v14+ recommended; managed if using Supabase Cloud)
- For self-hosting: Docker and Docker Compose (the official self-hosting stack)
- For edge functions: Deno runtime
- For storage: an S3-compatible object store (MinIO in self-hosted mode, or cloud S3)
- For realtime: Elixir/Erlang VM for the realtime server (bundled in Docker)
- SMTP or email provider for auth emails (self-hosted mode)

## Ops difficulty

**Medium** (self-hosted) / **Low** (cloud). The managed cloud tier requires minimal ops — just project configuration and monitoring. Self-hosting the full stack involves managing PostgreSQL, Kong, Redis, Go services, Deno edge functions, and object storage across Docker containers. The official `docker-compose` stack simplifies initial setup, but production self-hosting requires backup strategies, monitoring, and scaling planning for PostgreSQL.

## Health & viability

- **Maintenance**: Very active — pushed daily as of 2026-07, with a mature v2 platform and responsive core team (1,086 open issues). [推断]
- **Governance**: Owned by the `supabase` organization with a dedicated core team and clear product roadmap. The company has a strong open-source culture with Apache-2.0 licensing across the core stack. Bus factor is reasonable. [推断]
- **Backing**: Supabase Inc. is a venture-backed company with significant funding and a proven revenue model (managed cloud). The open-source core is strategically aligned with the commercial offering. [未验证]
- **Adoption**: Strong adoption with 105.0k stars, created in 2019 (7-year track record). Widely used in production across startups and enterprises. The Firebase alternative positioning drives consistent demand. [推断]
- **Risk flags**: Apache-2.0 is permissive. The venture-backed model means some features may be cloud-only (e.g., certain advanced analytics or enterprise features), but the core database, auth, and storage stack remains fully open-source. Monitor for open-core gating over time. [推断]

## Caveats (unverified)

- [未验证] Supabase Inc. has raised venture funding; the exact funding details and burn rate are not verified from primary sources.
- [推断] The self-hosted stack is documented but the primary engineering investment goes to the managed cloud; self-hosted users may encounter edge cases or slower bug fixes for non-cloud paths.
- [未验证] The exact feature parity between self-hosted and cloud tiers is not continuously documented; some enterprise features (e.g., SSO, advanced backups) may be cloud-only.
- [未验证] `pgvector` performance at very large scale (billions of embeddings) in a shared PostgreSQL instance has not been independently benchmarked for Supabase specifically.
