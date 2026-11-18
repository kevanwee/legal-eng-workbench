# A process model that explains the work

Model the whole **declared process boundary**: its business trigger, participants,
handoffs, normal completion, refusal outcomes, waiting, rework and unresolved work.
Do not imply that completing an initial response resolves the whole legal matter.

## Read the diagram as an operator

- Activity names say what someone does to what: **Reconcile affected-person counts
  against the incident reports**, rather than **Extract**. Use business vocabulary.
- Exclusive gateways ask a concrete question, such as **Is the evidence sufficient
  for legal assessment?** Give each conditional edge a short `label` expressing
  the answer and consequence. Keep the structured `condition` as executable truth.
- Name start events after the triggering business event and end events after the
  actual outcome. Name parallel gateways after the work they open or synchronise.
- `description` explains a task's purpose and business handoff. `instructions`
  states what to inspect, what to produce, how to handle missing evidence and who
  retains authority. Do not reuse generic instructions for unrelated activities.

## Participants, systems and work products

Optional model `systems` records have `id`, `name`, `description`. Work products
have those fields plus `kind`: `document` or `data_store`. Activities reference
them using `system_refs`, `work_products_in` and `work_products_out`.

When the systems catalogue is present, validation checks the performer:

- Manual work stays in a human lane and has no system reference.
- Interactive work stays in the human lane and identifies the system used.
- Automated work stays in a system lane, identifies its systems, and names an
  internal human `responsible_role`. System execution does not confer decision
  authority on the system. Host-operated AI preparation is labelled as such.

Systems are shown as labelled BPMN annotations. Work products appear as standard
data-object/data-store references with directional informational associations.
These references are descriptive. They do not establish an integration, create
a document, execute a timer, or replace task input/output evidence contracts.
Use external pools and message flows for actual external participants; a software
tool used by a participant is not automatically a counterparty or a separate pool.

## Review and edit

Use the emitted `process-guide.md` to inspect every node's performer, instructions,
systems, work products and next routes. Provide an overview and readable detail
views for long processes. Do not rely on a fitted thumbnail for substantive review.

Short labels and gateways without questions produce nonblocking modelling warnings
so older releases remain usable. Passing validation does not prove a meaningful
business model: the owner still reviews scope, wording, evidence and outcomes.

Edit systems/work products in the structured blueprint. The bounded canvas editor
preserves these references and refuses silent deletion or alteration. Work-product
references inside expanded subprocesses currently require a separate detailed model.
Do not silently turn informational artifacts into executable capabilities.

For revisions, use a new workflow version, inspect its changed blueprint, rerun
acceptance and take the appropriate design/release decisions. Keep prior versions.
