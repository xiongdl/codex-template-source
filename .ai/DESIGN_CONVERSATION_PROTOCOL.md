# Maintainer Design Conversation Protocol

For maintenance of `codex-template`, apply the complete project-agnostic Design Conversation Protocol in:

```text
template/.ai/DESIGN_CONVERSATION_PROTOCOL.md
```

That distributable artifact is the canonical shared behavior for conversation, Goal, persistent `Stable` / `Draft` design state, Decision Units, Human Decision Actions, State Operations, Exact Copy, Maturity, and Checkpoints. This maintainer entry point avoids duplicating the complete protocol across the governance and payload layers.

Apply the canonical protocol with these maintainer-specific boundaries:

- investigate root governance, `template/` payload, relevant ADRs, and authoritative evidence according to `.ai/TASK_READINESS.md`;
- distinguish changes to `codex-template` governance from behavior distributed to instantiated projects;
- preserve the project-agnostic principle and reference-governed change requirements;
- derive maintainer Task Contracts with root `.ai/CODEX_TASK_TEMPLATE.md` when the separate engineering workflow requires one;
- classify Preliminary Version Impact against `docs/VERSIONING.md` and repository-level `VERSION` and `CHANGELOG.md`.

The payload protocol remains normative for design-conversation semantics. These maintainer rules constrain evidence and contract placement; they do not add a conversation lifecycle, permit persistent-state mutation outside an explicit Human Decision Action, change Decision Unit selection, or alter Authoritative Task Core or Independent Review semantics.
