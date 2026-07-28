---
title: Data model
description: GB-STAMP records as a profile of W3C Web Annotation on IIIF canvases
---

# Data model

Text on a map **is an annotation**, structurally: the target is a region of an image, and the body is the
transcribed string, plus a link to a gazetteer entity, plus a classification. That is precisely the shape of
the [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/), and
[IIIF](https://iiif.io) supplies canonical image addressing over the canvases the map libraries we depend on
— the National Library of Scotland, Rumsey, the Library of Congress, the British Library — already serve.

So GB-STAMP does **not** define a new schema. It defines a **profile**: a documented use of two mature
standards, with the conventions this material actually needs. A parallel vocabulary would duplicate a
standard for no gain, and would strand us outside every IIIF viewer and annotation tool that exists.

This matters beyond tidiness. The
[MapText Data Model](https://github.com/maps-as-data/maptext_data_model) proposal — sketched at the Open
Maps Meeting in November 2024, and dormant since — names the requirement in its own README: *"to save as
IIIF annotations in particular"*. Nobody has acted on it. We think that instinct is right and should be the
organising principle rather than a footnote.

## One caveat, stated first

W3C Web Annotation is verbose, and anyone who knows the standard will reasonably ask whether we have thought
about that at scale. We have, and the position is deliberate:

> **Annotations are the interchange and provenance format at the point of extraction and correction. The
> attestation graph remains the internal model.**

The deliverable is the documented *mapping* between the two, not a wholesale re-serialisation of the index.

## The profile

### A word

One word found on the map, or one volunteer transcription.

```jsonc
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://whgazetteer.org/gb-stamp/anno/w/gb_4318_2824/00123",
  "type": "Annotation",
  "motivation": "transcribing",
  "body": [
    {"type": "TextualBody", "purpose": "transcribing", "value": "Middleton",
     "format": "text/plain", "language": "en"},
    {"purpose": "classifying", "source": "https://whgazetteer.org/gb-stamp/face/Upright-Solid-Serif"}
  ],
  "target": {
    "source": "https://maps.nls.uk/iiif/canvas/101603659",
    "selector": [
      {"type": "SvgSelector", "value": "<svg><polygon points='...'/></svg>"},
      {"type": "FragmentSelector", "conformsTo": "http://www.opengis.net/def/crs/EPSG/0/3857",
       "value": "..."}
    ]
  },
  "generator": {"id": "https://github.com/maps-as-data/MapTextPipeline",
                "type": "Software", "name": "MapTextPipeline ViTAEv2_S rumsey-finetune"},
  "generated": "2026-07-28T00:00:00Z"
}
```

### A label

The assembled label — and the reason ordering is not decoration: `MOOR MIDDLETON` is not the label
`MIDDLETON MOOR`. W3C already has the right construct, **`oa:List`**, an *ordered* multiplicity.

```jsonc
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://whgazetteer.org/gb-stamp/anno/l/gb_4318_2824/0007",
  "type": "Annotation",
  "motivation": "transcribing",
  "body": [
    {"type": "TextualBody", "purpose": "transcribing", "value": "Middleton Moor"},
    {"purpose": "classifying", "source": "http://vocab.getty.edu/aat/300008795"},
    {"purpose": "identifying", "source": "https://whgazetteer.org/places/12345"}
  ],
  "target": {
    "type": "List",
    "items": [
      "https://whgazetteer.org/gb-stamp/anno/w/gb_4318_2824/00123",
      "https://whgazetteer.org/gb-stamp/anno/w/gb_4318_2824/00124"
    ]
  }
}
```

This is the node nothing else in the ecosystem produces. Neither MapReader nor MapTextPipeline links words
into labels, although the ICDAR MapText competition scores linking as a task — see
[joining words into labels](label-assembly.md).

## The lettering itself, as a `describing` body

What the lettering physically *is* is a measurement, not a classification, so it does not belong in a
classifying body:

```jsonc
{"purpose": "describing", "type": "TextualBody", "format": "application/json",
 "value": "{\"cap_height_px\": 19.1, \"cap_height_m\": 13.4, \"slant_deg\": 1.2, \"lines\": 1,
            \"face\": {\"source\": \".../face/Upright-Solid-Serif\", \"confidence\": 0.61,
                      \"alternatives\": [...]}}"}
```

Cap height is carried in map pixels **and** in metres on the ground: pixels are comparable only within one
zoom level, and the ground figure is what a later analysis wants. It is deliberately kept out of the face,
because on this series the typeface encodes feature **type** while the size encodes **importance** — a
parish name and a county name can share a face and be separable by height alone. Folding one into the other
would discard half the signal.

## Provenance: `creator` and `generator` do the work

The distinction that matters most for evaluation is between text a **human** supplied and text a **machine**
found. W3C already separates these — `creator` for the agent responsible, `generator` for the software that
produced the serialisation — and the separation expresses our three cases exactly, without inventing a
vocabulary:

| our case | `creator` | `generator` | may it be scored against GB1900? |
|---|---|---|---|
| a volunteer read it | GB1900 contributor | — | it *is* the reference |
| a detector found it unaided | — | the spotter | **yes** |
| a detector was told where to look, by a pin | GB1900 contributor | the spotter | **no — circular** |

The third row is the important one. A **prompted** detection's text came *from* GB1900, so scoring it against
GB1900 returns a perfect result by construction. Expressing it as *both* a human creator and a software
generator is more honest than a flat label would be, because it records **why** the record is circular: the
human is in its provenance chain. A record with a `creator` cannot be scored against that creator's own data.

## The GB1900 pin is not the label's extent

A GB1900 pin is a point placed near a label's start, often just off the ink. Coercing it into the target
geometry would assert something false. In the profile it is a separate target on the same annotation, using a
`PointSelector`, so a record may legitimately have a pin and no region (a transcription nothing was found
at) or a region and no pin (a detection the crowd never made).

## Why this converges with the correction interface

Extracted map text lands as W3C annotations on IIIF canvases. A human corrector fixes them in
**[Annotorious](https://annotorious.dev)** or **[Recogito Studio](https://recogitostudio.org)** — mature
tools in the Pelagios orbit, with plugin ecosystems, polygon selection and geotagging already built — and the
corrected annotations flow onward carrying their provenance. Choosing the standard rather than a private
schema is what makes that possible at no cost to us; choosing a parallel vocabulary would mean building a
correction interface ourselves.

## Open questions we would want a community answer to

- May a label annotation nest — a label that is part of a larger label?
- How should we express that two annotations are the **same label found by different means**, which is
  exactly the join between a volunteer's pin and a machine's detection?
- Does confidence belong on the transcription body, the classifying body, or both?
- Is `oa:List` over annotation URIs the right construct for word→label membership, or should the label target
  the *canvas regions* directly and carry membership another way?

We intend to take these to the
[maptext_data_model](https://github.com/maps-as-data/maptext_data_model) repository, alongside the Pelagios
tooling, once our own dataset is final — so that the proposal arrives with a working implementation and a
corpus behind it rather than as an opinion.

[← Back to the methodology](index.md)
