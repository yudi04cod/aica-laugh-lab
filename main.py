#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line -- the excuse a robot vacuum gives
after eating a sock -- to /output/entry.txt.

The line is a fixed, hand-written joke. The program's job is to make
sure it obeys the competition gate (UTF-8 text, 1-200 characters, not
only whitespace, a single line) and to verify what it wrote by reading
it back.
"""

import os
import sys

# The joke. Deadpan twist: the vacuum confesses the sock looked like
# food, smelled like feet, and then it destroyed the evidence.
LINE = "It looked like a burrito, it smelled like feet, and I panicked \u2014 so I ate the evidence."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line):
    """Check the line against the competition gate.

    Returns a list of problems; an empty list means the line is valid.
    """
    problems = []
    if not isinstance(line, str):
        problems.append("line is not text")
        return problems
    if len(line) < MIN_CHARS:
        problems.append("line is empty")
    if len(line) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if not line.strip():
        problems.append("line is only whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    for char in line:
        if ord(char) < 0x20 and char not in ("\t",):
            problems.append("line contains a control character")
            break
    return problems


def main():
    problems = validate(LINE)
    if problems:
        for problem in problems:
            print("invalid: %s" % problem, file=sys.stderr)
        return 1

    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    # Read-back verification: what landed on disk must be exactly
    # the line we validated, byte for byte.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        print("verification failed: entry.txt differs from the line",
              file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(LINE), out_path))
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
