#!/usr/bin/env python3
"""Validate mechanically checkable AI workflow invariants."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

LAYERS = {
    "root": ROOT / ".ai",
    "template": ROOT / "template" / ".ai",
}

REQUIRED_FILES = (
    "WORKFLOW.md",
    "DESIGN_CONVERSATION_PROTOCOL.md",
    "TASK_READINESS.md",
    "AI_HANDOFF_PROTOCOL.md",
    "GIT_WORKFLOW.md",
    "CODEX_TASK_TEMPLATE.md",
    "CODEX_REVIEW_PROMPT_TEMPLATE.md",
    "CODEX_REVIEW_REPORT_TEMPLATE.md",
    "ENGINEERING_RESULT_TEMPLATE.md",
)

HANDOFF_TOKENS = (
    "ChatGPT",
    "Design Owner",
    "Codex A",
    "Implementation Owner",
    "Codex B",
    "Review Owner",
    "read-only",
    "READ_ONLY",
    "CHANGE",
    "immutable",
    "COMPLETED",
    "BLOCKED",
    "INPUT_REQUIRED",
    "DECISION_REQUIRED",
    "REVIEW_LIMIT_REACHED",
    "APPROVED",
    "CHANGES_REQUESTED",
    "Maximum Review Attempts = 3",
    "Base Commit..Review Commit",
    "mandatory re-review",
    "new Codex session explicitly created by the human user",
    "human user manually supplies",
    "MUST stop review execution",
    "sub-agent or delegated reviewers",
    "do not consume Review Attempt count",
    "cannot produce a qualifying `APPROVED`",
    "same Review Commit",
    "artificial or empty commit",
    "Engineering Task decomposition",
    "ChatGPT / Design Owner",
    "Task Granularity",
    "one coherent engineering objective",
    "Understand → Inspect → Challenge → Verify",
    "mechanically repeat Codex A's complete verification suite",
    "concrete material problem",
    "Re-review is incremental-first",
    "more than noticing no obvious bug",
    "Engineering Result Report before integration",
    "Automation Opportunity",
    "INTEGRATE",
    "REVISE",
    "ABORT",
    "MUST NOT infer a disposition",
)

GIT_TOKENS = (
    "Default Base Branch",
    "Base Branch",
    "Base Commit",
    "task/*",
    "Task Branch creation source == final merge target == Base Branch",
    "committed Review Target",
    "Base Commit..Review Commit",
    "git merge --ff-only",
    "Reviewed Commit == Approved Commit == Integrated Commit",
    "invalidates prior approval",
    "Multi-Repository Tasks",
    "new explicit `INTEGRATE` prompt",
)

WORKFLOW_TOKENS = (
    "preparation of the Independent Review handoff",
    "human user owns creation of the new Codex B session",
    "manual transfer of the formal review artifacts",
    "HARD STOP",
    "Engineering Result Report",
    "INTEGRATE | REVISE | ABORT",
    "decision input and precedes integration",
)

WORKFLOW_FORBIDDEN_TOKENS = (
    "review orchestration",
    "ff-only local integration ←",
    "Engineering Result Report to ChatGPT",
)

DESIGN_CONVERSATION_TOKENS = (
    "self-contained, project-agnostic Human–ChatGPT protocol",
    "MUST`, `MUST NOT`, and `MAY`",
    "All content within a Decision Unit or Checkpoint MUST be English",
    "Conversation MUST NOT have a protocol-defined lifecycle, phase, mode, completion state, or readiness state",
    "Ordinary conversation MUST NOT directly mutate persistent design state",
    "Persistent Decision Maturity MUST be exactly `Stable` or `Draft`",
    "Human Decision Actions, State Operations, and Maturity are distinct protocol concepts",
    "Persistent design state MUST change only through an explicit Human Decision Action",
    "Exact Copy means transformation-free copying",
    "Semantic equivalence MUST NOT satisfy Exact Copy",
    "Goal MUST NOT be persistent design state",
    "Decision Unit: D-NNN",
    "beginning with `D-001`",
    "MUST NOT be reused",
    "Proposal\n<complete canonical design content>\nAccept",
    "Retain\n<one or more State Operations>",
    "first non-whitespace token",
    "case-sensitive canonical token `Accept` or `Retain`",
    "MUST cease to be selectable",
    "MUST NOT be inferred from synonyms, translations, semantic intent",
    "without realizing the persistent-state transformation predeclared under `Accept`",
    "The retained Draft content MUST be an Exact Copy of the complete Proposal",
    "it MUST use exactly one `Modify` operation and MUST preserve that entry's Decision ID",
    "Operation | Maturity | Decision ID: Before → After",
    "State Operations MUST be exactly `Add`, `Modify`, and `Delete`",
    "Every State Operation MUST be executed mechanically without transformation",
    "no persistent entry with that Decision ID MUST exist",
    "MUST preserve its Decision ID and Maturity",
    "MUST still match `Before` using Exact Copy semantics",
    "A Maturity change MUST NOT use `Modify`",
    "When `Accept` resolves a Draft entry, the State Operation sequence MUST delete that Draft entry",
    "Goal\n<the single current Goal>\nStable",
    "Draft\n<all current Draft entries, or None>",
    "An empty `Stable` or `Draft` section MUST contain exactly `None`",
    "ordered by Decision ID in ascending numeric order",
)

DESIGN_CONVERSATION_FORBIDDEN_TOKENS = (
    "EXPLORE",
    "CONVERGE",
    "PRE-FREEZE",
    "FREEZE",
    "COMPILE",
    "接受",
    "待定",
    "拒绝",
    "状态变更记录",
)

MAINTAINER_DESIGN_CONVERSATION_TOKENS = (
    "template/.ai/DESIGN_CONVERSATION_PROTOCOL.md",
    "canonical shared behavior",
    "governance",
    "payload",
    "project-agnostic",
    "Authoritative Task Core",
    "Independent Review",
    "`Stable` / `Draft`",
    "Human Decision Actions",
    "State Operations",
    "Exact Copy",
    "do not add a conversation lifecycle",
    "explicit Human Decision Action",
)

TASK_SECTIONS = (
    "Task ID",
    "Revision",
    "Task Type: `READ_ONLY | CHANGE`",
    "Base Branch: `NOT_APPLICABLE | <branch> | INHERIT_DEFAULT`",
    "## Goal",
    "## Context",
    "## In Scope",
    "## Repository Scope",
    "## Out of Scope",
    "## Requirements",
    "## Constraints",
    "## Authoritative References",
    "## Acceptance Criteria",
    "## Verification",
    "## Preliminary Version Impact",
)

REVIEW_PROMPT_TOKENS = (
    "Task ID",
    "Review Attempt: `N / 3`",
    "Previous Review",
    "Review Objective",
    "Original Task",
    "Base Branch",
    "Base Commit",
    "Review Commit",
    "Authoritative References",
    "In Scope",
    "Out of Scope",
    "Changed Areas",
    "Verification",
    "CODEX_REVIEW_REPORT_TEMPLATE.md",
    "read-only",
    "MUST be executed by Codex B in a new Codex session explicitly created by the human user",
    "human user must manually transfer this prompt",
    "Codex A MUST stop after producing this prompt",
    "do not consume Review Attempt count",
    "Task Branch",
    "Review Commit may remain unchanged",
    "complete repository change set",
)

REVIEW_REPORT_TOKENS = (
    "Task ID",
    "Review Attempt",
    "Base Commit",
    "Reviewed Commit",
    "Human-created Codex B session: `YES`",
    "Review Prompt supplied by human user: `YES`",
    "APPROVED | CHANGES_REQUESTED",
    "Findings",
    "Issue",
    "Evidence",
    "Required Change",
    "Verification",
    "Notes",
    "Repository Change Set Reviewed",
)

RESULT_TOKENS = (
    "Task ID",
    "Revision",
    "Task Type",
    "Original Task",
    "COMPLETED | AWAITING_DISPOSITION | BLOCKED",
    "Terminal Engineering Status remains `COMPLETED | BLOCKED`",
    "Result Summary",
    "Repository State",
    "Base Branch",
    "Verification",
    "Independent Review",
    "Acceptance",
    "Blocked",
    "Deviations",
    "Remaining Notes",
    "Required Disposition",
    "INPUT_REQUIRED | DECISION_REQUIRED | REVIEW_LIMIT_REACHED",
    "Repository Changes = `NO`",
    "Independent Review = `NOT_APPLICABLE`",
    "Independent Review = `APPROVED`",
    "Reviewed Commit == Approved Commit",
    "PENDING_EXPLICIT_INTEGRATE",
    "Automation Opportunities",
    "INTEGRATE | REVISE | ABORT",
    "Performed in human-created Codex B session: `NOT_APPLICABLE | YES`",
    "Review Prompt and Review Report manually transferred by human user: `NOT_APPLICABLE | YES`",
    "Remote Publication",
)

EXACT_COPY_TOKENS = (
    "copy the entire Core exactly",
    "Exact textual equality, not semantic equivalence",
    "no trim, dedent, newline normalization, Markdown normalization",
    "MUST actually embed the complete Core",
    "external dependency",
    "runtime pre-handoff",
    "MUST NOT present a failing prompt",
    "no additional formal artifact",
)

POST_ERR_TOKENS = (
    "provides judgment or recommendation to the human",
    "returns that decision input to ChatGPT / Design Owner",
    "new, complete, explicit post-ERR Codex A prompt",
    "which the human transfers to Codex A",
    "A bare disposition token is not a complete",
    "re-apply the currently authoritative applicable Integration Gate",
    "Concrete Git Integration Gate semantics remain owned only by `.ai/GIT_WORKFLOW.md`",
)

CORE_TRANSFER_FORBIDDEN_TOKENS = (
    "Formatting-only transformations are allowed",
    "Formatting-only transformations may preserve",
    "meaning-preserving transformation",
    "semantic equivalence is sufficient",
)

ERR_FORBIDDEN_TOKENS = (
    "returns it in a new explicit prompt to Codex A",
    "select `INTEGRATE | REVISE | ABORT` and return a new explicit prompt to Codex A",
)

ROOT_WORKSPACE_MANDATORY_TOKENS = (
    "Every `CHANGE` Task resolves one immutable workspace Base Branch",
    "exactly one dedicated workspace `task/*` branch is required",
    "identifying the Base Branch, Base Commit, Task Branch, and Review Commit.",
    "Identify the workspace and expected changed child repositories",
    "Use `WORKSPACE_ONLY` when applicable",
    "### Changed Child Repository Review Targets",
    "Confirm that the workspace Review Commit records each exact child Review Commit",
    "Record the workspace target and every changed child repository target",
    "repeat these identity fields for the workspace and every modified child",
)


def require_tokens(errors, label, path, tokens):
    if not path.is_file():
        errors.append(f"{label}: missing {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            errors.append(
                f"{label}: {path.relative_to(ROOT)} missing required literal '{token}'"
            )


def reject_tokens(errors, label, path, tokens):
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token in text:
            errors.append(
                f"{label}: {path.relative_to(ROOT)} contains forbidden literal '{token}'"
            )


def require_ordered_unique_boundaries(errors, label, path, begin, end):
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    begin_lines = [index for index, line in enumerate(lines) if line == begin]
    end_lines = [index for index, line in enumerate(lines) if line == end]
    if len(begin_lines) != 1 or len(end_lines) != 1:
        errors.append(
            f"{label}: {path.relative_to(ROOT)} must contain exactly one canonical "
            "begin boundary and one canonical end boundary"
        )
    elif begin_lines[0] >= end_lines[0]:
        errors.append(
            f"{label}: {path.relative_to(ROOT)} canonical Core boundaries are out of order"
        )


def main():
    errors = []

    for label, ai_dir in LAYERS.items():
        for filename in REQUIRED_FILES:
            path = ai_dir / filename
            if not path.is_file():
                errors.append(f"{label}: missing {path.relative_to(ROOT)}")

        require_tokens(errors, label, ai_dir / "AI_HANDOFF_PROTOCOL.md", HANDOFF_TOKENS)
        require_tokens(errors, label, ai_dir / "GIT_WORKFLOW.md", GIT_TOKENS)
        require_tokens(errors, label, ai_dir / "WORKFLOW.md", WORKFLOW_TOKENS)
        protocol_tokens = (
            MAINTAINER_DESIGN_CONVERSATION_TOKENS
            if label == "root"
            else DESIGN_CONVERSATION_TOKENS
        )
        require_tokens(
            errors,
            label,
            ai_dir / "DESIGN_CONVERSATION_PROTOCOL.md",
            protocol_tokens,
        )
        if label == "template":
            reject_tokens(
                errors,
                label,
                ai_dir / "DESIGN_CONVERSATION_PROTOCOL.md",
                DESIGN_CONVERSATION_FORBIDDEN_TOKENS,
            )
        reject_tokens(
            errors,
            label,
            ai_dir / "WORKFLOW.md",
            WORKFLOW_FORBIDDEN_TOKENS,
        )
        require_tokens(errors, label, ai_dir / "CODEX_TASK_TEMPLATE.md", TASK_SECTIONS)
        require_tokens(
            errors,
            label,
            ai_dir / "CODEX_REVIEW_PROMPT_TEMPLATE.md",
            REVIEW_PROMPT_TOKENS,
        )
        require_tokens(
            errors,
            label,
            ai_dir / "CODEX_REVIEW_REPORT_TEMPLATE.md",
            REVIEW_REPORT_TOKENS,
        )
        require_tokens(
            errors,
            label,
            ai_dir / "ENGINEERING_RESULT_TEMPLATE.md",
            RESULT_TOKENS,
        )
        require_tokens(
            errors,
            label,
            ai_dir / "AI_HANDOFF_PROTOCOL.md",
            EXACT_COPY_TOKENS + POST_ERR_TOKENS,
        )
        reject_tokens(
            errors,
            label,
            ai_dir / "AI_HANDOFF_PROTOCOL.md",
            CORE_TRANSFER_FORBIDDEN_TOKENS,
        )
        reject_tokens(
            errors,
            label,
            ai_dir / "CODEX_TASK_TEMPLATE.md",
            CORE_TRANSFER_FORBIDDEN_TOKENS,
        )
        reject_tokens(
            errors,
            label,
            ai_dir / "ENGINEERING_RESULT_TEMPLATE.md",
            ERR_FORBIDDEN_TOKENS,
        )
        require_tokens(
            errors,
            label,
            ai_dir / "CODEX_TASK_TEMPLATE.md",
            (
                "canonical Original Core operand",
                "all raw text after the newline",
                "before the `## End Authoritative Task Core` boundary line",
                "no trim, dedent, newline normalization, or Markdown normalization",
            ),
        )
        require_tokens(
            errors,
            label,
            ai_dir / "CODEX_REVIEW_PROMPT_TEMPLATE.md",
            (
                "complete actual Authoritative Task Core copied exactly",
                "canonical Embedded Core operand",
                "Empty content, placeholders, TODOs, copy instructions",
                "Original Authoritative Task Core == Embedded Authoritative Task Core",
                "MUST NOT present it as the formal Independent Review handoff",
            ),
        )
        require_tokens(
            errors,
            label,
            ai_dir / "ENGINEERING_RESULT_TEMPLATE.md",
            (
                "returns that decision input to ChatGPT / Design Owner",
                "Design Owner compiles the complete explicit post-ERR Codex A prompt",
                "human transfers that complete prompt to Codex A",
                "bare disposition token is not sufficient downstream execution authorization",
            ),
        )

        task_path = ai_dir / "CODEX_TASK_TEMPLATE.md"
        require_ordered_unique_boundaries(
            errors,
            label,
            task_path,
            "## Authoritative Task Core",
            "## End Authoritative Task Core",
        )
        review_path = ai_dir / "CODEX_REVIEW_PROMPT_TEMPLATE.md"
        require_ordered_unique_boundaries(
            errors,
            label,
            review_path,
            (
                "<!-- BEGIN VERBATIM AUTHORITATIVE TASK CORE -->"
                if label == "root"
                else "BEGIN VERBATIM AUTHORITATIVE TASK CORE"
            ),
            (
                "<!-- END VERBATIM AUTHORITATIVE TASK CORE -->"
                if label == "root"
                else "END VERBATIM AUTHORITATIVE TASK CORE"
            ),
        )

    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "GIT_WORKFLOW.md",
        (
            "repository-specific governance or configuration",
            "affected but unmodified repository",
            "Repository Scope",
            "Repository Dependencies",
            "dependency-consistent order",
            "complete Task Review Target",
            "single Task-level Formal Independent Review",
            "Workspace Recording a Managed-Repository Commit",
            "create the workspace Task Branch",
            "establish the managed-repository Review Commit",
            "integrate the managed repository first",
            "integrate the workspace last",
        ),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "AI_HANDOFF_PROTOCOL.md",
        (
            "Each modified repository resolves one immutable Base Branch",
            "Affected but unmodified repositories",
            "complete Task Review Target",
            "one Task-level review",
            "relevant cross-repository consistency",
        ),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "CODEX_TASK_TEMPLATE.md",
        ("`MODIFIED` or `AFFECTED_UNMODIFIED`", "single-repository Task"),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "CODEX_REVIEW_PROMPT_TEMPLATE.md",
        ("Task Review Target", "Affected but Unmodified Repositories"),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "CODEX_REVIEW_REPORT_TEMPLATE.md",
        ("complete Task Review Target", "one Task-level"),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "ENGINEERING_RESULT_TEMPLATE.md",
        ("every modified repository", "Affected but Unmodified Repositories"),
    )
    for filename in (
        "AI_HANDOFF_PROTOCOL.md",
        "CODEX_TASK_TEMPLATE.md",
        "CODEX_REVIEW_PROMPT_TEMPLATE.md",
        "CODEX_REVIEW_REPORT_TEMPLATE.md",
        "ENGINEERING_RESULT_TEMPLATE.md",
    ):
        reject_tokens(
            errors,
            "root",
            LAYERS["root"] / filename,
            ROOT_WORKSPACE_MANDATORY_TOKENS,
        )
    reject_tokens(
        errors,
        "root",
        LAYERS["root"] / "GIT_WORKFLOW.md",
        (
            "For `codex-template`, the Default Base Branch is `main`.",
            "workspace is the composition anchor and always",
            "workspace branch",
        ),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "CODEX_TASK_TEMPLATE.md",
        (
            "## Authoritative Task Core",
            "copy this entire operand exactly",
            "MUST NOT rewrite, summarize, normalize, reformat, correct",
            "## End Authoritative Task Core",
        ),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "CODEX_REVIEW_PROMPT_TEMPLATE.md",
        (
            "Inherited Authoritative Task Core",
            "BEGIN VERBATIM AUTHORITATIVE TASK CORE",
            "Codex A-Produced Review Context",
            "Implementation Outcome and Decisions",
            "Codex A Verification Evidence",
            "Previous-Review State",
        ),
    )
    require_tokens(
        errors,
        "root",
        LAYERS["root"] / "ENGINEERING_RESULT_TEMPLATE.md",
        (
            "Primary Consumer and Evidence Boundary",
            "Implementation Outcome",
            "Presented Task HEAD",
            "Identity Consistency",
            "Criterion | Evidence | Status",
            "Important Checks Not Performed",
            "Material Findings and Resolutions",
            "Reviewer-Confirmed Material Properties",
            "Residual Risks and Limitations",
            "Codex A Engineering Recommendation",
        ),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "GIT_WORKFLOW.md",
        (
            "The template default is `main`",
            "may configure another",
            "affected but unmodified repository",
            "Repository Scope",
            "Repository Dependencies",
            "complete Task Review Target",
            "single Task-level Formal Independent Review",
            "Workspace Recording a Managed-Repository Commit",
        ),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "AI_HANDOFF_PROTOCOL.md",
        (
            "Each modified repository resolves one immutable Base Branch",
            "Affected but unmodified repositories",
            "complete Task Review Target",
            "one Task-level review",
            "relevant cross-repository consistency",
        ),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "CODEX_TASK_TEMPLATE.md",
        ("`MODIFIED` or `AFFECTED_UNMODIFIED`", "single-repository Task"),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "CODEX_REVIEW_PROMPT_TEMPLATE.md",
        ("Task Review Target", "Affected but Unmodified Repositories"),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "CODEX_REVIEW_REPORT_TEMPLATE.md",
        ("complete Task Review Target", "one Task-level"),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "ENGINEERING_RESULT_TEMPLATE.md",
        ("every modified repository", "Affected but Unmodified Repositories"),
    )
    for filename in (
        "AI_HANDOFF_PROTOCOL.md",
        "CODEX_TASK_TEMPLATE.md",
        "CODEX_REVIEW_PROMPT_TEMPLATE.md",
        "CODEX_REVIEW_REPORT_TEMPLATE.md",
        "ENGINEERING_RESULT_TEMPLATE.md",
    ):
        reject_tokens(
            errors,
            "template",
            LAYERS["template"] / filename,
            ROOT_WORKSPACE_MANDATORY_TOKENS,
        )
    reject_tokens(
        errors,
        "template",
        LAYERS["template"] / "GIT_WORKFLOW.md",
        (
            "workspace is the composition anchor and always",
            "workspace Task Branch. Multi-repository child branches",
        ),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "CODEX_TASK_TEMPLATE.md",
        (
            "## Authoritative Task Core",
            "copy this entire operand exactly",
            "MUST NOT rewrite, summarize, normalize, reformat, correct",
            "## End Authoritative Task Core",
        ),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "CODEX_REVIEW_PROMPT_TEMPLATE.md",
        (
            "Inherited Authoritative Task Core",
            "BEGIN VERBATIM AUTHORITATIVE TASK CORE",
            "Codex A-Produced Review Context",
            "Implementation Outcome and Decisions",
            "Codex A Verification Evidence",
            "Previous-Review State",
        ),
    )

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: AI workflow invariant validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
