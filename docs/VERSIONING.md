# codex-template Versioning

`codex-template` uses `MAJOR.MINOR.PATCH`.

The same Version Impact vocabulary used by instantiated projects applies to template governance:

- `NONE`
- `PATCH`
- `MINOR`
- `MAJOR`
- `UNKNOWN`

## Core Principle

> Change determines Version Impact.  
> Release determines Version Number.

## PATCH

Backward-compatible fixes or governance refinements that do not materially change the instantiated-project contract.

## MINOR

Backward-compatible new template capability or engineering convention.

## MAJOR

Breaking changes to the distributable template structure, required workflow, or instantiated-project contract.

## UNKNOWN

The impact is not yet reliably classified and must be resolved before release.

## Release Consistency

A formal `codex-template` release requires consistency between:

- root `VERSION`,
- root `CHANGELOG.md`,
- Git tag `v<version>`.

Material changes should follow `docs/CHANGE_POLICY.md`.
