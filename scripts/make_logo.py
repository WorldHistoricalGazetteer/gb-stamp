"""Generate the GB-STAMP logo + favicon: a Victorian postage stamp (perforated edge, cameo profile,
engraved frame). Writes docs/assets/logo.svg and docs/assets/favicon.svg."""
import os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARMINE, CREAM, CAMEO = "#a5322e", "#f4ecdb", "#87231f"

# Great Britain mainland outline (Natural Earth 1:50m, aspect-corrected, portrait 53.5 x 100).
GBW = 53.5
GB_PATH = open(f"{HERE}/reference/gb_outline_path.txt").read().strip()

def perf_mask(x0, y0, x1, y1, r, nh, nv, rx=6):
    circ = []
    for i in range(nh + 1):
        x = x0 + (x1 - x0) * i / nh
        circ += [(x, y0), (x, y1)]
    for j in range(1, nv):
        y = y0 + (y1 - y0) * j / nv
        circ += [(x0, y), (x1, y)]
    holes = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="black"/>' for x, y in circ)
    return (f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="{rx}" fill="white"/>{holes}')

def logo():
    W, H = 240, 288
    bx0, by0, bx1, by1 = 20, 20, 220, 268
    mask = perf_mask(bx0, by0, bx1, by1, 7, 12, 15)
    fx0, fy0, fx1, fy1 = 34, 34, 206, 254        # inner frame
    corners = "".join(f'<rect x="{x-3}" y="{y-3}" width="6" height="6" fill="{CREAM}" transform="rotate(45 {x} {y})"/>'
                      for x in (fx0, fx1) for y in (fy0, fy1))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="GB-STAMP">
<defs><mask id="perf">{mask}</mask></defs>
<rect x="{bx0}" y="{by0}" width="{bx1-bx0}" height="{by1-by0}" rx="6" fill="{CARMINE}" mask="url(#perf)"/>
<g mask="url(#perf)">
  <rect x="{fx0}" y="{fy0}" width="{fx1-fx0}" height="{fy1-fy0}" fill="none" stroke="{CREAM}" stroke-width="2.4"/>
  <rect x="{fx0+5}" y="{fy0+5}" width="{fx1-fx0-10}" height="{fy1-fy0-10}" fill="none" stroke="{CREAM}" stroke-width="1"/>
  {corners}
  <text x="120" y="58" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-weight="700"
        font-size="21" letter-spacing="2" fill="{CREAM}">GB&#8226;STAMP</text>
  <path d="{GB_PATH}" fill="{CREAM}" transform="translate(81 77) scale(1.46)"/>
  <text x="120" y="240" text-anchor="middle" font-family="Georgia,serif" font-style="italic"
        font-size="12.5" letter-spacing="1" fill="{CREAM}">OS Six-Inch &#183; c.1900</text>
</g>
</svg>'''

def favicon():
    W = 64
    mask = perf_mask(4, 4, 60, 60, 3.4, 9, 9, rx=3)
    s = 52 / 100.0                                # GB fills most of the stamp for 16px legibility
    tx, ty = 32 - GBW * s / 2, 33 - 52 / 2        # centre at (32,33)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" role="img" aria-label="GB-STAMP">
<defs><mask id="pf">{mask}</mask></defs>
<rect x="4" y="4" width="56" height="56" rx="3" fill="{CARMINE}" mask="url(#pf)"/>
<path d="{GB_PATH}" fill="{CREAM}" transform="translate({tx:.1f} {ty:.1f}) scale({s:.3f})"/>
</svg>'''

os.makedirs(f"{HERE}/docs/assets", exist_ok=True)
open(f"{HERE}/docs/assets/logo.svg", "w").write(logo())
open(f"{HERE}/docs/assets/favicon.svg", "w").write(favicon())
print("wrote docs/assets/logo.svg + favicon.svg")
