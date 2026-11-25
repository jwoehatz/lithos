# GeoGalactica × PhaseCast: How They Could Work Together

**Date:** 2026-11-25 · **Run:** abdopus `together-synthesis` (3 agents: ds-builder@1, glm-literature@1, director@1 — all blind to each other; ground truth = verified facts from the `geogalactica-apps` and `phasecast-apps` runs)
**Gate:** worker disagreement d ≈ 0.1 (< τ=0.3), all checks passed (2 + 15 + 0 URLs; 0 allowed for design) → compiled without director review. One sequencing difference between the director and both workers is reconciled explicitly below, not silently.

## Verdict

**The pairing is novel — no published work combines a geoscience LLM with a geochemical predictor — and the best-fit pattern is unambiguous: LLM orchestrates, PhaseCast executes (the ChemCrow mold), with structured grounding so the LLM never invents numbers.** But the honest conclusion is that **the concept is right and GeoGalactica is the wrong LLM**: its verified weaknesses (prompt-following failure, gating, >140GB footprint, license conflict, dormancy) make it impractical as the working component. GeoGalactica contributes the *idea* — geoscience tool-learning lineage — and a knowledge-engine role at best; a modern open instruction-tuned LLM takes the orchestrator seat. The pragmatic path is staged: deterministic pipeline first (lowest risk), agentic tool-calling second.

## Concepts

### 1. Agentic tool-calling — LLM frontend, PhaseCast tool backend

User asks in natural language → LLM extracts the whole-rock composition (pasted CSV or inline oxide list) → emits a structured tool call → a thin shim loads PhaseCast's two git-tracked checkpoints, runs a forward pass (~15 ms/rock on CPU, no Julia/MAGEMin needed) → returns a JSON posterior over 7 mineral groups + P/water/temperature path → LLM renders a grounded answer.

- **LLM contributes:** language interface, composition extraction, prose synthesis.
- **PhaseCast contributes:** the numeric inverse problem the LLM cannot do — mineralogy and formation conditions from chemistry.
- **Plausibility:** squarely in GeoGalactica's own lineage (geotools: ~10k ToolBench samples + geo_search); PhaseCast is the ideal tool shape (MIT, runnable, clean function contract, already parses ALS/Actlabs exports).
- **Risk (unverified):** whether GeoGalactica can produce reliable structured tool calls — the one third-party evaluation found it "not following our prompts." Tool-calling is instruction-following under load.

### 2. Structured grounding / fixed pipeline — PhaseCast first, LLM narrates

A batch CSV goes through PhaseCast → posteriors are serialized and injected into the LLM's context as a fixed text template → the LLM writes interpretation *strictly over the injected numbers*, never asserting mineralogy it wasn't given.

- **Plausibility:** sidesteps tool-call reliability entirely — the LLM only completes text, a completion-style task that suits a Galactica base. Plays to GeoGalactica's verified strength (broad geoscience text knowledge) while PhaseCast supplies the numbers it can't compute.
- **Risk:** hallucination beyond the injected facts (the paper prints its own warning); 2048-token context limits batch size. Needs a deterministic consistency check — extract mineral names from the narrative and flag any the posterior gives low probability.

### 3. LLM as scope and plausibility gate around PhaseCast

Before inference the LLM reads sample metadata and classifies volcanic vs out-of-scope; after inference it compares PhaseCast's formation conditions against tectonic-setting knowledge and flags conflicts. **Weakest concept:** the LLM's judgment is unvalidated, its hallucinations could produce false flags, and a simple SiO₂/TAS rule would probably beat it at the scope check. Worth naming to reject it honestly.

### 4. Embedding fusion — proposed, and rejected

The builder proposed PhaseCast's 256-d composition encoder as a geochemistry "sensor" modality projected into the LLM's embedding space. The literature arm rejected the pattern with evidence (benchmarking general LLMs for polymer property prediction found LLM-based methods "generally underperform in predictive accuracy" vs domain-specific encoders, arXiv:2506.02129), and the director rejected it on the facts (no shared representation exists; a 256-d composition encoder and a 30B text model's hidden states would need new paired training data and a trained adapter that doesn't exist). **All three positions converge on: not supported by the verified facts.** The one genuinely novel artifact in either project — PhaseCast's masked-element-pretrained latent — stays valuable *inside* PhaseCast, not as a cross-model bridge.

## Literature grounding

The dominant, validated pattern for LLM + scientific predictor is **tool-calling with structured grounding** — every successful system found uses orchestration, none fuse embeddings:

