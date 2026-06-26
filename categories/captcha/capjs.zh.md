---
name: Cap
slug: capjs
repo: https://github.com/tiagozip/cap
category: captcha
tags: [captcha, proof-of-work, bot-detection, anti-spam, self-hosted, privacy]
language: JavaScript
license: Apache-2.0
maturity: standalone v3.1.5, capjs-core v0.1.1, active (2026-06)
last_verified: 2026-06-26
type: library
---

# Cap

一个轻量、可自托管的 reCAPTCHA/hCaptcha/Turnstile 替代品：用一道无感的工作量证明（proof-of-work，客户端做 SHA-256 nonce 搜索，跑在 Rust→WASM worker 里）外加可选的 JavaScript instrumentation 检测来拦住某个动作，发放一个可兑换 token 让你的服务端校验——自托管时没有图片验证，也不向第三方发任何网络请求。

## 何时使用

你是后端或全栈工程师，手上有一个注册表单、一个联系页接口，或一条公开 API 路由，老被机器人刷——刷假账号、刷垃圾提交、撞库。你不想嵌 reCAPTCHA 或 Turnstile，因为那会把用户数据和一段脚本送到 Google/Cloudflare，你也不想让真人去点红绿灯方格图。你希望把滥用的成本压到**机器**身上（花 CPU 去解题），而不是耗用户的耐心和隐私。

Cap 正好适合这个场景。你在受保护的表单上放一个 `<cap-widget>`（也可以走编程式调用，或用无感的 floating 模式），服务端把 `capjs-core`——一个**无状态、自带存储**的生成/校验器——接进你的 Node 或 Bun handler。widget 拉一道挑战，让访客的 CPU 在并行 WASM worker 里花几百毫秒去凑 SHA-256 前缀，然后提交解；你的服务端重新生成同样的挑战、校验通过后发回一个 token，你在处理请求前用 `validateToken()` 检查它。如果你完全不想碰这个库，就跑 **Standalone** 的 Docker 镜像（`tiago2/cap:latest`），把应用指向它那个兼容 reCAPTCHA 的 `/siteverify` 接口，并在内置面板里管理 site key。

## 何时不用

- **你要挡住一个有钱有决心的攻击者或打码平台。** 工作量证明抬高的是滥用的*成本*，并不能*打败*一个愿意烧 CPU 或雇真人的求解者。它是摩擦，不是墙——高价值目标仍需限流、风控评分和服务端校验。
- **你想要一道全站 / 反向代理级的机器人墙。** Cap 守的是*具体动作*（表单、接口），放正常浏览通行。要在代理层把整站对爬虫封死，Anubis（`未收录`）才是对口工具；Cap 是按动作粒度的。
- **工作量证明对你用户的设备是硬伤。** PoW 会消耗客户端 CPU/电量；在低端手机上或难度调高时会增加延迟、耗电。如果你不能接受任何客户端计算，无感的行为/风险评分服务（Turnstile）是另一种取舍。
- **你要的是全托管、有 SLA、零运维的服务。** 自托管意味着*你*来跑服务（或 Standalone 容器 + Redis）、轮换密钥、自己扛可用性。没有厂商可呼叫。
- **你想把 CAPTCHA 当成一个有审计支持的法务/合规无障碍勾选项。** 这是个年轻的开源项目（`capjs-core` v0.1.1），不是带支持合同的企业级供应商。
- **你指望开箱即用的强机器人*分类*能力。** Cap 的 instrumentation 层增加了一些信号，但它不是 ML 风控引擎；它不会像商业服务宣称的那样去给访客打"有多像真人"的分。

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| reCAPTCHA (Google) | 未收录 | 全托管、免费、风控评分强——但会把用户数据送到 Google、要点图、是第三方依赖。Cap 自托管、隐私优先；运维归你，也拿不到 Google 量级的风控模型。 |
| hCaptcha | 未收录 | reCAPTCHA 的托管替代，可给站长分成；仍是第三方、基于图片。Cap 的 widget 约小 250 倍、可完全自托管、无外部请求。 |
| Cloudflare Turnstile | 未收录 | 全托管、无感、客户端不做 PoW，靠 Cloudflare 网络的行为信号——但它是托管在 Cloudflare 上的依赖。Cap 把一切留在你自己的基础设施里，代价是自己运维。 |
| Altcha | 未收录 | 最接近的同类：开源、客户端工作量证明、不做指纹、widget 为 MIT。Altcha 的开源版只有 PoW（ML 检测是付费的 Sentinel 产品），服务端/面板要你自己接；Cap 打包了 instrumentation + 带面板的 Standalone 服务，Apache-2.0。 |
| mCaptcha | 未收录 | 自托管的 Rust 工作量证明 CAPTCHA，有自己的限流式难度模型；目标重叠，技术栈与手感不同。 |
| FriendlyCaptcha | 未收录 | 注重隐私的 PoW CAPTCHA，但在维护的产品是托管的商业服务；Cap 完全开源、自托管。 |
| Anubis | 未收录 | 反向代理 / 全站级 PoW 网关，挡爬虫与 AI crawler——作用域不同（入口闸门 vs 按动作）。两者互补而非互替。 |

