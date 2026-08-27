# ADR-003: Bootstrap and Multi-Repository Workspace Model

## Status

Accepted

## Context

Real AI-assisted projects may begin before an Initial Commit and may keep implementation in multiple child Git repositories. Requiring the full reviewed CHANGE lifecycle before a valid `HEAD`, prescribing generic implementation directories, or copying workspace governance into children adds cost without improving the relevant risk boundary.

## Decision

- Detect Bootstrap solely by absence of a valid Git `HEAD`; the Initial Commit transitions into Normal Engineering.
- Treat Bootstrap as a lifecycle mode, not a third Task Type, and establish one coherent project-specific baseline.
- Keep the distributable payload a lean workspace for governance, project documentation, orchestration, and repository composition.
- Preserve child repositories' native layout and governance.
- Allow one coherent Engineering Task and one Independent Review Attempt to cover the workspace plus changed children, with exact child Review Commits recorded by the workspace.
- Prepare and integrate children first and the workspace last; keep remote publication separately authorized.

## Consequences

The template no longer prescribes `components/`, `tests/`, or `integration/`. Bootstrap may honestly leave executable lifecycle capabilities unavailable while `status` and `verify` describe and validate the supported baseline. Multi-repository review artifacts carry per-repository commit identity without adding Task IDs, verdicts, or formal artifact types.
