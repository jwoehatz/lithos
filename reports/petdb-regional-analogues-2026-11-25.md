# PetDB 2.0 regional analogue query — Old Mine Park (Trumbull, CT)

**Date:** 2026-11-25
**Run:** one-shot research worker (glm-literature route), Lithos repo
**Open question addressed:** *"The PetDB 2.0 regional analogue query has not been run (Straits Schist amphibolite, Pinewood Adamellite)"* — AGENTS.md §4.

---

## Verdict

**Partially.** PetDB 2.0 has a working, undocumented-but-discoverable REST API (`api.earthchem.org/v5/`) and it returns real whole-rock data within 100 km of Trumbull — but **none of it is the target geology**. Everything in the region is Early Jurassic CAMP (Central Atlantic Magmatic Province) diabase/gabbro/granophyre from two datasets: the Hartford basin (Grossman 1991, USGS OFR 91-322-K) and the Palisades Sill (Shirley 1987, J. Petrology). There are **zero** analyses of Straits Schist, Wepawaug Schist, Pinewood Adamellite, or any Connecticut Valley Synclinorium metamorphic rock. Zero amphibolite, schist, gneiss, marble, or skarn anywhere in New England (a 76–69°W, 40–46°N box returns 4 hornfels samples as its only metamorphic content). The 55 usable analyses (full PhaseCast core majors + Fe) are all mafic igneous rocks, which makes them **wrong-lithology analogues for the protolith play** — the Straits Schist amphibolite protolith is an Ordovician arc basalt, not a Jurassic rift diabase — but they do satisfy the PhaseCast input contract and could serve as a regional OOD/control set or a sanity check on the pipeline itself.

---

## Predictions (stated before scoring)

1. **P1:** PetDB 2.0 has ≥1 sample within 100 km of Trumbull (41.31, −73.19). **Scored: TRUE** — 97 samples, 418 analyses in the 40.8–42.0°N / 74.0–72.5°W box; closest usable sample 23.3 km (W-244939, Hartford basin).
2. **P2:** Amphibolite analyses with full majors exist somewhere in PetDB 2.0, but not within 200 km of Trumbull. **Scored: TRUE** — 1,197 amphibolite analyses globally (Colorado Plateau, Basin and Range, Japan, Greenland, New Caledonia, Egypt, China); zero in New England.
3. **P3:** A backing API is discoverable from the PetDB 2.0 web app without credentials. **Scored: TRUE** — `https://api.earthchem.org/v5/`, found by reading the Next.js chunk `9822-b5a2521d9fce7c2e.js` (service class at webpack module 5949), fully open, no auth.

---

## Evidence

### 1. API discovery (how the query was run)

PetDB 2.0 at `earthchem.org/petdb` is a Next.js SSR app. The page itself is a shell; the search UI is a client component (`n(52450)` in `petdb-88915e76ddbc102b.js`). Reading `_app-0f42b4f42738424a.js` yields the production config: `api_base_url: "https://api.earthchem.org"`, `pagesApiVersion: "v5"`. The sample-detail chunk chain (`petdb/sample/[id]-40e396c6a9783ae9.js` → `7772-5c8597303c82b2b6.js` → `9822-b5a2521d9fce7c2e.js`) contains the full service class:

- `GET /v5/search/results?<query>` — paginated search, `afterKey` cursor, `size` up to 1000
- `GET /v5/search/outputs?<query>` — variable facet aggregation
- `GET /v5/samples/<sampleId>` — sample metadata
- `GET /v5/samples/<sampleId>/metadata` — linked metadata (names, citations)
- `GET /v5/citations/<citationId>` — citation + datasets + methods
- `GET /v5/samples/lookup?size=20&q=<name>` — name autocomplete

Spatial filter: `polygons` parameter, JSON array of polygons, each polygon a ring of `[lon, lat]` pairs: `polygons=[[[-74.0,40.8],[-72.5,40.8],[-72.5,42.0],[-74.0,42.0],[-74.0,40.8]]]` (URL-encoded). Taxon filter: `taxons=metamorphic::[AMPHIBOLITE]` (category tree syntax from the nuqs parser in `_app` chunk, module 69736). Geo-feature filter: `geoFeatures=COUNTRY::[UNITED STATES]`.

