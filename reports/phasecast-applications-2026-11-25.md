# PhaseCast: Applications and Demonstrations

**Date:** 2026-11-25 · **Run:** abdopus `phasecast-apps` (3 agents: glm-literature@1, ds-skeptic@1, director@1 — all blind to each other)
**Gate:** disagreement d ≈ 0.05 (< τ=0.3), all deterministic checks passed (14 + 24 + 12 verified URLs, 0 cited-source failures) → director review skipped, compiled from converging worker reports + director's independent findings.

## Verdict

**PhaseCast is a real, runnable, unusually well-documented research artifact with zero adoption beyond its author.** Weights are downloadable (committed in git), the corpus is open on Zenodo, and the tutorial notebook is the de facto demo — but there are no third-party applications, forks, PRs, issues, or citations. The paper is a non-archival, reciprocal-reviewed NeurIPS Sim2Science workshop contribution that explicitly evaluates no external method. The "usable project" picture is real at the code level and empty at the adoption level — which is expected for a 4-week-old paper.

## Findings

### 1. Popular applications

**None exist.** Verified negative evidence:

- GitHub-wide search for "phasecast" returns exactly 2 repos: the original ([matthew-j-liu/phasecast](https://github.com/matthew-j-liu/phasecast)) and an unrelated [PHASECAST-MURO](https://github.com/alejandromuro2000-wq/PHASECAST-MURO) (resident space-object forecasting, different author, no code). **Zero forks** of the original.
- No HuggingFace model or dataset ([API search empty](https://huggingface.co/api/models?search=phasecast)); no HF papers page (404 — verified absence).
- All 95 issues and all 194 issue comments are authored by `matthew-j-liu` (28 open / 67 closed) — self-tracked research TODOs, zero third-party participation. 0 PRs.
- Citations: **OpenAlex cited_by_count = 0** ([W7224084396](https://openalex.org/W7224084396)); Crossref shows no citing works; Semantic Scholar rate-limited (429) but OpenAlex + Crossref agree on zero.
- Third-party "mentions" are all auto-generated aggregators: a [mining-eng.ir catalog page](https://www.mining-eng.ir/mining-github/matthew-j-liu-phasecast/?lang=en) (machine digest, 0 comments), a [ModelScope paper page](https://www.modelscope.cn/papers/2610.36429) (22 views, 0 comments), [alphaXiv](https://www.alphaxiv.org/abs/2610.36429) (33 views, no discussion), ResearchGate indexing (403 to fetch — unverified). None constitute use.

### 2. Demonstration projects

All demonstrations are **author's own**:

- **[docs/tutorial/](https://github.com/matthew-j-liu/phasecast/tree/main/docs/tutorial)** (added 2026-10-30): `inference.ipynb` with committed outputs — composition table in, per-rock posterior over mineralogy and formation conditions out, ~15 ms/rock on laptop CPU, no Julia/MAGEMin needed. The tutorial README calls this "the handoff for building a web app or a local tool."
- **[sim2sci-camera-ready release](https://github.com/matthew-j-liu/phasecast/releases)** (2026-10-21): code, checkpoints, benchmark tables, and figure inputs reproducing the paper. The README warns that `main` contains later research whose numbers differ from the paper — paper results reproduce only from the `submission` branch / release.
- **[Zenodo corpus release](https://zenodo.org/records/23992951)** (2026-11-06, CC BY 4.0): 1.26 GB simulated corpus + 787,721-row pretraining set. 47 downloads, 32 views as of 2026-11-25.
- **A planned web app that does not exist.** The tutorial says "the app code lives in its own repository," but the author has only 3 public repos (phasecast, AMBER-ff, personal site) — no app repo. The stable inference API is an open self-authored issue (#70). Treat the app as planned, not shipped.

### 3. Adoption signals

| Signal | Value |
|---|---|
| GitHub | 8 stars, 0 forks, 0 watchers, 480 commits (all solo), created 2026-05-13, last push 2026-11-06 |
| Issues/PRs | 95 issues — 100% self-authored; 0 PRs; 0 third-party comments |
| Citations | 0 (OpenAlex + Crossref) |
| Zenodo | 47 downloads, 32 views (2026-11-25) |
| CI | 1 workflow, 26 runs, latest success (2026-11-06) |

Context for the adoption numbers: the paper is 4 weeks old (arXiv v1 2026-10-27), and the author has [left LBNL for a stealth SF startup](https://matthew-j-liu.github.io/) (site created 2026-11-11) — a factor in whether the promised app and stable API ever materialize.

### 4. Weights and reproducibility

- **Weights are downloadable, tracked directly in git** (not HuggingFace, not LFS pointers — real blobs verified via GitHub contents API):
  - `checkpoints/pretrain_allrock_redox_seed0/epoch_best.pt` — 45,965,051 bytes (~44 MB, includes optimizer state)
  - `checkpoints/joint_heads_allrock_tuned_seed0/heads_best.pt` — 7,341,045 bytes (~7 MB)
- A user can run inference immediately with zero training; only regenerating the corpus needs Julia + MAGEMin.
- **Parameter-count discrepancy:** the tutorial puts the whole model at ~5M parameters; the prior scan's "~3.2M" likely counts only the encoder. Flagged for correction in future citations.
- **Corpus math verified internally consistent:** 9,946 train compositions × 48 draws × 2 readout rungs = 949,228 train labels + 125,105 valtest ≈ 1.07M ("nearly one million" reconciles).

### 5. Honest limitations (primary sources)

- **Workshop status:** NeurIPS Sim2Science 2026 (Paris, Dec 12) is **non-archival** ("no formal proceedings") with **reciprocal reviewing** (each paper nominates one author to review 2 others) — light-touch review by design, per the [official CFP](https://www.sim2science.com/cfp.html). PhaseCast was accepted ([OpenReview Submission 45](https://api2.openreview.net/notes/search?term=mineralogy&content=all&group=NeurIPS.cc/2026/Workshop/Sim2Sci)).
- **No external baseline — the paper admits it verbatim**: "no external method is evaluated." No XGBoost, no classical thermobarometry, no CIPW-norm comparison. The author's own issue tracker confirms: #95 "Baseline scoreboard… against simple baselines" and #19 (PCA/PPPC baseline) both still open.
- **Simulated-label risks, self-disclosed:** predicted abundances are "systematically offset from measured values" without recalibration (README); the recalibrator is a research tool excluded from the planned app; issue #74 says corpus scaling fails on real rocks; issue #57 notes simulated labels and measured benchmark may not describe the same crystal content for silica-rich rocks; almost no signal on the plutonic benchmark (commit 2026-10-05).
- **Narrow scope:** trained on volcanic compositions only (#91); benchmarked only on USGS data (Bodie Hills volcanic; du Bray plutonic); predicts 7 coarse mineral groups; redox input unused ("reserved for a future retrain").
- **Notable honesty:** the paper and repo disclose their own weaknesses (systematic abundance bias, teacher-forced errors, shared validation set, main-branch drift from paper numbers). This is a well-scoped workshop contribution presented as exactly that — not a paper-mill overclaim.

### 6. Adjacent ecosystem (what a user would combine it with)

- [MAGEMin](https://doi.org/10.1029/2022GC010427) (Riel et al. 2022) — the Gibbs-energy minimizer that generated the labels; needed only for retraining, not inference.
- [Gard, Hasterok & Halpin 2019](https://doi.org/10.5194/essd-11-1553-2019) whole-rock compilation — the pretraining data source.
- The tutorial documents parsing commercial lab exports (ALS, Actlabs certificates) into the model's CSV input contract — the practical bridge from geochemistry databases to PhaseCast.
- No integration exists yet with thermobarometry tools (Thermobar) or GEOROC/PetDB pipelines.

## Predictions

Stated before searching, scored at compile:

| # | Prediction (worker) | Outcome |
|---|---|---|
| 1 | glm-literature: ≥1 citation or third-party mention beyond the paper | **PARTIAL** — 0 citations; mentions are auto-generated aggregators only |
| 2 | glm-literature: repo activity beyond initial release | **CONFIRMED** — 30+ post-release commits, but all solo |
| 3 | glm-literature: no third-party application/fine-tune yet | **CONFIRMED** |
| 4 | ds-skeptic: repo <5 stars and no third-party issues/PRs | **FAIL on stars** (8 ≥ 5); second half true — conjunction fails |
| 5 | ds-skeptic: no citations beyond original paper | **CONFIRMED** — 0 across OpenAlex/Crossref |
| 6 | ds-skeptic: weights NOT downloadable (code-only) | **FAIL** — both checkpoints committed in git; corpus open on Zenodo |

Director predictions (scored against workers): "both agree weights downloadable; at least one will miss git-tracking or claim HF hosting" — half-hit (both agreed downloadable, both correctly said git-not-HF); "at least one worker will overstate adoption" — miss (neither did); "both report zero third-party apps and zero citations; at least one won't notice the missing-baseline admission" — hit on the first, miss on the second (both found #95/the verbatim admission); "at least one will repeat ~3.2M params without flagging the tutorial's ~5M" — hit (neither worker flagged it; only the director did).

## Check result

- **Verified URLs cited as fact: 50 total** (glm-literature 14, ds-skeptic 24, director 12; heavy overlap on core primary sources). 0 dead links among cited sources.
- Unverifiable items (ResearchGate 403, OpenReview bot-check, Semantic Scholar 429, Zenodo concept-DOI timeout) were quarantined under "Unverified links" by each agent and are not cited as fact; alternates were verified instead.
- Gate: d ≈ 0.05 < τ=0.3, all checks passed → compiled without director review. Zenodo counter drift (46 vs 47 downloads) is a live counter, not a disagreement.

## Sources (core, verified live 2026-11-25)

- https://github.com/matthew-j-liu/phasecast (repo, issues, pulls, releases, CI, contributors)
- https://api.github.com/repos/matthew-j-liu/phasecast (stars/forks/license/dates)
- https://arxiv.org/abs/2610.36429 · https://arxiv.org/html/2610.36429v2
- https://zenodo.org/records/23992951 (corpus, CC BY 4.0, download counts)
- https://openalex.org/W7224084396 (cited_by_count = 0)
- https://www.sim2science.com/cfp.html (non-archival, reciprocal review)
- https://matthew-j-liu.github.io/ (author site; startup move)
- https://huggingface.co/api/models?search=phasecast (verified absence)
