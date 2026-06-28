# workflow-orchestration

> Category node. Author, schedule, and monitor batch data/workflow pipelines (DAG orchestrators).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Apache Airflow** | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. | [→](airflow.md) |
| **Gaia** | Use it when studying the "pipelines-as-compiled-plugins" design as a read-only reference — the repo is archived and abandoned, never pick it for new production work. | [→](gaia.md) |
| **Airflow Maintenance DAGs** | Use it when self-managed Airflow needs proven copy-in DAGs to clean metadata-DB rows and stale logs — they run destructive DELETEs tied to version-specific internals, so dry-run and back up first. | [→](airflow-maintenance-dags.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Apache Airflow](airflow.md) | ✅ | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. |
| [Gaia](gaia.md) | ✅ | Use it when studying the "pipelines-as-compiled-plugins" design as a read-only reference — the repo is archived and abandoned, never pick it for new production work. |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.md) | ✅ | Use it when self-managed Airflow needs proven copy-in DAGs to clean metadata-DB rows and stale logs — they run destructive DELETEs tied to version-specific internals, so dry-run and back up first. |
| Prefect / Dagster / Argo Workflows / Temporal | 未收录 | Other workflow orchestrators named across the pages. |

## What belongs here

Tools whose primary job is to **author, schedule, and monitor batch data/workflow pipelines** as DAGs. Not low-latency event/stream processing, not agent build/run frameworks (see `agent-frameworks`).
