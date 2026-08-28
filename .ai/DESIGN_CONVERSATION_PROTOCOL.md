# Maintainer Design Conversation Protocol

For maintenance of `codex-template`, apply the complete project-agnostic Design Conversation Protocol in:

```text
template/.ai/DESIGN_CONVERSATION_PROTOCOL.md
```

That distributable artifact is the canonical shared behavior for `EXPLORE → CONVERGE → PRE-FREEZE → FREEZE → COMPILE`, State Anchors, decision routing, and minimum-sufficient Task Contract derivation. This maintainer entry point avoids duplicating the complete protocol across the governance and payload layers.

Apply the canonical protocol with these maintainer-specific boundaries:

- investigate root governance, `template/` payload, relevant ADRs, and authoritative evidence according to `.ai/TASK_READINESS.md`;
- distinguish changes to `codex-template` governance from behavior distributed to instantiated projects;
- preserve the project-agnostic principle and reference-governed change requirements;
- derive maintainer Task Contracts with root `.ai/CODEX_TASK_TEMPLATE.md`;
- classify Preliminary Version Impact against `docs/VERSIONING.md` and repository-level `VERSION` and `CHANGELOG.md`.

The payload protocol remains normative for design-conversation semantics. These maintainer rules constrain evidence and contract placement; they do not add phases or alter Freeze, Reopen, Authoritative Task Core, or Independent Review semantics.
