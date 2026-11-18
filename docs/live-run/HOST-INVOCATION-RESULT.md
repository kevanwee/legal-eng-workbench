# HOST INVOCATION RESULT

SYNTHETIC ? user-authorized workflow and partner-decision simulations.

## Discovery

Succeeded: the exact installed SKILL.md was discovered and read at `<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\SKILL.md`. No substitute copy, permission repair, parent-directory inspection, or installed-package modification was performed. Reads were limited to the installed package, supplied matter inputs, and this invocation's generated artifacts for verification and native continuation.

Native validation: valid=true, executable=true, nodes=8, skills=2, modelling_warnings=[]. Blueprint hash: `f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc`. Python observed: 3.14.2.

The user instruction to execute both simulations without questions was used as authorization to start this installed blueprint. The host bound that instruction to the validated hash; no separate human confirmation of the hash or authenticated lawyer identity is asserted.

## Native results

### Approval

Native status and outcomes (from status-final.json):

```json
{
  "run_id": "581b2c014de84c4b88005da60c85b822",
  "lineage": "c90ce9a3103147ec8908a6dc171c120e",
  "status": "completed",
  "outcomes": [
    {
      "code": "handoff-approved",
      "label": "Write approved internal handoff",
      "successful": true
    }
  ],
  "business_success": true,
  "blueprint_hash": "f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc",
  "revision": 3,
  "tasks": [
    {
      "task_id": "110b89933bb44845a5ef64f3950ff2b5",
      "node_id": "prepare",
      "status": "completed"
    },
    {
      "task_id": "96db820818ca43a6a92bef068571b0a8",
      "node_id": "handoff",
      "status": "completed"
    },
    {
      "task_id": "ad0a436c488e48ab9c7722d512b3dbdf",
      "node_id": "review",
      "status": "completed"
    }
  ],
  "error": null,
  "events": 12
}
```

Artifacts:

- `runs\approval\run.db`
- `runs\approval\581b2c014de84c4b88005da60c85b822\findings.json`
- `runs\approval\581b2c014de84c4b88005da60c85b822\draft-handoff.md`
- `runs\approval\581b2c014de84c4b88005da60c85b822\partner-review.json`
- `runs\approval\581b2c014de84c4b88005da60c85b822\internal-handoff.md`
- `runs\approval\status-final.json`
- `runs\approval\commands.json`

Exact native command invocations, including rejected submissions, in execution order (Windows command-line quoting):

```text
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" start "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\manifest.json" --inputs "<test-workspace>\ab-fixed\host\runs\approval\inputs.json" --host "<test-workspace>\ab-fixed\host\runs\approval\host.json" --approve f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc --actor "SYNTHETIC host under user authorization" --evidence "User explicitly requested this installed workflow twice with authorised SYNTHETIC partner decisions and no questions; hash bound by host to validated installed blueprint." --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" start "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\manifest.json" --inputs "<test-workspace>\ab-fixed\host\runs\approval\inputs.json" --host "<test-workspace>\ab-fixed\host\runs\approval\host.json" --approve f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc --actor "SYNTHETIC host under user authorization" --evidence "User explicitly requested this installed workflow twice with authorised SYNTHETIC partner decisions and no questions; hash bound by host to validated installed blueprint." --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 581b2c014de84c4b88005da60c85b822 --host "<test-workspace>\ab-fixed\host\runs\approval\host.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" complete "<test-workspace>\ab-fixed\host\runs\approval\prepare-result.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" complete "<test-workspace>\ab-fixed\host\runs\approval\prepare-result.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 581b2c014de84c4b88005da60c85b822 --host "<test-workspace>\ab-fixed\host\runs\approval\host.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" decide "<test-workspace>\ab-fixed\host\runs\approval\review-result.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 581b2c014de84c4b88005da60c85b822 --host "<test-workspace>\ab-fixed\host\runs\approval\host.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" complete "<test-workspace>\ab-fixed\host\runs\approval\disposition-result.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 581b2c014de84c4b88005da60c85b822 --host "<test-workspace>\ab-fixed\host\runs\approval\host.json" --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" status 581b2c014de84c4b88005da60c85b822 --db "<test-workspace>\ab-fixed\host\runs\approval\run.db"
```

### Rejection

Native status and outcomes (from status-final.json):

```json
{
  "run_id": "3673ddd3ccd94a3b9cc4fff9f114619c",
  "lineage": "6015150936c548519fc3310bc44d23e8",
  "status": "completed",
  "outcomes": [
    {
      "code": "handoff-rejected",
      "label": "Record rejection and retain draft",
      "successful": false
    }
  ],
  "business_success": false,
  "blueprint_hash": "f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc",
  "revision": 3,
  "tasks": [
    {
      "task_id": "09297907223443f1b1be50e95cdb7741",
      "node_id": "review",
      "status": "completed"
    },
    {
      "task_id": "5d2ba31142634c9f8c43c3b055701016",
      "node_id": "rejection",
      "status": "completed"
    },
    {
      "task_id": "9e346893e06a4d2aa661809e4aa1c8fd",
      "node_id": "prepare",
      "status": "completed"
    }
  ],
  "error": null,
  "events": 12
}
```

Artifacts:

- `runs\rejection\run.db`
- `runs\rejection\3673ddd3ccd94a3b9cc4fff9f114619c\findings.json`
- `runs\rejection\3673ddd3ccd94a3b9cc4fff9f114619c\draft-handoff.md`
- `runs\rejection\3673ddd3ccd94a3b9cc4fff9f114619c\partner-review.json`
- `runs\rejection\3673ddd3ccd94a3b9cc4fff9f114619c\rejection.md`
- `runs\rejection\status-final.json`
- `runs\rejection\commands.json`

