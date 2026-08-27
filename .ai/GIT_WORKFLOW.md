# Git Workflow

## Branch Model

Every repository defines one `Default Base Branch`. For `codex-template`, the Default Base Branch is `main`.

Each `CHANGE` Task resolves exactly one `Base Branch` for its complete lifecycle:

1. use the explicit Task Contract `Base Branch`, when provided;
2. otherwise use the repository `Default Base Branch`.

The Base Branch is the logical branch identity. The Base Commit is the exact commit of that branch used for a specific review or integration state. A Task's Base Branch is immutable: it is both the source from which the Task Branch is created and the final merge target.

Every `CHANGE` task uses exactly one short-lived branch:

The branch namespace is `task/*`.

```text
Base Branch
└── task/<task-id>-<short-name>
```

Create the Task Branch from the current Base Branch, not from another task branch. Do not require a framework-wide `main`, `dev`, `develop`, `feature/*`, `bugfix/*`, or `hotfix/*` taxonomy. `READ_ONLY` tasks require no task branch.

The invariant is:

```text
Task Branch creation source == final merge target == Base Branch
```

## Task History and Review Target

Multiple coherent commits are allowed. Before Review Attempt 1, local history may be cleaned up. After Review Attempt 1 begins, reviewed history should not normally be rewritten; review fixes are appended as commits. A rebase onto the updated Base Branch is allowed but invalidates prior approval.

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
- the Task Branch is based on the current Base Branch;
- required verification passes.

Integration must use:

```bash
git merge --ff-only
```

Do not squash the reviewed commits by default. The target invariant is:

```text
Reviewed Commit == Approved Commit == Integrated Commit
```

If the Base Branch advances before integration, rebase the Task Branch onto the current Base Branch, re-verify, identify the new Base and Review Commits, obtain a new Independent Review, and retry. Base Branch advancement alone is not a blocked condition.

## Permissions

A `CHANGE` Task Contract authorizes Codex A to inspect Git state, create its Task Branch from the resolved Base Branch, explicitly stage task-related paths, commit, locally rebase onto that Base Branch, perform ff-only local integration back into that same Base Branch after the gate, and delete the normally merged local Task Branch.

Codex A MUST NOT absorb unrelated pre-existing working-tree changes. Prefer explicit-path staging.

Remote push, remote branch creation or deletion, force push, release publication, Git tag publication, destructive cleanup, forced branch deletion, and rewriting shared history require explicit authorization or persistent project policy.
