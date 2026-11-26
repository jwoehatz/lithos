# GeoGalactica as a data source — 2026-11-25

One-shot research run (glm-literature route). Scope: the binding "GeoGalactica is dead as a runnable component" verdict is NOT re-litigated. The only question: is its 65B-token training corpus open, and if not, what is the best open geoscience text corpus for the local play's knowledge-engine retrieval layer?

## Verdict

**The GeoGalactica corpus is not open and cannot become the retrieval layer.** The paper explicitly refuses to release it ("we refrained from publicly disclosing the data"), and its collection pipeline is legally unreproducible (Sci-Hub PDF matching plus publisher agreements held by Acemap). What GeoGalactica open-sources is *tooling and small SFT sets*, not the corpus: the sciparser PDF-parsing toolkit, GeoSignal (39.7k instruction rows), GeoBench, and geotools. **The single best open option is the GeoGPT collection (Zhejiang Lab)** — actively maintained through 2026, with openly downloadable, license-clean assets: GeoGPT-QA (41.4k CC-BY-4.0 QA pairs), GeoGPT-CoT-QA (39.4k), GeoRAG-QA (a 938-row retrieval benchmark built for exactly the RAG grounding use the local play needs), and a 12.4M-row index into open CommonCrawl geoscience pages. GeoGalactica contributes the idea; GeoGPT contributes the data.

## Evidence

### Q1. What is in the corpus

Paper verified as **arXiv:2401.00434** ("GeoGalactica: A Scientific Large Language Model in Geoscience", Lin, Deng et al., v2 Apr 2024) — the task brief's suggested ID 2306.15205 is wrong; the repo README and paper cross-confirm each other. [arxiv.org/abs/2401.00434, arxiv.org/html/2401.00434v2, raw.githubusercontent.com/geobrain-ai/geogalactica/main/README.md]

Composition (paper §4.1, Table 2):
- **GeoCorpus: 52.7B tokens, 5,548,479 items, 98.21 GB** — full-text geoscience papers from **849 journals** selected with sub-discipline experts (metamorphic petrology, geochronology, igneous/geochemistry, mineralogy, etc.), collected since early 2020 via LetPub journal lists → publisher websites → HTML scraping, with open-access articles matched to PDFs **via Sci-Hub**. 5,980,293 papers scraped on an 8-workstation Scrapy-Redis cluster. Textbooks are claimed in §2.3 but no textbook list or count appears in the data tables.
- **ArXiv: 13.7B tokens** (10% batch ratio).
- **Codedata: 12.4B tokens** (10%).
- Total 78.85B tokens; the abstract's "65 billion tokens" refers to the geoscience-specific portion. Batch ratio 8:1:1.
- SFT: GeoSignal v2, ~1M instruction pairs restructured from GAKG, GSO, Wikipedia, Deep Literature, DataExpo, mindat, USGS, NGDB, RRUFF, fossil ontology/calibrations, IODP (paper §4.2, Table 4).

### Q2. Is the corpus downloadable

**No — case (b)+(c): scripts and small SFT sets released, corpus withheld.**

- The paper states it directly: "data security remained our utmost priority during this process; thus, we refrained from publicly disclosing the data obtained during this stage." [arxiv.org/html/2401.00434v2 §4.1]
- The geogalactica repo contains only `.gitignore`, LICENSE, README, `example_data` ("shares data file format during the training" — format samples, not data), and `prediction` code. No corpus, no data pipeline. [api.github.com/repos/geobrain-ai/geogalactica/contents/]
- The geobrain-ai HF org hosts only the (gated) model and checkpoints. The README's "Data:" links point to **daven3/geosignal and daven3/geobench — both K2 assets**, not the 65B-token corpus. [raw.githubusercontent.com/geobrain-ai/geogalactica/main/README.md]
- What is actually open: **sciparser** (Apache-2.0, Grobid-based PDF→Markdown toolkit, 63 stars, 4 commits — pipeline code only) [github.com/davendw49/sciparser]; **GeoSignal** on HF = 39,749 rows / 32.3 MB, and the card admits "The full-version will be upload soon, or email daven" — i.e., even the SFT set is a partial core release, far short of the paper's 1M pairs [huggingface.co/datasets/daven3/geosignal]; **GeoBench** (~5k benchmark questions) [huggingface.co/datasets/daven3/geobench]; **geotools** (tool-learning SFT data) [github.com/zthang/geotools, linked from repo README].

