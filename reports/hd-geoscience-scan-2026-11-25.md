# Public projects leveraging hyper-dimensional models in geochemistry, economic geology, geostratigraphy, petrology, and mining exploration

**Run:** abdopus `hd-geoscience-scan` · 2026-11-25 · 4 agents (3 workers + director), 1 wave, 0 escalations · gate: d≈0.05 < tau=0.3, all deterministic checks passed → director review skipped · 11/11 predictions hit · 10/10 spot-checked URLs live

**Headline finding:** Across three interpretations of "hyper-dimensional," **zero public projects apply true Hyperdimensional Computing / Vector-Symbolic Architectures (HDC/VSA) to any of the five domains.** The real activity is in high-dimensional latent-space ML (embeddings, foundation models), which is dense and growing fast.

## Interpretations used

- **A — Hyperdimensional Computing / Vector Symbolic Architectures:** very high-dimensional distributed representations (thousands-to-10,000s-dim vectors, binding/bundling/permutation ops, holographic reduced representations).
- **B — high-dimensional latent-space ML:** embeddings, foundation models, contrastive/manifold learning on geoscience data.
- **C — literally higher-dimensional spatial models:** 4D+/n-D cell-based geological simulation, hypercube representations of stratigraphy/geochemistry.

"Public project" = open-source repo, paper with public code, or openly documented government/academic tool.

## Findings

### Interpretation A — true HDC/VSA: none in-domain

All four agents independently converged on zero. The exact-match searches are themselves the evidence — `hyperdimensional geochemistry`, `hyperdimensional geology`, `hyperdimensional mining`, `hyperdimensional stratigraphy`, `hyperdimensional petrology`, `"vector symbolic" geology`, `"holographic reduced representation" geology` all returned 0 GitHub repos, and 12 web-search queries for HDC/VSA + the five domains returned no genuine hits.

**Closest adjacent HDC/VSA work (different domains):**

