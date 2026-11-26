# Research Notes — Index

Start here. Every research run in this repo lands in `reports/` with a date-stamped filename; this index lists them newest-first with one-line verdicts. Full run-by-run status log lives in the repo root `README.md`.

## Reports (newest first)

| Date | Report | Verdict in one line |
|---|---|---|
| 2026-11-26 | [phasecast-self-correcting-loop-2026-11-26.md](../reports/phasecast-self-correcting-loop-2026-11-26.md) | **Interim (run cut short):** loop buildable this week — register → tester → score → dated corrections; PhaseCast-vs-MAGEMin agreement is *teacher-agreement, not accuracy* (top poison risk); glm-literature round cancelled, brief preserved in appendix for re-dispatch |
| 2026-11-25 | [trap-falls-montana-claim-2026-11-25.md](../reports/trap-falls-montana-claim-2026-11-25.md) | "Trap Falls ≈ Montana formation" FALSIFIED — unsourced/misremembered; Trap Falls (CT, Ordovician Hartland Group) is its own best-studied analogue (McDaniel 1997) |
| 2026-11-25 | [nure-w-anomaly-map-2026-11-25.md](../reports/nure-w-anomaly-map-2026-11-25.md) | Old Mine Park does NOT stand out — CT NURE W is 95.5% below detection, the map maps the detection limit; Be is the only defensible near-park signal |
| 2026-11-25 | [petdb-regional-analogues-2026-11-25.md](../reports/petdb-regional-analogues-2026-11-25.md) | PARTIAL — 418 analyses in the Trumbull bbox, 55 PhaseCast-contract-ready, but all CAMP tholeiites; zero target-unit hits; pipeline-validation use only |
| 2026-11-25 | [llm-cluster-local-play-candidates-2026-11-25.md](../reports/llm-cluster-local-play-candidates-2026-11-25.md) | All six domain LLMs killed for the local play — use a general open instruction-tuned LLM as Stage-2 orchestrator; GeoVec verified but is a research artifact |
| 2026-11-25 | [local-play-anomaly-candidates-2026-11-25.md](../reports/local-play-anomaly-candidates-2026-11-25.md) | OpenGADBench classic baselines win for the NURE anomaly map (point-CSV contract match, label-free, MIT); PyKrige runner-up; five others blocked with reasons |
| 2026-11-25 | [geogalactica-as-data-source-2026-11-25.md](../reports/geogalactica-as-data-source-2026-11-25.md) | GeoGalactica's 65B-token corpus is NOT open and never will be; K2's likewise; best open geoscience text corpus = GeoGPT collection (Zhejiang Lab) |
| 2026-11-25 | [oldmine-phasecast-play-2026-11-25.md](../reports/oldmine-phasecast-play-2026-11-25.md) | PhaseCast runnable today (~15 ms/rock, CPU); input contract verbatim; OOD limits mapped; local data = 1970s USGS semi-quant only; stack: pyrolite → PhaseCast → MAGEMin → OpenGADBench |
| 2026-11-25 | [old-mine-park-trumbull-2026-11-25.md](../reports/old-mine-park-trumbull-2026-11-25.md) | "Decayed volcano root" is a simplification — exhumed ~28 km metamorphosed arc-related sequence; guidebook = CGNHS No. 11 (2022); collecting suspended since 2016 |
| 2026-11-25 | [geogalactica-phasecast-together-2026-11-25.md](../reports/geogalactica-phasecast-together-2026-11-25.md) | Novel pairing as of 2026-11-25: ChemCrow-style tool-calling with structured grounding; GeoGalactica contributes the idea, never the component |
| 2026-11-25 | [phasecast-applications-2026-11-25.md](../reports/phasecast-applications-2026-11-25.md) | PhaseCast is real and runnable, weights in git, zero third-party adoption; honest self-disclosed limitations; workshop (non-archival) paper |
| 2026-11-25 | [geogalactica-applications-2026-11-25.md](../reports/geogalactica-applications-2026-11-25.md) | GeoGalactica is a dormant artifact — gated weights, documented prompt failures, no downstream users; prior "Live" label downgraded |
| 2026-11-25 | [hd-geoscience-scan-2026-11-25.md](../reports/hd-geoscience-scan-2026-11-25.md) | "Hyper-dimensional" = three readings: HDC/VSA zero in-domain (paper-mill noise); high-dim latent ML is the real activity; literal n-D spatial simulation thin. Petrology thin-to-moderate, PhaseCast the sole latent-space project |

## HTML versions

- [hd-geoscience-scan-2026-11-25.html](../reports/hd-geoscience-scan-2026-11-25.html) — landscape scan, styled
- [oldmine-phasecast-play.html](../pages/oldmine-phasecast-play.html) — PhaseCast-on-local-rocks practical guide + the igneous-equivalent-of-protolith theory ([published page](https://app.superset.sh/page/old-mine-park-phasecast-the-local-play-in-practice-h42vn0))

## Data on disk

- `data/BronsonHill_WR_data.csv` — Valley et al. USGS release (doi:10.5066/P9W03VWZ), 94 whole-rock analyses, 12 mafic Waits River samples PhaseCast-ready (the protolith-analogue dataset)
- `data/nure-ct/` — CT NURE stream-sediment build (clean + scoring CSVs, build scripts, NGDB W sites)

## How reports are produced

Multi-angle research runs use the abdopus orchestration pattern: 3–4 blind diverse workers in parallel, deterministic checks per worker, a disagreement gate (τ=0.3), director rulings, and falsifiable predictions logged to a calibration ledger. Conventions: verdict first, every non-common-knowledge claim carries a fetch-verified URL, negative results recorded with evidence. See root `AGENTS.md` for the binding rulings.
