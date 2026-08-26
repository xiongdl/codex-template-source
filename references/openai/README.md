# OpenAI References

This directory contains curated upstream evidence used to evaluate and evolve `codex-template`.
It is not part of the distributable `template/`.

## Responsibility Model

### Human

- Select authoritative OpenAI material worth preserving.
- Add/update primary evidence under `snapshots/`.
- Approve material template design changes when required.

### ChatGPT

- Read and analyze the primary snapshot.
- Extract durable engineering practices.
- Distinguish durable guidance from product/model-specific behavior.
- Compare evidence against an exact `codex-template` baseline.
- Perform practice-by-practice Gap Analysis.
- Draft/update the formal reference note.
- Recommend exactly one outcome: `No Change`, `Monitor`, or `Change Proposed`.
- Identify whether an ADR is warranted.

Every Gap Analysis must pin the exact repository commit and template version.
A new snapshot does not imply that the template should change.

### Codex

- Inspect the actual repository before applying an approved note.
- Add/update notes under `notes/`.
- Maintain `SOURCES.md` and related derived artifacts consistently.
- Implement approved template changes only when explicitly justified.
- Update governance/versioning artifacts when required.
- Run `./scripts/check`.
- Report changed files and verification results.

Codex must not infer that a new snapshot automatically requires a template change.

## Reference Review Workflow

```text
Human
  │ curate authoritative evidence
  ▼
snapshots/                  Primary Evidence
  │
  ▼
ChatGPT
  ├── analyze
  ├── extract durable practices
  ├── pin template baseline
  ├── Gap Analysis
  └── recommend decision
          │
          ▼
      reference note
          │ approval when material
          ▼
        Codex
          ├── inspect actual repository
          ├── apply note
          ├── maintain derived artifacts
          ├── implement approved changes
          └── ./scripts/check
                  │
                  ▼
                 Git
```

## Evidence Model

```text
snapshots/        = Primary Evidence
SOURCES.md        = Derived Index
notes/            = Derived Analysis
docs/decisions/   = Durable Engineering Decisions
template/         = Implemented Project Template
```

See `snapshots/README.md` for snapshot rules.
See `notes/NOTE_TEMPLATE.md` for the formal review-note format.
