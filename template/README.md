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


## Project Entry Points

```text
README.md   → Human entry point
CHATGPT.md  → ChatGPT explicit bootstrap entry point
AGENTS.md   → Codex entry point
```

Shared AI policy lives under `.ai/`.

The workflow uses ChatGPT as Design Owner, Codex A as Implementation Owner, and Codex B as read-only Review Owner. See `.ai/AI_HANDOFF_PROTOCOL.md` and `.ai/GIT_WORKFLOW.md`; use the four artifact templates for Task, Review Prompt, Review Report, and Engineering Result handoffs.

## Project Versioning

Instantiated projects include:

```text
VERSION
CHANGELOG.md
docs/VERSIONING.md
```

The default version for a new project is `0.1.0`.

Existing projects must preserve and reconcile their existing authoritative versioning rather than being reset.

## AI Task Readiness

Before substantive work, AI agents apply `.ai/TASK_READINESS.md`.

```text
PASS     → continue silently
WARNING  → report risk and continue
BLOCKED  → stop substantive work
```
