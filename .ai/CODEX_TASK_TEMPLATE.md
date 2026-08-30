# Codex Task Prompt

## Task Identity

- Task ID:
- Revision:
- Task Type: `READ_ONLY | CHANGE`
- Base Branch: `NOT_APPLICABLE | <branch> | INHERIT_DEFAULT`

## Authoritative Task Core

The sections in this core contain the transient task-specific engineering intent. The canonical Original Core operand is all raw text after the newline terminating the `## Authoritative Task Core` boundary line and before the `## End Authoritative Task Core` boundary line. The boundary lines are framing and are not part of the operand. When preparing Independent Review, Codex A MUST copy this entire operand exactly into the Codex Review Prompt. Copying is textual equality, not semantic equivalence: Codex A MUST NOT rewrite, summarize, normalize, reformat, correct, reorder, abbreviate, expand, translate, or otherwise modify it, including its wording, punctuation, Markdown, whitespace, ordering, or content. Extraction and comparison perform no preprocessing, including no trim, dedent, newline normalization, or Markdown normalization. If the handoff medium cannot preserve the Core exactly, use a representation or transfer mechanism that can. Any later implementation interpretation or clarification belongs outside this core and must be clearly identified as Codex A-produced context.

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

## Preliminary Version Impact

`NONE | PATCH | MINOR | MAJOR | UNKNOWN`

Reason:

Repository-level review and Git rules are defined by `.ai/AI_HANDOFF_PROTOCOL.md` and `.ai/GIT_WORKFLOW.md`.
