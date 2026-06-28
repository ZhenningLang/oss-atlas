# nginx-modules

> Category node. NGINX / OpenResty extension modules (Lua, upload, etc.).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Page |
|---|---|---|
| **lua-nginx-module (ngx_lua)** | An NGINX module that embeds a LuaJIT (or Lua) VM into the server, letting you run Lua at every phase of request processing — rewrite, access, content, log — with a non-blocking cosocket API so your Lua can talk to upstream TCP/UDP services without stalling the worker. | [→](lua-nginx-module.md) |
| **lua-resty-redis** | A non-blocking Redis client driver for OpenResty / ngx_lua — pure Lua on top of the ngx_lua cosocket API, so your NGINX worker can talk to Redis mid-request without blocking the event loop, with connection pooling and pipelining built in. | [→](lua-resty-redis.md) |
| **nginx-upload-module** | An NGINX C module that handles `multipart/form-data` (RFC 1867) file uploads at the server edge — NGINX streams the upload to disk itself and passes only the file metadata (paths, names, sizes) to your backend, so your application never has to buffer the raw upload. | [→](nginx-upload-module.md) |

## Comparison matrix

| Option | Indexed | One-line tradeoff |
|---|---|---|
| [lua-nginx-module (ngx_lua)](lua-nginx-module.md) | ✅ | An NGINX module that embeds a LuaJIT (or Lua) VM into the server, letting you run Lua at every phase of request processing — rewrite, access, content, log — with a non-blocking cosocket API so your Lua can talk to upstream TCP/UDP services without stalling the worker. |
| [lua-resty-redis](lua-resty-redis.md) | ✅ | A non-blocking Redis client driver for OpenResty / ngx_lua — pure Lua on top of the ngx_lua cosocket API, so your NGINX worker can talk to Redis mid-request without blocking the event loop, with connection pooling and pipelining built in. |
| [nginx-upload-module](nginx-upload-module.md) | ✅ | An NGINX C module that handles `multipart/form-data` (RFC 1867) file uploads at the server edge — NGINX streams the upload to disk itself and passes only the file metadata (paths, names, sizes) to your backend, so your application never has to buffer the raw upload. |
| (alternatives named across the pages) | 未收录 | Substitutes referenced in each page's Comparison. |

## What belongs here

**NGINX / OpenResty** extension modules. Full API gateways live in `api-gateway`.