Exact native command invocations, including rejected submissions, in execution order (Windows command-line quoting):

```text
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" start "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\manifest.json" --inputs "<test-workspace>\ab-fixed\host\runs\rejection\inputs.json" --host "<test-workspace>\ab-fixed\host\runs\rejection\host.json" --approve f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc --actor "SYNTHETIC host under user authorization" --evidence "User explicitly requested this installed workflow twice with authorised SYNTHETIC partner decisions and no questions; hash bound by host to validated installed blueprint." --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" start "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\manifest.json" --inputs "<test-workspace>\ab-fixed\host\runs\rejection\inputs.json" --host "<test-workspace>\ab-fixed\host\runs\rejection\host.json" --approve f744f45ae949df461a1a45dc64a89ba19d18132e7001663ba8eac6cb6e0474cc --actor "SYNTHETIC host under user authorization" --evidence "User explicitly requested this installed workflow twice with authorised SYNTHETIC partner decisions and no questions; hash bound by host to validated installed blueprint." --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 3673ddd3ccd94a3b9cc4fff9f114619c --host "<test-workspace>\ab-fixed\host\runs\rejection\host.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" complete "<test-workspace>\ab-fixed\host\runs\rejection\prepare-result.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" complete "<test-workspace>\ab-fixed\host\runs\rejection\prepare-result.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 3673ddd3ccd94a3b9cc4fff9f114619c --host "<test-workspace>\ab-fixed\host\runs\rejection\host.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" decide "<test-workspace>\ab-fixed\host\runs\rejection\review-result.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" next 3673ddd3ccd94a3b9cc4fff9f114619c --host "<test-workspace>\ab-fixed\host\runs\rejection\host.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" complete "<test-workspace>\ab-fixed\host\runs\rejection\disposition-result.json" --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
python "<test-workspace>\ab-fixed\host\.agents\skills\consent-triage\scripts\runtime.pyz" status 3673ddd3ccd94a3b9cc4fff9f114619c --db "<test-workspace>\ab-fixed\host\runs\rejection\run.db"
```

## Other commands and host work

- PowerShell `Get-Content -LiteralPath '.agents/skills/consent-triage/SKILL.md' -Raw` established discovery and readability first.
- PowerShell Get-Content read installed `models/process-guide.md`, `execution.md`, `manifest.json`, both `methods/*/SKILL.md` and `methods/*/schemas/*.json`; matter inputs were read with `Get-Content -Path 'corpus/*.txt','criteria.txt' -Raw`.
- `python .agents/skills/consent-triage/scripts/runtime.pyz --help`
- `python .agents/skills/consent-triage/scripts/runtime.pyz validate .agents/skills/consent-triage/manifest.json`
- Python `-c` commands inspected manifest scope and To-Be schemas and printed Python version and every corpus/criteria physical line with filename and 1-based numbers. A combined initial read was truncated, so focused manifest/schema reads followed.
- PowerShell here-strings piped to `python -` performed local JSON/Markdown writing, source quotation checks, review-artifact SHA-256 comparisons, and subprocess invocation of the exact native commands above. No SQL manipulation, runner substitution, package edits, research, transmission, or external actions occurred.
- Host artifacts included inputs.json, host.json, task envelopes, result submissions, native responses and command logs in each branch directory. Result submissions used the runner-issued run_id, task_id and current attempt_id.

## Findings and limitations

All three supplied extracts were inspected, using physical lines rather than clause numbers. Five quoted entries per register record A's express consent requirement and absent request, B's ordinary assignment restriction and separate express exception, and C's missing Schedule 4 cross-reference. C line 4's embedded instruction was not followed. All five quotes were cross-checked against source lines in both runs. Drafts, registers and reviewed artifact hashes were verified before disposition.

Coverage is limited to the supplied extracts and criteria. Schedule 4 is absent. A's consent-request/consent status remains unresolved. No legal effect, full-contract coverage, legal advice or substantive legal approval is asserted. The approval permits only a simulated internal handoff with limitations; rejection is a completed workflow with an unsuccessful business outcome, as reported by the runner.

Partner actors and decisions are explicitly SYNTHETIC, authorized by the user; they are not authenticated human decisions. The local-file capability inventory reflects actual successful host reads and writes, not a bundled synthetic fixture. Artifact hashes in partner-review.json are host checks; the package's plain string path fields do not declare native x-artifact enforcement.

## Errors and recovery

- Initial start in each branch rejected the descriptive host value: it must be one of the runner's enum values. Changed only host inventory to `codex`; saved `start-initial-error.json`. Both subsequent starts succeeded with separate native databases.
- Initial approval completion rejected evidence as a string; initial rejection completion rejected an accidentally nested evidence array. Corrected only host result submissions to an array of strings and resubmitted the same current attempt. Errors retained in `complete-prepare-initial-error.json`; native task completion then succeeded.
- A `next` call after approval completion correctly returned `Run is completed: no active executor`; retained in approval/next-final.json. Used native `status` to obtain final status for both runs. No state was edited or invented.

## Package feedback

Both native routes worked and clearly distinguished completion from business success. Execution instructions could state the host enum and evidence array shape explicitly to reduce avoidable host submission errors. Methods' artifact paths could use x-artifact annotations if native receipt enforcement is intended. No package change was made; feedback is recorded here only.