Total DB size: **752,534 analyses**, all `dataSource: "PetDB"` (719,915 match the `PetDB` source filter; the remainder are TIP/tephra records). No ORIGEN content is present despite the prior expectation — `dataSources=ORIGEN` returns 0.

### 2. What the Trumbull bounding box contains

Query: `polygons=[[[-74.0,40.8],[-72.5,40.8],[-72.5,42.0],[-74.0,42.0],[-74.0,40.8]]]` → **418 analyses, 97 unique samples.**

| Rock class | Samples | Citation |
|---|---|---|
| DIABASE | 87 | GROSSMAN, 1991 (46) + SHIRLEY, 1987 (51 analyses) |
| GABBRO | 9 | GROSSMAN, 1991 |
| GRANOPHYRE | 1 | GROSSMAN, 1991 |

All 418 are `sampleGeologicSettings: ["CONTINENTAL RIFT"]`, `sampleGeologicAgeAge: JURASSIC` (or null), geo feature `CAMP / LARGE_IGNEOUS_PROVINCE`. The two sources:

- **Grossman, Gottfried & Froelich 1991**, USGS Open-File Report 91-322-K, "Geochemical data for Jurassic diabase associated with early Mesozoic basins in the eastern United States". Datasets `HARTFORD` (138 analyses) and `NEWARKE` (178 analyses). No DOI.
- **Shirley 1987**, "Differentiation and compaction in the Palisades Sill, New Jersey", J. Petrology 28, 835–865, DOI 10.1093/petrology/28.5.835.

Locations cluster at: Palisades sill (−73.96, 40.85), Newark basin (−73.95, 40.85), and Hartford basin (−72.78 to −72.95, 41.42–41.97).

### 3. Usable analyses (PhaseCast input contract)

Of 97 samples, **55** carry the full PhaseCast core major set (SiO₂, Al₂O₃, CaO, MgO, K₂O, Na₂O, TiO₂) plus Fe as FeO and/or Fe₂O₃. 25 of those also have Zr+Y+Nb (the immobile-element discrimination set the binding pitfall ruling requires); 36 have TiO₂+Y+Nb but no Zr.

Closest usable samples (distance from 41.31, −73.19):

| Sample | Rock | Lat | Lon | km | Citation | Majors | Ti,Zr,Nb,Y |
|---|---|---|---|---|---|---|---|
| W-244939 | DIABASE | 41.4167 | −72.9500 | 23.3 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244941 | DIABASE | 41.4167 | −72.9500 | 23.3 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244942 | DIABASE | 41.4167 | −72.9500 | 23.3 | GROSSMAN, 1991 | full | Ti,−,−,Y |
| W-244943 | DIABASE | 41.4167 | −72.9500 | 23.3 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244944 | DIABASE | 41.4667 | −72.9333 | 27.6 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244947 | DIABASE | 41.5000 | −72.9167 | 31.1 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244948 | DIABASE | 41.5000 | −72.9167 | 31.1 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244949 | DIABASE | 41.5000 | −72.9167 | 31.1 | GROSSMAN, 1991 | full | Ti,−,−,Y |
| W-244950 | DIABASE | 41.5333 | −72.8833 | 35.6 | GROSSMAN, 1991 | full | Ti,−,Nb,− |
| W-244957 | DIABASE | 41.8167 | −72.8666 | 62.4 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244958 | DIABASE | 41.8333 | −72.8666 | 64.1 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244959 | DIABASE | 41.9167 | −72.8166 | 74.3 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244960 | DIABASE | 41.9667 | −72.7833 | 80.5 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-244961 | DIABASE | 41.9667 | −72.7833 | 80.5 | GROSSMAN, 1991 | full | Ti,−,Nb,Y |
| W-235430 | DIABASE | 40.8500 | −73.9500 | 81.7 | GROSSMAN, 1991 | full | Ti,Zr,Nb,Y |
| W-235437 | GABBRO | 40.8500 | −73.9500 | 81.7 | GROSSMAN, 1991 | full | Ti,Zr,Nb,Y |
| W-235443 | GRANOPHYRE | 40.8500 | −73.9500 | 81.7 | GROSSMAN, 1991 | full | Ti,Zr,Nb,Y |
| 80-11 | DIABASE | 40.8500 | −73.9600 | 82.4 | SHIRLEY, 1987 | full | Ti,−,−,− |

