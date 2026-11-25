"""Alien Field Notes entry v2: write one alien tourist's review of Earth to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes on every run.
The review is a single line, 102 characters, one joke, punchline at the end.
"""

import os
from pathlib import Path

LINE = "The locals throw tomatoes at each other for fun and call it a festival. Four stars; I brought a salad."
# Entry line: 102 characters, one joke, punch ("I brought a salad") at the end.

MAX_CHARS = 200  # gate: entry.txt must hold 1-200 characters of UTF-8 text
# Output is written with write_bytes: no trailing newline, exactly 102 chars.


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars, gate is 1-200"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(text.encode("utf-8"))
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
