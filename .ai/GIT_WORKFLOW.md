# Git Workflow

## Repository-Local Branch Model

Every repository defines its own `Default Base Branch` in repository-specific governance or configuration. This generic workflow does not assign a Default Base Branch to any named repository.

For every repository modified by a `CHANGE` Task, resolve exactly one `Base Branch` for the complete Task lifecycle:

1. use the repository-specific Base Branch explicitly supplied by the Task Contract, when provided;
2. otherwise use that repository's Default Base Branch.

The Base Branch is the logical branch identity. The Base Commit is the expected `HEAD` of that resolved Base Branch for the applicable task, review, or integration state. A repository's Base Branch is immutable within the Task: it is both the source from which its Task Branch is created and the final merge target.

Each modified repository uses exactly one short-lived `Task Branch`, created from its resolved Base Branch. The branch namespace is `task/*`.

```text
Base Branch
└── task/<task-id>-<short-name>
```

Do not create a Task Branch in an affected but unmodified repository solely because it participates in inspection or verification. Do not require a framework-wide `main`, `dev`, `develop`, `feature/*`, `bugfix/*`, or `hotfix/*` taxonomy. `READ_ONLY` tasks require no Task Branch.

For every modified repository, the invariant is:

```text
Task Branch creation source == final merge target == Base Branch
```

Each modified repository independently establishes its Base Branch, Base Commit, Task Branch, Review Commit, repository-required verification, and Integration Gate state.

## Task History and Review Target

Multiple coherent commits are allowed. Before Review Attempt 1, local history may be cleaned up. After Review Attempt 1 begins, reviewed history should not normally be rewritten; review fixes are appended as commits. A rebase onto the updated Base Branch is allowed but invalidates prior approval.

Formal Independent Review requires a committed Review Target in every modified repository:

1. implement;
2. run that repository's required verification;
3. create a local commit;
4. identify the repository-specific Base Commit and Review Commit.

The Review Commit must be that repository's Task Branch `HEAD`. Review covers the complete `Base Commit..Review Commit` Task diff and the repository in the Review Commit state, not only the final commit.

After `CHANGES_REQUESTED`, a new Review Commit is required in each modified repository whose Finding resolution changes tracked state. The repository changes must be verified and committed, and its new Task Branch `HEAD` becomes the next Review Commit. Dependent exact-commit references must be updated when required. If resolution is solely through Task Contract revision, Design Owner decision, required external input, or requirement clarification and tracked state is unchanged, do not create an artificial or empty commit; the next Review Attempt may use the same Review Commit.

## Integration Gate

Codex A owns local integration after the post-ERR decision. Integrate each modified repository only when:

- the Task-level Independent Review is `APPROVED`;
- the Engineering Result Report has been returned and a new explicit `INTEGRATE` prompt has been received;
- that repository's Task Branch `HEAD` equals its Approved Commit;
- its tracked working tree is clean;
- its Task Branch is based on the current resolved Base Branch;
- its required verification passes;
- all dependency-order prerequisites for this integration step are satisfied.

Integration must use:

```bash
git merge --ff-only
```

Do not squash the reviewed commits by default. In every modified repository, the target invariant is:

```text
Reviewed Commit == Approved Commit == Integrated Commit
```

If a resolved Base Branch advances before integration, rebase the corresponding Task Branch onto the current Base Branch, re-verify, identify the new Base and Review Commit identities, update dependent exact-commit references when required, obtain a new Independent Review of the complete Task Review Target, and retry. Base Branch advancement alone is not a blocked condition.

## Multi-Repository Tasks

A multi-repository Engineering Task composes the same repository-local lifecycle for each modified repository. It does not create separate workspace and managed-repository lifecycle models.

At Task start, record the expected `Repository Scope`: every repository affected by implementation or verification, whether each is modified or affected but unmodified, and the applicable path and Base Branch when known. A modified repository is one whose tracked state the Task changes. An affected but unmodified repository participates only in inspection or verification and requires no Task Branch, Review Commit, or integration operation. The Task need not modify or otherwise place a workspace repository into the Git lifecycle when only a managed repository changes. Scope expansion follows normal Task revision and design-decision rules.

Record `Repository Dependencies` that constrain commit recording, validation, integration, or publication. Do not infer a universal workspace-first or managed-repository-first hierarchy. Coordinate Task Branch creation, review preparation, integration, and authorized publication in a dependency-consistent order established by the Task.

Each modified repository contributes one repository-specific Review Target containing its exact Base Commit and Review Commit. Together these pairs form the complete Task Review Target. Begin the single Task-level Formal Independent Review only after that complete target exists. The review evaluates every repository-specific target plus relevant cross-repository and dependency consistency, and produces one Task-level conclusion.

When one modified repository records or references the exact commit of another modified repository, the referenced repository must establish its Review Commit before the referencing repository establishes its corresponding Review Commit. If tracked-state resolution of `CHANGES_REQUESTED` changes a referenced Review Commit, update dependent exact-commit references, re-verify and establish new Review Commits where required before the next Review Attempt.

After approval and explicit integration authorization, integrate all modified repositories in dependency-consistent order using each repository's own ff-only Integration Gate. If coordinated integration is interrupted, preserve the already integrated approved commits, identify the remaining dependency-consistent steps, and resume until the approved Task composition is consistent; database-style rollback is not required.

Local completion does not require publication. With separate Human `REMOTE` authorization, publish modified repositories in an order that preserves dependency consistency. Before publishing a referencing commit, verify that every required referenced commit is reachable from its authorized official remote.

### Workspace Recording a Managed-Repository Commit

When a Task modifies both a workspace and a managed repository and the workspace records the managed repository's exact commit, apply this dependency-specific orchestration without changing either repository's local lifecycle:

1. create the workspace Task Branch from the workspace's resolved Base Branch;
2. create the managed-repository Task Branch from that repository's resolved Base Branch;
3. establish the managed-repository Review Commit;
4. record that exact Review Commit in the workspace and establish the workspace Review Commit;
5. begin Formal Independent Review only after both repository-specific targets form the complete Task Review Target;
6. after Task-level approval and explicit integration authorization, integrate the managed repository first;
7. verify that the managed-repository commit recorded by the approved workspace Review Commit is the commit integrated into the managed repository's resolved Base Branch;
8. integrate the workspace last.

Authorized publication follows the same dependency: publish and verify reachability of the managed-repository commit before publishing the referencing workspace commit.

## Permissions

A `CHANGE` Task Contract authorizes Codex A to perform these operations in each in-scope modified repository: inspect Git state; create its authorized Task Branch from its resolved Base Branch; explicitly stage task-related paths; commit; locally rebase onto the same Base Branch; perform ff-only local integration after the gate; and delete a normally merged local Task Branch.

Codex A MUST NOT absorb unrelated pre-existing working-tree changes. Prefer explicit-path staging.

Remote push, remote branch creation or deletion, force push, release publication, Git tag publication, destructive cleanup, forced branch deletion, and rewriting shared history require explicit authorization or persistent project policy.