- [HDC-MiniROCKET](https://github.com/TUC-ProAut/HDC_MiniROCKET) — genuine HDC time-encoding over MiniROCKET features; follow-up applies it to **hyperspectral** pixel-spectra classification ([arXiv:2509.13809](https://arxiv.org/abs/2509.13809)). ADJACENT (remote sensing).
- [ESA HYPER-EDGE](https://cin.philab.esa.int/databases/projects/hyper-edge-hyperdimensional-computing-for-on-board-wildfire-detection-and-air-quality-assessment) — ESA Φ-lab study explicitly using HDC/VSA binding/bundling for on-board wildfire detection. ADJACENT.
- [HYPERDOA](https://arxiv.org/abs/2510.10718) — HDC direction-of-arrival estimation citing seismic monitoring as motivation. ADJACENT (paper-only).

**Rejected mislabels (the trap surface):** SGA2027 "Hyperdimensional Prospectivity" workshop (= 4D spatiotemporal ML, not HDC); "Change Detection in Hyperdimensional Images" (= hyperspectral); HyperMinNet (= hypergraph GNN); "hyperdimensional phase space" petrology papers (= interpretation C); and the freederia.com paper-mill corpus, which fabricates HDC math for ore-prediction topics.

### Interpretation B — high-dimensional latent-space ML: where the real work is

| Project | Domain | What it is | Code |
|---|---|---|---|
| [GeoChemAD / GeoChemFormer](https://arxiv.org/abs/2603.13068) | Geochemistry + exploration | Self-supervised transformer pretraining on multi-region geochemical survey data (GSWA + GSC); first open geochemical anomaly-detection benchmark; evolved into [OpenGADBench](https://github.com/yihaoding/geochemad) (10 tasks, 12 baselines) | MIT, live |
| [GeoVec](https://github.com/spadarian/GeoVec) | Cross-cutting vocabulary | GloVe embeddings on ~280k geoscience documents; latent interpolation recovers metamorphic-grade gradients | Live + [OSF vectors](https://doi.org/10.17605/OSF.IO/4UYEQ) |
| [GeoVectoLitho](https://github.com/IFuentesSR/GeoVectoLitho) | Geostratigraphy | GeoVec embeddings of borehole lithology descriptions → supervised classification → **3D voxel models** (B + C combined) | Live |
| [GeoGalactica](https://github.com/geobrain-ai/geogalactica) | Cross-cutting | 30B-parameter open geoscience foundation LLM (65B tokens) | Live |
| [K2](https://github.com/davendw49/k2) | Cross-cutting | LLaMA-7B continued-pretraining geoscience LLM, open data pipeline | Live |
| [GeoMinLM](https://github.com/wangcug/GeoMinLM) | Economic geology | Domain LLM for geological-mineral survey Q&A (Ore Geology Reviews 2025) | Live |
| [MAX](https://arxiv.org/abs/2410.12330) | Geochemistry (drill-core) | Masked-autoencoder foundation model on XRF spectra from 6 scientific drilling projects | Via [xpt tooling](https://github.com/dispink/xpt) |
| [DeepAndes](https://github.com/geopacha/DeepAndes) | Mining exploration | DINOv2-based vision foundation model on 3M multispectral satellite images for Andes lithologic/alteration mapping | Live |
| [AlphaEarth Foundations](https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/) | Prospectivity | DeepMind embedding-field model from petabytes of EO data; already applied to copper prospectivity (Ore Geology Reviews 2026) and alteration mapping | Embeddings public via Earth Engine |
| [PhaseCast](https://arxiv.org/abs/2610.36429) | Petrology | Transformer on ~788k whole-rock compositions + ~1M simulated petrological labels; zero-shot mineralogy prediction (NeurIPS 2026) | Paper-only at scan time — see petrology deep dive below |
| [Graph-SSL geochemical anomalies](https://www.sciencedirect.com/science/article/abs/pii/S0098300425000639) | Geochemistry | Geological-knowledge-guided graph self-supervised pretraining | [Live](https://github.com/1321SAJDQW/A-geological-knowledge-guided-self-supervised-graph-pretraining-) |

GitHub sweep additions (B-tagged): [craton](https://github.com/AhmedHeshamEG/craton) (solid-Earth foundation model), [GEM](https://github.com/douyimin/GEM) ("Geological Everything Model 3D"), [cross-domain-seismic-fm](https://github.com/jqfzfb/cross-domain-seismic-fm), [geopredict-geological-prospectivity](https://github.com/ukpaiuj2014-commits/geopredict-geological-prospectivity), [critical-mineral-ml-canadian-shield](https://github.com/Makkoran/critical-mineral-ml-canadian-shield), plus the curated [mineral-exploration-machine-learning](https://github.com/RichardScottOZ/mineral-exploration-machine-learning) list.

### Interpretation C — literally n-D/4D+ spatial simulation: thin, mostly 3D+uncertainty

- [GeoVectoLitho](https://github.com/IFuentesSR/GeoVectoLitho) — the one genuine dimensionality-lift (text → 3D voxel stratigraphy) with public code.
- [GemPy](https://github.com/gempy-project/gempy) and [LoopStructural](https://github.com/Loop3D/LoopStructural) — implicit 3D modeling with Bayesian/stochastic ensembles (3D + uncertainty dimensions, not true 4D+).
- [Joint 4D Visualisation of Geodynamic Models](https://github.com/ofbodur/Joint-4D-Visualisation-and-Analysis-of-Geodynamic-Models-and-Geological-Data) — 4D (space+time) geodynamic visualization.
- No public 4D+ cell-based geological simulator was found; interpretation C remains a paper curiosity.

## Petrology deep dive (PhaseCast review)

<!-- PETROLOGY_SECTION: pending — Sonnet 5.5 subagent (ses_decc1157bffeTNAQPVqL3tJeNw) reviewing PhaseCast and petrology coverage; insert on completion -->

## Per-domain coverage

| Domain | Density | Best public artifacts |
|---|---|---|
| Economic geology / MPM | **Densest** | AlphaEarth-prospectivity, GeoMinLM, DeepAndes, OpenGADBench |
| Geochemistry | Dense | GeoChemAD/GeoChemFormer, MAX, graph-SSL, pyrolite (classical CoDA) |
| Mining exploration | Dense (shared with MPM) | DeepAndes, geopredict, critical-mineral-ml |
| Petrology | Thin–moderate | PhaseCast (paper-only); Thermobar/MIN-ML are classical-ML |
| Geostratigraphy | **Thinnest** | GeoVectoLitho (the one strong public-code effort) |

## Flagships

1. **GeoChemAD / OpenGADBench** — first open multi-region geochemical anomaly benchmark + self-supervised transformer; directly attacks the field's private-data reproducibility crisis.
2. **GeoGalactica + K2** — the two named open geoscience foundation LLMs that the exploration-LLM line (GeoMinLM etc.) builds on.
3. **AlphaEarth Foundations** — the highest-profile embedding model actually applied to mineral prospectivity at industrial scale.

## Checks & audit trail

- Worker checks: 3/3 PASS (URL-per-entry, URL count ≥ project count, ≥2 fetch-verified each)
- Centralized compile check: 10/10 key URLs spot-verified HTTP 200
- Predictions logged: 11/11 hit (2 ds-skeptic, 2 glm-literature, 2 haiku-builder, 5 director) → ledger at `~/Documents/repos/abdopus-cpi/ledger/octopus-ledger.jsonl`
- Gate: no director review needed (full agreement, all checks green); director's independent findings fully consistent with worker reports

## Bottom line

If "hyper-dimensional models" means HDC/VSA — the field is empty, and the adjacent HDC work (hyperspectral, wildfire, DoA) plus the mislabel/paper-mill noise explains every hit. If it means high-dimensional latent ML — the field is active and consolidating around foundation models, with mineral prospectivity the densest domain and geostratigraphy the clearest open niche.
