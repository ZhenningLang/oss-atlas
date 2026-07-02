---
name: Stable Diffusion WebUI
slug: stable-diffusion-webui
repo: https://github.com/AUTOMATIC1111/stable-diffusion-webui
category: on-device-ml
tags: [diffusion-model, image-generation, gradio, pytorch, gpu, local-inference]
language: Python
license: AGPL-3.0
maturity: v1.x, active, 164k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-03-02T07:00:53Z
  default_branch: master
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T12:43:31Z
  overall: "?"
  overall_score: null
  scored_axes: 0
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    maintenance: { reason: recency_unreadable }
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    longevity: { reason: not_found }
    governance: { reason: empty_or_gated }
    risk_license: { reason: repo_unreachable }
---

# Stable Diffusion WebUI

A web-based interface for Stable Diffusion image generation, built with Gradio, offering txt2img, img2img, inpainting, outpainting, upscaling, and a rich plugin ecosystem for local GPU inference.

![Stable Diffusion WebUI — health radar](../../assets/health/stable-diffusion-webui.svg)

## When to use

You're a creator, researcher, or developer who wants to generate images from text prompts or edit existing images using diffusion models on your own hardware. You need a local web UI where you can write prompts, tweak sampling parameters, do inpainting to remove or add objects, run img2img for style transfer, and train custom embeddings with textual inversion. You pick Stable Diffusion WebUI over ComfyUI because you want a conventional tabbed interface rather than a node graph; you choose it over InvokeAI because its extension ecosystem is larger and more documented; you prefer it over Fooocus because you need full parameter control rather than simplified presets. You have an NVIDIA GPU with at least 6–8 GB of VRAM and are comfortable installing Python packages and managing model checkpoints. You install the WebUI, download a Stable Diffusion checkpoint, and open the browser tab to start generating — no cloud credits, no API keys, full control over the model and the outputs.

## When NOT to use

- **CPU-only inference.** If you have no GPU and need to run diffusion models, use a cloud API like Midjourney or DALL-E instead of Stable Diffusion WebUI, because running diffusion on CPU is excruciatingly slow (minutes per image) and this tool is designed for CUDA GPUs.
- **Commercial use without checking AGPL-3.0.** If you need a locally run diffusion tool with a less restrictive license for commercial derivatives, use ComfyUI (GPL-3.0, a different copyleft scope) or a cloud API instead of Stable Diffusion WebUI, because its AGPL-3.0 carries strong network copyleft obligations that may affect your distribution plans.
- **Zero-setup or non-technical users.** If you want a one-click consumer experience without managing Python, CUDA, and model weights, use Fooocus or a cloud service like Midjourney instead of Stable Diffusion WebUI, because installation requires Python, PyTorch, CUDA drivers, and managing multi-gigabyte model files.
- **Team multi-user deployments.** If you need built-in RBAC, queue management, or user isolation for a shared server, use ComfyUI (which has better queue management) or a hosted cloud API instead of Stable Diffusion WebUI, because it has no native multi-user isolation and concurrent users will interfere with each other's jobs and settings.
- **Managed cloud preference.** If you want a hosted API without managing GPUs, drivers, and model files, use Midjourney, DALL-E, or a Stable Diffusion API service instead of Stable Diffusion WebUI, because it is strictly self-hosted.
- **Strict reproducibility needs.** If you need reproducible, version-controlled workflows across machines, use ComfyUI with its JSON workflow export or Diffusers (Hugging Face) programmatically instead of Stable Diffusion WebUI, because the WebUI exposes hundreds of parameters, sampler choices, and extension interactions that make exact reproduction across different PyTorch/CUDA versions difficult.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [ComfyUI](comfyui.md) | ✅ | Node-based modular workflow engine for diffusion. | ComfyUI offers deeper customization through node graphs and better for batch pipelines; WebUI is more approachable for casual exploration and has a simpler tabbed interface. |
| InvokeAI | 未收录 | Polished creative canvas with unified canvas and layer support. | More focused on the artistic workflow with a built-in canvas; less extension-heavy than WebUI. |
| Fooocus | 未收录 | Simplified one-click UI focused on ease of use. | Stripped-down presets and minimal controls; good for beginners but limiting for advanced users. |
| DiffusionBee | 未收录 | macOS-native desktop app for Stable Diffusion. | No command-line or extension ecosystem; Apple Silicon optimized but platform-locked. |
| Midjourney / DALL-E | 未收录 | Closed-source cloud-only image generation services. | Proprietary models, subscription-based, no local control; WebUI is open-source and runs on your own GPU. |

