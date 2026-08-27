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

Codex A is the Implementation Owner, responsible for repository inspection, approved implementation, repository consistency, validation, the local Git task lifecycle, preparation of the Independent Review handoff, Final Version Impact, and release preparation.

Codex B is the read-only Review Owner. It owns Review Findings and the review conclusion and MUST NOT modify the implementation under review. A qualifying Codex B MUST run in a new Codex session explicitly created by the human user; internal or sub-agent reviewers are informational only.

Research-heavy or architecture-defining work should normally arrive as an approved design or change proposal.

## Task Readiness

- `PASS` normally remains silent.
- `WARNING` must be surfaced when risk exists but no material user decision is required.
- `BLOCKED` must stop substantive execution.

Do not implement a change that violates the project-agnostic design principle, confuses governance with distributable payload, bypasses required reference review, introduces an unauthorized breaking change, or cannot be meaningfully verified.

## Task and Git Contracts

Read `.ai/AI_HANDOFF_PROTOCOL.md` and `.ai/GIT_WORKFLOW.md` for every Engineering Task. Use the artifact templates under `.ai/`.

Task Type is immutable and limited to `READ_ONLY` and `CHANGE`. A `CHANGE` requires one `task/*` branch, committed-state Independent Review, approval, and ff-only local integration before `COMPLETED`.

At review-ready state, Codex A creates the Review Commit and formal Codex Review Prompt, then stops. The human user creates the new Codex B session, transfers the prompt, and returns the formal Codex Review Report to Codex A.

Engineering Task decomposition belongs to ChatGPT / Design Owner. Do not delegate implementation ownership or create child Engineering Tasks.

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
