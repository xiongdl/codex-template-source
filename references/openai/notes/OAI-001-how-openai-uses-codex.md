# OAI-001 — How OpenAI uses Codex

## Status

Reviewed against `xiongdl/codex-template` commit `35ac63bfbadcfc7707559858f6953e42ef029d1c`.

## Evidence

### Primary Evidence

- ID: `OAI-001`
- Title: *How OpenAI uses Codex*
- Source: OpenAI
- Snapshot: `references/openai/snapshots/OAI-001-how-openai-uses-codex/2026-08-26.pdf`
- Metadata: `references/openai/snapshots/OAI-001-how-openai-uses-codex/metadata.yaml`

This note treats the stored snapshot as the authoritative source for OpenAI practices.

### Template Baseline

- Repository: `xiongdl/codex-template`
- Commit: `35ac63bfbadcfc7707559858f6953e42ef029d1c`
- Version: `1.5.0`
- Review date: 2026-08-26

At this commit, the repository has the intended two-layer architecture:

```text
codex-template/
├── template/       # distributable project template
├── docs/           # template governance/design
├── references/     # upstream evidence
├── scripts/        # repository-maintenance automation
├── tests/          # validation of the template/reference system
├── CHANGELOG.md
├── VERSION
└── README.md
```

The Gap Analysis below evaluates **the distributable `template/`**, while using the governance layer only where the question concerns evolution of `codex-template` itself.

## Executive Summary

OAI-001 largely **validates the current `codex-template` design rather than exposing major missing architecture**.

The most important OAI-001 practices are already represented in commit `35ac63b`:

- understand the repository before editing,
- plan before implementation,
- keep tasks scoped,
- provide implementation-ready task context,
- maintain persistent context in `AGENTS.md`,
- make environment/setup/build/test information discoverable,
- automate repeatable engineering workflows,
- make testing and verification part of completion.

The previous assessment that development-environment/reproducibility support was a major gap was incorrect for this commit. `template/.ai/PROJECT_INIT.md`, `template/docs/REPRODUCIBILITY.md`, `template/scripts/project`, and the shared Human/Codex/CI command convention already address that concern directly.

The remaining gaps are small and mostly intentional:

1. OAI-001's Codex task queue/backlog practice is not represented.
2. Best-of-N is not represented.
3. The template does not encode OAI-001's contemporary task-size heuristic.

None of these should currently become mandatory core-template mechanisms.

**Overall decision: No immediate template change required from OAI-001.**

## Relevant OAI-001 Practices

### P1 — Plan before large changes

For larger changes, use an initial planning step before implementation and carry the resulting plan into subsequent work.

### P2 — Keep tasks scoped

Codex performs better on coherent, bounded tasks. OAI-001 provides contemporary size heuristics, while acknowledging that appropriate task size changes as models improve.

### P3 — Continuously improve the development environment

Teams should make it increasingly easy for Codex to build, run, and verify the project. Failures caused by environment configuration should feed back into better project setup.

### P4 — Write prompts like implementation-ready GitHub issues

Provide relevant paths, components, current behavior, diffs or documentation context, constraints, and examples/patterns where useful.

### P5 — Use the task queue as a lightweight backlog

Tangential work can be captured as follow-up tasks instead of interrupting the current task.

### P6 — Use `AGENTS.md` for persistent context

Store important repository context that Codex cannot reliably infer from source code alone.

### P7 — Consider Best-of-N for difficult tasks

For sufficiently complicated work, generating multiple candidate solutions can help explore alternatives.

### P8 — Understand the repository before modifying it

Codex can be used to locate core logic, understand module relationships, trace data flow, and identify relevant implementation areas before making changes.

### P9 — Treat testing as part of implementation

Testing should cover expected behavior as well as relevant edge cases and failure paths, especially around fixes and refactoring.

### P10 — Use Codex for exploration and design challenge

Codex can compare alternatives, surface trade-offs, challenge assumptions, and identify related implications elsewhere in the repository.

## Gap Analysis

| OAI-001 Practice | `35ac63b` Template Mechanism | Coverage | Assessment |
|---|---|---|---|
| P1 Plan before large changes | `AGENTS.md`; `.ai/WORKFLOW.md` | **Strong** | Core workflow explicitly contains Understand → Design → Decide → Plan → Implement |
| P2 Keep tasks scoped | `AGENTS.md`; task templates | **Strong / principle-level** | Scoped changes and explicit Scope/Non-Goals are present; no brittle LOC/time rule |
| P3 Improve development environment | `.ai/PROJECT_INIT.md`; `docs/REPRODUCIBILITY.md`; `scripts/project` | **Strong** | Environment, dependencies, setup, build, test, verify and reproducibility are first-class |
| P4 Prompt like GitHub Issue | `.ai/CODEX_TASK_TEMPLATE.md`; `.ai/COMPONENT_TASK_TEMPLATE.md` | **Strong** | Task handoff contains context, behavior, goal, decisions, constraints, scope, files, verification and acceptance criteria |
| P5 Task queue / lightweight backlog | None | **Not covered — intentional** | Codex product workflow, not a stable project architecture requirement |
| P6 Persistent `AGENTS.md` context | `template/AGENTS.md` plus structured `docs/` | **Strong** | Persistent context and navigation are explicit |
| P7 Best-of-N | None | **Not covered — intentional** | Execution strategy/model capability; unsuitable as mandatory repository structure |
| P8 Understand repo before editing | `AGENTS.md`; `.ai/PROJECT_INIT.md`; `.ai/WORKFLOW.md` | **Strong** | Inspection and invariant discovery precede implementation |
| P9 Testing as implementation work | `AGENTS.md`; verification hierarchy; task templates | **Strong** | Component, integration, and project/E2E verification levels are explicit |
| P10 Exploration/design challenge | `.ai/WORKFLOW.md`; task design fields | **Covered** | Research/design/decision stages exist before implementation |