- **Toolformer** (Schick et al., [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)) — models trained to interleave API calls into generation.
- **Gorilla** (Patil et al., [arXiv:2305.15334](https://arxiv.org/abs/2305.15334)) — retrieval-grounded tool use "substantially mitigates hallucination"; documents LLMs' "inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call."
- **ChemCrow** (Bran et al., [arXiv:2304.05376](https://arxiv.org/abs/2304.05376)) — LLM chemistry agent with 18 expert tools; its most cited finding is the error-laundering risk: fluent narration converts tool output into confident-sounding prose.
- **Coscientist** (Boiko et al., [Nature 624](https://www.nature.com/articles/s41586-023-06792-0)) — GPT-4 planner driving deterministic engines; GPT-3.5 repeatedly failed valid JSON where GPT-4 complied (the format-failure gradient GeoGalactica sits on the wrong end of).
- **Logic-LM** (Pan et al., [arXiv:2305.12295](https://arxiv.org/abs/2305.12295)) — LLM translates, solver executes, solver errors drive self-refinement; +39.2% over LLM-alone.
- **polyT5** (Sahu et al., [arXiv:2510.18860](https://arxiv.org/abs/2510.18860)) — **structurally closest precedent**: a specialized property predictor coupled with a general-purpose LLM inside an agentic framework (polymer domain).
- **SciAgents** ([arXiv:2409.05556](https://arxiv.org/abs/2409.05556)), **SciAgent** ([arXiv:2402.11451](https://arxiv.org/abs/2402.11451)) — tool-augmented scientific reasoning at benchmark scale.
- **ChemToolAgent** ([arXiv:2411.07228](https://arxiv.org/abs/2411.07228)) — tool augmentation helps specialized prediction, not general knowledge questions; expect the same boundary here (PhaseCast calls are valuable for mineralogy questions, useless for "explain how arc magmas form").
- **Plausibility-validity gap** ([arXiv:2507.07328](https://arxiv.org/abs/2507.07328)) — outputs that "appear scientifically reasonable yet violate fundamental principles"; the exact failure mode of narrating PhaseCast's known systematic abundance offsets without carrying uncertainty.

**Novelty: confirmed by four negative arXiv searches** — `petrology + language model` = 0; `whole-rock + language model` = 0; `mineralogy + LLM` = 1 unrelated (lunar ISRU table extraction, [arXiv:2504.20125](https://arxiv.org/abs/2504.20125)); `geoscience + LLM + geochemistry` = 1 unrelated (HERMES document extraction, [arXiv:2608.14055](https://arxiv.org/abs/2608.14055)). No published work combines a geoscience LLM with a geochemical/mineralogy predictor. The closest precedents are all in chemistry/materials.

## Most promising: staged roadmap

The two workers lead with **tool-calling** (highest value, most generalizable — turns PhaseCast from "run a script" into "ask a question"); the director independently prefers the **fixed pipeline** first (lowest risk — the LLM never has to emit a correct call, and GeoGalactica's verified weakness is exactly call emission). The compile honors both as a sequence rather than picking silently:

- **Stage 1 — Pipeline (director's pick):** PhaseCast batch → JSON-to-text template → LLM narrates. Every call is deterministic; the LLM only completes text. Falsifiable cheaply via the consistency checker. This works *today* with PhaseCast's git-tracked weights and any completion-capable model.
- **Stage 2 — Agentic tool-calling (workers' pick):** expose PhaseCast as a typed tool (`predict_mineralogy(composition_table) -> posterior + uncertainty + scope flags`) behind a hard schema gate with error-feedback self-refinement (the Logic-LM mechanism). The orchestrator is a modern open instruction-tuned LLM (7–13B); GeoGalactica, if access is granted, is at most the geoscience knowledge engine for question interpretation and result narration — not the call emitter.

## Blockers

| Component | Blocker | Severity |
|---|---|---|
| GeoGalactica | Prompt-following failure ("model not following our prompts") | **Fatal** for it as tool-caller; kills the GeoGalactica-variant, not the concept |
| GeoGalactica | Gated weights (login+accept; ckpt request-only) | Demo can stall waiting for approval |
| GeoGalactica | >140 GB fp32, 2048-token context | Fatal for batch grounding; quantization quality untested |
| GeoGalactica | License conflict (Apache-2.0 code tag vs non-commercial research-preview README) + Sci-Hub copyright controversy | Rules out commercial use; public demo legally risky |
| GeoGalactica | Dormant (~1 download/month, no maintainers) | No ecosystem to build on |
| PhaseCast | Volcanic-only training, 7 coarse mineral groups | Limits domain; **no concept overcomes this without retraining** |
| PhaseCast | No external baseline; simulated (MAGEMin) labels; known systematic abundance offset (11.0% → 9.5% recalibrated) | The LLM must caveat; trust is unbenchmarked |
| PhaseCast | Solo author, now at a stealth startup; zero adoption | Expect to fork and maintain yourself |
| Combined | Both unvalidated on independent ground truth — stacking them stacks uncertainty | A demo can show the plumbing works; it cannot show the answers are correct |

## Minimal demo (~2 weeks)

**Week 1**
- Install PhaseCast from GitHub (weights are in the repo); pull the Zenodo corpus.
- Pick ~50 volcanic samples with published modal mineralogy (PhaseCast's own `data/real_mineralogy/` benchmark set is public-domain USGS) — the only external check available.
- Run inference; turn posteriors into a JSON-to-text template.
- In parallel, request GeoGalactica access. Fallback: a 7–13B open instruction-tuned model, labeled clearly as a substitute.

**Week 2**
- LLM writes a 1-paragraph interpretation per sample (Stage 1 pipeline).
- Build the **consistency checker**: extract mineral names from the narrative, compare against the PhaseCast posterior, flag contradictions. Add a hard schema gate if any tool-calling is attempted (Stage 2).
- Score three things: (a) PhaseCast's agreement with published modes at mineral-group level; (b) the share of narratives that contradict the posterior; (c) for GeoGalactica specifically, the share of outputs that are well-formed.

**Expected result:** PhaseCast gives plausible group-level calls on volcanic samples. The narrative layer contradicts the posterior noticeably more often with GeoGalactica than with a modern instruction-tuned model. The deliverable is a **measured contradiction rate** — not a claim that the system is right.

## Predictions

Stated before dispatch, scored at compile:

| # | Prediction (agent) | Outcome |
|---|---|---|
| 1 | ds-builder: most promising integration uses PhaseCast as a tool called by an LLM, not the reverse | **CONFIRMED** — both workers and the director structure it this way |
| 2 | ds-builder: GeoGalactica unusable as the LLM component; modern open LLM substitutes | **CONFIRMED** — all three agents converge |
| 3 | ds-builder: no concept overcomes volcanic-only training without retraining | **CONFIRMED** — all three treat scope as a hard limit |
| 4 | glm-literature: dominant pattern is tool-calling, not embedding fusion | **CONFIRMED** — every verified system orchestrates; fusion evidence is negative |
| 5 | glm-literature: no published geoscience-LLM + geochemical-predictor work exists | **CONFIRMED** — 4 negative arXiv searches; pairing is novel |
| 6 | glm-literature: ChemCrow or close analogue is the closest precedent | **CONFIRMED and refined** — polyT5 is structurally closest |
| 7 | director: both workers will lead with PhaseCast-as-tool | **HIT** |
| 8 | director: at least one worker will propose unsupported embedding fusion | **HIT** — builder proposed it, self-flagged as speculative; literature rejected with evidence |
| 9 | director: at least one worker will recommend substituting a modern open LLM | **HIT** — builder explicitly |
| 10 | director: neither worker will propose an automated narrative-vs-posterior consistency check | **HIT** — only the director did |

Director calibration note: 4/4 hits this run (after 2/5 in Run 1 and a mixed Run 2) — its workers-are-sloppy predictions were accurate in Run 1 and too pessimistic in Run 3, while its structural predictions (what a design pass will and won't think of) held throughout.

## Check result

- **Verified URLs: 17** (builder 2 — both repos fetched to confirm interface facts; literature 15 — all fetched or returned by arXiv API queries this session; director 0, allowed for a design task).
- 0 dead links among cited sources. The `websearch` tool returned zero results for every agent across all three runs this session (quota/bot-blocked); all agents pivoted to direct fetches and API queries — a recurring environment observation, logged to the CPI ledger.
- Gate: d ≈ 0.1 < τ=0.3, checks passed → compiled without director review. The director-vs-workers sequencing difference is reconciled explicitly in the roadmap, not silently.

## Sources

- https://github.com/matthew-j-liu/phasecast · https://github.com/geobrain-ai/geogalactica (interface facts, fetched by builder)
- arXiv:2302.04761 (Toolformer) · arXiv:2305.15334 (Gorilla) · arXiv:2304.05376 (ChemCrow) · Nature s41586-023-06792-0 (Coscientist) · arXiv:2305.12295 (Logic-LM) · arXiv:2510.18860 (polyT5) · arXiv:2409.05556 (SciAgents) · arXiv:2402.11451 (SciAgent) · arXiv:2411.07228 (ChemToolAgent) · arXiv:2507.07328 (plausibility-validity gap) · arXiv:2506.02129 (polymer LLM benchmark) · arXiv:2504.20125 · arXiv:2608.14055 (negative-search confirmations)
- Ground truth from runs 1–2: arXiv:2401.00434, arXiv:2610.36429, zenodo.org/records/23992951, huggingface.co/geobrain-ai/geogalactica
