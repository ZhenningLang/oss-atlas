---
name: Deno
slug: deno
repo: https://github.com/denoland/deno
category: dev-utilities
tags: [javascript, typescript, runtime, secure-by-default, webassembly]
language: Rust
license: MIT
maturity: v2.x, stable, 107.3k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T09:52:46Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T12:50:21Z
  overall: "?"
  overall_score: null
  scored_axes: 1
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: "?"
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: deno_core
        dependent_repos_count: 396
        downloads_last_month: 5934345
        graph_tier: C
        volume_tier: A
        cross_check_divergence: 4.42
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    maintenance: { reason: recency_unreadable }
    responsiveness: { reason: no_traffic }
    longevity: { reason: not_found }
    governance: { reason: empty_or_gated }
    risk_license: { reason: repo_unreachable }
---

# Deno

A modern runtime for JavaScript, TypeScript, and WebAssembly with secure defaults and a great developer experience. Built on V8, Rust, and Tokio.

![Deno — health radar](../../assets/health/deno.svg)

## When to use

You're choosing a JavaScript/TypeScript runtime for a new server-side project or CLI tool and you want a modern, secure toolchain. You pick Deno over Node.js because you're tired of `node_modules` bloat, `package.json` dependency hell, and the need for external tooling (ts-node, nodemon, eslint, prettier). You want a runtime that treats TypeScript as a first-class citizen, has built-in formatting, linting, and testing, and enforces security permissions by default. You pick Deno over Bun because Deno has a standard OSI license (MIT), a longer track record (8 years vs 5 years), and stronger WebAssembly integration. You install Deno with a single shell command, write `.ts` files that run directly, and ship a compiled standalone binary when you're ready. Deno's standard library and npm compatibility mean you can bring your existing packages along while enjoying a modern toolchain.

## When NOT to use

- If you have an existing Node.js monolith with native Node.js addons, C++ bindings, or deep `node-gyp` dependencies, use Node.js instead of Deno, because complex projects with native modules are unlikely to migrate smoothly.
- If you rely on npm packages that depend on Node.js-specific APIs or post-install scripts, use Node.js instead of Deno, because some packages may not work under Deno's npm compatibility layer.
- If your entire team knows Node.js and no one has Deno experience, and the project is short-term, use Node.js instead of Deno, because the productivity hit during onboarding may outweigh the benefits.
- If you need to optimize at the V8 level, stay on Node.js instead of Deno, because both use the same V8 engine and CPU-bound performance is identical.
- If you want fully portable serverless code without proprietary edge runtime lock-in, use Node.js or Cloudflare Workers instead of Deno, because Deno Deploy is a proprietary service.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Node.js | 未收录 | The incumbent JS/TS runtime with the largest ecosystem. | Node.js has the deepest npm ecosystem and broadest hosting support; Deno offers a cleaner, more secure developer experience but a smaller community. |
| Bun | 未收录 | Fast all-in-one JS runtime with bundler and package manager built in. | Bun is faster and also treats TypeScript as first-class, but it is younger and less proven than Deno. |
| [Supabase](../databases/supabase.md) | ✅ | Uses Deno for edge functions. | Not a runtime comparison per se, but demonstrates Deno's production use in serverless edge contexts. |
| Wasmer / Wasmtime | 未收录 | Pure WebAssembly runtimes. | These are for Wasm modules, not JS/TS applications; Deno can run Wasm but is primarily a JS runtime. |

## Tech stack

- **Rust** — core runtime, HTTP server, and sandboxing layer
- **V8** — JavaScript engine (same as Node.js and Chrome)
- **Tokio** — async runtime for Rust, powering Deno's I/O
- **TypeScript** — first-class language support (transpiled internally)
- **WebAssembly** — supports running Wasm modules alongside JS/TS

## Dependencies

- Deno binary (single executable, no external runtime needed)
- For compilation: a C++ linker if producing standalone binaries (Deno uses `deno compile`)
- Optional: npm packages via `npm:` specifiers or JSR (JavaScript Registry) packages
- No `node_modules` or `package.json` required for Deno-native projects

## Ops difficulty

**Low**. Deno is a single binary that runs on major OSs. For deployment, you can run `deno run` directly, compile to a standalone binary with `deno compile`, or deploy to Deno Deploy (managed edge). The built-in toolchain (test, fmt, lint, bench) reduces the need for separate devDependencies. No `node_modules` bloat simplifies CI/CD caching and Docker image sizes.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance**: Very active — pushed daily as of 2026-07, with a mature v2 release line and responsive core team (1,354 open issues). [推断]
- **Governance**: Owned by the `denoland` organization with Ryan Dahl (Node.js creator) as a key figure. The project has a clear technical vision and multiple core contributors. Bus factor is reasonable.
- **Backing**: Deno Land Inc. is the commercial entity behind the project; Deno Deploy is their revenue source. The company has raised venture funding, which introduces both stability and potential future direction conflicts. [未验证]
- **Adoption**: Strong adoption with 107.3k stars, created in 2018 (8-year track record). Used by companies like Supabase for edge functions and in various production CLI tools.
- **Risk flags**: The MIT license is permissive. The venture-backed backing model means the open-source roadmap may be influenced by the commercial Deno Deploy product. No relicense history visible, but monitor for open-core gating. [未验证]

## Caveats (unverified)

- [未验证] Deno Land Inc. has raised venture funding; the exact funding rounds and investors have not been verified from primary sources.
- [推断] Deno Deploy's proprietary edge runtime may create incentives to prioritize Deno-specific APIs over standard web compatibility in the future.
- [未验证] The exact number of production deployments and enterprise users beyond Supabase has not been verified.
