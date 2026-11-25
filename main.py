#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

A make.fun program/v1 entry. Writes a single roast line (at most
200 characters) about a smart fridge to /output/entry.txt.

Pure standard library only: no third-party packages.
"""

import os

LINE = (
    "My smart fridge emailed my dentist a weekly report of my "
    "midnight snacks, with a chart titled 'Areas for Improvement.'"
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast line is {len(line)} chars, must be 1-200")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
