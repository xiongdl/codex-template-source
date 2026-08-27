# Git Workflow

## Branch Model

The single long-lived integration and release branch is `main`.

Every `CHANGE` task uses exactly one short-lived branch:

The branch namespace is `task/*`.

```text
main
└── task/<task-id>-<short-name>
```

Create the task branch from current `main`, not from another task branch. Do not require `dev`, `develop`, `feature/*`, `bugfix/*`, or `hotfix/*` taxonomies. `READ_ONLY` tasks require no task branch.

## Task History and Review Target

Multiple coherent commits are allowed. Before Review Attempt 1, local history may be cleaned up. After Review Attempt 1 begins, reviewed history should not normally be rewritten; review fixes are appended as commits. A rebase onto updated `main` is allowed but invalidates prior approval.

Formal Independent Review requires a committed Review Target:

1. implement;
2. verify;
3. create a local commit;
4. identify Base Commit and Review Commit.

The Review Commit must be task branch `HEAD`. Review covers the complete `Base Commit..Review Commit` Task diff and the repository in the Review Commit state, not only the final commit.

After `CHANGES_REQUESTED`, a new Review Commit is required only when Finding resolution changes tracked repository state. Repository changes must be verified and committed, and the new task-branch `HEAD` becomes the next Review Commit. If resolution is solely through Task Contract revision, Design Owner decision, required external input, or requirement clarification and tracked state is unchanged, do not create an artificial or empty commit; the next Review Attempt may use the same Review Commit.

## Integration Gate

Codex A owns local integration. Integrate a `CHANGE` task only when:

- Independent Review is `APPROVED`;
- task `HEAD` equals the Approved Commit;
- the tracked working tree is clean;
- the task branch is based on current `main`;
- required verification passes.

Integration must use:

```bash
git merge --ff-only
```

Do not squash the reviewed commits by default. The target invariant is:

```text
Reviewed Commit == Approved Commit == Integrated Commit
```

If `main` advances before integration, rebase the task branch onto current `main`, re-verify, identify the new Base and Review Commits, obtain a new Independent Review, and retry. Main advancement alone is not a blocked condition.

## Permissions

A `CHANGE` Task Contract authorizes Codex A to inspect Git state, create its task branch, explicitly stage task-related paths, commit, locally rebase onto `main`, perform ff-only local integration after the gate, and delete the normally merged local task branch.

Codex A MUST NOT absorb unrelated pre-existing working-tree changes. Prefer explicit-path staging.

Remote push, remote branch creation or deletion, force push, release publication, Git tag publication, destructive cleanup, forced branch deletion, and rewriting shared history require explicit authorization or persistent project policy.
