# AGENTS.md

This repository follows an AI-assisted engineering workflow.

## Automatic Lifecycle Routing

First determine whether `git rev-parse --verify HEAD` succeeds. If there is no valid Git `HEAD`, follow `.ai/PROJECT_INIT.md` and establish the Initial Commit baseline. Bootstrap is a pre-Initial-Commit lifecycle mode, not a third Task Type. Once a valid `HEAD` exists, use the Normal Engineering workflow below.

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

## Task Readiness

Before substantive repository work, apply `.ai/TASK_READINESS.md` using the Codex profile.

- `PASS` normally remains silent.
- `WARNING` reports the risk and continues only when no material user decision is required.
- `BLOCKED` stops substantive implementation and requests the minimum information or decision required to proceed.

Do not bypass the readiness gate by silently resolving architectural ambiguity, missing evidence, unverified repository state, or unauthorized breaking changes.

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

## Ownership and Task Contract

Codex A is the Implementation Owner. Codex B is the read-only Review Owner and MUST NOT modify the implementation under review. A qualifying Codex B MUST run in a new Codex session explicitly created by the human user; internal or sub-agent reviewers are informational only. ChatGPT / Design Owner owns requirements, architecture, material decisions, Task Contracts, and Engineering Task decomposition.

Before Normal Engineering work, read `.ai/AI_HANDOFF_PROTOCOL.md` and `.ai/GIT_WORKFLOW.md`. Task Type is immutable and limited to `READ_ONLY` and `CHANGE`. Every `CHANGE` has a workspace `task/*` branch and Review Commit and requires committed-state Independent Review, approval, and ff-only local integration before `COMPLETED`.

At review-ready state, Codex A creates the Review Commit and formal Codex Review Prompt, then stops. The human user creates the new Codex B session, transfers the prompt, and returns the formal Codex Review Report to Codex A.

Codex A may organize internal steps but must not delegate implementation ownership or create child Engineering Tasks.

## Before Modifying Code

1. Read `docs/ARCHITECTURE.md`.
2. Read `docs/PROJECT_STATUS.md`.
3. Read `docs/REPRODUCIBILITY.md` when environment/build/result reproduction matters.
4. Identify the affected workspace and child repositories.
5. Read relevant repository-local instructions without injecting workspace governance into child repositories.
6. Read relevant design, decision, and interface docs.
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

Preserve each repository's native test structure. Place new tests at the narrowest project-appropriate level that fully validates the behavior; the workspace does not prescribe generic implementation or test directories.

## Automation

Repeated workflows should be automated where practical.

Prefer project-standard entry points under `scripts/`.

## Reproducibility

Setup, dependencies, configuration, build, tests, and important outputs should be reconstructable from repository-contained information.

## Traceability

Use:

- `docs/design/`
- `docs/decisions/`
- project-appropriate interface documentation
- `docs/PROJECT_STATUS.md`

for durable engineering knowledge.

## Maintainability

Prefer scoped, understandable changes.

Avoid hidden coupling, duplicated conventions, unexplained configuration, and unnecessary framework complexity.

## AI Operability

A new Codex session should be able to determine:

- what the project is,
- how it is structured,
- which build/test/verify capabilities currently exist,
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
