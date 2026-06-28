---
name: django-rules
slug: django-rules
repo: https://github.com/dfunckt/django-rules
category: auth
tags: [django, authorization, permissions, object-level-permissions, rbac, predicates, python]
language: Python
license: MIT
maturity: v3.x, active (2026-06)
last_verified: 2026-06-28
type: library
---

# django-rules

A tiny Django app that provides **object-level permissions without a database** — you express authorization as composable predicate functions ("rules") and plug them into Django's permission system, views, templates, and DRF.

## When to use

You're building a Django app where "can this user do this?" depends on the *object*, not just a global role — the author can edit their own post, a project member can see a project, a manager can approve their team's requests. Django's built-in permissions are model-level and DB-backed; per-object checks usually mean either ad-hoc `if` logic scattered through views or a heavyweight DB-row permission system like `django-guardian`. With django-rules you instead write small predicate functions (`is_author`, `is_project_member`) and compose them with `&`, `|`, `~` into rules, then register them against permission names. Now `user.has_perm('posts.change_post', post)` evaluates your logic on the fly, with no permission rows to store or sync, and the same rules drive `@permission_required` decorators, the `{% has_perm %}` template tag, and DRF permission classes.

You reach for it when your authorization is *logic*, not *data* — rules derived from relationships and object state rather than rows an admin toggles. It's also usable as a standalone rule-engine outside Django, since the predicate core doesn't depend on the framework. It shines for keeping authorization declarative, testable, and out of your view bodies.

## When NOT to use

- **Admins must grant/revoke per-object permissions at runtime (data-driven).** If permissions are *assigned* (a UI where someone ticks "user X can edit object Y"), you need stored rows — use `django-guardian`; django-rules computes permissions from logic, it doesn't store grants.
- **You need group/role rows managed in the DB and the Django admin.** Django's native permissions + groups (or guardian) are the DB-backed model; django-rules deliberately avoids the database.
- **You want centralized policy-as-code across many services.** For cross-service, language-agnostic policy use OPA/Rego or a dedicated authorization service (OpenFGA/Zanzibar-style); django-rules is in-process and Django-shaped.
- **Your rules are expensive to evaluate per request.** Predicates run on each check; if a rule hits the DB or an external service, per-object loops can be costly — cache or denormalize. [推断]
- **You're not on Django and want full framework integration.** The predicate core works standalone, but the decorators/template-tag/DRF glue are Django-specific — outside Django you get less of the value.

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| django-guardian | 未收录 | Stores per-object permissions as DB rows (assignable via admin/API); the right tool when grants are *data*, but adds tables, queries and sync — heavier than rules-as-logic. |
| Django built-in permissions | 未收录 | Model-level, DB-backed, admin-managed; no per-object granularity without extra work — django-rules fills exactly that gap. |
| Casbin (pycasbin) | 未收录 | Policy-engine with multiple models (RBAC/ABAC) and external policy storage; more general and framework-agnostic, more setup than predicate functions. |
| OPA / OpenFGA | 未收录 | External, language-agnostic policy/authorization services (Rego / Zanzibar-style relationships); powerful at scale and across services, far heavier than an in-process Django lib. |
| ad-hoc `if` checks | 未收录 | The status quo django-rules replaces — no dependency, but scattered, untested, and easy to get subtly wrong. |

## Tech stack

- **Language:** Python; a Django app plus a framework-independent predicate core (`rules`).
- **Model:** predicate functions composed with boolean operators (`&`, `|`, `~`) into named rules, registered into a rule set and exposed via Django's permission backend.
- **Integrations:** Django auth backend (`has_perm`), `@permission_required`/`@objectpermission_required` decorators, a `{% has_perm %}` template tag, and Django REST Framework permission classes.
- **Distribution:** PyPI as `rules` (`pip install rules`); no database tables added.

## Dependencies

- **Runtime:** Python and Django (for the Django integration); the predicate core can be used standalone with just Python. Supported Django/Python versions are set by the current release's metadata. [未验证]
- **Database:** **none required** — that's the headline; it adds no models/migrations. Whatever your rules query (e.g. checking object relationships) uses your app's existing DB.
- **DRF (optional):** only if you use the provided DRF permission classes.
- **No external services or datastore of its own.**

## Ops difficulty

**Low.** It's a pure library with **no migrations, tables, or services** to operate — `pip install rules`, add it to `INSTALLED_APPS`, register predicates. Nothing to deploy or maintain at the infra level. The only real cost is design-time and runtime-correctness: writing and testing predicates carefully (authorization bugs are security bugs), and watching the per-request evaluation cost if predicates touch the database or external systems.

## Health & viability

- **Maintenance (2026-06).** Last pushed 2025-10 with a v3.x release line (latest tags v3.4/v3.5); steady, if unhurried, releases tracking Django versions — **active**, not abandoned. Not archived. [推断]
- **Governance / bus factor.** Led by the original author (dfunckt) on a personal account with a recurring contributor tail; small-team but long-sustained. A single-lead bus-factor consideration, mitigated by the library's small, stable surface. [推断]
- **Age & Lindy verdict.** ~12 years old (created 2014-03) and **still releasing** ⇒ a **strong Lindy** signal: a mature, narrowly-scoped library that has long since stabilized. [推断]
- **Adoption.** ~2k stars; a well-known, commonly-recommended answer for Django object-level permissions, with good docs and test coverage. [未验证]
- **Risk flags.** MIT-licensed, no relicense history found; main consideration is Django-version-tracking cadence (it must keep up with Django releases) and single-lead governance. [推断]

## Caveats (unverified)

- [未验证] ~2k stars and a v3.x release line (latest ~v3.5) as of 2026-06; star counts and version numbers drift — indicative only.
- [未验证] The exact supported Django and Python version ranges are set by the current release metadata and change over time; not asserting specific numbers.
- [推断] Per-request predicate evaluation cost when rules query the DB/external services is an inherent design property, not a measured performance figure.
- [推断] "Active" is inferred from the 2025-10 last-push and tag history, not a precise release-interval measurement.
- [推断] Single-lead/bus-factor characterization is inferred from contributor distribution and personal-account ownership, not a governance document.
