# codex-template Maintenance Scripts

These scripts maintain the **template repository itself**.

They are not copied into instantiated projects.

## `check_openai_references.py`

Checks the official OpenAI sources registered in:

```text
references/openai/SOURCES.md
```

Run:

```bash
python scripts/check_openai_references.py
```

After manually reviewing the current upstream state, establish/update the baseline with:

```bash
python scripts/check_openai_references.py --update-state
```

A changed source is only a review signal.

The script must never automatically modify `template/`.
