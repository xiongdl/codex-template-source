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
)

WORKFLOW_TOKENS = (
    "preparation of the Independent Review handoff",
    "human user owns creation of the new Codex B session",
    "manual transfer of the formal review artifacts",
    "HARD STOP",
)

WORKFLOW_FORBIDDEN_TOKENS = (
    "review orchestration",
)

TASK_SECTIONS = (
    "Task ID",
    "Revision",
    "Task Type: `READ_ONLY | CHANGE`",
    "Base Branch: `NOT_APPLICABLE | <branch> | INHERIT_DEFAULT`",
    "## Goal",
    "## Context",
    "## In Scope",
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
)

RESULT_TOKENS = (
    "Task ID",
    "Revision",
    "Task Type",
    "Original Task",
    "COMPLETED | BLOCKED",
    "Result Summary",
    "Repository State",
    "Base Branch",
    "Verification",
    "Independent Review",
    "Acceptance",
    "Blocked",
    "Deviations",
    "Remaining Notes",
    "Recommended Next Step",
    "INPUT_REQUIRED | DECISION_REQUIRED | REVIEW_LIMIT_REACHED",
    "Repository Changes = `NO`",
    "Independent Review = `NOT_APPLICABLE`",
    "Independent Review = `APPROVED`",
    "Reviewed Commit == Approved Commit == Integrated Commit",
    "Performed in human-created Codex B session: `NOT_APPLICABLE | YES`",
    "Review Prompt and Review Report manually transferred by human user: `NOT_APPLICABLE | YES`",
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
        "root",
        LAYERS["root"] / "GIT_WORKFLOW.md",
        ("For `codex-template`, the Default Base Branch is `main`.",),
    )
    require_tokens(
        errors,
        "template",
        LAYERS["template"] / "GIT_WORKFLOW.md",
        ("The template default is `main`", "may configure another"),
    )

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: AI workflow invariant validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
