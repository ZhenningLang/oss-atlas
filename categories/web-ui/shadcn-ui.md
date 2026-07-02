---
name: shadcn/ui
slug: shadcn-ui
repo: https://github.com/shadcn-ui/ui
category: web-ui
tags: [react, components, tailwind, radix, design-system, ui-library, accessibility, nextjs]
language: TypeScript
license: MIT
maturity: active, ~117.7k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-06-30T06:34:55Z
  default_branch: main
  default_branch_sha: 0000000000000000000000000000000000000000
  archived: false
health:
  schema: 1
  computed_at: 2026-07-01T00:00:00Z
  overall: "?"
  overall_score: 0.0
  scored_axes: 0
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
      grade: "?"
      raw: {}
    longevity:
      grade: "?"
      raw: {}
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
---

# shadcn/ui

A set of beautifully-designed, accessible React components and a code distribution platform that you copy into your project and own completely — built on Tailwind CSS and Radix UI primitives.

![shadcn/ui — health radar](../../assets/health/shadcn-ui.svg)

## When to use

You're a React developer building a new product and you need a solid, accessible UI foundation without fighting a third-party component library's theming system. You want buttons, dialogs, dropdowns, tables, and forms that look great out of the box, but you also want to be able to change every pixel — the colors, the spacing, the animations — without overriding CSS layers or waiting for a library update. You run `npx shadcn@latest add button dialog`, and the components are copied directly into your codebase as source files you own. They use Tailwind CSS for styling and Radix UI for accessibility and behavior, so you get keyboard navigation, ARIA attributes, and focus management for free, while the visual layer is yours to customize.

You also reach for it when you want a design system that stays in your repo, not in `node_modules`. Because shadcn/ui is a copy-and-own model, there is no runtime dependency to version-lock or worry about breaking changes from upstream. If the upstream project adds a new component, you can selectively adopt it; if you need a bespoke variant, you edit the copied file directly.

## When NOT to use

- **You are not using React.** shadcn/ui is React-only; there is no Vue, Angular, or Svelte equivalent in this ecosystem. For other frameworks, use their respective component libraries.
- **You want a zero-config UI kit where you don't touch the code.** shadcn/ui requires you to own and maintain the component files in your repo. If you prefer a library where you import `<Button>` and never look at its implementation, use Material UI or Chakra UI.
- **You need a strict, enterprise-grade design system with governance.** shadcn/ui is a starting point, not a governed design system. It does not enforce token usage, component usage rules, or visual consistency across teams — you must build that governance yourself.
- **You are already committed to another component library.** Migrating from Material UI, Ant Design, or Chakra to shadcn/ui means replacing components one by one and rebuilding your theme layer in Tailwind. The payoff is ownership, but the migration cost is real.
- **You need complex data-grid or chart components out of the box.** shadcn/ui provides primitives and basic table patterns; for heavy data grids, pivot tables, or charts, you will need to integrate dedicated libraries (TanStack Table, AG Grid, Recharts, etc.).
- **You don't use Tailwind CSS.** The components are styled with Tailwind utility classes; if your project uses CSS-in-JS, Styled Components, or plain CSS, you will need to rewire the styling layer entirely.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Material UI (MUI) | 未收录 | Use this page for its stated niche; choose MUI when you need a comprehensive, Google-Material-themed component library with a large enterprise ecosystem. | Comprehensive Google-Material-themed React component library with enterprise adoption and paid support; heavier and more opinionated than shadcn/ui. |
| Chakra UI | 未收录 | Use this page for its stated niche; choose Chakra UI when you want a simpler, styled-system-based React component library with good DX. | Simple, styled-system-based React library with good DX and a consistent theme API; less customizable at the file level than shadcn/ui's copy-and-own model. |
| Ant Design | 未收录 | Use this page for its stated niche; choose Ant Design when you need a full-featured enterprise UI framework with many built-in components. | Full-featured enterprise UI framework with a vast component set and Chinese-first community; heavier and less Tailwind-native than shadcn/ui. |
| Radix UI | 未收录 | Use this page for its stated niche; choose Radix UI when you need headless, unstyled primitives and plan to build your own styling layer from scratch. | Headless, unstyled accessibility primitives; shadcn/ui builds on Radix and adds Tailwind styling and a distribution workflow. |
| Headless UI | 未收录 | Use this page for its stated niche; choose Headless UI when you want Tailwind-compatible, unstyled components from the Tailwind team. | Tailwind-team-authored unstyled components; fewer primitives than Radix and no built-in "copy to own" distribution system. |

