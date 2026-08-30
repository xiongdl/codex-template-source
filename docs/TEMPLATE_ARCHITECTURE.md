# Template Architecture

## Two-Layer Repository

The repository is intentionally split into two layers.

### Layer A — Distributable Template

```text
template/
```

This content is copied into instantiated engineering projects.

It contains only project-agnostic engineering bootstrap material.

### Layer B — Template Governance

```text
docs/
tests/
VERSION
CHANGELOG.md
```

This layer exists only to design, validate, version, and evolve `codex-template`.

It must not leak into instantiated projects.

## Distributable Template Responsibilities

The payload provides:

- AI collaboration rules,
- a lightweight design-conversation protocol with explicitly authorized current state, auditable Checkpoints, and design Freeze before deriving a minimum-sufficient Task Contract,
- project initialization workflow,
- automatic pre-Initial-Commit Bootstrap and project-specific documentation,
- lean workspace and child-repository composition,
- honest incremental lifecycle inspection and verification,
- automation entry-point convention,
- workspace-owned Environment Modules composition introduced only for validated needs,
- lightweight formal-document and reproducible-figure conventions,
- traceability guidance.

## Governance Responsibilities

The governance layer provides:

- design principles,
- template architecture,
- change policy,
- template ADRs,
- validation,
- versioning,
- release history.

## Lifecycle

```text
Design
  ↓
Modify template/
  ↓
Validate
  ↓
Version
  ↓
Release
  ↓
Instantiate
  ↓
Observe real-project use
  ↓
Feed improvements back
```

## Upstream Evidence Layer

```text
references/
```

contains curated external evidence used to evaluate template evolution.

```text
scripts/
```

contains maintenance automation for the `codex-template` repository itself.

Neither directory is part of the distributable `template/` payload.

The evidence flow is:

```text
Upstream Source
→ Reference Registry
→ Change Detection
→ Human/ChatGPT Review
→ ADR when material
→ Template Change
→ Validation
→ Versioned Release
```

## Snapshot Evidence Boundary

Human-curated upstream evidence is stored under:

```text
references/openai/snapshots/
```

This is primary evidence.

`SOURCES.md` and `notes/` are derived reference-maintenance artifacts.
They are not the human-maintained source of truth.

Snapshot format is enforced by repository validation.

## Dogfooding Architecture

`codex-template` itself is governed as an AI-assisted engineering project through root `CHATGPT.md`, `AGENTS.md`, `.ai/WORKFLOW.md`, and `.ai/TASK_READINESS.md`.

The root project and distributable `template/` share role separation, readiness semantics, version-impact concepts, and verification discipline, but their policy contents differ because their responsibilities differ.

## Shared AI Engineering Contract

Both layers use the same core model:

- ChatGPT as Design Owner;
- Codex A as Implementation Owner;
- Codex B as read-only Review Owner in a new Codex session explicitly created by the human user;
- immutable `READ_ONLY` / `CHANGE` Task Types;
- committed-state Independent Review for `CHANGE`;
- one repository Default Base Branch, with `main` as the template default;
- one immutable workspace Base Branch and one short-lived workspace `task/*` Task Branch per `CHANGE` Task;
- at most one associated Task Branch per modified child repository, with each repository's Task Branch creation and final integration against its own stable Base Branch;
- ff-only integration of the exact approved commit;
- four standardized cross-role artifacts.

The distributable payload treats the workspace as the composition anchor for governance, project documentation, orchestration, and managed child repositories. It does not prescribe generic `components/`, `tests/`, or `integration/` directories and does not inject workspace governance into child repositories.

The human user is the explicit Independent Review handoff boundary: Codex A stops after producing the formal Review Prompt, the human creates Codex B's session and transfers the prompt, and the human returns Codex B's formal Review Report. Internal or sub-agent review is informational and cannot satisfy the gate.

Technical approval and final Task disposition are separate boundaries. After approval, Codex A returns an Engineering Result Report before integration. ChatGPT / Design Owner advises the human, the human selects `INTEGRATE`, `REVISE`, or `ABORT` and returns that decision input to the Design Owner, then the Design Owner compiles a complete explicit prompt for human transfer to Codex A. Environment composition remains workspace-owned; automation remains with the engineering responsibility it performs.

Root `.ai/` policies govern maintenance of `codex-template`. `template/.ai/` contains the project-agnostic contract copied to instantiated projects. The files intentionally have layer-specific surrounding guidance while preserving these invariants.
