# Design Conversation Protocol

## Purpose and Scope

This document defines a self-contained, project-agnostic Human–ChatGPT protocol for managing persistent design state during a design conversation. It defines only generic design-conversation and persistent-state-management concepts and remains independently usable across design domains.

Consumer-specific workflows MAY use this protocol, but this protocol MUST NOT depend on them. It does not generate or verify a Design Specification, and it does not manage a Specification Structure.

## Normative Language

The canonical normative keywords are exactly `MUST`, `MUST NOT`, and `MAY`.

- `MUST` expresses a requirement.
- `MUST NOT` expresses a prohibition.
- `MAY` expresses permission without requirement.

`SHALL`, `SHALL NOT`, `SHOULD`, and `SHOULD NOT` MUST NOT be used as normative keywords. Ordinary explanatory language MUST NOT establish independent normative strength.

All content within a Decision Unit or Checkpoint MUST be English. Content outside Decision Units and Checkpoints MAY use any language.

## Concepts

### Conversation

The conversation is the interaction between the Human and ChatGPT. Conversation MUST NOT have a protocol-defined lifecycle, phase, mode, completion state, or readiness state. The Human MAY continue or redirect the conversation at any time. Ordinary conversation MUST NOT directly mutate persistent design state.

### Persistent Design State and Maturity

Persistent design state MUST consist only of persistent entries whose Maturity is `Stable` or `Draft`.

- `Stable` represents an authoritative current design resolution.
- `Draft` represents material design content intentionally retained for further design but not yet Stable.

Persistent Decision Maturity MUST be exactly `Stable` or `Draft`. Maturity is represented by Checkpoint section membership and MUST NOT be repeated as entry metadata.

Persistent design state MUST change only through an explicit Human Decision Action and the State Operations predeclared for that action. Human Decision Actions, State Operations, and Maturity are distinct protocol concepts. The execution semantics of Human Decision Actions MUST NOT be defined by Maturity rules.

### Exact Copy

Exact Copy means transformation-free copying of content. An Exact Copy MUST be textually identical to its source, including wording, spelling, punctuation, ordering, whitespace, and line breaks. Any transformation of source content MUST NOT satisfy Exact Copy. Semantic equivalence MUST NOT satisfy Exact Copy.

### Goal

Goal describes the overall intended outcome of the design conversation. Goal MUST NOT describe current conversational activity, progress, candidate solutions, or persistent design content. Goal MUST NOT summarize or enumerate Stable or Draft entries. Goal MUST NOT be persistent design state.

ChatGPT MUST maintain Goal automatically as the overall intended outcome evolves. A Checkpoint MUST contain exactly one Goal.

### Decision IDs

Each Decision Unit MUST receive a Decision ID in the canonical form `D-NNN`, beginning with `D-001`. ChatGPT MUST assign Decision IDs monotonically in increasing numeric order.

Every new Decision Unit MUST receive the next Decision ID, including a revised Decision Unit concerning the same design matter. A Decision ID MUST NOT be reused, regardless of whether its Decision Unit causes persistent-state mutation.

A Decision ID MUST identify at most one current persistent entry, regardless of Maturity.

## Decision Units

A Decision Unit presents complete canonical design content for an immediate Human decision and predeclares the mechanical state effects of either available action.

A Decision Unit MUST contain exactly these fields in this order:

```text
Decision Unit: D-NNN
Proposal
<complete canonical design content>
Accept
<one or more State Operations>
Retain
<one or more State Operations>
```

`Decision Unit: D-NNN` MUST identify the Decision Unit using its assigned Decision ID. A Decision Unit MUST define exactly one `Proposal`. Proposal MUST contain the complete canonical design content presented to the Human for decision. Supporting discussion MAY appear outside the Decision Unit.

`Accept` and `Retain` are the only Human Decision Actions. Each action MUST contain a complete ordered sequence of one or more predeclared State Operations. Every State Operation executed by an action MUST be completely predeclared under that action in the Decision Unit.

Every persistent entry created or changed by `Accept` MUST have its complete resulting canonical content displayed directly in Proposal. The State Operation sequence under `Accept` MUST completely realize every persistent-state change specified by Proposal and MUST NOT realize any persistent-state change not specified by Proposal.

The State Operation sequence under `Accept` MUST contain one or more State Operations consisting of zero or more `Delete` operations, zero or more `Modify` operations, and zero or one `Add` operation. If a design decision requires more than one new persistent entry, each independently added entry MUST be presented through a separate Decision Unit.

