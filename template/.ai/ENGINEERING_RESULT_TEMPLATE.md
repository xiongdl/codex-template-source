# Engineering Result Report

## Task Identity

- Task ID:
- Revision:
- Task Type: `READ_ONLY | CHANGE`
- Original Task:

## Engineering State

`COMPLETED | AWAITING_DISPOSITION | BLOCKED`

For an approved `CHANGE`, use `AWAITING_DISPOSITION`: this report precedes integration and is not a terminal Engineering Status. Terminal Engineering Status remains `COMPLETED | BLOCKED`.

## Result Summary

## Repository State

For a multi-repository Task, repeat these identity fields for the workspace and every modified child. Local completion does not require remote publication.

- Repository Changes: `YES | NO`
- Task Branch: `NOT_APPLICABLE | task/...`
- Base Branch: `NOT_APPLICABLE | <branch>`
- Base Commit: `NOT_APPLICABLE | <commit>`
- Reviewed Commit: `NOT_APPLICABLE | <commit>`
- Approved Commit: `NOT_APPLICABLE | <commit>`
- Integrated Commit: `NOT_APPLICABLE | PENDING_EXPLICIT_INTEGRATE | <commit>`
- Working Tree:
- Remote Publication: `NOT_AUTHORIZED | NOT_PUBLISHED | PUBLISHED`

For `READ_ONLY + COMPLETED`, Repository Changes = `NO` and Independent Review = `NOT_APPLICABLE`.

For `CHANGE + AWAITING_DISPOSITION`, Independent Review = `APPROVED` and was performed by Codex B in a new Codex session explicitly created by the human user, Reviewed Commit == Approved Commit, and Integrated Commit = `PENDING_EXPLICIT_INTEGRATE`.

## Verification

## Independent Review

- Status: `NOT_APPLICABLE | APPROVED | CHANGES_REQUESTED`
- Performed in human-created Codex B session: `NOT_APPLICABLE | YES`
- Review Prompt and Review Report manually transferred by human user: `NOT_APPLICABLE | YES`
- Review Attempts:
- History:

## Acceptance

## Blocked

- Blocked Reason: `NOT_APPLICABLE | INPUT_REQUIRED | DECISION_REQUIRED | REVIEW_LIMIT_REACHED`
- Required Input or Decision:

## Deviations

## Remaining Notes

Optional: add an `Automation Opportunities` section only when a concrete recurring deterministic procedure was discovered. A suggestion is not authorization to implement it.

## Final Version Impact

`NONE | PATCH | MINOR | MAJOR | UNKNOWN`

## Required Disposition

ChatGPT / Design Owner evaluates this ERR and advises the human. The human selects `INTEGRATE | REVISE | ABORT` and returns that decision input to ChatGPT / Design Owner. The Design Owner compiles the complete explicit post-ERR Codex A prompt required by `.ai/AI_HANDOFF_PROTOCOL.md`, and the human transfers that complete prompt to Codex A. A bare disposition token is not sufficient downstream execution authorization.
