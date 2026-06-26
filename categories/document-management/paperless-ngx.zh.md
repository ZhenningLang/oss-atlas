---
name: paperless-ngx
slug: paperless-ngx
repo: https://github.com/paperless-ngx/paperless-ngx
category: document-management
tags: [dms, ocr, self-hosted, django, angular, full-text-search, document-archive, homelab, tesseract, gplv3]
language: Python (backend) + TypeScript/Angular (frontend)
license: GPL-3.0
maturity: Mature, active; stable v2.20.x (2026-04), v3.0 in beta as of 2026-06 (see caveats)
last_verified: 2026-06-26
---

# paperless-ngx

一套自托管文档管理系统（DMS），基于 Django + Angular，配合 PostgreSQL/Redis，把账单、发票、信件等纸质/扫描件自动 OCR、打标签、建索引并提供全文检索。

## 何时使用

自托管用户或小型办公室想把实体纸质文件（发票、账单、信件、收据）数字化，整理成家用服务器 / NAS / homelab 上的**单一可检索档案库**。你把扫描件丢进 consume 文件夹，paperless 会对其进行 OCR，按匹配规则自动套上标签、通信方（correspondent）、文档类型，并提供全文检索和 Web UI。

最适合的场景是：部署在**受信任的内部网络**上，文档规模处于个人到小团队级别，目标是「扫描、归档、然后忘掉」——而非协作编辑或正式审批流程。Docker 优先的安装方式让它无需深厚运维功力即可上手。

## 何时不用

- **不是安全/合规存储库**——文档以明文形式存储在磁盘上，全文以明文存入数据库，文件名也不加密。内置文档加密功能已被移除（paperless-ng 0.9，v3 再次移除），并且 `[未验证]` 据称维护者表示没有添加静态加密的计划。磁盘级加密得你自己来。
- **不要跑在不可信/共享主机上**——项目明确警告反对这样做。
- **不适合严格的多租户 / 逐文档隐私**——权限/归属模型存在已知缺口（例如经 consume 文件夹导入的文档可能没有 owner，从而对所有用户可见）。它不是一套加固过的多用户系统。
- **不是企业级 EDMS**——没有内置的多步审批工作流、生命周期/留存管理或电子签名（这些请用 Mayan EDMS）。
- **不适合协作撰写/编辑**——它是*已完成*文档的档案库，而非 Google Docs 的替代品。
- **弱硬件上做大批量 OCR 体验差**——OCR 和自动匹配都吃 CPU/RAM；文档自身就建议在受限设备（树莓派等）上削减 worker 数、只处理首页、禁用 NLTK。
- **不支持 Windows**（需要 Linux 主机）。
- **升级锁定 / 维护风险**——社区维护，无商业方背书；大版本会带来重大破坏性变更（v3 移除 API v1、重建 migrations、改动 pre/post-consume 脚本参数）。升级前请锁定版本并阅读 release notes。

## 横向对比

| 替代方案 | 是否收录 | 取舍 |
|---|---|---|
| Mayan EDMS | 未收录 | 同样是 Python/Django，但属于更重的企业级 EDMS，带有真正的工作流引擎、版本管理和细粒度权限；运维陡峭得多，对个人扫描档案库而言是杀鸡用牛刀。Apache-2.0（比 paperless 的 GPLv3 更宽松）。 |
| Docspell | 未收录 | 收件箱/元数据抽取模型，邮件导入能力强；Scala/JVM 技术栈意味着更重的内存占用，社区也比 paperless-ngx 小。 |
| Teedy / sismics docs | 未收录 | 轻量级 Java DMS，带版本管理、界面干净、资源需求适中；自动 OCR/自动打标签较弱，势头也较小。 |
| OpenDocMan | 未收录 | 面向企业文件管控和访问规则的 PHP/MySQL DMS；界面陈旧，没有一流的 OCR/自动打标签——仅当你需要在既有 PHP 栈上做简单 Web 访问控制时才考虑。 |
| 自建（Tesseract + Meilisearch/Elasticsearch + 对象存储） | 未收录 | 灵活性最高，对加密/schema 完全掌控，但你得自行搭建并维护整条 ingest/OCR/index/UI 流水线——只有当 paperless 的数据模型或安全约束成为硬伤时才值得。 |

## 技术栈

- Python、Django（后端）；Angular、TypeScript（前端）
- PostgreSQL（推荐）；支持 SQLite 或 MariaDB
- Redis / Valkey（消息代理）
- Tesseract OCR、ImageMagick
- Apache Tika + Gotenberg（可选——Office/HTML 格式）
- Whoosh（搜索，v2）→ Tantivy（搜索，v3）
- Docker / docker-compose

## 依赖

- **PostgreSQL**（推荐；也支持 SQLite 或 MariaDB）
- **Redis 或 Valkey**（必需的消息代理）
- **Tesseract OCR** 4.0.0+ 及语言包
- **ImageMagick** 6+
- **Apache Tika + Gotenberg**——仅在需要导入 Office/非 PDF 格式时
- **Docker + docker-compose**（推荐的部署方式）
- **Linux 主机**（不支持 Windows）；裸机安装时，v3 线上为 Python 3.11–3.14 `[未验证]`（据称 v2.20.x 稳定线仍支持 Python 3.10+）

## 运维难度

**中等。** 多容器 docker-compose 栈（web + worker + Redis + DB，处理 Office 文档还需加 Tika/Gotenberg）。配置完成后日常运维很轻，但是：OCR 吃 CPU/RAM，在低功耗硬件上很慢；数据库和文档/媒体卷的备份都得你自己负责；大版本升级带破坏性变更（v3 移除 API v1、放弃 Python 3.10、重建 migrations、改动 consume 脚本），因此升级需要阅读 release notes。绝不能暴露在不可信主机上。

## 存疑（未验证）

- **Star 数**——42.5k，来自单次抓取 GitHub 仓库页面（2026-06），未与 API 交叉核对。`[未验证]`
- **Release 版本/日期**——v2.20.15（约 2026-04-27）和 v3.0.0-beta.rc1（约 2026-05-05）来自搜索聚合器（releasebot/newreleases），本次未在 GitHub releases 页面上确认。`[未验证]`
- **v3 特性清单**——tantivy 后端、本地「Paperless AI」、文档版本、OCR 插件框架、移除 API v1、放弃 Python 3.10、consume 脚本变更——取自对 v3 beta 的搜索摘要，而非完整 release notes。`[未验证]`
- **Gotenberg**——基于 `-tika` 的 compose 文件被列为可选配套组件；在抽取出的安装文档中未明确确认。`[未验证]`
- **资源需求**——「吃 CPU/RAM」是根据文档中省资源指引得出的定性判断；官方未发布最低 RAM/CPU 规格。`[未验证]`