## Detailed Mapping

### 1. Planning — Strongly Covered

`template/AGENTS.md` defines:

```text
Understand
→ Design
→ Decide
→ Plan
→ Implement
→ Verify
→ Document
→ Record
→ Review
```

`.ai/WORKFLOW.md` independently reinforces the same sequence by separating ChatGPT research/design, design decision, Codex task, Codex inspection/planning, implementation, and verification.

This is stronger than merely telling Codex to “make a plan”: planning is embedded in the engineering lifecycle.

**Gap:** None.

**Action:** Preserve.

### 2. Scoped Tasks — Strongly Covered at the Correct Abstraction Level

The template prefers scoped, understandable changes, while `CODEX_TASK_TEMPLATE.md` explicitly separates:

- Goal
- Scope
- Non-Goals
- Constraints
- Affected components
- Relevant files
- Verification
- Acceptance criteria

This captures the durable principle behind OAI-001 without freezing a model-era-specific number of lines or hours.

**Gap:** None requiring action.

**Action:** Do not add a fixed LOC/time task limit.

### 3. Development Environment — Strongly Covered

This is the largest correction relative to the earlier, stale-repository analysis.

`PROJECT_INIT.md` requires inspection of:

- build systems,
- configuration,
- environment requirements,
- dependencies,
- scripts/tools,
- CI.

It then explicitly discovers existing setup/build/test/verification workflows and establishes project automation entry points.

`REPRODUCIBILITY.md` provides dedicated sections for:

- Supported Environment
- Dependencies
- Setup
- Build
- Test
- Verify
- Configuration
- Artifacts
- Reproducing Important Results
- Known Reproducibility Gaps

The project-level automation contract is:

```bash
./scripts/project setup
./scripts/project build
./scripts/project test
./scripts/project verify
./scripts/project clean
./scripts/project status
```

The stub intentionally leaves project-specific behavior to initialization rather than embedding a language/framework assumption.

**Gap:** No structural gap.

**Possible future refinement:** Real instantiated projects should feed recurring Codex environment failures back into these setup/reproducibility mechanisms. This is an operational behavior to observe in real projects, not a reason to add more template structure now.

### 4. GitHub-Issue-Style Task Context — Strongly Covered

`CODEX_TASK_TEMPLATE.md` contains the important context fields OAI-001 motivates:

```text
Task
Context
Owning Component / Area
Affected Components / Areas
Current Behavior
Goal
Design Decisions
Constraints
Scope
Non-Goals
Relevant Files / Components
Cross-Component Impact
Reproducibility Impact
Implementation Guidance
Verification
Acceptance Criteria
Documentation Updates
```

This is already an implementation-ready handoff format rather than a conversational prompt.

**Gap:** None.

**Action:** Preserve; evolve only from real-project feedback.

### 5. Task Queue — Intentionally Not Covered

OAI-001's lightweight backlog/task-queue practice can be useful during Codex work, but it is tied to Codex product workflow.

Adding a second repository backlog abstraction would:

- duplicate issue/task-management systems,
- increase template surface area,
- couple the template to a particular Codex product behavior,
- weaken the Minimal Core principle.

**Decision:** Do not add to core template.

**Status:** Monitor.

### 6. `AGENTS.md` Persistent Context — Strongly Covered

`template/AGENTS.md` tells a new Codex session where to find:

- architecture,
- project status,
- reproducibility information,
- component-local guidance,
- design decisions,
- integration documentation,
- implementation/tests/automation/configuration.

It also states that important project knowledge must not exist only in conversation history.

This directly implements the persistent-context principle while avoiding the mistake of putting all project knowledge into one file.

**Gap:** None.

**Action:** Preserve the “map to structured docs” role.

### 7. Best-of-N — Intentionally Not Covered

Best-of-N is a useful task execution strategy, but it is not a durable property of an engineering repository.

It may depend on:

- current Codex capabilities,
- model cost,
- task complexity,
- UI/product workflow.

**Decision:** Do not add to `AGENTS.md` or core project structure.

