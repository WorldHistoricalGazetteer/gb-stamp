"""Generate docs/characteristic-sheets.md — the table of our Ordnance Survey Characteristic-Sheet
extraction: each writing category, its exemplar strip, its letterform/style, date regime, and (where
resolved) its Getty AAT mapping. Data: reference/os_categories.json (+ gb_stamp_aat_crosswalk.json)."""
import json, os, html

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cats = json.load(open(f"{HERE}/reference/os_categories.json"))["categories"]
xwalk = json.load(open(f"{HERE}/reference/gb_stamp_aat_crosswalk.json"))

STYLE = {"upright": "Upright roman", "italic": "Italic", "blackletter": "Blackletter (Gothic)",
         "caps": "Upright <b>CAPS</b>", "numeral": "Numeral", "roman": "Upright roman"}
GROUP_ORDER = ["admin", "settlement", "water", "antiquity", "relief", "communications", "other"]

EXDIR = f"{HERE}/docs/assets/exemplars"
EX = [f[3:-4] for f in os.listdir(EXDIR) if f.startswith("ex_") and f.endswith(".jpg")] if os.path.isdir(EXDIR) else []
def find_ex(key):
    """map a category key to the best-matching exemplar filename stem (names differ slightly)."""
    if key in EX: return key
    cands = [e for e in EX if e in key or key in e or e.startswith(key[:7]) or key.startswith(e[:7])]
    if not cands: return None
    return max(cands, key=lambda e: len(os.path.commonprefix([e, key])))

def aat_for(cat):
    key, label = cat["key"], cat["label"].lower()
    words = set(key.split("_")) | set(label.replace(",", " ").replace(".", " ").split())
    best = None
    for tok, entry in xwalk.items():
        tw = set(tok.split("_"))
        if tok in key or key in tok or (tw & words):
            b = entry.get("best")
            if b and b.get("aat_id") and (best is None or b["score"] > best["score"]):
                best = b
    return best

def regime(c):
    if c.get("recent_only"): return "‡ post-1879 (more recent maps)"
    if c.get("pre1879"): return "† pre-1879"
    return "any edition"

rows = []
for c in sorted(cats, key=lambda c: (GROUP_ORDER.index(c.get("group", "other")) if c.get("group") in GROUP_ORDER else 9, c["label"])):
    key = c["key"]; stem = find_ex(key); ex = f"assets/exemplars/ex_{stem}.jpg" if stem else None
    have = bool(stem)
    style = c.get("style") or ("caps" if str(c.get("letterform", "")).isupper() and len(str(c.get("letterform", ""))) <= 2 else "upright")
    aat = aat_for(c)
    aat_cell = (f'<a href="http://vocab.getty.edu/page/aat/{aat["aat_id"]}">{html.escape(aat["aat_term"])}</a>'
                f'<br><span class="muted">aat:{aat["aat_id"]}</span>') if aat else '<span class="muted">— (in progress)</span>'
    img = f'<img loading="lazy" src="{ex}" alt="{html.escape(c["label"])}" style="max-height:34px">' if have else '<span class="muted">—</span>'
    rows.append(f'<tr><td>{img}</td><td><b>{html.escape(c["label"])}</b></td><td>{html.escape(c.get("group","") or "")}</td>'
                f'<td>{STYLE.get(style, html.escape(style))}{" · size-variable" if c.get("size_variable") else ""}</td>'
                f'<td class="muted">{regime(c)}</td><td>{aat_cell}</td></tr>')

page = f"""---
title: The Ordnance Survey Characteristic Sheets — our extraction
description: OS writing categories, exemplars, letterforms, and Getty AAT mappings
---

# The Ordnance Survey Characteristic Sheets

The Ordnance Survey published **"Characteristic Sheets"** — reference keys to the lettering it used on
its maps. GB-STAMP is grounded in the sheet
**["Examples for the Characters of the Writing on the Engraved Six-Inch Ordnance Maps of Great Britain" (1897)](https://maps.nls.uk/view/128076792)**,
digitised by the **National Library of Scotland** (reproduced under CC-BY), together with the later
(c. 1923) revision.

These sheets are the Rosetta Stone of the project: they record the Ordnance Survey's *own* rule that
**the style of the lettering encodes the kind of feature**. Two points are worth emphasising because they
do a lot of work in the method:

- **Administrative levels are distinguished by different ALL-CAPITALS and fancy faces.** Counties,
  divisions of counties, hundreds, ancient parishes, civil parishes/townships, liberties, boroughs and wards
  are *not* all set the same way — each rung of the administrative hierarchy has its own capital or
  decorated letterform, so the typography alone signals *which level of jurisdiction* a name belongs to.
- **The convention changed in 1879.** Names marked † on the sheet were lettered one way before 1879 and
  differently after, so the style→type mapping is **edition-dependent**: we key each label to its sheet's
  publication date.

Below is our machine-readable extraction of the sheet — the categories, an exemplar clipped from the sheet
itself, the letterform we assign, the date regime, and the Getty **Art & Architecture Thesaurus** term the
category maps to. AAT mappings are still being finalised; cells marked *in progress* are not yet resolved.

<style>
.cs-table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
.cs-table td, .cs-table th {{ border: 1px solid #ddd; padding: 6px 8px; vertical-align: middle; text-align: left; }}
.cs-table th {{ background: #f4f4f4; }}
.cs-table tr:nth-child(even) {{ background: #fafafa; }}
.muted {{ color: #888; font-size: 12px; }}
</style>

<table class="cs-table">
<thead><tr><th>Exemplar</th><th>Category</th><th>Group</th><th>Letterform</th><th>Date regime</th><th>Getty AAT</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>

*Exemplar strips are clipped from the NLS scan of the 1897 Characteristic Sheet (CC-BY). {len(cats)} categories extracted.*

[← Back to the methodology](index.md)
"""
open(f"{HERE}/docs/characteristic-sheets.md", "w").write(page)
print(f"wrote docs/characteristic-sheets.md — {len(cats)} categories, "
      f"{sum(1 for c in cats if aat_for(c))} with AAT, "
      f"{sum(1 for c in cats if find_ex(c['key']))} with exemplars")