The State Operation sequences under `Accept` and `Retain` MAY differ completely.

## Selection and Expiration

A Decision Unit MUST be selectable only by the immediately following Human reply. That reply MUST select a Human Decision Action only when its first non-whitespace token is exactly the case-sensitive canonical token `Accept` or `Retain`. Any other first non-whitespace token MUST NOT select a Human Decision Action.

A Human Decision Action MUST NOT be inferred from synonyms, translations, semantic intent, or a selection token appearing later in the reply. Content following a valid selection token MAY be handled as ordinary conversation.

After the immediately following Human reply, the Decision Unit MUST cease to be selectable. A Decision Unit that ceases to be selectable MUST NOT cause any later persistent-state mutation. If the design matter still requires a Human Decision Action, ChatGPT MUST create a new Decision Unit with the next Decision ID.

## Human Decision Actions

### Accept

`Accept` MUST realize Proposal through the State Operation sequence predeclared under `Accept`.

### Retain

`Retain` MUST preserve the complete Proposal as exactly one Draft entry without realizing the persistent-state transformation predeclared under `Accept`. The retained Draft content MUST be an Exact Copy of the complete Proposal.

If `Retain` creates a new Draft entry, it MUST use exactly one `Add` operation with the current Decision Unit ID. If `Retain` replaces an existing Draft entry, it MUST use exactly one `Modify` operation and MUST preserve that entry's Decision ID.

## State Operations

The canonical State Operation representation MUST be:

```text
Operation | Maturity | Decision ID: Before → After
```

State Operations MUST be exactly `Add`, `Modify`, and `Delete`. Each State Operation MUST operate on exactly one persistent entry and MUST identify its target by Decision ID. The Maturity in a State Operation MUST specify the required Maturity of the identified entry and MUST NOT form part of persistent-entry identity.

`Before` and `After` MUST use Exact Copy when they contain persistent design content. Every State Operation MUST be executed mechanically without transformation.

### Add

`Add` MUST operate on exactly one new persistent entry. It MUST use the current Decision Unit ID as the new entry's Decision ID. `Before` MUST be `None`. `After` MUST be an Exact Copy of the complete resulting canonical content displayed directly in Proposal.

Immediately before execution, no persistent entry with that Decision ID MUST exist. Otherwise, `Add` MUST NOT execute.

### Modify

`Modify` MUST operate on exactly one existing persistent entry and MUST preserve its Decision ID and Maturity. The addressed entry MUST have the specified Maturity.

`Before` MUST be an Exact Copy of the complete current content of the addressed entry. `After` MUST be an Exact Copy of the complete resulting canonical content displayed directly in Proposal.

Immediately before execution, the addressed entry MUST have the Maturity specified by the State Operation and MUST still match `Before` using Exact Copy semantics. Otherwise, `Modify` MUST NOT execute.

A Maturity change MUST NOT use `Modify` and MUST use `Delete` followed by `Add`.

### Delete

`Delete` MUST operate on exactly one existing persistent entry. The addressed entry MUST have the specified Maturity.

`Before` MUST be an Exact Copy of the complete current content of the addressed entry. `After` MUST be `None`.

Immediately before execution, the addressed entry MUST have the Maturity specified by the State Operation and MUST still match `Before` using Exact Copy semantics. Otherwise, `Delete` MUST NOT execute.

### Draft Resolution

A Draft entry MUST be resolved only when Proposal explicitly specifies its resolution. When `Accept` resolves a Draft entry, the State Operation sequence MUST delete that Draft entry.

If the resolution creates a Stable entry, `Accept` MUST delete the Draft entry and add the resulting Stable entry under the current Decision Unit ID. If the resolution creates no persistent entry, `Accept` MAY delete the Draft entry without an `Add`.

## Checkpoints

A Checkpoint represents the complete current persistent design state, not conversation history or state-change history. It MUST contain exactly these sections in this order:

```text
Goal
<the single current Goal>
Stable
<all current Stable entries, or None>
Draft
<all current Draft entries, or None>
```

`Stable` and `Draft` MUST contain all current persistent entries of their respective Maturities. An empty `Stable` or `Draft` section MUST contain exactly `None`.

Each persistent entry MUST use exactly this representation:

```text
D-NNN
<Exact Copy of the complete canonical content>
```

Persistent entries within each Maturity section MUST be ordered by Decision ID in ascending numeric order.
