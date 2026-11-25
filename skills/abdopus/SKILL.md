---
name: abdopus
description: Use for multi-angle research, design, or review tasks worth fanning out to several subagents under a strongest-model director, with deterministic checks, disagreement-gated escalation, and a calibration ledger. Skip tiny one-shot tasks.
---

# Abdopus (octopus orchestration pattern)

Named for the algae octopus, which walks on two arms while the rest work on their own: a few arms carry out the plan, the others act independently.

Orchestrate a small set of diverse, cheap workers in parallel, have one strong director review their reports, and compile the result with deterministic checks. Escalate only when the workers disagree or fail a check.

Use this when the output can be checked (tests, schemas, grep, a compile step, a numeric bound) and the question has several angles worth comparing. Do not use it for everything. See "When NOT to use".

## Roles (model-agnostic)

Pick models by role, not by name. Use the example mapping at the end only as a snapshot.

- **Orchestrator**: the agent running this skill. Mid-tier is enough. It frames the task, runs bidding, writes briefs, dispatches, and compiles.
- **Director**: the strongest available model. Forms its own findings, reviews worker reports, and issues binding rulings.
- **Workers**: cheap, diverse models, each a named identity from the persistent roster (E8). Split into one-shot workers, multi-step workers, and mechanical-sweep workers as needed.
- **Specialists**: narrow workers with a fixed tool or source (a database, an API, a code search). Treat them as workers with a stricter brief.
- **Verifier**: a deterministic check, not a model. A script, test, schema validator, grep, or `node --check`. Verifiers are the ground truth. A model judge is never the only check.

## Flow

```
                    +------------------+
   request ------>  | 0. cache check   |--hit (shadow 2-5%)--> compile, skip to 4
                    +--------+---------+
                             | miss
                    +--------v---------+
                    | 1. coarse pass   |  orchestrator reads plan, frames constraints
                    +--------+---------+
                             |
                    +--------v---------+
                    | 1b. bid (E7)     |  2-4 roster workers bid short plans
                    | skip if small    |  score = EV / cost; award or merge
                    +--------+---------+
                             | award (director plan only if no bid clears)
                             | dispatch in parallel, workers blind to each other
          +------------------+----+-----------------+
          v                       v                 v
   workers (2+, diverse)   specialists          director (own findings)
   each: self-verify,      (fixed source)       states falsifiable predictions
   retry locally           each: verify         |
          +------------------+------------------+
                             |
                    +--------v---------+
                    | gate: disagree   |--no, all pass, not forced--> 4
                    | >= tau OR fail?  |
                    +--------+---------+
                             | yes (or forced)
                    +--------v---------+
                    | 2. director      |  binding rulings + revision briefs
                    |    review        |  may rule phases unnecessary
                    +--------+---------+
                             |
                    +--------v---------+
                    | 3. revise in     |  reuse ORIGINAL worker sessionIDs
                    |    same sessions |  (only if director asked)
                    +--------+---------+
                             |
                    +--------v---------+
                    | 4. compile +     |  deterministic check on output
                    |    verify        |  + director ruling; log to ledger
                    +--------+---------+
                             |
                       done, or escalate: cheap -> mid -> director -> human
```

## Phase 0: Cache check (before phase 1)

If a compiled ruling or script already exists for this task type, use it first (see E4). Compute the canonical key from task type plus normalized slots. Do not match on raw text similarity. On a hit, run the cached check. Shadow-check 2-5% of hits with a fresh worker. A miss goes to phase 1.

## Phase 1: Coarse pass and parallel dispatch

