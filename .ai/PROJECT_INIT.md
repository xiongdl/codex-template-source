# Project Initialization

Use this once when creating a project from this template.

## Objective
Turn the generic template into a repository-specific engineering environment without implementing new product features.

## Codex initialization prompt

```text
Read AGENTS.md and .ai/WORKFLOW.md first.

Initialize this repository as an AI-assisted engineering project.

1. Inspect the repository structure, existing code, build files, tests, and documentation.
2. Determine the project's purpose, major components, build flow, and test flow from repository evidence.
3. Fill the project-specific section of AGENTS.md.
4. Create or update README.md with practical setup/build/test information.
5. Create or update docs/ARCHITECTURE.md to describe the current architecture only. Do not invent planned components as existing functionality.
6. Create or update docs/PROJECT_STATUS.md with evidence-based current status, known issues, and immediate next work.
7. Add initial design/decision documents only when repository evidence justifies them.
8. Do not implement new features during initialization.
9. Clearly mark unknowns instead of guessing.
10. Finish with a summary of what was learned, files updated, and unresolved questions.
```

## Initialization checklist
- [ ] `AGENTS.md` contains project-specific build/test/constraints.
- [ ] `README.md` describes the actual repository.
- [ ] `docs/ARCHITECTURE.md` reflects current architecture.
- [ ] `docs/PROJECT_STATUS.md` reflects current state.
- [ ] Existing tests/build commands are documented.
- [ ] Unknowns are explicit.
- [ ] No feature implementation was mixed into initialization.
