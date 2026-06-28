# media-processing

> Category node. Decode/encode/transcode/filter audio & video (media frameworks & toolchains).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **FFmpeg** | Use it when you must decode/encode/transcode/filter virtually any audio or video in a pipeline — mind the LGPL→GPL build trap. | [→](ffmpeg.md) |
| **ffmpeg-python** | Python bindings for FFmpeg that let you build complex filter graphs as chained Python expressions instead of hand-writing `-filter_complex` strings — it constructs the FFmpeg command line for you and shells out to the `ffmpeg` binary. | [→](ffmpeg-python.md) |
| **VMAF** | Netflix's Emmy-winning perceptual video-quality metric — a C library `libvmaf` (plus a `vmaf` CLI and a Python wrapper) that scores how good a distorted/encoded video looks to a human vs a reference, and also implements PSNR, SSIM, MS-SSIM, PSNR-HVS, CIEDE2000 and the CAMBI banding detector. | [→](vmaf.md) |
| **m3u8** | A Python parser and serializer for HLS (HTTP Live Streaming) `.m3u8` playlists — load a playlist from a URL, file, or string into a typed object model, inspect/modify segments and variants, and dump it back out (RFC 8216). | [→](m3u8.md) |
| **ffsubsync** | A language-agnostic CLI that automatically re-times an out-of-sync subtitle file against the video (or a reference subtitle), aligning speech segments via FFT cross-correlation. | [→](ffsubsync.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [FFmpeg](ffmpeg.md) | ✅ | The universal media swiss-army-knife (CLIs + libav*); steep API and an LGPL/GPL build-licensing trap. |
| [ffmpeg-python](ffmpeg-python.md) | ✅ | Python bindings for FFmpeg that let you build complex filter graphs as chained Python expressions instead of hand-writing `-filter_complex` strings — it constructs the FFmpeg command line for you and shells out to the `ffmpeg` binary. |
| [VMAF](vmaf.md) | ✅ | Netflix's Emmy-winning perceptual video-quality metric — a C library `libvmaf` (plus a `vmaf` CLI and a Python wrapper) that scores how good a distorted/encoded video looks to a human vs a reference, and also implements PSNR, SSIM, MS-SSIM, PSNR-HVS, CIEDE2000 and the CAMBI banding detector. |
| [m3u8](m3u8.md) | ✅ | A Python parser and serializer for HLS (HTTP Live Streaming) `.m3u8` playlists — load a playlist from a URL, file, or string into a typed object model, inspect/modify segments and variants, and dump it back out (RFC 8216). |
| [ffsubsync](ffsubsync.md) | ✅ | A language-agnostic CLI that automatically re-times an out-of-sync subtitle file against the video (or a reference subtitle), aligning speech segments via FFT cross-correlation. |
| GStreamer / HandBrake / MLT / cloud transcoders | 未收录 | Other media frameworks/encoders named across the pages. |

## What belongs here

Frameworks/tools whose primary job is **processing media** — decode, encode, transcode, mux, filter. Not downloading media from sites (see `media-download`), not non-linear video editors as the main use case.
