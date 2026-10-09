#!/usr/bin/env python3
"""自绘暗黑极简 SVG —— 零外部依赖服务。
数据来源：GitHub GraphQL / REST（由 workflow 注入 gh_*.json）
输出：可直接被 GitHub README 引用的静态 SVG。
"""
import json, os, math, datetime, pathlib

OUT = pathlib.Path("assets"); OUT.mkdir(exist_ok=True)

BG      = "#08090c"
PANEL   = "#0d1017"
BORDER  = "#1c2230"
GRID    = "#141922"
DIM     = "#3d4757"
MUTED   = "#6e7b8f"
TEXT    = "#c8d3e3"
ACCENT  = "#4ee39b"
ACCENT2 = "#3b82f6"
WARN    = "#f59e0b"

MONO = "ui-monospace,'SF Mono','Cascadia Code','JetBrains Mono',Consolas,monospace"

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

def head(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">'
            f'<title>{esc(title)}</title>'
            f'<style>text{{font-family:{MONO};}}</style>')

# ─────────────────────────  1. 终端头部  ─────────────────────────
def terminal_header(user, name, tagline):
    w, h = 900, 210
    lines = [
        (f"{user}@{user}", ACCENT,  " ~ % ", MUTED, "whoami"),
        ("",              TEXT,    "",      TEXT,  name),
        ("",              TEXT,    "",      TEXT,  tagline),
    ]
    s = [head(w, h, "terminal header")]
    s.append(f'<rect width="{w}" height="{h}" fill="{BG}"/>')
    s.append(f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    # 窗口控制点
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        s.append(f'<circle cx="{28+i*20}" cy="26" r="6" fill="{c}" opacity=".85"/>')
    s.append(f'<line x1="0" y1="48" x2="{w}" y2="48" stroke="{BORDER}"/>')
    y = 82
    for prompt, pc, sep, sc, cmd in lines:
        if prompt:
            s.append(f'<text x="28" y="{y}" font-size="15" fill="{pc}">{esc(prompt)}</text>')
            x = 28 + len(prompt) * 9.0
            s.append(f'<text x="{x:.0f}" y="{y}" font-size="15" fill="{sc}">{esc(sep)}</text>')
            x += len(sep) * 9.0
            s.append(f'<text x="{x:.0f}" y="{y}" font-size="15" fill="{TEXT}" font-weight="600">{esc(cmd)}</text>')
        else:
            s.append(f'<text x="28" y="{y}" font-size="15" fill="{TEXT}">{esc(cmd)}</text>')
        y += 30
    # 光标
    s.append(f'<rect x="28" y="{h-34}" width="9" height="17" fill="{ACCENT}">'
             f'<animate attributeName="opacity" values="1;0;1" dur="1.15s" repeatCount="indefinite"/></rect>')
    s.append("</svg>")
    (OUT / "header.svg").write_text("".join(s), encoding="utf-8")

# ─────────────────────────  2. 贡献热力条  ─────────────────────────
def heatmap(cal, user):
    """按 GitHub 原生布局：列=周，行=星期（7 行）。
    宽度随周数自适应，图例固定在右上，日期单独占底部一行。
    """
    weeks = cal["weeks"]
    ncols = len(weeks)
    cw, gap, rows = 11, 3.5, 7
    left, top = 30, 58
    grid_w = ncols * (cw + gap)
    w = max(900, int(grid_w + left * 2))
    grid_h = rows * (cw + gap)
    h = int(top + grid_h + 46)
    maxc = max((d["contributionCount"] for wk in weeks for d in wk["contributionDays"]), default=1) or 1

    s = [head(w, h, "contribution heatmap")]
    s.append(f'<rect width="{w}" height="{h}" fill="{BG}"/>')
    s.append(f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    s.append(f'<text x="{left}" y="32" font-size="12" fill="{MUTED}" letter-spacing="1.5">CONTRIBUTIONS</text>')
    s.append(f'<text x="{w-left}" y="32" font-size="12" fill="{ACCENT}" text-anchor="end" font-weight="600">'
             f'{cal["totalContributions"]} TOTAL</text>')

    # 列 = 周，行 = 星期
    for ci, wk in enumerate(weeks):
        for ri, d in enumerate(wk["contributionDays"]):
            c = d["contributionCount"]
            col, op = (GRID, "1") if c == 0 else (ACCENT, f"{0.22 + 0.78*(c/maxc):.2f}")
            x = left + ci * (cw + gap)
            y = top + ri * (cw + gap)
            s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw}" height="{cw}" rx="2.5" '
                     f'fill="{col}" opacity="{op}"><title>{d["date"]}: {c}</title></rect>')

    # 图例：独立一行，避开网格与日期
    ly = h - 30
    s.append(f'<text x="{left}" y="{ly+10}" font-size="11" fill="{DIM}">less</text>')
    for i in range(5):
        s.append(f'<rect x="{left+36+i*17}" y="{ly}" width="11" height="11" rx="2.5" '
                 f'fill="{ACCENT}" opacity="{0.22 + 0.195*i:.2f}"/>')
    s.append(f'<text x="{left+36+5*17+6}" y="{ly+10}" font-size="11" fill="{DIM}">more</text>')
    s.append(f'<text x="{w-left}" y="{ly+10}" font-size="11" fill="{DIM}" text-anchor="end">'
             f'{weeks[0]["contributionDays"][0]["date"]} → {weeks[-1]["contributionDays"][-1]["date"]}</text>')
    s.append("</svg>")
    (OUT / "heatmap.svg").write_text("".join(s), encoding="utf-8")

