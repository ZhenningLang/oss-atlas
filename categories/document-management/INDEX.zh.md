# document-management

> 三级路由的第 2 级。把扫描件/纸质文档做摄取、OCR、打标签与全文检索。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 许可证 | 页面 |
|---|---|---|---|
| **paperless-ngx** | 在受信任的家用服务器 / NAS 上自托管一个可检索的扫描件档案库（发票、账单、信件），带 OCR + 自动打标签。 | GPL-3.0 | [→](paperless-ngx.zh.md) |

## 对比矩阵

项目页里点到、但**尚未收录**的替代方案。

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [paperless-ngx](paperless-ngx.zh.md) | ✅ | 个人/小团队扫描档案库里势头最好的自托管 DMS；OCR + 自动打标签出色——但无静态加密、多租户权限弱、非企业级 EDMS。 |
| Mayan EDMS | 未收录 | 更重的企业级 EDMS：真正的工作流引擎、版本管理、细粒度权限（Apache-2.0）——但运维陡峭得多，对个人档案库是杀鸡用牛刀。 |
| Docspell | 未收录 | 邮件导入 + 元数据抽取强——但 Scala/JVM 栈、内存更重、社区更小。 |
| Teedy / sismics docs | 未收录 | 轻量 Java DMS，界面干净、资源适中——但 OCR/自动打标签较弱、势头较小。 |
| 自建（Tesseract + Meilisearch + 对象存储） | 未收录 | 对加密/schema 完全掌控——但整条流水线都得你自己搭建维护。 |

## 什么该放这里

主要职责是**摄取、OCR、组织、检索**文档的系统。不包括通用文件同步（Nextcloud）、笔记、协作撰写。
