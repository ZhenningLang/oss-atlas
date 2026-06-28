---
name: UI for Apache Kafka (provectus/kafka-ui)
slug: kafka-ui
repo: https://github.com/provectus/kafka-ui
category: kafka-tools
tags: [kafka, web-ui, cluster-management, monitoring, schema-registry, kafka-connect]
language: Java
license: Apache-2.0
maturity: v0.7.2 (2024-04), upstream stalled — see Health, ~12.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
---

# UI for Apache Kafka (provectus/kafka-ui)

A free, open-source web UI for managing and observing Apache Kafka clusters — browse brokers, topics, partitions, consumer groups and their lag, produce/inspect messages, and wire in Schema Registry and Kafka Connect, all from a browser. **Note:** active development has moved to the community fork `kafbat/kafka-ui` (see Health).

## When to use

You're an engineer or SRE running one or more Kafka clusters and you're tired of `kafka-console-consumer.sh` and a wall of CLI flags every time someone asks "is this topic getting messages?" or "why is this consumer group lagging?". You want a lightweight dashboard you can stand up in one `docker run` that shows brokers, topics, partition assignments, consumer-group lag, and lets you click into a topic and actually *read* the messages — JSON, plain text, Avro, Protobuf — without writing a consumer. You point it at your bootstrap servers (and optionally Schema Registry and a Connect cluster), open `:8080`, and your data flows are suddenly observable to the whole team, not just whoever has the CLI and the right configs on their laptop.

It also fits when you need a self-hosted, no-license-cost alternative to commercial Kafka consoles, with OAuth (GitHub/GitLab/Google), role-based access control, and data masking for sensitive fields — enough governance to put in front of a team without exposing raw PII. For ad-hoc producing of test messages, creating/configuring topics by hand, and registering schemas through a few clicks, it removes a lot of console friction.

## When NOT to use

- **You want the actively-maintained edition.** This `provectus/kafka-ui` repo has effectively stalled (last release v0.7.2, 2024-04; last push 2024-07). The community fork **`kafbat/kafka-ui`** is where development continued. For a fresh deployment, prefer the maintained fork over this upstream — running unmaintained software against an evolving Kafka protocol is the headline risk here.
- **You need a full streaming control plane.** It's an observability/admin UI, not Kafka governance/lineage/data-catalog tooling and not a managed-platform control plane. Topic/ACL-as-code, large-scale multi-tenant governance, and lineage need dedicated tools.
- **Very large multi-cluster fleets with heavy RBAC/audit needs.** It does multi-cluster and RBAC, but enterprise audit trails, fine-grained quota management, and SLA support are where commercial consoles (Confluent Control Center, Conduktor) differentiate.
- **You're not on the JVM/Docker path.** It's a Spring-Boot Java app; you run a JVM (usually via the official Docker image). If you want a tiny single-binary or a desktop app, this isn't that.
- **Write-heavy admin as the primary workflow.** It can create topics and produce messages, but treating a click-UI as your provisioning system of record is fragile — keep destructive/admin operations in version-controlled tooling.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| kafbat/kafka-ui | 未收录 | The **maintained community fork** of this exact project — same UI, ongoing releases; for new installs it's generally the better choice than the stalled upstream. |
| Conduktor | 未收录 | Polished desktop/web Kafka platform; richer features and enterprise governance, but freemium/commercial — not a fully-open self-hosted OSS UI. |
| Confluent Control Center | 未收录 | Deep, enterprise-grade monitoring/governance in the Confluent Platform; commercial and tied to that ecosystem, far heavier than a single-container UI. |
| AKHQ | 未收录 | Open-source (Apache-2.0) Kafka web UI with similar scope (topics, consumers, Connect, schema registry, ACLs); a direct OSS substitute, different stack/UX. |
| Redpanda Console | 未收录 | Open-source Kafka/Redpanda UI (Go); clean, fast, works with vanilla Kafka too; some advanced features gated toward Redpanda's commercial tier. |
| kafka-python admin CLI | 未收录 | CLI, not a UI — scriptable/headless admin; complements rather than replaces a dashboard. |