## Tech stack

- **Python** — primary implementation language
- **Gradio** — web UI framework for the frontend
- **PyTorch** — deep learning framework for model inference
- **CUDA** — GPU acceleration via NVIDIA drivers
- **Stable Diffusion models** — community checkpoints, LoRAs, embeddings, and VAEs loaded at runtime

## Dependencies

- **NVIDIA GPU** with at least 6 GB VRAM (8 GB+ recommended for larger models and higher resolutions)
- **Python 3.10+** and matching PyTorch/CUDA versions
- **Model checkpoints** — multi-gigabyte `.safetensors` or `.ckpt` files downloaded from community hubs (e.g., Civitai, Hugging Face)
- **Optional: xformers** — for memory-efficient attention and speedups
- **Optional: GFPGAN, CodeFormer, RealESRGAN** — for face restoration and upscaling in the Extras tab

## Ops difficulty

**Medium.** Installation is a one-click script for basic setups, but the real burden is keeping the Python environment, PyTorch, CUDA drivers, and extension ecosystem compatible. Extension updates can break the WebUI after a `git pull`, and model files consume tens of gigabytes of disk space. GPU thermal management, VRAM limits, and batch-size tuning are ongoing concerns. For a personal workstation this is manageable; for a shared server or production pipeline, expect frequent troubleshooting.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance**: Active but last push was 2026-03, a few months before verification date. The project has a large open-issue backlog (2,493), suggesting both high usage and some strain on maintainer capacity.
- **Governance**: Owned by a single GitHub user (`AUTOMATIC1111`), not an organization. This creates a significant bus-factor risk; the project's continuity depends on one individual's continued involvement. [未验证]
- **Backing**: No corporate or foundation backing visible; funded by community donations and volunteer contributions.
- **Adoption**: Extremely popular (164k stars) and the de-facto standard local interface for Stable Diffusion. A vast ecosystem of extensions, models, and community tutorials exists.
- **Age & Lindy**: Created 2022-08 (~4 years old), which is young but has outlasted many AI-hype tools. It has been continuously active since launch, giving it a partial Lindy signal, though the 4-month gap since last push is worth monitoring.
- **Risk flags**: AGPL-3.0 copyleft license may affect commercial derivative use. Single-maintainer bus factor is the largest structural risk. The project also carries the general model-license risk: community checkpoints have their own licenses (some non-commercial) separate from the tool's AGPL-3.0.

## Caveats (unverified)

- [未验证] The exact maintenance status of the `AUTOMATIC1111` user account and their continued availability is not publicly documented; the bus factor is a genuine concern.
- [未验证] The 2026-03-02 last push date means there has been a ~4 month gap at verification time; verify current activity before assuming the project is still on its previous cadence.
- [未验证] Individual model checkpoints and extensions carry their own licenses and safety filters; the tool's AGPL-3.0 does not govern the weights you download.
- [推断] The 164k star count reflects both genuine popularity and the 2022–2023 AI art boom; some of that visibility is hype-driven rather than current active-user signal.
- [未验证] Specific VRAM requirements vary dramatically by model size, resolution, and enabled extensions; the "6–8 GB" figure is a rule of thumb, not a guarantee.
