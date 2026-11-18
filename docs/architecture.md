# Scope and architecture

The workbench owns the authoring lifecycle: brief, host-authored model, explicit method resolution, candidate build, rehearsal receipt, review, immutable release and host installation. The active agent host supplies reasoning, source retrieval, tools and interaction with the lawyer.

The bundled `legal-processmodelling-meta-skill` zipapp owns manifest validation, compilation, BPMN generation, execution state, routing, decisions and checkpoints. It is pinned by source commit and artifact SHA-256 in `workbench/resources/runtime.lock.json`. Its MIT license and third-party notices are retained. No second workflow engine or server is introduced here.

`model` imports a host-authored canonical manifest. It does not convert prose to a legal process autonomously. `resolve` can generate declared methods or reuse a supplied folder with an exact matching definition. Automatic skill search, semantic compatibility and adapters are future work. `build` assembles one self-contained discoverable workflow skill, with its methods under `methods/` and its native runtime under `scripts/`.

Candidate digests cover source identities and generated package bytes. Rehearsal uses the native runner with explicitly supplied synthetic outputs. Review and rehearsal bind to the candidate. Release requires both passing rehearsal and approval. Changed source/method/package content invalidates the candidate. Published workflow/version directories cannot be replaced. Candidates, releases and installations are staged in a sibling folder created with an ordinary `mkdir`, so they inherit the destination's permissions, and are then renamed into place atomically. Owner-only `mkdtemp` staging is avoided because its ACL survives the rename and hides packages from other host identities. Installation refuses conflicts and never overwrites a different installed skill. Local hashes detect changes; they are not signatures against an adversarial local owner.

The rehearsal channel is the default. A synthetic model or decision cannot create a reviewed release. Reviewed still means recorded review, not independent legal certification. Identity is an attestation supplied by the user/host. Team accounts, portals, VDR services, enterprise authorization and matter-management screens are outside this product's initial scope.

Only Codex and Claude Code project-folder installation is implemented. The ZIP is a portable skill artifact, not an automatically registered plugin. Invocation text is a handoff to the active host, not evidence that a model ran. Record actual host evaluation separately from scripted rehearsal.

The DD example remains in this repository until independent ownership, maintenance or distribution justifies a separate package repository. Its fixture is intentionally labelled Stage 3 and synthetic. Do not promote string-reference rehearsals into claims of document processing or legal quality.
