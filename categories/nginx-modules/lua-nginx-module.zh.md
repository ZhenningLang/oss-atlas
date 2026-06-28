---
name: lua-nginx-module (ngx_lua)
slug: lua-nginx-module
repo: https://github.com/openresty/lua-nginx-module
category: nginx-modules
tags: [nginx, lua, luajit, openresty, web-server, scripting, cosocket]
language: C
license: BSD-2-Clause
maturity: v0.10.31 line, active, ~11.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
---

# lua-nginx-module (ngx_lua)

一个把 LuaJIT（或 Lua）虚拟机嵌入服务器的 NGINX 模块，让你在请求处理的每个阶段——rewrite、access、content、log——运行 Lua，并配一套非阻塞 cosocket API，使你的 Lua 能与上游 TCP/UDP 服务通信而不卡住 worker。

## 何时使用

你在 NGINX 之上构建网关/边缘逻辑——鉴权、请求整形、A/B 路由、动态上游选择、限流、自定义 header——你已经撞到了静态 `nginx.conf` 指令能表达的天花板。你不想为每次行为变更去写 C 模块再重编 NGINX，也不想只为做个路由决策就在请求路径上塞一个单独的应用服务器。你引入 `ngx_lua`（几乎总是通过 OpenResty 套件），于是这些逻辑都用 Lua 写：`access_by_lua_block { ... }` 拦请求、`content_by_lua_block { ... }` 直接出响应、`rewrite_by_lua` 改 URI——全部跑在 NGINX worker 内、带着 LuaJIT 的速度。

决定性的特性是 **cosocket** API：你的 Lua 能在请求中途对 Redis、数据库或某个内部 HTTP 服务开非阻塞 TCP/UDP 连接，`await` 结果再继续——而不阻塞事件循环。正是它把 NGINX 从静态代理变成可编程平台，也是 API 网关（Kong、APISIX）、WAF 和定制边缘逻辑的底座。当你想要 NGINX 的性能、又需要真正的逐请求可编程时，就选它。

## 何时不用

- **你只需要静态配置。** 若 `proxy_pass`、`map`、`limit_req` 之类已经表达了你的路由，再加一个 Lua VM 就是多余复杂度和新的故障面。配置能声明的就别去写脚本。
- **你不走 OpenResty/LuaJIT 路线。** 这个模块与特定 NGINX 版本和 LuaJIT 紧耦合；你几乎从不单独构建它——你用 OpenResty。把它 pin 到某个最前沿或厂商打过补丁的 NGINX 上很痛、也容易搞错。
- **在 Lua 里做阻塞 I/O。** 整个模型依赖 cosocket 和非阻塞调用。在处理器里调阻塞 C 库、`os.execute` 或同步 DB 驱动，会卡死整个 worker——刚接触事件模型的团队最容易踩的雷。
- **逐请求做 CPU 密集工作。** Lua 跑在 worker 里；逐请求做重型加密、大数据运算或长循环，会拖累该 worker 上所有人的延迟。把它下放给上游服务。
- **你想要开箱即用的网关。** 这是*基质*，不是产品。若你想要现成的路由、插件、鉴权和管理 API，请用基于它构建的网关（Kong/APISIX），而不是从裸 `ngx_lua` 拼一个。
- **对维护者集中度敏感。** 开发高度集中在 OpenResty 核心（见健康度）；对一个久经沙场的模块没问题，但若你需要广泛的独立治理，要掂量。

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| OpenResty（套件） | 未收录 | *打包发行*本模块外加 LuaJIT、lua-resty-* 库和一个匹配 NGINX 的完整发行版——实际上你就是这么消费 ngx_lua 的；本仓库是其中一个组件。 |
| njs（nginx JavaScript） | 未收录 | NGINX 官方脚本模块，用 JS 子集；第一方、安装更简单，但生态更小、不如 Lua/OpenResty 世界成熟。 |
| nginx C 模块 | 未收录 | 性能/控制力最强，但你要写 C 且每次变更都重编 NGINX——正是 ngx_lua 要消除的摩擦。 |
| Envoy + Lua/Wasm 过滤器 | 未收录 | 另一种代理，自带 Lua 和 WebAssembly 过滤模型；xDS/可观测性更丰富，运维比 NGINX+Lua 更重。 |
| Caddy + 插件（Go） | 未收录 | 基于 Go 的服务器，带插件模型和自动 TLS；语言/生态不同，边缘脚本深度不如 ngx_lua。 |
| [lua-resty-redis](lua-resty-redis.zh.md) | ✅ | 不是替代——是*跑在*本模块 cosocket API *之上*、用来连 Redis 的库；互补关系。 |

