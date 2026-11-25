# Recover a failed or stalled RCA as Factory admin

Implementation status: **local candidate, not commissioned**. The supported CLI
inspects, stops and recovers eligible work. Pre-merge acceptance is local fault
tests and offline template/deployment tests. Effective IAM and one bounded real
recovery proof follow the single reviewed merged deployment and worker installation.
Historical original/R3 attempts remain FAIL with causes UNKNOWN; supplemental
existing-comment evidence used a local snapshot ledger, not real DynamoDB CAS.
Existing retained fixture debt is excluded from new acceptance and remains unresolved.

## Trigger and prerequisites

Use for previously approved RCA work that failed or stopped making progress.
An inspection candidate is not execution authority. Mutations require fresh STS
verification of the existing Factory administrator role, plus the existing worker
configuration for the intended environment. Never substitute a profile name or
caller-supplied operator string for verified identity.

The existing Factory D1 administrator access is sufficient; no new permission set
or credential workaround is required. The launch role must trust the exact
configured SSO role, in addition to the unchanged worker principal. Fresh STS alone
does not prove target trust, SCP/boundary permission or successful client construction.

Before reserving or stopping a run, verify `FACTORY_COMPUTE_ROLE_ARN` trusts the
configured administrator's IAM role ARN, not its STS session ARN. Do not clear that
setting or substitute credentials to bypass a failed assumption. See
[coding-shell configuration](coding-shell.md#configure-the-consumer) for the exact
principal format and role-recreation procedure.

| Trust configuration                                         | Worker                   | Administrator                                            |
| ----------------------------------------------------------- | ------------------------ | -------------------------------------------------------- |
| Admin parameter absent or empty                             | Existing trust preserved | No added trust                                           |
| Exact approved admin role configured                        | Existing trust preserved | Only that role receives the added `sts:AssumeRole` trust |
| Different or unrelated caller                               | Existing trust preserved | No grant from the configured admin statement             |
| Wildcard, wrong-account, non-admin or session ARN parameter | No intended change       | Template input rejected                                  |

## Single deployment and post-install acceptance

Follow [Coordinated API/worker update](deploy-dev-mcp.md#coordinated-apiworker-update)
for fresh inventory, admission pause, queued/DLQ disposition, drain and worker stop.
Do not substitute historical counts, a healthy unit or approximate queue size for
that evidence. Jimmy attends; no unknown active work may be carried through install.
For this release use the attended operator command below instead of a second
workflow deployment. Both operate on the same reviewed merged Development SHA.
The existing automatic push workflow refuses a changed worker pin before control
deployment without attended workflow-dispatch confirmation. Do not dispatch that
workflow alongside this local cutover or broaden its privileges to update guest trust.
The option forwards `FactoryControlStack:WorkerRevision` to that SHA, preserves
existing control parameters and excludes bootstrap/self-trust. It updates only the
existing guest stack's reviewed admin trust; it never creates that stack.

Commands below are a deployment-time checklist, not authorization to execute now.
Set `MERGED_SHA` to the exact reviewed first-parent `dev` commit and `RECEIPTS` to
the approved private cutover directory. Retain previous API/worker revisions,
configuration and clean checkout there before starting.

```bash
AWS_PROFILE=factory-admin scripts/factory-deploy-local.sh --confirm "$MERGED_SHA" --include-admin-recovery-trust --worker-cutover-confirmed --dry-run
AWS_PROFILE=factory-admin scripts/factory-deploy-local.sh --confirm "$MERGED_SHA" --include-admin-recovery-trust --worker-cutover-confirmed
aws --profile factory-admin cloudformation describe-stacks --region us-east-1 --stack-name FactoryControlStack --query 'Stacks[0].Outputs' --output json > "$RECEIPTS/control-outputs.json"
jq -e --arg sha "$MERGED_SHA" 'map({key:.OutputKey,value:.OutputValue}) | from_entries | .FactoryApiRevision == $sha and .FactoryWorkerRevision == $sha' "$RECEIPTS/control-outputs.json"
jq -er '.[] | select(.OutputKey == "FactoryWorkerConfiguration") | .OutputValue' "$RECEIPTS/control-outputs.json" > "$RECEIPTS/worker-config.json"
```

Compare the configuration and Docs policy digest to the saved values. From a clean
checkout at that exact SHA on the existing worker host, use frozen dependencies
and the normal installation path; the config path must be absolute under `/workspace`.

```bash
uv sync --project mcp_services/factory_mcp_py --frozen --no-dev
scripts/factory-mcp-worker check "$RECEIPTS/worker-config.json"
scripts/factory-mcp-worker install "$RECEIPTS/worker-config.json"
scripts/factory-mcp-worker status
systemctl show factory-mcp-worker --property=ExecStart,WorkingDirectory,User
git rev-parse HEAD
sha256sum "$RECEIPTS/worker-config.json"
journalctl -u factory-mcp-worker --since '5 minutes ago' --no-pager
```

Require installed paths/HEAD/config digest to match the read-back API and worker
pin, then fresh IAM trust/client and unchanged worker-path checks. Keep credential
responses private and do not print tokens. Restore only the already authorized
internal admission cohort, then conduct **one** bounded recovery proof with a new
explicitly approved run ID, budget, destination and cleanup owner. Exclude the old
R3 fixture. Use supported commands against the installed configuration:

```bash
AWS_PROFILE=factory-admin scripts/factory-rca-recovery inspect "$PROOF_RUN_ID"
AWS_PROFILE=factory-admin scripts/factory-rca-recovery stop "$PROOF_RUN_ID" --configuration "$RECEIPTS/worker-config.json"
AWS_PROFILE=factory-admin scripts/factory-rca-recovery recover "$PROOF_RUN_ID" --configuration "$RECEIPTS/worker-config.json"
```

Acceptance requires actual fenced stop/revocation/custody, useful original findings,
correct original/successor/operation identity and provider readback, persisted receipt,
and exact cleanup evidence. A new execution requires its explicit proof budget;
no automatic extra attempt is implied. Pause admission on failure and preserve
unknown launch/custody/persistence debt. Ops destination/membership and human inbox
observations remain independent gates, not inferred from local tests.

For rollback, review a normal commit setting `FactoryAdminRoleArn` to `""` in
`stack-config.json`; after merge run the same attended dry-run/deploy path. Empty is
forwarded explicitly, never `UsePreviousValue`. The worker trust and all other
stack parameters remain unchanged. Removing trust does not revoke existing sessions
or settle retained cleanup debt. Revert incompatible runtime through the normal
coordinated API/worker procedure, not by installing mismatched revisions.

## Steps

With the existing Factory admin session checked out in `us-east-1`, from this repo:

```bash
scripts/factory-rca-recovery inspect <run-id>
```

This command verifies the existing Factory administrator session, consistently reads
one run from `factory-phase2-runs`, and prints bounded JSON. It does not include the
request contents or credentials and does not change the run or contact Linear.

- `failed`: approved failure within the 24-hour recovery window.
- `stalled`: approved work has no observed progress for at least 15 minutes.
- `timing_unproven`: timestamps are absent or invalid; inspect evidence before acting.
- Other reasons describe why this run is not a recovery candidate.

Heartbeat updates, polling and reconciliation do not count as progress. The
24-hour window is measured from recorded failure and does not shorten existing
audit retention. Never-approved, denied, cancelled and pre-execution-expired work
remain excluded. A successful investigation's Linear delivery must be checked
through the ENG-4100 handoff path, not inferred from this classifier.

Do not manually edit approval timestamps,
clear launch evidence, enqueue a replacement, or fabricate a consumed approval.
To recover eligible work using this source candidate:

```bash
scripts/factory-rca-recovery recover <run-id> --configuration <worker-configuration.json>
```

It retries retained findings first. A usable screened final draft can be delivered
when an interrupted execution saved no separate report; the comment explicitly
states that investigation completion is unverified. Invalid or credential-bearing
retained content is not published. Without retained findings, it settles the
original publication and creates one linked replacement under explicit admin
authorization. The replacement follows the ordinary dispatch/Worker path with
the original requester and scope. To explicitly request a fresh investigation even
when findings are retained, add `--replace`; the original discussion is preserved.
Read the returned status: `delivered` proves handoff readback; `replacement_queued`
requires following that successor to its own actual result and delivery receipt.

To reserve and stop without queuing a successor:

```bash
scripts/factory-rca-recovery stop <run-id> --configuration <worker-configuration.json>
```

The receipt includes the immutable recovery operation ID. Repeating the operation
reuses its reservation. Confirmed stop preserves original approval and scope,
fences the former worker, and records cleanup; it does not launch a successor or
rewrite a successful outcome. Unknown launch acceptance remains unresolved until
actual compute evidence is available; never clear a launch token to force recovery.

## Linear delivery policy

Retry screened retained findings before running Pi again. Original binding and
Linear context stay together in private root-delivery custody, separate from every
successor execution binding. Preserve the original final comment and stable ID.
If successor findings create that absent final, no extra follow-up is needed. If
the original final already exists, publish one labeled recovery follow-up with a
stable successor/operation-derived ID, both run IDs and the original comment link.
Include actual findings and limitations; a partial or blocked answer is not complete.

An existing root receipt does not establish delivery of successor findings. An
existing follow-up with matching successor provenance can settle its own lost
response. Preserve earlier discussion; never overwrite a report or infer usefulness
from an identity-only readback. This policy is approved; it is not awaiting a new
product decision.

## Ops commissioning

Configure a separately verified private `ops_channel_id` in the existing Slack
configuration. Keep the approval channel pinned. Bot membership and the actual
ops destination must be verified before enabling delivery; the approvers channel
is not a substitute. A sending/uncertain receipt must not be blindly reposted.
Local virtual-time tests prove the 15-minute threshold and message updates, not
live Slack acceptance. A separately authorized fixture message and installed
requester/admin acceptance remain rollout gates.

## Verification without a Factory deployment

From `mcp_services/factory_mcp_py`, install `uv sync --group test --group dev`,
then run:

```bash
uv run pytest tests/test_admin_recovery.py tests/test_admin_replacement.py tests/test_recovery_custody.py tests/test_ops_notices.py tests/test_run_recovery.py -q
uv run python -m tests.admin_recovery_drive
```

The drive rig starts an ephemeral loopback AWS emulator, seeds a synthetic approved
RCA, and runs the actual shell command with emulated administrator credentials.
It checks stalled output, malformed IDs, refusal of unsupported replacement and
explicit stop with preserved original approval/scope, then stops the emulator.
It clears inherited AWS configuration;
no real credentials, cloud resources or product stack are needed. This proves
the inspection/stop command boundary, not real STS, Pi recovery or Linear publication.

## Rollback

Stop initiating new recoveries. Preserve recovery intents, immutable links, retained
findings and publication receipts. Never roll back to a worker that ignores a
reserved predecessor or remove fencing metadata to resume it. Stopping compute is
not reversible by rewriting its old terminal ledger; any replacement must follow
the authorized linked recovery path.

## Related

- [Admin authority](../adr/0054-authorize-rca-recovery-through-factory-admin.md)
- [Recovery identity and publication](../adr/0055-link-superseded-rca-runs-without-rewriting-identity.md)

## Recovery reconciliation states

- `investigation_cleanup_custody_missing`: the VM may be stopped, but source-token
  revocation/private credential cleanup is unproven. Preserve the reservation and
  original evidence; reconcile the original host/capability. Do not force cleanup
  to confirmed or clear the launch record.
- `workflow_manifest_changed`: the configured worker cannot execute the admitted
  historical manifest. No successor is linked. Reconcile supported worker/source
  compatibility before retrying; do not rewrite the admitted manifest.
- `retained_findings_require_reconciliation`: useful ledger or old private findings
  exist without validated delivery custody. Preserve and reconcile them. An explicit
  `--replace` authorizes fresh investigation; the default must not infer that choice.
- `recovery_delivered`: receipt-bound findings were delivered; the original failed
  execution remains failed. For report-only successors, use the same admin
  `recover <successor-id> --configuration ...` command, not the ordinary root-only
  `app.rca_linear` retry.

A stale update claim with a known Slack message can update that same message after
60 seconds using a conditional claim. Unknown initial-send acceptance is never a
reason to post another notice. These local rules do not commission the private ops
channel or prove live notification delivery.
