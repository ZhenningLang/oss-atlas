# im-automation

> 分类节点。即时通讯机器人与自动化（微信等 IM 平台）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **ItChat** | 仅作为旧版微信机器人代码学习——已停更，且其依赖的网页协议已失效，基本不可用。 | C（4/6） | [→](itchat.zh.md) |
| **WeChatPlugin-MacOS** | 当前微信别用——一个 patch macOS 微信客户端二进制的小助手，每次微信更新就失效、已 ~2 年没动；有封号与安全风险。 | D（3/6） | [→](wechatplugin-macos.zh.md) |
| **wxpy** | 仅作为旧版微信机器人代码学习——2019 年起已归档，且基于已失效的微信网页协议，基本不可用。 | D（5/6） | [→](wxpy.zh.md) |
| **wxappUnpacker** | 当你需要把自有的微信小程序 .wxapkg 包反编译回可读源码时用它——但本仓库已被清空成墓碑，请改用仍存活的 fork。 | E（4/6） | [→](wxappunpacker.zh.md) |
| **Douyin-Bot** | 仅当你想要一份 ADB 屏幕坐标手机自动化的历史示例时用它——切勿部署，2018 年的硬编码坐标与失效的腾讯人脸 API 意味着它早已跑不通。 | D（3/6） | [→](douyin-bot.zh.md) |
| **WeChat Bot** | 当你需要仍在维护、支持多 IM 通道和多种 LLM 后端的 Node.js CLI，并接受非官方个人微信通道可能触发警告或封号时用它。 | B（5/6） | [→](wechat-bot.zh.md) |
| **ChatGPT-wechat-bot** | 只把它当作 2022 至 2023 年的精简 Wechaty／ChatGPT 参考；项目已停更、模型路径陈旧，个人微信号仍承担非官方 puppet 风险。 | D（3/6） | [→](chatgpt-wechat-bot.zh.md) |
| **OpeniLink Hub** | 当多个接入 iLink 的微信 Bot 需要自托管控制面、持久化、trace 和 App 时用它；项目很年轻，并明确声明与 iLink 官方团队没有关联或背书。 | B（5/6） | [→](openilink-hub.zh.md) |
| **Dify Enterprise WeChat Bot** | 只用于固定企业微信客户端版本的隔离 Windows 原型；消息链路含闭源二进制，Workflow 支持未完成，项目也已停滞。 | C（3/6） | [→](dify-enterprise-wechat-bot.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [ItChat](itchat.zh.md) | ✅ | C（4/6） | 仅作为旧版微信机器人代码学习——已停更，且其依赖的网页协议已失效，基本不可用。 |
| [WeChatPlugin-MacOS](wechatplugin-macos.zh.md) | ✅ | D（3/6） | 当前微信别用——一个 patch macOS 微信客户端二进制的小助手，每次微信更新就失效、已 ~2 年没动；有封号与安全风险。 |
| [wxpy](wxpy.zh.md) | ✅ | D（5/6） | 仅作为旧版微信机器人代码学习——2019 年起已归档，且基于已失效的微信网页协议，基本不可用。 |
| [wxappUnpacker](wxappunpacker.zh.md) | ✅ | E（4/6） | 当你需要把自有的微信小程序 .wxapkg 包反编译回可读源码时用它——但本仓库已被清空成墓碑，请改用仍存活的 fork。 |
| [Douyin-Bot](douyin-bot.zh.md) | ✅ | D（3/6） | 仅当你想要一份 ADB 屏幕坐标手机自动化的历史示例时用它——切勿部署，2018 年的硬编码坐标与失效的腾讯人脸 API 意味着它早已跑不通。 |
| [WeChat Bot](wechat-bot.zh.md) | ✅ | B（5/6） | 仍在维护的多通道 CLI 和模型 adapter，但非官方个人微信路径伴随账号警告与封禁风险。 |
| [ChatGPT-wechat-bot](chatgpt-wechat-bot.zh.md) | ✅ | D（3/6） | 小型历史 Wechaty／ChatGPT 示例，已经停更，仍依赖不受支持的个人号通道。 |
| [OpeniLink Hub](openilink-hub.zh.md) | ✅ | B（5/6） | 带持久化、trace 和 App 的年轻多 Bot 控制面，但没有 iLink 官方关联或背书。 |
| [Dify Enterprise WeChat Bot](dify-enterprise-wechat-bot.zh.md) | ✅ | C（3/6） | 固定版本 Windows 企业微信到 Dify 的桥接，helper 为闭源二进制，Workflow 通道也未完成。 |
| Wechaty / 企业微信官方 API / CowAgent / WeChatFerry / Dify-on-WeChat / OpeniLink SDK | 未收录 | — | 各页提到的 framework、官方通道、客户端注入与专用 SDK 替代方案。 |

## 什么该放这里

面向**即时通讯平台**（微信等 IM）的机器人与自动化。不含 Web/浏览器自动化（见 `web-automation`），不含团队聊天应用（见 `team-chat`）。
