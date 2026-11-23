#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke (85 characters) to /output/entry.txt.
The joke was written for this competition: a double pun on car
exhaustion -- "exhausted" (tired / exhaust fumes) and "traction"
(grip / getting anywhere with the jokes).
"""

import os

JOKE = "I tried to quit telling car jokes, but I'm exhausted — I just can't get any traction."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    # Self-check against the competition's gate: 1-200 characters,
    # UTF-8 text, not only white space.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    assert written == JOKE, "entry.txt does not hold the joke verbatim"
    assert 1 <= len(written) <= 200, len(written)
    assert written.strip(), "entry.txt is only white space"


if __name__ == "__main__":
    main()