## 技术栈

- **Widget：** JavaScript web component（`<cap-widget>`），gzip 后约 20 KB、运行时零依赖；支持 normal、floating（无感）和编程式三种模式。
- **求解器：** 挑战在客户端通过反复对 salt+nonce 做 **SHA-256** 直到 hash 命中目标前缀来求解；热循环是 **Rust 编译成 WebAssembly**（`@cap.js/wasm`），并在多个 **Web Worker** 里并行跑。
- **服务端库（`capjs-core`）：** 面向 Node.js 和 Bun 的无状态 TypeScript/ESM 模块，负责生成挑战、兑换解（`redeemChallenge()`）、校验 token（`validateToken()`）。它定义了挑战与 token 的*可插拔存储接口*（`store/read/delete/deleteExpired`）——存储用 Postgres、内存 `state` 对象或任何后端都行。
- **Standalone 服务：** 基于 **Bun** + **Elysia**，自带面板、兼容 reCAPTCHA 的 `/siteverify` 接口、多 site key 支持，可选 MaxMind GeoIP 与无头浏览器检测。
- **Instrumentation 挑战：** 可选，在沙箱 iframe 中解压并执行，与 PoW 一起构成第二道校验层。

## 依赖

- **库路径（`capjs-core`）：** Node.js 或 Bun 运行时。*不自带存储 / 文件系统*——存储后端由你提供（如 Postgres），或用内存 `state` 对象。构建期依赖 `esbuild`（可选 `javascript-obfuscator`）。
- **Standalone 路径：** Docker（镜像 `tiago2/cap:latest`）加一个 **Redis 兼容存储**（官方 `docker compose` 用 **Valkey**，经 `REDIS_URL` 连接）。配置走环境变量：`ADMIN_KEY`（面板登录，建议 32+ 字符）、`REDIS_URL`；默认端口 `3000`。
- **客户端：** 支持 WebAssembly + Web Workers 的现代浏览器（实际上等于所有当前浏览器）。

## 运维难度

**库路径低，Standalone 低到中。** 在已有的 Node/Bun 服务里用 `capjs-core` 基本就是接线活：实现（或复用）一个存储适配器，在 handler 之前加一次校验调用，再嵌上 widget。没有独立服务要看护。**Standalone** 路线则多出一个容器加一个 Redis/Valkey 实例要运行和备份、一个 `ADMIN_KEY` secret 要管理、跨站点的密钥轮换——是标准的小型服务运维，但比"插一段 script"要重。真正需要判断的是*难度调参*：调太低，PoW 几乎挡不住机器人；调太高，会拖累正常用户的设备。预期要按接口逐个调参、盯着滥用指标，而不是一劳永逸。

## 存疑（未验证）

- [未验证] 仓库活跃度与所谓热度（2026-06 约 7k GitHub stars）——GitHub stars 不可靠且对日期敏感，仅供参考。
- [未验证] "约 20 KB / 比 hCaptcha 小 250 倍"以及与 Altcha（约 34 KB）的体积对比，是项目自己 README/docs 里的营销数字，本页未独立复测。
- [未验证] 对比表里 Cap-vs-Altcha / vs-Anubis / vs-Turnstile 的定位取自 Cap 自己的文档；竞品当前能力（如 Altcha Sentinel、Turnstile 内部机制）未独立复核。
- [推断] License 判为 Apache-2.0：仓库 LICENSE 文件是逐字的 Apache 2.0 文本，但 GitHub API 报 `NOASSERTION`（文件头部非标准），自动 SPDX 检测器可能会标记。
- [未验证] 对真实打码服务 / 打码平台的实际抵抗效果本页未测；工作量证明抬高成本但可被足够算力或付费人工求解攻破。
- [推断] `capjs-core` 处于 v0.1.x，说明是年轻的、pre-1.0 的库面；API（存储接口、`validateToken` 选项）在版本间可能变化——请锁定版本。
- [未验证] Standalone 里的 MaxMind GeoIP 与无头浏览器检测在文档中被描述为可选特性，其确切行为/准确度未实测。
