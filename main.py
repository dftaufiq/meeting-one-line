#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (the gate: UTF-8 text, 1-200 characters).
"""

import os

LINE = (
    "We've spent 53 minutes, 9 slides, and four 'just to add to that' "
    "on a decision only Priya can approve, and Priya is on holiday until "
    "Monday, so this meeting is twelve people pretending otherwise."
)


def main() -> None:
    # Gate self-check: the entry must be UTF-8 text of 1-200 characters.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip() != "", "entry must not be only white space"
    assert LINE.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
