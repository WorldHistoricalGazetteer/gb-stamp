---
title: Joining words into labels
description: Why a text spotter's output is not a gazetteer, and how GB1900 lets us measure the join
---

# Joining words into labels

A text spotter finds **words**. A gazetteer needs **labels**. On the six-inch maps a great many labels are
several words long — *Middleton Moor*, *Home Farm*, *St Mary's Church*, *Old Clay Pits* — and until those
words are joined back together, almost nothing downstream can work properly. A box reading `MOOR` can never
match a transcription reading *Middleton Moor*, so any comparison between spotter output and GB1900 measures
the missing join rather than the quality of either.

This turns out to be a harder problem than it sounds, and it is a known one: the ICDAR **MapText**
competitions score "linking words into phrase blocks" as an explicit task alongside detection and
recognition, and the 2025 organisers report that while detection performance is strong, **recognition and
linking remain difficult** — citing dense text, rotated and curved text, and widely spaced characters, all
of which the OS six-inch sheets have in abundance.

## Why GB1900 is an unusually good test set for it

Most work on this problem is evaluated on curated benchmarks of a few hundred to a few thousand annotated
map images. GB1900 offers something different: **2.67 million volunteer transcriptions on a single,
typographically consistent map series**. A volunteer's transcription names *every word of a label*, which
means it can be used to check a join without anyone annotating anything new.

That gives a strict test. We do not ask whether two boxes overlap; we ask whether the **assembled label
reproduces the volunteer's transcription exactly**.

It also gives training data. Where the words detected near a pin account for exactly that pin's
transcription — every token matched by a distinct word — we have a known-good label group. Pairs of words
drawn from one group are positive examples of "these belong together"; pairs spanning two groups are
negative.

**Transcription errors are handled structurally rather than statistically.** Comparison is
case-insensitive and punctuation-insensitive, so a volunteer's capitalisation slip is invisible. A more
substantial error means a token matches no detected word, so the group fails the all-tokens test and is
**discarded** — a bad transcription costs a training example rather than corrupting one. Where two pins
claim the same word (as happens constantly with *STREET*), both groups are dropped rather than guessed at.

## How the join works

Every word carries its own typography, and that is enough to say where its continuation must be. From a
word's minimum-area rectangle come three things: a **direction**, a **cap height**, and a **character
pitch** (its length divided by its characters). A second word continues the first when it lies *ahead*
along that direction, within a few of *its own* pitches, off the baseline by only a fraction of the cap
height, and set at the same size and angle.

Projecting along each word's *own* direction matters on a map, where labels run at every angle, curve along
rivers and interleave with one another. A fixed horizontal search window would either miss the rotated
labels or sweep in a neighbour's words.

A label set on two or three lines is one label. Its lines share a size and a direction, sit about a
line-height apart, and — the sharp part of the test — are **centred on a common perpendicular axis**.
Requiring that shared centre rejects the far commoner arrangement of two unrelated labels that merely
happen to sit one above the other.

## A structural finding: a label is a sequence, not a clique

The join decision is made by a classifier trained on the GB1900-derived pairs, using only geometry
expressed in units the typography itself supplies. It is accurate: **held-out pairwise AUC 0.957**, with
whole 12-km blocks held out so that a region the model has seen cannot flatter it.

Feeding those pairwise decisions into a naive connected-components grouping was **catastrophic**. At 93%
pairwise precision — roughly one candidate pair in fourteen wrong — transitive closure welds neighbouring
labels together, and then welds the welds. On one evaluation it produced 31 components swallowing 9,819 of
16,243 words, the largest a single "label" 1,548 words long, and end-to-end accuracy collapsed to *below*
that of simple hand-set rules.

The fix is structural rather than a matter of thresholds. **Reading along its own direction, a word has at
most one predecessor and at most one successor.** Constraining the grouping to that shape means a false pair
must out-score every true rival on both sides to do any damage, and it can never fan out into a blob.

A related caution: the hand-set rules had appeared robust against this failure, but only because their
recall was low enough to leave the graph too sparse to percolate. Their apparent stability was a
side-effect of missing half the true joins.

## Results

Measured on **5,037 GB1900 labels** in regions the model was never trained on, counting a success only when
the assembled label reproduces the transcription **exactly**:

| method | exact reproduction |
|---|---|
| nearest single word alone | 0.219 |
| hand-set geometric rules | 0.381 |
| learned join + sequence constraint | **0.425** |

On the 93% of labels whose every word was read without an unknown-character marker — where a mismatch is a
*grouping* mistake rather than a reading one — the figure is **0.449**. Recognition is therefore not the
limiting factor: grouping is.

Two honest caveats on that number. It is measured against an **unknown ceiling below 1.0**, because some
GB1900 transcriptions are themselves wrong; quantifying that ceiling needs human adjudication of
disagreements, which we intend to run and which doubles as a set of crowd-transcription corrections.
And the training set is filtered to labels the recogniser read exactly as the volunteer did, which biases it
toward legible, conventional lettering — a bias the held-out score cannot reveal, because the test set is
filtered the same way.

## Two things that did not work

Reported because negative results are cheap to repeat otherwise.

**A coarse typeface signal added nothing.** Giving the classifier each word's font classification
(upright / italic / blackletter, with confidences) changed held-out pairwise AUC by less than a thousandth
and left end-to-end accuracy identical. Coverage was ample, so this is not an artefact of missing data. The
explanation appears in the feature weights: when the font features were added, the importance of a simple
*is-this-word-in-capitals* feature fell correspondingly. On these sheets the upright-versus-italic axis is
largely **redundant with letter case**, which the model already had for free. Whether the finer face
inventory helps — separating faces that case cannot proxy — is a different question and remains open.

**A more sophisticated linking rule added nothing.** Replacing mutual-best-neighbour matching with greedy
global assignment made no measurable difference, despite fixing a real defect in principle. The situation it
repairs evidently almost never arises here.

## Reproducibility

Results computed against a tile service depend on that service's health on the day. GB-STAMP therefore
holds its own copy of the ~8 million map tiles it needs, in a local block store, so a figure can be
recomputed rather than merely re-requested.

[← Back to the methodology](index.md)
