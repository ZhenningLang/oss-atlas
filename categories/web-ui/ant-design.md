---
name: Ant Design
slug: ant-design
repo: https://github.com/ant-design/ant-design
category: web-ui
tags: [react, ui-library, design-system, enterprise, components, typescript]
language: TypeScript
license: MIT
maturity: v5.x, stable, 98.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-01T10:31:49Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-02T08:27:28Z
  overall: A
  overall_score: 4.0
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.1
        qualifying_issues: 41
        band: default
        window_offset_days: 5
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 4087
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 73
        top1_share: 0.209
        top3_share: 0.52
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: registry_no_counts }
---

# Ant Design

An enterprise-class UI design language and React UI library. One of the most widely adopted component libraries for building admin dashboards, data-dense applications, and enterprise tools in the React ecosystem.

![Ant Design — health radar](../../assets/health/ant-design.svg)

## When to use

You're building a data-dense admin dashboard, an internal operations tool, or a B2B SaaS application in React. You need a comprehensive set of pre-built, accessible components: tables with sorting and filtering, forms with validation, date pickers, modals, trees, and upload widgets. You want these components to look professional out of the box without hiring a designer. You install Ant Design via npm, import the components, and your app looks consistent and polished immediately. The design system is battle-tested by Alibaba and thousands of other companies, so you know it scales to complex, multi-role enterprise interfaces.

## When NOT to use

- **Non-React projects** — Ant Design is a React library. For Vue, there is Ant Design Vue (a separate project), but the core library is React-only. For Svelte or plain HTML, look elsewhere.
- **Highly custom branded apps** — Ant Design's visual language is distinctive (the "Ant Design look"). If your brand requires a unique visual identity that deviates significantly from Material Design or Apple's Human Interface, overriding the default styles can be tedious and fragile.
- **Bundle size sensitivity** — The full Ant Design library is large. If you don't use tree-shaking or import components individually, your bundle will bloat. Even with tree-shaking, the design tokens and CSS can add significant weight.
- **Mobile-first consumer apps** — While Ant Design Mobile exists, the primary library is desktop-focused. For consumer mobile apps, consider frameworks like Ionic or native solutions.
- **Zero-CSS-override projects** — Ant Design uses Less for theming and requires specific build tooling (or CSS-in-JS workarounds) for deep customization. If your stack forbids Less or you want CSS-module-level isolation, friction will occur. [推断]
- **Teams that want headless components** — Ant Design is a styled component library. If you want unstyled, headless primitives (like Radix UI) and full control over styling, Ant Design is the wrong abstraction level.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Material UI (MUI) | 未收录 | The most popular React UI library with a Material Design aesthetic and a large enterprise presence. | MUI is more ubiquitous in the West; Ant Design dominates in China and Asia-Pacific enterprise. Both are comprehensive; choose based on design language preference and regional ecosystem. |
| [shadcn/ui](shadcn-ui.md) | ✅ | Copy-paste React components you own, built on Radix UI and Tailwind CSS. | shadcn/ui gives you full ownership and no npm dependency; Ant Design gives you a faster start but deeper lock-in and less styling flexibility. |
| Chakra UI | 未收录 | Modular React component library with a focus on developer experience and accessibility. | Chakra UI is more "developer-friendly" for custom theming; Ant Design has more enterprise-grade components (especially data tables and forms). |
| Radix UI | 未收录 | Headless, unstyled primitives for building your own design system. | Radix is lower-level (you bring your own styles); Ant Design is a complete, styled system. |
| Bootstrap / React-Bootstrap | 未收录 | Classic CSS framework with React wrappers. | Bootstrap is older and simpler; Ant Design is more modern, component-rich, and better suited for complex data-driven apps. |

## Tech stack

- **TypeScript** — primary language; all components are typed
- **React** — the target UI framework (Ant Design is a React library)
- **Less** — CSS pre-processor for theming and component styles
- **CSS-in-JS** — used internally for dynamic styling (via `@ant-design/cssinjs`)
- **Design Tokens** — centralized token system for colors, spacing, typography
- **Ant Design Mobile** — separate React Native / mobile component library (not the same package)
- **dumi** — documentation site generator used for ant.design

## Dependencies

- **React** — required peer dependency (v16.8+ for hooks, v18+ recommended)
- **ReactDOM** — required peer dependency
- **TypeScript** — optional but strongly recommended for type safety
- **Build toolchain** — Webpack, Vite, or esbuild for bundling and Less compilation
- **Optional: moment.js / dayjs / date-fns** — Ant Design's date components require a date library (dayjs is recommended as the lighter alternative)
- **Optional: @ant-design/icons** — the official icon library (separate package)
- **Optional: ant-design/charts or AntV** — for data visualization (separate ecosystem)

## Ops difficulty

**Low**. Ant Design is an npm library, not a standalone service. Operational concerns are limited to:
- Keeping the library updated (major version upgrades can involve breaking changes in component APIs and theming)
- Managing bundle size by importing only the components you use
- Customizing the theme via Less variables or the ConfigProvider component
- Ensuring your build pipeline handles Less compilation or that you use the pre-built CSS
- Monitoring for accessibility issues in complex components (tables, forms) that may need manual ARIA adjustments

## Health & viability

- **Maintenance**: Very active — daily pushes as of 2026-07, with a regular release schedule and a large issue/PR throughput (98.5k stars, 1,284 open issues). [推断]
- **Governance**: Maintained by the Ant Design Team within Alibaba's open-source ecosystem. The project has multiple core committers and a clear governance model. Bus factor is moderate to good. [推断]
- **Backing**: Backed by Alibaba, one of China's largest tech companies. This provides stability and resources but also means the project's direction is influenced by Alibaba's internal needs. [推断]
- **Adoption**: Extremely strong adoption in the Asia-Pacific enterprise market and growing globally. 98.5k stars, created in 2015 (11-year track record). Used by Alibaba, Tencent, and thousands of startups. [推断]
- **Risk flags**: The MIT license is permissive. No relicense history visible. The project's close ties to Alibaba mean geopolitical or compliance concerns could affect some Western enterprises. The v4-to-v5 migration involved breaking theming changes; future major versions may require similar effort. [未验证]

## Caveats (unverified)

- [未验证] The exact proportion of Ant Design's user base in China versus the rest of the world has not been verified.
- [推断] Ant Design's CSS-in-JS approach (via `@ant-design/cssinjs`) may have performance implications in very large applications with many dynamic style updates.
- [未验证] The accessibility audit results for all Ant Design components have not been independently verified.
- [推断] The level of influence Alibaba's internal product roadmap has on Ant Design's open-source priorities is not transparently documented.
