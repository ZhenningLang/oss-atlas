# nginx-modules

> 分类节点。NGINX / OpenResty 扩展模块(Lua、上传等)。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 页面 |
|---|---|---|
| **lua-nginx-module (ngx_lua)** | 一个把 LuaJIT（或 Lua）虚拟机嵌入服务器的 NGINX 模块，让你在请求处理的每个阶段——rewrite、access、content、log——运行 Lua，并配一套非阻塞 cosocket API，使你的 Lua 能与上游 TCP/UDP 服务通信而不卡住 worker。 | [→](lua-nginx-module.zh.md) |
| **lua-resty-redis** | 一个面向 OpenResty / ngx_lua 的非阻塞 Redis 客户端驱动——纯 Lua，跑在 ngx_lua cosocket API 之上，让你的 NGINX worker 能在请求中途连 Redis 而不阻塞事件循环，内建连接池和 pipeline。 | [→](lua-resty-redis.zh.md) |
| **nginx-upload-module** | 一个在服务器边缘处理 `multipart/form-data`（RFC 1867）文件上传的 NGINX C 模块——NGINX 自己把上传流式写到磁盘，只把文件元数据（路径、文件名、大小）传给你的后端，于是你的应用永远不必缓冲原始上传内容。 | [→](nginx-upload-module.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 一句话取舍 |
|---|---|---|
| [lua-nginx-module (ngx_lua)](lua-nginx-module.zh.md) | ✅ | 一个把 LuaJIT（或 Lua）虚拟机嵌入服务器的 NGINX 模块，让你在请求处理的每个阶段——rewrite、access、content、log——运行 Lua，并配一套非阻塞 cosocket API，使你的 Lua 能与上游 TCP/UDP 服务通信而不卡住 worker。 |
| [lua-resty-redis](lua-resty-redis.zh.md) | ✅ | 一个面向 OpenResty / ngx_lua 的非阻塞 Redis 客户端驱动——纯 Lua，跑在 ngx_lua cosocket API 之上，让你的 NGINX worker 能在请求中途连 Redis 而不阻塞事件循环，内建连接池和 pipeline。 |
| [nginx-upload-module](nginx-upload-module.zh.md) | ✅ | 一个在服务器边缘处理 `multipart/form-data`（RFC 1867）文件上传的 NGINX C 模块——NGINX 自己把上传流式写到磁盘，只把文件元数据（路径、文件名、大小）传给你的后端，于是你的应用永远不必缓冲原始上传内容。 |
| (各页对比里点到的替代品) | 未收录 | 详见各页 Comparison。 |

## 什么该放这里

**NGINX / OpenResty** 扩展模块。完整 API 网关见 `api-gateway`。
