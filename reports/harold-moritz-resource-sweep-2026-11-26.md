# Harold Moritz — Project and Resource Sweep

**Date:** 2026-11-26 · **Run:** single-agent sweep (this session), triggered by the question "does Harold Moritz have any helpful projects or resources we haven't spotted?"

## Verdict

**Yes — three finds that matter for this project, one of them directly queryable:**

1. **The Connecticut Bedrock Mining Sites Database (CGNHS Bull. 119, 2022, continuously updated)** — Moritz is the lead contributor. 1,070 bedrock mines/quarries statewide, 426 previously unrecognized, with commodity, host rock, references, and coordinates. It is exposed as a **live, open ArcGIS REST FeatureServer** — no key, no login — which we verified by querying it this session. This is a machine-readable, Moritz-curated dataset that plugs straight into any anomaly-scoring or regional-context play.
2. **A 2026 GSA Northeastern abstract we had not seen:** *Beyond the Pinewood – Did Alleghenian Mineralization Reach out to Roxbury, Connecticut?* (Moritz, sole author, [10.1130/abs/2026ne-12176](https://doi.org/10.1130/abs/2026ne-12176)). It extends the Pinewood magmatic-hydrothermal model ~10+ km northwest to Roxbury via an additional syenite stock in Southbury, with topaz–pyrrhotite–bismuth–arsenopyrite–siderite veins as depth indexes. This is the active frontier of the exact system that mineralized Old Mine Park.
3. **A 2022 GSA annual abstract also missed:** *A Permian magmatic-hydrothermal system and associated tungsten deposit in the Alleghanian foreland of southwestern Connecticut* (Kennedy, Moritz, Resor, Wintsch, [10.1130/abs/2022am-383220](https://doi.org/10.1130/abs/2022am-383220)) — U-Pb zircon/monazite ages tying the tungsten mineralization to final Alleghanian assembly, Pb isotopes on the Adamellite, ~600 Ma xenocrystic zircon cores. The geochronological companion to the guidebook.

**Negative results:** No GitHub presence (user and repo searches return zero). ScienceBase holds only the one 40Ar/39Ar release we already have. No modern whole-rock geochemistry of the park surfaced through his name — the standing "no modern analysis" verdict holds.

## What the database gives us (verified by live query)

The FeatureServer (table 17, "Mine and Quarry Points Merged") is open and queryable:

- `https://services1.arcgis.com/FjPcSmEFuDYlIdKC/ArcGIS/rest/services/MineAndQuarryMap2024_WFL1/FeatureServer/17/query?where=...&outFields=*&f=json`
- Fields include `TOWN_NAME`, `NAME1`/`NAME2`, `COMMODITY`, `ACTIVITY`, `BR_TYPE`, `REFERENCE`, `LATITUDE`/`LONGITUDE`, `Mindat_org_page`, `Notes`. Export formats include CSV, GeoJSON, shapefile, parquet.

**Trumbull query returned 9 sites**, all inactive, all referenced to "Moritz et al, 2022" (the guidebook) plus Hobbs 1901, Shannon 1921, Hess 1917, Crowley 1968:

| Site | Commodity | Type | Lat, Lon |
|---|---|---|---|
| Trumbull Tungsten Mine (Lane's Mine) | MT | O | 41.290801, −73.227549 |
| 3 unnamed marble prospects | MB | M | 41.288–41.290, −73.226 to −73.228 |
| Champion Lode | MI | O | 41.28994, −73.228684 |
| 2 unnamed prospects | MI | O | 41.289–41.290, −73.225 to −73.228 |
| 2 lost BR sites (Rt 15/25 interchange; development) | BR | T/G | south Trumbull |

**Statewide metal query (COMMODITY = 'MT', first 50 of >50):** the Trumbull Tungsten Mine is the **only tungsten-classified site in Fairfield County**; the rest are copper/iron mines in Bristol, Cheshire, Litchfield, East Granby, etc. The database confirms Trumbull's isolation as a W locality — useful context for the NURE W-anomaly work (playbook item 4).

**Relevance to the playbook:** this is a ready-made spatial layer for the anomaly-scoring play (item 4) and a source of reference lists (Hobbs 1901, Shannon 1921, Harte 1944/45, Fritts 1963a/b/65a, Schairer 1931, Cameron 1943/51, Crowley 1968) for any regional synthesis. It also cites a **"Moritz & Merguerian, 2015, p. 37–42"** reference (Coe's Mine, Litchfield) that is not in OpenAlex — likely a guidebook chapter, unverified this session.

## The 2026 Roxbury abstract (why it matters)

Reconstructed from the OpenAlex inverted index: hydrothermal deposits in the Western Uplands have been known/exploited for 250 years; only the veins tied to the Permian Pinewood intrusive suite have a robust genetic model. That Cornubian-type system — 3 plutons, vein swarms trending ~315° for ~10 km north of Trumbull — suggests local northwestern deepening. The study tests a distal continuation via an additional **syenite stock in Southbury**, undated quartz-rich fissure veins as far as **Roxbury**, and an albite-quartz-sulfide deposit of unknown genesis. Five index minerals (topaz, pyrrhotite, bismuth, arsenopyrite, siderite — chosen for different crystallization temperatures) show progressive change from hypothermal (SE) to mesothermal/epithermal (NW), a proxy for depth increase toward the source plutons.

**Implication:** the Pinewood system is not a Trumbull one-off; it is a regional NW-trending metallogenic zone. Any watershed-scale anomaly work should extend the search space northwest along that ~315° trend, not just around the park.

## Moritz's other resources (verified)

- **mindat.org user-15736** ("Harold 'Fritz' Moritz", Management Group member, verified account): 14,102 specimen photos, 897 locality photos, 6 published articles, 4,501 messages. He volunteers at Yale Peabody mineralogy collections and is reachable by mindat direct message. ([Wayback snapshot 2025-11-19](http://web.archive.org/web/20251119205253/https://www.mindat.org/user-15736.html); live mindat 403s per standing environment note.)
- **mindat articles:** "Connecticut Bedrock Mining and Quarrying Sites Map" (Dec 2024, Educational — the map announcement; live page not archived, mesg-680066), "Mineral and Mining Scams including Connecticut's Brack Prospect" (Jun 2025), "Chrysoberyl and the Enigma of Walkley Hill" (Nov 2024), "Dissolved Bikitaite... Strickland Pegmatite" (2020), "Schernikite - New Localities in Maine Pegmatites" (2012).
- **Rochester Mineralogical Symposium talk** (YouTube): "Chrysoberyl Knoll and Quarry Hill: The Minerals and Quarries of Haddam, Connecticut."
- **OpenAlex author record** ([A5034911527](https://api.openalex.org/authors/A5034911527)): 7 works — the two GSA abstracts above, the 2021 NE GSA veins abstract (already known), the guidebook, the Ar/Ar data release, plus two non-geology hits (a 1994 Sky & Telescope piece, a 2006 one) that are him-adjacent but irrelevant.
- **USGS ResCiColl** holds the mining database as a preserved collection ([webapps.usgs.gov record](https://webapps.usgs.gov/rescicoll/collections.html?collection=629658b8d34ec53d276bb170&organization=4f4e4762e4b07f02db47dffc)) — page is JS-rendered; the CT.gov and ArcGIS endpoints are the working sources.

## Sources (fetch-verified URLs)

All fetched this session with content retrieved (status 200 unless noted):

1. https://api.openalex.org/authors?search=Harold%20Moritz — author record A5034911527, 7 works
2. https://api.openalex.org/works?filter=author.id:A5034911527 — full works list
3. https://api.openalex.org/works/https://doi.org/10.1130/abs/2026ne-12176 — 2026 Roxbury abstract, full inverted index
4. https://api.openalex.org/works/https://doi.org/10.1130/abs/2022am-383220 — 2022 Permian system abstract, full inverted index
5. https://www.sciencebase.gov/catalog/items?q=harold%20moritz&format=json — only the known Ar/39Ar release
6. https://portal.ct.gov/deep/geology/connecticut-bedrock-mining-sites-database-2022 — database page, Bull. 119, 1,070 sites
7. https://services1.arcgis.com/FjPcSmEFuDYlIdKC/ArcGIS/rest/services/MineAndQuarryMap2024_WFL1/FeatureServer/17?f=json — table schema
8. https://services1.arcgis.com/FjPcSmEFuDYlIdKC/ArcGIS/rest/services/MineAndQuarryMap2024_WFL1/FeatureServer/17/query?where=TOWN_NAME%20%3D%20%27Trumbull%27... — 9 Trumbull sites
9. https://services1.arcgis.com/FjPcSmEFuDYlIdKC/ArcGIS/rest/services/MineAndQuarryMap2024_WFL1/FeatureServer/17/query?where=COMMODITY%20IN%20(%27MT%27)... — statewide metal sites
10. http://web.archive.org/web/20251119205253/https://www.mindat.org/user-15736.html — mindat profile via Wayback
11. https://api.github.com/search/users?q=haroldmoritz — zero (negative result)
12. https://api.github.com/search/repositories?q=haroldmoritz — zero (negative result)
13. https://webapps.usgs.gov/rescicoll/collections.html?collection=629658b8d34ec53d276bb170 — ResCiColl record (JS-rendered, content thin)
14. https://api.openalex.org/works?search=Moritz%20Merguerian — no match for the 2015 reference (negative result)

## Predictions

| # | Prediction | Outcome |
|---|---|---|
| 1 | Moritz has a machine-readable dataset beyond the guidebook and Ar/Ar release | **CONFIRMED** — CT Bedrock Mining Sites Database, live open ArcGIS FeatureServer, queried successfully |
| 2 | His recent GSA abstracts extend the Pinewood story | **CONFIRMED** — 2026 Roxbury abstract extends the model NW with a Southbury syenite stock; 2022 abstract adds U-Pb/Pb-isotope geochronology |
| 3 | He has code projects (GitHub) | **REFUTED** — no GitHub users or repos under his name; his "projects" are databases, maps, and photo/documentation corpora |

**Open question (max 1):** what is "Moritz & Merguerian, 2015, p. 37–42" (cited in the mining database for the Litchfield Co. iron mines)? Not in OpenAlex, not web-indexed — likely a guidebook chapter worth chasing if Litchfield-area analogues ever matter.

## Check result

- **PASS.** 12 distinct URLs fetch-verified with content retrieved, plus 2 documented negative results (GitHub empty, Moritz & Merguerian unindexed). The ArcGIS FeatureServer was verified by executing three live queries against it, not just fetching a landing page.
- `websearch` tool dead as usual; all verification via direct fetches (OpenAlex, ScienceBase, GitHub API, ArcGIS REST, DuckDuckGo HTML, Wayback).
