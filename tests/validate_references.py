#!/usr/bin/env python3

from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = ROOT / "references" / "openai" / "snapshots"

DIR_RE = re.compile(r"^(OAI-\d{3})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.(pdf|html|md)$")
APPROVED_DOMAINS = (
    "openai.com",
    "help.openai.com",
    "platform.openai.com",
    "developers.openai.com",
    "cdn.openai.com",
)

def parse_simple_yaml(path: Path) -> dict[str, str]:
    """
    Minimal parser for the flat metadata.yaml schema used here.
    Avoids adding a PyYAML dependency to template governance.
    """
    data: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid metadata line: {raw!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key or not value:
            raise ValueError(f"invalid metadata entry: {raw!r}")
        data[key] = value
    return data

def valid_openai_url(url: str) -> bool:
    if not url.startswith("https://"):
        return False
    host = url[len("https://"):].split("/", 1)[0].split(":", 1)[0].lower()
    return any(host == d or host.endswith("." + d) for d in APPROVED_DOMAINS)

def main() -> int:
    errors: list[str] = []

    if not SNAPSHOTS.is_dir():
        errors.append("missing references/openai/snapshots/")
    else:
        seen_ids: set[str] = set()

        for entry in sorted(SNAPSHOTS.iterdir()):
            if entry.name == "README.md":
                continue

            if not entry.is_dir():
                errors.append(f"unexpected file in snapshots root: {entry.name}")
                continue

            match = DIR_RE.fullmatch(entry.name)
            if not match:
                errors.append(
                    f"invalid source directory '{entry.name}'; expected OAI-NNN-<lowercase-slug>"
                )
                continue

            source_id = match.group(1)
            if source_id in seen_ids:
                errors.append(f"duplicate source ID: {source_id}")
            seen_ids.add(source_id)

            metadata = entry / "metadata.yaml"
            if not metadata.is_file():
                errors.append(f"{entry.name}: missing metadata.yaml")
            else:
                try:
                    meta = parse_simple_yaml(metadata)
                except ValueError as exc:
                    errors.append(f"{entry.name}/metadata.yaml: {exc}")
                    meta = {}

                required = ("id", "title", "source", "url")
                for key in required:
                    if not meta.get(key):
                        errors.append(f"{entry.name}/metadata.yaml: missing '{key}'")

                if meta.get("id") and meta["id"] != source_id:
                    errors.append(
                        f"{entry.name}/metadata.yaml: id '{meta['id']}' does not match '{source_id}'"
                    )

                if meta.get("source") and meta["source"] != "OpenAI":
                    errors.append(
                        f"{entry.name}/metadata.yaml: source must be exactly 'OpenAI'"
                    )

                if meta.get("url") and not valid_openai_url(meta["url"]):
                    errors.append(
                        f"{entry.name}/metadata.yaml: URL is not an approved OpenAI HTTPS URL"
                    )

            seen_dates: set[str] = set()
            for child in sorted(entry.iterdir()):
                if child.name == "metadata.yaml":
                    continue

                if child.is_dir():
                    errors.append(f"{entry.name}: unexpected subdirectory '{child.name}'")
                    continue

                m = FILE_RE.fullmatch(child.name)
                if not m:
                    errors.append(
                        f"{entry.name}: invalid snapshot filename '{child.name}'; "
                        "expected YYYY-MM-DD.(pdf|html|md)"
                    )
                    continue

                date_text = m.group(1)
                try:
                    date.fromisoformat(date_text)
                except ValueError:
                    errors.append(
                        f"{entry.name}: invalid calendar date in '{child.name}'"
                    )
                    continue

                if date_text in seen_dates:
                    errors.append(
                        f"{entry.name}: multiple snapshots for date {date_text}"
                    )
                seen_dates.add(date_text)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: OpenAI snapshot references validation succeeded")
    return 0

if __name__ == "__main__":
    sys.exit(main())
