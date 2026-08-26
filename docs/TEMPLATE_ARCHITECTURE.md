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
- project initialization workflow,
- architecture/status/reproducibility documentation bootstrap,
- component and integration abstractions,
- verification hierarchy,
- automation entry-point convention,
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
