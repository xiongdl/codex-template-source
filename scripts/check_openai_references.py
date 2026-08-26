#!/usr/bin/env python3
"""
Check tracked OpenAI reference URLs for basic availability and content changes.

This script is intentionally conservative:
- it does not modify template/
- it does not make template decisions
- it records machine-readable state locally
- a detected change means "review this source", not "change the template"

Usage:
    python scripts/check_openai_references.py
    python scripts/check_openai_references.py --update-state
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "references" / "openai" / "SOURCES.md"
STATE = ROOT / "references" / "openai" / ".source_state.json"

URL_RE = re.compile(r"^https://(?:openai\.com|help\.openai\.com)/\S+$")

def extract_urls() -> list[str]:
    urls = []
    for line in SOURCES.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if URL_RE.match(line):
            urls.append(line)
    return urls

def fetch(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "codex-template-reference-checker/1.0"},
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        body = response.read()
        return {
            "final_url": response.geturl(),
            "status": getattr(response, "status", 200),
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
            "sha256": hashlib.sha256(body).hexdigest(),
            "bytes": len(body),
        }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--update-state",
        action="store_true",
        help="accept current upstream content as the new local baseline",
    )
    args = parser.parse_args()

    previous = {}
    if STATE.exists():
        previous = json.loads(STATE.read_text(encoding="utf-8"))

    current = {}
    changed = []
    failures = []

    for url in extract_urls():
        try:
            info = fetch(url)
            current[url] = info
            old = previous.get(url)
            if old and old.get("sha256") != info["sha256"]:
                changed.append(url)
            state = "CHANGED" if url in changed else ("NEW" if old is None else "OK")
            print(f"{state:7} {info['status']} {url}")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            failures.append((url, str(exc)))
            print(f"ERROR   --- {url}: {exc}")

    if changed:
        print("\nSources requiring review:")
        for url in changed:
            print(f"- {url}")

    if args.update_state:
        STATE.write_text(
            json.dumps(current, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"\nUpdated baseline: {STATE.relative_to(ROOT)}")
    elif not STATE.exists():
        print("\nNo baseline exists yet.")
        print("After reviewing current sources, run with --update-state.")

    if failures:
        print("\nSome sources could not be checked.")
        return 2

    return 1 if changed else 0

if __name__ == "__main__":
    sys.exit(main())
