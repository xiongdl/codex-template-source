# Template Architecture

## Independent Repositories

The maintenance architecture contains two independent Git repositories:

```text
codex-template-source          source, governance, validation, release workspace
└── template/                  Git submodule checkout of codex-template

codex-template                 independent distributable template repository
```

`codex-template-source` develops, governs, validates, and prepares releases of `codex-template`; it is not itself the distributable template repository. `codex-template` remains independently usable as the upstream repository from which downstream projects inherit Git history.

The source workspace does not depend on a particular permitted downstream instantiation method. Downstream project instantiation and upstream synchronization are consumer-facing concerns, separate from this internal maintainer architecture. Downstream projects do not inherit the source workspace's submodule relationship.

## Submodule Registration and Baseline

Git submodules are the canonical repository-registration and baseline mechanism for repositories managed by the source workspace:

- `.gitmodules` records the managed repository's path and remote URL;
- the source workspace gitlink records the exact accepted `codex-template` baseline revision;
- `template/` provides a checkout of that independent repository for development and validation.

No separate manifest duplicates submodule path, URL, or revision information. A managed-repository checkout may advance beyond or otherwise diverge from the recorded gitlink during normal authorized development. That checkout state is not inherently an error; the source workspace's gitlink continues to identify its accepted baseline until deliberately updated by a reviewed Task.

## Repository Responsibilities

The source workspace owns:

- design principles and architecture decisions;
- evidence and change policy;
- cross-repository validation and release preparation;
- source-workspace AI and Git governance;
- source-workspace versioning and release history.

The independent distributable repository owns the project-agnostic bootstrap material inherited by downstream projects, including its own documentation, AI collaboration contract, scripts, version, changelog, and Git history.

Source-workspace governance is not copied into downstream projects. Distributable content is not duplicated outside the `template/` submodule.

## Repository-Local Engineering Lifecycle

Every repository modified by an Engineering Task follows the same project-agnostic repository-local Git lifecycle: it resolves its own Base Branch and Base Commit, creates its own Task Branch, establishes a verified Review Commit, satisfies its Integration Gate, and integrates ff-only after approval and explicit authorization.

Multi-repository behavior is Task-level composition of those repository-local lifecycles, not a separate workspace-versus-managed-repository workflow. The Task records repository scope and dependencies, distinguishes modified repositories from affected but unmodified repositories, assembles the exact Base Commit / Review Commit pair from every modified repository into one Task Review Target, and receives one Task-level Independent Review conclusion. Coordination and authorized publication preserve dependency consistency.

When the source workspace records the exact commit of a modified managed repository, the managed repository establishes its Review Commit before the workspace records it and establishes its own Review Commit. After approval, the managed repository integrates before the referencing workspace. These are dependency-specific orchestration rules, not distinct local lifecycles.

## Validation and Release Flow

```text
Evidence or real-project feedback
→ Design decision
→ Repository-scoped implementation
→ Repository-required and cross-repository validation
→ Task-level Independent Review
→ Explicit dependency-consistent integration
→ Authorized release preparation and publication
→ Downstream observation
```

The source workspace validates the `codex-template` revision recorded by its gitlink for baseline and release preparation. During an authorized multi-repository Task, validation may also inspect the managed checkout's intended Review Commit as specified by that Task.

## Evidence Boundary

Human-curated upstream evidence is stored under `references/openai/snapshots/`. `SOURCES.md` and `notes/` are derived reference-maintenance artifacts, not the human-maintained source of truth. Snapshot format is mechanically validated before evidence informs an approved design decision.

## Shared AI Engineering Contract

The source workspace and distributable repository use the same core ownership model:

- ChatGPT is Design Owner;
- Codex A is Implementation Owner;
- Codex B is read-only Review Owner in a new human-created session;
- Task Type is immutable and limited to `READ_ONLY` and `CHANGE`;
- every `CHANGE` uses committed repository-specific Review Targets and one Task-level conclusion;
- exact approved commits integrate ff-only;
- standardized cross-role artifacts carry transient task and review intent.

Root `.ai/` policies govern `codex-template-source`. Files under the independent repository's `template/.ai/` checkout govern instantiated-project behavior. Detailed Git rules remain authoritative in root `.ai/GIT_WORKFLOW.md` for source-workspace maintenance and in the managed repository's own governance for its local tasks.
