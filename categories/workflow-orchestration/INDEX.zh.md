# workflow-orchestration

> 分类节点。编写、调度并监控批处理数据/工作流管线（DAG 编排器）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Apache Airflow** | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 | [→](airflow.zh.md) |
| **Gaia** | 一个自动化/流水线平台，让你用任意编程语言（Go、Python、Java、C++……）构建流水线——把你的代码编译成插件来执行——**现已归档，不再维护**。 | [→](gaia.zh.md) |
| **Airflow Maintenance DAGs** | 一组现成的 Apache Airflow DAG，用来让 Airflow 部署保持健康——清理元数据库的旧记录、删除陈旧任务日志、清掉僵尸任务，以及其它你本来要自己写脚本做的杂务。 | [→](airflow-maintenance-dags.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Apache Airflow](airflow.zh.md) | ✅ | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 |
| [Gaia](gaia.zh.md) | ✅ | 一个自动化/流水线平台，让你用任意编程语言（Go、Python、Java、C++……）构建流水线——把你的代码编译成插件来执行——**现已归档，不再维护**。 |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.zh.md) | ✅ | 一组现成的 Apache Airflow DAG，用来让 Airflow 部署保持健康——清理元数据库的旧记录、删除陈旧任务日志、清掉僵尸任务，以及其它你本来要自己写脚本做的杂务。 |
| Prefect / Dagster / Argo Workflows / Temporal | 未收录 | 各页对比里点到的其他工作流编排器。 |

## 什么该放这里

主要职责是把批处理数据/工作流管线作为 DAG **编写、调度与监控**的工具。不含低延迟事件/流处理，不含 agent 构建/运行框架(见 `agent-frameworks`)。
