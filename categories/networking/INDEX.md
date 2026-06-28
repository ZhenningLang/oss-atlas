# networking

> Category node. Networking libraries — SSH, DNS, tunnels, RPC, and traffic shaping.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **Paramiko** | Use it when Python code must open SSH/SFTP connections and run remote commands programmatically — but it's pure-Python (slower than OpenSSH), threading-only, and LGPL-2.1. | [→](paramiko.md) |
| **sshtunnel** | Use it when a Python script needs a clean context-managed SSH port-forward to a service behind a bastion — but it has no auto-reconnect and is low-activity (0.4.0, 2021). | [→](sshtunnel.md) |
| **dnspython** | Use it when Python needs arbitrary record types, custom resolvers, zone transfers, DNSSEC, or DoH/DoT — but it bypasses /etc/hosts and the OS resolver, requires Python 3.10+, and is a library not a CLI. | [→](dnspython.md) |
| **wondershaper** | Use it when one Linux NIC needs a quick up/down bandwidth ceiling without hand-writing tc rules — but it's HTB-era (not bufferbloat-aware like cake/fq_codel) and Linux-only, coasting since 2024-07. | [→](wondershaper.md) |
| **ThriftPy** | Use it only to understand a legacy service still importing thriftpy before migrating — the repo is archived and deprecated, so all new Thrift work should go to the maintained thriftpy2. | [→](thriftpy.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [Paramiko](paramiko.md) | ✅ | Use it when Python code must open SSH/SFTP connections and run remote commands programmatically — but it's pure-Python (slower than OpenSSH), threading-only, and LGPL-2.1. |
| [sshtunnel](sshtunnel.md) | ✅ | Use it when a Python script needs a clean context-managed SSH port-forward to a service behind a bastion — but it has no auto-reconnect and is low-activity (0.4.0, 2021). |
| [dnspython](dnspython.md) | ✅ | Use it when Python needs arbitrary record types, custom resolvers, zone transfers, DNSSEC, or DoH/DoT — but it bypasses /etc/hosts and the OS resolver, requires Python 3.10+, and is a library not a CLI. |
| [wondershaper](wondershaper.md) | ✅ | Use it when one Linux NIC needs a quick up/down bandwidth ceiling without hand-writing tc rules — but it's HTB-era (not bufferbloat-aware like cake/fq_codel) and Linux-only, coasting since 2024-07. |
| [ThriftPy](thriftpy.md) | ✅ | Use it only to understand a legacy service still importing thriftpy before migrating — the repo is archived and deprecated, so all new Thrift work should go to the maintained thriftpy2. |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries/tools for **network protocols and links** — SSH, DNS, tunnels, RPC, bandwidth shaping.
