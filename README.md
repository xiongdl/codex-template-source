# codex-template

`codex-template` has two responsibilities:

1. `template/` — the actual project template users copy or instantiate.
2. Repository governance — the design, validation, versioning, and evolution of the template itself.

## Repository Structure

```text
codex-template/
├── template/                  # distributable project template
│   ├── AGENTS.md
│   ├── README.md
│   ├── .ai/
│   ├── docs/
│   ├── third_party/
│   └── scripts/
├── docs/                      # codex-template design/governance
│   ├── DESIGN_PRINCIPLES.md
│   ├── TEMPLATE_ARCHITECTURE.md
│   ├── CHANGE_POLICY.md
│   └── decisions/
├── references/                # upstream evidence for template evolution
│   └── openai/
├── scripts/                   # maintenance/update tooling for codex-template
├── tests/                     # tests for the template itself
│   ├── validate_template.py
│   └── validate_ai_workflow.py
├── CHANGELOG.md
├── VERSION
└── README.md
```

## Important Separation

`docs/` describes and governs `codex-template` itself.

`template/docs/` is copied into instantiated engineering projects.

## Evolution Flow

```text
Need / Real-project feedback
        ↓
Template design discussion
        ↓
Design principle / ADR
        ↓
Modify template/
        ↓
Validate
        ↓
Version + Changelog
        ↓
Release
        ↓
Instantiate in real projects
        ↓
Feedback
```

## Validate

```bash
./scripts/check
```

## AI Engineering Workflow

The root project dogfoods the complete workflow defined in `.ai/WORKFLOW.md`, `.ai/AI_HANDOFF_PROTOCOL.md`, and `.ai/GIT_WORKFLOW.md`:

```text
ChatGPT / Design Owner
→ Codex A / Implementation Owner
→ Codex B / read-only Review Owner
→ Codex A / ff-only integration
→ ChatGPT / Engineering Result
```

The four cross-role artifact templates live under root `.ai/`. Their project-agnostic counterparts are distributed under `template/.ai/`.

## Upstream Reference Workflow

Official upstream material is tracked under `references/`.

For OpenAI sources:

```bash
python scripts/check_openai_references.py
```

Detected changes are reviewed before any modification to `template/`.

## Snapshot Maintenance

OpenAI upstream evidence is intentionally human-curated.

Only `references/openai/snapshots/` is manually maintained as primary evidence.
Strict naming and metadata validation is enforced by:

```bash
./scripts/check
```


## Reference Governance

```text
Human   → curate primary snapshots and approve material decisions
ChatGPT → analyze evidence, perform commit-pinned Gap Analysis, draft notes
Codex   → apply repository changes, maintain consistency, run validation
```

Formal notes use `references/openai/notes/NOTE_TEMPLATE.md`.
Every review ends in `No Change`, `Monitor`, or `Change Proposed`.
Only an approved `Change Proposed` outcome can proceed toward a template modification.


## v1.7 Project Governance Additions

The distributable template establishes:

- explicit ChatGPT bootstrap via `template/CHATGPT.md`,
- shared AI Task Readiness via `template/.ai/TASK_READINESS.md`,
- instantiated-project versioning via `template/VERSION`, `template/CHANGELOG.md`, and `template/docs/VERSIONING.md`,
- preliminary and final Version Impact workflow.

See `docs/VERSIONING.md` for `codex-template`'s own release policy.

## codex-template Project Entry Points

`codex-template` itself uses the same AI-engineering discipline it promotes:

```text
README.md   → Human entry point
CHATGPT.md  → ChatGPT explicit bootstrap entry point
AGENTS.md   → Codex entry point
```

Shared project-maintenance policy lives under `.ai/`.

The root project maintains/evolves `codex-template`; `template/` bootstraps instantiated engineering projects.