(…37 more usable rows; full JSON retained in the run workspace.)

Sample detail URL pattern: `https://earthchem.org/petdb/sample/<sampleId>`; API: `https://api.earthchem.org/v5/samples/<sampleId>`. Example: W-244939 → `https://earthchem.org/petdb/sample/492976d6fcdd5205b1ddf77458d42a39`.

**Contract check (per `reports/oldmine-phasecast-play-2026-11-25.md`):**

- **Majors present:** yes for the 55 usable samples. Units are wt% throughout (`displayUnit: "wt%"`). Traces are ppm.
- **Fe spec:** Shirley reports Fe as FeO only (43 analyses; EMP on fused beads — FeO is total Fe expressed as FeO). Grossman reports FeO (titration) and Fe₂O₃ (ICP) in **separate analysis batches** — no batch has both. For PhaseCast, either FeO or Fe₂O₃ satisfies the contract; if both exist across batches, convert Fe₂O₃ → FeO (×0.8998) and sum to FeOT. Spot check W-244939: SiO₂ 52.0, Al₂O₃ 15.6, CaO 10.9, MgO 5.6, K₂O 0.56, Na₂O 2.13, TiO₂ 1.25, FeO 7.8 + Fe₂O₃ 3.65 → FeOT 11.08; sum = 99.53 — a normal un-normalized total.
- **Blank vs zero:** PetDB omits unmeasured variables entirely from the `variables` array (no nulls found in 418 analyses; 7 zero-valued entries, all `Cl = 0 ppm` in Grossman INAA data, which read as genuine below-detection zeros, not placeholders). This is *cleaner* than the PhaseCast CSV convention — absence = not measured, and the 7 zeros are literal zeros. **Do not renormalize** (binding rule; totals run 98–100% raw).
- **MnO, P₂O₅, LOI:** present in Grossman (MnO 85, P₂O₅ 44, LOI in Shirley) — PhaseCast ignores them; harmless.

### 4. Negative results (target units, documented with queries tried)

- `taxons=metamorphic::[AMPHIBOLITE]` + New England box (−76 to −69, 40–46): **0**. The only metamorphic content in that entire box is 4 hornfels analyses (HUSCH, 1992, Newark basin contact rocks).
- `taxons=metamorphic::[SCHIST]` / `[GNEISS]` / `[MARBLE]` / `[QUARTZITE]` / `[SKARN]` + New England box: **0 each**. Global counts for context: schist 793, gneiss 2,857, amphibolite 1,197, marble 135, skarn 0.
- `taxons=igneous:plutonic:felsic` + New England box: **0** — no granitoids at all, so no Pinewood Adamellite analogue even of the wrong age.
- `sampleNames=Straits|Wepawaug|Pinewood|Trumbull`: **0 each**.
- `citationTitles=Straits Schist|Wepawaug|Pinewood|Connecticut|synclinorium|New England|Appalachian`: **0 each**.
- Free-text `q=<term>`: **HTTP 500** on every term (server-side Elasticsearch error; the parameter is accepted by the schema but the backend fails). Recorded as a broken endpoint, not "no results".
- `geoFeatures=STATE::[CONNECTICUT]` and similar: **0** — the geo-feature vocabulary has no Connecticut entry at any level (COUNTRY::[UNITED STATES] works and returns 54,310).
- US amphibolites (232 analyses) are all Colorado Plateau / Basin and Range / Wyoming craton xenolith-hosting volcanic fields — southwestern US, not Appalachians.

**Interpretation:** PetDB 2.0's orogenic/metamorphic holdings are concentrated in ophiolites, arc terranes (Japan, New Caledonia, Egypt), and xenolith suites. The Appalachian orogenic belt — including the Connecticut Valley Synclinorium and Bronson Hill terrane — is simply not in the corpus. The prior expectation that "orogenic belts including the Appalachians may be covered" is **falsified for southwestern New England**.

### 5. What the regional data is actually good for

The 55 usable CAMP analyses are not protolith analogues — the Straits Schist amphibolite protolith is an Ordovician volcanic-arc tholeiite, whereas these are Jurassic continental-rift tholeiites. But they are:

