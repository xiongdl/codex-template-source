# Changelog

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
