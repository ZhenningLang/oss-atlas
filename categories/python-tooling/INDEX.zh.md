# python-tooling

> 分类节点。Python 开发者工具——编译器、进程注入、notebook、异步 HTTP。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Cython** | 一个把 Python（以及带类型标注的 Python 超集）编译成 C、产出原生 CPython 扩展模块的编译器——是让热点 Python 代码变快、或封装 C/C++ 库的标准做法。 | [→](cython.zh.md) |
| **pyrasite** | 一个把任意 Python 代码注入**正在运行**的 Python 进程的工具——通过 gdb 挂到一个活的 PID 上，跑诊断片段、dump 对象，或开一个反向 shell，全程不重启目标。 | [→](pyrasite.zh.md) |
| **gophernotes** | **Go** 语言的一个 Jupyter 内核——在 Jupyter 笔记本（以及 nteract）里逐 cell 交互式地写和跑 Go，cell 之间状态持久。 | [→](gophernotes.zh.md) |
| **GRequests** | Requests + Gevent：用熟悉的 `requests` API 并发发出大量 HTTP 请求，通过 `map()`/`imap()` 收集结果，而不必自己写异步代码。 | [→](grequests.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Cython](cython.zh.md) | ✅ | 一个把 Python（以及带类型标注的 Python 超集）编译成 C、产出原生 CPython 扩展模块的编译器——是让热点 Python 代码变快、或封装 C/C++ 库的标准做法。 |
| [pyrasite](pyrasite.zh.md) | ✅ | 一个把任意 Python 代码注入**正在运行**的 Python 进程的工具——通过 gdb 挂到一个活的 PID 上，跑诊断片段、dump 对象，或开一个反向 shell，全程不重启目标。 |
| [gophernotes](gophernotes.zh.md) | ✅ | **Go** 语言的一个 Jupyter 内核——在 Jupyter 笔记本（以及 nteract）里逐 cell 交互式地写和跑 Go，cell 之间状态持久。 |
| [GRequests](grequests.zh.md) | ✅ | Requests + Gevent：用熟悉的 `requests` API 并发发出大量 HTTP 请求，通过 `map()`/`imap()` 收集结果，而不必自己写异步代码。 |
| (各页对比里点到的替代品) | 未收录 | 详见各页 Comparison。 |

## 什么该放这里

面向 **Python** 生态的开发者工具——编译器、调试器/注入、内核、HTTP 辅助。
