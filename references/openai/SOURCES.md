# OpenAI Reference Sources

Last registry update: 2026-08-26

This registry tracks official OpenAI sources that may affect the design of `codex-template`.

| ID | Source | Category | Relevance | Last Reviewed | Status |
|---|---|---|---|---|---|
| OAI-001 | Harness engineering: leveraging Codex in an agent-first world | Engineering Practice | High | 2026-08-26 | Active |
| OAI-002 | Unrolling the Codex agent loop | Codex Architecture | High | 2026-08-26 | Active |
| OAI-003 | Unlocking the Codex harness: how we built the App Server | Codex Architecture | Medium | 2026-08-26 | Active |
| OAI-004 | Codex product page | Product Capability | Medium | 2026-08-26 | Active |
| OAI-005 | Codex release notes | Product Evolution | High | 2026-08-26 | Active |

## OAI-001 — Harness engineering

Official URL:
https://openai.com/index/harness-engineering/

Track for:

- repository knowledge as system of record,
- `AGENTS.md` design,
- agent legibility,
- architecture enforcement,
- feedback loops,
- repository automation,
- technical-debt / entropy management.

Current template relevance:

- supports keeping `AGENTS.md` concise and navigational,
- supports structured repository documentation,
- supports mechanically enforceable architecture and verification,
- supports continuous repository maintenance rather than periodic large cleanup.

## OAI-002 — Unrolling the Codex agent loop

Official URL:
https://openai.com/index/unrolling-the-codex-agent-loop/

Track for:

- Codex instruction/context behavior,
- tools and execution model,
- agent-loop behavior,
- configuration mechanisms,
- future changes that affect repository guidance.

Current template relevance:

- informs how repository-contained instructions should be structured,
- helps avoid assumptions about Codex behavior that may become stale.

## OAI-003 — Unlocking the Codex harness

Official URL:
https://openai.com/index/unlocking-the-codex-harness/

Track for:

- Codex harness architecture,
- thread lifecycle,
- configuration,
- tool execution,
- skills and extensions.

Current template relevance:

- useful when deciding whether a workflow belongs in the repository, Codex configuration, skills, or external tooling.

## OAI-004 — Codex product page

Official URL:
https://openai.com/codex/

Track for:

- product-level capabilities,
- multi-agent workflows,
- skills,
- cloud/local workflow evolution.

Current template relevance:

- helps prevent duplicating capabilities that Codex provides natively.

## OAI-005 — Codex release notes

Official URL:
https://help.openai.com/en/articles/6825453-codex-release-notes

Track for:

- new Codex capabilities,
- changed behavior,
- deprecated workflow assumptions,
- new automation / collaboration features.

Current template relevance:

- primary change-detection source for product evolution.

## Review Rule

A detected upstream change should produce one of:

```text
No template impact
        │
        └── update review metadata / note

Potential template impact
        │
        └── create/update analysis note

Material template impact
        │
        └── ADR / design update
                ↓
           modify template/
                ↓
             validate
                ↓
       CHANGELOG + VERSION
```
