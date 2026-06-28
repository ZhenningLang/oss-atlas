---
name: Tesseract
slug: tesseract
repo: https://github.com/tesseract-ocr/tesseract
category: ocr
tags: [ocr, text-recognition, lstm, libtesseract, document, cli, offline]
language: C++
license: Apache-2.0
maturity: v5.5.2, active (2026-06), ~75.0k stars
last_verified: 2026-06-28
type: library
---

# Tesseract

经典的开源 OCR 引擎：一个 C++ 的 `libtesseract` 库加一个命令行程序，把文字图片转成可读文本，完全离线运行，通过单独下载的训练数据支持 100+ 种语言。

## 何时使用

你是后端开发者，要给文档管线接上 OCR——一批来自档案系统的扫描 PDF、传真和 TIFF，大多是几种已知语言的清晰印刷体。你需要在自己的服务器上把文字抽出来(数据不出内网、不按页给云厂商付费)，而且要的是一个能嵌进代码的库调用，而不是一个要 POST 过去的 SaaS。你装上 `tesseract` 二进制(或链接 `libtesseract`)，拉下你预期那几种语言的 `tessdata` 训练模型，再在 worker 里用 `pytesseract` 这种薄封装调它。对清晰、去倾斜、高 DPI 的印刷体扫描件，它无需 GPU、无需联网、Apache-2.0 宽松许可，就能干好这活——而且它输出的不只是纯文本，还有 hOCR、ALTO、PAGE、TSV 和可搜索 PDF，词级 bounding box 也留得住，方便下游建索引。

当你能掌控输入质量时，你也会选它。Tesseract 吃预处理这一套：二值化、去倾斜、去噪，喂给它 300 DPI 的行图，默认(v4 起)的 LSTM 行识别器既准又便宜，能在一群 CPU worker 上规模化跑。某种语言或字体覆盖不好时，它可训练——你可以微调或自建 `tessdata`——所以一条长期存在、面向可预测文档类型的内部管线，正是它的甜区。

## 何时不用

- **野外照片、复杂版式或手写体。** 这是最锋利的边界：Tesseract 假定输入是清晰、以印刷体为主、大致去倾斜的文本。面对带透视和不均匀光照的手机照片、报刊那种多栏版式、或任何手写，现代深度学习 OCR——PaddleOCR、EasyOCR、云端 Vision/Textract、TrOCR——通常大幅胜出。[推断]
- **你不想背预处理负担。** 准确率高度依赖输入质量；README 自己就说你常常得先*改善图像*。如果你没法投入二值化/去倾斜/DPI 归一化，结果会让你失望。
- **你需要文档版式、表格或阅读顺序。** Tesseract 的页面切分很基础——它是文字*识别器*，不是版式/表格/结构抽取器。要解析文档结构(表格、分栏、阅读顺序、键值)，请在 OCR 之上(或替代它)加一层文档解析，比如 docling(`未收录`)。
- **你需要 LaTeX / 数学公式识别。** Tesseract 不懂数学记号；请用专门工具，比如 LaTeX-OCR(`未收录`)。
- **你想要开箱即用的 GUI 或端到端应用。** 它不带 GUI——它是引擎加 CLI。前端(比如 OCRmyPDF 那类封装)得你自己配。

## 横向对比

| 替代品 | 是否收录 | 取舍 |
|---|---|---|
| PaddleOCR | 未收录 | 深度学习 OCR + 版式/表格/结构模型；在复杂版式、照片和中日韩上强得多，但依赖更重(PaddlePaddle)、Apache-2.0、有 GPU 更好——是完整管线，而非 Tesseract 的单一识别器。 |
| EasyOCR | 未收录 | 基于 PyTorch,80+ 语言，安装简单，对场景/照片文字开箱即用效果不错；运行时更大、偏 GPU，在极端规模下不如 Tesseract 的 C++ 内核久经考验。 |
| Google Cloud Vision / AWS Textract | 未收录 | 托管云 OCR；对脏输入准确率一流，Textract 还能抽表格/表单，但按页计费、数据出内网、不能离线/自托管——和 Tesseract 的部署模型正相反。 |
| TrOCR | 未收录 | 微软的 Transformer(编码器-解码器)OCR；在手写和难行上很强，但模型重、偏 GPU，且是行级识别，没有 Tesseract 那套完整的页面/格式工具。 |
| docTR | 未收录 | TF/PyTorch 的深度学习 OCR(检测+识别),Python API 干净；对多样版式比 Tesseract 好，但依赖更重、语言覆盖更小。 |

