#!/usr/bin/env python3
"""One Line, No Deadline Met.

A tiny program that emits a single original one-line joke excusing a
missed deadline and stores it at /output/entry.txt, where the make.fun
grader reads it.
"""

import os

TEXT = "I didn't miss the deadline, I just kept hitting remind me later until it stopped asking."
MAX_CHARS = 200
DESTINATION = os.path.join("/output", "entry.txt")


def entry_text():
    text = TEXT.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must fit on one line")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError("entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    return text


def save(text):
    folder = os.path.dirname(DESTINATION)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text)


def main():
    text = entry_text()
    save(text)
    print("wrote %d characters to %s" % (len(text), DESTINATION))


if __name__ == "__main__":
    main()
