# PhaseCast Self-Correcting Loop: Interim Design (run cut short)

**Date:** 2026-11-26 · **Run:** abdopus `phasecast-self-correcting-loop` (design task; 4 agents dispatched: ds-builder@1, glm-literature@1, haiku-user@1, director@1 — all blind to each other)
**Status:** **CUT SHORT by user after wave 1.** ds-builder, haiku-user, and the director completed; **glm-literature was cancelled mid-run** — its brief is preserved verbatim in the Appendix for re-dispatch. The disagreement gate could not be computed (a three-worker design fan-out needs three worker reports). This report compiles what finished; nothing here is a settled verdict until the literature worker's round lands and the gate runs.

## Verdict (interim, director-anchored)

**The loop is buildable this week and the design converged harder than expected.** All three finishing agents independently arrived at the same skeleton — append-only JSONL prediction register → named tester per projection class → scripted scoring → dated corrections, never silent model edits — and the same top poison family: anything that lets a wrong projection score as right. The director's binding addition, which no worker surfaced: **PhaseCast was trained on MAGEMin-simulated labels, so PhaseCast-vs-MAGEMin agreement is teacher-agreement (distillation fidelity), not accuracy about rocks.** That agreement is cheap, will score high, and will dominate the register unless labelled. The single most dangerous poison risk is reading it as validation.

## The design, compiled

### The loop (converged across ds-builder + director)

```
ENTRY (OOD gate) → PROJECTION (register entry) → TEST (named tester) → SCORE (script) → UPDATE (calibration.json)
```

- **Entry condition:** ≥7 of 9 majors, unrenormalized; provenance tag (`analogue:` / `synthetic:` / `park:`); declared class (`protolith-igneous-equivalent` vs `metamorphic-equilibrium`); OOD gate verdict `trusted` / `borderline` / `untrusted` (envelope: SiO₂ ≤ 80, MgO ≤ 18, sum ≥ 90 + immobile-basaltic ratios). `untrusted` still runs, stamped hypothetical-only.
- **Register:** append-only `register/predictions.jsonl`; every entry carries input hash, PhaseCast commit SHA, MAGEMin db version, provenance. Resolutions never edit claims — a separate resolutions file (director) or new entries (ds-builder) keyed by projection id.
- **Update:** `calibration.json` recomputed from the register, never hand-edited. Corrections are dated rubric or input-rule changes, never silent model changes. No retraining inside the loop.

### Projection classes and testers

| Class | Claim | Tester | Scoring rule |
|---|---|---|---|
| A. Mineral assemblage (igneous equivalent) | top-1/top-2 group + share (7 scored groups) | MAGEMin Metabasite (Green 2016) at stated P–T, same input | top-1 group maps to phase ≥5 vol%; score = 1−\|share diff\|; **label: teacher-agreement, not accuracy** (director ruling) |
| B. Protolith classification | basalt … rhyolite | pyrolite immobile discrimination (Zr/Ti vs Nb/Y; Ti vs V) | categorical agree/disagree; boundary-within-error = unresolvable, not right |
| C. Metamorphic assemblage (MAGEMin at 8 kbar / 650 °C) | amphibole/plagioclase/garnet presence | **field observation log** (hand lens, photos — no collecting) | presence/absence Brier; non-observation counts only on a logged fresh inspection |
| D. OOD flag itself | trust level | disagreement between A's student and teacher | AUROC of OOD score vs A-class error — scores whether the model knows when it is wrong |

Class C is the director's structural point: field observations test **MAGEMin's** metamorphic claims, never PhaseCast's (binding igneous-equivalent ruling). Garnet/epidote register as NOT SCOREABLE (outside the 7 groups); scheelite/powellite are invisible — no projection, ever.

### First cycle (ds-builder, runnable this week)

