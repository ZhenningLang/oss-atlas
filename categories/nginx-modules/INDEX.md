# nginx-modules

> Category node. NGINX / OpenResty extension modules (Lua, upload, etc.).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **lua-nginx-module (ngx_lua)** | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. | [→](lua-nginx-module.md) |
| **lua-resty-redis** | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. | [→](lua-resty-redis.md) |
| **nginx-upload-module** | Use it when you want NGINX to stream large multipart uploads to disk and hand your backend just file metadata — but you're compiling an aging, single-maintainer C fork (last push 2024-07); direct-to-S3 presigned uploads often beat it now. | [→](nginx-upload-module.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [lua-nginx-module (ngx_lua)](lua-nginx-module.md) | ✅ | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. |
| [lua-resty-redis](lua-resty-redis.md) | ✅ | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. |
| [nginx-upload-module](nginx-upload-module.md) | ✅ | Use it when you want NGINX to stream large multipart uploads to disk and hand your backend just file metadata — but you're compiling an aging, single-maintainer C fork (last push 2024-07); direct-to-S3 presigned uploads often beat it now. |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

**NGINX / OpenResty** extension modules. Full API gateways live in `api-gateway`.
