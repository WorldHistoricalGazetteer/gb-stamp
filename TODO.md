# TODO

## After the dataset is final

- [ ] **Take the data model to `maps-as-data/maptext_data_model`.**
      The MapText Data Model is a sketch from the Open Maps Meeting (Nov 2024) — a README, a diagram, two
      commits, no schema, dormant since Jan 2025 — and the repository explicitly asks for people to help
      formalise it. We are unusually well placed to contribute, because we hold the two things the sketch
      most needs evidence for:
      - a working implementation of `CombinedAnnotation` (ordered word→label linking), which nothing else in
        the ecosystem produces — neither MapReader nor MapTextPipeline links words, though ICDAR MapText
        scores it as a task;
      - a corpus large enough that the `provenance` distinction actually bites, between a volunteer
        transcription, an unaided detection, and a detection prompted by a pin.
      Our instantiation is written up at [`docs/data-model.md`](docs/data-model.md), including the three
      open questions we would want a community answer to (nesting, cross-provenance identity, where
      confidence belongs). **Deliberately deferred until the dataset is final**, so the proposal arrives with
      evidence rather than as an opinion.

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
