---
name: factory-rca-recovery
description: Inspect and explicitly recover previously approved failed or stalled RCA runs with the existing Factory administrator session, preserving requester, scope, original discussion and immutable run identities.
---

# Factory RCA recovery

Read `docs/software-factory/runbooks/admin-rca-recovery.md`. Use the supported
helper from the Factory checkout with the existing administrator session. An ops
notice identifies a candidate; it does not grant execution authority.

1. Inspect the supplied original run ID:

   ```bash
   scripts/factory-rca-recovery inspect <run-id>
   ```

2. For an explicit recovery request, use the existing nonsecret worker
   configuration for the intended environment:

   ```bash
   scripts/factory-rca-recovery recover <run-id> --configuration <worker-configuration.json>
   ```

   This verifies fresh STS identity, reserves and stops the predecessor, retries
   retained findings first, and otherwise queues one linked replacement under
   separate admin authorization. It does not request another Slack approval.
   Repeating the same source operation reuses its successor. Report the returned
   IDs and actual delivery state; queued is not completed.

3. If the operator explicitly requests another investigation despite available
   retained findings, add `--replace`. Retry/settle the original publication first.
   Do not infer that prose is complete or blocked from a process exit code.

4. Follow the successor through owner-scoped Factory `get_run`/`get_run_result`.
   A verified original comment does not prove successor findings arrived. Require
   the matching successor publication receipt or report delivery incomplete.

Never edit approval timestamps, clear launch tokens, rewrite IDs, reset terminal
ledger state or replay a completed user investigation. Unknown compute acceptance
must be reconciled with provider evidence before replacement. The eligible failure
window is 24 hours; existing audit/session retention is not shortened. Keep native
sessions and credential material private. Do not send Slack messages as part of
this skill; ops notices come from the configured worker/presenter.

For implementation verification, synthetic initial approval fixtures must be
labeled fixture-origin. Local emulation does not establish real STS, cloud compute,
Linear delivery or live Slack acceptance; use the separately released proof plan.
