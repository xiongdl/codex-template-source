# AGENTS.md

This repository follows an AI-assisted engineering workflow.

## Engineering Goals

Changes should move the project toward:

1. Modular
2. Extensible
3. Testable
4. Automated
5. Reproducible
6. Traceable
7. Maintainable
8. AI-operable

## Core Workflow

Understand
→ Design
→ Decide
→ Plan
→ Implement
→ Verify
→ Document
→ Record
→ Review

## Before Modifying Code

1. Read `docs/ARCHITECTURE.md`.
2. Read `docs/PROJECT_STATUS.md`.
3. Read `docs/REPRODUCIBILITY.md` when environment/build/result reproduction matters.
4. Identify affected component(s).
5. Read the nearest component `AGENTS.md` if present.
6. Read relevant design, decision, and integration docs.
7. Inspect implementation, tests, automation, and configuration.
8. Identify existing invariants.

Do not infer architectural intent solely from code.

## Modularity

Prefer meaningful responsibility and dependency boundaries.

A component boundary should be a real engineering boundary, not only a directory boundary.

## Extensibility

Prefer stable interfaces, composition, and replaceable components.

Avoid unnecessary coupling to another component's internal implementation.

## Testability

Distinguish clearly between implemented, tested, partially verified, and not verified.

Never claim verification that was not performed.

## Test Placement

```text
components/<component>/tests/  → Component-local tests
integration/tests/             → Cross-component tests
tests/                         → Project-level / End-to-End tests
```

Place tests at the narrowest level that fully validates the behavior.

## Automation

Repeated workflows should be automated where practical.

Prefer project-standard entry points under `scripts/`.

## Reproducibility

Setup, dependencies, configuration, build, tests, and important outputs should be reconstructable from repository-contained information.

## Traceability

Use:

- `docs/design/`
- `docs/decisions/`
- `docs/integration/`
- `docs/PROJECT_STATUS.md`

for durable engineering knowledge.

## Maintainability

Prefer scoped, understandable changes.

Avoid hidden coupling, duplicated conventions, unexplained configuration, and unnecessary framework complexity.

## AI Operability

A new Codex session should be able to determine:

- what the project is,
- how it is structured,
- how to build/test/verify it,
- what is currently in progress,
- why important decisions were made.

Important project knowledge must not exist only in conversation history.

## After Implementation

When applicable:

- run relevant project-standard checks,
- update tests,
- update design/integration docs,
- record significant decisions,
- update `docs/PROJECT_STATUS.md`,
- update reproducibility docs if setup/configuration changed.

Report commands actually executed and verification results.
