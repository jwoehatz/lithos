---
name: subagent-dispatch-matrix
description: Pick the role and model for any subagent dispatch (director, middle-manager, workers, specialists, named-agent fleet), and run the creative pre-flight gate before any creative task goes to a budget worker. Use whenever you dispatch a subagent without a specified model, plan a multi-agent fan-out, or hand voice, lore, naming or narrative work to a cheaper model.
---

# Subagent dispatch matrix + creative pre-flight

One skill for two linked rules: **which model gets which job**, and **when to ask before spending the strongest model on creative work**.

## Files

- `references/matrix.md`: the full canonical matrix (roles, scores, DeepSeek-over-GPT ruling, fleet, billing caveats, octopus pattern). Read it when you need a reason, not only a route.
- `references/creative-preflight.md`: the full gate procedure with worked examples.
- `data/matrix.json`: machine-readable routes and fleet. The scripts read it. **If you change the matrix, update both files.**
- `scripts/route.py <task-type>`: prints role, model and whether pre-flight applies. `--list` shows all task types.
- `scripts/preflight_prompt.py <brief.md|->`: wraps a worker brief in the single-response assessment prompt for the director.
- `scripts/check_fleet.py [agents-dir]`: compares each named agent's `model:` against the matrix and exits 1 on drift. Use it after editing agents, or when a model looks wrong.

The scripts use only the Python 3 standard library. Each script has a `--help` flag.

## Quick routes

| Task | Role | Model |
|---|---|---|
| Review, rulings, creative pre-flight | Director | Opus 5.5 |
| Decompose, dispatch, final compile | Middle-manager | GLM 5.3 (session) |
| One-shot research / creative / code | Worker | GLM 5.3 |
| Multi-step feature or research; voice/lore | Worker | Haiku 5.5 |
| Single-file / mechanical sweeps | Worker | GLM 5.2 Fast |
| Research fan-out, generic leaf lookups | Budget worker | DeepSeek V4 Flash 0731 |
| Slot where GPT would be picked | Worker | DeepSeek V4 Pro 0813 |

Sonnet 5.5 and all Llama models have no role. GLM 5.3 Flash and DeepSeek V4.1 Flash are blocked by default. Probe with one cheap dispatch before you rely on either. Named specialists (DbResearch, IntercomReader, StripeReader, Renmin, Jianghu) have their models set in config. Pass only the question and the IDs, with no model parameter.

## Creative pre-flight gate

This applies when the route is a **creative** task type (`route.py` prints `preflight_required: true`): voice, lore, naming, narrative design or tone-sensitive copy.

1. Write the worker brief: 3 to 6 deliverables, a do-NOT-redo list, and at most one open question.
2. `python3 scripts/preflight_prompt.py brief.md`, then send the output to the director (Opus 5.5) as **one response**. Never send it the full task.
3. `BUDGET_OK`: dispatch the brief as planned and note the verdict.
   `NEEDS_STRONGEST`: **STOP.** Ask the user: "Opus's read is this needs Opus-level execution because [signals]. Commit Opus 5.5 to the full run?"
4. If the user approves, run Opus. If they decline, run the budget worker. Never silently upgrade or downgrade.

## Brief hygiene (all dispatches)

- 3 to 6 deliverables, an explicit do-NOT-redo list, and at most one open question.
- For multi-angle research or design, use the `abdopus` skill (octopus pattern). This matrix supplies its model choices.
- Do not send messages to a subagent session while it is still working. Reuse sessionIDs for revisions.
