# media-processing

> 分类节点。解码/编码/转码/滤镜处理音视频（媒体框架与工具链）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FFmpeg** | 当你需要在管线里解码/编码/转码/滤镜处理几乎任何音视频时用它——注意 LGPL→GPL 的构建授权陷阱。 | A（3/6） | [→](ffmpeg.zh.md) |
| **HandBrake** | 当你需要预设驱动的 GUI 或 CLI 将视频转码/翻录为现代 MP4/MKV 配合 H.264/H.265 时用它——但它是终端用户应用，不是库，且远比原生 FFmpeg 窄。 | — | [→](handbrake.zh.md) |
| **ffmpeg-python** | 当你想用 Python 编排复杂的 FFmpeg 滤镜图、把不可读的 -filter_complex 字符串换成可读的 DAG 代码时用它——但它自 2024 年起停更、仅单人维护，且仍依赖系统已装 ffmpeg 二进制。 | C（4/6） | [→](ffmpeg-python.zh.md) |
| **PyAV** | 当你需要在 Python 中以进程内方式把视频/音频帧作为 NumPy 数组进行程序化访问时用它——但它比 CLI 包装器更底层、安装更重（需要针对 FFmpeg 头文件编译 Cython 扩展）。 | — | [→](pyav.zh.md) |
| **VMAF** | 当你在调编码档位、需要用业界通用的 0—100 感知分对比编解码器与预设时用它——但它只支持全参考，且选错模型会悄悄让跨版本对比失效。 | B（5/6） | [→](vmaf.zh.md) |
| **SSIMULACRA2** | 当你需要对比图像编解码器（JPEG XL、AVIF、WebP）并需要一个与人类主观评分相关的感知质量分时用它——但它仅限图像，非对称，且采用度不及 VMAF。 | — | [→](ssimulacra2.zh.md) |
| **m3u8** | 当你需要把 HLS 的 .m3u8 清单当作带类型的对象模型来解析或改写、而非正则硬抠时用它——但它仅限 Python 与 HLS，且自 2025 年起沉寂，最新的 rfc8216bis 标签可能滞后。 | C（3/6） | [→](m3u8.zh.md) |
| **ffsubsync** | 当字幕整体存在恒定偏移、你想用一条命令做 FFT 音频对齐而不手动设同步点时用它——但它修不了内容内部的逐行／变动漂移，且仅单人维护。 | B（6/6） | [→](ffsubsync.zh.md) |
| **MoviePy** | 当你想用友好的 Python API 做程序化视频编辑——剪辑、合成、文字、特效——时用它——但它是纯离线批处理，对大文件比原生 FFmpeg 慢，且维护速度已从巅峰期下降。 | ?（0/6） | [→](moviepy.zh.md) |
| **GStreamer** | 当你需要实时、持久、嵌入应用的音视频管线框架而非 CLI 工具时用它——但要接受陡峭的学习曲线和插件依赖管理。 | — | [→](gstreamer.zh.md) |
| **MLT** | 当你需要构建自定义视频编辑器或需要时间线模型的自动化剪辑管线时用它——但它是框架，不是开箱即用的 NLE，且底层编解码工作委托给 FFmpeg。 | — | [→](mlt.zh.md) |
| **OpenAI Whisper** | 当你需要通用的多语言语音转文字转写或从音视频英译时用它——但它默认不是实时系统，大模型在 CPU 上很慢，且对非语音内容会幻觉。 | — | [→](whisper.zh.md) |
| **sharp** | High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library. | ?（0/6） | [→](sharp.zh.md) |
| **ImageMagick** | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. | ?（0/6） | [→](imagemagick.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.zh.md) | ✅ | A（3/6） | 通用媒体瑞士军刀（CLI + libav*）;API 陡峭，且有 LGPL/GPL 构建授权陷阱。 |
| [HandBrake](handbrake.zh.md) | ✅ | — | 预设驱动的 GUI 与 CLI，用于翻录/转码为现代 MP4/MKV；终端用户应用，不是库，远比原生 FFmpeg 窄。 |
| [ffmpeg-python](ffmpeg-python.zh.md) | ✅ | C（4/6） | 当你想用 Python 编排复杂的 FFmpeg 滤镜图、把不可读的 -filter_complex 字符串换成可读的 DAG 代码时用它——但它自 2024 年起停更、仅单人维护，且仍依赖系统已装 ffmpeg 二进制。 |
| [PyAV](pyav.zh.md) | ✅ | — | 面向 FFmpeg 的 libav* 库的 Pythonic 绑定——在进程内完成解码/编码，可逐帧访问 NumPy 数组；比 CLI 包装器更底层、安装更重。 |
| [VMAF](vmaf.zh.md) | ✅ | B（5/6） | 当你在调编码档位、需要用业界通用的 0—100 感知分对比编解码器与预设时用它——但它只支持全参考，且选错模型会悄悄让跨版本对比失效。 |
| [SSIMULACRA2](ssimulacra2.zh.md) | ✅ | — | 当你需要对比图像编解码器（JPEG XL、AVIF、WebP）并需要一个与人类主观评分相关的感知质量分时用它——但它仅限图像，非对称，且采用度不及 VMAF。 |
| [m3u8](m3u8.zh.md) | ✅ | C（3/6） | 当你需要把 HLS 的 .m3u8 清单当作带类型的对象模型来解析或改写、而非正则硬抠时用它——但它仅限 Python 与 HLS，且自 2025 年起沉寂，最新的 rfc8216bis 标签可能滞后。 |
| [ffsubsync](ffsubsync.zh.md) | ✅ | B（6/6） | 当字幕整体存在恒定偏移、你想用一条命令做 FFT 音频对齐而不手动设同步点时用它——但它修不了内容内部的逐行／变动漂移，且仅单人维护。 |
| [MoviePy](moviepy.zh.md) | ✅ | ?（0/6） | 当你想用友好的 Python API 做程序化视频编辑——剪辑、合成、文字、特效——时用它——但它是纯离线批处理，对大文件比原生 FFmpeg 慢，且维护速度已从巅峰期下降。 |
| [GStreamer](gstreamer.zh.md) | ✅ | — | 面向实时、持久、嵌入应用的音视频管线式多媒体框架——不是 CLI 工具。学习曲线陡峭，在嵌入式 Linux 和 GTK 应用中表现强劲。 |
| [MLT](mlt.zh.md) | ✅ | — | 用于构建带时间线模型的非线性视频编辑器的多媒体框架——不是独立编辑器，底层编解码工作全部委托给 FFmpeg。需要开箱即用 NLE 时请选 Shotcut 或 Kdenlive。 |
| [OpenAI Whisper](whisper.zh.md) | ✅ | — | 通用多语言语音转文字转写与音视频英译。默认非实时，大模型需要 GPU，且对非语音内容会幻觉。 |

## 什么该放这里

主要职责是**处理媒体**——解码、编码、转码、封装、滤镜——的框架/工具。不含从站点下载媒体（见 `media-download`），不含以非线性视频剪辑为主用途的编辑器。
