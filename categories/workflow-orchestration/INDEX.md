# workflow-orchestration

> Category node. Author, schedule, and monitor batch data/workflow pipelines (DAG orchestrators).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Apache Airflow** | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. | [→](airflow.md) |
| **Gaia** | An automation/pipeline platform that lets you build pipelines in any programming language (Go, Python, Java, C++, …) by compiling your code into plugins it executes — **now archived and no longer maintained**. | [→](gaia.md) |
| **Airflow Maintenance DAGs** | A small collection of ready-made Apache Airflow DAGs that keep an Airflow deployment healthy — clearing old metadata-DB rows, deleting stale task logs, killing zombie tasks, and similar housekeeping you'd otherwise script yourself. | [→](airflow-maintenance-dags.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Apache Airflow](airflow.md) | ✅ | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. |
| [Gaia](gaia.md) | ✅ | An automation/pipeline platform that lets you build pipelines in any programming language (Go, Python, Java, C++, …) by compiling your code into plugins it executes — **now archived and no longer maintained**. |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.md) | ✅ | A small collection of ready-made Apache Airflow DAGs that keep an Airflow deployment healthy — clearing old metadata-DB rows, deleting stale task logs, killing zombie tasks, and similar housekeeping you'd otherwise script yourself. |
| Prefect / Dagster / Argo Workflows / Temporal | 未收录 | Other workflow orchestrators named across the pages. |

## What belongs here

Tools whose primary job is to **author, schedule, and monitor batch data/workflow pipelines** as DAGs. Not low-latency event/stream processing, not agent build/run frameworks (see `agent-frameworks`).
