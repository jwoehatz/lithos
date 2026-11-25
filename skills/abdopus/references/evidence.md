# Evidence behind abdopus

Source: `~/Downloads/Octopus Arms, Agent Swarms (v1).html` (internal research note, v3 deep-research pass).

Status: every item below is cited from the note's abstract-level summaries. None was independently verified against the full papers. Treat the numbers as reported in the note, not as confirmed results.

## Findings used in the skill

- **Verifier false-positive ceiling (Stroebl et al. 2024).** With a non-zero verifier false-positive rate, resampling cannot push accuracy past a bound set by that rate, however much compute is spent. Optimal sampling attempts are often fewer than 10. Basis for E2 (prefer deterministic checks) and for keeping worker counts small.

- **Correlated errors (Kim et al. 2025).** Across 350+ LLMs, when two models both answer wrong on one leaderboard dataset, they give the same wrong answer 60% of the time. Correlation is higher among more accurate models and among models from the same developer. Basis for E5 (heterogeneous families), for forcing the director on high-stakes output, and for the same-wrong redundancy check and 60% threshold in E8.

- **Interaction tax (Ann et al. 2026).** When agents read each other's complete outputs, their proposals converge within one round, erasing diversity. Independent proposal generation avoids this. Basis for the blind round in phase 1.

- **Diversity beats count (Yang et al. 2026).** Performance is bounded by intrinsic task uncertainty, not agent count. Homogeneous agents saturate early. Two diverse agents can match or exceed sixteen homogeneous ones. Basis for E5 and for keeping N small.

- **Skill compilation (SkillCache, Ni et al. 2026, NVIDIA).** Compiles a completed skill invocation into a parameterized capsule of programs plus natural-language steps, replays it before reuse, and keeps the source skill for recovery. Warm execution cut tokens by 81% (Claude Sonnet 4.6) and 74% (Claude Opus 4.8) at comparable reward across 87 skills. Basis for E4 (muscle-memory cache). The 74–81% figure is the token cut reported in the note.

- **Strategy bidding (SALE, Alazraki et al. 2026, Meta, arXiv 2602.02751).** Small agents bid short plans, scored by cost against value. Reported: reliance on the largest agent cut by 52%, overall cost by 35%, quality improved. Basis for E7 (bidding before dispatch).

- **Plan-time model tiering (Planner-as-Router, Singh 2026, arXiv 2609.32917).** Assigns a model tier per subtask at plan time. Reported: 44% lower cost for a 2.9-point accuracy loss. Basis for the cost tiers in E7 bids.

- **Early stopping (CGES, Aghazadeh et al. 2026).** Bayesian posteriors over candidate answers, halting once one accumulates enough mass. Average calls fell from 16.0 to 6.7 (−58%), within 0.4 points of fixed self-consistency. Basis for the disagreement gate (E1).

- **Semantic agreement cascades (Soiffer et al. 2025, CMU).** For open-ended generation, meaning-level agreement among ensemble outputs is a stronger deferral signal than token-level confidence. Semantic cascades matched or beat the target model's quality at 40% of the cost. Basis for measuring disagreement by meaning in the gate.

## Caveats

- Results come from different benchmarks and model generations. Do not transfer the percentages directly to Hatz models.
- SALE and Planner-as-Router are cited from their abstracts only. Their figures (52%, 35%, 44%, 2.9 points) are not independently verified. The bid cost weights and the 0.25 minimum score in E7 are local choices, not taken from either paper.
- The note itself marks the diversity and interaction-tax claims as "established" from the abstract level only.
- Re-check any number before quoting it outside this skill.
