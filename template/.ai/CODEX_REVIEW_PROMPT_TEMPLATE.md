# Codex Review Prompt

## Review Identity

- Task ID:
- Review Attempt: `N / 3`
- Previous Review: `NOT_APPLICABLE | <artifact/reference>`

## Review Objective

This prompt MUST be executed in a Codex session distinct from the Implementation Owner session.

Independently review the complete Task change set and repository state. This is read-only: Codex B MUST NOT modify repository artifacts or the implementation under review.

## Original Task

Reference the Codex Task Prompt:

## Git Review Target

- Base Commit:
- Review Commit:

The Review Commit must be task branch `HEAD`. Review `Base Commit..Review Commit`, not only the last commit.

For re-review after contract- or decision-only resolution with unchanged tracked repository state, reference the updated Task Contract revision and Previous Review Report above; the Review Commit may remain unchanged.

## Authoritative References

## In Scope

## Out of Scope

## Changed Areas

Navigation hints only; Codex A's implementation narrative is not evidence of correctness.

## Verification

Inspect or run the checks needed to validate acceptance and record what was performed.

## Required Output

Return `.ai/CODEX_REVIEW_REPORT_TEMPLATE.md`: `APPROVED` for zero Findings, otherwise `CHANGES_REQUESTED`.
