# Verification

Run `python -m unittest discover -s tests -v` for candidate/release/installation invariants and `python scripts/demo.py` for the full synthetic DD example.

## Initial local result — 18 November 2026

On Windows with Python 3.14, eight lifecycle tests passed. All nine DD route scenarios passed their declared expectations. The authoring skill, generated workflow skill and five generated methods passed the skill frontmatter validator, and their Markdown resource links resolved. A wheel built and imported outside the source checkout, exporting native schemas successfully.

The DD package installed in clean Codex and Claude Code project directories, where its bundled native runtime validated its manifest. The process brief was included after a portability correction. The final replay initially hit a Windows permission error while renaming a staged installation; bounded retry handling was added, tested with an injected transient lock, and the same released package then installed successfully in both clean targets. Existing installation conflicts still fail without replacement.

See [machine-readable results](initial-verification.json). Synthetic review rejection blocks release; synthetic approval cannot create a reviewed release; changed source invalidates a candidate; changed release bytes and conflicting installations are refused. Tests also cover compatible reuse, changed reused content, and incorrect expected outcomes.

The full demo ran before the installation retry fix; its nine route results remain valid, and the corrected installation stage was rerun against that exact release. The complete lifecycle suite was rerun after the fix. This is local Windows evidence, not a claim that hosted Linux/Windows CI passed.

Rehearsal uses supplied task outputs and synthetic decisions. It executes native routing; it does not evaluate legal analysis or prove that a model was invoked. The demo checks installed artifact portability by running its native runtime from clean target folders. Actual fresh-session host discovery and legal-quality evaluation are separate next steps.

The upstream runtime is unmodified. `workbench/resources/runtime.lock.json` records source commit and artifact hash; the original license/notices remain alongside it. Local content hashes are integrity checks, not authenticated third-party signatures.

## Live invocation test, 18 November 2026

The [live invocation test](live-invocation.md) found the root cause of the audit's cross-process failure (owner-only `mkdtemp` staging), fixed it, and added a regression test. It then ran a generated skill, released by a sandboxed session, in a fresh Codex session on three unseen synthetic extracts. Approval and rejection completed under the native runner, every citation matched its source line, and an embedded document instruction was not followed. The lifecycle suite now has nine tests.

## Runtime re-pin

The bundled runtime was later re-pinned to upstream revision `4541864` (artifact SHA-256 `6f37e298…`), which removes non-essential reference text from the runtime's methodology note. Compiler and runner code are unchanged. The lifecycle tests and the demo pass on the new pin. The hashes in `initial-verification.json` record the runtime used at that time.

## Subsequent fresh-host audit

The [installation/invocation audit](host-audit/README.md) adds actual Codex model authoring of a new workflow. It also exposes a limitation the original same-process tests did not catch: a sandbox-created installed package was readable in its creating session but inaccessible to a fresh host scanner. The later generated-skill model turn also failed on a usage limit. A normal-process reinstallation passed native validation, but no fresh sandboxed source-document analysis completed. These findings narrow the portability claim; they do not invalidate the recorded mechanical tests.
