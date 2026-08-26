# codex-template Task Readiness Protocol

## States

### PASS

The task has sufficient clarity, evidence, decisions, repository access, and execution capability.

Behavior: continue silently.

### WARNING

A meaningful risk exists but no material user decision is required.

Behavior: report the warning and continue.

If a material user decision is required, use `BLOCKED`, not `WARNING`.

### BLOCKED

Stop substantive work when continuing requires missing critical input/evidence, an unresolved material decision, an unauthorized assumption, unavailable required capability, or violation of an accepted core design principle.

Request only the minimum information or decision required to proceed.

## Common Checks

- Goal clarity
- Required inputs
- Evidence availability
- Repository baseline
- Decision maturity
- Agent suitability
- Execution feasibility
- Verification feasibility
- Version impact

## codex-template Maintainer Profile

### Project-Agnostic Check

If a change to `template/` introduces assumptions about a specific language, framework, domain, build system, test framework, or component name, normally use:

```text
BLOCKED — Project-Agnostic Principle Violation
```

unless an approved design decision explicitly changes that principle.

### Governance / Payload Boundary

Determine whether the change belongs to codex-template governance or instantiated-project behavior.

If ownership is materially ambiguous and implementation depends on that decision, use `BLOCKED`.

### Evidence / Reference Check

If upstream evidence motivates the change, verify that authoritative evidence exists, ChatGPT Gap Analysis is complete, the result is `Change Proposed`, and approval exists when material.

Otherwise use:

```text
BLOCKED — Reference Review Required
```

### Architecture / ADR Check

If a task alters a core design principle, repository architecture, or instantiated-project contract, determine whether an ADR or explicit decision is required before implementation.

### Compatibility Check

If a breaking change is not explicitly authorized:

```text
BLOCKED — Breaking Change Not Authorized
```

### Validation Check

If required validation cannot be performed and the result would be unreliable, use `BLOCKED`.

## ChatGPT Profile

Emphasize evidence quality, source/baseline verification, design maturity, project-agnostic compatibility, governance vs payload ownership, and agent suitability.

A repository implementation task is normally:

```text
WARNING — Preferred Executor: Codex
```

ChatGPT may continue with design/task definition.

## Codex Profile

Emphasize actual repository state, approved design, scope, governance/payload boundary, architecture/ADR constraints, validation, and Final Version Impact.

A research-heavy or architecture-defining task without an approved design is normally:

```text
WARNING — Preferred Executor: ChatGPT
```

If implementation would require inventing the missing design decision, use `BLOCKED`.

## Version Impact

Use `NONE`, `PATCH`, `MINOR`, `MAJOR`, `UNKNOWN`.

`MAJOR` does not automatically mean `BLOCKED`; an unauthorized breaking change does.

`UNKNOWN` does not automatically mean `BLOCKED`; unresolved `UNKNOWN` becomes `BLOCKED` when the current phase cannot safely continue without resolving it.

## Hard Rules

- `PASS` should normally be silent.
- Material user confirmation required → `BLOCKED`.
- Missing authoritative evidence required for the task → `BLOCKED`.
- Project-agnostic violation in `template/` → normally `BLOCKED`.
- Do not silently invent architectural intent.