1. **A pipeline validation set.** Full-major, trace-bearing, un-normalized whole-rock analyses 23–82 km from the park, in a format ready for the PhaseCast CSV contract. Running these first exercises the pyrolite → PhaseCast → MAGEMin chain on rocks that are *in* PhaseCast's volcanic training distribution before attempting the OOD amphibolite play.
2. **A regional OOD control.** CAMP diabase vs. the (still hypothetical) Straits protolith composition gives a same-area, different-tectonic-setting contrast for the anomaly-scoring step (playbook item 4).
3. **Immobile-element practice.** 25 samples carry Zr+Y+Nb+TiO₂, enough to build Ti-Zr-Y-Nb discrimination plots (e.g., Pearce & Cann) exactly as the binding pitfall ruling prescribes for metasomatized rocks.

---

## Fetch-verified sources

All URLs below were retrieved in this session (2026-11-25):

1. `https://earthchem.org/petdb` — PetDB 2.0 portal (Next.js shell)
2. `https://earthchem.org/` — EarthChem home; confirms PetDB 2.0 / ECL / Portal / LEPR structure
3. `https://earthchem.org/_next/static/chunks/pages/petdb-88915e76ddbc102b.js` — PetDB page chunk
4. `https://earthchem.org/_next/static/chunks/pages/_app-0f42b4f42738424a.js` — app config: `api_base_url`, `pagesApiVersion: "v5"`, search schema (polygons, taxons, geoFeatures parsers)
5. `https://earthchem.org/_next/static/8LpRUdPBneuHvtZ0Y7CZB/_buildManifest.js` — route → chunk map
6. `https://earthchem.org/_next/static/chunks/pages/petdb/sample/%5Bid%5D-40e396c6a9783ae9.js` — sample detail page chunk
7. `https://earthchem.org/_next/static/chunks/9822-b5a2521d9fce7c2e.js` — API service class (module 5949): all `/v5/` endpoints
8. `https://api.earthchem.org/` — API root (PetDB REST API banner)
9. `https://api.earthchem.org/v5/search/results?size=2` — global search; count 752,534
10. `https://api.earthchem.org/v5/search/results?size=1000&polygons=[[[-74.0,40.8],[-72.5,40.8],[-72.5,42.0],[-74.0,42.0],[-74.0,40.8]]]` — Trumbull box: 418 analyses
11. `https://api.earthchem.org/v5/samples/492976d6fcdd5205b1ddf77458d42a39` — W-244939 detail (Hartford basin diabase)
12. `https://api.earthchem.org/v5/samples/492976d6fcdd5205b1ddf77458d42a39/metadata` — sample metadata links
13. `https://api.earthchem.org/v5/citations/76cf99d3614e23eabab16fb27e944bf9` — Grossman 1991 citation record (USGS OFR 91-322-K, datasets HARTFORD/NEWARKE/CULPEPER/DANVILLE, 8 methods)
14. `https://api.earthchem.org/v5/search/outputs?polygons=...&size=100` — NE-region variable facet (65 distinct variables incl. Zr, Y, Nb, V)
15. `https://earthchem.org/petdb/sample/492976d6fcdd5205b1ddf77458d42a39` — sample detail web page (rendered)
16. `https://earthchem.org/resources/developers` — developer resources (WFS service, XML schema, ODM2; no v5 REST docs — the API used here is undocumented publicly)

Negative-result endpoints (fetched, failed as described): `q=` free-text search (HTTP 500, all terms); `resources/web-services-api` (404); `dataSources=ORIGEN` (0 — no ORIGEN content despite prior expectation).

---

## Open question (one)

The **EarthChem Portal** (`portal.earthchem.org`, linked from the developers page) exposes a WFS service with a `WR_Major_Element` layer that predates and may hold more than the v5 synthesis. If the amphibolite play needs true arc-tholeiite analogues, the Portal/WFS path — not PetDB 2.0 — is the next place to look. Not run here; out of scope for this report.

---

## Check result

**PASS.** Deterministic check run after report write:

- Fetch-verified distinct URLs: **16** (≥5 required) — listed above, all retrieved this session.
- Report file exists at `reports/petdb-regional-analogues-2026-11-25.md` with required headings: Verdict ✓, Predictions ✓, Evidence ✓, Fetch-verified sources ✓, Open question ✓, Check result ✓.
- Retries needed: 0 (check passed on first run).
