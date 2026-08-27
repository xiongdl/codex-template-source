# Project Bootstrap

Use this contract whenever the project has no valid Git `HEAD`: either the directory is not a Git repository or Git has no commit. A valid `HEAD` automatically ends Bootstrap and starts Normal Engineering. Do not add a persistent lifecycle flag.

Bootstrap is a repository lifecycle mode, not a third Engineering Task Type. Before the Initial Commit it does not require a Task ID, Task Branch, Base Commit, Review Commit, Independent Review, integration, or Engineering Result Report.

## Outcome

Create one coherent, honest Initial Commit that makes the project ready for its next normal Engineering Task. Infer what can safely be learned from the user's request, repository metadata, template, and existing child repositories. Ask only for genuinely project-defining decisions that cannot be inferred.

Establish, as applicable:

- project identity, purpose, goals, and useful non-goals;
- repository composition and project-specific repository roles;
- supplied branch or revision pins;
- workspace versus child-repository responsibilities and modification boundaries;
- the Default Base Branch used after Bootstrap;
- project-level documentation and validation boundaries;
- a minimal lifecycle inspection/verification interface;
- honest initial capability and project status.

Do not create a deliberately skeletal baseline and defer obvious initialization work into artificial Tasks. Do not implement genuine product or engineering capabilities merely to finish Bootstrap. Bootstrap establishes readiness for engineering; later Engineering Tasks establish capabilities.

## Inspect and Preserve

Inspect the actual workspace and any existing child repositories before assuming structure. Preserve child repositories' native source layout, build systems, tests, documentation, and conventions. Do not restructure them to match the workspace, and do not inject workspace copies of `AGENTS.md`, `CHATGPT.md`, `.ai/`, `PROJECT_STATUS.md`, Task artifacts, or Review artifacts.

The workspace is primarily the composition anchor for AI governance, project-level documentation, orchestration, and repository composition. `docs/`, `scripts/`, and `third_party/` are useful conventions; implementation directories arise only from project design.

## Documentation and Versioning

Create or update the project-level `README.md`, `docs/ARCHITECTURE.md`, `docs/PROJECT_STATUS.md`, and `docs/REPRODUCIBILITY.md` to describe the real project and its repository composition.

Inspect existing `VERSION`, tags, package/release metadata, and `CHANGELOG.md`. Preserve an existing authoritative versioning scheme. For a genuinely new project, initialize `VERSION` to `0.1.0` with `CHANGELOG.md` and `docs/VERSIONING.md`. If authoritative version sources conflict materially, stop with `BLOCKED — Version Source Conflict` and request the minimum decision needed.

## Lifecycle Interface

Treat commands in two groups:

```text
Inspection / Validation: status, verify
Executable Lifecycle:    setup, build, test, clean
```

`status` is observational, low-cost, safe, and non-destructive. It reports current capability honestly, including `NOT_IMPLEMENTED` or `UNAVAILABLE` when appropriate.

`verify` checks only the baseline and capabilities currently claimed to be supported. Bootstrap verification may check workspace structure, identity/configuration, governance consistency, repository presence, requested pins, modification boundaries, and lifecycle configuration. It must not imply that unsupported build, test, simulation, toolchain, or hardware capability was verified.

Bootstrap does not require complete `setup`, `build`, `test`, or `clean` implementations. Later coherent Engineering Tasks may enable them incrementally.

## Initial Commit

Run the cheapest deterministic checks that provide reasonable confidence in the declared baseline. Record actual checks and limitations in project status. Then create the Initial Commit. Once `git rev-parse --verify HEAD` succeeds, route all further work through `.ai/WORKFLOW.md`, `.ai/AI_HANDOFF_PROTOCOL.md`, and `.ai/GIT_WORKFLOW.md`.

Summarize the initialized composition, supported capabilities, verification performed, limitations, and recommended first meaningful Engineering Task. Do not create a separate formal Bootstrap Result artifact.
