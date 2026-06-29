---
name: ThriftPy
slug: thriftpy
repo: https://github.com/Thriftpy/thriftpy
category: networking
tags: [thrift, rpc, serialization, python, deprecated, archived]
language: Python
license: MIT
maturity: v0.3.9 (2016-08), deprecated + archived, ~1.1k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
health:
  schema: 1
  computed_at: 2026-06-29T10:06:43Z
  overall: D
  overall_score: 0.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 2830
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: default
        window_offset_days: 2
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 4521
        last_commit_age_days: 2830
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: unattributable }
---

# ThriftPy

Apache Thrift 的纯 Python 实现：运行时直接加载 `.thrift` 文件、即时生成 RPC 客户端/服务端代码——**已弃用并归档**，由 [thriftpy2](https://github.com/Thriftpy/thriftpy2) 取代。

![thriftpy — 健康度雷达](../../assets/health/thriftpy.zh.svg)

## 何时使用

说实话，2026 年你几乎不会为新项目去选*这个*仓库——但它的来历仍值得一说。你是某家服务间走 Apache Thrift 的公司的 Python 后端工程师，官方 `thrift` 的 Python 绑定让你头疼：它需要一步代码生成（`thrift --gen py`），生成的代码冗长，构建时还可能拖进一个编译器。你只想直接对着 `.thrift` IDL，让可用的客户端/服务端对象凭空出现。ThriftPy 当年的卖点正是这个：`pingpong = thriftpy.load("pingpong.thrift")`，模块就在进程内出现，没有 codegen 构建步骤，且与上游 Thrift 服务端/客户端在线协议上兼容。用 `make_server` 起服务端、`make_client` 起客户端，几行就搞定。

实际上今天这个卖点活在 **thriftpy2**（维护中的 fork）里。你会落到*本*页，通常是因为接手了一个还在 `import thriftpy` 的遗留服务（Python 2.7 时代）、需要在迁移前搞清它在做什么，或者在选这个家族时需要知道：活着的成员是 thriftpy2，不是这个已归档的原版。

## 何时不用

- **它已弃用且仓库已归档。** README 第一句就让你迁移到 thriftpy2；GitHub 仓库处于归档状态（只读，不再有新提交/issue）。别在它上面起任何新东西。[推断]
- **2016 年后无发布、2018 年后无 push。** 最后一个 tag `v0.3.9` 是 2016-08，最后 push 是 2018-12。它早于现代 Python——为 Python 2.7 / 3.4+ 而写——对更新的解释器或 CVE 没有任何修复。[未验证]
- **你想要维护中的版本。** 改用 **thriftpy2**——同样的运行时加载 `.thrift` 模型，仍在活跃 push（2026-06），支持当前 Python。
- **你需要它那套之外的协议/传输。** 它实现的是 2016 年的 binary/compact/JSON 协议与 buffered/framed/tornado/http 传输；Apache Thrift 里更新的东西这里没有。
- **你依赖旧的 tornado 集成。** 它的异步服务端/客户端钉死在 `tornado>=4.0,<5.0` 和 `toro` 上——两者都早已过时，无法与现代异步栈共存。
- **你需要厂商/基金会支持。** 它是社区项目（最初出自 eleme），如今冻结，没有支持渠道。

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| thriftpy2 | 未收录 | 同一组织维护的后继者——同样运行时加载 `.thrift` 模型、支持当前 Python、2026 年仍活跃。离开本仓库的直接理由。 |
| Apache Thrift（官方 `thrift` Python 库） | 未收录 | 标准、多语言、基金会治理；需要一步代码生成、更重，但它是参考实现且广受支持。 |
| gRPC + Protocol Buffers | 未收录 | 不同的 IDL/线协议（HTTP/2、protobuf）；生态与工具链大得多，是现代新 RPC 的常见选择，但与 Thrift 不兼容。 |
| Apache Avro | 未收录 | 基于 schema 的序列化且带 RPC；schema 用 JSON 定义，在数据/Hadoop 生态里很强；与 Thrift 线协议不兼容。 |

## 技术栈

- **语言：** 纯 Python（按 2016 年 README，支持 CPython 2.7 / 3.4+、PyPy），并带**可选的 Cython** 扩展，为 binary/compact 协议与 buffered 传输的热路径加速。
- **解析器：** `ply`（Python Lex-Yacc）是唯一的硬运行时依赖——它在加载时解析 `.thrift` IDL。
- **协议：** binary（py + cython）、compact（py + cython）、JSON。**传输：** buffered（py + cython）、framed、tornado、http。
- **模型：** 运行时把 `.thrift` 文件加载成 Python 模块对象（`thriftpy.load`），也可走 import hook，取代离线 codegen 步骤。

## 依赖

- **运行时：** `ply>=3.4,<4.0`（必需）。这是唯一的强制依赖。
- **可选：** `tornado>=4.0,<5.0` + `toro>=0.6` 用于异步 tornado 服务端/客户端；`cython>=0.23` 在构建期编译原生协议/传输扩展（在 PyPy / 非 UNIX / 无 Cython 时回退到纯 Python）。
- **外部服务：** 它自己不需要——它是 RPC 客户端/服务端库；在线协议上说 Thrift 的服务由你提供。

## 运维难度

**运维本身低，但因为它已冻结所以*风险*高。** 作为库，除了 `pip install` 和你自己的服务进程之外没什么要部署或运行——没有数据存储、没有守护进程。运维负担全在陈旧上：它面向 Python 2.7/3.4、钉死过时的 tornado；在现代解释器上你可能撞到不兼容，而且因为仓库已归档不会有上游修复。这里真实的“运维”任务是**迁移到 thriftpy2**，而不是运行它。[推断]

## 健康度与可持续性

- **维护（2026-06）。** **已废弃 / 已归档。** 最后发布 `v0.3.9` 在 2016-08，最后 push 在 2018-12，仓库在 GitHub 上标记为 `archived`。README 明确弃用它、改荐 thriftpy2。[推断]
- **治理 / bus factor。** 归在 `Thriftpy` GitHub 组织下（Organization 所有者），最初创建于 eleme。维护精力已完全转移到 thriftpy2 仓库；这个仓库什么都收不到。[推断]
- **年龄 × Lindy。** 2014-02 创建（约 12 岁）但**已不再活跃**——一个长期*被废弃*的项目不通过 Lindy 检验，而非通过它。这里的长寿是历史，不是安全信号。[推断]
- **后继者健康度。** **thriftpy2**（同组织）是活着的延续：2026-06 仍有 push、未归档、约 587 star、约 43 个 open issue——若你想押这个家族，押它。[未验证]
- **风险标记。** 弃用通知（明确）、归档仓库、Python 2 时代代码、过时的钉死异步依赖。无 relicense 历史（全程 MIT）。主要风险就是它已到生命终点。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1,148 star / 281 fork / 72 个 open issue（来自 GitHub API）——star/issue 数对时间敏感、仅供参考；归档仓库的 open-issue 数实际已冻结。
- [未验证] Python 版本支持（2.7 / 3.4+ / PyPy）与确切的协议/传输清单取自 2016 年的 README 与 `setup.py`；在当前 Python 3.12+ 上的行为未验证，很可能已劣化。
- [未验证] thriftpy2 的事实（2026 年活跃、约 587 star）来自 GitHub API 快照，并基于 README 的迁移链接假定它是维护中的后继者；与本仓库的功能 parity 未逐项 diff。
- [推断] “已冻结 / 不会再修”是从 `archived` 标记加弃用通知推断的，并非来自一份枚举弃用范围的维护者声明。
- [推断] 可选 Cython 构建的回退行为是从 `setup.py` 逻辑（仅 UNIX + CPython）读出的，未在此实跑验证。
