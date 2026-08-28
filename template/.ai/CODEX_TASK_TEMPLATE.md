# Codex Task Prompt

## Task Identity

- Task ID:
- Revision:
- Task Type: `READ_ONLY | CHANGE`
- Base Branch: `NOT_APPLICABLE | <branch> | INHERIT_DEFAULT`

## Authoritative Task Core

The sections in this core contain transient task-specific engineering intent. When preparing Independent Review, Codex A MUST transfer this core verbatim to the Codex Review Prompt and MUST NOT reinterpret, summarize, weaken, replace, or otherwise rewrite it. Formatting-only transformations may preserve unchanged meaning. Later implementation interpretation belongs outside this core as Codex A-produced context.

## Goal

## Context

## In Scope

## Repository Scope

Identify the workspace and expected changed child repositories. For each expected modified repository, record its path and Base Branch when known. Use `WORKSPACE_ONLY` when applicable.

## Out of Scope

## Requirements

## Constraints / Decisions

## Acceptance Criteria

## End Authoritative Task Core

## Authoritative References

## Verification

Specify relevant component-local, cross-component, project-level/end-to-end, regression, or other project-defined checks.

## Preliminary Version Impact

`NONE | PATCH | MINOR | MAJOR | UNKNOWN`

Reason:

Repository-level review and Git rules are defined by `.ai/AI_HANDOFF_PROTOCOL.md` and `.ai/GIT_WORKFLOW.md`.