## 技术栈

- **语言：** C++(`libtesseract` 引擎与 `tesseract` CLI)；常通过 `pytesseract` 在 Python 里调用，也有多语言绑定。
- **识别引擎：** 基于 LSTM 的行识别器(Tesseract 4 起为默认)，同时保留较旧的字符模式"legacy"引擎以向后兼容。
- **训练数据：** 语言/字符集模型放在单独的 `tessdata` 文件里(有 `tessdata`、`tessdata_fast`、`tessdata_best` 几种)；模型不随引擎打包，需按语言单独下载。
- **输出格式：** 纯文本、hOCR(HTML)、可搜索/隐藏文字 PDF、TSV、ALTO、PAGE——可拿到词/行 bounding box，不只是扁平文本。
- **可训练：** 通过 Tesseract 训练工具支持训练/微调，以增加语言或字体。

## 依赖

- **`libtesseract`:** 你链接(或经 CLI 调用)的核心引擎。
- **Leptonica:** 必需的图像处理库——Tesseract 用它打开和处理输入图像。这是关键的构建/运行时依赖。
- **`tessdata` 模型：** 各语言/字符集的训练数据文件，单独下载；按需在 `tessdata_fast`(求快)和 `tessdata_best`(求准)之间选。[推断]
- **语言包：** 每种要识别的语言一个 `*.traineddata` 文件(如 `eng.traineddata`)；所请求语言的数据没装好时引擎会报错。
- **无 GPU、无网络、无数据存储：** 模型就位后纯 CPU、完全离线运行。

## 运维难度

**低到中。** 引擎本身好运维：一个 CPU 二进制，没有常驻服务、没有 GPU、没有网络，以 OS 包和 Docker 镜像分发。成本在两处。其一是**输入预处理**——要拿到可用准确率，你通常得在它前面搭一段二值化/去倾斜/去噪/DPI 归一化的处理，而大部分工程量和调参都落在这条管线(而非 Tesseract)上。其二是**模型管理**——你得为每种语言取来并版本化对应的 `tessdata`，还要在 `fast`/`best` 变体间做取舍，这是个部署产物层面的事。扩展是 CPU worker 间的尴尬并行，所以吞吐是扇出问题，不是集群问题。难的很少是跑 Tesseract；难的是把图像弄得够干净，让 Tesseract 跑得好。

## 存疑（未验证）

- [未验证] 截至 2026-06，仓库显示约 75.0k GitHub star、最新发布 v5.5.2(2025-12-26)——star 数对时间敏感，仅供参考。
- [未验证] "开箱 100+ 语言"和输出格式列表(hOCR/PDF/TSV/ALTO/PAGE)是 README 自己的表述；确切语言数量和各语言模型质量各有差异。
- [推断] 在复杂版式、照片和手写上与现代深度学习 OCR(PaddleOCR/EasyOCR/云端 Vision/TrOCR/docTR)的准确率差距，是从架构和常见基准做出的推断，不是对你具体文档的实测——请在你自己的数据上跑基准。
- [推断] `tessdata` / `tessdata_fast` / `tessdata_best` 变体及各语言 `*.traineddata` 的打包方式是按项目惯例描述的；请对照当前活跃仓库核实下载布局与所需版本兼容性。
- [推断] 页面切分/版式能力相对专门的文档解析工具被表述为"基础"；这是相对判断，不是对某个具体 PSM 模式的实测。