## Tech stack

- **Language:** TypeScript, compiled to JavaScript; all components are typed and tree-shakeable.
- **Styling:** Tailwind CSS utility classes for all visual styles; no separate CSS file or CSS-in-JS runtime.
- **Primitives:** Built on Radix UI primitives for accessibility (ARIA, keyboard navigation, focus trapping, portal behavior) and behavior (dialogs, dropdowns, accordions, etc.).
- **Distribution:** CLI (`npx shadcn@latest add <component>`) copies source files into your project's `components/ui/` directory; no npm dependency on the component library itself.
- **Framework support:** Optimized for Next.js and React 18+; also works with Vite, Remix, and other React frameworks. [未验证]

## Dependencies

- **Runtime:** React 18+ and a Tailwind CSS project. The components assume Tailwind is configured and its utility classes are available in your build.
- **Library deps:** The copied components may pull in small Radix UI sub-packages and `clsx` / `tailwind-merge` for class merging; these are normal runtime dependencies you already manage.
- **No backend:** It is a client-side UI library; no server, database, or service required.
- **Build integration:** Your bundler (Vite, Next.js, webpack) must process Tailwind CSS and the TypeScript/JSX component files. [推断]

## Ops difficulty

**Low.** There is nothing to deploy or operate beyond your normal React build pipeline. The operational burden is in **maintenance of the copied components**: when you upgrade the shadcn/ui CLI or add a new component, you may need to reconcile styling changes or Tailwind config updates. Because the components live in your repo, you must patch them yourself if a bug is found — you cannot just bump a version in `package.json`. The flip side is that you are never blocked by upstream release cadence. For a small team, the copy-and-own model is low-friction; for a large org with many teams, you may need to build your own internal distribution mechanism to keep component variants consistent. [推断]

## Health & viability

- **Maintenance (2026-07).** Last pushed 2026-06-30 with a very active commit history and frequent releases; the project is not archived and has a thriving community. [推断]
- **Governance / bus factor.** Owned by the `shadcn-ui` GitHub organization (multi-maintainer), with shadcn as the visible lead. The project has strong community contribution and a clear CLI-driven distribution model. [推断]
- **Age & Lindy verdict.** ~2.5 years old (created 2023-01) and extremely popular ⇒ a **moderate Lindy** signal for a UI library; it has become the dominant React component distribution model in the modern Tailwind ecosystem. [推断]
- **Adoption & ecosystem.** ~117.7k stars and massive real-world adoption across Next.js, SaaS, and open-source projects. The "copy-and-own" model has influenced many other component libraries. [未验证]
- **Risk flags.** MIT license with no relicense history. The main risk is **ecosystem coupling**: the project is tightly bound to React + Tailwind CSS + Radix UI; if any of those shifts significantly (e.g., React Server Components behavior changes, Tailwind v4 breaking changes), the component files in your repo may need manual updates. [推断]

## Caveats (unverified)

- [未验证] ~117.7k GitHub stars as of 2026-07-01; star counts are approximate and time-sensitive.
- [未验证] The exact React version compatibility and framework support (Next.js, Vite, Remix) shift with the CLI releases; verify the current docs before installing.
- [未验证] The `npx shadcn` CLI distribution model and available component registry are evolving rapidly; the exact set of installable components and their options may change.
- [推断] The copy-and-own model means you are responsible for merging upstream fixes into your local component files; there is no automatic patch mechanism.
- [推断] Large organizations may struggle with consistency across multiple teams each copying and modifying components independently; internal governance is required.
- [推断] While the primitives are accessible, the final accessibility of your application depends on how you compose and configure the copied components in your own code.
