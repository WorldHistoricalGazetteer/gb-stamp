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

1. **Find the words on the map.** Starting from each GB1900 point, we locate the corresponding label on the scanned map image and delineate it cleanly with **[MapReader](https://github.com/maps-as-data/MapReader)**, a text-spotting toolkit for historical maps. This gives us a tidy picture of each label in its original font — not just the transcribed text.
2. **Learn the OS alphabet, face by face.** Each Characteristic-Sheet exemplar gives us a single letter of one OS writing face. From that one seed we grow the whole alphabet: we find that letter across the real maps by matching letter-shapes, and from the confident matches we harvest the *other* letters of the same face — repeating until we have a real-map alphabet for **every** style the OS used — water, the four antiquity hands, the settlement roman, and each administrative capital. Font is read from the letterforms alone — the *same* letter compared against the *same* letter — so what a label *says* never leaks into what face it is judged to be.
3. **Best three guesses, then arbitrate with text.** Some OS faces are genuinely alike — and a few categories were engraved in an *identical* face — so each label gets a ranked **top-three** font reading with confidences, not a single verdict. Those three are then re-weighted by evidence the letterforms cannot see: which words co-occur with which face across the whole corpus, and independent records of the very civic status the OS capitals were themselves encoding — administrative areas, market towns, parliamentary representation.
4. **Map to a shared vocabulary.** Finally, the recovered types are aligned to a standard controlled vocabulary (the Getty **Art & Architecture Thesaurus**), so the enriched gazetteer can be searched, filtered, and linked to other datasets.

### What is honest to say at this stage

This is a research method, and we are reporting it *before* the final numbers so the approach can be scrutinised. The letterform signal is strongest for the visually distinctive faces — the ornate administrative capitals, the blackletter antiquity hands, the numerals — and weakest for the plain serif faces used for ordinary names, which even a careful eye finds marginal at this map scale. Where two OS categories were engraved in the *same* face they are inseparable by design; rather than pretend to split them, we identify such pairs and merge them under human review. The best-three-guesses output, with the text and civic re-weighting, is built precisely so that hard or shared faces degrade gracefully instead of producing false certainty. Full evaluation — including which faces the maps actually let us distinguish — will be published here.

---

## 4. Results so far

*Preliminary — the font model is being built against the full Characteristic-Sheet taxonomy; corpus-wide coverage is still growing.*

**Building the font model.** We are training the letterform reader against the **whole** Characteristic-Sheet taxonomy — around **44 writing faces** (water, the four antiquity hands, the settlement roman, the numerals, and the full administrative capital hierarchy), one real-map reference alphabet per face, each grown letter-by-letter from a single Characteristic-Sheet exemplar. Every label will carry a **best-three** font reading with confidences. A **separability analysis** — measuring which faces the six-inch maps actually let us tell apart, and which collapse onto a shared face — is under way; its results, including per-face reliability and the human-confirmed identical-face merges, will be published here as they are validated.

**Where the value really is:** the font *disambiguates text*. "Camp", "Castle", "Cross", "Stone" mean an *antiquity* in the antiquity hand but a modern feature in roman or italic — so typing is **font-conditioned**. A companion analysis mines the corpus for exactly which words are font-ambiguous, so the recovered face resolves the many ordinary place-names that the text alone leaves undecided.

**Coverage:** the current edition assigns a feature type to **871,359 of the 2,666,341 labels (32.7%)**, across **15 Getty-AAT-aligned classes** — derived from the OS-grounded lexicon, the OS single-letter abbreviations (e.g. a standalone italic *W* = *well*, ~191k labels), and the font signal where a sheet has been read. Because most of that typing rests on the text and the abbreviation conventions, it is **already national in scope** and does not wait on font-spotting. The typographic reading itself is being extended across **all 35,514 label-bearing map regions** (a resumable GPU job), which progressively enriches the font-conditioned cases; the remaining ~67% of labels are as yet untyped and are shown in grey on the map.

## Getting the data

The enriched gazetteer is published as a **[GitHub Release](https://github.com/WorldHistoricalGazetteer/gb-stamp/releases)** — the simplest "download directly from GitHub" route. The current preview, **[v0.1.0-alpha](https://github.com/WorldHistoricalGazetteer/gb-stamp/releases/tag/v0.1.0-alpha)**, contains the full **2,666,341-record** edition (gzipped JSONL, ~60 MB). Each record carries the raw text + coordinates (CC0 raw dump), a clean feature type + Getty AAT mapping where assigned, and the recovered lettering style where the sheet has been read.

**[→ Browse the interactive map](map/)** · **[web-map feasibility / scale-up note](webmap.md)**

*Alpha preview: feature type is drawn from the OS-grounded lexicon and abbreviation conventions; the full typographic reading is being built and its coverage will grow.*

---

## 5. Why it matters

If it works, GB-STAMP adds the one thing GB1900 lacks: a **feature-type layer** over 2.67 million historical labels, derived not from guesswork but from the Ordnance Survey's *own* classification as expressed in its typography. That makes the whole corpus **thematically searchable and mappable**, and connectable to the wider ecosystem of historical gazetteers — including the [World Historical Gazetteer](https://whgazetteer.org).

---

## Acknowledgements

- **GB1900** was created by thousands of volunteers and by the **Great Britain Historical GIS / A Vision of Britain through Time** (**Humphrey Southall**, University of Portsmouth), the **National Library of Scotland**, **Aberystwyth University**, and **People's Collection Wales**. GB-STAMP builds directly on their work.
- Labels are located and delineated with **[MapReader](https://github.com/maps-as-data/MapReader)** — Wood, R., Hosseini, K., Westerling, K., Smith, A., Beelen, K., Wilson, D.C.S., & McDonough, K. (2024). *MapReader: Open software for the visual analysis of maps.* Journal of Open Source Software, 9(101), 6434. [doi:10.21105/joss.06434](https://doi.org/10.21105/joss.06434). Maintained by [maps-as-data](https://github.com/maps-as-data); developed at Living with Machines / The Alan Turing Institute.
- The **Ordnance Survey Characteristic Sheets** are reproduced from scans by the **[National Library of Scotland](https://maps.nls.uk/view/128076792)** (CC-BY).
- Feature types use the Getty **Art & Architecture Thesaurus (AAT)**, made available under the [ODC Attribution License](https://www.getty.edu/research/tools/vocabularies/license.html).
- Computation ran on the **HTC, H2P, and GPU clusters at the University of Pittsburgh Center for Research Computing and Data** (RRID:SCR_022735), supported by NIH award S10OD028483 and NSF award OAC-2117681.
- GB-STAMP is developed by **Stephen Gadd** within the **[World Historical Gazetteer](https://whgazetteer.org)** indexing infrastructure.

## Licence

See **[Licensing](licensing.md)**. In brief: the **code** is MIT; the **data and documentation** are **CC-BY 4.0** (the most open licence compatible with the sources — the GB1900 raw dump is CC0, so no share-alike applies). **Any re-use must credit Stephen Gadd and the World Historical Gazetteer**, alongside GB1900 and the other upstream sources.
