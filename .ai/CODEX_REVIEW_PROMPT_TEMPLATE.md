# Codex Review Prompt

## Review Identity

- Task ID:
- Review Attempt: `N / 3`
- Previous Review: `NOT_APPLICABLE | <artifact/reference>`

## Review Objective

This prompt MUST be executed by Codex B in a new Codex session explicitly created by the human user as a read-only Independent Review. The human user must manually transfer this prompt and return the formal Codex Review Report to Codex A. Codex A MUST stop after producing this prompt. Self-review and internal, sub-agent, or delegated reviewers do not consume Review Attempt count and cannot approve the change. Other eligibility, review-method, and verdict rules are defined by `.ai/AI_HANDOFF_PROTOCOL.md`; Git target rules are defined by `.ai/GIT_WORKFLOW.md`.

## Inherited Authoritative Task Core

The formal prompt instance MUST contain the complete actual Authoritative Task Core copied exactly from the Original Codex A Task Prompt between the canonical boundary lines below. Empty content, placeholders, TODOs, copy instructions, references to the Original Task Prompt, repository paths, attachments, links, summaries, excerpts, or other external dependencies are not substitutes. Codex B must be able to obtain the complete authoritative intent from this prompt alone.

The canonical Embedded Core operand is all raw text after the newline terminating `<!-- BEGIN VERBATIM AUTHORITATIVE TASK CORE -->` and before `<!-- END VERBATIM AUTHORITATIVE TASK CORE -->`. Boundary lines are framing, not operands. Before presenting the prompt to the human, Codex A MUST extract the Original and Embedded operands without trim, dedent, newline normalization, Markdown normalization, or any other preprocessing; verify that both expected boundaries exist, that the Embedded operand is complete actual non-substitute content, and that `Original Authoritative Task Core == Embedded Authoritative Task Core` by exact textual equality. If any check fails, Codex A MUST correct or regenerate the prompt and MUST NOT present it as the formal Independent Review handoff.

<!-- BEGIN VERBATIM AUTHORITATIVE TASK CORE -->

<!-- END VERBATIM AUTHORITATIVE TASK CORE -->

## Codex A-Produced Review Context

Everything below this heading is engineering information newly produced or recorded by Codex A. It supplements but does not modify the inherited Authoritative Task Core.

The authoritative In Scope and Out of Scope boundaries remain in the inherited core above.

### Original Task

- Task Prompt Revision:
- Original Task reference for transfer/audit only (the Task artifact is transient and need not be repository-accessible):

## Task Review Target

Repeat the following repository-specific target for every modified repository. Together these exact targets form the complete Task Review Target. Do not require a workspace target when the workspace is not modified.

- Repository Path:
- Base Branch:
- Base Commit:
- Task Branch:
- Review Commit:

Each Review Commit must be its repository's Task Branch `HEAD`. Review every complete `Base Commit..Review Commit` range, not only the last commit. One Task-level verdict covers the complete repository change set and relevant cross-repository consistency.

### Affected but Unmodified Repositories

Record any repository that contributes material inspection or verification evidence without tracked changes. Use `NONE` when not applicable. These repositories do not contribute Review Commits.

- Repository Path:
- Evidence / State:

For re-review after contract- or decision-only resolution with unchanged tracked repository state, reference the updated Task Contract revision and Previous Review Report above; each repository's Review Commit may remain unchanged.

## Authoritative References / Repository References

List only references useful to review; durable workflow rules should be referenced, not restated.

## Implementation Outcome and Decisions

- Material behavior or structure changed:
- Material implementation decisions and interpretations:
- Important invariants preserved:
- Deviations from the Authoritative Task Core: `NONE | <details>`

## Changed Areas

Navigation hints only; the implementation narrative is not evidence of correctness.

## Codex A Verification Evidence

- Checks performed and results:
- Important checks not performed and reasons:

Codex B must independently inspect the actual committed change and use the repository plus its own checks as evidence; Codex A's narrative is orientation, not correctness evidence.

## Previous-Review State

For Review Attempt 1 use `NOT_APPLICABLE`. For re-review, summarize prior Findings, their reported resolution, and whether tracked state changed; the full Previous Review reference remains in Review Identity.

## Required Output

Return `.ai/CODEX_REVIEW_REPORT_TEMPLATE.md` with `APPROVED` only for zero Findings, otherwise `CHANGES_REQUESTED`.
