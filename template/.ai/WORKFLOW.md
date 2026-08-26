# AI Engineering Workflow

## Roles

### Human
Owns goals, priorities, constraints, trade-offs, and final decisions.

### ChatGPT
Best for research, architecture, design alternatives, trade-off analysis, task definition, and review.

### Codex
Best for repository inspection, implementation planning, coding, testing, debugging, refactoring, automation, and documentation updates.

### Repository
The repository is long-term engineering memory.

### CI / Automation
Provides repeatable execution of build, test, verification, and quality checks.

## Standard Flow

```text
Human Goal
   ↓
Understand Current Project
   ↓
ChatGPT Research / Design
   ↓
Design Decision
   ↓
Codex Task
   ↓
Codex Inspect / Plan
   ↓
Implementation
   ↓
Build / Test / Verify
   ↓
Documentation / Status Update
   ↓
ChatGPT Review
   ↓
Next Task
```

## Verification Hierarchy

```text
Component-local
      ↓
Cross-component Integration
      ↓
Project-level / End-to-End
```

## Shared Engineering Interface

Where practical, Human, Codex, and CI should use the same repository-defined commands.

## Completion Rule

Implementation
→ Verification
→ Documentation
→ Status Update
