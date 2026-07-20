---
title: Serving 2.67 million points in the browser
description: Feasibility and architecture for a static, searchable MapLibre interface to GB-STAMP
---

# Can we serve GB-STAMP as a searchable map — with no server?

**Short answer: yes, realistically — for the *map* it is a solved problem, and for *search* it is achievable with care.** The trick is to split the two concerns and keep the heavy data off GitHub Pages itself.

The corpus is ~2.67 million points, each with a short text label, a location, and (after GB-STAMP) a feature type and confidence. That is large for a naïve "load it all into memory" web app, but well within reach of the modern static-first stack.

## The map: PMTiles + MapLibre (a solved problem)

Rendering millions of points client-side is routine now using **vector tiles**:

- Tile the whole corpus once with **[tippecanoe](https://github.com/felt/tippecanoe)** into a single **[PMTiles](https://docs.protomaps.com/pmtiles/)** archive — one static file that behaves like a tiny database. The browser fetches only the tiles for the current view via **HTTP range requests**, so it never downloads the whole thing.
- Render with **[MapLibre GL JS](https://maplibre.org/)**: cluster points at low zoom, show individuals at high zoom, colour by feature type, and drive a type/confidence filter entirely on the GPU.

2.67M points is comfortably within what this stack handles smoothly. Expect a PMTiles archive on the order of a few hundred MB depending on how many attributes we carry per point.

**One caveat about hosting.** GitHub Pages caps individual files at ~100 MB and applies soft bandwidth limits, so a multi-hundred-MB PMTiles file should **not** live in the repo. The clean pattern is:

- **GitHub Pages** hosts the small static app (HTML/JS/CSS) and enables the whole thing to be free and versioned.
- **The PMTiles archive lives on cheap object storage** that supports range requests — Cloudflare R2 (generous free tier), Source Cooperative, or similar. MapLibre reads it directly from there; no server, no per-request cost of note.

## Search: achievable, with the right index (and this is where IndexedDB earns its place)

Free-text search over 2.67M labels is the genuinely interesting part. Three tiers, easiest to hardest:

1. **Typeahead / prefix search** ("show me names starting *Llan…*") — **easy.** A compact prefix index (a finite-state transducer, or a library such as **FlexSearch**) over 2.67M short strings is on the order of tens of MB. Download it once, **cache it in IndexedDB**, and prefix lookups are instant on repeat visits — and work offline.
2. **Filtered + spatial search** ("watermills in the Pennines", "antiquities in this rectangle") — **easy-to-moderate.** This is mostly a matter of filtering the vector tiles / a lightweight attribute store by feature type, confidence, and viewport; it does not need a full-text engine.
3. **Full fuzzy search** ("find things *like* *tumulus*, tolerating misspellings") over the entire corpus at once — **the one hard part.** A full in-memory inverted index over 2.67M documents is heavy (hundreds of MB of RAM, awkward on mobile). The realistic answers are to **shard** the index (by region, or by first letters) and load shards on demand into IndexedDB, or to compile a **compact FST in WebAssembly** for memory-efficient fuzzy matching. Neither is exotic; both are more engineering than tier 1.

**What IndexedDB is for**, concretely: it is the browser's durable store for the downloaded search-index shards and any per-point attribute blobs, so the app is fast on return visits, resilient to reloads, and usable offline. With the Persistent Storage permission, browsers will hold hundreds of MB to a few GB — ample for a sharded index. It is *not* the right tool for the spatial rendering itself (that is PMTiles' job).

## Recommended architecture

```
  ┌── GitHub Pages (free, versioned) ───────────────┐
  │   static app: MapLibre + UI + search glue        │
  └───────────────┬──────────────────────────────────┘
                  │ range requests
     ┌────────────┴───────────────┐
     │ object storage (R2 / Source Co-op)          │
     │  • gb-stamp.pmtiles   (the map)             │
     │  • search shards      (fuzzy index)         │
     └────────────┬───────────────┘
                  │ cached in
            ┌─────┴──────┐
            │ IndexedDB   │  index shards + attributes; offline + instant repeat visits
            └────────────┘
```

## Honest limits

- **Big blobs must live off Pages** (PMTiles + search shards on object storage). Pages hosts the app, not the data.
- **Full-corpus fuzzy search is the only genuinely hard piece**; typeahead, spatial, and type-filtered search are straightforward. A first release can ship tiers 1–2 and add tier 3 later.
- **Mobile memory** bounds how large a search index we can hold at once — another reason to shard.

**Verdict:** a static, serverless, in-browser MapLibre interface over the full GB-STAMP corpus is realistic. The map is a solved problem via PMTiles; search is achievable, with the fuzzy tier being the part that warrants deliberate engineering. GitHub Pages is the right home for the *application*, with the large tiles and index blobs served from cheap range-request object storage and cached in IndexedDB.
