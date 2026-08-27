# codex-template AI Engineering Workflow

## Purpose

`codex-template` dogfoods the same core AI engineering workflow it provides to instantiated projects while retaining its maintainer responsibilities.

## Ownership

- ChatGPT = Design Owner
- Codex A = Implementation Owner
- Codex B = Review Owner

Detailed task, handoff, review, and status contracts are in `.ai/AI_HANDOFF_PROTOCOL.md`. Reproducible branch, review-target, and integration rules are in `.ai/GIT_WORKFLOW.md`.

## Standard Flow

```text
Human Goal
    ↓
ChatGPT / Design Owner
    ↓ requirements, decisions, Task Contract
Codex A / Implementation Owner
    ↓ readiness, task branch, implementation, verification, commit
Codex B / Review Owner
    ↓ read-only Independent Review
APPROVED ──────────────── CHANGES_REQUESTED
    ↓                         ↓ fix, verify, commit, re-review
ff-only local integration ←───┘
    ↓
Engineering Result Report to ChatGPT
```

Task Type is immutable and limited to `READ_ONLY` and `CHANGE`. A `CHANGE` requires committed-state Independent Review and approval before completion. Engineering terminal status is limited to `COMPLETED` and `BLOCKED`.

## Maintainer Responsibilities

For changes to `codex-template`, Codex A also validates the governance/payload boundary, project-agnostic compatibility, relevant evidence and ADR constraints, repository consistency, Final Version Impact, changelog, and release preparation. Run `./scripts/check`.

Reference-driven changes still require an approved `Change Proposed`; a new reference never directly authorizes `template/` modification.

## Dogfooding Principle

Root governance and `template/` share the core ownership, Task Contract, review, Git, and artifact model. Their surrounding policy differs because root files maintain the product while payload files guide an instantiated project.

## Task Completion vs Release

Task determines Version Impact. Release determines Version Number. Local task completion does not authorize remote push, tag publication, or release publication.
