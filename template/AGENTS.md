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

At review-ready state, Codex A creates the Review Commit and formal Codex Review Prompt, then stops. The human user creates the new Codex B session, transfers the prompt, and returns the formal Codex Review Report to Codex A. After approval, Codex A produces the Engineering Result Report and stops again. Integration, revision, or abort requires a new explicit post-ERR prompt reflecting the ChatGPT / Design Owner and human decision.

Codex A may organize internal steps but must not delegate implementation ownership or create child Engineering Tasks.

## Before Modifying Code

Begin with task-relevant context and targeted searches, then expand inspection when correctness, uncertainty, impact, or regression risk requires it. Relevant starting points are hints, not inspection allowlists. Do not impose token, file, search, or output limits.

1. Read the relevant portions of `docs/ARCHITECTURE.md`.
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

Stable, repeatable deterministic procedures are automation candidates when they provide recurring value. Codex may report a concrete opportunity, but MUST NOT implement it unless the current Engineering Task explicitly authorizes automation.

Automation lives with the responsibility it automates: preserve child-native build, test, and generation automation; keep workspace composition and cross-repository checks at workspace level; keep AI workflow governance in workspace governance. Prefer thin project-standard entry points under `scripts/` rather than duplicating native implementations.

## Engineering Environment

Environment Modules are the canonical workspace environment-composition mechanism. Conda may provide managed software and packages within that composition; Git records source state; repository automation performs engineering procedures. Environment definitions are workspace-owned even when a validated combination serves only one child repository.

Reuse a validated module combination when it fits. Add a directly sourceable `env/<name>.csh` and workspace-local modulefiles only for a real compatibility or isolation need; do not create placeholder profiles or one universal environment. Modulefiles select existing tools and configure paths and variables. They MUST NOT clone, build, test, install, download, or provision software.

Prefer declarative Conda environments where dependencies fit naturally. If pip is necessary, use it inside the appropriate Conda environment. Do not install or modify host-level tools without explicit authorization.

## Engineering Documentation and Figures

Use Markdown for repository-facing guidance. Use AsciiDoc as the reviewable source for formal specifications and guides, with PDF as the sole formal output generated by Asciidoctor PDF. Add a thin deterministic generation command only when real formal documentation exists; do not create a documentation platform or require byte-identical PDFs.

For data-driven figures, preserve data and a reproducible project-native or script-based generator. For conceptual diagrams, preserve editable `.drawio` source and generate SVG with the validated draw.io CLI. Check draw.io only when the Task changes such a diagram; never install or substitute it autonomously.

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

Use targeted verification during implementation and expand it when failure, uncertainty, or regression risk warrants. Before the Review Commit, run all checks required by the Task, repository governance, affected implementation, and actual risk. Prefer concise successful command output and expand failure details as needed. Report commands actually executed and verification results proportionately.
