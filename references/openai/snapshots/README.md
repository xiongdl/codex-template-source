# OpenAI Snapshots

Human maintenance responsibility is intentionally narrow:

> Add or update authoritative OpenAI snapshot files under this directory.

The rest of the reference system may be maintained by ChatGPT/Codex.

## Source Directory Naming

Each tracked source must use:

```text
OAI-NNN-<slug>/
```

Rules:

- `NNN` is a zero-padded numeric ID, for example `001`.
- `<slug>` uses lowercase ASCII letters, digits, and `-` only.
- IDs must be unique.
- Directory names must remain stable once referenced by notes or decisions.

Example:

```text
OAI-001-harness-engineering/
```

## Required Metadata

Each source directory must contain:

```text
metadata.yaml
```

Required fields:

```yaml
id: OAI-001
title: Harness engineering
source: OpenAI
url: https://openai.com/...
```

Rules:

- `id` must match the directory ID.
- `source` must be exactly `OpenAI`.
- `url` must use `https://` and an approved OpenAI domain.

## Snapshot File Naming

Snapshot files must use:

```text
YYYY-MM-DD.<ext>
```

Allowed extensions:

```text
.pdf
.html
.md
```

Examples:

```text
2026-08-26.pdf
2026-11-10.html
2027-01-03.md
```

Rules:

- the date must be a real calendar date,
- only one snapshot per source per date,
- filenames must not contain additional suffixes such as `final`, `v2`, or timestamps,
- temporary/editor files are not allowed.

## Validation

Run:

```bash
./scripts/check
```

Invalid snapshot structure, names, or metadata cause a non-zero exit status and should block commit/CI.

The snapshot tree is primary evidence.
Do not store template analysis or decisions here.