1. Read the plan or request. Write down the constraints: scope, forbidden actions, output format, and the deterministic check that will judge success. If you cannot name a check, stop. See "When NOT to use". Name the task type (for example `research`, `design`, `review`, `code`, `sweep`). The ledger and roster key on it.
2. Decide whether to bid (E7). Small tasks and tasks with one obvious route skip bidding and go straight to step 3.
3. Choose N workers from the roster (E8). Start small. Two diverse workers usually beat many identical ones (E5). Use fewer than 10 unless the task clearly rewards more. Specialists are separate from this count. If bidding ran, the awarded plan's workers are the ones dispatched.
4. Give every worker a different model family and/or a different lens. Same-question workers must not share both. The roster rules enforce this (E8). Correlated errors are common across models from one developer and across samples from one model (Kim 2025). Diversity is what makes agreement mean something.
5. Dispatch the director and all workers and specialists in parallel. Do not let workers read each other's output in this round. Read-your-peers collapses diversity within one round (interaction tax). Bidders are also blind to each other.
6. Every agent (director included) must state explicit falsifiable predictions, such as "the function X is called from Y", "tests A and B fail", or "the benchmark moves by more than 2%". Vague predictions cannot be scored in E3.
7. Each worker brief must include:
   - **Identity**: its `worker_id@version`, so its ledger lines and track record attach to the right identity.
   - **Deliverables**: 3-6 numbered items. No more.
   - **Do-NOT-redo list**: what other agents or earlier phases already covered.
   - **At most one open question**. Put it last. If you need more, the task is underspecified; fix the brief first.
   - **Deterministic acceptance check** (E2): the exact command or validator the worker must run before reporting. Examples: a JSON schema validation, `node --check file.js`, `grep -c 'X' file` must return N, a test filter that must pass.
   - **Local retry rule**: fix and rerun the check locally, up to 2 retries. Report the final check result either way.
   - **Prediction line**: their falsifiable predictions.

### Worker types

- **One-shot worker**: single-question lookup or analysis with a fixed answer format.
- **Multi-step worker**: several dependent steps. Scope each brief small. Multi-step work degrades fast when briefs are large.
- **Mechanical-sweep worker**: repetitive find-and-replace or extraction across many files. Its output is checked by grep or tests, not by the director.
- **Specialist**: fixed source (a DB, Intercom, Stripe, a repo). Its brief names the exact source and the exact query shape.

### Strategy bidding before dispatch (E7)

Small agents that bid short plans, scored by cost against value, cut reliance on the largest agent in SALE (Alazraki et al. 2026). Planner-as-Router (Singh 2026) assigns a model tier per subtask at plan time. Both are abstract-level sources (see `references/evidence.md`).

- **Who bids**: 2-4 roster workers whose `task_types` include this task type, chosen by the selection rules in E8. Bids are blind.
- **Bid format**: a plan of 3-5 lines, an estimated `cost_tier` (`low`, `mid`, or `high`), the deterministic check the bidder will satisfy, and one falsifiable prediction about the result.
- **Score**: `score = EV / cost`. Cost weights: low = 1, mid = 2, high = 4. EV is the worker's expected hit rate on this task type: a Thompson draw from `Beta(correct+1, incorrect+1)` over its record (E8). A worker with no history gets the neutral prior, `Beta(1,1)`, mean 0.5.
- **Award**: the orchestrator awards the top-scoring plan, or merges two complementary plans. The director's plan competes only when no cheap bid clears the minimum score of 0.25. The director's own findings in phase 1 step 5 still run for the gate. Only its plan is affected here.
- **Not a verdict**: bids are not worker verdicts. Do not count them in the disagreement measure `d`.
- **Ledger**: log every bid as a line with `role` `bid`. Set its `outcome` to `awarded` or `not_awarded` at award time. Resolve a prediction only for awarded bids. Leave `not_awarded` bids with `correct` null.
- **Skip** bidding for small tasks or tasks with one obvious route. There the bidding round costs more than it saves.

## Gate: Does the director run? (E1)

Compute two things after the workers finish.

- **Disagreement** `d`: the fraction of worker verdicts or key facts that differ from the majority. For open-ended output, compare meaning, not tokens. Semantic agreement is a stronger signal than token overlap (Soiffer 2025). Start with `tau = 0.3` and recalibrate from the ledger (E3).
- **Checks**: did every worker pass its deterministic check?

Decision:

- `d < tau` AND all checks pass AND not forced: skip the director. Go to phase 4.
- `d >= tau` OR any check fails: run phase 2.
- High-stakes output (anything that ships to customers, changes data, or sets policy): force phase 2 regardless of agreement. Confident consensus can still be wrong, because errors are correlated.

