# python-tooling

> Category node. Python developer tooling — compilers, process injection, notebooks, async HTTP.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Cython** | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. | [→](cython.md) |
| **pyrasite** | Use it when you must inject diagnostic code into a stuck or leaking live Python process you can't restart — but injection can crash the target, treat it as incident-only. | [→](pyrasite.md) |
| **gophernotes** | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. | [→](gophernotes.md) |
| **GRequests** | Use it when you want to make existing synchronous `requests` code concurrent with minimal diff via `map()` — but gevent monkeypatches the stdlib and can collide with your stack. | [→](grequests.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Cython](cython.md) | ✅ | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. |
| [pyrasite](pyrasite.md) | ✅ | Use it when you must inject diagnostic code into a stuck or leaking live Python process you can't restart — but injection can crash the target, treat it as incident-only. |
| [gophernotes](gophernotes.md) | ✅ | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. |
| [GRequests](grequests.md) | ✅ | Use it when you want to make existing synchronous `requests` code concurrent with minimal diff via `map()` — but gevent monkeypatches the stdlib and can collide with your stack. |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

Developer tooling for the **Python** ecosystem — compilers, debuggers/injection, kernels, HTTP helpers.
