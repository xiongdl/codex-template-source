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
│   ├── components/
│   ├── integration/
│   ├── third_party/
│   ├── tests/
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
│   └── validate_template.py
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
python tests/validate_template.py
```

## Upstream Reference Workflow

Official upstream material is tracked under `references/`.

For OpenAI sources:

```bash
python scripts/check_openai_references.py
```

Detected changes are reviewed before any modification to `template/`.
