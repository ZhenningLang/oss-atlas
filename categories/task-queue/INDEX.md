# task-queue

> Category node. Distributed background job execution — task queues and job schedulers.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **XXL-JOB** | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. | [→](xxl-job.md) |
| **Celery** | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. | [→](celery.md) |
| **Kombu** | Use it when a Python service must publish/consume messages across swappable brokers (RabbitMQ, Redis, SQS) — virtual transports emulate AMQP imperfectly, so "swap the URL" is not identical behavior. | [→](kombu.md) |
| **Flower** | Use it when a production Celery cluster needs a live dashboard to inspect and control workers and export Prometheus metrics — it can revoke tasks, so never expose it unauthenticated. | [→](flower.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [XXL-JOB](xxl-job.md) | ✅ | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. |
| [Celery](celery.md) | ✅ | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. |
| [Kombu](kombu.md) | ✅ | Use it when a Python service must publish/consume messages across swappable brokers (RabbitMQ, Redis, SQS) — virtual transports emulate AMQP imperfectly, so "swap the URL" is not identical behavior. |
| [Flower](flower.md) | ✅ | Use it when a production Celery cluster needs a live dashboard to inspect and control workers and export Prometheus metrics — it can revoke tasks, so never expose it unauthenticated. |
| RQ / Dramatiq / arq / Quartz / PowerJob | 未收录 | Other task queues & schedulers named across the pages. |

## What belongs here

Systems whose primary job is **distributed background job execution** — task queues and job schedulers. Not workflow/DAG orchestrators (see `workflow-orchestration`), not agent runtimes (see `agent-frameworks`).
