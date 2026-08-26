# Codex Template

A lightweight repository template for using a human engineer, ChatGPT, and Codex as one repeatable engineering workflow.

## Principle

**Think → Decide → Plan → Implement → Verify → Record → Review**

- **Human:** goals, constraints, final decisions
- **ChatGPT:** research, analysis, architecture, design, task formulation, review
- **Codex:** repository inspection, implementation, testing, debugging, documentation updates
- **Repository:** long-term memory and source of truth

## Start a new project

1. Copy or clone this template into a new repository.
2. Add/import the project's existing code if applicable.
3. Open the repository in Codex.
4. Follow `.ai/PROJECT_INIT.md` once.
5. For each non-trivial feature, discuss design first when needed and formulate work using `.ai/CODEX_TASK_TEMPLATE.md`.
6. Keep `docs/PROJECT_STATUS.md` current.
7. Record durable architecture choices as ADRs.

## Core files

- `AGENTS.md` — default Codex behavior and repository navigation
- `.ai/WORKFLOW.md` — human + ChatGPT + Codex collaboration model
- `.ai/CODEX_TASK_TEMPLATE.md` — standard ChatGPT → Codex handoff
- `.ai/PROJECT_INIT.md` — one-time repository initialization procedure
- `docs/ARCHITECTURE.md` — current architecture
- `docs/PROJECT_STATUS.md` — current project state
- `docs/design/` — detailed designs
- `docs/decisions/` — architecture decision records

## Keep it lightweight
V1 intentionally avoids a large documentation bureaucracy. Add `research/`, `plans/`, `reviews/`, `benchmarks/`, or other structures only after real usage demonstrates the need.
