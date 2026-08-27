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

## Workspace Model

The template is a lean workspace for AI governance, project-level documentation, orchestration, and repository composition. Implementation may live in one or more native child Git repositories. `docs/`, `scripts/`, and `third_party/` are useful conventions; no generic implementation or test directory is prescribed.

If there is no valid Git `HEAD`, `AGENTS.md` automatically routes Codex to `.ai/PROJECT_INIT.md` for Bootstrap and the Initial Commit. Users do not need to request a separate Project Definition task.

## Standard Engineering Entry Point

Where practical:

`./scripts/project status` observes current capability without modification. `./scripts/project verify` validates the currently supported baseline. `setup`, `build`, `test`, and `clean` are enabled incrementally when the real project requires them.

Human users, Codex, and CI should prefer the same project entry points.

## Verification

Preserve child repositories' native build and test structures. Verification should run at the narrowest project-appropriate level and must distinguish supported, unavailable, and not-yet-implemented capabilities.


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
