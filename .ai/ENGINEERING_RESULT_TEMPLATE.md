# Engineering Result Report

## Task Identity

- Task ID:
- Revision:
- Task Type: `READ_ONLY | CHANGE`
- Original Task: `<identity/reference only; do not restate Task content already available to ChatGPT / Design Owner>`

## Engineering State

`COMPLETED | AWAITING_DISPOSITION | BLOCKED`

For an approved `CHANGE`, use `AWAITING_DISPOSITION`: this report precedes integration and is not a terminal Engineering Status. Terminal Engineering Status remains `COMPLETED | BLOCKED`.

## Primary Consumer and Evidence Boundary

The primary consumer is ChatGPT / Design Owner. Together with the original Task and pre-Task repository context, this report is the self-contained execution-to-design evidence handoff for the normal engineering disposition judgment. It reports decision-relevant facts produced or discovered during execution; it does not reproduce the complete diff or repository state.

ChatGPT evaluates this reported evidence without needing the temporary task branch, task commits, changed files, complete diff, or post-Task repository state. That evidence-based judgment does not imply direct inspection and does not replace Codex B's Independent Review of the actual committed change.

## Implementation Outcome / Result Summary

- Material behavior or structure changed:
- Material implementation decisions:
- Important invariants preserved:
- Changed areas and consequences:
- Other facts needed to interpret acceptance and review evidence:

## Repository State

For a multi-repository Task, repeat these identity fields for the workspace and every modified child. Local completion does not require remote publication.

- Repository Changes: `YES | NO`
- Task Branch: `NOT_APPLICABLE | task/...`
- Base Branch: `NOT_APPLICABLE | <branch>`
- Base Commit: `NOT_APPLICABLE | <commit>`
- Reviewed Commit: `NOT_APPLICABLE | <commit>`
- Approved Commit: `NOT_APPLICABLE | <commit>`
- Presented Task HEAD: `NOT_APPLICABLE | <commit>`
- Integrated Commit: `NOT_APPLICABLE | PENDING_EXPLICIT_INTEGRATE | <commit>`
- Working Tree:
- Remote Publication: `NOT_AUTHORIZED | NOT_PUBLISHED | PUBLISHED`
- Identity Consistency: `<state whether Reviewed Commit == Approved Commit == Presented Task HEAD; explain every mismatch, uncertainty, child-repository relationship, or material working-tree effect>`

For `READ_ONLY + COMPLETED`, Repository Changes = `NO` and Independent Review = `NOT_APPLICABLE`.

For `CHANGE + AWAITING_DISPOSITION`, Independent Review = `APPROVED` and was performed by Codex B in a new Codex session explicitly created by the human user, Reviewed Commit == Approved Commit, and Integrated Commit = `PENDING_EXPLICIT_INTEGRATE`.

## Acceptance Evidence

Map each material acceptance criterion, or a clearly identified equivalent requirement, to execution evidence. Reference Verification Evidence rather than duplicating check detail.

| Criterion | Evidence | Status |
| --- | --- | --- |
|  |  | `SATISFIED | NOT_SATISFIED | NOT_ASSESSABLE` |

## Verification Evidence

Record checks actually performed and their results. Include evidence detail sufficient for ChatGPT to assess proportionality without rerunning the checks.

| Check | Scope / Purpose | Result | Evidence |
| --- | --- | --- | --- |
|  |  | `PASS | FAIL` |  |

### Important Checks Not Performed

Use `NONE` or identify the omitted check, why it was omitted, and the resulting implication or residual risk.

## Independent Review

- Final Review Target: `NOT_APPLICABLE | <Base Commit>..<Review Commit>`
- Final Verdict: `NOT_APPLICABLE | APPROVED | CHANGES_REQUESTED`
- Performed in human-created Codex B session: `NOT_APPLICABLE | YES`
- Review Prompt and Review Report manually transferred by human user: `NOT_APPLICABLE | YES`
- Review Attempts: `<count>`
- Material Findings and Resolutions: `NONE | <finding → implementation effect → resolution>`
- Final Unresolved Findings: `NONE | <details>`
- Reviewer Verification: `NOT_APPLICABLE | <checks and results reported by Codex B>`
- Reviewer-Confirmed Material Properties: `NONE | <properties directly inspected or verified by Codex B that matter to the Design Owner judgment>`

Codex B's verdict must result from independent inspection of the actual committed change, not validation of Codex A's narrative. This section reports that review evidence; it does not transfer Codex B's direct-inspection capability to ChatGPT.

## Blocked

- Blocked Reason: `NOT_APPLICABLE | INPUT_REQUIRED | DECISION_REQUIRED | REVIEW_LIMIT_REACHED`
- Required Input or Decision:

## Deviations

Include implementation deviations from the original Task, workflow deviations, and every material identity mismatch or uncertainty. Use `NONE` only when none exist.

## Residual Risks and Limitations

Use `NONE` or report decision-relevant residual risks, limitations, and evidence uncertainty.

## Codex A Engineering Recommendation

State a plain-language engineering recommendation supported by the evidence, if useful. This is neither ChatGPT / Design Owner's independent judgment nor the human's final disposition and does not authorize integration.

## Remaining Notes

Optional: add an `Automation Opportunities` section only when a concrete recurring deterministic procedure was discovered. A suggestion is not authorization to implement it.

## Final Version Impact

`NONE | PATCH | MINOR | MAJOR | UNKNOWN`

## Required Disposition

ChatGPT / Design Owner independently evaluates the original Task, pre-Task context, and this ERR, then advises the human. The human selects the final `INTEGRATE | REVISE | ABORT` disposition and returns it in a new explicit prompt to Codex A. Optional human code review may supplement this flow.
