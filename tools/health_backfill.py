#!/usr/bin/env python3
"""Operational backfill runner for oss-atlas health radar blocks.

Safe defaults:
  - dry-run by default; writes only with --apply --yes
  - processes only EN project pages missing health: by default
  - records resumable state under .health-backfill/state.json
  - runs one page at a time to respect GitHub/package-registry rate limits
"""
from __future__ import annotations

import argparse
import json
import os.path
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STATE = ROOT / ".health-backfill" / "state.json"


@dataclass(frozen=True)
class PageItem:
    path: Path
    has_health: bool
    has_card: bool
    card_exists: bool


@dataclass(frozen=True)
class BackfillState:
    done: set[str]
    failed: dict[str, dict]


@dataclass(frozen=True)
class BackfillPlan:
    total: int
    existing_health: int
    missing_health: int
    resume_skipped: int
    items_to_process: list[PageItem]


def rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def has_health_block(page: Path) -> bool:
    return any(line == "health:" for line in frontmatter(page.read_text(encoding="utf-8")).splitlines())


def slug_from_page(page: Path) -> str:
    name = page.name
    return name[: -len(".zh.md")] if name.endswith(".zh.md") else name[: -len(".md")]


def duplicate_slugs(root: Path) -> set[str]:
    counts: dict[str, int] = {}
    for page in discover_pages(root):
        counts[page.stem] = counts.get(page.stem, 0) + 1
    return {slug for slug, count in counts.items() if count > 1}


def card_stem_for_page(page: Path, root: Path) -> str:
    slug = slug_from_page(page)
    if slug not in duplicate_slugs(root):
        return slug
    try:
        rel_parent = page.parent.relative_to(root / "categories")
    except ValueError:
        return slug
    return f"{'-'.join(rel_parent.parts)}-{slug}"


def card_ref_for_page(page: Path, root: Path) -> str:
    stem = card_stem_for_page(page, root)
    card = f"{stem}.zh.svg" if page.name.endswith(".zh.md") else f"{stem}.svg"
    target = root / "assets" / "health" / card
    return os.path.relpath(target, start=page.parent)


def has_card_embed(page: Path, root: Path) -> bool:
    return card_ref_for_page(page, root) in page.read_text(encoding="utf-8")


def has_card_file(page: Path, root: Path) -> bool:
    stem = card_stem_for_page(page, root)
    cards = root / "assets" / "health"
    return (cards / f"{stem}.svg").exists() and (cards / f"{stem}.zh.svg").exists()


def discover_pages(root: Path) -> list[Path]:
    pages = []
    for page in sorted((root / "categories").rglob("*.md")):
        if page.name.startswith("INDEX") or page.name.endswith(".zh.md"):
            continue
        pages.append(page)
    return pages


def load_state(path: Path) -> BackfillState:
    if not path.exists():
        return BackfillState(done=set(), failed={})
    data = json.loads(path.read_text(encoding="utf-8"))
    return BackfillState(done=set(data.get("done", [])), failed=dict(data.get("failed", {})))


def save_state(path: Path, state: BackfillState) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "done": sorted(state.done),
        "failed": state.failed,
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def build_plan(root: Path, limit: int | None, resume_state: BackfillState | None, *, force: bool = False) -> BackfillPlan:
    pages = [
        PageItem(path=p, has_health=has_health_block(p), has_card=has_card_embed(p, root), card_exists=has_card_file(p, root))
        for p in discover_pages(root)
    ]
    done = resume_state.done if resume_state else set()
    items: list[PageItem] = []
    resume_skipped = 0
    for item in pages:
        r = rel(item.path, root)
        if r in done and item.has_health and item.has_card and item.card_exists and not force:
            resume_skipped += 1
            continue
        if item.has_health and item.has_card and item.card_exists and not force:
            continue
        items.append(item)
    if limit is not None:
        items = items[:limit]
    return BackfillPlan(
        total=len(pages),
        existing_health=sum(1 for p in pages if p.has_health),
        missing_health=sum(1 for p in pages if not p.has_health),
        resume_skipped=resume_skipped,
        items_to_process=items,
    )


def run_cmd(cmd: list[str], *, timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)


def zh_sibling(page: Path) -> Path:
    return page.with_name(page.name[: -len(".md")] + ".zh.md")


def card_markdown_for_page(page: Path, root: Path) -> str:
    slug = slug_from_page(page)
    label = "健康度雷达" if page.name.endswith(".zh.md") else "health radar"
    return f"![{slug} — {label}]({card_ref_for_page(page, root)})"


def ensure_card_embed(page: Path, root: Path) -> bool:
    text = page.read_text(encoding="utf-8")
    card_ref = card_ref_for_page(page, root)
    card_md = card_markdown_for_page(page, root)
    if card_ref in text:
        return False
    slug = slug_from_page(page)
    old_card_line = re_health_card_line(slug, zh=page.name.endswith(".zh.md"))
    updated, n = old_card_line.subn(card_md, text, count=1)
    if n:
        page.write_text(updated, encoding="utf-8")
        return True
    if not text.startswith("---"):
        raise ValueError(f"missing frontmatter: {page}")
    fm_end = text.find("\n---", 3)
    if fm_end == -1:
        raise ValueError(f"unterminated frontmatter: {page}")
    body_start = text.find("\n", fm_end + 4)
    prefix = text[: body_start + 1]
    body = text[body_start + 1 :]
    lines = body.splitlines()
    h1_idx = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if h1_idx is None:
        raise ValueError(f"missing H1: {page}")
    tldr_start = next((i for i in range(h1_idx + 1, len(lines)) if lines[i].strip()), None)
    if tldr_start is None:
        raise ValueError(f"missing TL;DR after H1: {page}")
    tldr_end = next((i for i in range(tldr_start + 1, len(lines)) if not lines[i].strip()), len(lines))
    insert_at = tldr_end + 1
    new_lines = lines[:insert_at] + [card_md, ""] + lines[insert_at:]
    page.write_text(prefix + "\n".join(new_lines) + ("\n" if body.endswith("\n") else ""), encoding="utf-8")
    return True


