# media-processing

> 分类节点。解码/编码/转码/滤镜处理音视频(媒体框架与工具链)。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **FFmpeg** | 当你需要在管线里解码/编码/转码/滤镜处理几乎任何音视频时用它——注意 LGPL→GPL 的构建授权陷阱。 | [→](ffmpeg.zh.md) |
| **ffmpeg-python** | FFmpeg 的 Python 绑定，让你把复杂的滤镜图写成链式 Python 表达式，而不必手搓 `-filter_complex` 字符串——它替你拼出 FFmpeg 命令行，再去调用 `ffmpeg` 二进制。 | [→](ffmpeg-python.zh.md) |
| **VMAF** | Netflix 的、获 Emmy 奖的感知视频质量指标——一个 C 库 `libvmaf`（外加一个 `vmaf` CLI 和一个 Python wrapper），用来评估失真/编码后的视频相对参考在人眼看来有多好，同时还实现了 PSNR、SSIM、MS-SSIM、PSNR-HVS、CIEDE2000 以及 CAMBI 色带检测器。 | [→](vmaf.zh.md) |
| **m3u8** | 一个面向 HLS（HTTP Live Streaming）`.m3u8` 播放列表的 Python 解析器与序列化器——把来自 URL、文件或字符串的播放列表加载成一个类型化对象模型，查看/修改 segment 与变体，再 dump 回去（RFC 8216）。 | [→](m3u8.zh.md) |
| **ffsubsync** | 一个语言无关的命令行工具，把时间轴对不上的字幕文件自动重新对齐到视频（或一份参考字幕）上，靠 FFT 互相关来对齐语音段。 | [→](ffsubsync.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [FFmpeg](ffmpeg.zh.md) | ✅ | 通用媒体瑞士军刀(CLI + libav*);API 陡峭，且有 LGPL/GPL 构建授权陷阱。 |
| [ffmpeg-python](ffmpeg-python.zh.md) | ✅ | FFmpeg 的 Python 绑定，让你把复杂的滤镜图写成链式 Python 表达式，而不必手搓 `-filter_complex` 字符串——它替你拼出 FFmpeg 命令行，再去调用 `ffmpeg` 二进制。 |
| [VMAF](vmaf.zh.md) | ✅ | Netflix 的、获 Emmy 奖的感知视频质量指标——一个 C 库 `libvmaf`（外加一个 `vmaf` CLI 和一个 Python wrapper），用来评估失真/编码后的视频相对参考在人眼看来有多好，同时还实现了 PSNR、SSIM、MS-SSIM、PSNR-HVS、CIEDE2000 以及 CAMBI 色带检测器。 |
| [m3u8](m3u8.zh.md) | ✅ | 一个面向 HLS（HTTP Live Streaming）`.m3u8` 播放列表的 Python 解析器与序列化器——把来自 URL、文件或字符串的播放列表加载成一个类型化对象模型，查看/修改 segment 与变体，再 dump 回去（RFC 8216）。 |
| [ffsubsync](ffsubsync.zh.md) | ✅ | 一个语言无关的命令行工具，把时间轴对不上的字幕文件自动重新对齐到视频（或一份参考字幕）上，靠 FFT 互相关来对齐语音段。 |
| GStreamer / HandBrake / MLT / 云转码 | 未收录 | 各页对比里点到的其他媒体框架/编码器。 |

## 什么该放这里

主要职责是**处理媒体**——解码、编码、转码、封装、滤镜——的框架/工具。不含从站点下载媒体(见 `media-download`)，不含以非线性视频剪辑为主用途的编辑器。
