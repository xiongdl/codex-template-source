# ADR-004: Engineering Environment, Formal Documentation, and Post-ERR Disposition

## Status

Accepted

## Context

Repeatable engineering needs a clear workspace environment boundary and a lightweight formal-document path. The workflow also needs to separate technical Independent Review approval from the human decision to integrate, revise, or abort.

## Decision

- Use Environment Modules as the canonical workspace-owned environment-composition mechanism. Add validated combinations only for actual compatibility or isolation needs; Conda may provide managed dependencies within the composition.
- Keep automation with the responsibility it performs. Codex may report an automation opportunity but may implement it only under explicit Engineering Task scope.
- Use Markdown for repository guidance and AsciiDoc to Asciidoctor PDF for formal documents. Preserve reproducible inputs for figures, using `.drawio` to generated SVG for conceptual diagrams.
- After Independent Review approval, produce the Engineering Result Report before integration. Require a new explicit `INTEGRATE`, `REVISE`, or `ABORT` prompt reflecting the ChatGPT / Design Owner and human decision.

## Consequences

The template gains project-agnostic environment and formal-document conventions without placeholder profiles or a documentation platform. Technical approval no longer implies integration. The additional human decision boundary adds one explicit handoff while preserving exact-commit review and integration invariants.
