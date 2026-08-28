# AI Handoff Protocol

## Purpose

This protocol makes cross-role engineering work reproducible from repository state and durable artifacts rather than conversation history.

## Owners

- **ChatGPT is the Design Owner.** It owns requirements, architecture, material decisions, Task Contracts, and Engineering Task decomposition.
- **Codex A is the Implementation Owner.** It owns repository implementation, verification, the local Git task lifecycle, Engineering Task status, and preparation of the Independent Review handoff.
- **Codex B is the Review Owner.** It independently reviews the implementation and owns Review Findings and the review conclusion. Codex B is read-only and MUST NOT modify the implementation under review.

## Task Contract

Every Codex Task Prompt declares an immutable Task ID and Task Type plus a Revision.

Every `CHANGE` Task resolves one immutable workspace Base Branch: the explicit Task Contract Base Branch when provided, otherwise the repository Default Base Branch. The same Base Branch is the workspace Task Branch creation source and final merge target. A multi-repository Task additionally resolves one stable Base Branch and at most one Task Branch for each modified child repository.

Task Type is limited to:

- `READ_ONLY`: repository modification is not authorized, no task branch is required, and Independent Review is `NOT_APPLICABLE`.
- `CHANGE`: repository modification is authorized only within scope, exactly one dedicated workspace `task/*` branch is required, changed child repositories may each use at most one associated Task Branch, and Independent Review is mandatory before completion.

Task Type is immutable within a Task Contract. Discovering required changes during a `READ_ONLY` task requires a new `CHANGE` Task Contract from the Design Owner. Task Contract revisions may clarify the same task but do not reset Review Attempt count.

Engineering Task decomposition belongs exclusively to ChatGPT / Design Owner. Codex A may organize internal implementation steps but MUST NOT create child Engineering Tasks, delegate implementation ownership to another Codex, or create independent implementation subtasks for other Codex sessions. If Design Owner decomposition is required, return `BLOCKED` with `DECISION_REQUIRED`.

## Formal Handoff Artifacts

Exactly four formal cross-role artifacts are used:

1. ChatGPT → Codex A: Codex Task Prompt (`CODEX_TASK_TEMPLATE.md`)
2. Codex A → Codex B: Codex Review Prompt (`CODEX_REVIEW_PROMPT_TEMPLATE.md`)
3. Codex B → Codex A: Codex Review Report (`CODEX_REVIEW_REPORT_TEMPLATE.md`)
4. Codex A → ChatGPT: Engineering Result Report (`ENGINEERING_RESULT_TEMPLATE.md`)

Conversation and formal artifact instances are transient; Task, Review Prompt, Review Report, and Engineering Result Report instances are not persisted in the repository. The repository remains the durable source for governance, architecture, and implementation state. During a handoff, the receiving artifact plus the repository state available to that role is the operative contract.

Each artifact is a standalone, easily copyable Markdown document. Include decision-relevant identity, intent or verdict, commit identities, changed-area navigation, evidence, authoritative repository references, and the required next action. Refer to durable repository governance instead of substantially restating it, while retaining short action-critical instructions needed by a fresh receiving session. Optimize for information quality and self-sufficient handoff rather than minimum length. Implementation narrative is context, not correctness evidence.

The Codex Task Prompt contains an Authoritative Task Core: Goal, Scope, Out of Scope, Requirements, material Constraints / Decisions, and Acceptance Criteria, with related task-specific context as the template defines. It carries transient engineering intent that cannot reliably be recovered from repository state. When Codex A prepares the Codex Review Prompt, it MUST transfer that core verbatim and MUST NOT reinterpret, summarize, weaken, replace, or otherwise rewrite it. Formatting-only transformations may be used when the medium requires them without changing the authoritative content. Codex A records any implementation interpretation, clarification, deviation, implementation evidence, verification evidence, navigation, and previous-review state separately as Codex A-produced context.

