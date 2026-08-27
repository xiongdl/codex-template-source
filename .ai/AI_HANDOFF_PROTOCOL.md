# AI Handoff Protocol

## Purpose

This protocol makes cross-role engineering work reproducible from repository state and durable artifacts rather than conversation history.

## Owners

- **ChatGPT is the Design Owner.** It owns requirements, architecture, material decisions, Task Contracts, and Engineering Task decomposition.
- **Codex A is the Implementation Owner.** It owns repository implementation, verification, the local Git task lifecycle, Engineering Task status, and preparation of the Independent Review handoff.
- **Codex B is the Review Owner.** It independently reviews the implementation and owns Review Findings and the review conclusion. Codex B is read-only and MUST NOT modify the implementation under review.

## Task Contract

Every Codex Task Prompt declares an immutable Task ID and Task Type plus a Revision.

Every `CHANGE` Task resolves one immutable Base Branch: the explicit Task Contract Base Branch when provided, otherwise the repository Default Base Branch. The same Base Branch is the Task Branch creation source and final merge target. Each `CHANGE` Task retains exactly one Base Branch and one Task Branch throughout its lifecycle.

Task Type is limited to:

- `READ_ONLY`: repository modification is not authorized, no task branch is required, and Independent Review is `NOT_APPLICABLE`.
- `CHANGE`: repository modification is authorized only within scope, exactly one dedicated `task/*` branch is required, and Independent Review is mandatory before completion.

Task Type is immutable within a Task Contract. Discovering required changes during a `READ_ONLY` task requires a new `CHANGE` Task Contract from the Design Owner. Task Contract revisions may clarify the same task but do not reset Review Attempt count.

Engineering Task decomposition belongs exclusively to ChatGPT / Design Owner. Codex A may organize internal implementation steps but MUST NOT create child Engineering Tasks, delegate implementation ownership to another Codex, or create independent implementation subtasks for other Codex sessions. If Design Owner decomposition is required, return `BLOCKED` with `DECISION_REQUIRED`.

## Formal Handoff Artifacts

Exactly four formal cross-role artifacts are used:

1. ChatGPT → Codex A: Codex Task Prompt (`CODEX_TASK_TEMPLATE.md`)
2. Codex A → Codex B: Codex Review Prompt (`CODEX_REVIEW_PROMPT_TEMPLATE.md`)
3. Codex B → Codex A: Codex Review Report (`CODEX_REVIEW_REPORT_TEMPLATE.md`)
4. Codex A → ChatGPT: Engineering Result Report (`ENGINEERING_RESULT_TEMPLATE.md`)

Conversation is transient. Artifact plus repository state is the handoff contract.

Same-task Codex A1 → Codex A2 continuation is allowed without another formal artifact. It preserves Task ID, Task Type, Task Contract identity, task branch, and Review Attempt count. Repository state, commits, Task Contract, and Review Reports are the system of record. Checkpoint commits are allowed but are not Review Commits.

## Independent Review

For every `CHANGE` task, Independent Review MUST be performed by Codex B in a new Codex session explicitly created by the human user. The human user manually supplies Codex A's formal Codex Review Prompt to that session and returns Codex B's formal Codex Review Report to Codex A.

Codex A must implement, verify, commit, and provide a Codex Review Prompt identifying the Base Branch, Base Commit, Task Branch, and Review Commit. The Review Commit must be task-branch `HEAD`; working-tree-only review is invalid. Once the prompt is ready, Codex A MUST stop review execution in the Implementation Owner session. The next workflow action belongs to the human user, who explicitly creates the new Codex B session and transfers the prompt.

Codex A self-review, same-session role switching, internal reviewer contexts, sub-agent or delegated reviewers, hidden or automatically spawned reviewer contexts, and any reviewer context not explicitly created as a new Codex session by the human user do not satisfy the Independent Review Gate. They may be supplementary informational checks only: they do not count as formal Independent Review, do not consume Review Attempt count, cannot authorize integration, and cannot produce a qualifying `APPROVED`. Internal-agent isolation is not evaluated for eligibility.

Codex B reviews the complete `Base Commit..Review Commit` change set and the repository at the Review Commit. Codex A's implementation narrative is not evidence of correctness.

Review Result is limited to:

- `APPROVED`: zero Findings.
- `CHANGES_REQUESTED`: one or more Findings.

A Review Finding contains only:

- Finding ID
- Issue
- Evidence
- Required Change

Non-blocking observations belong in Notes. Codex B does not return Task-level `BLOCKED`.

Every `CHANGES_REQUESTED` result requires mandatory re-review by the same Review Owner. Codex A may challenge a Finding with repository, design, or test evidence, but may not close it unilaterally; only Codex B may withdraw it. Review Attempt increments normally and does not reset.

If resolving Findings changes any tracked repository artifact, Codex A must resolve and verify the changes, create a new local commit as the next Review Commit, and generate the next Codex Review Prompt. Re-review still covers the complete Base Commit through the current Review Commit; the previous reviewed commit may be used to focus Finding resolution.

If Findings are resolved solely through Task Contract revision, a Design Owner decision, required external input, or requirement clarification and tracked repository state does not change, no artificial or empty commit is required. The next Review Attempt may target the same Review Commit. Its Review Prompt must reference the updated Task Contract revision, the Previous Review Report, and the unchanged Review Commit.

Task Contract revision must not hide or waive a genuine implementation defect. Incorrect behavior, missing required implementation, missing verification, or another repository defect requires normal repository resolution unless the Design Owner legitimately changes the Task Contract. A contract change that materially redefines Task identity, core scope, or acceptance intent requires a new Engineering Task.

Maximum Review Attempts = 3 per Task ID. The count survives Task Contract revisions and session continuation. A third `CHANGES_REQUESTED` produces Engineering Status `BLOCKED` with reason `REVIEW_LIMIT_REACHED`.

Approval is bound to the exact Approved Commit. Any later repository modification or rebase invalidates approval and requires verification and a new Independent Review.

## Engineering Status

Terminal Engineering Status is limited to:

- `COMPLETED`
- `BLOCKED`

Execution and verification failures are intermediate engineering conditions, not additional terminal statuses. Engineering-task Blocked Reason is limited to:

- `INPUT_REQUIRED`
- `DECISION_REQUIRED`
- `REVIEW_LIMIT_REACHED`

## Human Boundary

Human authority is concentrated in `INPUT`, `DECISION`, `REVIEW_SESSION`, `REMOTE`, and `RELEASE`. Independent Review requires the human user to create the new Codex B session and manually transfer the formal review artifacts. Normal implementation and approved local integration do not require step-by-step confirmation. Remote writes and release publication require explicit authority.