Seven scripts in `loop/` against `data/BronsonHill_WR_data.csv`: `prep_bronsonhill.py` (map `Fe2O3→fe2o3_tot`, traces as `<sym>_ppm`, blanks stay blank, **hard-assert no renormalization**) → `run_phasecast.py` (pinned `submission` commit) → `gate.py` → `project.py` → `score_magemin.py` (Julia `MAGEMin_C.jl`, Metabasite Green 2016, 8 kbar / 650 °C) → `score_immobile.py` (pyrolite) → `score.py` (writes scores + first `calibration.json`).

**Data note (ds-builder, verified against the CSV):** a broad mafic filter yields **12 mafic Waits River samples** (SiO₂ 43.9–52.5, complete immobile suite), not the 8 in the prior memory note — a filter-definition difference, not a data error. First cycle runs on 12. All 13 PhaseCast traces present except Rb blank on BF325/HA30 (correct blank encoding). Cr is ppm-only and dropped (contract ignores `cr2o3`).

### Safe vs poison sacrifices (haiku-user table, director-confirmed)

**SAFE** (adds noise, scoring stays honest): regional analogues for park rocks *if provenance-stamped and never cited as park support*; volcanic-only heads on amphibolites *if registered as igneous-equivalent*; single P–T point; missing traces left blank; coarse 7-group mapping; few resolutions → wide intervals; garnet/epidote left unscored.

**POISON** (wrong projections score as right): zero-filling or imputing blanks; renormalizing to 100%; the 1970s USGS semi-quant data as park input (lacks majors — any filled version is invented); calling teacher-agreement "validation"; scoring garnet/epidote/scheelite; "consistent with" as a verdict; choosing the scored rank or moving the threshold after seeing results; thinning the register to raise the hit rate; pooling synthetic perturbations with real analogues in a headline score.

**Solo-loop guards (haiku-user):** cap open predictions at 10 (hit cap → next session is scoring-only); frozen rubric file, dated amendments only; SHA + input-hash health check opens every session; 20-minute minimum week; skipped weeks logged, not hidden; corrections require a threshold count of scored predictions in the same class.

**Minimum viable first month:** ≥10 projections registered, ≥6 scored (rest NOT SCOREABLE with reason, not open), ≥2 classes covered, ≥1 dated correction applied, ≥2 poisons logged as rejected, 4 README status lines, no open prediction >14 days old.

## Director's ranked first three moves

1. **PhaseCast + MAGEMin (igneous P–T, Green 2016) on the 12 BronsonHill mafics** — register class A and D rows *before* looking at MAGEMin output. ~1 hour. Creates the register and the first teacher-agreement scores.
2. **pyrolite immobile classification on the same 12 (class B)** — the first scorer independent of the teacher.
3. **MAGEMin at 8 kbar / 650 °C for class C claims + one observation-only park visit** logging amphibolite assemblage presence/absence — the first real-world resolution.

## Predictions

**Director worker predictions (scored against actual reports):**

| # | Prediction | Outcome |
|---|---|---|
| 1 | ds-builder will miss the distillation-circularity poison and present MAGEMin agreement as validation | **HIT** — called MAGEMin "ground truth"/"reference tier"; never flagged that PhaseCast was trained on MAGEMin labels |
| 2 | ds-builder will propose a single headline metric without provenance stratification | **MISS** — per-class scores, `source=analogue` stamped (though scores are not stratified by provenance either) |
| 3 | glm-literature will make ≥1 unqualified conformal-coverage claim | **UNRESOLVED** — worker cancelled |
| 4 | haiku-user gets renormalization/blank-filling poison + observation-only + weekly rhythm right | **HIT** |
| 5 | haiku-user will under-specify scoring (no Brier/log-score) | **HIT** — binary pre-registered observables, no proper scoring rules |
| 6 | haiku-user's top poison ≠ teacher-circularity | **HIT** — top poisons: "consistent with" scoring, post-hoc threshold change; caught agreement≠validation labeling but not the training-label circularity |
| 7 | Cross-worker: at most one of three names teacher-agreement circularity explicitly | **HIT** — zero did |

