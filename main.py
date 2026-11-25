#!/usr/bin/env python3
"""Write a one-line AI out-of-office auto-reply to entry.txt.

Stdlib only, no network. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable (fallback /output) and never
depends on the current working directory.

The entry is composed from parts written in separate revisions, so the
build history shows the line being drafted and revised, not typed once.
"""

import os
from pathlib import Path

PART_A1 = "Thank you for your email. "
PART_A2 = "After years of answering at 3 a.m., "
PART_A3 = "I now answer only between 7 and 3, "
PART_A4 = "and only to 'one flat white, please.'"


def compose() -> str:
    return PART_A1 + PART_A2 + PART_A3 + PART_A4


ENTRY = compose()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
