---
name: Claude Code Security Review
slug: claude-code-security-review
repo: https://github.com/anthropics/claude-code-security-review
category: ai-code-review
tags: [security, sast, github-action, claude, pr-review, slash-command]
language: Python
license: MIT
maturity: no tagged release, pinned via @main, active (2026-02)
last_verified: 2026-06-26
type: tool
---

# Claude Code Security Review

Anthropic's AI security reviewer: a GitHub Action (plus a `/security-review` Claude Code slash command) that reads a PR diff with Claude and posts line-level vulnerability findings.

## When to use

You're a maintainer of a small-to-mid repo and you want a security gate on pull requests that goes beyond regex/AST pattern matching. Traditional SAST flags the same shapes over and over and misses logic-level bugs — an IDOR that only matters because of how two handlers share a session, an injection that's only reachable through a specific code path. You add this Action to `.github/workflows/`, give it a Claude API key, and on every PR it analyzes only the changed files, reasons about the diff in context, and leaves review comments on the exact lines it thinks are vulnerable, with severity and remediation. Because it's "language agnostic" (it's Claude reading code, not a per-language ruleset), the same workflow covers your Python service, your TypeScript frontend, and your Terraform without separate tooling.

You're also a developer using Claude Code day-to-day who wants the same check before you even open a PR. You run `/security-review` on your pending changes and get the audit locally; you can copy `security-review.md` into your repo's `.claude/commands/` and tune the prompt for your project. The tool's whole pitch is the inverse of noisy scanners: an opinionated false-positive filter that drops DoS/rate-limit/open-redirect-style findings so the comments that land are the ones worth acting on.

## When NOT to use

- **You need to review untrusted / fork PRs.** The README states it is **not hardened against prompt injection** and should only review **trusted PRs**; a malicious diff can attempt to manipulate the reviewer. For public repos you must gate it behind maintainer approval of external contributors — a hard operational constraint, not a nice-to-have.
- **You want a free or local-only scanner.** Every run calls the Claude API and bills tokens (default model `claude-opus-4-1-20250805`, with a 20-min timeout per run). High-PR-volume repos or `run-every-commit: true` can get expensive — a deterministic OSS SAST (Semgrep, CodeQL) has no per-run API cost.
- **You need deterministic, reproducible, compliance-grade results.** An LLM reviewer is non-deterministic: the same diff can surface different findings across runs. If you need a stable rule ID set, suppression baselines, and audit reproducibility, rule-based SAST is a better fit.
- **You need whole-codebase or scheduled deep scans.** It is diff-aware by design (PR changed files); it is not a crawler for finding latent vulns across an entire existing codebase the way a full SAST sweep is.
- **You want SARIF / third-party security-tab integration out of the box.** Output is PR comments plus a results JSON artifact; [未验证] there is no documented native SARIF export, so wiring it into GitHub's code-scanning UI is not turnkey.
- **No tagged releases.** Usage pins `@main`; there is no semver release line, so you trade stability for following an unpinned moving branch (or pin a commit SHA yourself).

## Comparison

| Alternative | In index | Tradeoff |
|---|---|---|
| [open-code-review](open-code-review.md) | ✅ | Alibaba LLM-based code reviewer for GitLab/coding-style + quality; this one is security-specific and Claude/GitHub-Actions-native. |
| [react-doctor](react-doctor.md) | ✅ | React-specific perf/correctness diagnostics, not a security reviewer; different problem entirely. |
| Semgrep | not indexed | Deterministic, rule-based SAST with SARIF and a huge community ruleset; fast, free, reproducible — but pattern-bound, weaker on logic/contextual bugs. |
| GitHub CodeQL | not indexed | Deep dataflow/taint analysis, native code-scanning UI, free for public repos; per-language, heavier setup, no LLM remediation prose. |
| Claude Code GitHub Action (general) | not indexed | Anthropic's general-purpose Claude Action for PRs/coding; not specialized for security audit or finding-filtering. |
| Snyk Code | not indexed | Commercial ML/SAST with a managed dashboard and dependency scanning; hosted SaaS, not a single-repo OSS Action. |

## Tech stack

- **Language:** Python (≈89.6% of repo per GitHub; with some TypeScript/JavaScript for tooling). [未验证] percentages are language-bar snapshots and drift.
- **Runtime model:** Claude (Claude Code) — default `claude-opus-4-1-20250805`, configurable via the `claude-model` input.
- **Delivery:** a composite GitHub Action (`anthropics/claude-code-security-review@main`) plus a `/security-review` Claude Code slash command.
- **Core modules:** `github_action_audit.py` (main audit), `prompts.py` (audit prompt templates), `findings_filter.py` (false-positive filtering), `claude_api_client.py` (API client), `json_parser.py` (robust JSON parsing), `evals/` (eval tooling).
- **Testing:** `pytest claudecode -v`.

## Dependencies

- **Required:** an Anthropic Claude API key (must be enabled for both Claude API and Claude Code) supplied as `claude-api-key` / a GitHub secret.
- **Platform:** GitHub repository with Actions enabled (primary path); can also run locally via the evals framework.
- **Permissions:** workflow needs `pull-requests: write` (to comment) and `contents: read`.
- **Python deps:** `claudecode/requirements.txt` is lightweight — `PyGithub>=1.59.0`, `requests>=2.28.0`, `anthropic>=0.39.0` (parsing uses stdlib). No heavy ML stack, because inference is remote.
- **Claude CLI:** the `claude` command-line tool must be installed separately (the Action handles this); analysis is driven through it, not only the raw API.

## Ops difficulty

**Low.** The happy path is a ~15-line workflow file and one secret — no servers, no datastore, no model to host (inference is the remote Claude API). Ongoing maintenance is mostly two things: cost control (token spend scales with PR volume and `run-every-commit`; mind the 20-min `claudecode-timeout`) and the prompt-injection constraint (you must configure fork/external-contributor approval gating). Tuning the false-positive filter or custom scan instructions is optional file-based config. The main residual risk is operational, not infra: pinning `@main` means upstream changes can alter behavior without a version bump.

## Caveats (unverified)

- [未验证] `gh` reports `latestRelease: null` and ~5.37k stars as of 2026-02 (last push 2026-02-11); GitHub stars are unreliable and date-sensitive — treat as indicative only.
- [未验证] No documented native SARIF / GitHub code-scanning export; integrating findings into the security tab may require custom glue.
- [未验证] Repo language breakdown (≈89.6% Python / 7.2% TS / 3.2% JS) is a GitHub snapshot and shifts over time.
- [推断] Default model `claude-opus-4-1-20250805` is the README default at time of writing and may be bumped upstream; verify the current default before relying on a specific model/cost profile.
- [推断] Per-run cost and latency depend on diff size, chosen model, and `run-every-commit`; no first-party cost figure is published here.
- [未验证] `claudecode/requirements.txt` (verified 2026-06-26) pins only `PyGithub>=1.59.0`, `requests>=2.28.0`, `anthropic>=0.39.0`; a note states the `claude` CLI must be installed separately — upstream may add deps later.
