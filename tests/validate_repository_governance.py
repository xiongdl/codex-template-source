#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "CHATGPT.md",
    "AGENTS.md",
    "VERSION",
    "CHANGELOG.md",
    ".ai/WORKFLOW.md",
    ".ai/TASK_READINESS.md",
    "docs/DESIGN_PRINCIPLES.md",
    "docs/TEMPLATE_ARCHITECTURE.md",
    "docs/CHANGE_POLICY.md",
    "docs/VERSIONING.md",
    "scripts/check",
]

def main():
    errors = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required repository-governance path: {rel}")

    version_path = ROOT / "VERSION"
    if version_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append(f"invalid root VERSION format: '{version}'")
        changelog = ROOT / "CHANGELOG.md"
        if changelog.is_file() and f"## {version}" not in changelog.read_text(encoding="utf-8"):
            errors.append(f"root CHANGELOG.md does not contain current version {version}")

    chatgpt_path = ROOT / "CHATGPT.md"
    if chatgpt_path.is_file():
        text = chatgpt_path.read_text(encoding="utf-8")
        for ref in (
            "VERSION",
            ".ai/TASK_READINESS.md",
            ".ai/WORKFLOW.md",
            "docs/DESIGN_PRINCIPLES.md",
            "docs/TEMPLATE_ARCHITECTURE.md",
            "docs/CHANGE_POLICY.md",
        ):
            if ref not in text:
                errors.append(f"root CHATGPT.md does not reference '{ref}'")

    agents_path = ROOT / "AGENTS.md"
    if agents_path.is_file():
        text = agents_path.read_text(encoding="utf-8")
        for ref in (
            ".ai/TASK_READINESS.md",
            "docs/DESIGN_PRINCIPLES.md",
            "docs/TEMPLATE_ARCHITECTURE.md",
            "docs/CHANGE_POLICY.md",
            "./scripts/check",
        ):
            if ref not in text:
                errors.append(f"root AGENTS.md does not reference '{ref}'")

    readiness_path = ROOT / ".ai/TASK_READINESS.md"
    if readiness_path.is_file():
        text = readiness_path.read_text(encoding="utf-8")
        for token in (
            "PASS",
            "WARNING",
            "BLOCKED",
            "Project-Agnostic",
            "Governance / Payload Boundary",
            "Reference Review Required",
            "Breaking Change Not Authorized",
            "NONE",
            "PATCH",
            "MINOR",
            "MAJOR",
            "UNKNOWN",
        ):
            if token not in text:
                errors.append(
                    f"root .ai/TASK_READINESS.md missing required concept '{token}'"
                )

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: codex-template repository governance validation succeeded")
    return 0

if __name__ == "__main__":
    sys.exit(main())
