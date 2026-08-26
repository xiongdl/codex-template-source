# Codex Task: <short task name>

## Context
Why is this work needed? What user/system problem does it solve?

## Current Behavior
Describe the relevant behavior today. Reference concrete modules/files when known.

## Goal
Describe the desired end state in observable terms.

## Design Decisions
List decisions already made. Codex should implement these rather than reopen them unless repository evidence reveals a conflict.

- Decision 1:
- Decision 2:

## Constraints
- Compatibility:
- Performance/resource constraints:
- Interface/protocol constraints:
- Other invariants:

## Scope
This task includes:
- ...

## Non-goals
This task intentionally does not include:
- ...

## Relevant Components
Likely files/modules/tests. Treat this as guidance; inspect the repository to verify.

- `path/to/module`
- `path/to/test`

## Implementation Guidance
Suggested approach, algorithms, sequencing, or pitfalls. Do not prescribe line-by-line edits unless required.

## Verification
Run or add checks covering at least:
- nominal behavior;
- boundary cases;
- backpressure/error/failure cases where relevant;
- regression of existing behavior.

Suggested commands:
```bash
# TBD
```

## Acceptance Criteria
- [ ] Target behavior is implemented.
- [ ] Existing relevant tests pass.
- [ ] New/updated tests cover the behavioral change.
- [ ] Relevant build/lint/simulation checks pass.
- [ ] No unrelated refactor is introduced.
- [ ] Relevant documentation is updated.
- [ ] `docs/PROJECT_STATUS.md` is updated if project status changed.

## Documentation Updates
Expected documentation changes:
- `docs/design/...`
- `docs/decisions/...` if a new architectural decision is made
- `docs/PROJECT_STATUS.md`

## Completion Report
At completion, report:
1. Changes made
2. Files changed
3. Tests/checks run and results
4. Deviations from this task and why
5. Known limitations
6. Recommended next step