## 技术栈

- **语言：** C（NGINX 模块），嵌入 **LuaJIT**（首选）或标准 Lua 5.1。
- **执行模型：** 在 NGINX 请求各阶段挂 Lua 处理器（`set_by_lua`、`rewrite_by_lua`、`access_by_lua`、`content_by_lua`、`header_filter_by_lua`、`body_filter_by_lua`、`log_by_lua`，外加 `init_by_lua`/定时器）。
- **cosocket API：** 与 NGINX 事件循环集成的非阻塞 TCP/UDP socket——`lua-resty-*` 驱动生态的基础。
- **分发：** 编译期内建进 NGINX 二进制；实际上通过 OpenResty 套件消费（匹配的 NGINX + LuaJIT + lua-resty 库）。

## 依赖

- **一棵匹配的 NGINX 源码树**和 **ngx_devel_kit（NDK）**模块，一起编译——你是把本模块编进 NGINX，而非默认动态加载（动态模块构建可行，但对版本敏感）。[未验证]
- **LuaJIT**（推荐）或 Lua 5.1 的头文件/运行时，构建期需要。
- **实际上：OpenResty**——几乎所有人都消费预打包、版本匹配的发行版，而非手工把 NGINX + NDK + LuaJIT + 本模块接起来。
- **运行时：** 你的 Lua 通过 cosocket 连的东西（Redis、DB、HTTP 上游）——你自己跑。

## 运维难度

**中。** 日常它就跟 NGINX 一样跑——你运维一个服务进程，Lua 写在配置文件里。成本集中在边缘：（1）**构建**对版本敏感——模块 ⇄ NGINX ⇄ LuaJIT 版本必须对齐，这正是强烈建议用 OpenResty 套件（而非手工编译）的原因；（2）**编程模型不饶人**——处理器里一个阻塞调用就卡死一个 worker，团队必须理解 cosocket/非阻塞纪律；（3）**可观测性**——在请求路径里调试 Lua 需要 `lua_code_cache`、error-log 纪律，以及对 shared dict 状态的小心。升级意味着重新验证那个版本三元组。一旦稳定，它跑起来和 NGINX 本身一样无聊。

## 健康度与可持续性

- **维护（2026-06）——活跃。** 最后 push 在 **2026-06**；v0.10.31 / v0.10.32rc 线的 tag 较新。license 文件里 2009→2025 的版权年份和持续的 tag 都确认在继续干。未归档。**活跃。** [推断]
- **治理 / 背书。** `Organization` 所有（OpenResty / OpenResty Inc.，由章亦春 agentzh 创立）。开发**高度集中**在 OpenResty 核心团队（agentzh 及一小撮人主导贡献者）——是厂商/创始人主导而非基金会治理，即便团队真实存在，这仍是个 bus-factor 考量。[推断]
- **年龄 × Lindy。** 2010-04 创建（约 16 年）且**仍在活跃维护** ⇒ **极强 Lindy** 信号；它是广泛部署的网关（Kong、APISIX）底下的基础设施，熬过了每一代 NGINX。老而活跃，最安全的象限。[推断]
- **采用度。** 极广——是主流 API 网关和无数边缘部署底下的基质；约 393 个 open issue 反映的是一个庞大、长寿的表面，而非被忽视。许可为 BSD-2-Clause（从 README 许可小节读得），宽松，未发现 relicense 历史。[推断]
- **风险标记。** 创始人/核心团队集中度，以及与 NGINX/LuaJIT 的紧版本耦合，是真正的风险；非阻塞编程模型是运维上的雷，而非项目健康红旗。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 11.8k star / 约 393 open issue / 最后 push 2026-06，tag 在 v0.10.31–v0.10.32rc 附近——易变，请重新核实。
- [未验证] 许可：GitHub API 未返回 SPDX id（`license: null`）；README 的「Copyright and License」小节写明 **BSD**（2 句文本，版权 2009–2025 chaoslawful / agentzh / OpenResty Inc.）——此处依据阅读该小节记为 BSD-2-Clause，但未通过 API 定位到专门的 `LICENSE`/`COPYRIGHT` 文件。
- [未验证] 动态模块与静态编译的构建细节，以及确切的 NGINX/LuaJIT 版本矩阵，对版本敏感、此处未 pin；请查 OpenResty 套件文档。
- [推断]「核心团队集中 / 厂商主导治理」由贡献者列表和 OpenResty Inc. 的角色推断，而非已发布的治理文档。