Escalation ladder when a check fails or workers disagree:

1. Retry the failing worker once with a sharper brief (same session).
2. Re-run with a mid-tier worker from a different model family on the roster.
3. Director review (phase 2).
4. Human. Stop and report the disagreement. Do not pick a winner silently.

Use the director's running hit rate (E3) to decide whether its rulings can be trusted without human review. If the hit rate is below the agreed floor, route its rulings to a human.

## Phase 2: Director review (only if the gate says so)

The director receives every worker report, its own independent findings, and the original request. It must:

1. Compare each worker's claims to its own findings and to the original request. Mark each claim: accepted, rejected, or needs revision.
2. Issue **binding rulings**. Each ruling is one sentence, names the evidence, and is final for this task.
3. For each worker that needs more work, write a **revision or next-step brief** in the same format as phase 1 (3-6 deliverables, do-NOT-redo list, at most one open question, deterministic check).
4. Rule phases unnecessary if the workers already answered. Say so explicitly.
5. Score its own predictions against the evidence it now has. Record hits and misses (see E3).

The director does not rewrite worker deliverables. It rules and briefs.

## Phase 3: Revision in original sessions

Send revision briefs to the **original worker sessions** (reuse `sessionID`) so they keep their context. Do not start fresh workers unless the session is dead or the revision needs a different model family. A different model family means a different roster identity, not an edit to the old one.

Rules:

- Never message a subagent session while it is still working. Wait for it to finish, then send the brief.
- Revisions also go through the deterministic check. A revision that fails its check goes back through the escalation ladder, not straight to the director again.
- Stop after one revision round unless the director explicitly asks for another. Loops cost more than they fix.

## Phase 4: Intensive final compile and verification

1. Compile the accepted outputs into one deliverable. Keep the director's binding rulings visible in the compile, so the reasoning is auditable.
2. Run the **centralized deterministic check** on the compiled output (E6). Examples: the test suite, schema validation, a build, `node --check` on the inlined script, grep for required and forbidden strings, a numeric bound. The director's ruling and the deterministic check must both pass. An LLM judge alone can be gamed or fooled, so never accept a compile on judge approval alone.
3. Log predictions and outcomes to the ledger (E3, E8). Append one line per prediction, to `octopus-ledger.jsonl` in the task's working directory:
   ```
   {"date":"YYYY-MM-DD","task":"<short task id>","task_type":"<type>","worker":"<id>@<version>","role":"worker","prediction":"<falsifiable claim>","outcome":"<what happened>","correct":true,"cost_tier":"low"}
   ```
   Use `role` `bid` for bids and `director` for the director's lines. The director is also a roster entry (outside the bid pool), so its `worker` is `director@<version>`. Fill `outcome` and `correct` only when the result is known. Leave them null until then.
4. If the compile passes both checks and the ruling is stable, promote the ruling to the muscle-memory cache (E4) if the task type recurs.
5. Report to the user: the result, which checks passed, which predictions were logged, and anything escalated to a human.

## Muscle-memory cache (E4)

Compile a director ruling into a reusable script or checklist only when the same ruling repeats on a recurring task pattern. Rules:

- Key the cache on canonicalized intent: task type plus normalized slots. Never key on raw text similarity.
- Version every cached item. When a ruling changes, bump the version. Keep the old version for rollback.
- Measure **hit precision**, not hit rate. A cache that serves wrong answers fast is worse than none.
- Shadow-check 2-5% of hits with a fresh worker. If shadow results disagree with the cache, demote the entry and send the task through phase 1.
- Do not cache anything whose check is a model judge.

## Calibration ledger (E3)

- `octopus-ledger.jsonl` tracks each prediction and its outcome: director predictions, worker predictions, and bids (see phase 4 step 3).
- Track hit rate per `worker_id@version` per `task_type`, and for the director per `task_type`. Hit rate = correct / resolved predictions, over a rolling window. Do not collapse it into one global number.
- Trust rulings only while the director's hit rate meets the agreed floor. Below the floor, escalate every director ruling to a human until the rate recovers.
- Use the ledger to recalibrate `tau`. If the director often agrees with the workers when they are right, `tau` can rise. If workers often disagree and are right, lower `tau`.

