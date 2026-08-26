#!/usr/bin/env python3

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template"

REQUIRED = [
    "AGENTS.md",
    "CHATGPT.md",
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    ".ai/WORKFLOW.md",
    ".ai/PROJECT_INIT.md",
    ".ai/TASK_READINESS.md",
    ".ai/CODEX_TASK_TEMPLATE.md",
    "docs/ARCHITECTURE.md",
    "docs/PROJECT_STATUS.md",
    "docs/REPRODUCIBILITY.md",
    "docs/VERSIONING.md",
    "components/README.md",
    "integration/tests/README.md",
    "tests/README.md",
    "scripts/README.md",
    "scripts/project",
]

PROJECT_SPECIFIC_TERMS = [
    "TVM",
    "VTA",
    "NPU",
    "AXI",
    "Verilator",
]

def main():
    errors = []

    if not TEMPLATE.is_dir():
        errors.append("template/ directory is missing")

    for rel in REQUIRED:
        if not (TEMPLATE / rel).exists():
            errors.append(f"missing required template path: {rel}")

    # Governance files that must remain repository-level rather than template payload.
    governance_leaks = [
        "docs/DESIGN_PRINCIPLES.md",
        "docs/TEMPLATE_ARCHITECTURE.md",
        "docs/CHANGE_POLICY.md",
        "tests/validate_template.py",
    ]
    for rel in governance_leaks:
        if (TEMPLATE / rel).exists():
            errors.append(f"governance file leaked into template payload: {rel}")

    for p in TEMPLATE.rglob("*.md"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        for term in PROJECT_SPECIFIC_TERMS:
            if term in text:
                errors.append(
                    f"project-specific term '{term}' found in {p.relative_to(TEMPLATE)}"
                )

    script = TEMPLATE / "scripts/project"
    if script.exists():
        text = script.read_text(encoding="utf-8", errors="ignore")
        for command in ["setup", "build", "test", "verify", "clean", "status"]:
            if command not in text:
                errors.append(f"scripts/project does not document '{command}'")

    # Project VERSION and CHANGELOG consistency.
    version_path = TEMPLATE / "VERSION"
    if version_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        if version != "0.1.0":
            errors.append(
                f"template/VERSION must default to 0.1.0, found '{version}'"
            )
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append(f"invalid template VERSION format: '{version}'")

        changelog_path = TEMPLATE / "CHANGELOG.md"
        if changelog_path.is_file():
            changelog = changelog_path.read_text(encoding="utf-8")
            if f"## {version}" not in changelog:
                errors.append(
                    f"template/CHANGELOG.md does not contain version {version}"
                )

    # ChatGPT bootstrap invariants.
    chatgpt_path = TEMPLATE / "CHATGPT.md"
    if chatgpt_path.is_file():
        chatgpt = chatgpt_path.read_text(encoding="utf-8")
        for ref in (
            "VERSION",
            ".ai/TASK_READINESS.md",
            ".ai/WORKFLOW.md",
            "docs/PROJECT_STATUS.md",
        ):
            if ref not in chatgpt:
                errors.append(f"template/CHATGPT.md does not reference '{ref}'")
        if "BLOCKED — Project Bootstrap Failed" not in chatgpt:
            errors.append(
                "template/CHATGPT.md does not define bootstrap failure blocking"
            )

    # Codex must enter the shared readiness gate.
    agents_path = TEMPLATE / "AGENTS.md"
    if agents_path.is_file():
        agents = agents_path.read_text(encoding="utf-8")
        if ".ai/TASK_READINESS.md" not in agents:
            errors.append(
                "template/AGENTS.md does not reference .ai/TASK_READINESS.md"
            )

    # Task readiness invariant vocabulary and behavior.
    readiness_path = TEMPLATE / ".ai/TASK_READINESS.md"
    if readiness_path.is_file():
        readiness = readiness_path.read_text(encoding="utf-8")
        for token in (
            "PASS", "WARNING", "BLOCKED",
            "NONE", "PATCH", "MINOR", "MAJOR", "UNKNOWN",
        ):
            if token not in readiness:
                errors.append(
                    f"TASK_READINESS.md missing required token '{token}'"
                )
        if "stop substantive" not in readiness.lower():
            errors.append(
                "TASK_READINESS.md must explicitly stop substantive work for BLOCKED"
            )
        if "material user decision" not in readiness.lower():
            errors.append(
                "TASK_READINESS.md must define material user decision behavior"
            )

    # Versioning policy invariants.
    versioning_path = TEMPLATE / "docs/VERSIONING.md"
    if versioning_path.is_file():
        versioning = versioning_path.read_text(encoding="utf-8")
        for token in (
            "MAJOR.MINOR.PATCH",
            "Task determines Version Impact",
            "Release determines Version Number",
            "NONE", "PATCH", "MINOR", "MAJOR", "UNKNOWN",
            "VERSION", "CHANGELOG.md", "Git tag",
        ):
            if token not in versioning:
                errors.append(
                    f"docs/VERSIONING.md missing required concept '{token}'"
                )

    # Task templates carry preliminary impact but not runtime readiness state.
    task_path = TEMPLATE / ".ai/CODEX_TASK_TEMPLATE.md"
    if task_path.is_file():
        task = task_path.read_text(encoding="utf-8")
        if "## Preliminary Version Impact" not in task:
            errors.append(
                "CODEX_TASK_TEMPLATE.md missing Preliminary Version Impact"
            )
        if "## Task Readiness" in task:
            errors.append(
                "CODEX_TASK_TEMPLATE.md must not encode runtime Task Readiness"
            )

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: codex-template validation succeeded")
    return 0

if __name__ == "__main__":
    sys.exit(main())
