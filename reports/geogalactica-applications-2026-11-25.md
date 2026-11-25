# GeoGalactica: Applications and Demonstrations

**Date:** 2026-11-25 · **Run:** abdopus `geogalactica-apps` (3 agents: glm-literature@1, ds-skeptic@1, director@1 — all blind to each other)
**Gate:** disagreement d ≈ 0.1 (< τ=0.3), all deterministic checks passed (22 + 21 + 8 verified URLs, 0 failures) → director review skipped, compiled from converging worker reports + director's independent findings.

## Verdict

**GeoGalactica is a paper-and-code artifact, not a live application.** No third-party project, tool, or product uses its weights. All demonstrations are by the original SJTU/Acemap team inside the technical report (arXiv:2401.00434). The repo is dormant (last commit 2024-06-27), the weights are gated, the only public demo is broken, and the project carries a documented copyright-infringement controversy. The prior scan's "Live" label (hd-geoscience-scan-2026-11-25.md) is **overstated** — accurate label: *weights reachable, project dormant*.

## Findings

### 1. Popular applications

**None found.** All 64 citing papers (Semantic Scholar API, verified 2026-11-25) fall into three buckets, none of which use the weights:

- **Related-work/survey mentions** — PEACE/GeoMap-Agent ([arXiv:2501.06184](https://arxiv.org/abs/2501.06184)), PANGAEA-GPT ([arXiv:2503.05854](https://arxiv.org/abs/2503.05854)), GeoAgent ([arXiv:2410.18792](https://arxiv.org/abs/2410.18792)), geotechnical LLM review ([arXiv:2507.05613](https://arxiv.org/abs/2507.05613)), foundation-model surveys.
- **GeoBench/GeoSignal data-lineage users** (data comes from K2, not the GeoGalactica model) — serverless GeoBench benchmarking ([DOI:10.5753/pesquisanuvem.2026.22263](https://doi.org/10.5753/pesquisanuvem.2026.22263)), JiuZhou ([DOI:10.1080/17538947.2025.2449708](https://doi.org/10.1080/17538947.2025.2449708)).
- **Same-team follow-ons** citing it as lineage, not as a component — DS-Agent ([arXiv:2402.17453](https://arxiv.org/abs/2402.17453)), NovelQA ([arXiv:2403.12766](https://arxiv.org/abs/2403.12766)), Innovator ([arXiv:2507.18671](https://arxiv.org/abs/2507.18671)).

Third-party baseline usage exists but is evaluation, not application: GR1 (ACL 2026 Findings, [2026.findings-acl.1140](https://aclanthology.org/2026.findings-acl.1140.pdf)) reports GeoGalactica-30B scores (All 30.34); an AACL 2026 survey lists availability as "P" (paper). The "largest geoscience LLM" claim is superseded (GeoGPT at 70B+ has passed it).

### 2. Demonstration projects

All working demonstrations are **original-author only**, inside the paper:

- **Geoscience Q&A at three difficulty levels** — human evaluation by 10 geoscientists vs 5 general LLMs; GeoGalactica ranks third overall, behind ChatGPT (§6.2).
- **Research-paper titling and summarization** — ChatGPT and MOSS still beat it on summarization (§6.2.6–6.2.7).
- **Tool learning** — ~10k ToolBench samples + custom `geo_search`; released as [geotools](https://github.com/zthang/geotools). The paper calls this "Primitive Explorations to Use Tools."
- **Byproducts** — sciparser (PDF parsing), GeoSignal/GeoBench datasets, GeoGalactica_Analysis (plotting scripts, 4 stars).

The **only third-party demo attempt** — HF Space [Nightseeker/geobrain-ai-geogalactica](https://huggingface.co/spaces/Nightseeker/geobrain-ai-geogalactica) — is a bare `gr.load()` wrapper that fails live with `ModelNotFoundError` (the gating breaks even the demo). Verified broken 2026-11-25.

### 3. Adoption signals

| Signal | Value |
|---|---|
| GitHub | 44 stars, 9 forks, 1 watcher, 12 commits (all README-level), last commit **2024-06-27** (~29 months stale) |
| HuggingFace | gated; **1 download last month**; 18 likes; no inference provider; no downstream fine-tunes/derivatives |
| Citations | 64 (Semantic Scholar), 1 marked influential; all related-work/data-lineage per citation-context sampling |
| Issues | 2 open from Jan 2024, unanswered by maintainers (local deployment, data-mixing questions) |

### 4. Weights availability

- [HF model](https://huggingface.co/geobrain-ai/geogalactica): gated (login + accept conditions); 13 shards ~9.9 GB each (~120 GB); fp32 inference needs **>140 GB memory**.
- [geogalactica-ckpt](https://huggingface.co/geobrain-ai/geogalactica-ckpt): request-only via email with "strict verification"; only the first 3/4 of pre-training is open-sourced — the final SFT model is not freely downloadable.
- **Licensing conflict:** HF tag says Apache-2.0 (covers code only); README says "research preview intended for non-commercial use only," subject to Galactica's CC-BY-NC and OpenAI terms on distilled SFT data.

### 5. Limitations and red flags (primary sources)

- **Hallucination warning printed in the paper itself**: "The model in this manuscript might produce hallucinations and reader discretion is recommended."
- **MMLU regressions** vs base Galactica-30B: physics, medicine, medical genetics, electrical engineering all decline.
- **GeoBench profile**: strong on NPEE (graduate-exam), poor on AP Study (foundational) — attributed to paper-heavy training corpus.
- **Practical barriers**: 2048-token context; 2022-era Galactica base.
- **Third-party prompt-following failure**: "Which is the Best LLM for Geosciences?" (IGARSS 2025, [DOI:10.1109/IGARSS55030.2025.11243488](https://doi.org/10.1109/IGARSS55030.2025.11243488)) — "implemented Geogalactica but did not achieve meaningful results due to the model not following our prompts"; results omitted from that paper. (ds-skeptic attributes an equivalent quote to an IEEE JSTARS 2026 comparative evaluation — likely the same line of work reported at two venues; IGARSS DOI cited as primary.)
- **Copyright infringement (documented)**: the paper admits Sci-Hub PDF scraping; The Geoscientist (2025) states GeoGalactica "is acknowledged to have extensively infringed copyright (Cleverley et al., 2024; Ludden et al., 2025)."
- **DDE affiliation controversy**: mislabeled as a DDE collaboration without DDE review; IUGS instigated a review of DDE activities (Feb 2024). The GitHub README now disavows DDE, but the geogalactica-ckpt model card still names the DDE Science Center, and a 2024 EGU abstract ([EGU24-6431](https://doi.org/10.5194/egusphere-egu24-6431)) still claims DDE support — disavowal inconsistent across surfaces.

## Correction to prior scan

`hd-geoscience-scan-2026-11-25.md` lists GeoGalactica as "Live." This run's evidence downgrades it: **dormant artifact** (repo untouched ~29 months, gated weights, 1 download/month, zero downstream use). Any future work in this repo should treat GeoGalactica as a citable lineage item, not a usable component.

## Predictions

Stated before searching, scored at compile:

| # | Prediction (worker) | Outcome |
|---|---|---|
| 1 | glm-literature: ≥1 published downstream application beyond the original paper | **FAIL** — 64 citations, zero weight-users |
| 2 | glm-literature: weights publicly downloadable | **PARTIAL/FAIL** — exist but gated; ckpt request-only |
| 3 | glm-literature: ≥1 third-party demo/tutorial exists | **FAIL** — only candidate is broken |
| 4 | ds-skeptic: no substantive commit in last 6 months | **CONFIRMED** — last commit 2024-06-27 |
| 5 | ds-skeptic: no third-party published application exists | **CONFIRMED** |
| 6 | ds-skeptic: weights NOT trivially downloadable (gated/request-only) | **CONFIRMED** |

Director predictions (scored against worker reports): "at least one worker will miss the gating" — miss (both caught it); "at least one worker will present an original-author item as third-party" — miss (both attributed correctly); "neither finds a working third-party product" — hit; "if both check commit dates they agree it is stale" — hit (both checked, both said stale); "at least one worker will miss the prompt-following failure report" — miss (both found it). Director's workers-read-the-evidence predictions were largely too pessimistic; its repo-vitality conditional was correct.

## Check result

- **Verified URLs cited as fact: 51 total** (glm-literature 22, ds-skeptic 21, director 8; overlap on core primary sources). 0 dead links among cited sources.
- Unverified items were quarantined under "Unverified links" by each agent and are not cited as fact here (README-linked sibling repos fetched by at most one agent; Geoscientist viewpoint pieces verified in a prior run, not re-fetched).
- Gate: d ≈ 0.1 < τ=0.3, all checks passed → compiled without director review. The one venue discrepancy (IGARSS 2025 vs IEEE JSTARS 2026 for the prompt-following failure) is flagged inline above.

## Sources (core, verified live 2026-11-25)

- https://github.com/geobrain-ai/geogalactica (repo, commits, issues)
- https://huggingface.co/geobrain-ai/geogalactica · https://huggingface.co/geobrain-ai/geogalactica-ckpt
- https://huggingface.co/spaces/Nightseeker/geobrain-ai-geogalactica (broken demo)
- https://arxiv.org/abs/2401.00434 (technical report)
- https://api.semanticscholar.org/graph/v1/paper/arXiv:2401.00434 (citationCount=64 + contexts)
- https://aclanthology.org/2026.findings-acl.1140.pdf (GR1 baseline usage)
- https://www.researchgate.net/publication/415127119_A_Comparative_Evaluation_of_Open-Weight_LLMs_for_Geoscientific_Tasks
- https://geoscientist.online/sections/viewpoint/geogpt-an-update/ (copyright/DDE controversy; prior-run verified)
- https://www.ddeworld.org/news/detail/297 · https://doi.org/10.5194/egusphere-egu24-6431