## Tech stack

- **Backend:** Java / Spring Boot (reactive), packaged as a JAR and an official Docker image (`provectuslabs/kafka-ui`).
- **Frontend:** a JavaScript/TypeScript single-page web UI served by the backend.
- **Kafka integrations:** Kafka Admin/Consumer/Producer APIs, Schema Registry (Avro / JSON Schema / Protobuf), Kafka Connect, and pluggable serde (custom serialization/deserialization plugins, e.g. AWS Glue).
- **Auth & security:** OAuth 2.0 (GitHub/GitLab/Google), role-based access control, data masking.

## Dependencies

- **A JVM runtime** — in practice the official Docker image; or run the JAR yourself.
- **One or more Kafka clusters** to point at (bootstrap servers) — the whole reason it exists.
- **Optional integrations:** Schema Registry, Kafka Connect cluster(s), an OAuth identity provider for SSO. Dynamic config requires `DYNAMIC_CONFIG_ENABLED=true`.
- **No database of its own required for the basic single-cluster case** — it reads cluster state live; config is via env/YAML. [推断]

## Ops difficulty

**Low to medium.** The demo path is genuinely one command (`docker run -p 8080:8080 -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui`). For real use you write a config (YAML/env) listing clusters, schema registries, Connect endpoints, and auth — straightforward but it grows with the number of clusters and the RBAC matrix. JVM memory tuning matters under heavy message browsing on big topics. The larger, often-missed cost is **staying on an unmaintained upstream**: you'll likely want to migrate to the `kafbat/kafka-ui` fork for security and Kafka-version fixes, so factor a migration into your ops plan rather than pinning this repo forever.

## Health & viability

- **Maintenance (2026-06) — upstream stalled.** `provectus/kafka-ui` last released v0.7.2 in **2024-04** and last pushed **2024-07**; ~2 years without a release at time of writing. The API does **not** flag it `archived`, but it reads as **dormant**, not active. Active development continued in the community fork **`kafbat/kafka-ui`** (pushed 2026-06). This is the dominant verdict: treat the upstream as frozen. [推断]
- **Governance / backing.** `Organization`-owned (Provectus, a consulting company); the README states it stays free/open-source with no paid tier. But a single-vendor-curated OSS project that the vendor stops shipping is exactly the bus-factor scenario that played out — the community had to fork to keep it alive. [推断]
- **Age × Lindy.** Created 2019-11 (~6–7 years). Moderate age, but the *upstream's* Lindy is undercut by the maintenance halt — old-and-stalled fails the "still active" test. The **fork** carries the Lindy forward, not this repo. [推断]
- **Adoption.** Strong historical adoption (~12.2k stars, ~1.4k forks, large Docker-pull history) — the codebase is proven and widely deployed; the question is forward maintenance, not whether it works. [未验证]
- **Risk flags.** Running de-facto-unmaintained software against an evolving Kafka protocol (new broker versions, CVEs) is the principal risk; mitigation is migrating to the maintained fork. Apache-2.0, no relicense history found. [推断]

## Caveats (unverified)

- [未验证] ~12.2k stars / 346 open issues / last push 2024-07 / last release v0.7.2 (2024-04) as of 2026-06 — volatile, re-check.
- [推断] "Upstream dormant, development moved to kafbat/kafka-ui" is inferred from release/push recency on both repos (kafbat pushed 2026-06, ~2.5k stars) plus the well-known community fork; the upstream is not API-flagged `archived`.
- [推断] "No own database required" for the basic case is inferred from its live-read architecture, not confirmed against every deployment mode (some features may need extra stores).
- [未验证] Exact current feature parity and config differences between provectus upstream and the kafbat fork are not verified here — confirm against the fork's docs before migrating.
