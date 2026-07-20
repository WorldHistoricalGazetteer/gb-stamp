---
title: GB-STAMP
description: Recovering feature types for the GB1900 gazetteer from Ordnance Survey map typography
---

<img src="assets/logo.svg" alt="GB-STAMP" align="right" width="132" style="margin:0 0 8px 16px">

# GB-STAMP

**GB-STAMP — *Semantic Typing of Antiquarian Map Placenames*** — gives the [GB1900](https://www.visionofbritain.org.uk/gb1900) gazetteer a sense of **what** each place is, not just its name and location, by reading the Ordnance Survey's own map **typography**. (The name is also a small pun: the Ordnance Survey *stamped* a distinct lettering style onto every kind of feature when it engraved its plates; GB-STAMP reads that stamp back.)

*A methodology note. Results are pending; this page describes the source, its limitations, and our approach. Accuracy, coverage, and an honest account of the limits will be added as the work is validated.*

---

## 1. The source, in plain terms

Between roughly 2016 and 2018, a large volunteer effort called **[GB1900](https://www.visionofbritain.org.uk/gb1900)** transcribed **every piece of text printed on the Ordnance Survey's "six-inch to one mile" County Series maps of Great Britain** — the detailed edition surveyed in the decades around 1900. Thousands of volunteers read the maps sheet by sheet and typed out what each label said, pinning it to the exact spot on the map where it appeared.

The result is extraordinary: a gazetteer of roughly **2.67 million labels**, each one a **point on the map plus the text that was written there** — farm names, streams, churches, wells, footpaths, ancient monuments, quarries, milestones, and much more. It is one of the richest historical snapshots of the British landscape ever assembled, and it was released for reuse under an open licence (CC-BY-SA).

GB1900 grew out of the **Great Britain Historical GIS** and **[A Vision of Britain through Time](https://www.visionofbritain.org.uk)**, the long-running project led by **Humphrey Southall** at the University of Portsmouth, and was delivered as a partnership with the National Library of Scotland, Aberystwyth University, People's Collection Wales, and its many volunteers.

---

## 2. What plain GB1900 does *not* tell you

GB1900 records **what a label says and where it is** — but not **what kind of thing it refers to**. To the dataset, `Tumulus`, `Smithy`, `Ford`, `St Mary's Church`, and `Manor Farm` are all just strings of text at points. There is no field that says "this is an *antiquity*", "this is a *water feature*", "this is a *place of worship*".

That missing layer — **feature type** — is exactly what turns a list of names into something you can *search*, *filter*, *map thematically*, and *link* to other gazetteers and authorities. Without it you cannot ask questions like *"show me every ancient monument in Wales"* or *"map all the watermills in the Pennines"*, even though the data to answer them is sitting right there in the labels.

Two further wrinkles are worth knowing:

- **The Abridged gazetteer.** GB1900 is distributed both as a **Complete** gazetteer and as a smaller **Abridged** one. The Abridged version strips out the huge number of repetitive, generic labels — the endless `F.P.` (foot path), `Well`, `P` (post), `Spr` (spring), spot heights, and boundary marks — to leave a cleaner set of *distinctive* names. That makes it more manageable, but it **discards real evidence**: those repeated labels are genuine features on the ground, and the abridgement also removes many duplicate instances of the same name. For landscape-scale analysis the Complete gazetteer is richer but noisier; the Abridged one is tidier but partial.
- **It is points, not shapes, and transcriptions, not truth.** Every entry is a single point (not the extent of a wood or the line of a river), and every entry is a human transcription of century-old print — so there are reading errors, abbreviations, and inconsistencies to contend with.

---

## 3. Our idea: let the map's *typography* tell us the type

The Ordnance Survey did not choose fonts at random. Across its maps it used a **deliberate, documented system of typography** in which *the style of the lettering encodes the kind of feature*:

- **Water and natural features** (rivers, brooks, springs) are set in a **sloping *italic*** serif.
- **Antiquities** (tumuli, cairns, camps, the sites of former buildings) are set in an ornate **blackletter / Gothic** hand — and, in fact, in *four* distinct antiquity styles depending on period.
- **Settlements, civil features, and buildings** (churches, schools, woods) are set in an **upright roman**.
- **Administrative units are distinguished by different ALL-CAPITALS and fancy faces** — counties, divisions, hundreds, ancient and civil parishes, liberties, boroughs and wards each have their *own* capital or decorated letterform, so the lettering alone tells you *which rung of the administrative hierarchy* a name belongs to.
- **Heights, bench-marks, and boundary marks** have their own numeral and symbol conventions.

These conventions are laid out in the Ordnance Survey's own reference documents, the **Characteristic Sheets** — the map-maker's key to its own visual language. In other words, the OS already *classified* every feature when it drew the map; it simply encoded that classification in **how the words look** rather than in a separate label. Crucially, the convention **changed in 1879**, so the style→type mapping is edition-dependent, and we key each label to the publication date of its sheet.

**[→ See our full extraction of the Characteristic Sheets](characteristic-sheets.md)** — every writing category, an exemplar clipped from the sheet, the letterform, the date regime, and its Getty AAT mapping.

GB1900 volunteers transcribed the *words* but, understandably, not the *style* they were printed in. **GB-STAMP recovers that lost styling from the original scanned maps and turns it back into feature types.**

### How it works, step by step

1. **Find the words on the map.** Starting from each GB1900 point, we locate the corresponding label on the scanned map image and delineate it cleanly with a modern map text-spotting model. This gives us a tidy picture of each label in its original font — not just the transcribed text.
2. **Read the letterforms.** We compare each label's lettering against the Characteristic-Sheet conventions and against a set of examples verified by eye. Because the *same letter* in different styles is the cleanest signal (an italic *a* versus an upright *a*), we compare letter-for-letter, and we learn a compact "style fingerprint" for each letterform from the millions of unlabelled examples the maps provide.
3. **Combine style with text.** The words themselves already carry a great deal of type information — `Tumulus` is self-evidently an antiquity, `Ford` a water crossing, `B.M.` a bench-mark — so we **fuse the typographic signal with text-based rules**. Each reinforces the other: the text resolves cases the font cannot, and the font resolves the many ordinary place-names that the text alone leaves ambiguous.
4. **Map to a shared vocabulary.** Finally, the recovered types are aligned to a standard controlled vocabulary (the Getty **Art & Architecture Thesaurus**), so the enriched gazetteer can be searched, filtered, and linked to other datasets.

### What is honest to say at this stage

This is a research method, and we are reporting it *before* the final numbers so that the approach can be scrutinised. Some parts are already reliable — antiquities (blackletter) and numeric labels are strongly distinguished, and the text signal is dependable wherever a label names its own type. The **hardest case is the subtle difference between the upright and italic serif faces** used for ordinary place-names, which even a careful human eye finds marginal at this map scale; we treat the font signal there as a *confidence-weighted* contribution rather than a verdict. Full evaluation will be published here as it is completed.

---

## 4. Getting the data

The enriched gazetteer will be published as a **[GitHub Release](https://github.com/WorldHistoricalGazetteer/gb-stamp/releases)** on this repository — the simplest possible "download directly from GitHub" route (release assets allow up to 2 GB per file and are served over a CDN). We expect the typed corpus to be a modest download: 2.67 million records with a handful of fields, distributed as compressed **Parquet** and **GeoJSONL**, is on the order of tens of megabytes. A browsable, searchable map interface is also planned — see the **[web-map feasibility note](webmap.md)**.

*Releases will appear once the typing is validated.*

---

## 5. Why it matters

If it works, GB-STAMP adds the one thing GB1900 lacks: a **feature-type layer** over 2.67 million historical labels, derived not from guesswork but from the Ordnance Survey's *own* classification as expressed in its typography. That makes the whole corpus **thematically searchable and mappable**, and connectable to the wider ecosystem of historical gazetteers — including the [World Historical Gazetteer](https://whgazetteer.org).

---

## Acknowledgements

- **GB1900** was created by thousands of volunteers and by the **Great Britain Historical GIS / A Vision of Britain through Time** (**Humphrey Southall**, University of Portsmouth), the **National Library of Scotland**, **Aberystwyth University**, and **People's Collection Wales**. GB-STAMP builds directly on their work.
- The **Ordnance Survey Characteristic Sheets** are reproduced from scans by the **[National Library of Scotland](https://maps.nls.uk/view/128076792)** (CC-BY).
- Feature types use the Getty **Art & Architecture Thesaurus (AAT)**, made available under the [ODC Attribution License](https://www.getty.edu/research/tools/vocabularies/license.html).
- Computation ran on the **HTC, H2P, and GPU clusters at the University of Pittsburgh Center for Research Computing and Data** (RRID:SCR_022735), supported by NIH award S10OD028483 and NSF award OAC-2117681.
- GB-STAMP is developed by **Stephen Gadd** within the **[World Historical Gazetteer](https://whgazetteer.org)** indexing infrastructure.

## Licence

See **[Licensing](licensing.md)**. In brief: the **code** is MIT; the **data and documentation** are **CC-BY 4.0** (the most open licence compatible with the sources — the GB1900 raw dump is CC0, so no share-alike applies). **Any re-use must credit Stephen Gadd and the World Historical Gazetteer**, alongside GB1900 and the other upstream sources.
