# dev-utilities

> 分类节点。独立开发者工具、数据处理瑞士军刀与可自托管的基础设施。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **DevToys** | 想把 Base64/JSON/哈希/diff 等开发小工具离线本地化、收进一个跨平台桌面应用、不再用不可信在线网站时，用它。 | B（4/6） | [→](devtoys.zh.md) |
| **CyberChef** | 当你需要在浏览器里离线串联编解码、加解密、压缩和数据分析变换、且数据不能外发时用它。 | B（6/6） | [→](cyberchef.zh.md) |
| **Cockpit** | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 | D（5/6） | [→](cockpit.zh.md) |
| **Telegraf** | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 | A（5/6） | [→](telegraf.zh.md) |
| **OpenZL** | 当你要把 TB 级的某种高度结构化/数值格式压得比通用 zstd 更狠时使用。 | B（4/6） | [→](openzl.zh.md) |
| **Certbot** | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 | A（5/6） | [→](certbot.zh.md) |
| **tqdm** | 当你想给 Python 循环/CLI/notebook 加一个快速、低开销的进度条时用它。 | B（5/6） | [→](tqdm.zh.md) |
| **SlimToolkit** | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 | B（5/6） | [→](slim.zh.md) |
| **Faker (faker-js)** | 当你需要在 JS/TS 里生成逼真的假/mock 数据（姓名、地址、金融…）用于测试和填充时用它。 | A（5/6） | [→](faker-js.zh.md) |
| **fontTools** | 当你需要对字体做程序化处理——子集化网页字体、转格式、查改表——时用它——但它只编辑字体文件，不绘制字形也不做文字排版。 | A（6/6） | [→](fonttools.zh.md) |
| **Flashlight** | 当你在维护一台 10.10–10.15 的老 macOS、想给 Spotlight 加插件时用它——但它自 2020 年起已弃，且需关闭 SIP，日常机器上别碰。 | E（3/6） | [→](flashlight.zh.md) |
| **IdeaVim** | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 | B（5/6） | [→](ideavim.zh.md) |
| **VS Code** | 当你需要一款快速、跨平台、具备智能补全、调试功能和最大扩展市场的代码编辑器时用它——但它是 Electron 应用，且分发版包含微软遥测。 | ?（0/6） | [→](vscode.zh.md) |
| **Clash Verge Rev** | 当你想要一款现代化的跨平台 GUI 代理客户端，支持基于规则的路由、内置 mihomo 内核和 TUN 模式时用它——但仅限桌面端且为 GPL-3.0 许可。 | ?（0/6） | [→](clash-verge-rev.zh.md) |
| **RustDesk** | 当你需要一款开源、自托管的跨平台远程桌面来访问自己的机器时用它——但需要自己管理中继服务器或接受 P2P 局限。 | ?（0/6） | [→](rustdesk.zh.md) |
| **Tauri** | 当你想用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用，替代 Electron 时用它。 | ?（0/6） | [→](tauri.zh.md) |
| **Deno** | 当你想要一个具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JavaScript/TypeScript 运行时，无需 node_modules 时用它。 | ?（0/6） | [→](deno.zh.md) |
| **Vaultwarden** | 当你想要一款自托管的、Rust 编写的 Bitwarden 兼容密码管理器时用它——但它是非官方实现，AGPL-3.0 许可，且核心维护者为单人。 | ?（0/6） | [→](vaultwarden.zh.md) |
| **Bun** | 当你想要一个极速一体化 JavaScript/TypeScript 工具集（运行时、打包器、测试运行器、包管理器）集成在单个二进制文件中时用它——但商用前请核实许可证。 | ?（0/6） | [→](bun.zh.md) |
| **Zed** | 当你想要一个高性能原生代码编辑器，支持实时多人协作时用它——但它的扩展生态远小于 VS Code，且仅约 4 年历史。 | ?（0/6） | [→](zed.zh.md) |
| **ripgrep** | 当你需要一个快速、智能、跨平台的搜索工具，默认遵守 gitignore，且在 Windows、macOS 和 Linux 上行为一致时用它。 | ?（0/6） | [→](ripgrep.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [DevToys](devtoys.zh.md) | ✅ | B（4/6） | 想把 Base64/JSON/哈希/diff 等开发小工具离线本地化、收进一个跨平台桌面应用、不再用不可信在线网站时，用它。 |
| [CyberChef](cyberchef.zh.md) | ✅ | B（6/6） | 当你需要在浏览器里离线串联编解码、加解密、压缩和数据分析变换、且数据不能外发时用它。 |
| [Cockpit](cockpit.zh.md) | ✅ | D（5/6） | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 |
| [Telegraf](telegraf.zh.md) | ✅ | A（5/6） | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 |
| [OpenZL](openzl.zh.md) | ✅ | B（4/6） | 当你要把 TB 级的某种高度结构化/数值格式压得比通用 zstd 更狠时使用。 |
| [Certbot](certbot.zh.md) | ✅ | A（5/6） | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 |
| [tqdm](tqdm.zh.md) | ✅ | B（5/6） | 当你想给 Python 循环/CLI/notebook 加一个快速、低开销的进度条时用它。 |
| [SlimToolkit](slim.zh.md) | ✅ | B（5/6） | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 |
| [Faker (faker-js)](faker-js.zh.md) | ✅ | A（5/6） | 当你需要在 JS/TS 里生成逼真的假/mock 数据（姓名、地址、金融…）用于测试和填充时用它。 |
| [fontTools](fonttools.zh.md) | ✅ | A（6/6） | 当你需要对字体做程序化处理——子集化网页字体、转格式、查改表——时用它——但它只编辑字体文件，不绘制字形也不做文字排版。 |
| [Flashlight](flashlight.zh.md) | ✅ | E（3/6） | 当你在维护一台 10.10–10.15 的老 macOS、想给 Spotlight 加插件时用它——但它自 2020 年起已弃，且需关闭 SIP，日常机器上别碰。 |
| [IdeaVim](ideavim.zh.md) | ✅ | B（5/6） | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 |
| [VS Code](vscode.zh.md) | ✅ | ?（0/6） | 轻量但强大的跨平台代码编辑器，拥有最大的扩展市场；基于 Electron，微软分发版包含遥测。 |
| [Clash Verge Rev](clash-verge-rev.zh.md) | ✅ | ?（0/6） | 现代化跨平台 GUI 代理客户端，支持基于规则的路由与内置 mihomo 内核；仅限桌面端且为 GPL-3.0 许可。 |
| [RustDesk](rustdesk.zh.md) | ✅ | ?（0/6） | 开源跨平台自托管远程桌面；需要自己管理中继服务器或接受 P2P 局限。 |
| [Tauri](tauri.zh.md) | ✅ | ?（0/6） | 用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用；Electron 的替代方案。 |
| [Deno](deno.zh.md) | ✅ | ?（0/6） | 具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JS/TS 运行时；无需 node_modules，但生态比 Node.js 小。 |
| [Vaultwarden](vaultwarden.zh.md) | ✅ | ?（0/6） | 自托管的 Rust 版 Bitwarden 兼容密码管理器；非官方、AGPL-3.0、单人核心维护者模式。 |
| [Zed](zed.zh.md) | ✅ | ?（0/6） | 由 Atom 创作者打造的高性能原生代码编辑器，支持实时多人协作；扩展生态远小于 VS Code，仅约 4 年历史。 |
| [ripgrep](ripgrep.zh.md) | ✅ | ?（0/6） | 快速、感知 gitignore 的面向行搜索工具，跨平台支持一流；10 年历史，Lindy 信号强劲，单人维护但可靠性高。 |
| [Bun](bun.zh.md) | ✅ | ?（0/6） | 极速一体化 JS/TS 工具集（运行时、打包器、测试运行器、包管理器）；单二进制文件，但许可证为自定义 NOASSERTION，且比 Node.js/Deno 年轻。 |

## 什么该放这里

不归入更窄的 AI/agent 分类的**通用独立开发者工具与可自托管基础设施**——编码器、管理界面、采集器、压缩器。一个刻意宽泛的兜底分类；溢出时再拆子分类。
