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

### Where does the big tile file live? — GitHub Releases largely solve it

GitHub Pages caps individual files at ~100 MB, applies soft bandwidth limits, and — crucially — does **not** reliably support the **HTTP range requests** that PMTiles depends on. So a multi-hundred-MB PMTiles archive should not sit in the Pages tree. Three options, best first:

1. **GitHub Releases (recommended).** A **Release asset can be up to 2 GB**, does not count against the repo or Pages limits, and is served from a CDN that **does support range requests** — so **MapLibre can read a single PMTiles archive directly from a Release**, and the enriched dataset can be downloaded directly from the same Release. This keeps *everything on GitHub*: the app on Pages, the tiles and data as Release assets.
2. **External object storage** — Cloudflare R2 (generous free tier), Source Cooperative, or similar. Also range-friendly; useful if bandwidth grows beyond GitHub's fair-use comfort zone.
3. **Splitting for Pages itself** — possible but awkward. Because Pages lacks reliable range support, you would either shard the corpus into many small per-region PMTiles archives *each fetched whole* (works, but loses PMTiles' efficiency), or fall back to a classic **static tile pyramid** of individual `z/x/y.pbf` vector tiles served as plain files (works on Pages with no range requests, but is tens of thousands of small files). Given that Releases remove the need, this is rarely worth it.

**So: yes, a Release sidesteps the storage *and* the range-request problem** — it is the cleanest all-GitHub answer for both the tiles and the downloadable dataset.

## Search: achievable, with the right index (and this is where IndexedDB earns its place)

Free-text search over 2.67M labels is the genuinely interesting part. Three tiers, easiest to hardest:

1. **Typeahead / prefix search** ("show me names starting *Llan…*") — **easy.** A compact prefix index (a finite-state transducer, or a library such as **FlexSearch**) over 2.67M short strings is on the order of tens of MB. Download it once, **cache it in IndexedDB**, and prefix lookups are instant on repeat visits — and work offline.
2. **Filtered + spatial search** ("watermills in the Pennines", "antiquities in this rectangle") — **easy-to-moderate.** This is mostly a matter of filtering the vector tiles / a lightweight attribute store by feature type, confidence, and viewport; it does not need a full-text engine.
3. **Full fuzzy search** ("find things *like* *tumulus*, tolerating misspellings") over the entire corpus at once — **the one hard part.** A full in-memory inverted index over 2.67M documents is heavy (hundreds of MB of RAM, awkward on mobile). The realistic answers are to **shard** the index (by region, or by first letters) and load shards on demand into IndexedDB, or to compile a **compact FST in WebAssembly** for memory-efficient fuzzy matching. Neither is exotic; both are more engineering than tier 1.

**What IndexedDB is for**, concretely: it is the browser's durable store for the downloaded search-index shards and any per-point attribute blobs, so the app is fast on return visits, resilient to reloads, and usable offline. With the Persistent Storage permission, browsers will hold hundreds of MB to a few GB — ample for a sharded index. It is *not* the right tool for the spatial rendering itself (that is PMTiles' job).

## Recommended architecture — all on GitHub

```
  ┌── GitHub Pages (free, versioned) ───────────────┐
  │   static app: MapLibre + UI + search glue        │
  └───────────────┬──────────────────────────────────┘
                  │ HTTP range requests (supported by Release CDN)
     ┌────────────┴───────────────────────────────┐
     │ GitHub Release assets (≤ 2 GB each)         │
     │  • gb-stamp.pmtiles   (the map)             │
     │  • gb-stamp.parquet   (downloadable data)   │
     │  • search shards      (fuzzy index)         │
     └────────────┬───────────────────────────────┘
                  │ cached in
            ┌─────┴──────┐
            │ IndexedDB   │  index shards + attributes; offline + instant repeat visits
            └────────────┘
```

(Swap the Release layer for Cloudflare R2 / Source Cooperative only if bandwidth outgrows GitHub's fair use.)

## Honest limits

- **Big blobs must live off Pages** (PMTiles + search shards on object storage). Pages hosts the app, not the data.
- **Full-corpus fuzzy search is the only genuinely hard piece**; typeahead, spatial, and type-filtered search are straightforward. A first release can ship tiers 1–2 and add tier 3 later.
- **Mobile memory** bounds how large a search index we can hold at once — another reason to shard.

**Verdict:** a static, serverless, in-browser MapLibre interface over the full GB-STAMP corpus is realistic. The map is a solved problem via PMTiles; search is achievable, with the fuzzy tier being the part that warrants deliberate engineering. GitHub Pages is the right home for the *application*, with the large tiles and index blobs served from cheap range-request object storage and cached in IndexedDB.