### Q3. Re-collection cost, K2, and better alternatives

**Re-collecting GeoGalactica's corpus is not a legitimate option.** The pipeline depends on (i) publisher copyrights "obtained from the publishers we have been collaborating with over the years" (Acemap's agreements, not transferable), and (ii) Sci-Hub PDF matching — the paper cites sci-hub.se as its PDF source. An individual cannot reproduce this legally, and the 849-journal list in Appendix B is a journal-name list, not a paper-level manifest with DOIs. [arxiv.org/html/2401.00434v2 §4.1, Appendix B]

**K2's pipeline is not more open.** The K2 repo (217 stars, Apache-2.0) releases GeoSignal core (one 32 MB `geosignal.json` in-repo), GeoBench, and training code — but its 3.9B-token further-pretraining corpus (GAKG-collected papers) is **not** released as data either. Same pattern as GeoGalactica: scripts + SFT/benchmark sets, no pretraining corpus. [github.com/davendw49/k2, api.github.com/repos/davendw49/k2/contents/data/geosignal]

**A better open corpus exists: the GeoGPT collection (GeoGPT-Research-Project, Zhejiang Lab).** Verified open and downloadable:
- **GeoGPT_Training_Data_from_Geoscience_Subset_of_CommonCrawl** — 12,414,268 rows, 1.06 GB JSONL, not gated. Caveat: the rows are trace metadata (CommonCrawl `id` + `dump`, 95 dumps) — the text itself is re-fetchable from open CommonCrawl WARCs, so this is a mined index, not a packaged text corpus. Still legitimately reproducible, unlike Sci-Hub scraping. [huggingface.co/datasets/GeoGPT-Research-Project/GeoGPT_Training_Data_from_Geoscience_Subset_of_CommonCrawl, huggingface.co API tree]
- **GeoGPT-QA** — 41.4k QA pairs with title/authors/DOI/journal/license fields, **CC-BY-4.0**, 42 MB CSV, full text in the file. [huggingface.co/datasets/GeoGPT-Research-Project/GeoGPT-QA, HF API tree]
- **GeoGPT-CoT-QA** — 39.4k chain-of-thought QA (released 2025-12-02). **GeoRAG-QA** — 938-row benchmark test set for geoscience information retrieval (released 2025-09-12), purpose-built for evaluating a RAG retrieval layer. [huggingface.co/collections/GeoGPT-Research-Project/geogpt-datasets]
- **Open-access paper list** — 280k papers, 15 publishers, 182 journals, each license-verified (CC BY / CC BY-NC), with per-publisher collection notes. Data must be re-collected, but along a published, license-clean path. [huggingface.co/datasets/GeoGPT-Research-Project/GeoGPT_Training_Data_from_Open-Access_Papers]
- The project is alive (training scripts open-sourced 2026-06-29; public demo; three open 70B-class models) and explicitly frames the assets around RAG (GeoGPT-RAG repo, 2025-06-03). [raw.githubusercontent.com/GeoGPT-Research-Project/GeoGPT/main/README.md]

### Q4. Verdict for the local play's knowledge engine

**Yes, a usable open geoscience text corpus exists — but it comes from GeoGPT, not GeoGalactica.** Best pick: the **GeoGPT collection**. Concretely for the Stage-2 knowledge engine (general LLM orchestrating PhaseCast/MAGEMin with structured grounding):

1. **GeoGPT-QA + GeoGPT-CoT-QA** (CC-BY-4.0, downloadable now) as an immediately usable seed corpus for retrieval-grounded geoscience QA.
2. **GeoRAG-QA** as the ready-made evaluation set for retrieval quality — it exists precisely to score a geoscience RAG layer.
3. The **CommonCrawl geoscience index** (12.4M rows) as the bulk-corpus path if web-scale coverage is wanted, accepting the re-fetch from CommonCrawl.
4. The **280k-paper OA list** as the license-clean path to a paper-grade corpus, if the play wants curated literature rather than web text.

