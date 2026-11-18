# Manifest authoring and compilation

Use `schemas/ProcessManifest.schema.json` as the authoritative contract. The bundled `assets/workflow/manifest.json`, when present, is a synthetic example or the packaged workflow, not instructions to apply its business rules to other clients.

1. Create `sources`, `hierarchy`, `objective`, `trigger`, and the process input schema. Sources include locators, concise excerpts, and confirmed/proposed/unresolved status.
2. Create separate `as_is` and `to_be` graphs, each with `version`, `swimlanes`, `nodes`, `edges`, `conditional_edges`, `subprocesses`, and `messages`. Empty collections must be explicit.
3. Add issues, recommendations, metrics, business rules, use-case/function packages, and unresolved questions. Unknown metrics use null. A draft can validate with `--draft`; it cannot compile for execution until unresolved questions/sources are resolved.
4. Define reusable `skills`. Each has stable ID, semantic version, owner, purpose, trigger, instructions, inline input/output JSON Schemas, required capabilities, and approved reusable references. Never copy client data into these definitions.
5. Map every AI/integration task to a skill with identical input/output schemas. Task instructions describe process-specific work; they are not copied into standalone skills. Use `required_capabilities` for abstract capability IDs, not invented tool endpoints.

## Graph conventions

For meaningful labels, visible system references and work products, follow [model-quality.md](model-quality.md). Optional `systems` and `work_products` catalogues belong to each model; activity `system_refs`, `work_products_in`, `work_products_out`, `description` and `responsible_role` retain their business meaning. Branch `label` is readable presentation text; the structured condition still controls execution. The compiler also emits `models/process-guide.md`. Canvas changes must preserve informational references; edit their definitions in the structured blueprint.

- Types: start, end, ai, integration, human, wait, exclusive, parallel_split, parallel_join.
- Give top-level end nodes an `outcome` with `code`, `label`, and `successful` (boolean).
  A completed run only means execution ended; status separately reports `outcomes` and
  `business_success`. Older unlabelled workflows report unknown business success.
- A sign-off that decides whether work proceeds needs an explicit exclusive route.
  A human/wait result alone does not gate its outgoing flow. Test refusal and approval.
- IDs use lowercase letters/digits/hyphens, beginning with a letter, at most 63 characters. IDs for nodes, lanes, edges, messages, and subprocesses are distinct within a model.
- Tasks have `inputs`, `input_schema`, `output_schema`, `instructions`, and `required_capabilities`. Human/wait nodes execute as human; AI/integration nodes execute as agent. Control nodes execute as runner.
- `inputs` maps each task input field to `input.<field>` or `tasks.<node-id>.<output-field>`. Only mapped fields enter the task envelope. Inputs cannot read future/skipped tasks; use separate downstream tasks when branches have different data availability.
- Validation requires declared required source paths and a producer completed on every
  incoming route. Parallel joins combine completed branch outputs; alternative routes
  intersect. Optional source fields cannot be mapped as guaranteed values: map their
  required parent object and handle alternatives explicitly. Common primitive type
  mismatches are rejected; this is not a general JSON Schema subtype proof.
- Normal nodes have one outgoing edge. Exclusive gateways use conditional edges exclusively; each edge has either a `condition` or `default: true`. Multiple matches or missing referenced data stop execution; a default does not hide missing data.
- Conditions use `eq`, `ne`, `lt`, `lte`, `gt`, `gte`, `in` with `path`/`value`; `all`/`any` use `args`; `not` uses `arg`. No code strings or eval.
- Parallel gateways name each other through `pair`. Sibling branches may merge only at that join, and cannot share task nodes. Nested pairs are supported. Each parallel execution uses an instance ID.
- Every node has an implicit `max_visits: 1`. On a rework route, explicitly set the visit limit on every revisited node, including gateways. Limits are 1–100. Exhaustion blocks the run for review.
- An expanded subprocess declares `id`, `name`, `owner`, `entry`, and `exit`. Its members name the subprocess. Entry is a start node with one incoming outer edge; exit is an end node with one outgoing outer edge. Cross-boundary edges use those ports only. Nested subprocess containers are not supported in v1.
- External lanes are black-box participants. `messages` connect an internal node to an external lane; execution waits at an explicit internal `wait` task. Messages alone do not send anything.
- Set `external_effect: true` for any externally mutating action. A successful result then requires a receipt and evidence. Use `allow_human_fallback: true` only when that fallback is part of the proposed blueprint.

## Commands

Here and in the execution guide, `LE` means `python <skill-directory>/scripts/legal-engineering.pyz` (or `python -m legal_engineering` in the source checkout).

```text
LE validate manifest.json --draft
LE validate manifest.json
LE compile manifest.json --out artifacts
LE package artifacts/workflows/<id>/<version> --host codex --out packages
```

Targets are `codex`, `claude-code`, `chatgpt`, and `claude-chat`. Generated packages are deliverables, not automatically installed plugins. To revise behavior, increment workflow and affected skill versions; published versions are immutable. A run pins its complete manifest and skills.
