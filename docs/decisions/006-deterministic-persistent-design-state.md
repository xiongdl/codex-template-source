# ADR-006: Deterministic Persistent Design State

## Status

Accepted

## Context

ADR-005 introduced explicit design state, decision authorization, and Checkpoints, but coupled them to a phase-based conversation lifecycle, localized action tokens, per-interval change history, and state semantics that were more complex than necessary. The protocol now needs a smaller project-agnostic contract in which Human-confirmed design decisions are the only persistent state and every mutation is mechanically determined.

## Decision

- Replace the protocol-defined design lifecycle with unrestricted ordinary conversation and no conversation phase, mode, completion, or readiness state.
- Limit persistent design state to `Stable` and `Draft` entries while keeping Goal automatic and non-persistent.
- Use immediately selectable Decision Units with exactly `Accept` and `Retain`, monotonically assigned Decision IDs, and complete predeclared State Operations.
- Limit State Operations to `Add`, `Modify`, and `Delete`, with exact-copy preconditions and mechanical execution.
- Make each Checkpoint a complete `Goal / Stable / Draft` current-state view without conversation or mutation history.
- Keep the payload protocol canonical and the maintainer protocol as a layer-specific entry point.

This decision supersedes ADR-005's lifecycle, state vocabulary, choice, operation, identity, and Checkpoint-shape decisions. ADR-005 remains as historical rationale for the prior `2.0.0` contract.

## Consequences

Design-state mutation becomes deterministic from a Decision Unit and the immediately following Human reply. The protocol loses phase, Freeze, compilation, blocker-set, rejection, no-op, and Checkpoint history semantics. Consumer workflows may independently use the protocol but cannot become dependencies of it. The change is project-agnostic and document-only, but it is a breaking instantiated-project workflow-contract change.