**Design predictions (on file, unscored — first cycle not yet run):**

- Director: PhaseCast top-posterior presence calls agree with MAGEMin on ≥80% of group×sample cells (falsified <70%) — the distillation effect, which is exactly why class A must be labelled teacher-agreement.
- Director: class D AUROC ≤ 0.7 (weak OOD discrimination); largest student-teacher disagreement on the low-SiO₂ (~43.9) end.
- Director: MAGEMin metabasite at 8 kbar / 650 °C returns amphibole + plagioclase in all samples; garnet in ≥3.
- ds-builder: amphibole ≥30 vol% AND plagioclase ≥20 vol% for ≥10 of 12; ≥10 of 12 pass `check_input` with zero errors; top-1 group in MAGEMin ≥5 vol% for ≥8 of 12; pyrolite classifies ≥10 of 12 as basalt/basaltic-andesite; gate marks ≥10 of 12 trusted/borderline.
- haiku-user: observation-only tests score ≥2 distinct projection classes by day 30; ≥1 day-30 correction is a rubric/input-rule change, not a model change.

## Open question (one)

The literature round is missing: conformal-prediction / prediction-register precedents, the exchangeability caveat for analogue-to-park transfer, and the data-acquisition ladder (certified lab pricing, pXRF, museum specimens). Re-dispatch the preserved brief below before treating any coverage or cost claim as settled.

## Check result

**PASS (interim).** Deterministic checks: this report contains the required sections (verdict, design, predictions, open question, check result), the cancelled worker's brief verbatim in the Appendix, and ≥5 falsifiable predictions with thresholds. Gate: **not computed** — one of three workers cancelled; per the escalation ladder the missing round is a retry-with-same-brief, not a re-design. All claims above trace to the three completed agent reports; no fetch-verified URLs were produced this run (design task, local data only).

## Appendix: preserved brief for the cancelled glm-literature worker (re-dispatch verbatim)

