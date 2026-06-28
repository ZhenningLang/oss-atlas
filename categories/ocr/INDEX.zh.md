# ocr

> 分类节点。光学字符识别引擎——图像/扫描件转文本。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Tesseract** | 当你需要离线、可嵌入、覆盖 100+ 语言、面向清晰印刷文本的 OCR 时用它——不适合野外照片或手写。 | [→](tesseract.zh.md) |
| **LaTeX-OCR (pix2tex)** | 当你要把数学公式图片转成 LaTeX(pix2tex)时用它——只管公式、已放缓，VLM 可能更强。 | [→](latex-ocr.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Tesseract](tesseract.zh.md) | ✅ | 面向清晰印刷文本的成熟离线 OCR 引擎；对版面、手写、野外照片较弱。 |
| [LaTeX-OCR (pix2tex)](latex-ocr.zh.md) | ✅ | 当你要把数学公式图片转成 LaTeX(pix2tex)时用它——只管公式、已放缓，VLM 可能更强。 |
| PaddleOCR / EasyOCR / TrOCR / Cloud Vision / Textract | 未收录 | 各页对比里点到的深度学习/云端 OCR(对杂乱输入更强)。 |

## 什么该放这里

主要职责是**识别图像/扫描件中文字**的引擎/库。不含面向 gen-AI 的文档版面与表格解析(见 `document-parsing`)，不含文档归档/检索(见 `document-management`)。
