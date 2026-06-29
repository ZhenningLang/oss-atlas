# media-processing

> Category node. Decode/encode/transcode/filter audio & video (media frameworks & toolchains).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FFmpeg** | Use it when you must decode/encode/transcode/filter virtually any audio or video in a pipeline — mind the LGPL→GPL build trap. | A (3/6) | [→](ffmpeg.md) |
| **ffmpeg-python** | Use it when you're scripting complex FFmpeg filter graphs in Python and want readable DAG code instead of write-only -filter_complex strings — but it's coasting since 2024, single-maintainer, and still needs the ffmpeg binary installed. | C (4/6) | [→](ffmpeg-python.md) |
| **VMAF** | Use it when you're tuning an encoding ladder and need a perceptual 0-100 score to compare codecs/presets the way the industry does — but it's full-reference only, and picking the wrong model silently invalidates cross-version comparisons. | B (5/6) | [→](vmaf.md) |
| **m3u8** | Use it when you must parse or rewrite HLS .m3u8 manifests programmatically as a typed object model rather than regex — but it's Python-only, HLS-specific, and quiet since 2025 so the newest rfc8216bis tags may lag. | C (3/6) | [→](m3u8.md) |
| **ffsubsync** | Use it when a subtitle file is off by a constant global offset and you want one-command FFT audio-sync without manual sync points — but it can't fix per-line/variable drift inside the content, and it's single-maintainer. | B (6/6) | [→](ffsubsync.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.md) | ✅ | A (3/6) | The universal media swiss-army-knife (CLIs + libav*); steep API and an LGPL/GPL build-licensing trap. |
| [ffmpeg-python](ffmpeg-python.md) | ✅ | C (4/6) | Use it when you're scripting complex FFmpeg filter graphs in Python and want readable DAG code instead of write-only -filter_complex strings — but it's coasting since 2024, single-maintainer, and still needs the ffmpeg binary installed. |
| [VMAF](vmaf.md) | ✅ | B (5/6) | Use it when you're tuning an encoding ladder and need a perceptual 0-100 score to compare codecs/presets the way the industry does — but it's full-reference only, and picking the wrong model silently invalidates cross-version comparisons. |
| [m3u8](m3u8.md) | ✅ | C (3/6) | Use it when you must parse or rewrite HLS .m3u8 manifests programmatically as a typed object model rather than regex — but it's Python-only, HLS-specific, and quiet since 2025 so the newest rfc8216bis tags may lag. |
| [ffsubsync](ffsubsync.md) | ✅ | B (6/6) | Use it when a subtitle file is off by a constant global offset and you want one-command FFT audio-sync without manual sync points — but it can't fix per-line/variable drift inside the content, and it's single-maintainer. |
| GStreamer / HandBrake / MLT / cloud transcoders | 未收录 | — | Other media frameworks/encoders named across the pages. |

## What belongs here

Frameworks/tools whose primary job is **processing media** — decode, encode, transcode, mux, filter. Not downloading media from sites (see `media-download`), not non-linear video editors as the main use case.
