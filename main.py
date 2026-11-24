#!/usr/bin/env python3
"""Monday, Reviewed in One Line R1 — writes the entry to /output/entry.txt.

Entry: "The Refund Was a Tuesday" (108 chars, one line).
Stdlib only. The grader runs python:3.13-slim with no site-packages.
"""
import os

ENTRY = (
    "Would not recommend Monday. The commute was long, the coffee was "
    "cold, and the refund was a Tuesday."
)

OUT_PATH = "/output/entry.txt"


def main():
    # Gate: UTF-8, 1-200 characters.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    # One line: no newline characters anywhere in the entry.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    # Structure: it is a review of the entrant's own Monday, and the punch
    # lands in the last words (the refund is a Tuesday).
    assert ENTRY.startswith("Would not recommend Monday"), (
        "entry must open as a review of the entrant's own Monday"
    )
    assert ENTRY.endswith("was a Tuesday."), (
        "entry must land its punch in the last words"
    )
    assert "Monday" in ENTRY, "entry must name the Monday it reviews"
    data = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "wb") as f:
        f.write(data)
    # Byte-verify: read back exactly what was written, and re-check the
    # gate from the bytes on disk, not just the in-memory string.
    with open(OUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "bytes on disk do not match entry"
    decoded = back.decode("utf-8")  # strict: raises on invalid UTF-8
    assert decoded == ENTRY, "round-trip decode mismatch"
    assert 1 <= len(decoded) <= 200, "file on disk outside 1-200 chars"
    assert "\n" not in decoded, "file on disk is not one line"
    print(f"wrote {OUT_PATH}: {len(ENTRY)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
