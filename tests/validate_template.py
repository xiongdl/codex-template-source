#!/usr/bin/env python3

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template"

REQUIRED = [
    "AGENTS.md",
    "README.md",
    ".ai/WORKFLOW.md",
    ".ai/PROJECT_INIT.md",
    ".ai/CODEX_TASK_TEMPLATE.md",
    "docs/ARCHITECTURE.md",
    "docs/PROJECT_STATUS.md",
    "docs/REPRODUCIBILITY.md",
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

    governance_leaks = [
        "CHANGELOG.md",
        "VERSION",
        "docs/DESIGN_PRINCIPLES.md",
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

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: codex-template validation succeeded")
    return 0

if __name__ == "__main__":
    sys.exit(main())
