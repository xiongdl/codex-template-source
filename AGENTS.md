# AGENTS.md

## Purpose
This repository follows an AI-assisted engineering workflow. The repository is the long-term source of truth; chat sessions are working memory.

## Core workflow
For non-trivial work follow:

**Understand → Research/Design → Decide → Plan → Implement → Test → Document → Record → Review**

## Before modifying code
1. Read `docs/ARCHITECTURE.md` and `docs/PROJECT_STATUS.md`.
2. Read relevant files under `docs/design/`, `docs/decisions/`, and `.ai/`.
3. Inspect the current implementation and tests before proposing changes.
4. Identify architectural invariants and existing interfaces.
5. Do not infer architectural intent from code alone.
6. For non-trivial changes, state an implementation plan before editing.

## During implementation
- Keep changes scoped to the requested task.
- Prefer extending the existing architecture over silently redesigning it.
- Preserve backward compatibility unless the task explicitly changes it.
- Add or update tests for behavioral changes.
- Run the relevant lint/build/test commands.
- Fix failures introduced by the change; do not hide or disable tests to get green results.
- Do not make major architectural decisions when requirements are ambiguous; surface the decision and alternatives.

## After implementation
Update, when applicable:
- `docs/ARCHITECTURE.md`
- relevant `docs/design/*`
- relevant `docs/decisions/*`
- `docs/PROJECT_STATUS.md`

Report:
1. What changed
2. Why it changed
3. Tests/checks run and results
4. Known limitations or unresolved issues
5. Suggested next step

## Documentation rules
- Current truth belongs in architecture/design/status docs.
- Important decisions and rationale belong in `docs/decisions/`.
- Temporary implementation plans belong in the task or `.ai/` workflow artifacts, not in `AGENTS.md`.
- Keep this file concise. Put detailed project knowledge in `docs/`.

## Project-specific section
Fill this section during project initialization.

### Project
- Name: TBD
- Purpose: TBD

### Build
- TBD

### Test
- TBD

### Project-specific constraints
- TBD
