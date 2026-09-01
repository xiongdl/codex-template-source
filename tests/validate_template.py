#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess
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
    ".ai/DESIGN_CONVERSATION_PROTOCOL.md",
    ".ai/PROJECT_INIT.md",
    ".ai/TASK_READINESS.md",
    ".ai/CODEX_TASK_TEMPLATE.md",
    ".ai/AI_HANDOFF_PROTOCOL.md",
    ".ai/GIT_WORKFLOW.md",
    ".ai/CODEX_REVIEW_PROMPT_TEMPLATE.md",
    ".ai/CODEX_REVIEW_REPORT_TEMPLATE.md",
    ".ai/ENGINEERING_RESULT_TEMPLATE.md",
    "docs/ARCHITECTURE.md",
    "docs/PROJECT_STATUS.md",
    "docs/REPRODUCIBILITY.md",
    "docs/VERSIONING.md",
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

    for rel in ("components", "tests", "integration"):
        path = TEMPLATE / rel
        if path.exists() and any(item.is_file() for item in path.rglob("*")):
            errors.append(f"template must not prescribe generic workspace directory: {rel}")

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
            if re.search(rf"\b{re.escape(term)}\b", text):
                errors.append(
                    f"project-specific term '{term}' found in {p.relative_to(TEMPLATE)}"
                )

    script = TEMPLATE / "scripts/project"
    if script.exists():
        text = script.read_text(encoding="utf-8", errors="ignore")
        for command in ["setup", "build", "test", "verify", "clean", "status"]:
            if command not in text:
                errors.append(f"scripts/project does not document '{command}'")
        status_result = subprocess.run(
            [str(script), "status"], capture_output=True, text=True, check=False
        )
        if status_result.returncode != 0 or "NOT_IMPLEMENTED" not in status_result.stdout:
            errors.append("scripts/project status must report capability state successfully")
        if "verify: AVAILABLE" not in status_result.stdout:
            errors.append("scripts/project status must report native verify as AVAILABLE")
        verify_result = subprocess.run(
            [str(script), "verify"], capture_output=True, text=True, check=False
        )
        if verify_result.returncode != 0 or "verify: PASS" not in verify_result.stdout:
            errors.append("scripts/project verify must validate the distributable baseline")

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
            ".ai/DESIGN_CONVERSATION_PROTOCOL.md",
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
        for token in ("git rev-parse --verify HEAD", ".ai/PROJECT_INIT.md", "not a third Task Type"):
            if token not in agents:
                errors.append(f"template/AGENTS.md missing Bootstrap routing concept '{token}'")

    project_init_path = TEMPLATE / ".ai/PROJECT_INIT.md"
    if project_init_path.is_file():
        project_init = project_init_path.read_text(encoding="utf-8")
        for token in (
            "no valid Git `HEAD`", "Initial Commit", "not a third Engineering Task Type",
            "status", "observational", "verify", "setup", "build", "test", "clean",
            "NOT_IMPLEMENTED", "child repositories", "Do not restructure",
        ):
            if token not in project_init:
                errors.append(f"PROJECT_INIT.md missing Bootstrap concept '{token}'")

    reproducibility_path = TEMPLATE / "docs/REPRODUCIBILITY.md"
    if reproducibility_path.is_file():
        reproducibility = reproducibility_path.read_text(encoding="utf-8")
        for token in (
            "Environment Modules", "workspace-owned", "env/<name>.csh",
            "env/modulefiles/", "Conda", "pip", "AsciiDoc", "Asciidoctor PDF",
            ".drawio", "draw.io Desktop 31.3.2", "--svg-theme light",
        ):
            if token not in reproducibility:
                errors.append(f"docs/REPRODUCIBILITY.md missing engineering infrastructure concept '{token}'")

    if (TEMPLATE / "env").exists():
        errors.append("template must not pre-create placeholder environment combinations")

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

    # Entry points navigate to the durable workflow contracts.
    for rel in ("AGENTS.md", "CHATGPT.md", "README.md"):
        path = TEMPLATE / rel
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for ref in (".ai/AI_HANDOFF_PROTOCOL.md", ".ai/GIT_WORKFLOW.md"):
                if ref not in text:
                    errors.append(f"template/{rel} does not reference '{ref}'")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: codex-template validation succeeded")
    return 0

if __name__ == "__main__":
    sys.exit(main())
