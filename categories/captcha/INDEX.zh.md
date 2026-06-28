# captcha

> 分类节点。CAPTCHA / 机器人检测挑战(工作量证明、点击、行为式)。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Cap** | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明(Rust→WASM worker 做 SHA-256 nonce 搜索)发放服务端可校验 token——无图片、不调第三方。 | [→](capjs.zh.md) |
| **Text_select_captcha** | 一个中文深度学习库，用于识别**点选/文字点选验证码**——给一张"按顺序点这些字"的图，它用 YOLO 检测候选字形、用孪生网络（Siamese）把它们与提示匹配，返回点击坐标。 | [→](text-select-captcha.zh.md) |
| **pytorch-captcha-recognition** | 一个小巧的 PyTorch 示例，训练一个"端到端"CNN 来识别**定长图片验证码**（如 4 位数字/字母数字码），一次性把所有字符分类——一个学习/参考项目，最后更新于 2020 年。 | [→](pytorch-captcha-recognition.zh.md) |
| **captcha (lepture)** | 一个小巧的 Python 库，把你给定的字符串渲染成扭曲的图片验证码，或合成语音验证码——挑战文本、存储和校验都归你管，它只负责画图和发声。 | [→](lepture-captcha.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Cap](capjs.zh.md) | ✅ | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明(Rust→WASM worker 做 SHA-256 nonce 搜索)发放服务端可校验 token——无图片、不调第三方。 |
| [Text_select_captcha](text-select-captcha.zh.md) | ✅ | 一个中文深度学习库，用于识别**点选/文字点选验证码**——给一张"按顺序点这些字"的图，它用 YOLO 检测候选字形、用孪生网络（Siamese）把它们与提示匹配，返回点击坐标。 |
| [pytorch-captcha-recognition](pytorch-captcha-recognition.zh.md) | ✅ | 一个小巧的 PyTorch 示例，训练一个"端到端"CNN 来识别**定长图片验证码**（如 4 位数字/字母数字码），一次性把所有字符分类——一个学习/参考项目，最后更新于 2020 年。 |
| [captcha (lepture)](lepture-captcha.zh.md) | ✅ | 一个小巧的 Python 库，把你给定的字符串渲染成扭曲的图片验证码，或合成语音验证码——挑战文本、存储和校验都归你管，它只负责画图和发声。 |
| hCaptcha / Cloudflare Turnstile / Friendly Captcha / Altcha | 未收录 | 页面里点到的其他 CAPTCHA / 机器人检测服务。 |

## 什么该放这里

**CAPTCHA / 机器人检测**挑战系统——工作量证明、点击或行为式。本宽泛索引里的一个独立领域。
