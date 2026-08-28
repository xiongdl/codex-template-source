# Git Workflow

## Branch Model

Every repository defines one `Default Base Branch`. The template default is `main`; an instantiated project may configure another project-defined long-lived branch.

Each `CHANGE` Task resolves exactly one `Base Branch` for its complete lifecycle:

1. use the explicit Task Contract `Base Branch`, when provided;
2. otherwise use the repository `Default Base Branch`.

The Base Branch is the logical branch identity. The Base Commit is the exact commit of that branch used for a specific review or integration state. A Task's Base Branch is immutable: it is both the source from which the Task Branch is created and the final merge target.

Every `CHANGE` Task uses exactly one short-lived workspace Task Branch. Multi-repository child branches are governed separately below.

The branch namespace is `task/*`.

```text
Base Branch
└── task/<task-id>-<short-name>
```

Do not branch from another Task Branch. Do not impose a framework-wide `main`, `dev`, `develop`, `feature/*`, `bugfix/*`, or `hotfix/*` taxonomy. `READ_ONLY` tasks need no branch.

```text
Task Branch creation source == final merge target == Base Branch
```

## Committed Review Target

Formal review requires a committed Review Target.

Multiple coherent task commits are allowed. Before Review Attempt 1, local history may be cleaned up. After it begins, reviewed history should not normally be rewritten and review fixes should be appended. Rebasing onto the updated Base Branch is allowed but invalidates prior approval.

Before Independent Review, Codex A must implement, verify, commit, and identify Base Commit and Review Commit. The Review Commit must be task branch `HEAD`. Review covers the complete `Base Commit..Review Commit` Task change set and repository at Review Commit, not only the final commit.

After `CHANGES_REQUESTED`, a new Review Commit is required only when Finding resolution changes tracked repository state. Repository changes must be verified and committed, and the new task-branch `HEAD` becomes the next Review Commit. If resolution is solely through Task Contract revision, Design Owner decision, required external input, or requirement clarification and tracked state is unchanged, do not create an artificial or empty commit; the next Review Attempt may use the same Review Commit.

## Integration Gate

Codex A integrates locally only after Independent Review is `APPROVED`, the Engineering Result Report has been returned for decision, and a new explicit `INTEGRATE` prompt has been received. Task `HEAD` must equal Approved Commit, the tracked working tree must be clean, the Task Branch must be based on the current Base Branch, and required verification must pass.

Integration must use:

```bash
git merge --ff-only
```

Do not squash reviewed commits by default. The target is:

```text
Reviewed Commit == Approved Commit == Integrated Commit
```

If the Base Branch advances, rebase the Task Branch onto the current Base Branch, re-verify, identify new Base and Review Commits, obtain a new Independent Review, and retry. Base Branch advancement alone is not `BLOCKED`.

## Multi-Repository Tasks

One coherent workspace Engineering Task may modify the workspace and managed child Git repositories. The workspace is the composition anchor and always has the Task Branch and top-level Review Commit. At Task start, record expected repository scope; for each modified repository record path, Base Branch, Base Commit, Task Branch, and Review Commit. Do not create branches in unchanged children or classify repositories as PRIMARY/DEPENDENCY. Scope expansion follows normal Task revision and design-decision rules.

Create the workspace Task Branch first. Each changed child uses at most one Task Branch, normally with the workspace branch name, created from its own stable Base Branch. Child repositories retain native governance and layout; workspace artifacts are not injected into them.

Prepare review child-first and workspace-last: commit each child Review Commit, record its exact gitlink or composition identity in the workspace, then create the workspace Review Commit. The single Review Prompt and Review Attempt cover the complete repository change set and cross-repository consistency. If a child Review Commit changes during re-review, update and recommit the workspace composition.

After exact-commit approval and the explicit post-ERR `INTEGRATE` prompt, integrate changed children first and the workspace last using each repository's ff-only Base Branch. For every changed repository, `Reviewed Commit == Approved Commit == Integrated Commit`. An interrupted local sequence is resumed until the approved composition is consistent; database-style rollback is not required.

Local completion does not require publication. With separate Human REMOTE authorization, publish changed child commits first, verify they are reachable from configured official remotes, and publish the referencing workspace last.

## Permissions

A `CHANGE` Task Contract authorizes these local operations in the workspace and in-scope modified child repositories: Git inspection, authorized Task Branch creation from each resolved Base Branch, explicit-path staging, local commits, local rebase onto that same Base Branch, ff-only integration after the gate, and normal deletion of merged local Task Branches. Codex A MUST NOT absorb unrelated pre-existing changes.

Remote push or branch writes, force push, release or Git tag publication, destructive cleanup, forced branch deletion, and shared-history rewriting require explicit authority or persistent project policy.
