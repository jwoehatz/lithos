# Trap Falls and the Montana Analogy Claim — Verification

**Date:** 2026-11-25 · **Run:** abdopus worker ds-skeptic@1 (deepseek, skeptic lens), task well-studied-analogue.
**Question:** Verify or falsify the user's recollection that "the nearby Trap Falls may be analogous to a formation in Montana."

## What Trap Falls is

**Trap Falls is a real, named Ordovician metasedimentary formation in southwestern Connecticut — not a Montana unit, and not merely a locality.**

- **Trap Falls Formation** (Hartland Group), named by Crowley (1968) in the Long Hill and Bridgeport quadrangles, Fairfield Co., CT: "leucocratic feldspathic gneiss with interlayered schist and pegmatite," including the Shelton facies. Overlies The Straits Schist; underlies Southington Mountain Formation or Prospect Gneiss. Middle and Late Ordovician. ([USGS Geolex TrapFalls refs](https://ngmdb.usgs.gov/Geolex/UnitRefs/TrapFallsRefs_4151.html))
- Rodgers (1985) divided it into three members: lower schist and granulite member, Shelton (white gneiss) Member, and Carringtons Pond Member; age modified to Early–Middle Ordovician. ([USGS Geolex TrapFalls refs](https://ngmdb.usgs.gov/Geolex/UnitRefs/TrapFallsRefs_4151.html))
- Macrostrat at the Shelton locality (41.32 N, −73.09 W) confirms the unit and its members: Carringtons Pond Mbr (448–450 Ma), Shelton white gneiss Mbr (450–457 Ma), Schist and Granulite Mbr (457–464 Ma), plus the adjacent Pinewood Adamellite and The Straits Schist. ([Macrostrat API](https://macrostrat.org/api/units?lat=41.32&lng=-73.09&format=json))
- **Direct link to the local play:** CGNHS Guidebook No. 11 (2022) explains that Crowley's "upper member of The Straits Schist" was reinterpreted by Dieterich (1968) and folded by Rodgers (1985) into the Trap Falls Formation. So Trap Falls is the same belt as Old Mine Park's Straits Schist — the unit that absorbed part of what was once mapped as Straits. ([CGNHS No. 11 extracted text](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf), p. 12)
- The Trap Falls Formation is **well studied**: McDaniel, Hanson, McLennan & Sevigny (1997, *Can. J. Earth Sci.* 34:1286–1294) published whole-rock major elements, REE, Nd–Pb isotopes, and detrital zircon U–Pb for it — Grenvillian provenance, protolith of aluminous muds + quartz arenites on a trailing-edge margin. ([OpenAlex W1986516343](https://api.openalex.org/works/W1986516343))

## The Montana claim (verdict + verbatim quote if found)

**VERDICT: UNSOURCED — the claim is a misremembering. No published comparison between Trap Falls (or the Straits/Wepawaug/Hartland package) and any Montana formation exists, and no place named "Trap Falls" exists in Montana.**

Evidence, all fetch-verified this session:

1. **No "Trap Falls" place name in Montana.** GeoNames fulltext search for "Trap Falls" in the US returns exactly six features: Trap Falls Reservoir + Trap Falls Reservoir Dam (Trumbull/Shelton, CT — the local one), Trap Falls Brook (Ashby, MA), Trap Falls + Little Trap Falls (Ontonagon County, MI), and Trap Creek (Bonneville Co., ID). **Zero in Montana.** ([GeoNames](https://geonames.org/search.html?q=Trap+Falls&country=US); [Nominatim](https://nominatim.openstreetmap.org/search?q=Trap+Falls&format=json&countrycodes=us&limit=20) independently confirms MI + MA only)
2. **No literature pairing.** OpenAlex full-text search for "Trap Falls" + Montana returns only USGS water-quality reports (Circular 643, 1971; WSP 1871, 1968) — nationwide surface-water trace-element reconnaissance that sampled a "Trap Falls" site (the CT reservoir) and separately covers Montana. That is a coincidental co-occurrence in a nationwide dataset, **not a geological analogy**. ([OpenAlex](https://api.openalex.org/works?search=%22Trap%20Falls%22%20Montana&per-page=25))
3. **No Straits/Wepawaug/Hartland–Montana link.** OpenAlex full-text: "Straits Schist" + Montana → nothing relevant; "Wepawaug" + Montana → nothing relevant; "Hartland Group" + "Belt Supergroup" → nothing (only a USGS lexicon volume). ([OpenAlex Straits+MT](https://api.openalex.org/works?filter=fulltext.search:%22Straits%20Schist%22%20Montana&per-page=25&select=id,title,publication_year,doi,primary_location); [OpenAlex Wepawaug+MT](https://api.openalex.org/works?filter=fulltext.search:%22Wepawaug%22%20Montana&per-page=25&select=id,title,publication_year,doi,primary_location); [OpenAlex Hartland+Belt](https://api.openalex.org/works?filter=fulltext.search:%22Hartland%20Group%22%20%22Belt%20Supergroup%22&per-page=25&select=id,title,publication_year,doi,primary_location))
4. **The local guidebook never mentions Montana.** The full extracted text of CGNHS Guidebook No. 11 (203,485 chars) contains **zero** occurrences of "Montana" and only one passing mention of Trap Falls (the Dieterich/Rodgers reinterpretation above). The companion GEMS bedrock-map text (45,417 chars) also has zero Montana mentions. ([CGNHS No. 11 extracted text](https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf))
5. **DuckDuckGo returns nothing** for "Trap Falls" + Montana (geology, waterfall, creek, river, Belt Supergroup, NEIGC, Straits Schist, Hartland, Wepawaug — all zero-result). Wikipedia has no "Trap Falls Formation" article.

**Most plausible source of the confusion** (inference, not sourced): the word "trap" in geology means dark volcanic rock (trap rock) — CT's own Mesozoic basalt traps are famous — and "Trap Falls"/"Trap Hills" is a real place name in **Michigan's** Keweenaw (Ontonagon County), not Montana. The user likely conflated one of these with a Montana recollection. No Montana formation is named "Trap" in any source found.

## Is the analogue better studied?

**The honest answer: the best-studied analogue for the local rocks is not in Montana — it is the Trap Falls Formation itself, immediately adjacent and in the same belt.**

- The Trap Falls Formation has published **whole-rock majors + REE + Nd–Pb isotopes + detrital zircon U–Pb** (McDaniel et al. 1997) — precisely the data PhaseCast's protolith-reconstruction play needs, and far more than exists for Old Mine Park itself (only sparse 1970s USGS NGDB W/Be/Cu).
- Along-strike correlatives in MA/VT (Goshen Formation, Russell Mountain Formation, Moretown/Hawley) are the standard lithostratigraphic comparisons in the literature — but those are the "distal segments" another worker covers, and none of them is in Montana.
- Montana's metamorphic belts (Belt Supergroup, Dillon block) are not compared to the Connecticut Valley Synclinorium in any source found. The Belt Supergroup is a Proterozoic rift/passive-margin package — a poor protolith analogue for a Silurian–Devonian arc-derived sequence anyway.

**Bottom line for the play:** skip Montana. If the goal is a well-studied analogue with whole-rock data, the Trap Falls Formation literature (McDaniel et al. 1997) is the closest, best-studied, same-belt source — and it is already in the local belt, not a distant analogue.

## Sources (fetch-verified URLs)

All fetched this session with content retrieved (200 unless noted):

1. https://ngmdb.usgs.gov/Geolex/UnitRefs/TrapFallsRefs_4151.html — USGS Geolex Trap Falls publications (Crowley 1968 named; Rodgers 1985 members)
2. https://macrostrat.org/api/units?lat=41.32&lng=-73.09&format=json — Macrostrat units at Shelton (Trap Falls Fm + members, Pinewood Adamellite, Straits Schist)
3. https://api.openalex.org/works?search=%22Trap%20Falls%22%20Montana&per-page=25 — OpenAlex: only water-quality reports (Circular 643, WSP 1871)
4. https://api.openalex.org/works?filter=fulltext.search:%22Trap%20Falls%20Formation%22&per-page=25&select=id,title,publication_year,doi,primary_location — OpenAlex: 9 hits, all CT geology (McDaniel 1993/1996/1997, Sevigny & Hanson 1993, etc.)
5. https://api.openalex.org/works?filter=fulltext.search:%22Straits%20Schist%22%20Montana&per-page=25&select=id,title,publication_year,doi,primary_location — OpenAlex: nothing relevant
6. https://api.openalex.org/works?filter=fulltext.search:%22Wepawaug%22%20Montana&per-page=25&select=id,title,publication_year,doi,primary_location — OpenAlex: nothing relevant
7. https://api.openalex.org/works?filter=fulltext.search:%22Hartland%20Group%22%20%22Belt%20Supergroup%22&per-page=25&select=id,title,publication_year,doi,primary_location — OpenAlex: 1 hit, USGS lexicon only
8. https://api.openalex.org/works/W1986516343 — McDaniel, Hanson, McLennan & Sevigny 1997, Trap Falls provenance (CJES 34:1286–1294)
9. https://geonames.org/search.html?q=Trap+Falls&country=US — GeoNames: 6 US "Trap Falls" features, zero in Montana
10. https://nominatim.openstreetmap.org/search?q=Trap+Falls&format=json&countrycodes=us&limit=20 — Nominatim: MI + MA only
11. https://portal.ct.gov/-/media/DEEP/geology/guidebooks/CGNHSGuidebookNo11.pdf — CGNHS No. 11 (extracted text, 203,485 chars, zero "Montana")
12. https://digitalmaine.com/geo_docs/204 — NEIGC 2025 guidebook record (Rooney & Long, southwestern CT)
13. https://html.duckduckgo.com/html/?q=%22Trap+Falls%22+%22Montana%22 — zero results
14. https://html.duckduckgo.com/html/?q=%22Straits+Schist%22+Montana — zero relevant results
15. https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=%22Trap%20Falls%20Formation%22 — zero results

## Predictions

1. The Montana claim cannot be sourced — it is a misremembering. (Confidence: high; the name "Trap Falls" does not exist in Montana and no literature pairs the units.)
2. If any "Trap Falls"–Montana co-occurrence exists, it is a coincidental nationwide water-quality dataset (USGS Circular 643), not a geological analogy. (Confirmed: that is exactly what OpenAlex returned.)
3. The genuinely useful well-studied analogue for the local play is the Trap Falls Formation itself (McDaniel et al. 1997 whole-rock + isotope data), not any Montana unit. (Confirmed by the provenance literature.)

## Check result

- **PASS.** 15 distinct fetch-verified URLs with content retrieved this session (well above the ≥5 threshold), including two independent geoname authorities (GeoNames, Nominatim), three OpenAlex full-text queries, the USGS Geolex nomenclature record, and the locally extracted CGNHS No. 11 full text.
- Explicit verdict line present: **UNSOURCED / misremembered** — no Montana "Trap Falls" exists and no published CT↔Montana analogy exists.
- Negative results documented with evidence (zero-result searches, zero "Montana" occurrences in the 203K-char guidebook text), not just "not found."