The Review Prompt visibly separates the inherited Authoritative Task Core from Codex A-produced engineering information. It supplies a fresh Codex B session with the unchanged Task Core, exact Git review targets, the material implementation delta and decisions, Codex A verification evidence, useful navigation, deviations, and previous-review state when applicable. The Task artifact need not be persisted, and Codex B must not reconstruct transient task intent from Git history.

## Task Granularity

An Engineering Task SHOULD represent one coherent engineering objective, not one command, file, repository, or implementation step. Related activities may share a Task when they form a reviewable scope and meaningful acceptance boundary. Separate genuinely independent objectives when dependencies, risks, review context, acceptance boundaries, or failure independence materially differ. Governance should reduce engineering risk without unnecessary Task administration.

Same-task Codex A1 → Codex A2 continuation is allowed without another formal artifact. It preserves Task ID, Task Type, Task Contract identity, task branch, and Review Attempt count. Repository state, commits, Task Contract, and Review Reports are the system of record. Checkpoint commits are allowed but are not Review Commits.

## Independent Review

For every `CHANGE` task, Independent Review MUST be performed by Codex B in a new Codex session explicitly created by the human user. The human user manually supplies Codex A's formal Codex Review Prompt to that session and returns Codex B's formal Codex Review Report to Codex A.

Codex A must implement, verify, commit, and provide a Codex Review Prompt identifying the Base Branch, Base Commit, Task Branch, and Review Commit. The Review Commit must be task-branch `HEAD`; working-tree-only review is invalid. Once the prompt is ready, Codex A MUST stop review execution in the Implementation Owner session. The next workflow action belongs to the human user, who explicitly creates the new Codex B session and transfers the prompt.

Codex A self-review, same-session role switching, internal reviewer contexts, sub-agent or delegated reviewers, hidden or automatically spawned reviewer contexts, and any reviewer context not explicitly created as a new Codex session by the human user do not satisfy the Independent Review Gate. They may be supplementary informational checks only: they do not count as formal Independent Review, do not consume Review Attempt count, cannot authorize integration, and cannot produce a qualifying `APPROVED`. Internal-agent isolation is not evaluated for eligibility.

Codex B reviews the complete `Base Commit..Review Commit` change set and the repository at the Review Commit. Codex A's implementation narrative is not evidence of correctness.

Codex B uses a lightweight but independent `Understand → Inspect → Challenge → Verify` review. It inspects the complete committed Task change set and relevant surrounding context, asks where the implementation could be materially wrong, and runs targeted additional checks when they increase confidence. It does not default to exhaustive repository scanning or mechanically repeat Codex A's complete verification suite.

Before approval, Codex B determines that the Task appears correctly satisfied, no material correctness or regression issue remains, and verification provides reasonable confidence. `APPROVED` is not formal proof, but it must mean more than noticing no obvious bug.

Review Result is limited to:

- `APPROVED`: zero Findings.
- `CHANGES_REQUESTED`: one or more Findings.

A Review Finding contains only:

- Finding ID
- Issue
- Evidence
- Required Change

Non-blocking observations belong in Notes. Codex B does not return Task-level `BLOCKED`.

A Finding is reserved for a concrete material problem that should block integration. Naming, style, optional refactoring, non-essential comments, and unrelated pre-existing issues belong in Notes, if mentioned at all.

Every `CHANGES_REQUESTED` result requires mandatory re-review by the same Review Owner. Codex A may challenge a Finding with repository, design, or test evidence, but may not close it unilaterally; only Codex B may withdraw it. Review Attempt increments normally and does not reset.

Re-review is incremental-first: inspect previous Findings and their resolution, check fix-related regressions, then confirm that the complete current change remains acceptable. Expand review when the new Review Commit materially changes broader behavior; do not mechanically repeat unaffected exploration.

If resolving Findings changes any tracked repository artifact, Codex A must resolve and verify the changes, create a new local commit as the next Review Commit, and generate the next Codex Review Prompt. Re-review still covers the complete Base Commit through the current Review Commit; the previous reviewed commit may be used to focus Finding resolution.

If Findings are resolved solely through Task Contract revision, a Design Owner decision, required external input, or requirement clarification and tracked repository state does not change, no artificial or empty commit is required. The next Review Attempt may target the same Review Commit. Its Review Prompt must reference the updated Task Contract revision, the Previous Review Report, and the unchanged Review Commit.

