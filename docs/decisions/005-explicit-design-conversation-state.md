# ADR-005: Explicit Design Conversation State and Decision Authorization

## Status

Accepted

## Context

The Design Conversation Protocol needs to minimize user interaction while making the current design state and every user-authorized state transition inspectable. Conversation history, implicit interpretation of ordinary replies, and partial Checkpoints do not provide a stable audit boundary and can silently blur confirmed, unresolved, and immediately blocking matters.

## Decision

- Keep the existing `EXPLORE → CONVERGE → PRE-FREEZE → FREEZE → COMPILE` lifecycle as the only design lifecycle.
- Represent the current user-authorized design state explicitly as `已确认` and `未确认`, while keeping `未确认` distinct from the minimum blocker set for the current next action.
- Permit state mutation only through a formal Decision ID unit with exactly `接受 / 待定 / 拒绝` and complete branch operations displayed before the immediately following user choice.
- Address entries by field plus creating Decision ID and express cross-field changes as delete-old plus add-current-ID operations.
- Make Checkpoint a complete current-state and per-interval change-audit surface with exactly `目标 / 已确认 / 未确认 / 状态变更记录`; do not use it for conversation recovery or execution planning.
- Enforce the critical structural vocabulary and invariants with repository validation rather than adding runtime or persistence machinery.

## Consequences

Design conversations gain explicit authorization, deterministic token expiry, complete current-state presentation, and mechanically detectable structural regressions. The protocol becomes a breaking workflow-contract change for instantiated projects, but remains project-agnostic and document-only. ChatGPT still minimizes questions by resolving only the current action's minimum blockers, and the existing Design Owner, Codex A, Codex B, Authoritative Task Core, and Independent Review boundaries remain unchanged.