def compute_streak(cal):
    """当前连续提交天数（末尾往前数）。"""
    days = [d for wk in cal["weeks"] for d in wk["contributionDays"]]
    streak = 0
    for d in reversed(days):
        if d["contributionCount"] > 0:
            streak += 1
        else:
            break
    return streak

# ─────────────────────────  3. 语言条  ─────────────────────────
def stackbar(items):
    """技术栈标签行 —— 极简风里比语言饼图更贴，也避开历史仓库占比的误导。"""
    w = 900
    tag_h, gap_x, gap_y = 26, 8, 10
    left, top, max_x = 30, 52, w - 30

    # 先排布算高度，再绘制（避免底部留白）
    def text_w(s):
        # 中日韩按双宽估算，其余按等宽字符宽度
        return sum(2 if ord(c) > 0x2E80 else 1 for c in s)

    placed, x, y = [], left, top
    for label, kind in items:
        tw = 18 + text_w(label) * 8.2
        if x + tw > max_x and x > left:
            x = left; y += tag_h + gap_y
        placed.append((label, kind, x, y, tw))
        x += tw + gap_x
    h = int(y + tag_h + 30)

    s = [head(w, h, "stack")]
    s.append(f'<rect width="{w}" height="{h}" fill="{BG}"/>')
    s.append(f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    s.append(f'<text x="{left}" y="28" font-size="12" fill="{MUTED}" letter-spacing="1.5">STACK</text>')
    for label, kind, tx, ty, tw in placed:
        stroke, fg = BORDER, MUTED
        if kind == "core":
            stroke, fg = ACCENT, ACCENT
        elif kind == "active":
            stroke, fg = ACCENT2, ACCENT2
        s.append(f'<rect x="{tx:.1f}" y="{ty}" width="{tw:.1f}" height="{tag_h}" rx="6" '
                 f'fill="none" stroke="{stroke}"/>')
        s.append(f'<text x="{tx+tw/2:.1f}" y="{ty+17}" font-size="12" fill="{fg}" '
                 f'text-anchor="middle">{esc(label)}</text>')
    s.append("</svg>")
    (OUT / "stack.svg").write_text("".join(s), encoding="utf-8")

# ─────────────────────────  4. 指标行  ─────────────────────────
def metrics(stats):
    w, h = 900, 96
    items = list(stats.items())[:4]
    s = [head(w, h, "metrics")]
    s.append(f'<rect width="{w}" height="{h}" fill="{BG}"/>')
    s.append(f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    cw = (w - 2) / max(len(items), 1)
    for i, (k, v) in enumerate(items):
        cx = cw * i + cw / 2
        if i: s.append(f'<line x1="{cw*i:.0f}" y1="22" x2="{cw*i:.0f}" y2="{h-22}" stroke="{BORDER}"/>')
        s.append(f'<text x="{cx:.0f}" y="46" font-size="26" fill="{ACCENT}" text-anchor="middle" font-weight="700">{esc(v)}</text>')
        s.append(f'<text x="{cx:.0f}" y="68" font-size="11" fill="{MUTED}" text-anchor="middle" letter-spacing="1.2">{esc(k)}</text>')
    s.append("</svg>")
    (OUT / "metrics.svg").write_text("".join(s), encoding="utf-8")

if __name__ == "__main__":
    data = json.loads(pathlib.Path("gh_data.json").read_text(encoding="utf-8"))
    data["metrics"]["STREAK"] = compute_streak(data["calendar"])
    terminal_header(data["user"], data["name"], data["tagline"])
    heatmap(data["calendar"], data["user"])
    stackbar(data["stack"])
    metrics(data["metrics"])
    print("generated:", sorted(p.name for p in OUT.glob("*.svg")))
