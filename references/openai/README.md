# OpenAI References

This directory contains curated upstream evidence used to evaluate and evolve `codex-template`.

It is not part of the distributable `template/`.

## Responsibility Split

### Human

Maintain only authoritative snapshot inputs:

```text
references/openai/snapshots/
```

### ChatGPT / Codex

May maintain derived material:

```text
SOURCES.md
notes/
docs/decisions/
template/
CHANGELOG.md
VERSION
```

based on reviewed snapshot evidence and project feedback.

## Evidence Flow

```text
Human updates snapshots/
        ↓
./scripts/check
        ↓
Derived source/index maintenance
        ↓
ChatGPT / Codex analysis
        ↓
No impact / Note / ADR
        ↓
Template change when justified
        ↓
Validation
        ↓
Versioned release
```

A snapshot update never automatically implies a template change.

See `snapshots/README.md` for strict naming and metadata rules.
