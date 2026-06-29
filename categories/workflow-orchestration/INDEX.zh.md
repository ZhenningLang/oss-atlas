# workflow-orchestration

> 分类节点。编写、调度并监控批处理数据/工作流管线（DAG 编排器）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Apache Airflow** | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 | A（6/6） | [→](airflow.zh.md) |
| **Gaia** | 当作只读参考研究「流水线即编译插件」设计时用它——仓库已归档废弃，绝不可用于新的生产部署。 | D（5/6） | [→](gaia.zh.md) |
| **Airflow Maintenance DAGs** | 当自管 Airflow 需要现成 DAG 清理元数据库行和陈旧日志时用它——它执行依赖版本内部结构的破坏性删除，先 dry-run 并备份。 | D（4/6） | [→](airflow-maintenance-dags.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Apache Airflow](airflow.zh.md) | ✅ | A（6/6） | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 |
| [Gaia](gaia.zh.md) | ✅ | D（5/6） | 当作只读参考研究「流水线即编译插件」设计时用它——仓库已归档废弃，绝不可用于新的生产部署。 |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.zh.md) | ✅ | D（4/6） | 当自管 Airflow 需要现成 DAG 清理元数据库行和陈旧日志时用它——它执行依赖版本内部结构的破坏性删除，先 dry-run 并备份。 |
| Prefect / Dagster / Argo Workflows / Temporal | 未收录 | — | 各页对比里点到的其他工作流编排器。 |

## 什么该放这里

主要职责是把批处理数据/工作流管线作为 DAG **编写、调度与监控**的工具。不含低延迟事件/流处理，不含 agent 构建/运行框架（见 `agent-frameworks`）。