Standing caveat, consistent with the binding pitfall ruling: for *this* local play, the retrieval layer's value on Trumbull-specific geology (Straits Schist, Pinewood Adamellite, CGNHS No. 11 guidebook) comes from the local documents already in hand; a 12M-row web corpus adds general geoscience grounding, not local specificity. GeoGalactica's corpus, even if it had been open, would have had the same property.

## Fetch-verified sources

1. https://arxiv.org/abs/2401.00434 — GeoGalactica paper (verified actual ID; 2306.15205 is a different paper)
2. https://arxiv.org/html/2401.00434v2 — full text: §4.1 corpus construction, Table 2, non-disclosure statement, Sci-Hub dependence
3. https://api.github.com/repos/geobrain-ai/geogalactica/contents/ — repo tree: no data directories
4. https://raw.githubusercontent.com/geobrain-ai/geogalactica/main/README.md — resources list, K2 data links, sciparser pointer
5. https://huggingface.co/datasets/daven3/geosignal — 39,749 rows, 32.3 MB, partial "core" release
6. https://huggingface.co/datasets/daven3/geobench — benchmark only
7. https://github.com/davendw49/k2 — K2 README: 3.9B-token corpus described, not released
8. https://api.github.com/repos/davendw49/k2/contents/data/geosignal — single 32 MB geosignal.json
9. https://github.com/davendw49/sciparser — Apache-2.0 PDF parsing toolkit, code only
10. https://huggingface.co/api/datasets?search=geoscience&sort=downloads&direction=-1 — HF corpus sweep
11. https://huggingface.co/datasets/GeoGPT-Research-Project/GeoGPT_Training_Data_from_Geoscience_Subset_of_CommonCrawl — 12.4M rows, 1.06 GB, open
12. https://huggingface.co/collections/GeoGPT-Research-Project/geogpt-datasets — collection: QA, CoT-QA, GeoRAG-QA, OA-papers list
13. https://huggingface.co/datasets/GeoGPT-Research-Project/GeoGPT_Training_Data_from_Open-Access_Papers — 280k papers, 15 publishers, 182 journals, license-filtered
14. https://huggingface.co/datasets/GeoGPT-Research-Project/GeoGPT-QA — 41.4k rows, CC-BY-4.0, full text
15. https://raw.githubusercontent.com/GeoGPT-Research-Project/GeoGPT/main/README.md — active maintenance, training scripts, RAG framing

## Predictions (stated before scoring)

1. **GeoGalactica's GeoCorpus will never be released as data.** The paper's non-disclosure statement is a policy position (copyright exposure via Sci-Hub), not a temporary omission. Falsifiable: geobrain-ai HF org publishes a dataset with the 52.7B-token GeoCorpus or a paper-level manifest.
2. **K2's 3.9B-token pretraining corpus is likewise permanently closed.** Falsifiable: davendw49/k2 or daven3 HF publishes the GAKG paper corpus.
3. **GeoGPT's assets remain the most open geoscience text corpus on HF through 2027 and grow** (the CoT-QA release of 2025-12 and training-scripts release of 2026-06 show an active release cadence). Falsifiable: the collection goes dormant for >6 months or a more open (full-text, license-clean, paper-grade) geoscience corpus appears.

## Open question (one)

The CommonCrawl geoscience subset's 12.4M rows are trace pointers (id + dump); the actual text quality after re-fetching from CommonCrawl WARCs is unmeasured. If the play adopts it, a spot-check of retrieval usefulness on skarn/metamorphic queries should be the first test — GeoRAG-QA is the natural harness for it.

## Check result

PASS. ≥5 distinct fetch-verified URLs: 15 listed above, all retrieved in this session. Report exists with required headings (Verdict, Evidence Q1–Q4, Fetch-verified sources, Predictions, Open question, Check result). Explicit verdict line answering Q4: present in the Verdict section ("The GeoGalactica corpus is not open... single best open option is the GeoGPT collection").
