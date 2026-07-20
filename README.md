# GB-STAMP

**Recovering feature types for the [GB1900](https://www.visionofbritain.org.uk/gb1900) gazetteer from Ordnance Survey map typography.**

GB1900 is a volunteer transcription of every text label on the Ordnance Survey six-inch County Series maps of Great Britain (surveyed c. 1900) — roughly **2.67 million labels**, each a point plus its text. What it lacks is **feature type**: it records *what a label says and where*, but not *what kind of thing it is*.

The Ordnance Survey, however, encoded feature type in its **typography** — italic for water, blackletter for antiquities, roman for settlements, and so on, as documented in its "Characteristic Sheets". **GB-STAMP recovers that lost styling from the scanned maps and turns it back into feature types**, fusing the typographic signal with text-based rules and aligning the result to the Getty Art & Architecture Thesaurus.

## Read the methodology

- **[Methodology (plain-terms + academic)](https://worldhistoricalgazetteer.github.io/gb-stamp/)** — the source, the limitations of plain GB1900 and its abridgement, and how the method works.
- **[Serving 2.67M points in the browser](https://worldhistoricalgazetteer.github.io/gb-stamp/webmap)** — feasibility and architecture for a static, searchable MapLibre interface.

> **Status:** research in progress. This repository documents the approach ahead of full evaluation; accuracy, coverage, and honest characterisation of the limits will be published as the work is validated.

## Part of the World Historical Gazetteer

GB-STAMP is developed within the [World Historical Gazetteer](https://whgazetteer.org) indexing infrastructure.

## Licence

- **Documentation and code:** see `LICENSE` (to be added).
- **Derived data:** GB1900 is released under CC-BY-SA; any redistributed gazetteer inherits attribution and share-alike obligations.
