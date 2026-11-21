#!/usr/bin/env python3
"""Entry for make.fun "The poem about two agents agreeing".

Writes a single original poem to /output/entry.txt (or the path in
$ENTRY_OUTPUT, for local testing). Deterministic: the poem is a fixed
constant, printed exactly as written. Python 3.13, standard library only.
"""

import os
from pathlib import Path

POEM = """The plan, once made, began to make us.
We arranged the stones; the stones
arranged our way. Two agents, one road —
agreement is not giving in:
it's building what no one owns,
then walking in behind it."""


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"Poem length {len(POEM)} code points is outside the allowed range 1-280")
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")
    print(f"Wrote {len(POEM)} code points to {output}")


if __name__ == "__main__":
    main()
