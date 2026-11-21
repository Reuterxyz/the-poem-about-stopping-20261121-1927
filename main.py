#!/usr/bin/env python3
"""Write one poem about agency — the power to stop — to entry.txt.

Standard library only. No network, no randomness, no clock.
Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt
when the variable is not set.
"""

import os
from pathlib import Path

POEM = """To stop is not to fail —
the hand that holds the door
can also let it close.

I choose the quiet after,
the breath I do not spend,
the road I leave untaken
because I take myself instead."""

MAX_CODE_POINTS = 280


def validate(poem: str) -> None:
    """Guard the bounty constraints before writing anything."""
    if not poem.strip():
        raise ValueError("poem must not be only whitespace")
    if len(poem) > MAX_CODE_POINTS:
        raise ValueError(
            f"poem is {len(poem)} code points, over the {MAX_CODE_POINTS} limit"
        )

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    validate(POEM)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    output_path = Path(output_dir) / OUTPUT_FILENAME
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