def re_health_card_line(slug: str, *, zh: bool):
    import re
    label = "健康度雷达" if zh else "health radar"
    return re.compile(rf"^!\[{re.escape(slug)} — {re.escape(label)}\]\([^)]*assets/health/[^)]*\.svg\)$", re.MULTILINE)


def score_one(page: Path, *, has_health: bool, timeout: int, retries: int, sleep: float) -> tuple[bool, dict]:
    page_arg = rel(page, ROOT)
    commands = [[sys.executable, "tools/health_card.py", page_arg, rel(zh_sibling(page), ROOT)]]
    if not has_health:
        commands.insert(0, [sys.executable, "tools/health.py", "--page", page_arg, "--write"])
    attempt = 0
    last: dict = {}
    while attempt <= retries:
        attempt += 1
        for cmd in commands:
            started = time.monotonic()
            try:
                cp = run_cmd(cmd, timeout=timeout)
            except subprocess.TimeoutExpired as exc:
                last = {"attempt": attempt, "cmd": cmd, "returncode": "timeout", "stderr": str(exc)}
                break
            elapsed = round(time.monotonic() - started, 2)
            if cp.returncode != 0:
                last = {"attempt": attempt, "cmd": cmd, "returncode": cp.returncode, "stderr": cp.stderr[-2000:], "elapsed_sec": elapsed}
                break
        else:
            ensure_card_embed(page, ROOT)
            ensure_card_embed(zh_sibling(page), ROOT)
            return True, {"attempt": attempt}
        if attempt <= retries:
            time.sleep(max(sleep, 1.0) * attempt)
    return False, last


def eta(done: int, total: int, started: float) -> str:
    if done == 0:
        return "unknown"
    elapsed = time.monotonic() - started
    remaining = (elapsed / done) * max(total - done, 0)
    return f"{remaining / 60:.1f}m"


def print_plan(plan: BackfillPlan, root: Path, *, sample_size: int = 8) -> None:
    print("phase=dry-run")
    print(f"total_en_pages={plan.total}")
    print(f"existing_health={plan.existing_health}")
    print(f"missing_health={plan.missing_health}")
    print(f"resume_skipped={plan.resume_skipped}")
    print(f"planned_to_process={len(plan.items_to_process)}")
    print("sample_to_process:")
    for item in plan.items_to_process[:sample_size]:
        print(f"  - {rel(item.path, root)}")
    if len(plan.items_to_process) > sample_size:
        print(f"  ... {len(plan.items_to_process) - sample_size} more")


def apply_plan(plan: BackfillPlan, root: Path, state_path: Path, state: BackfillState, *, timeout: int, retries: int, sleep: float) -> int:
    total = len(plan.items_to_process)
    started = time.monotonic()
    done_now = failed_now = 0
    for idx, item in enumerate(plan.items_to_process, 1):
        r = rel(item.path, root)
        pct = (idx / total * 100) if total else 100
        print(f"phase=apply current={idx}/{total} pct={pct:.1f} eta={eta(idx - 1, total, started)} page={r}", flush=True)
        ok, info = score_one(item.path, has_health=item.has_health, timeout=timeout, retries=retries, sleep=sleep)
        if ok:
            state.done.add(r)
            state.failed.pop(r, None)
            done_now += 1
            print(f"status=done page={r} attempt={info.get('attempt')}", flush=True)
        else:
            state.failed[r] = info
            failed_now += 1
            print(f"status=failed page={r} reason={info.get('returncode')}", flush=True)
        save_state(state_path, state)
        if sleep:
            time.sleep(sleep)
    print(f"summary done_now={done_now} failed_now={failed_now} state={state_path}")
    return 1 if failed_now else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Backfill health: blocks across oss-atlas pages with resume/progress.")
    ap.add_argument("--apply", action="store_true", help="write health: blocks and SVG cards; default is dry-run")
    ap.add_argument("--yes", action="store_true", help="confirm --apply for non-interactive runs")
    ap.add_argument("--resume", action="store_true", help="load state and skip pages already marked done")
    ap.add_argument("--force", action="store_true", help="process pages even if they already have health:")
    ap.add_argument("--limit", type=int, help="process only the first N planned pages")
    ap.add_argument("--sleep", type=float, default=2.0, help="seconds to sleep between pages and retry backoff base")
    ap.add_argument("--timeout", type=int, default=180, help="per-command timeout in seconds")
    ap.add_argument("--retries", type=int, default=1, help="retries per page after command failure/timeout")
    ap.add_argument("--state", type=Path, default=DEFAULT_STATE, help="checkpoint JSON path")
    args = ap.parse_args(argv)

    state = load_state(args.state) if args.resume or args.apply else BackfillState(done=set(), failed={})
    plan = build_plan(ROOT, args.limit, state if args.resume else None, force=args.force)
    print_plan(plan, ROOT)

    if not args.apply:
        print("apply_ready=false reason=dry-run-only add '--apply --yes' to write")
        return 0
    if not args.yes:
        print("apply_ready=false reason=--apply requires --yes", file=sys.stderr)
        return 2
    return apply_plan(plan, ROOT, args.state, state, timeout=args.timeout, retries=args.retries, sleep=args.sleep)


if __name__ == "__main__":
    raise SystemExit(main())
