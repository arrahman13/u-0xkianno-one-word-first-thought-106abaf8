"""One Word, First Thought — entry program.

Writes exactly one word to the harness output directory as entry.txt.
The gate asks for UTF-8 text of 1 to 24 characters that is not only
white space, so the word is written exactly, with no trailing newline.
"""

import os

WORD = "murmuration"


def main() -> None:
    # The gate in one place: one word, 1 to 24 characters, not blank.
    assert 1 <= len(WORD) <= 24 and WORD.strip(), "word fails the gate"
    assert " " not in WORD, "the entry must be exactly one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(WORD)
    # Read it back so a bad write can never slip through silently:
    # what the judge sees must be the word itself, byte for byte.
    with open(path, encoding="utf-8") as fh:
        assert fh.read() == WORD, "entry.txt does not match the word"


if __name__ == "__main__":
    main()
