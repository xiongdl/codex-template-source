# Git Workflow

## Branch Model

Every repository defines one `Default Base Branch`. For `codex-template`, the Default Base Branch is `main`.

Each `CHANGE` Task resolves exactly one `Base Branch` for its complete lifecycle:

1. use the explicit Task Contract `Base Branch`, when provided;
2. otherwise use the repository `Default Base Branch`.

The Base Branch is the logical branch identity. The Base Commit is the exact commit of that branch used for a specific review or integration state. A Task's Base Branch is immutable: it is both the source from which the Task Branch is created and the final merge target.

Every `CHANGE` task uses exactly one short-lived workspace branch. Multi-repository child branches are governed separately below.

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

Codex A owns local integration after the post-ERR decision. Integrate a `CHANGE` task only when:

- Independent Review is `APPROVED`;
- the Engineering Result Report has been returned and a new explicit `INTEGRATE` prompt has been received;
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

## Multi-Repository Tasks

One coherent workspace Engineering Task may modify the workspace and managed child Git repositories. The workspace is the composition anchor and always has the Task Branch and top-level Review Commit. At Task start, record expected repository scope; for each modified repository record path, Base Branch, Base Commit, Task Branch, and Review Commit. Do not create branches in unchanged children or classify repositories as PRIMARY/DEPENDENCY. Scope expansion follows normal Task revision and design-decision rules.

Create the workspace Task Branch first. Each changed child uses at most one Task Branch, normally with the workspace branch name, created from its own stable Base Branch. Child repositories retain native governance and layout; workspace artifacts are not injected into them.

Prepare review child-first and workspace-last: commit each child Review Commit, record its exact gitlink or composition identity in the workspace, then create the workspace Review Commit. The single Review Prompt and Review Attempt cover the complete repository change set and cross-repository consistency. If a child Review Commit changes during re-review, update and recommit the workspace composition.

After exact-commit approval and the explicit post-ERR `INTEGRATE` prompt, integrate changed children first and the workspace last using each repository's ff-only Base Branch. For every changed repository, `Reviewed Commit == Approved Commit == Integrated Commit`. An interrupted local sequence is resumed until the approved composition is consistent; database-style rollback is not required.

Local completion does not require publication. With separate Human REMOTE authorization, publish changed child commits first, verify they are reachable from configured official remotes, and publish the referencing workspace last.

## Permissions

A `CHANGE` Task Contract authorizes Codex A to perform these operations in the workspace and in-scope modified child repositories: inspect Git state; create the authorized Task Branches from their resolved Base Branches; explicitly stage task-related paths; commit; locally rebase onto the same Base Branch; perform ff-only local integration after the gate; and delete normally merged local Task Branches.

Codex A MUST NOT absorb unrelated pre-existing working-tree changes. Prefer explicit-path staging.

Remote push, remote branch creation or deletion, force push, release publication, Git tag publication, destructive cleanup, forced branch deletion, and rewriting shared history require explicit authorization or persistent project policy.
