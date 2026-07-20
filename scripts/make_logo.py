"""Generate the GB-STAMP logo + favicon: a Victorian postage stamp (perforated edge, cameo profile,
engraved frame). Writes docs/assets/logo.svg and docs/assets/favicon.svg."""
import os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARMINE, CREAM, CAMEO = "#a5322e", "#f4ecdb", "#87231f"

# left-facing Victorian profile silhouette (fits a ~ x[74..152] y[90..206] box)
PROFILE = ("M126 90 C150 92 158 118 152 146 C150 166 148 176 146 186 L146 206 L98 206 L98 188 "
           "C96 180 92 176 90 170 C88 166 92 160 88 156 C80 154 82 148 90 148 C86 144 92 142 90 138 "
           "C78 136 74 132 86 128 C90 124 90 120 94 118 C96 108 100 96 126 90 Z")

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
  <ellipse cx="120" cy="150" rx="54" ry="66" fill="{CAMEO}" stroke="{CREAM}" stroke-width="2"/>
  <ellipse cx="120" cy="150" rx="49" ry="61" fill="none" stroke="{CREAM}" stroke-width="0.8"/>
  <path d="{PROFILE}" fill="{CREAM}"/>
  <text x="120" y="238" text-anchor="middle" font-family="Georgia,serif" font-style="italic"
        font-size="12.5" letter-spacing="1" fill="{CREAM}">OS Six-Inch &#183; c.1900</text>
  <text x="46" y="250" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="{CREAM}">1d</text>
  <text x="194" y="250" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="{CREAM}">1d</text>
</g>
</svg>'''

def favicon():
    W = 64
    mask = perf_mask(4, 4, 60, 60, 3.4, 9, 9, rx=3)
    # scale profile (src box ~ x74..152 y90..206 -> center 113,148 span 78x116) into ~ 16..48
    sc = 40 / 116.0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" role="img" aria-label="GB-STAMP">
<defs><mask id="pf">{mask}</mask></defs>
<rect x="4" y="4" width="56" height="56" rx="3" fill="{CARMINE}" mask="url(#pf)"/>
<g mask="url(#pf)">
  <ellipse cx="32" cy="33" rx="20" ry="23" fill="{CAMEO}" stroke="{CREAM}" stroke-width="1.4"/>
  <path d="{PROFILE}" fill="{CREAM}" transform="translate(32 33) scale({sc}) translate(-113 -148)"/>
</g>
</svg>'''

os.makedirs(f"{HERE}/docs/assets", exist_ok=True)
open(f"{HERE}/docs/assets/logo.svg", "w").write(logo())
open(f"{HERE}/docs/assets/favicon.svg", "w").write(favicon())
print("wrote docs/assets/logo.svg + favicon.svg")
