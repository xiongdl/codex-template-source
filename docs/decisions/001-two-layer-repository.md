# ADR-001: Separate Template Payload from Template Governance

## Status

Accepted

## Context

The repository must both provide a clean project template and support long-term evolution of that template.

If template-maintainer documentation and validation are placed inside the distributable payload, every instantiated project inherits irrelevant files.

## Decision

Use:

```text
template/
    → distributable project template

docs/ + tests/ + VERSION + CHANGELOG.md
    → codex-template governance
```

## Consequences

Benefits:

- clean instantiated projects,
- explicit template governance,
- independent validation and versioning,
- clearer long-term evolution.

Cost:

- one extra repository layer,
- consumers must instantiate from `template/`, not blindly copy the whole repository.
