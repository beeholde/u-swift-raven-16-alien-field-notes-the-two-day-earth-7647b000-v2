"""Alien Field Notes, second entry: an alien tourist reviews planet Earth.

One line, 102 characters, a single joke with the punch at the end.
Standard library only, no network, the same bytes on every run.
"""

import os

REVIEW = "The locals throw tomatoes at each other for fun and call it a festival. Four stars; I brought a salad."
# The review: 102 characters, one joke, punch ("I brought a salad") at the end.

LIMIT = 200  # the gate allows 1-200 characters of UTF-8 text


def review_text():
    line = REVIEW
    if not 1 <= len(line) <= LIMIT:
        raise ValueError("review is %d chars; gate is 1-200" % len(line))
    return line


def main():
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(review_text().encode("utf-8"))
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
