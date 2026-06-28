# networking

> Category node. Networking libraries — SSH, DNS, tunnels, RPC, and traffic shaping.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Paramiko** | The leading pure-Python implementation of the SSHv2 protocol — client and server, with SFTP — letting Python code open SSH connections, run remote commands, and transfer files without shelling out to the `ssh` binary. | [→](paramiko.md) |
| **sshtunnel** | A small Python library (and CLI) that wraps Paramiko to give you SSH port-forwarding tunnels as a context manager — `with SSHTunnelForwarder(...) as t:` opens a local port that bridges, through an SSH bastion, to a service you can't reach directly. | [→](sshtunnel.md) |
| **dnspython** | A powerful, pure-Python DNS toolkit — both high-level resolution (`dns.resolver`) and low-level message/record manipulation (queries, zone transfers, dynamic updates, TSIG, DNSSEC, and modern transports: UDP/TCP, DoH, DoT, DoQ). | [→](dnspython.md) |
| **wondershaper** | A single Bash script that wraps Linux `tc` (traffic control) to cap the up/download bandwidth of a network adapter with one command — `wondershaper -a eth0 -d 8192 -u 2048` instead of a wall of HTB queueing-discipline incantations. | [→](wondershaper.md) |
| **ThriftPy** | A pure-Python implementation of Apache Thrift that loads a `.thrift` file at runtime and generates the RPC client/server code on the fly — **deprecated and archived**, superseded by [thriftpy2](https://github.com/Thriftpy/thriftpy2). | [→](thriftpy.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Paramiko](paramiko.md) | ✅ | The leading pure-Python implementation of the SSHv2 protocol — client and server, with SFTP — letting Python code open SSH connections, run remote commands, and transfer files without shelling out to the `ssh` binary. |
| [sshtunnel](sshtunnel.md) | ✅ | A small Python library (and CLI) that wraps Paramiko to give you SSH port-forwarding tunnels as a context manager — `with SSHTunnelForwarder(...) as t:` opens a local port that bridges, through an SSH bastion, to a service you can't reach directly. |
| [dnspython](dnspython.md) | ✅ | A powerful, pure-Python DNS toolkit — both high-level resolution (`dns.resolver`) and low-level message/record manipulation (queries, zone transfers, dynamic updates, TSIG, DNSSEC, and modern transports: UDP/TCP, DoH, DoT, DoQ). |
| [wondershaper](wondershaper.md) | ✅ | A single Bash script that wraps Linux `tc` (traffic control) to cap the up/download bandwidth of a network adapter with one command — `wondershaper -a eth0 -d 8192 -u 2048` instead of a wall of HTB queueing-discipline incantations. |
| [ThriftPy](thriftpy.md) | ✅ | A pure-Python implementation of Apache Thrift that loads a `.thrift` file at runtime and generates the RPC client/server code on the fly — **deprecated and archived**, superseded by [thriftpy2](https://github.com/Thriftpy/thriftpy2). |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries/tools for **network protocols and links** — SSH, DNS, tunnels, RPC, bandwidth shaping.
