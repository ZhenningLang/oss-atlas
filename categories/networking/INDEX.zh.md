# networking

> 分类节点。网络库——SSH、DNS、隧道、RPC 与流量整形。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **Paramiko** | 最主流的纯 Python SSHv2 协议实现——客户端与服务端，带 SFTP——让 Python 代码无需 shell 调用 `ssh` 二进制就能打开 SSH 连接、跑远程命令、传文件。 | [→](paramiko.zh.md) |
| **sshtunnel** | 一个小巧的 Python 库（兼 CLI），封装 Paramiko，把 SSH 端口转发隧道做成上下文管理器——`with SSHTunnelForwarder(...) as t:` 打开一个本地端口，经由 SSH 堡垒机桥接到你直连不到的服务。 | [→](sshtunnel.zh.md) |
| **dnspython** | 一个强大的纯 Python DNS 工具包——既有高层解析（`dns.resolver`），也有底层报文/记录操作（查询、区域传送、动态更新、TSIG、DNSSEC，以及现代传输：UDP/TCP、DoH、DoT、DoQ）。 | [→](dnspython.zh.md) |
| **wondershaper** | 一个单文件 Bash 脚本，封装 Linux `tc`（流量控制），一条命令就给某个网卡的上/下行带宽封顶——`wondershaper -a eth0 -d 8192 -u 2048`，而不是一大堆 HTB 排队规则咒语。 | [→](wondershaper.zh.md) |
| **ThriftPy** | Apache Thrift 的纯 Python 实现：运行时直接加载 `.thrift` 文件、即时生成 RPC 客户端/服务端代码——**已弃用并归档**，由 [thriftpy2](https://github.com/Thriftpy/thriftpy2) 取代。 | [→](thriftpy.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [Paramiko](paramiko.zh.md) | ✅ | 最主流的纯 Python SSHv2 协议实现——客户端与服务端，带 SFTP——让 Python 代码无需 shell 调用 `ssh` 二进制就能打开 SSH 连接、跑远程命令、传文件。 |
| [sshtunnel](sshtunnel.zh.md) | ✅ | 一个小巧的 Python 库（兼 CLI），封装 Paramiko，把 SSH 端口转发隧道做成上下文管理器——`with SSHTunnelForwarder(...) as t:` 打开一个本地端口，经由 SSH 堡垒机桥接到你直连不到的服务。 |
| [dnspython](dnspython.zh.md) | ✅ | 一个强大的纯 Python DNS 工具包——既有高层解析（`dns.resolver`），也有底层报文/记录操作（查询、区域传送、动态更新、TSIG、DNSSEC，以及现代传输：UDP/TCP、DoH、DoT、DoQ）。 |
| [wondershaper](wondershaper.zh.md) | ✅ | 一个单文件 Bash 脚本，封装 Linux `tc`（流量控制），一条命令就给某个网卡的上/下行带宽封顶——`wondershaper -a eth0 -d 8192 -u 2048`，而不是一大堆 HTB 排队规则咒语。 |
| [ThriftPy](thriftpy.zh.md) | ✅ | Apache Thrift 的纯 Python 实现：运行时直接加载 `.thrift` 文件、即时生成 RPC 客户端/服务端代码——**已弃用并归档**，由 [thriftpy2](https://github.com/Thriftpy/thriftpy2) 取代。 |
| (各页对比里点到的替代品) | 未收录 | 详见各页 Comparison。 |

## 什么该放这里

面向**网络协议与链路**的库/工具——SSH、DNS、隧道、RPC、带宽整形。
