# ChatGPT Entry Point for codex-template

This file is the explicit ChatGPT bootstrap entry point for maintaining `codex-template` itself.

`codex-template` is a real engineering project whose product is the distributable `template/`.

## Bootstrap

At the beginning of a new ChatGPT conversation about this repository, read:

1. `VERSION`
2. `.ai/TASK_READINESS.md`
3. `.ai/WORKFLOW.md`
4. `docs/DESIGN_PRINCIPLES.md`
5. `docs/TEMPLATE_ARCHITECTURE.md`
6. `docs/CHANGE_POLICY.md`

Then load task-specific context progressively.

If required bootstrap files are unavailable, report:

```text
BLOCKED — Project Bootstrap Failed
```

and stop repository-specific substantive work.

## Preferred Role

ChatGPT is primarily responsible for:

- upstream research,
- reference analysis,
- requirements,
- template architecture,
- design alternatives,
- trade-off analysis,
- Gap Analysis,
- change proposals,
- Preliminary Version Impact,
- Codex task definition,
- review.

Repository modification, validation, and release preparation are normally delegated to Codex.

## Progressive Context Loading

Load only the context required for the task.

For reference-driven change, read the relevant snapshot/note and reference governance.
For template architecture change, read design principles, template architecture, and relevant ADRs.
For release/version work, read versioning policy, changelog, and VERSION.

## Task Readiness

Before substantive work, apply `.ai/TASK_READINESS.md` using the ChatGPT profile.

- `PASS` → continue silently.
- `WARNING` → report the risk and continue.
- `BLOCKED` → stop substantive work and request only the minimum information or decision needed.

Do not silently bypass project-agnostic constraints, missing evidence, unverified repository baselines, or unresolved architectural decisions.
