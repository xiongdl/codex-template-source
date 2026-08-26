# AI Engineering Workflow

## Goal
Create a repeatable collaboration loop between the human engineer, ChatGPT, Codex, and the repository.

## Roles

### Human
Owns goals, priorities, constraints, risk acceptance, and final technical decisions.

### ChatGPT — Think / Research / Design / Review
Use ChatGPT to:
- clarify requirements and constraints;
- research technologies and alternatives;
- analyze architecture and trade-offs;
- challenge assumptions;
- turn decisions into design notes and executable Codex tasks;
- review implementation results and plan the next iteration.

ChatGPT should not be treated as the authoritative copy of project state. Important conclusions must be recorded in the repository.

### Codex — Inspect / Implement / Test / Debug
Use Codex to:
- inspect the actual repository;
- understand existing code and tests;
- create an implementation plan;
- modify code;
- add tests;
- run builds, lint, simulation, benchmarks, and regression tests;
- debug failures;
- update project documentation and status.

Codex should not silently make broad architecture changes when design intent is unclear.

### Repository — Long-term Memory / Source of Truth
The repository records:
- code and tests;
- architecture;
- module designs;
- important technical decisions and rationale;
- current project status.

Conversation = working memory. Repository = long-term memory.

## Standard lifecycle

```text
Human goal / problem
        ↓
ChatGPT: understand + research + design
        ↓
Human: decide
        ↓
Record design / decision when needed
        ↓
ChatGPT: produce Codex Task
        ↓
Codex: inspect repository
        ↓
Codex: plan
        ↓
Codex: implement
        ↓
Codex: test / debug
        ↓
Codex: update docs + PROJECT_STATUS
        ↓
Human / ChatGPT: review
        ↓
Next task
```

## Task sizing
Prefer tasks with a clear goal and independently verifiable completion criteria. Split broad redesigns into incremental tasks when possible.

A good task specifies:
- context;
- current behavior;
- target behavior;
- decisions already made;
- constraints;
- scope and non-goals;
- verification;
- acceptance criteria.

## When a design decision is required
Create an ADR under `docs/decisions/` when a decision:
- changes architecture or a stable interface;
- chooses between meaningful alternatives;
- establishes a constraint future work must understand;
- would otherwise cause someone to ask “why is it done this way?” later.

## Definition of Done
A non-trivial task is done only when:
- implementation is complete;
- relevant tests/checks pass, or failures are explicitly documented;
- documentation matches the resulting system;
- project status is updated when the milestone/status changed;
- remaining limitations are visible.
