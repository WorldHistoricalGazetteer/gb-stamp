---
title: GB-STAMP
description: Recovering feature types for the GB1900 gazetteer from Ordnance Survey map typography
---

# GB-STAMP

**Giving the GB1900 gazetteer a sense of *what* each place is — not just its name and location — by reading the Ordnance Survey's own map typography.**

*A methodology note. Results are pending; this page describes the source, its limitations, and our approach. Numbers and evaluation will be added as the work is validated.*

---

## 1. The source, in plain terms

Between roughly 2016 and 2018, a large volunteer effort called **[GB1900](https://www.visionofbritain.org.uk/gb1900)** transcribed **every piece of text printed on the Ordnance Survey's "six-inch to one mile" County Series maps of Great Britain** — the detailed edition surveyed in the decades around 1900. Thousands of volunteers read the maps sheet by sheet and typed out what each label said, pinning it to the exact spot on the map where it appeared.

The result is extraordinary: a gazetteer of roughly **2.67 million labels**, each one a **point on the map plus the text that was written there** — farm names, streams, churches, wells, footpaths, ancient monuments, quarries, milestones, and much more. It is one of the richest historical snapshots of the British landscape ever assembled, and it was released for reuse under an open licence (CC-BY-SA).

GB1900 was a partnership effort involving the National Library of Scotland, the Great Britain Historical GIS / *A Vision of Britain through Time* (University of Portsmouth), Aberystwyth University, People's Collection Wales, and many volunteers.

---

## 2. What plain GB1900 does *not* tell you

GB1900 records **what a label says and where it is** — but not **what kind of thing it refers to**. To the dataset, `Tumulus`, `Smithy`, `Ford`, `St Mary's Church`, and `Manor Farm` are all just strings of text at points. There is no field that says "this is an *antiquity*", "this is a *water feature*", "this is a *place of worship*".

That missing layer — **feature type** — is exactly what turns a list of names into something you can *search*, *filter*, *map thematically*, and *link* to other gazetteers and authorities. Without it you cannot ask questions like *"show me every ancient monument in Wales"* or *"map all the watermills in the Pennines"*, even though the data to answer them is sitting right there in the labels.

There are two further wrinkles worth knowing:

- **The Abridged gazetteer.** GB1900 is distributed both as a **Complete** gazetteer and as a smaller **Abridged** one. The Abridged version removes the huge number of repetitive, generic labels — the endless `F.P.` (foot path), `Well`, `P` (post), `Spr` (spring), spot heights, and boundary marks — to leave a cleaner set of *distinctive* names. That makes it more manageable, but it **discards real evidence**: those repeated labels are genuine features on the ground, and the abridgement also removes many duplicate instances of the same name. For landscape-scale analysis, the Complete gazetteer is richer but noisier; the Abridged one is tidier but partial.
- **It is points, not shapes, and transcriptions, not truth.** Every entry is a single point (not the extent of a wood or the line of a river), and every entry is a human transcription of century-old print — so there are OCR-style reading errors, abbreviations, and inconsistencies to contend with.

---

## 3. Our idea: let the map's *typography* tell us the type

Here is the insight GB-STAMP is built on. The Ordnance Survey did not choose fonts at random. Across its maps it used a **deliberate, documented system of typography** in which *the style of the lettering encodes the kind of feature*:

- **Water and natural features** (rivers, brooks, springs) are set in a **sloping *italic*** serif.
- **Antiquities** (tumuli, cairns, camps, the sites of former buildings) are set in an ornate **blackletter / Gothic** hand — and, in fact, in *four* distinct antiquity styles depending on period.
- **Settlements, civil features, and buildings** (churches, schools, woods) are set in an **upright roman**.
- **Administrative boundaries, heights, and bench-marks** each have their own conventions and numerals.

These conventions are laid out in the Ordnance Survey's own reference documents, the **"Characteristic Sheets"** — the map-maker's key to its own visual language. In other words, the OS already *classified* every feature when it drew the map; it simply encoded that classification in **how the words look** rather than in a separate label.

GB1900 volunteers transcribed the *words* but, understandably, not the *style* they were printed in. **GB-STAMP recovers that lost styling from the original scanned maps and turns it back into feature types.**

### How it works, step by step

1. **Find the words on the map.** Starting from each GB1900 point, we locate the corresponding label on the scanned map image and delineate it cleanly, using a modern map text-spotting model. This gives us a tidy picture of each label in its original font — not just the transcribed text.
2. **Read the letterforms.** We compare each label's lettering against the Ordnance Survey's Characteristic-Sheet conventions and against a set of examples verified by eye. Because the *same letter* in different styles is the cleanest signal (an italic *a* versus an upright *a*), we compare letter-for-letter, and we learn a compact "style fingerprint" for each letterform from the millions of unlabelled examples the maps provide.
3. **Combine style with text.** The words themselves already carry a great deal of type information — `Tumulus` is self-evidently an antiquity, `Ford` a water crossing, `B.M.` a bench-mark — so we **fuse the typographic signal with text-based rules**. Each reinforces the other: the text resolves cases the font cannot, and the font resolves the many ordinary place-names that the text alone leaves ambiguous.
4. **Map to a shared vocabulary.** Finally, the recovered types are aligned to a standard controlled vocabulary (the Getty **Art & Architecture Thesaurus**), so the enriched gazetteer can be searched, filtered, and linked to other datasets.

### What is honest to say at this stage

This is a research method, and we are reporting it *before* the final numbers so that the approach can be scrutinised. Some parts are already reliable — antiquities (blackletter) and numeric labels are strongly distinguished, and the text signal is dependable wherever a label names its own type. The **hardest case is the subtle difference between the upright and italic serif faces** used for ordinary place-names, which even a careful human eye finds marginal at this map scale; we treat the font signal there as a *confidence-weighted* contribution rather than a verdict. Full evaluation — accuracy by feature class, coverage, and honest characterisation of the limits — will be published here as it is completed.

---

## 4. Why it matters

If it works, GB-STAMP adds the one thing GB1900 lacks: a **feature-type layer** over 2.67 million historical labels, derived not from guesswork but from the Ordnance Survey's *own* classification as expressed in its typography. That makes the whole corpus **thematically searchable and mappable**, and connectable to the wider ecosystem of historical gazetteers — including the [World Historical Gazetteer](https://whgazetteer.org).

---

*GB-STAMP is developed as part of the World Historical Gazetteer's indexing infrastructure. See the [interactive-map feasibility note](webmap.md) for how a corpus of this size can be served and searched entirely in the browser.*
