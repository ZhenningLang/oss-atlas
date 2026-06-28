# task-queue

> 分类节点。分布式后台任务执行——任务队列与作业调度器。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **XXL-JOB** | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 | [→](xxl-job.zh.md) |
| **Celery** | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 | [→](celery.zh.md) |
| **Kombu** | 一个 Python 消息库，用一套地道的高层 API 统一封装多种消息 broker——AMQP/RabbitMQ，外加可插拔的"虚拟"传输（Redis、Amazon SQS、MongoDB、ZooKeeper、内存）——它正是 Celery 所构建于其上的传输层。 | [→](kombu.zh.md) |
| **Flower** | 面向 Celery 的实时 Web 看板与管理工具——展示任务/worker 的实时状态，可巡检并控制 worker，并为运行中的 Celery 集群暴露 REST API 与 Prometheus 指标。 | [→](flower.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [XXL-JOB](xxl-job.zh.md) | ✅ | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 |
| [Celery](celery.zh.md) | ✅ | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 |
| [Kombu](kombu.zh.md) | ✅ | 一个 Python 消息库，用一套地道的高层 API 统一封装多种消息 broker——AMQP/RabbitMQ，外加可插拔的"虚拟"传输（Redis、Amazon SQS、MongoDB、ZooKeeper、内存）——它正是 Celery 所构建于其上的传输层。 |
| [Flower](flower.zh.md) | ✅ | 面向 Celery 的实时 Web 看板与管理工具——展示任务/worker 的实时状态，可巡检并控制 worker，并为运行中的 Celery 集群暴露 REST API 与 Prometheus 指标。 |
| RQ / Dramatiq / arq / Quartz / PowerJob | 未收录 | 各页对比里点到的其他任务队列与调度器。 |

## 什么该放这里

主要职责是**分布式后台任务执行**的系统——任务队列与作业调度器。不含工作流/DAG 编排器(见 `workflow-orchestration`)，不含 agent 运行时(见 `agent-frameworks`)。
