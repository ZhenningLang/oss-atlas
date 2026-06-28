# captcha

> Category node. CAPTCHA / bot-detection challenges (proof-of-work, click, behavioral).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Cap** | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. | [→](capjs.md) |
| **Text_select_captcha** | A Chinese deep-learning library for **click/text-select CAPTCHA** recognition — given an image that asks "click these characters in order", it detects the candidate glyphs (YOLO) and matches them to the prompt (Siamese network), returning the click coordinates. | [→](text-select-captcha.md) |
| **pytorch-captcha-recognition** | A small PyTorch example that trains an "end-to-end" CNN to read **fixed-length image CAPTCHAs** (e.g. 4-character digit/alphanumeric codes), classifying all characters at once — a learning/reference project, last updated 2020. | [→](pytorch-captcha-recognition.md) |
| **captcha (lepture)** | A small Python library that renders distorted image CAPTCHAs and synthesizes audio CAPTCHAs from a string you supply — you own the challenge text, storage, and verification; it only draws and speaks. | [→](lepture-captcha.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Cap](capjs.md) | ✅ | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. |
| [Text_select_captcha](text-select-captcha.md) | ✅ | A Chinese deep-learning library for **click/text-select CAPTCHA** recognition — given an image that asks "click these characters in order", it detects the candidate glyphs (YOLO) and matches them to the prompt (Siamese network), returning the click coordinates. |
| [pytorch-captcha-recognition](pytorch-captcha-recognition.md) | ✅ | A small PyTorch example that trains an "end-to-end" CNN to read **fixed-length image CAPTCHAs** (e.g. 4-character digit/alphanumeric codes), classifying all characters at once — a learning/reference project, last updated 2020. |
| [captcha (lepture)](lepture-captcha.md) | ✅ | A small Python library that renders distorted image CAPTCHAs and synthesizes audio CAPTCHAs from a string you supply — you own the challenge text, storage, and verification; it only draws and speaks. |
| hCaptcha / Cloudflare Turnstile / Friendly Captcha / Altcha | 未收录 | Other CAPTCHA / bot-detection services named on the page. |

## What belongs here

**CAPTCHA / bot-detection** challenge systems — proof-of-work, click, or behavioral. A standalone domain in this broad index.