It may be mentioned in external usage guidance if future evidence repeatedly supports it.

### 8. Repository Understanding — Strongly Covered

Before modification, `AGENTS.md` requires reading project architecture/status/reproducibility information, identifying affected components, reading relevant local guidance and design/decision/integration documents, inspecting implementation/tests/automation/configuration, and identifying invariants.

`PROJECT_INIT.md` provides an even broader initial repository-discovery process.

**Gap:** None.

### 9. Testing and Verification — Strongly Covered

The template formalizes three verification scopes:

```text
components/<component>/tests/
    → Component-local tests

integration/tests/
    → Cross-component tests

tests/
    → Project-level / End-to-End tests
```

It also establishes the principle that a test belongs at the narrowest level that fully validates the intended behavior.

Task definitions include explicit verification and acceptance criteria, and `AGENTS.md` prohibits claiming verification that was not actually performed.

**Gap:** None.

### 10. Exploration and Design Challenge — Covered

`.ai/WORKFLOW.md` assigns research, architecture, alternatives, trade-off analysis, task definition, and review to ChatGPT, while Codex handles repository inspection, implementation planning, coding, testing, debugging, refactoring, automation, and documentation.

The overall workflow deliberately creates a design/decision stage before implementation.

**Gap:** No structural gap identified from OAI-001.

## What OAI-001 Validates in the Template

OAI-001 provides strong external support for several existing design principles:

### Repository as long-term memory

The repository should contain enough durable knowledge for a fresh Codex session to recover project context.

### Inspect before assume

Repository understanding precedes modification.

### Shared engineering interface

Build/test/verify should be executable through discoverable repository mechanisms rather than existing only as prose or human habit.

### Reproducibility by default

Environment and setup knowledge are part of AI operability.

### Testability by design

Verification is part of implementation, not an optional final step.

### Scoped task handoff

A Codex task should resemble an implementation-ready engineering issue.

## Remaining Gaps

After reviewing commit `35ac63b`, there is **no major OAI-001-derived gap requiring a template architecture change**.

The remaining differences are deliberate exclusions:

```text
Task Queue
    → product-specific workflow
    → Monitor

Best-of-N
    → model/product execution strategy
    → Do not put in Core

Specific task size numbers
    → time-sensitive heuristic
    → Keep only qualitative scoped-task principle
```

A smaller operational question remains:

> Do real instantiated projects consistently convert recurring Codex environment/setup failures into improvements to `scripts/project`, reproducibility documentation, and project setup?

OAI-001 supports that feedback loop, but evidence from actual instantiated projects is needed before adding more template machinery.

## Recommendations

1. **Do not change `template/` solely because of OAI-001.**
2. Keep the current planning, task-template, `AGENTS.md`, reproducibility, automation, and verification architecture.
3. Treat task queue and Best-of-N as optional Codex usage practices rather than template requirements.
4. Do not encode fixed task duration or LOC limits.
5. Use real-project feedback to determine whether the environment-improvement feedback loop needs stronger automation later.
6. Use OAI-001 as external evidence supporting the existing Design Principles rather than as a source of new mandatory files.

## Decision

**Decision: No immediate template change.**

Classification:

| Area | Decision |
|---|---|
| Plan before implementation | Keep |
| Scoped tasks | Keep |
| Development environment | Already covered |
| Reproducibility | Already covered |
| GitHub-Issue-style task handoff | Already covered |
| `AGENTS.md` persistent context | Keep |
| Repository-first inspection | Keep |
| Testing / verification | Keep |
| Task queue | Monitor; no core change |
| Best-of-N | No core change |
| Fixed task-size heuristic | Do not adopt |

## ADR Requirement

**No ADR required.**

OAI-001 does not currently justify a new architectural decision. It primarily validates decisions already represented in the template.

If future evidence leads to a new persistent mechanism—for example, an automated environment-health or engineering-entropy feedback loop—evaluate that separately and create an ADR if it materially changes the template architecture.

## Follow-Up

The next reference review should follow the same process:

```text
Primary Snapshot
      ↓
Extract durable practices
      ↓
Pin repository baseline commit
      ↓
Map practice → actual template artifact
      ↓
Classify coverage
      ↓
Identify genuine gaps
      ↓
No Change / Monitor / Change Proposal
      ↓
ADR only when architecturally material
```

For future notes, always record the exact repository commit used for Gap Analysis so results remain reproducible.

## Review History

### 2026-08-26

Initial formal review corrected and regenerated against:

```text
xiongdl/codex-template
35ac63bfbadcfc7707559858f6953e42ef029d1c
VERSION 1.5.0
```

Main correction from the earlier draft:

- the current template **does** contain the two-layer repository architecture;
- environment/reproducibility support is **already strongly covered** by `PROJECT_INIT.md`, `REPRODUCIBILITY.md`, and `scripts/project`;
- the task template already provides a strong implementation-ready handoff;
- therefore OAI-001 currently validates the template more than it motivates new template changes.
