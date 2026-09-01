# codex-template-source

`codex-template-source` is the source, governance, validation, and release workspace for [`codex-template`](https://github.com/xiongdl/codex-template), an independent Git repository containing the distributable, project-agnostic template.

The `template/` path is a Git submodule checkout of `codex-template`. The source workspace's gitlink records the exact distributable-repository revision used for validation and release preparation; `.gitmodules` records its path and remote URL. It is not an ordinary distributable directory tracked inside this repository.

## Repository Structure

```text
codex-template-source/
├── template/                  # Git submodule: independent codex-template repository
├── .gitmodules                # submodule path and remote URL
├── .ai/                       # source-workspace engineering governance
├── docs/                      # architecture, design, change, and version policy
├── references/                # curated upstream evidence
├── scripts/                   # source-workspace maintenance and validation tools
├── tests/                     # source-workspace and checked-out template validation
├── CHANGELOG.md
├── VERSION
└── README.md
```

The two repositories retain independent Git histories and repository-local lifecycles. A multi-repository Engineering Task composes those lifecycles according to its dependencies. A managed checkout may temporarily diverge from the source workspace's recorded gitlink during authorized development; the gitlink remains the accepted validation and release baseline until the source workspace records another commit.

## Maintainer Flow

```text
Need / real-project feedback
        ↓
Design decision and source-workspace task
        ↓
Modify the applicable independent repository or repositories
        ↓
Validate the dependency-consistent repository set
        ↓
Independent Review and explicit integration decision
        ↓
Prepare and publish an authorized codex-template release
        ↓
Observe downstream use and feed improvements back
```

Run the shared validation entry point from the source workspace:

```bash
./scripts/check
```

The root project dogfoods the workflow defined in `.ai/WORKFLOW.md`, `.ai/AI_HANDOFF_PROTOCOL.md`, and `.ai/GIT_WORKFLOW.md`. The four cross-role artifact templates live under root `.ai/`; project-agnostic counterparts live in the independent repository checked out at `template/.ai/`.

## Evidence and Release Governance

Official upstream material is curated under `references/`. Human-maintained snapshots are primary evidence; ChatGPT performs commit-pinned analysis and proposes decisions; Codex applies approved repository changes and verifies them. A new reference never directly authorizes a distributable-template modification.

`docs/VERSIONING.md` defines source-workspace release-impact policy. Local task completion does not authorize remote pushes, tags, or releases.

Downstream project instantiation and later upstream synchronization are consumer concerns documented by `codex-template`. They are conceptually separate from this source workspace's internal submodule-based maintenance architecture, and downstream projects do not inherit the `codex-template-source` → `codex-template` submodule relationship.

## Project Entry Points

```text
README.md   → Human entry point
CHATGPT.md  → ChatGPT bootstrap entry point
AGENTS.md   → Codex entry point
```
