# Third-party resources

The offline runtime includes private copies of:

- jsonschema 4.17.3 — MIT license.
- attrs 25.4.0 — MIT license.
- pyrsistent 0.20.0 — MIT license.

Their license texts and package metadata are preserved in `legal_engineering/resources/vendor/`. Versions and checksums are recorded in `legal_engineering/resources/portable-dependencies.json`.

The BPMN XSDs are the OMG-published machine-readable resources for BPMN 2.0.2. Original headers are preserved; source URLs/checksums are in `legal_engineering/resources/bpmn-xsd/provenance.json`.

bpmn-js and Playwright are development-only independent verification tools, not dependencies of the distributed Python runner.
