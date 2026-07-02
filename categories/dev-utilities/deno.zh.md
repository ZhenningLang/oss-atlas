---
name: Deno
slug: deno
repo: https://github.com/denoland/deno
category: dev-utilities
tags: [javascript, typescript, runtime, secure-by-default, webassembly]
language: Rust
license: MIT
maturity: v2.x, stable, 107.3k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T09:52:46Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T10:00:00Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
    responsiveness:
      grade: ?
      raw: {}
    adoption:
      grade: A
      raw:
        stars: 107352
    longevity:
      grade: B
      raw: {}
    governance:
      grade: A
      raw:
        owner_type: Organization
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_data }
---

# Deno

一款现代 JavaScript、TypeScript 和 WebAssembly 运行时，具备安全默认设置和出色的开发者体验。基于 V8、Rust 和 Tokio 构建。

![Deno — 健康度雷达](../../assets/health/deno.zh.svg)

## 何时使用

你正在用 JavaScript/TypeScript 构建新的服务端项目或 CLI 工具，厌倦了 Node.js 的复杂性：`node_modules` 膨胀、`package.json` 依赖地狱，以及对外部工具（ts-node、nodemon、eslint、prettier）的需求。你想要一个将 TypeScript 视为一等公民、内置格式化、代码检查和测试、并默认强制执行安全权限（没有显式标志就不允许文件或网络访问）的运行时。你用一条 shell 命令安装 Deno，直接运行 `.ts` 文件，准备好时编译成独立二进制。Deno 的标准库和 npm 兼容性意味着你可以带着现有包一起迁移，同时享受现代工具链。

## 何时不用

- **现有 Node.js 单体应用**——Deno 可以通过 `npm:` 标识符运行许多 npm 包，但带有原生 Node.js 插件、C++ 绑定或深层 `node-gyp` 依赖的复杂项目不太可能平滑迁移。
- **深度 npm 生态锁定**——虽然 Deno 有 npm 兼容性，但某些包依赖 Node.js 特定 API 或 post-install 脚本，可能无法运行。请务必测试依赖树。
- **团队不熟悉 Deno**——如果你的整个团队都熟悉 Node.js 而没有人有 Deno 经验，对于短期项目来说， onboarding 期间的生产力下降可能超过收益。
- **V8 特定性能调优**——Deno 和 Node.js 一样使用 V8，因此 CPU 密集型性能相似。如果你需要在 V8 层面优化，切换运行时没有帮助。
- **Deno Deploy 锁定顾虑**——Deno 的云边缘运行时（Deno Deploy）是专有服务；如果你希望完全可移植的无服务器代码，请确认能否在其他地方运行。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| Node.js | 未收录 | 现任 JS/TS 运行时，拥有最大的生态。 | Node.js 拥有最深的 npm 生态和最广泛的托管支持；Deno 提供更干净、更安全的开发者体验，但社区更小。 |
| Bun | 未收录 | 快速的全能 JS 运行时，内置打包器和包管理器。 | Bun 也很快且将 TypeScript 视为一等公民，但比 Deno 更年轻、未经充分检验。 |
| [Supabase](../databases/supabase.zh.md) | ✅ | 使用 Deno 作为边缘函数运行时。 | 不是运行时本身的对比，但展示了 Deno 在无服务器边缘场景的生产级使用。 |
| Wasmer / Wasmtime | 未收录 | 纯 WebAssembly 运行时。 | 这些是用于 Wasm 模块的，不是 JS/TS 应用；Deno 可以运行 Wasm，但主要是 JS 运行时。 |

## 技术栈

- **Rust**——核心运行时、HTTP 服务器和沙箱层
- **V8**——JavaScript 引擎（与 Node.js 和 Chrome 相同）
- **Tokio**——Rust 的异步运行时，驱动 Deno 的 I/O
- **TypeScript**——一等语言支持（内部转译）
- **WebAssembly**——支持在 JS/TS 旁边运行 Wasm 模块

## 依赖

- Deno 二进制文件（单一可执行文件，无需外部运行时）
- 编译时：生成独立二进制需要 C++ 链接器（Deno 使用 `deno compile`）
- 可选：通过 `npm:` 标识符使用 npm 包，或通过 JSR（JavaScript Registry）使用包
- Deno 原生项目不需要 `node_modules` 或 `package.json`

## 运维难度

**低**。Deno 是可在主流操作系统上运行的单一二进制文件。部署时，可以直接运行 `deno run`，用 `deno compile` 编译为独立二进制，或部署到 Deno Deploy（托管边缘）。内置工具链（test、fmt、lint、bench）减少了对单独 devDependencies 的需求。没有 `node_modules` 膨胀简化了 CI/CD 缓存和 Docker 镜像大小。

## 健康度与可持续性

- **维护**：非常活跃——截至 2026-07 每日推送，v2 版本线成熟，核心团队响应迅速（1,354 个开放 issue）。[推断]
- **治理**：由 `denoland` 组织所有，Ryan Dahl（Node.js 创建者）是关键人物。项目有清晰的技术愿景和多个核心贡献者。bus factor 合理。
- **背书**：Deno Land Inc. 是项目背后的商业实体；Deno Deploy 是其收入来源。该公司已获得风险投资，这既带来稳定性，也可能导致未来方向冲突。[未验证]
- **采用**：采用度强劲，107.3k star，2018 年创建（8 年记录）。被 Supabase 等公司用于边缘函数，并在各种生产级 CLI 工具中使用。[推断]
- **风险旗标**：MIT 许可非常宽松。风险投资支持的背书模式意味着开源路线图可能受商业产品 Deno Deploy 的影响。未见 relicense 历史，但需关注是否出现 open-core 阉割。[未验证]

## 存疑（未验证）

- [未验证] Deno Land Inc. 已获得风险投资；具体融资轮次和投资者尚未从一手来源核实。
- [推断] Deno Deploy 的专有边缘运行时可能产生激励，使未来优先发展 Deno 特定 API 而非标准 Web 兼容性。
- [未验证] 除 Supabase 外的生产级部署数量和企业用户尚未核实。
