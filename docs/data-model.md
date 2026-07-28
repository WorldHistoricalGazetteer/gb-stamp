---
title: Data model
description: How GB-STAMP records text on maps, and a proposal for interchange
---

# Data model

GB-STAMP emits three kinds of record, and the distinctions between them do real work — most importantly the
distinction between *what a volunteer read*, *what a machine found by itself*, and *what a machine found
because it was told where to look*. Conflating those would let circular evidence into an evaluation.

This model is deliberately shaped to the **[MapText Data Model](https://github.com/maps-as-data/maptext_data_model)**
sketched at the Open Maps Meeting in November 2024. That sketch is a proposal rather than a schema — no
serialisation has been formalised yet — so what follows is our concrete instantiation of it, offered as
something the community can adopt, amend or reject. Where we have invented a field name we say so.

## The three record types

| type | in the sketch | what it is here |
|---|---|---|
| `TextAnnotation` | `TextAnnotation` | one word found on the map, or one volunteer transcription |
| `CombinedAnnotation` | `CombinedAnnotation` | a whole label: **ordered** member words |
| `SymbolAnnotation` | `SymbolAnnotation` | reserved; not yet emitted |

A **label** is a `CombinedAnnotation`, and its members are ordered because reading order is part of what the
label *is*: `MOOR MIDDLETON` is not the same label as `MIDDLETON MOOR`. This is the node in the sketch that
nothing in the ecosystem currently produces — neither MapReader nor MapTextPipeline performs word-to-label
linking, though the ICDAR MapText competition scores it as a task.

## Fields

Every annotation carries:

```jsonc
{
  "id":            "gbstamp:w/gb_4318_2824/00123",   // stable, namespaced
  "type":          "TextAnnotation",                  // or CombinedAnnotation
  "transcription": {"text": "Middleton", "confidence": 0.97},
  "target": {                                         // where it is
    "geometry":   {"type": "Polygon", "coordinates": [[...]]},
    "baseline":   {"type": "LineString", "coordinates": [[...]]},  // the text's centre-line
    "crs":        "EPSG:3857"
  },
  "reference_point": {"type": "Point", "coordinates": [x, y]},     // optional; see below
  "semantic_type": {"label": "wells", "uri": "http://vocab.getty.edu/aat/300006861",
                    "confidence": 0.62, "alternatives": [...]},    // optional
  "provenance": {
    "mode":  "automatic",                             // manual | automatic | prompted
    "agent": "MapTextPipeline/ViTAEv2_S rumsey-finetune",
    "tool":  "gb-stamp/spot_sheet",
    "date":  "2026-07-28"
  }
}
```

A `CombinedAnnotation` adds:

```jsonc
{
  "type": "CombinedAnnotation",
  "items": ["gbstamp:w/.../00123", "gbstamp:w/.../00124"],   // ORDERED, reading order
  "lines": 2,                                                // 1 unless set on multiple lines
  "transcription": {"text": "Middleton Moor", "confidence": 0.94}
}
```

### `provenance.mode` — the field that matters most

| value | meaning | may it be scored against GB1900? |
|---|---|---|
| `manual` | a GB1900 volunteer read this | it *is* the reference |
| `automatic` | a detector found it unaided | **yes** |
| `prompted` | a detector was told where to look, by a GB1900 pin | **no — circular** |

A prompted detection's text comes *from* GB1900, so scoring it against GB1900 measures nothing and returns a
perfect result by construction. Recording the mode makes that structural rather than a matter of anyone
remembering. Prompted records remain valuable — a label the crowd found and the spotter missed can still be
given a box, and from that box a typographic reading — but they are a different kind of evidence and are
labelled as such.

### `reference_point` versus `target.geometry`

GB1900 gives a **point**, placed near the start of a label and often just off the ink. It is not the label's
extent. Keeping it in `reference_point` rather than coercing it into `target.geometry` preserves that
difference; a record may legitimately have a reference point and no geometry (an unmatched volunteer pin), or
geometry and no reference point (a detection the crowd never pinned).

### `target.baseline`

The text's centre-line, distinct from the outline. On a curved label the outline's bounding rectangle points
*across* the curve rather than along it, so the baseline is the honest carrier of direction. MapTextPipeline
emits one per detection; where a record predates its capture we reconstruct it from the outline and say so in
`provenance.tool`.

### `semantic_type`

Getty AAT as `label` + `uri`, with `confidence` and ranked `alternatives`. Several OS writing categories are
engraved in an *identical* face and are inseparable by design, so a single verdict would be false precision;
the alternatives list is how that degrades gracefully.

## What we are proposing, and what we are not

**Proposing:** the field shapes above, in particular the three-valued `provenance.mode`, the separation of
`reference_point` from `target.geometry`, the explicit `baseline`, and `items` as an *ordered* list.

**Not proposing:** a serialisation. The sketch names JSON-LD (W3C) and COCOtext, with transformation to IIIF
Presentation. We emit newline-delimited JSON because that is what our pipeline and our release format need;
the field names are chosen so a JSON-LD context can be laid over them later without renaming anything.

**Open questions we would want a community answer to:** whether `CombinedAnnotation` may nest (a label that
is part of a larger label); how to express that two annotations are the *same* label found by different
means, which is the join between a volunteer pin and a machine detection; and whether confidence belongs on
the transcription, the semantic type, or both.

We intend to take these to the
[maptext_data_model](https://github.com/maps-as-data/maptext_data_model) repository once our own dataset is
final, so that the proposal arrives with evidence attached rather than as an opinion.

[← Back to the methodology](index.md)
