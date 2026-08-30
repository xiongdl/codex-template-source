# codex-template AI Engineering Workflow

## Purpose

`codex-template` dogfoods the same core AI engineering workflow it provides to instantiated projects while retaining its maintainer responsibilities.

## Ownership

- ChatGPT = Design Owner
- Codex A = Implementation Owner
- Codex B = Review Owner

Detailed task, handoff, review, and status contracts are in `.ai/AI_HANDOFF_PROTOCOL.md`. Reproducible branch, review-target, and integration rules are in `.ai/GIT_WORKFLOW.md`.

Codex A owns preparation of the Independent Review handoff. The human user owns creation of the new Codex B session and manual transfer of the formal review artifacts.

## Standard Flow

```text
Human Goal
    ↓
ChatGPT / Design Owner
    ↓ requirements, decisions, Task Contract
Codex A / Implementation Owner
    ↓ readiness, task branch, implementation, verification, commit, Review Prompt
HARD STOP → Human creates new Codex B session and transfers Review Prompt
    ↓
Codex B / Review Owner in the human-created session
    ↓ read-only Independent Review
Human returns Review Report to Codex A
    ↓
APPROVED ──────────────── CHANGES_REQUESTED
    ↓                         ↓ resolve and verify
Engineering Result Report     new Review Commit when tracked state changed
                              ↓ same Codex B re-review
    ↓
HARD STOP → ChatGPT judgment/recommendation → Human disposition
    ↓ disposition returned to Design Owner
Design Owner compiles complete explicit post-ERR prompt → Human transfers it
    ↓
INTEGRATE | REVISE | ABORT
```

Task Type is immutable and limited to `READ_ONLY` and `CHANGE`. A `CHANGE` requires committed-state Independent Review by Codex B in a new Codex session explicitly created by the human user and approval before completion. Internal, delegated, sub-agent, hidden, automatically spawned, same-session, and self-review mechanisms are informational only and do not consume Review Attempt count. Every `CHANGES_REQUESTED` requires re-review; a new Review Commit is required only when Finding resolution changes tracked repository state. `APPROVED` is technical approval, not integration authorization. The Engineering Result Report is decision input and precedes integration. Codex A must not infer the disposition. A bare disposition is not a complete execution handoff; the Design Owner compiles the complete post-ERR prompt under `.ai/AI_HANDOFF_PROTOCOL.md`. `INTEGRATE` binds that prompt to the current `.ai/GIT_WORKFLOW.md` Integration Gate; `REVISE` returns any changed intended state through verification and Independent Review; `ABORT` does not authorize destructive cleanup. Engineering terminal status remains limited to `COMPLETED` and `BLOCKED`.

Codex A uses the smallest inspection and verification that provides reasonable confidence for the actual Task risk while still implementing the objective completely and running repository-required checks. Worktrees, extra reviewers, sub-agents, exhaustive inspection, and a duplicate adversarial review are not required workflow mechanics.

## Maintainer Responsibilities

For changes to `codex-template`, Codex A also validates the governance/payload boundary, project-agnostic compatibility, relevant evidence and ADR constraints, repository consistency, Final Version Impact, changelog, and release preparation. Run `./scripts/check`.

Reference-driven changes still require an approved `Change Proposed`; a new reference never directly authorizes `template/` modification.

## Dogfooding Principle

Root governance and `template/` share the core ownership, Task Contract, review, Git, and artifact model. Their surrounding policy differs because root files maintain the product while payload files guide an instantiated project.

## Task Completion vs Release

Task determines Version Impact. Release determines Version Number. Local task completion does not authorize remote push, tag publication, or release publication.
