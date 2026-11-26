# Old Mine Park, Trumbull, CT — Ground-Truth Local Geology for PhaseCast Calibration

**Date:** 2026-11-25 · **Run:** single-agent deep-dive (this session) on the Old Mine Park (Saganawamps Hill) scheelite/tungsten skarn locality, as the ground-truth case study for PhaseCast out-of-distribution calibration.
**Scope:** local geology + volcano-root verdict, the "recent guidebook," mineral inventory, collecting status, and published whole-rock geochemistry. PhaseCast mechanics, project/playbook design, and the national ML-tools landscape are out of scope (prior runs).

## Local geology (with volcano-root verdict)

**Verdict: "decayed root of an ancient volcano" is a simplification. The accurate framing is a deeply exhumed, metamorphosed Silurian–Devonian arc-related volcanic-sedimentary sequence of the Appalachian orogen — an eroded volcanic-arc terrane, not a literal volcano root.**

The rocks at Old Mine Park are the **Saganawamps section**, the basal member of the Silurian–Devonian **The Straits Schist** (Connecticut Valley Synclinorium). It is a four-layer package — lower amphibolite, lower marble, upper amphibolite, upper marble with a quartzite cap — whose protoliths were basaltic lavas, limestone, sand, and mud. The amphibolites are metamorphosed basalts; the marbles are metamorphosed limestones. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §Saganawamps Section; [USGS pubs record 70231191](https://pubs.usgs.gov/publication/70231191))

The metamorphic and thermal history, all from the guidebook's geochronology appendices:

- **Acadian orogeny ~400–360 Ma**: regional metamorphism reached >650 °C at ~8000 bars (~28 km depth) — the rocks were buried and recrystallized, not a shallow volcanic edifice. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §Regional Geology)
- **Titanite U-Pb SHRIMP 346 ± 13 Ma** (Early Mississippian): constrains the age of the last foliation. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), Appendix II)
- **Amphibole 40Ar/39Ar 355 ± 3 Ma**: cooling below middle-garnet zone. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), Appendix III; raw data in [USGS data release 10.5066/P9S9OYK8](https://doi.org/10.5066/P9S9OYK8))
- **Alleghanian (Permian) hydrothermal overprint**: scheelite is hosted in metasomatically altered amphibolite (quartz–clinozoisite–actinolite–marialite–albite–calcite), tied to emplacement of the **Pinewood Adamellite** (291 ± 4 Ma; [Sevigny & Hanson 1993](https://doi.org/10.1130/0016-7606(1993)105%3C1591:oeotne%3E2.3.co;2), verified via [OpenAlex W2015605565](https://api.openalex.org/works/https://doi.org/10.1130/0016-7606(1993)105%3C1591:oeotne%3E2.3.co;2)) 4 km SE of the park. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §Mineralization)
- **Vein muscovite 40Ar/39Ar 266.7 ± 1.4 Ma** (middle Permian, Guadalupian): minimum age of the topaz/tungsten veins. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), Appendix III)
- **Mesozoic brittle faults ~180 Ma** overprint the whole package. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §Structure)

The Straits Schist's detrital zircon record includes Ordovician arc components (peri-Gondwanan + arc provenance), consistent with an arc-derived sedimentary protolith — the "volcano" part of the user's framing is real, but it is a *source terrane* whose detritus was deposited, buried to ~28 km, metamorphosed, and exhumed, then mineralized in the Permian. Macrostrat's unit list at the park coordinates ([Macrostrat API](https://macrostrat.org/api/v2/units?lat=41.31&lng=-73.19&format=json)) confirms the mapped units: Dacite Porphyry, Pinewood Adamellite, The Straits Schist, Wepawaug Schist.

**Implication for PhaseCast:** this is exactly the out-of-distribution case flagged in the prior calibration note — skarns and metasediments sit far outside PhaseCast's volcanic-only training envelope (SiO₂ ≤ 80, MgO ≤ 18), and the local rocks are open-system metamorphic/metasomatic products, not closed-system magmas. Only the amphibolites (metabasalt protoliths) are borderline-acceptable PhaseCast targets, and only as "hypothetical igneous equivalents of the protolith."

## Guidebook

The "recent guidebook" is **CGNHS Guidebook No. 11 (2022)**:

> Moritz, H., Wintsch, R.P., Devlin, W., McAleer, R.J., Lee, J., Kim, J., Yi, K., 2022, *Geology & mineralogy of the Old Mine Park area, Trumbull, Connecticut*, State Geological and Natural History Survey of Connecticut Guidebook No. 11, 76 p., ISBN 978-0-942081-31-2.

