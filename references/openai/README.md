# OpenAI References

This directory contains curated upstream evidence used to evaluate and evolve `codex-template`.

It is **not** part of the distributable project template.

## Purpose

The reference workflow is:

```text
Official OpenAI Source
        ↓
Track / Review
        ↓
Extract Template-Relevant Insight
        ↓
Evaluate Generality
        ↓
ADR / Design Decision when needed
        ↓
Modify template/
        ↓
Validate
        ↓
CHANGELOG + VERSION
```

## Directory Structure

```text
references/openai/
├── README.md
├── SOURCES.md
├── notes/
└── snapshots/
```

### `SOURCES.md`

Registry of upstream sources worth monitoring.

### `notes/`

Local analysis and distilled implications for `codex-template`.

Notes should summarize rather than reproduce source documents.

### `snapshots/`

Optional immutable copies of source artifacts when there is a strong reason to preserve a specific upstream version.

Do not mirror the OpenAI website here by default.

## Source Policy

Prefer first-party OpenAI sources.

Suggested priority:

1. Official Codex documentation / specifications
2. OpenAI engineering articles describing Codex or agent engineering
3. Official Codex release notes / product documentation
4. Other official OpenAI materials with direct template relevance

Every source entry should record:

- source title,
- official URL,
- source category,
- relevance,
- last reviewed date,
- current status,
- template implications.

A source change is evidence for review, not an automatic instruction to change the template.
