---
name: creative-preflight
description: Before dispatching a creative task (voice, lore, naming, narrative design, nuanced copy) to a cheaper worker model like Haiku, run a quick strongest-model assessment pass on the brief. If the assessment says the task would benefit from strongest-model execution, stop and ask the user to commit that model to the full run before spending it. Never silently upgrade.
---

# Creative pre-flight gate

A cheap triage step that decides whether a creative task can safely go to a budget worker or needs the strongest model committed up front.

## Why

Creative work fails differently than code: a wrong voice or flat naming ships looking "fine" and only reads wrong later. Budget workers (Haiku 5.5 tier) handle most creative briefs well, but the misses are expensive to catch after the fact. A one-response assessment from the strongest model costs almost nothing; a full strongest-model run costs a lot. The gate spends the cheap one to protect the decision about the expensive one.

## When to use

Apply before dispatching any **creative** task to a worker model. Creative means: voice/lore writing, naming proposals, narrative design, worldbuilding, tone-sensitive copy, visual/UX creative direction. Not: mechanical text sweeps, code, research fan-out, or lookup tasks — those follow the normal dispatch matrix.

## The gate

1. **Frame the brief.** Write the worker brief as you normally would (3–6 deliverables, explicit do-NOT-redo list, one open question max).
2. **Run the assessment pass.** Dispatch a single-response triage to the strongest model (Opus 5.5) with the brief and the question: *can a budget worker handle this alright, or does this task need strongest-model execution?* Ask for a verdict plus the specific signals: nuance density, voice constraints, number of interacting creative judgments, cost of a miss.
3. **Branch on the verdict:**
   - **Budget worker fine** → dispatch the original brief as planned. Record the assessment result in the dispatch note.
   - **Would benefit from strongest model** → STOP. Do not dispatch. Do not upgrade silently. Ask the user: "Opus's read is this task benefits from Opus-level execution because [signals]. Commit Opus 5.5 to the full run?"
4. **On user approval**, dispatch the full task to the strongest model. On decline, dispatch to the budget worker as originally planned — the gate informs, the user decides.

## Rules

- The assessment is one cheap response, never the full task.
- Never silently upgrade to the strongest model on creative work; the gate is cheap, the full run is not.
- Never silently downgrade either: if the user committed the strongest model, that's the dispatch.
- The gate applies per-task, not per-session: a batch of small creative tasks can share one assessment if the briefs are similar.
- If the strongest model is unavailable or blocked, say so and ask the user which model should both assess and run.

## Example

> Brief: "Rename these 10 visitor archetypes to garden vocabulary; keep the LLM-infrastructure metaphor readable in each; one open question on cadence."
>
> Assessment (Opus 5.5, single response): "Budget worker fine — mechanical-ish naming with a clear metaphor constraint; the miss cost is low because names are individually reviewable."
>
> → Dispatch to Haiku 5.5 as planned.

> Brief: "Write the fall-of-rent economy montage: 9 beats, each beat must carry the comic-book-store canon constraint, the windowsill voice, and land the kudzu pest origin reveal in beat 7."
>
> Assessment: "Would benefit from strongest-model execution — three interacting voice/canon constraints per beat and a mid-sequence reveal whose placement is load-bearing."
>
> → Stop. Ask the user to commit Opus 5.5 before spending the run.
