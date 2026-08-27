# Git Workflow

## Branch Model

`main` is the single long-lived integration and release mainline. Every `CHANGE` task uses exactly one short-lived branch created from current `main`:

The branch namespace is `task/*`.

```text
main
└── task/<task-id>-<short-name>
```

Do not normally branch from another task branch. Do not require `dev`, `develop`, `feature/*`, `bugfix/*`, or `hotfix/*`. `READ_ONLY` tasks need no branch.

## Committed Review Target

Formal review requires a committed Review Target.

Multiple coherent task commits are allowed. Before Review Attempt 1, local history may be cleaned up. After it begins, reviewed history should not normally be rewritten and review fixes should be appended. Rebasing onto updated `main` is allowed but invalidates prior approval.

Before Independent Review, Codex A must implement, verify, commit, and identify Base Commit and Review Commit. The Review Commit must be task branch `HEAD`. Review covers the complete `Base Commit..Review Commit` Task change set and repository at Review Commit, not only the final commit.

## Integration Gate

Codex A integrates locally only when Independent Review is `APPROVED`, task `HEAD` equals Approved Commit, the tracked working tree is clean, the task branch is based on current `main`, and required verification passes.

Integration must use:

```bash
git merge --ff-only
```

Do not squash reviewed commits by default. The target is:

```text
Reviewed Commit == Approved Commit == Integrated Commit
```

If `main` advances, rebase onto current `main`, re-verify, identify new Base and Review Commits, obtain a new Independent Review, and retry. Main advancement alone is not `BLOCKED`.

## Permissions

A `CHANGE` Task Contract authorizes normal local task lifecycle operations: Git inspection, task branch creation, explicit-path staging, local commits, local rebase onto `main`, ff-only integration after the gate, and normal deletion of a merged local task branch. Codex A MUST NOT absorb unrelated pre-existing changes.

Remote push or branch writes, force push, release or Git tag publication, destructive cleanup, forced branch deletion, and shared-history rewriting require explicit authority or persistent project policy.
