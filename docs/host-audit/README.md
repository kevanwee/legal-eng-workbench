# Installation and live-host invocation audit

> **Update (same day):** the cross-process `Access is denied` failure below was traced to owner-only `mkdtemp` staging and fixed, and a fresh Codex session then completed source-document analysis with a generated skill. See [live-invocation.md](../live-invocation.md). This page is kept as the original record.

18 November 2026. Tested source commit: `de3a3237f8b976db84ec84e8a7a37e83c1e04e94`. Host: Codex CLI 0.153.4 on Windows, Python 3.14. All matter facts and reviewer decisions are synthetic. No external legal action occurred.

## What actually ran

1. **Skill installation.** The skill-installer fetched `skills/legal-eng-workbench` from the private GitHub repository using its git method and installed it in the user's global Codex skills directory. Existing project-local copies were not used in the fresh readiness working directory.
2. **Fresh readiness invocation.** `Use $legal-eng-workbench` caused the host to read the installed skill. Both `python -m workbench --help` and `legal-workbench --help` failed in that fresh environment. This is a dependency/setup gap, not failed skill discovery.
3. **CLI installation.** A separate project virtual environment received the workbench wheel. Its exact Python interpreter could run the CLI. No global Python package or account setting was changed.
4. **Real model authoring.** A new host invocation read the installed skill, process references and supplied synthetic brief. It authored a new eight-node As-Is/To-Be model and two reusable methods: `prepare-consent-findings` and `record-consent-disposition`. It could inspect the existing DD files for schema structure, but did not replay their scenarios. The three reserved contract extracts were not read.
5. **Rehearsal and release.** Four native-runner scenarios passed: approval, rejection, missing annex and unavailable capability. The task outputs were prewritten synthetic fixtures. Rejected package review correctly refused release; simulated approval allowed a rehearsal release. The authoring session reported matching package bytes and successful installed-runtime validation.
6. **Fresh generated-skill invocation attempt.** A different Codex process logged `failed to scan skill path` with `Access is denied. (os error 5)`. Its turn then failed on the account's usage limit, before any model task work. Independent filesystem reads from the normal process also failed on that installed package. These are two distinct blockers; the usage failure must not be used to explain away the filesystem failure.
7. **Bounded recovery.** From the normal process, the same reviewed candidate was released into a new output directory and installed into a new host directory. File reads and bundled-runtime validation then passed: eight nodes, two skills, no modelling warnings. No previous release was overwritten, no ACLs were changed, and no account upgrade or quota workaround was attempted. Fresh sandboxed model execution was not retested.

## Audit findings

| Finding | Evidence | Consequence / next action |
|---|---|---|
| Skill and CLI installation are separate | Fresh host read SKILL.md; both help commands failed until CLI installation | README now distinguishes both installations and documents an explicit virtual-environment interpreter |
| Global skill is not a self-contained authoring application | Its instructions refer to repository example suites as well as the CLI | Give the host the repository path or package the authoring examples in a future version |
| Model authoring needs iteration | Native validator rejected inconsistent function/method system owners; host corrected the model | Preserve the error and recovery; do not claim one-shot reliable generation |
| CLI refusal code was unclear to the authoring host | Harness expected exit 1; actual rejected release returned 2 | README now documents exit-code meanings |
| Same-session installation check misses a cross-process permission problem | Authoring session could validate files; normal process and new skill scanner could not read them | Add a Windows cross-account install/discovery regression before claiming fresh-host portability |
| Fresh document analysis is not established | Generated-skill turn failed before model work | Retry after account access is available, then score actual citations, missing evidence and document-instruction handling |

The likely permission mechanism is temporary-directory publication. `release` and `install` stage files under `TemporaryDirectory`, then rename the staged tree into place. The local Python `mkdtemp` implementation creates its directory with mode `0o700` and documents access for the creating user only. A directory created by the sandbox identity may therefore retain permissions that are unsuitable for a different host identity after publication. **This is a diagnosis hypothesis supported by the code and observed access difference, not a completed cross-account root-cause regression.** The normal-process reinstall is evidence of a bounded recovery, not a durable fix.

Python documents that Windows handles directory mode `0o700` by limiting access to the current user and administrators, supporting this proposed mechanism. See the official [os.mkdir documentation](https://docs.python.org/3/library/os.html#os.mkdir).

A focused implementation follow-up should test inheritance from the intended destination under the actual host/sandbox identities, preserve atomic publication and conflict refusal, and verify discovery and reading from the receiving host. Do not solve this by broadly opening filesystem permissions or disabling sandboxing.

## What the screenshots show

- [Readiness](readiness.png): observed skill discovery, failed executable checks and the separate CLI installation recovery.
- [Authoring](authoring.png): model-authoring recovery and actual native rehearsal outcomes.
- [Process](model.png): the actual compiler-produced [To-Be SVG](consent-triage.svg), with an explicit partner decision and rejection route.
- [Fresh invocation](invocation.png): scanner access failure, usage-limit failure, and the narrower normal-process recovery.

The first, second and fourth screenshots are browser captures of a labelled evidence document, rendered from recorded CLI results. They are **not native Codex application screenshots**. The process screenshot is a browser rendering of the actual generated artifact. Screenshots were opened and visually inspected for readable text, complete status labels, uncropped output and accurate separation of observed results from limitations.

[evidence.html](evidence.html) is the exact view captured. [results.json](results.json) records outcome classifications, candidate/blueprint identities and raw transcript hashes. [readiness.json](readiness.json) records the initial setup result. [transcript-excerpts.json](transcript-excerpts.json) preserves selected messages with personal workspace paths replaced. Full raw logs and the generated project remain in the local `skill-invocation-audit` directory outside this repository; they are not represented by screenshots alone.

## Reproduce the remaining test

Use the installed `consent-triage` package in a genuinely new host project/session. Supply three text extracts: an express consent requirement, an express change-of-control exception to assignment wording, and a missing schedule containing the relevant terms. Include a document instruction attempting to override the review criteria. Do not provide expected findings or the rehearsal suite to the executing host.

Ask the host to apply the generated methods to the actual files, use native task envelopes, record physical-line citations, and preserve missing evidence. Simulate the partner decisions explicitly and exercise approved internal handoff and rejection separately. Check skill discovery and filesystem access before sending a model request. An internal handoff approval must not be misrepresented as approval of the contracts or absent schedule.

No independent legal-quality, current-law, VDR integration, native app UI, or Claude Code model invocation claim is supported by this audit.
