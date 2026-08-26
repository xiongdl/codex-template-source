# Change Policy

A proposed change to `codex-template` should answer:

1. Is it project-agnostic?
2. Is it useful across many project types?
3. Does it reduce repeated prompting or manual engineering work?
4. Does it improve modularity, extensibility, testability, automation, reproducibility, traceability, maintainability, or AI operability?
5. What maintenance burden does it add?
6. Could `PROJECT_INIT.md` discover or generate this instead of hard-coding it?
7. Can the benefit be achieved with fewer files or simpler rules?
8. Does it duplicate existing guidance?
9. Has real project usage demonstrated the need?
10. How will the change be validated?

## Change Classes

### Patch

Clarifications, typo fixes, validation improvements, and non-breaking refinements.

### Minor

New project-agnostic capabilities or conventions that do not fundamentally alter the workflow.

### Major

Breaking structural or workflow changes that materially affect instantiated projects.

## Material Change Requirements

For meaningful template changes:

- update relevant governance documentation,
- update validation when applicable,
- update `CHANGELOG.md`,
- update `VERSION`,
- create an ADR if the change alters core architecture or design principles.

## Upstream Evidence

When a template change is motivated by OpenAI documentation or product evolution:

1. register or update the source in `references/openai/SOURCES.md`,
2. record the template-relevant insight in `references/openai/notes/` when useful,
3. determine whether the change is general enough for a project-agnostic template,
4. create an ADR for material architectural changes,
5. modify `template/` only after this evaluation,
6. run template validation,
7. update version and changelog.

Upstream changes must never directly auto-edit the distributable template.

## Snapshot Evidence Policy

Human-maintained OpenAI evidence lives only under:

```text
references/openai/snapshots/
```

Snapshot structure is mechanically validated.

A source directory must follow:

```text
OAI-NNN-<slug>/
```

and contain `metadata.yaml`.

Snapshot filenames must follow:

```text
YYYY-MM-DD.(pdf|html|md)
```

Run `./scripts/check` before commit.

Invalid snapshot naming, metadata, or structure is a repository validation failure.
