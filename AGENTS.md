# AGENTS.md — codex-template Maintainer Instructions

This repository develops and maintains the distributable project template under `template/`.

Codex must treat `codex-template` itself as a governed engineering project.

## Before Substantive Work

Apply `.ai/TASK_READINESS.md` using the Codex profile.

Then inspect, as relevant:

1. `docs/DESIGN_PRINCIPLES.md`
2. `docs/TEMPLATE_ARCHITECTURE.md`
3. `docs/CHANGE_POLICY.md`
4. `docs/VERSIONING.md`
5. relevant ADRs
6. relevant reference notes/evidence
7. affected repository files and tests

## Preferred Role

Codex is primarily responsible for repository inspection, approved implementation, repository consistency, validation, Final Version Impact, and release preparation.

Research-heavy or architecture-defining work should normally arrive as an approved design or change proposal.

## Task Readiness

- `PASS` normally remains silent.
- `WARNING` must be surfaced when risk exists but no material user decision is required.
- `BLOCKED` must stop substantive execution.

Do not implement a change that violates the project-agnostic design principle, confuses governance with distributable payload, bypasses required reference review, introduces an unauthorized breaking change, or cannot be meaningfully verified.

## Repository Boundary

`template/` is the distributable product.

Root-level `docs/`, `references/`, `scripts/`, `tests/`, `VERSION`, and `CHANGELOG.md` govern and validate `codex-template` itself.

## After Implementation

When applicable:

1. run `./scripts/check`,
2. update relevant tests,
3. update governance docs,
4. update ADRs when architecturally material,
5. report Final Version Impact,
6. update `CHANGELOG.md`,
7. update `VERSION` when preparing a release.

Do not claim verification that was not performed.