Task Contract revision must not hide or waive a genuine implementation defect. Incorrect behavior, missing required implementation, missing verification, or another repository defect requires normal repository resolution unless the Design Owner legitimately changes the Task Contract. A contract change that materially redefines Task identity, core scope, or acceptance intent requires a new Engineering Task.

Maximum Review Attempts = 3 per Task ID. The count survives Task Contract revisions and session continuation. A third `CHANGES_REQUESTED` produces Engineering Status `BLOCKED` with reason `REVIEW_LIMIT_REACHED`.

Approval is bound to the exact Approved Commit. Any later repository modification or rebase invalidates approval and requires verification and a new Independent Review.

## Engineering Result and Post-ERR Decision

After `APPROVED`, Codex A produces the Engineering Result Report before integration. ChatGPT / Design Owner is its primary consumer. The normal flow is `Codex A → ERR → ChatGPT judgment/recommendation → Human disposition`; optional human code review may supplement it.

Together with the original Task and pre-Task repository context, ERR is the self-contained execution-to-design evidence boundary for the normal Design Owner judgment. ChatGPT is not expected to access Codex A's temporary task branch, task commits, changed files, complete diff, or other post-Task repository state. ERR therefore returns decision-relevant facts produced or discovered during execution that ChatGPT cannot otherwise observe, without repeating original Task content or durable pre-Task governance unnecessarily and without becoming a repository mirror.

ERR reports the material implementation outcome and decisions, preserved invariants, changed-area consequences, deviations, criterion-linked acceptance evidence, checks performed and results, important verification omissions, Independent Review target and attempt history, material Findings and resolutions, unresolved Findings, final verdict, relevant reviewer verification and confirmed material properties, residual risks, and Final Version Impact when applicable. It also reports enough repository identities and relationships to assess whether the reviewed and approved implementation is the implementation presented for disposition, including material working-tree or child-repository state. Every material mismatch or uncertainty is explicit.

Evidence is preferred over unsupported status assertions. The ERR must allow ChatGPT to assess reported acceptance, verification proportionality, Independent Review evidence, and commit-identity consistency, but the resulting judgment is not equivalent to direct implementation inspection and does not replace Codex B's Independent Review of the actual committed change. It may identify a concrete recurring deterministic procedure as an Automation Opportunity, including likely ownership, but this does not authorize implementation.

Codex A may add a plain-language engineering recommendation grounded in the reported evidence. It is distinct from ChatGPT / Design Owner's independent engineering judgment and from the human's final `INTEGRATE | REVISE | ABORT` disposition; it introduces no new formal status.

The report is decision input, not integration authorization. Codex A then stops. ChatGPT / Design Owner interprets it with the human decision and supplies a new explicit disposition prompt:

- `INTEGRATE`: authorize exact-approved-commit integration under `.ai/GIT_WORKFLOW.md`;
- `REVISE`: authorize the stated revision; any changed intended integrated state returns through verification and Independent Review;
- `ABORT`: end normal integration without implying reset, deletion, rollback, or other destructive cleanup.

Codex A MUST NOT infer a disposition from technical approval or from the report.

## Engineering Status

Terminal Engineering Status is limited to:

- `COMPLETED`
- `BLOCKED`

Execution and verification failures are intermediate engineering conditions, not additional terminal statuses. Engineering-task Blocked Reason is limited to:

- `INPUT_REQUIRED`
- `DECISION_REQUIRED`
- `REVIEW_LIMIT_REACHED`

## Human Boundary

Human authority is concentrated in `INPUT`, `DECISION`, `REVIEW_SESSION`, `REMOTE`, and `RELEASE`. Independent Review requires the human user to create the new Codex B session and manually transfer the formal review artifacts. Normal implementation does not require step-by-step confirmation; approved local integration requires the explicit post-ERR `INTEGRATE` decision, not additional command-by-command confirmation. Remote writes and release publication require explicit authority.
