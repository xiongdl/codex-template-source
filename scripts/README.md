# codex-template Maintenance Scripts

These scripts maintain the `codex-template` repository itself.

They are not copied into instantiated projects.

## `./scripts/check`

Canonical repository validation entry point.

It runs:

```text
tests/validate_template.py
tests/validate_references.py
```

Use:

```bash
./scripts/check
```

Human contributors, Codex, and CI should use this same entry point.

## Reference Maintenance

OpenAI web pages are not fetched automatically.

Human responsibility:

```text
update references/openai/snapshots/
```

Repository validation checks:

- source directory naming,
- metadata presence and consistency,
- approved OpenAI URLs,
- snapshot filename/date/extension rules.

Derived indexes, notes, decisions, and template changes are handled separately.