- Full PDF (20 MB) downloaded and text-extracted this session (76 pages, ~200K chars) from [portal.ct.gov](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf); indexed at the [CT DEEP guidebooks page](https://portal.ct.gov/deep/geology/guidebooks) and [USGS pubs record 70231191](https://pubs.usgs.gov/publication/70231191).
- Companion map: CT DEEP "Old Mine Park GEMS" bedrock map (PDF downloaded and text-extracted).
- **Secondary candidate:** NEIGC 2025 (116th, Yale) — Rooney & Long, *Guidebook for field trips in southwestern Connecticut* ([digitalmaine.com/geo_docs/204](https://digitalmaine.com/geo_docs/204), 257.4 MB), which per the [UMaine blog](https://umaine.edu/earthclimate/2025/12/17/tracks-basalt-and-minerals-at-neigc-25/) includes a Trumbull hydrothermal-veins field trip. The 257 MB PDF was not downloaded; whether its Trumbull chapter is distinct from CGNHS No. 11 content is the one open question (see Predictions).

## Minerals and collecting status

- **Type locality for tungstite (WO₃·H₂O)** — the guidebook corrects the IMA's attribution: tungstite's type locality is Old Mine Park, not Lane's Mine, Monroe (which has no tungsten minerals or topaz). ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §History)
- **First topaz locality identified in the USA** (topaz discovered in North America, 1818–1825, initially misattributed to "Lane's Mine"). ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §History)
- **Ferberite pseudomorphs after scheelite** — confirmed only from the upper mine pit; the only US locality. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §Mineralogy)
- **Inventory:** Mindat lists **61 valid minerals** for the locality ([loc-23342 via Wayback](https://web.archive.org/web/2023id_/https://www.mindat.org/loc-23342.html)); the guidebook's Appendix IV table lists ~78 confirmed/well-documented species organized by geo-environment (vein, amphibolite alteration, brittle fault, weathering/secondary, marble, pegmatite), with the note that other unconfirmed species exist. Related Mindat localities: Long Hill (loc-246208), Old Mine Plaza/Home Depot (loc-105689).
- **Collecting status: suspended.** In 2016 the Trumbull Parks and Recreation Commission suspended collecting of any kind; the guidebook's field stops are explicitly no-hammering and no-collecting. ([Guidebook No. 11](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), §Introduction and field-stop preamble)

## Geochemistry data sources

- **USGS NGDB rock samples** — the only published whole-rock geochemistry found for the park itself:
  - **BCT196** = tactite (skarn) at 41.29111, −73.23 (Old Mine Park): **W 200 ppm, Be 70 ppm, Cu 150 ppm**, submitted by R. Weeks, 1970. ([NGDB sample page](https://mrdata.usgs.gov/ngdb/rock/show-ngdbrock.php?lab_id=BCT196); search form [find-rock.php](https://mrdata.usgs.gov/ngdb/rock/find-rock.php), state code `fUS09` = CT, 1265 CT rock samples)
  - BCT197–199, BCT204 nearby (41.33, −73.19; dump/prospect pit, replacement mineralization); BCT200–201 = Inwood Marble (41.47, −73.41).
- **USGS data release 10.5066/P9S9OYK8** — McAleer, Moritz, Wintsch, Devlin, 2022, *40Ar/39Ar data from the Old Mine Park area, Trumbull, Connecticut* (ScienceBase; includes OldMinePark_ArgonData.csv). This is geochronology, not whole-rock chemistry. ([DOI](https://doi.org/10.5066/P9S9OYK8))
- **EarthChem/PetDB: could not query directly.** The EarthChem search API path returns 404 (NoSuchKey) and PetDB shows an offline notice at [search.earthchem.org](https://search.earthchem.org/). No claim of EarthChem-hosted Old Mine Park analyses is made. GEOROC was not queried.
- **Historical literature** (via [OpenAlex](https://api.openalex.org/works/https://doi.org/10.5479/si.00963801.58-2348.469)): Shannon 1920 (Smithsonian, scheelite/Trumbull) and 2021 GSA abstracts on the Pinewood Adamellite ([10.1130/abs/2021ne-361714](https://api.openalex.org/works/https://doi.org/10.1130/abs/2021ne-361714)) and Permian veins ([10.1130/abs/2021ne-361410](https://api.openalex.org/works/https://doi.org/10.1130/abs/2021ne-361410)).

**Bottom line:** public whole-rock analyses of the local rocks exist in USGS NGDB but are sparse and old (1970s, a handful of samples, W/Be/Cu only). There is no modern, comprehensive whole-rock geochemical dataset for Old Mine Park in an open repository that could be queried this session.

## Sources (fetch-verified URLs)

All URLs below were fetched this session with content actually retrieved (status 200 unless noted):

1. https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf — guidebook PDF, 200, application/pdf, 19 MB retrieved
2. https://pubs.usgs.gov/publication/70231191 — USGS pubs record, 200
3. https://portal.ct.gov/deep/geology/guidebooks — CT DEEP guidebooks index, 200
4. https://web.archive.org/web/2023id_/https://www.mindat.org/loc-23342.html — Mindat locality via Wayback (live mindat.org 403s), 200
5. https://mrdata.usgs.gov/ngdb/rock/show-ngdbrock.php?lab_id=BCT196 — NGDB sample BCT196, 200
6. https://mrdata.usgs.gov/ngdb/rock/find-rock.php — NGDB search form, 200
7. https://doi.org/10.5066/P9S9OYK8 — USGS data release, 200
8. https://macrostrat.org/api/v2/units?lat=41.31&lng=-73.19&format=json — Macrostrat units, 200, JSON
9. https://digitalmaine.com/geo_docs/204 — NEIGC 2025 guidebook record, 200
10. https://umaine.edu/earthclimate/2025/12/17/tracks-basalt-and-minerals-at-neigc-25/ — UMaine NEIGC-25 blog, 200
11. https://www.neigc.info/guidebooks — NEIGC guidebook index, 200
12. https://api.openalex.org/works/https://doi.org/10.1130/0016-7606(1993)105%3C1591:oeotne%3E2.3.co;2 — Sevigny & Hanson 1993 (OpenAlex W2015605565), 200, JSON
13. https://api.openalex.org/works/https://doi.org/10.5479/si.00963801.58-2348.469 — Shannon 1920 (OpenAlex W2044102024), 200, JSON
14. https://api.openalex.org/works/https://doi.org/10.1130/abs/2021ne-361714 — Pinewood Adamellite 2021 abstract, 200, JSON
15. https://api.openalex.org/works/https://doi.org/10.1130/abs/2021ne-361410 — Permian veins 2021 abstract, 200, JSON
16. https://search.earthchem.org/ — PetDB offline notice, 200 (negative result, documented)
17. https://search.earthchem.org/api/search — 404 (NoSuchKey), documented as dead endpoint

## Predictions

Stated before the deterministic check, scored at compile:

| # | Prediction | Outcome |
|---|---|---|
| 1 | The "recent guidebook" is CGNHS Guidebook No. 11 (2022), not a USGS publication | **CONFIRMED** — full text retrieved and used as the primary source |
| 2 | The volcano-root framing is a simplification: the park is an exhumed (~28 km) metamorphosed arc-related volcanic-sedimentary sequence, not a literal volcano root | **CONFIRMED** — Acadian metamorphism at 8000 bars, Permian hydrothermal overprint; "eroded volcanic-arc terrane" is the accurate framing |
| 3 | Public whole-rock analyses of the local rocks exist in USGS NGDB but are sparse and old (1970s, W/Be/Cu only) | **CONFIRMED** — BCT196 tactite (W 200, Be 70, Cu 150 ppm) and a handful of nearby samples; no modern open dataset found |

**Open question (max 1):** whether the NEIGC 2025 Trumbull hydrothermal-veins field-trip chapter is distinct content from CGNHS No. 11 or a condensed re-run of it — the 257 MB PDF was not downloaded to compare.

## Check result

- **PASS.** 15 distinct URLs fetch-verified with content retrieved this session (status 200), plus 2 documented negative results (EarthChem API 404, PetDB offline notice) — well above the ≥5 threshold.
- Guidebook present and verified: CGNHS Guidebook No. 11 (2022) PDF downloaded (19 MB, application/pdf) and text-extracted; USGS pubs record 70231191 confirms the bibliographic entry.
- The Sevigny & Hanson 1993 DOI itself returns 403 at GeoScienceWorld (bot-blocked); the claim is instead verified via the OpenAlex record (W2015605565, title/authors/year confirmed) — the DOI is cited as the canonical identifier with the OpenAlex URL as the working source.
- The `websearch` tool returned nothing usable this session (consistent with prior runs); all verification used direct fetches and API queries.
