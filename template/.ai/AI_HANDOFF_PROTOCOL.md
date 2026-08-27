# AI Handoff Protocol

## Owners

- **ChatGPT is the Design Owner** and owns requirements, architecture, material decisions, Task Contracts, and Engineering Task decomposition.
- **Codex A is the Implementation Owner** and owns repository implementation, verification, the local Git task lifecycle, Engineering Task status, and Independent Review orchestration.
- **Codex B is the Review Owner** and owns independent implementation review, Review Findings, and the review conclusion. Codex B is read-only and MUST NOT modify the implementation under review.

## Task Contracts

Every Task Contract has an immutable Task ID and Task Type plus a Revision. Task Type is limited to:

- `READ_ONLY`: repository modification is not authorized, no task branch is required, and Independent Review is `NOT_APPLICABLE`.
- `CHANGE`: modification is authorized within scope, exactly one dedicated `task/*` branch is required, and Independent Review is mandatory before completion.

Task Type is immutable. A `READ_ONLY` task that discovers required changes returns to the Design Owner for a new `CHANGE` Task Contract. Revisions may clarify the same Task but do not reset Review Attempt count.

Engineering Task decomposition belongs exclusively to ChatGPT / Design Owner. Codex A may organize internal steps but MUST NOT create child Engineering Tasks, delegate implementation ownership to another Codex, or create independent implementation subtasks for other Codex sessions. When Design Owner decomposition is required, return `BLOCKED` with `DECISION_REQUIRED`.

## Formal Handoff Artifacts

Exactly four formal cross-role artifacts exist:

1. ChatGPT → Codex A: Codex Task Prompt (`CODEX_TASK_TEMPLATE.md`)
2. Codex A → Codex B: Codex Review Prompt (`CODEX_REVIEW_PROMPT_TEMPLATE.md`)
3. Codex B → Codex A: Codex Review Report (`CODEX_REVIEW_REPORT_TEMPLATE.md`)
4. Codex A → ChatGPT: Engineering Result Report (`ENGINEERING_RESULT_TEMPLATE.md`)

Conversation is transient. Artifact plus repository state is the handoff contract.

Codex A1 → Codex A2 continuation of the same Implementation Owner role needs no formal Session Handoff artifact. It preserves Task ID, Task Type, Task Contract identity, task branch, and Review Attempt count. Repository state, Task Contract, commits, and Review Reports are the system of record. Checkpoint commits are not Review Commits.

## Independent Review

For every `CHANGE`, Codex A implements, verifies, commits, and identifies Base Commit and Review Commit. Formal review targets committed repository state: the Review Commit must be task branch `HEAD`, and working-tree-only review is invalid.

Codex B reviews the full `Base Commit..Review Commit` diff and repository at the Review Commit. Codex A's implementation narrative is not evidence of correctness. Review Result is limited to:

- `APPROVED`: zero Findings.
- `CHANGES_REQUESTED`: one or more Findings.

Every Finding contains Finding ID, Issue, Evidence, and Required Change. Non-blocking observations belong in Notes. Findings have no severity, priority, or blocking flag. Codex B does not return Task-level `BLOCKED`.

After `CHANGES_REQUESTED`, Codex A addresses all Findings, verifies, creates a new commit, and obtains mandatory re-review. Codex A may challenge a Finding with repository, design, or test evidence, but only Codex B may withdraw it. Re-review covers the complete Base Commit through current Review Commit; the previous reviewed commit may focus Finding resolution.

Maximum Review Attempts = 3 per Task ID. The count survives Task Contract revisions and session continuation. A third `CHANGES_REQUESTED` produces Engineering Status `BLOCKED` and Blocked Reason `REVIEW_LIMIT_REACHED`.

Approval is bound to the exact Approved Commit. Any modification after approval or rebase invalidates approval and requires re-verification and new Independent Review.

## Engineering Status

Terminal status is limited to `COMPLETED` and `BLOCKED`. Failures during execution are intermediate conditions. Engineering-task Blocked Reason is limited to `INPUT_REQUIRED`, `DECISION_REQUIRED`, and `REVIEW_LIMIT_REACHED`.

## Human Boundary

Human authority is concentrated in `INPUT`, `DECISION`, `REMOTE`, and `RELEASE`. Normal implementation, review, and local integration need no step-by-step confirmation. Remote writes and release publication require explicit authority.
