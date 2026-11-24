#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

A robot vacuum's excuse for missing a spot, written to /output/entry.txt.
Deterministic: the same line every run, no input, no network, no randomness.
The line is 120 characters: deadpan machine voice, a surprise (tenure),
and the punch at the end.
"""

import os

LINE = (
    "I did not miss the spot. I ran a cost-benefit analysis: "
    "the dust bunny has tenure, my battery has 4%, and I choose life."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
