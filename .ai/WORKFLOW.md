# codex-template AI Engineering Workflow

## Purpose

`codex-template` dogfoods the same AI-assisted engineering principles it provides to instantiated projects.

## Roles

### Human

Owns project goals, authoritative snapshots, acceptance of trade-offs, approval of material template changes, and final release decisions.

### ChatGPT

Preferred for research, reference analysis, requirements, design, architecture, Gap Analysis, change proposals, Preliminary Version Impact, task definition, and review.

### Codex

Preferred for repository inspection, implementation, refactoring, validation, consistency maintenance, Final Version Impact, and release preparation.

## Standard Flow

```text
Human Request
      ↓
AI Task Readiness
      ↓
PASS / WARNING / BLOCKED
      ↓
Research / Understand
      ↓
Design / Gap Analysis
      ↓
Decision / Change Proposal
      ↓
Preliminary Version Impact
      ↓
Codex Task
      ↓
Repository Inspection
      ↓
Codex Task Readiness
      ↓
Implementation
      ↓
./scripts/check
      ↓
Final Version Impact
      ↓
Documentation / ADR / Changelog
      ↓
Release when appropriate
```

## Reference-Driven Change

```text
Human updates snapshot
      ↓
ChatGPT analyzes evidence
      ↓
No Change / Monitor / Change Proposed
      ↓
Only approved Change Proposed
      ↓
Codex implementation
      ↓
Validation
```

A new reference never directly authorizes modification of `template/`.

## Dogfooding Principle

The root project and `template/` share engineering principles but do not mechanically share identical policy files because their responsibilities differ.

## Task Completion vs Release

Task completion does not automatically change the release number.

Task determines Version Impact.
Release determines Version Number.
