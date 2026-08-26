# Changelog

## 1.7.1

- Made `codex-template` itself dogfood the AI engineering workflow defined for instantiated projects.
- Added root `CHATGPT.md` as the explicit ChatGPT bootstrap entry point.
- Added root `AGENTS.md` as the Codex maintainer entry point.
- Added root `.ai/WORKFLOW.md` and `.ai/TASK_READINESS.md`.
- Added a codex-template Maintainer Readiness Profile covering project-agnostic checks, governance/payload boundaries, reference governance, ADR/architecture impact, compatibility, validation, and version impact.
- Formalized ChatGPT/Codex preferred executor routing for template maintenance.
- Added `tests/validate_repository_governance.py`.
- Extended `./scripts/check` to validate root project governance in addition to template and reference validation.


## 1.7.0

- Added explicit ChatGPT project bootstrap through `template/CHATGPT.md`.
- Added shared `AI Task Readiness Protocol` with `PASS`, `WARNING`, and `BLOCKED`.
- Added ChatGPT and Codex readiness profiles.
- Added instantiated-project versioning and default project version `0.1.0`.
- Added `template/VERSION`, `template/CHANGELOG.md`, and `template/docs/VERSIONING.md`.
- Added Preliminary/Final Version Impact flow using `NONE`, `PATCH`, `MINOR`, `MAJOR`, and `UNKNOWN`.
- Added version discovery and version-source conflict handling to project initialization.
- Added `docs/VERSIONING.md` for `codex-template` itself.
- Extended template validation to enforce bootstrap, readiness, and versioning invariants.


## 1.6.0

- Formalized Reference Governance responsibilities across Human, ChatGPT, and Codex.
- Defined Human-maintained snapshots as primary evidence and notes/indexes as derived artifacts.
- Added `references/openai/notes/NOTE_TEMPLATE.md` for reproducible reference reviews.
- Required every Gap Analysis to pin an exact repository commit and template version.
- Standardized decisions as `No Change`, `Monitor`, or `Change Proposed`.
- Required approved `Change Proposed` outcomes before upstream evidence may drive template changes.
- Extended reference validation to enforce governance artifacts and note-template structure.


## 1.5.0

- Changed OpenAI reference maintenance to human-curated snapshots only.
- Removed automated OpenAI web fetching/change detection.
- Added strict snapshot source-directory, metadata, filename, date, extension, and URL validation.
- Added `tests/validate_references.py`.
- Added canonical repository validation entry point `./scripts/check`.
- Formalized snapshot evidence as primary input and SOURCES/notes as derived maintenance artifacts.


## 1.4.0

- Added `references/openai/` as a curated upstream-evidence layer.
- Added an official OpenAI source registry and initial analysis baseline.
- Added `scripts/check_openai_references.py` for conservative upstream change detection.
- Formalized the Source → Insight → Decision → Template Change workflow.
- Explicitly prevents upstream changes from automatically modifying the distributable template.


## 1.3.0

- Split the repository into a distributable `template/` payload and a template-governance layer.
- Added template design principles, architecture, change policy, and ADRs.
- Added automated validation for required structure and project-agnostic content.
- Formalized the verification hierarchy:
  - component-local tests,
  - cross-component tests,
  - project-level / end-to-end tests.
- Preserved the unified project automation entry-point convention.
