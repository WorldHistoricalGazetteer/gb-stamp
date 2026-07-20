# GB-STAMP

**Semantic Typing of Antiquarian Map Placenames** — recovering feature types for the [GB1900](https://www.visionofbritain.org.uk/gb1900) gazetteer from Ordnance Survey map typography.

GB1900 is a volunteer transcription of every text label on the Ordnance Survey six-inch County Series maps of Great Britain (surveyed c. 1900) — roughly **2.67 million labels**, each a point plus its text. What it lacks is **feature type**: it records *what a label says and where*, but not *what kind of thing it is*.

The Ordnance Survey, however, encoded feature type in its **typography** — italic for water, blackletter for antiquities, roman for settlements, and distinct capitals for each rung of the administrative hierarchy, as documented in its "Characteristic Sheets". **GB-STAMP recovers that lost styling from the scanned maps and turns it back into feature types**, fusing the typographic signal with text-based rules and aligning the result to the Getty Art & Architecture Thesaurus.

## Read more

- **[Methodology](https://worldhistoricalgazetteer.github.io/gb-stamp/)** — the source, the limitations of plain GB1900 and its abridgement, and how the method works (plain-terms + academic).
- **[Characteristic-Sheet extraction](https://worldhistoricalgazetteer.github.io/gb-stamp/characteristic-sheets)** — every OS writing category, with exemplars, letterforms, and AAT mappings.
- **[Web-map feasibility](https://worldhistoricalgazetteer.github.io/gb-stamp/webmap)** — a static, serverless, searchable MapLibre interface over 2.67M points (PMTiles + IndexedDB, hosted from GitHub Releases).
- **[Licensing](https://worldhistoricalgazetteer.github.io/gb-stamp/licensing)**.

> **Status:** research in progress. This repository documents the approach ahead of full evaluation; accuracy, coverage, and honest characterisation of the limits will be published as the work is validated. The enriched dataset will be distributed as a [GitHub Release](https://github.com/WorldHistoricalGazetteer/gb-stamp/releases).

## Acknowledgements

Builds on **GB1900** (Great Britain Historical GIS / *A Vision of Britain through Time* — Humphrey Southall, University of Portsmouth — with the National Library of Scotland, Aberystwyth University, and People's Collection Wales). Characteristic-Sheet scans by the **National Library of Scotland** (CC-BY); feature types from the Getty **AAT** (ODC-BY). Computation ran on the **University of Pittsburgh Center for Research Computing and Data** (RRID:SCR_022735), supported by NIH award S10OD028483 and NSF award OAC-2117681. Developed by **Stephen Gadd** within the [World Historical Gazetteer](https://whgazetteer.org).

## Licence

**Code: MIT. Data & documentation: CC-BY-SA 4.0** (the most open licence compatible with GB1900's own share-alike terms). **Any re-use must credit Stephen Gadd and the World Historical Gazetteer.** See [`LICENSE`](LICENSE) and [licensing](https://worldhistoricalgazetteer.github.io/gb-stamp/licensing).
