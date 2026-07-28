# TODO

## After the dataset is final

- [ ] **Take the annotation profile to the Maps as Data and Pelagios communities.**
      Not a new schema — a **profile of W3C Web Annotation on IIIF canvases**. Text on a map *is* an
      annotation, and a parallel vocabulary would duplicate a mature standard for no gain while stranding us
      outside every IIIF viewer and annotation tool that exists. The
      [MapText Data Model](https://github.com/maps-as-data/maptext_data_model) README names the requirement
      itself — *"to save as IIIF annotations in particular"* — and nobody has acted on it. It has been
      dormant since January 2025.
      We are well placed to lead it, holding the two things the sketch most needs evidence for:
      - a working implementation of ordered word→label linking (`oa:List`), which nothing else in the
        ecosystem produces — neither MapReader nor MapTextPipeline links words, though ICDAR MapText scores
        linking as a task;
      - a corpus large enough that the `creator`/`generator` provenance distinction actually bites, between
        a volunteer transcription, an unaided detection, and a detection prompted by a pin.
      Write-up at [`docs/data-model.md`](docs/data-model.md), with four open questions stated rather than
      assumed away. **Deliberately deferred until the dataset is final**, so the proposal arrives with a
      working implementation and a corpus behind it rather than as an opinion.

- [ ] **Converge with the Pelagios correction tooling.** Extracted text lands as W3C annotations on IIIF
      canvases; a corrector fixes them in Annotorious or Recogito Studio; corrected annotations flow onward
      carrying provenance. That is the human-in-the-loop interface a spotter pipeline needs and which we
      would otherwise have to build. Recogito Studio's geotagging plugin already ships a WHG connector, so
      there is a live downstream consumer to harden rather than a relationship to start.

- [ ] Quantify the ceiling on transcription agreement. Some GB1900 transcriptions are wrong, so exact
      reproduction can never reach 1.0. Needs human adjudication of a disagreement sample — which doubles as
      a set of crowd-transcription corrections, i.e. it is a deliverable, not just a measurement.

## In progress

- [ ] Fetch the full z17 tile corpus to local block storage (~8.06M tiles) so results stop depending on a
      third-party CDN's health on the day.
- [ ] Re-spot all 1,307 regions from the local corpus, so the whole dataset comes from one code version and
      every detection carries the model's own baseline.
- [ ] Then measure what proportion of non-numeric labels GB1900 and GB-STAMP each miss. A first attempt was
      contaminated by regions processed while the tile service was failing; those regions look identical to
      empty countryside in the output.

## Known open

- [ ] The join's training set is filtered to labels the recogniser read exactly as the volunteer did, which
      biases it toward legible, conventional lettering. The held-out score cannot reveal this, because the
      test set is filtered the same way. Unusual faces — blackletter, ornate, outline — are likely
      under-represented, and those are where the typographic reading is meant to earn its place.
- [ ] Six of the fifteen inventory faces still carry no verified reference labels.
