# Initial OpenAI Reference Baseline

## Sources

- OAI-001 — Harness engineering
- OAI-002 — Unrolling the Codex agent loop
- OAI-003 — Unlocking the Codex harness
- OAI-004 — Codex product page
- OAI-005 — Codex release notes

## Template-Relevant Insights

### Repository knowledge should be durable

Important engineering knowledge should live in the repository rather than conversation history.

### `AGENTS.md` should be a map

Keep core agent guidance concise and point to deeper structured documentation.

### Agent legibility matters

Architecture, commands, tests, and expected behavior should be easy for an agent to discover and verify.

### Feedback loops should be executable

Build, test, verification, review, and maintenance workflows should increasingly become repository-visible automation.

### Avoid duplicating native Codex capabilities

As Codex gains skills, multi-agent workflows, automation, and other native features, evaluate whether repository conventions can become simpler.

## Existing Coverage

Current template already addresses:

- structured `docs/`,
- `AGENTS.md`,
- project initialization,
- standard engineering commands,
- verification hierarchy,
- reproducibility,
- template validation.

## Candidate Future Improvements

- explicit freshness checks for repository knowledge,
- mechanically enforceable architecture invariants,
- lightweight recurring maintenance / entropy checks,
- clearer guidance for Codex-native skills versus repository scripts.

## Decision

Monitor and use this baseline as evidence for future template changes. No automatic template payload change is required solely from creating this reference system.
