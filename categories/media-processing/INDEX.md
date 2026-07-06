# media-processing

> Category node. Decode/encode/transcode/filter audio & video (media frameworks & toolchains).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FFmpeg** | Use it when you must decode/encode/transcode/filter virtually any audio or video in a pipeline — mind the LGPL→GPL build trap. | A (3/6) | [→](ffmpeg.md) |
| **HandBrake** | Use it when you need a preset-driven GUI or CLI to rip/transcode video to modern MP4/MKV with H.264/H.265 — but it's an end-user app, not a library, and far narrower than raw FFmpeg. | — | [→](handbrake.md) |
| **ffmpeg-python** | Use it when you're scripting complex FFmpeg filter graphs in Python and want readable DAG code instead of write-only -filter_complex strings — but it's coasting since 2024, single-maintainer, and still needs the ffmpeg binary installed. | C (4/6) | [→](ffmpeg-python.md) |
| **PyAV** | Use it when you need programmatic, in-process access to video/audio frames as NumPy arrays from Python — but it's lower-level than a CLI wrapper and heavier to install (Cython compilation against FFmpeg headers). | — | [→](pyav.md) |
| **VMAF** | Use it when you're tuning an encoding ladder and need a perceptual 0-100 score to compare codecs/presets the way the industry does — but it's full-reference only, and picking the wrong model silently invalidates cross-version comparisons. | B (5/6) | [→](vmaf.md) |
| **SSIMULACRA2** | Use it when you're benchmarking image codecs (JPEG XL, AVIF, WebP) and need a perceptual quality score that correlates with human subjective ratings — but it's image-only, asymmetric, and lacks the adoption of VMAF. | — | [→](ssimulacra2.md) |
| **m3u8** | Use it when you must parse or rewrite HLS .m3u8 manifests programmatically as a typed object model rather than regex — but it's Python-only, HLS-specific, and quiet since 2025 so the newest rfc8216bis tags may lag. | C (3/6) | [→](m3u8.md) |
| **ffsubsync** | Use it when a subtitle file is off by a constant global offset and you want one-command FFT audio-sync without manual sync points — but it can't fix per-line/variable drift inside the content, and it's single-maintainer. | B (6/6) | [→](ffsubsync.md) |
| **MoviePy** | Use it when you want a friendly Python API for programmatic video editing — cutting, compositing, text, effects — but it's batch-only, slower than raw FFmpeg for large files, and maintenance has slowed from its peak. | ? (0/6) | [→](moviepy.md) |
| **GStreamer** | Use it when you need a real-time, persistent, application-embedded audio/video pipeline framework — not a CLI tool — but accept a steep learning curve and plugin-dependency management. | — | [→](gstreamer.md) |
| **MLT** | Use it when you're building a custom video editor or automated editing pipeline that needs a timeline model — but it's a framework, not a ready-to-use NLE, and the actual codec work is delegated to FFmpeg. | — | [→](mlt.md) |
| **OpenAI Whisper** | Use it when you need general-purpose multilingual speech-to-text transcription or translation to English from audio/video files — but it's not real-time by default, large models are slow on CPU, and it hallucinates on non-speech content. | — | [→](whisper.md) |
| **sharp** | High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library. | ? (0/6) | [→](sharp.md) |
| **ImageMagick** | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. | ? (0/6) | [→](imagemagick.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.md) | ✅ | A (3/6) | The universal media swiss-army-knife (CLIs + libav*); steep API and an LGPL/GPL build-licensing trap. |
| [HandBrake](handbrake.md) | ✅ | — | Preset-driven GUI and CLI for ripping/transcoding to modern MP4/MKV; end-user app, not a library, far narrower than raw FFmpeg. |
| [ffmpeg-python](ffmpeg-python.md) | ✅ | C (4/6) | Use it when you're scripting complex FFmpeg filter graphs in Python and want readable DAG code instead of write-only -filter_complex strings — but it's coasting since 2024, single-maintainer, and still needs the ffmpeg binary installed. |
| [PyAV](pyav.md) | ✅ | — | Pythonic bindings to FFmpeg's libav* libraries — in-process decode/encode with frame-by-frame NumPy array access; lower-level and heavier to install than a CLI wrapper. |
| [VMAF](vmaf.md) | ✅ | B (5/6) | Use it when you're tuning an encoding ladder and need a perceptual 0-100 score to compare codecs/presets the way the industry does — but it's full-reference only, and picking the wrong model silently invalidates cross-version comparisons. |
| [SSIMULACRA2](ssimulacra2.md) | ✅ | — | Use it when you're benchmarking image codecs (JPEG XL, AVIF, WebP) and need a perceptual quality score that correlates with human subjective ratings — but it's image-only, asymmetric, and lacks the adoption of VMAF. |
| [m3u8](m3u8.md) | ✅ | C (3/6) | Use it when you must parse or rewrite HLS .m3u8 manifests programmatically as a typed object model rather than regex — but it's Python-only, HLS-specific, and quiet since 2025 so the newest rfc8216bis tags may lag. |
| [ffsubsync](ffsubsync.md) | ✅ | B (6/6) | Use it when a subtitle file is off by a constant global offset and you want one-command FFT audio-sync without manual sync points — but it can't fix per-line/variable drift inside the content, and it's single-maintainer. |
| [MoviePy](moviepy.md) | ✅ | ? (0/6) | Use it when you want a friendly Python API for programmatic video editing — cutting, compositing, text, effects — but it's batch-only, slower than raw FFmpeg for large files, and maintenance has slowed from its peak. |
| [GStreamer](gstreamer.md) | ✅ | — | A pipeline-based multimedia framework for real-time, persistent, application-embedded audio/video processing — not a CLI tool. Steep learning curve, strong in embedded Linux and GTK apps. |
| [MLT](mlt.md) | ✅ | — | A multimedia framework for building non-linear video editors with a timeline model — not a standalone editor, and delegates all codec work to FFmpeg underneath. Use Shotcut or Kdenlive if you want a ready-made NLE. |
| [OpenAI Whisper](whisper.md) | ✅ | — | General-purpose multilingual speech-to-text transcription and translation to English from audio/video. Not real-time by default, large models need GPU, and hallucinates on non-speech content. |

## What belongs here

Frameworks/tools whose primary job is **processing media** — decode, encode, transcode, mux, filter. Not downloading media from sites (see `media-download`), not non-linear video editors as the main use case.