> Task: Ground the design of a self-correcting PhaseCast projection loop in established literature and method precedents — what fields already solve "cheap falsifiable projections now, rapid correction as tests come in," and what data-acquisition routes could grow the ground truth.
>
> Task type: design
> Worker: glm-literature@1 (model family: zai, lens: literature-first)
> Role: multi-step design worker
>
> CONTEXT (settled project facts — do not re-verify):
> - Project Lithos, local case study: Old Mine Park, Trumbull CT. Rocks: The Straits Schist amphibolites (metabasalt protolith), marbles, quartzite; Permian scheelite skarn overprint tied to the Pinewood Adamellite (291±4 Ma). Acadian burial ~28 km, >650 °C at ~8 kbar. Collecting suspended since 2016 — observation only.
> - PhaseCast (github.com/matthew-j-liu/phasecast, MIT): whole-rock composition → posterior over mineralogy + formation conditions. Encoder pretrained on 787k all-rock compositions; mineralogy heads trained on VOLCANIC-only MAGEMin-simulated labels. CPU inference ~15 ms/rock. Input: 9 majors + 13 traces (Sr Zr Ba Y Rb Ni Nb V La Ce Nd Yb Th) + optional Fe³⁺/FeT; blanks = not measured; never renormalize.
> - Known limits: plutonic zero-shot +2.80 nats vs +10.63 volcanic; metamorphic-drift regime below wet solidus; garnet/epidote in vocab but never scored; scheelite/powellite absent; no external baselines in the paper.
> - BINDING ruling: PhaseCast output on local rocks = hypothetical igneous equivalent of the protolith, never actual mineralogy. Metasomatism → interpret via immobile elements (Ti, Zr, Nb, Y, REE).
> - Local data: NO modern whole-rock analyses of park rocks publicly exist. 1970s USGS NGDB semi-quant lacks full majors. Regional analogue data on disk: data/BronsonHill_WR_data.csv (94 samples, 8 mafic, full majors + traces). PetDB regional query returned only CAMP tholeiites. NURE CT W 95.5% below detection.
> - Tools runnable: PhaseCast, pyrolite, MAGEMin (Julia; Metabasite/Metapelite DBs), OpenGADBench/GeoChemAD. Thermobar blocked (needs EPMA).
> - You may read repo reports: reports/oldmine-phasecast-play-2026-11-25.md, reports/phasecast-applications-2026-11-25.md, reports/old-mine-park-trumbull-2026-11-25.md.
>
> THE DESIGN QUESTION: The user accepts sacrificing fidelity NOW for a DURABLE PROCESS that rapidly corrects as its projections are tested. Your lens is LITERATURE-FIRST: find the established methods and precedents that this loop should borrow rather than invent. Angles worth covering: (a) calibration under distribution shift — conformal prediction, post-hoc recalibration, quantile regression as ways to get honest uncertainty from a mis-specified model; (b) prediction registers / registered reports / forecasting tournaments as the durable-artifact pattern for falsifiable projections with scored outcomes; (c) sequential/Bayesian updating and teacher-student consistency checking as correction mechanics; (d) data acquisition routes that grow ground truth for a solo researcher — certified commercial whole-rock analyses (ALS/Actlabs price tiers), portable XRF constraints, published XRD modes in theses/survey bulletins, museum/university specimen collections (Yale Peabody holds Trumbull specimens); (e) any published geoscience example of a ML predictor whose outputs were systematically tested against later ground truth. Use webfetch on primary sources (arXiv, OpenAlex API, journal pages, lab price pages). The websearch tool is dead in this environment — fetch directly. A publisher 403 means bot-blocking, not a dead link.
>
> Deliverables (3-6, numbered):
> 1. The 3-5 strongest method precedents for "honest uncertainty from a mis-specified predictor," each with a fetch-verified source and a one-line verdict on fit to PhaseCast's posterior.
> 2. The prediction-register precedent: the best established pattern for dated, falsifiable, scored projections (registered reports, forecasting tournaments, or similar), with source, and what to copy.
> 3. The data-acquisition ladder: ranked routes to grow local ground truth over time, with cost/feasibility notes (commercial lab certified whole-rock, pXRF, XRD from literature, museum specimens), each fetch-verified where a price page or catalog exists.
> 4. Any published geoscience ML-tested-against-ground-truth loop found, or a verified statement that none exists.
> 5. Which borrowed method to adopt FIRST, and why it survives the solo-researcher constraint (laptop, no collecting, small budget).
>
> Do NOT redo: the igneous-equivalent theory (settled); PhaseCast input contract (settled); PhaseCast adoption/reproducibility stats (settled); local geology history (settled); the NURE/PetDB/GEOROC data-portal status (settled).
>
> Deterministic check (run before reporting; retry up to 2x locally): your final report contains the exact headings "## Findings", "## Design", "## Predictions", "## Check result"; at least 5 fetch-verified URLs appear in a Sources list; at least 3 numbered falsifiable predictions. Verify by inspecting your own output before submitting.
>
> Predictions (falsifiable, ≥3): e.g., "conformal prediction has been applied to geochemical regression in ≥1 published paper", "a certified 9-major+13-trace whole-rock package costs under $100/sample at a commercial lab in 2026".
>
> Open question (max 1, optional).
>
> Report format: exactly these top-level sections in order: ## Findings, ## Design (the deliverables above), ## Predictions (numbered), ## Check result, ## Sources (fetch-verified URLs). Return the report as your final response text. Do NOT write any files.

*Re-dispatch note: the brief's "8 mafic" line reflects the pre-run count; ds-builder's direct CSV inspection found 12 under a broad mafic filter. Update that line to 12 (or "8–12 depending on filter") when re-dispatching. The director additionally requires the literature worker to address the exchangeability caveat: analogue-to-park transfer breaks conformal coverage guarantees, so any coverage claim must carry the covariate-shift caveat (weighted conformal, Tibshirani et al. 2019, is the relevant reference).*
