# Public projects leveraging hyper-dimensional models in geochemistry, economic geology, geostratigraphy, petrology, and mining exploration

**Run:** abdopus `hd-geoscience-scan` · 2026-11-25 · 4 agents (3 workers + director), 1 wave, 0 escalations · gate: d≈0.05 < tau=0.3, all deterministic checks passed → director review skipped · 11/11 predictions hit · 10/10 spot-checked URLs live · follow-up passes: Sonnet 5.5 petrology deep dive + 2-worker loose-ends verification (all checks passed)

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
| [PhaseCast](https://arxiv.org/abs/2610.36429) | Petrology | Transformer on ~788k whole-rock compositions + ~1M simulated petrological labels; zero-shot mineralogy prediction (NeurIPS 2026) | [Live](https://github.com/matthew-j-liu/phasecast) (MIT, released 2026-11) — see petrology deep dive below |
| [Graph-SSL geochemical anomalies](https://www.sciencedirect.com/science/article/abs/pii/S0098300425000639) | Geochemistry | Geological-knowledge-guided graph self-supervised pretraining | [Live](https://github.com/1321SAJDQW/A-geological-knowledge-guided-self-supervised-graph-pretraining-) |

GitHub sweep additions (B-tagged): [craton](https://github.com/AhmedHeshamEG/craton) (solid-Earth foundation model), [GEM](https://github.com/douyimin/GEM) ("Geological Everything Model 3D"), [cross-domain-seismic-fm](https://github.com/jqfzfb/cross-domain-seismic-fm), [geopredict-geological-prospectivity](https://github.com/ukpaiuj2014-commits/geopredict-geological-prospectivity), [critical-mineral-ml-canadian-shield](https://github.com/Makkoran/critical-mineral-ml-canadian-shield), plus the curated [mineral-exploration-machine-learning](https://github.com/RichardScottOZ/mineral-exploration-machine-learning) list.

Verified loose ends (follow-up pass, all primary-source verified):

- [Geo-Hgan](https://github.com/cbn001012/Geo-Hgan-Unsupervised-anomaly-detection-in-geochemical-data-via-latent-space-learning) — autoencoder + latent-space GAN for unsupervised geochemical anomaly detection (Ding et al., *Computers & Geosciences* 192:105703, 2024, [doi](https://doi.org/10.1016/j.cageo.2024.105703); 85% AUROC). **B**, economic geology, Apache-2.0, live.
- [Causal-VAE geochemical anomalies](https://www.sciencedirect.com/science/article/pii/S0098300425002407) — Ni & Xiong, interpretable causal VAE (SCM DAG over ore-controlling factors, counterfactual reasoning; 39-dim input → 117-dim latent; Nanling case study), *C&G* 208:106090, Feb 2026, [doi](https://doi.org/10.1016/j.cageo.2025.106090). **B**, code [live](https://github.com/kiritonfan/An-interpretable-causal-variational-autoencoder) (MIT).
- [DEEP-SEAM](https://gmd.copernicus.org/articles/19/2593/2026) — explainable semi-supervised deep learning (DevNet) for REE prospectivity, Northern Curnamona Province, South Australia; 57 multi-source features, SHAP interpretability (Luo et al., *GMD* 19:2593–2625, 2026; preprint [EGUsphere-2025-3283](https://doi.org/10.5194/egusphere-2025-3283)). **B**, code on [Zenodo](https://doi.org/10.5281/zenodo.17098677) + [github.com/EarthByte/MPM_Curnamona_REE](https://github.com/EarthByte/MPM_Curnamona_REE) (GPL-3.0).
- [PetroMind](https://github.com/connamulder/PetroMind) — multimodal petrographic foundation model built on Qwen2.5-VL (LoRA adapters; rock-image classification ≈97% accuracy, lithological description generation; SA-Rock metric), Chen et al., *Appl. Comput. Geosci.* 29:100314, 2026, [doi](https://doi.org/10.1016/j.acags.2025.100314). **B**, petrology-relevant but **imagery-only** (thin-section photos, no geochemistry), Apache-2.0, live.
- [Parsa et al. 2026](https://link.springer.com/article/10.1007/s11053-025-10564-0) — fine-tuned BERT (768-d embeddings per H3 cell, 1.8M cells across Canada) + self-supervised transformer over 790 covariates (50-d embeddings) for critical-minerals prospectivity mapping (MVT Zn–Pb), *Nat. Resour. Res.* 35:207–225. **B**, economic geology; no official code, third-party implementation [live](https://github.com/RichardScottOZ/geoscience-transformers-for-predictive-mapping-of-critical-minerals).

Additional projects surfaced via the Taghipour et al. 2026 mineral-exploration foundation-model survey ([preprint](https://www.preprints.org/manuscript/202607.2303), DOI 10.20944/preprints202607.2303.v1 — not peer-reviewed; preprints.org page bot-blocked, verified via DOI and MCML page), all with public code, none in the earlier lists:

- [JiuZhou](https://github.com/THU-ESIS/JiuZhou) — geoscience LLM (Mistral-7B, two-stage pre-adaptation), open weights.
- [MetalGPT-1](https://huggingface.co/nn-tech/MetalGPT-1) — Nornickel 32B metallurgy/mining LLM (Qwen3-32B base), open weights (cc-by-nc-sa-4.0).
- [PEACE / GeoMap-Agent](https://github.com/microsoft/PEACE) — MLLM for geologic-map understanding (CVPR 2025), MIT, code + GeoMap-Bench dataset.
- [DAN-GRF](https://github.com/Saeid1986/DAN-GRF) — deep autoencoder + geographical random forest for geochemical anomaly detection (R).
- [NRCan geoscience language models](https://github.com/NRCan/geoscience_language_models) — GloVe + BERT retrained on geoscience text (MIT); the base of the Parsa et al. embedding pipeline.

Also named by the survey but **no public code**: GFM4MPM (arXiv:2406.12756, SRI; US patent app 18/980,409 only).

### Interpretation C — literally n-D/4D+ spatial simulation: thin, mostly 3D+uncertainty

- [GeoVectoLitho](https://github.com/IFuentesSR/GeoVectoLitho) — the one genuine dimensionality-lift (text → 3D voxel stratigraphy) with public code.
- [G2S](https://github.com/GAIA-UNIL/G2S) — QuickSampling multiple-point statistics stochastic simulation, "developed without restrictions regarding the dimensionality of the data (e.g. 1D, 2D, 3D, nD)" (Gravey & Mariethoz 2020, [GMD 13:2611](https://doi.org/10.5194/gmd-13-2611-2020)). The one verified genuinely n-D geoscience simulation tool. **C**, GPL-3.0, actively maintained (GAIA lab, UNIL + IGF).
- [GemPy](https://github.com/gempy-project/gempy) and [LoopStructural](https://github.com/Loop3D/LoopStructural) — implicit 3D modeling with Bayesian/stochastic ensembles (3D + uncertainty dimensions, not true 4D+).
- [Joint 4D Visualisation of Geodynamic Models](https://github.com/ofbodur/Joint-4D-Visualisation-and-Analysis-of-Geodynamic-Models-and-Geological-Data) — 4D (space+time) geodynamic visualization.
- No public 4D+ cell-based geological simulator was found; interpretation C remains a paper curiosity.

Loose-end rulings on interpretation C (follow-up pass):

- **pyKriging** ([repo](https://github.com/capaulson/pyKriging), 390★, MIT, active) — dimension-agnostic but a **general surrogate-modelling/GP toolkit for expensive-function optimization**, not a geoscience tool. Excluded from C. The geoscience kriging tool is a different project: GeoStat-Framework/PyKrige (2D/3D).
- **USGS mineral-prospectivity code: does not exist.** The `usgs` GitHub org was archived Sep 2026; org searches for "prospectivity" and "mineral" return 0 repos. USGS publishes prospectivity **models as data** (tri-national Critical Minerals Mapping Initiative gradient-boosting GeoTIFF grids, [doi](https://doi.org/10.5066/P970GDD5)), with AI assessment work done externally (DARPA CriticalMAAS). Nearest open-government equivalents: [GeoscienceAustralia/MPM-WofE](https://github.com/GeoscienceAustralia/MPM-WofE) (R, Apache-2.0) and [GeoscienceAustralia/minpot-toolkit](https://github.com/GeoscienceAustralia/minpot-toolkit) (archived Oct 2025).

## Petrology deep dive (PhaseCast review)

Reviewed by a dedicated Sonnet 5.5 subagent, 2026-11-25. All URLs fetch-verified (5/5 HTTP 200).

**Classification: Interpretation B.** PhaseCast is a latent-space ML model — a pretrained transformer encoder with learned heads. It involves no hypervector algebra (not A), and its input is a flat vector of oxides and trace elements with no spatial or n-D structure (not C).

**Paper:** "Simulated petrological labels enable probabilistic mineralogy prediction from whole-rock geochemistry" (Liu, Kaplan, Whittaker, Persson; LBNL; [arXiv:2610.36429](https://arxiv.org/abs/2610.36429), v2 of 30 Oct 2026). NeurIPS 2026 Sim2Science workshop poster ([OpenReview](https://openreview.net/forum?id=XH2fnz0Enx)).

**Architecture and dimensionality.**
- **Encoder:** an adapted CrabNet. "Each element is one token; self-attention across tokens and a masked mean pool yield one latent vector per rock."
- **Size:** d_model = 256 ("Dimensionality of latent representation"), 4 layers, 8 heads; 3,234,699 trainable parameters — a small model.
- **Element embeddings:** a 121×200 table initialised from the published 200-dimensional mat2vec embeddings, left trainable.
- **Input:** 9 major and 13 trace elements plus an Fe3+/total-Fe row — a 23-token sequence.
- **Pretraining:** masked-element modeling on 787,721 measured whole-rock compositions (Gard et al. 2019 global compilation). Median log-space R² of 0.89 (major) and 0.84 (trace) when imputing a hidden element from the frozen latent.
- **Heads (MLPs on the frozen latent):** a Bernoulli presence factor over 21 phases × a Dirichlet abundance factor (assemblage head); a per-mineral oxide composition head; a P/T/water conditions head. Recalibration is an affine map on presence logits plus multiplicative rescaling of Dirichlet concentrations.

The high-dimensional element is modest: a 256-d latent and a 2^21 assemblage space.

**Simulated-label pipeline.**
- **Engine:** MAGEMin, a Gibbs-energy minimizer, run unmodified through its Julia interface — not MELTS, Perple_X, or Thermo-Calc (cited only as alternatives). The paper notes MAGEMin is "fast enough to sweep candidate conditions."
- **Compositions:** 9,946 held-out measured volcanic compositions (SiO2 ≤ 80 wt%, MgO ≤ 18 wt%, foidites excluded).
- **Draws:** 48 sampled (pressure, dissolved-water) draws per composition, each cooled 1200 → 600 °C in 20 °C steps.
- **Labels:** assemblage recorded at 50 and 30 wt% residual melt, melt/fluid removed, solids renormalised — about 950k labels. Cost: ~62 h CPU on an M4 Max for the training split.

**Zero-shot claims and baselines.**
- **Benchmark:** 640 USGS volcanic rocks (Bodie Hills; Tonopah/Divide/Goldfield), 7 mineral categories, splits 368/111/161.
- **Presence discrimination:** AUROC 0.575–0.870 across categories (amphibole lowest; no median stated).
- **Abundance:** Spearman positive in 6 of 7 categories; zero-shot abundance error 11.0% → 9.5% recalibrated.
- **Joint NLL:** validation 13.4 → 0.97 nats with the full fitting set; a 25-rock fit gives 3.97 nats (76% of the reduction). Test set: 9.36 → 1.58 nats with a 25-rock fit.
- **Baseline:** internal only — the same head on the pretrained latent beats the head on raw geochemistry by 0.50–0.67 nats. The paper's own limitations section says "no external method is evaluated." Caveats: absolute errors are teacher-forced; the benchmark records phenocryst modes while labels are equilibrium solids; the abundance factor appears learned from minerals present rather than chemistry.
- **"Zero-shot" is a narrow claim:** it means "no measured mineralogy used in head training" — not a claim to beat norm calculators or other methods.

**Code status as of 2026-11-25: RELEASED** — supersedes the scan's "paper-only" status. The code is at [github.com/matthew-j-liu/phasecast](https://github.com/matthew-j-liu/phasecast) (MIT, created 2026-05-13, last push 2026-11-06, 8 stars), with a linked Zenodo DOI (10.5281/zenodo.23992950). The repo includes checkpoints, configs, src, tests, and MAGEMin scripts. The `submission` branch reproduces the paper; `main` holds later work whose results differ.

**Other petrology high-dimensional work: none beyond PhaseCast.** Empty searches: "foundation model OR self-supervised embedding mineral chemistry OR petrology OR thermobarometry transformer 2026"; "arXiv 2026 pretrained transformer whole-rock geochemistry embeddings petrology masked element modeling". Adjacent items that surfaced (neither is petrology geochemistry):
- **PetroMind** (Chen et al., Appl. Comput. Geosci. 2026, [doi:10.1016/j.acags.2025.100314](https://doi.org/10.1016/j.acags.2025.100314)) — multimodal petrographic model for rock-image classification/description (thin-section imagery, not geochemistry; unverified).
- **Parsa et al.**, "Large Language Models and Geoscience Transformers for Predictive Mapping of Canadian Critical Minerals", Nat. Resour. Res. 2026 ([link](https://link.springer.com/article/10.1007/s11053-025-10564-0)) — 768-d BERT embeddings per H3 cell for prospectivity (exploration, not petrology).
- The mineral-exploration foundation-model survey ([preprints.org/manuscript/202607.2303](https://www.preprints.org/manuscript/202607.2303)) — useful pointer for the exploration section.

**Thermobar / MIN-ML classification:**
- [Thermobar](https://github.com/PennyWieser/Thermobar) — **classical.** Calibrated thermobarometry/hygrometry equations; its ML thermobarometers use Petrelli's tree-based regressors ([PMC9285709](https://pmc.ncbi.nlm.nih.gov/articles/PMC9285709/)). No latent or embedding component.
- [MIN-ML](https://ui.adsabs.harvard.edu/abs/2023EGUGA..2513612S/abstract) — **classical.** Supervised classifier of igneous minerals from oxide data, no learned representation.

**Verdict on petrology density:** stays **thin-to-moderate, leaning thin.** PhaseCast is the only latent-space petrology model found (one 3.2M-parameter, 256-d, workshop-level paper) with no external baseline. Only its code-availability status changes: paper-only → MIT-licensed code and checkpoints released.

## Per-domain coverage

| Domain | Density | Best public artifacts |
|---|---|---|
| Economic geology / MPM | **Densest** | AlphaEarth-prospectivity, GeoMinLM, DeepAndes, OpenGADBench, DEEP-SEAM, Parsa et al., Geo-Hgan, causal-VAE |
| Geochemistry | Dense | GeoChemAD/GeoChemFormer, MAX, graph-SSL, DAN-GRF, pyrolite (classical CoDA) |
| Mining exploration | Dense (shared with MPM) | DeepAndes, geopredict, critical-mineral-ml, JiuZhou, MetalGPT-1, PEACE |
| Petrology | Thin–moderate, leaning thin | PhaseCast (code released, MIT); PetroMind (imagery-only); Thermobar/MIN-ML are classical-ML |
| Geostratigraphy | **Thinnest** | GeoVectoLitho (the one strong public-code effort) |

## Flagships

1. **GeoChemAD / OpenGADBench** — first open multi-region geochemical anomaly benchmark + self-supervised transformer; directly attacks the field's private-data reproducibility crisis.
2. **GeoGalactica + K2** — the two named open geoscience foundation LLMs that the exploration-LLM line (GeoMinLM etc.) builds on.
3. **AlphaEarth Foundations** — the highest-profile embedding model actually applied to mineral prospectivity at industrial scale.

## Checks & audit trail

- Worker checks: 3/3 PASS (URL-per-entry, URL count ≥ project count, ≥2 fetch-verified each)
- Centralized compile check: 10/10 key URLs spot-verified HTTP 200
- Petrology deep dive (Sonnet 5.5): 5/5 URLs fetch-verified; 3 predictions logged (1 hit, 2 misses — code-release miss corrected the report)
- Loose-ends pass (2 workers): all checks PASS (10 distinct URLs verified by glm-literature; 3 primary URLs verified by ds-skeptic, with preprints.org bot-blocked at 403 and existence confirmed via DOI/MCML); 4 predictions logged (3 hits, 1 miss)
- Predictions logged: 18 total across the run → ledger at `~/Documents/repos/abdopus-cpi/ledger/octopus-ledger.jsonl`
- Gate: no director review needed at any pass (full agreement, all checks green); director's independent findings fully consistent with worker reports

## Bottom line

If "hyper-dimensional models" means HDC/VSA — the field is empty, and the adjacent HDC work (hyperspectral, wildfire, DoA) plus the mislabel/paper-mill noise explains every hit. If it means high-dimensional latent ML — the field is active and consolidating around foundation models, with mineral prospectivity the densest domain and geostratigraphy the clearest open niche.
