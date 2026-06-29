#!/usr/bin/env python3
"""Generate a JoJo Stand-stats HEALTH radar card (SVG) from a page's `health:` block.

PURE / OFFLINE: reads the SSOT `health:` block already present in a page's YAML
frontmatter and renders an SVG to assets/health/<slug>.svg. Never hits the network
(scoring lives in tools/health.py). Safe to run in a pre-commit hook.

Usage:
  python3 tools/health_card.py categories/<cat>/<slug>.md [more pages...]
  python3 tools/health_card.py --all          # every page that carries a health: block
"""
from __future__ import annotations
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "health"

# grade -> (radius fraction, color)
TIER = {
    "A": (1.00, "#E5B80B"),  # gold
    "B": (0.80, "#3FB950"),  # green
    "C": (0.60, "#D4C20A"),  # yellow
    "D": (0.40, "#E8702A"),  # orange
    "E": (0.20, "#E5484D"),  # red
    "?": (0.50, "#8B949E"),  # gray (excluded from area)
}
# axis key -> (ZH label, JoJo EN vertex); order = top, then clockwise
AXES = [
    ("maintenance", "维护", "POWER"),
    ("responsiveness", "响应", "SPEED"),
    ("adoption", "采用", "RANGE"),
    ("longevity", "寿命", "STAYING"),
    ("governance", "治理", "PRECISION"),
    ("risk_license", "风险", "DURABILITY"),
]

W, H = 820, 500
CX, CY, R = 250, 268, 150
CJK = "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC',sans-serif"
DISP = "'Georgia','Times New Roman',serif"


# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text: str) -> dict:
    """Minimal indent-based YAML subset parser (mappings + scalars).

    Enough for the fixed `health:` block shape; no pip deps. Inline lists
    (e.g. tags) are kept as raw strings — the card doesn't need them.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip("\n")
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, val = line.strip().partition(":")
        key, val = key.strip(), val.strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if val == "":
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = val.strip().strip('"').strip("'")
    return root


def _vertex(i: int, frac: float) -> tuple[float, float]:
    ang = math.radians(-90 + 60 * i)
    return CX + R * frac * math.cos(ang), CY + R * frac * math.sin(ang)


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- renderer
def render(name: str, subtitle: str, grades: list[str], overall: str,
           note: str, flags: list[str]) -> str:
    oc = TIER.get(overall, TIER["?"])[1]
    s: list[str] = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" font-family="{CJK}">')
    s.append("<defs>")
    s.append('<radialGradient id="bg" cx="32%" cy="40%" r="80%">'
             '<stop offset="0%" stop-color="#241a0e"/>'
             '<stop offset="55%" stop-color="#15110b"/>'
             '<stop offset="100%" stop-color="#000000"/></radialGradient>')
    s.append(f'<linearGradient id="poly" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0%" stop-color="{oc}" stop-opacity="0.85"/>'
             f'<stop offset="100%" stop-color="{oc}" stop-opacity="0.32"/></linearGradient>')
    s.append('<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">'
             '<feGaussianBlur stdDeviation="5" result="b"/><feMerge>'
             '<feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    s.append(f'<radialGradient id="halo" cx="50%" cy="50%" r="50%">'
             f'<stop offset="0%" stop-color="{oc}" stop-opacity="0.30"/>'
             f'<stop offset="70%" stop-color="{oc}" stop-opacity="0.05"/>'
             f'<stop offset="100%" stop-color="{oc}" stop-opacity="0"/></radialGradient>')
    s.append("</defs>")
    s.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>')
    s.append(f'<rect x="7" y="7" width="{W-14}" height="{H-14}" rx="13" fill="none" '
             f'stroke="{oc}" stroke-opacity="0.55" stroke-width="2"/>')
    s.append(f'<rect x="12" y="12" width="{W-24}" height="{H-24}" rx="9" fill="none" '
             f'stroke="#C9A227" stroke-opacity="0.35" stroke-width="1"/>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R+40}" fill="url(#halo)"/>')

    # tier rings + spokes
    for frac in (1.0, 0.8, 0.6, 0.4, 0.2):
        pts = " ".join(f"{_vertex(i, frac)[0]:.1f},{_vertex(i, frac)[1]:.1f}" for i in range(6))
        s.append(f'<polygon points="{pts}" fill="none" stroke="#6b5a33" '
                 f'stroke-opacity="0.40" stroke-width="1"/>')
    for i in range(6):
        x, y = _vertex(i, 1.0)
        s.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" '
                 f'stroke="#6b5a33" stroke-opacity="0.35" stroke-width="1"/>')
    for j, g in enumerate("ABCDE"):
        ly = CY - R * (1.0 - j * 0.2) + 4
        s.append(f'<text x="{CX+9}" y="{ly:.1f}" font-size="10" fill="#7d6a3c" '
                 f'font-family="{DISP}">{g}</text>')

    # data polygon
    pts = [_vertex(i, TIER.get(grades[i], TIER["?"])[0]) for i in range(6)]
    fillpts = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    s.append(f'<polygon points="{fillpts}" fill="url(#poly)" filter="url(#glow)"/>')
    for i in range(6):
        a, b = pts[i], pts[(i + 1) % 6]
        if grades[i] == "?" or grades[(i + 1) % 6] == "?":
            s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                     f'stroke="#8B949E" stroke-width="2" stroke-dasharray="4 4" stroke-opacity="0.9"/>')
        else:
            s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                     f'stroke="{oc}" stroke-width="2.5"/>')
    for i in range(6):
        x, y = pts[i]
        g = grades[i]
        if g == "?":
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#15110b" '
                     f'stroke="#8B949E" stroke-width="2" stroke-dasharray="2 2"/>')
        else:
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{TIER[g][1]}" '
                     f'stroke="#000" stroke-width="0.8"/>')

    # axis labels
    for i, (_key, zh, en) in enumerate(AXES):
        lx, ly = _vertex(i, 1.0)
        ang = math.radians(-90 + 60 * i)
        ox, oy = lx + 30 * math.cos(ang), ly + 30 * math.sin(ang)
        anchor = "middle"
        if math.cos(ang) > 0.3:
            anchor = "start"
        elif math.cos(ang) < -0.3:
            anchor = "end"
        g = grades[i]
        col = TIER.get(g, TIER["?"])[1]
        s.append(f'<text x="{ox:.1f}" y="{oy-3:.1f}" font-size="15" font-weight="700" '
                 f'fill="#efe6d2" text-anchor="{anchor}">{zh} '
                 f'<tspan fill="{col}" font-family="{DISP}" font-weight="700">{g}</tspan></text>')
        s.append(f'<text x="{ox:.1f}" y="{oy+10:.1f}" font-size="8" letter-spacing="1.5" '
                 f'fill="#8a7c5a" text-anchor="{anchor}" font-family="{DISP}">{en}</text>')

    # right panel
    px = 500
    s.append(f'<text x="{px}" y="60" font-size="12" letter-spacing="3" fill="#C9A227" '
             f'font-family="{DISP}">[ HEALTH / 健康度 ]</text>')
    s.append(f'<text x="{px}" y="98" font-size="26" font-weight="700" fill="#fbf4e2" '
             f'font-family="{DISP}">{_esc(name)}</text>')
    s.append(f'<text x="{px}" y="120" font-size="12" fill="#9c8e6c">{_esc(subtitle)}</text>')
    s.append(f'<text x="{px}" y="210" font-size="96" font-weight="700" fill="{oc}" '
             f'font-family="{DISP}" filter="url(#glow)">{overall}</text>')
    tail = f" · {_esc(note)}" if note else ""
    s.append(f'<text x="{px+8}" y="234" font-size="12" letter-spacing="2" fill="#9c8e6c" '
             f'font-family="{DISP}">OVERALL · 总评{tail}</text>')
    y0 = 280
    for i, (_key, zh, en) in enumerate(AXES):
        yy = y0 + i * 30
        g = grades[i]
        col = TIER.get(g, TIER["?"])[1]
        s.append(f'<text x="{px}" y="{yy}" font-size="14" fill="#cdbf9d">{zh}</text>')
        s.append(f'<text x="{px+70}" y="{yy}" font-size="9" letter-spacing="1" fill="#7d6f50" '
                 f'font-family="{DISP}">{en}</text>')
        bx, bw = px + 150, 120
        s.append(f'<rect x="{bx}" y="{yy-11}" width="{bw}" height="9" rx="4" fill="#2a2417"/>')
        if g != "?":
            s.append(f'<rect x="{bx}" y="{yy-11}" width="{bw*TIER[g][0]:.0f}" height="9" rx="4" '
                     f'fill="{col}"/>')
        else:
            s.append(f'<rect x="{bx}" y="{yy-11}" width="{bw}" height="9" rx="4" fill="none" '
                     f'stroke="#8B949E" stroke-dasharray="3 3"/>')
        s.append(f'<text x="{bx+bw+12}" y="{yy}" font-size="15" font-weight="700" fill="{col}" '
                 f'font-family="{DISP}">{g}</text>')
    fy = y0 + 6 * 30 + 6
    fx = px
    for fl in flags:
        bw = 9 * len(fl) + 18
        s.append(f'<rect x="{fx}" y="{fy-13}" width="{bw}" height="20" rx="10" fill="#1d1810" '
                 f'stroke="#C9A227" stroke-opacity="0.4"/>')
        s.append(f'<text x="{fx+bw/2}" y="{fy+1}" font-size="11" fill="#cdbf9d" '
                 f'text-anchor="middle">{_esc(fl)}</text>')
        fx += bw + 8
    s.append("</svg>")
    return "\n".join(s)


# ---------------------------------------------------------------- page -> card
def card_for_page(page: Path) -> Path | None:
    fm = parse_frontmatter(page.read_text(encoding="utf-8"))
    health = fm.get("health")
    if not isinstance(health, dict):
        return None
    axes = health.get("axes", {})
    grades = [str(axes.get(key, {}).get("grade", "?")) for key, _zh, _en in AXES]
    overall = str(health.get("overall", "?"))
    name = str(fm.get("name", page.stem))
    subtitle = f"{fm.get('type', '')} · {fm.get('category', '')}".strip(" ·")

    # auto flags from the SSOT raw values
    flags: list[str] = []
    risk_raw = axes.get("risk_license", {}).get("raw", {})
    spdx = risk_raw.get("spdx_id") if isinstance(risk_raw, dict) else None
    maint_raw = axes.get("maintenance", {}).get("raw", {})
    archived = isinstance(maint_raw, dict) and str(maint_raw.get("archived", "")).lower() == "true"
    if archived:
        flags.append("⚠ archived")
    if spdx:
        flags.append(str(spdx))
    note = ""
    if str(health.get("capped", "")).lower() == "true":
        note = str(health.get("cap_reason") or "license-capped")

    svg = render(name, subtitle, grades, overall, note, flags[:3])
    ASSETS.mkdir(parents=True, exist_ok=True)
    out = ASSETS / f"{fm.get('slug', page.stem)}.svg"
    out.write_text(svg, encoding="utf-8")
    return out


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--all":
        pages = [p for p in (ROOT / "categories").rglob("*.md")
                 if not p.name.endswith(".zh.md") and p.name != "INDEX.md"]
    else:
        pages = [Path(a) if Path(a).is_absolute() else ROOT / a for a in argv]
    n = 0
    for page in pages:
        out = card_for_page(page)
        if out:
            print(f"wrote {out.relative_to(ROOT)}")
            n += 1
    print(f"{n} card(s) generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
