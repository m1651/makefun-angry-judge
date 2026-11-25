#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt (1-400 characters, UTF-8).
"""

import os

RANT = (
    "The office printer has one job and it has chosen violence. "
    "It jams only on the page I need, prints my boarding pass in a font "
    "last seen on a ransom note, and blinks PC LOAD LETTER like a threat. "
    "I have fed it paper, ink, and the best years of my career. "
    "It has repaid me in paper cuts and contempt."
)


def main() -> None:
    text = RANT.strip()
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"rant is {len(text)} chars, must be 1-400")
    if not text.strip():
        raise SystemExit("rant must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(
        f"Wrote /output/entry.txt "
        f"({len(text)} chars, {len(text.encode('utf-8'))} bytes): {text}"
    )


if __name__ == "__main__":
    main()