## Persistent roster (E8)

The ledger is only meaningful if the same worker is tracked across runs. Each worker is a named, versioned identity.

- **Recipe**: `id` (a short name), `version`, `model_family`, `model`, `lens`, `temperature`, `tools`, and `task_types`. The example roster is `references/roster.example.json`.
- **Lens**: a fixed framing, such as `skeptic`, `builder`, `user-advocate`, `cost-hawk`, or `literature-first`.
- **Frozen versions**: a recipe does not change within its version. Changing the model, lens, or prompt bumps `version` and starts a fresh track record. The old record stays readable. Never silently edit a live worker.
- **Diversity rules**: no two workers may share both `model_family` and `lens`. Keep at least 3 model families and at least 3 lenses. In each dispatch, use at most one worker per model family unless the roster lacks options. The director is outside this count.
- **Track record**: per worker per `task_type`, read from the ledger. Every ledger line carries `worker_id@version` and `task_type`.
- **Redundancy check**: periodically compute the same-wrong rate for each pair of workers. Among items both got wrong, count how often they gave the same wrong answer. Kim 2025 reports about 60% for cross-model correlation. If a pair exceeds about 60% over at least 10 joint-wrong items, retire or re-lens one of them. Diversity is measured, not assumed.
- **Selection**: Thompson sampling or UCB over each worker's record for the task type. Keep an exploration floor of about 15% of dispatches (10-20%) going to non-leading or new workers. This stops the roster from collapsing into a monoculture and lets new versions earn a record.
- **Retirement**: a worker whose record stays below the median for a task type, over at least about 10 scored predictions, is benched for that task type. Its record is kept. Benching is per task type, not global.
- **Storage**: the live roster is `abdopus-roster.json`, beside `octopus-ledger.jsonl` in the caller's workspace. If none exists, copy `references/roster.example.json` to that path and edit it there. The skill ships only the example.

## Brief template

```
Task: <one line>
Task type: <type>
Worker: <worker_id@version> (model family: <family>, lens: <lens>)
Role: <worker type>
Context you need: <the minimum>
Deliverables (3-6):
  1. ...
Do NOT redo: <list>
Deterministic check (run before reporting; retry up to 2x locally):
  <exact command or validator>
Predictions (falsifiable, one per line):
  - ...
Open question (max 1, optional): ...
Report format: <schema or fixed headings>
```

## When NOT to use

- **No checkable output.** If checking the answer is as hard as producing it, voting and review add cost without signal. Use one strong model.
- **Cheap models are mostly wrong.** Voting makes that worse. Check the workers' accuracy on a small pilot first. If they are mostly wrong, use the director alone.
- **Tiny one-shot tasks or a single obvious route.** The coordination cost outweighs the gain. Do it directly. Skip bidding too.
- **Fewer than two model families available.** The diversity rules (E5, E8) cannot be met, so agreement means little. Use the director alone, or wait until a second family is available.
- **High-stakes single decisions with no second source.** Forced director review does not replace a human decision. Escalate to a human.

## Example model mapping (Hatz, Nov 2026)

This table is a snapshot for one provider. Re-check model IDs and availability before use. The roles above are the stable part. `references/roster.example.json` uses these IDs.

| Role | Model |
|---|---|
| Director | hatz/anthropic.claude-opus-5-5 |
| Orchestrator | hatz/zai.glm-5.3 |
| One-shot worker | hatz/zai.glm-5.3 |
| Multi-step worker | hatz/anthropic.claude-haiku-5-5 |
| Mechanical sweep worker | hatz/zai.glm-5.2-fast |
| Budget research worker | hatz/deepseek.v4-flash-0731 |
| General worker (alt) | hatz/deepseek.v4-pro-0813 |

When choosing between comparable-tier models, prefer DeepSeek over GPT. Keep at least two model families in any worker set (E5).

For the research basis behind these rules, see `references/evidence.md`.
