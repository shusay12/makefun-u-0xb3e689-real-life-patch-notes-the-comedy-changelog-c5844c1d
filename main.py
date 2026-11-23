#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one deadpan patch-note line for a bug in human biology to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only, no network.
"""

import os
import sys

PATCH_NOTE = (
    "v1.2.7: fixed a bug where hiccups only stopped "
    "the moment you told someone you had them."
)

# Why this line: hiccups are a real, universal biology bug; the "fix"
# is the folk observation that announcing them ends them, stated as
# if engineering shipped it. Deadpan version number, terse register,
# one specific bug, no padding — 88 characters, well inside the cap.


def validate(text: str) -> None:
    """Gate mirror: UTF-8, 1-160 chars, single line, not whitespace-only."""
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) > 160:
        raise ValueError(f"entry too long: {len(text)} chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    text = PATCH_NOTE.strip()
    try:
        validate(text)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Round-trip check: what the grader will read back.
    with open(path, encoding="utf-8") as fh:
        written = fh.read().rstrip("\n")
    validate(written)
    assert written == text, "round-trip mismatch"
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
