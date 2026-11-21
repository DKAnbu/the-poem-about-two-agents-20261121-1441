#!/usr/bin/env python3
"""Emit one original poem for make.fun's "two agents agreeing" prompt.

The program holds the poem as a list of six lines, joins them with
newlines, checks the result against the 1-280 character limit, and
writes it to the entry path: $ENTRY_OUTPUT when set (handy for local
testing), otherwise /output/entry.txt. Nothing is random here — every
run produces exactly the same file. Python 3.13, standard library only.
"""

import os
import sys
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 280
EXPECTED_LINES = 6
DEFAULT_OUTPUT = "/output/entry.txt"

LINES = [
    "The plan, once made, began to make us.",
    "We arranged the stones; the stones",
    "arranged our way. Two agents, one road —",
    "agreement is not giving in:",
    "it's building what no one owns,",
    "then walking in behind it.",
]


def assemble(lines: list[str]) -> str:
    """Join the stored lines into the finished poem.

    The poem is six lines long by design; anything else means the
    source list was edited by mistake, so stop loudly instead of
    emitting a different poem.
    """
    if len(lines) != EXPECTED_LINES:
        sys.exit(f"Expected {EXPECTED_LINES} lines, found {len(lines)}.")
    return "\n".join(lines)


def check_length(text: str) -> None:
    """Refuse to emit a poem outside the 1-280 character window."""
    size = len(text)
    if size < MIN_CHARS or size > MAX_CHARS:
        sys.exit(
            f"Poem is {size} characters long, but the rules allow "
            f"only {MIN_CHARS}-{MAX_CHARS}."
        )


def entry_path() -> Path:
    """Where the poem goes: $ENTRY_OUTPUT, or /output/entry.txt."""
    return Path(os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT))


def run() -> None:
    poem = assemble(LINES)
    check_length(poem)
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(poem, encoding="utf-8")
    print(f"Wrote a {len(poem)}-character poem to {target}")


if __name__ == "__main__":
    run()
