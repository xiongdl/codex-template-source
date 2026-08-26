# Project Template

This directory is the actual project template.

It is intentionally project-agnostic.

## Engineering Goals

Projects instantiated from this template should progressively become:

- Modular
- Extensible
- Testable
- Automated
- Reproducible
- Traceable
- Maintainable
- AI-operable

## Core Workflow

> Understand → Design → Decide → Plan → Implement → Verify → Record → Review → Evolve

## Standard Engineering Entry Point

Where practical:

```bash
./scripts/project setup
./scripts/project build
./scripts/project test
./scripts/project verify
./scripts/project clean
./scripts/project status
```

Human users, Codex, and CI should prefer the same project entry points.

## Verification Hierarchy

```text
components/<component>/tests/
        │
        └── Component-local tests

integration/tests/
        │
        └── Cross-component tests

tests/
        │
        └── Project-level / End-to-End tests
```

A test should live at the narrowest level that fully validates the intended behavior.
