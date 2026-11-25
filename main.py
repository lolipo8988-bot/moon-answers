"""The Moon Finally Answers Back — make.fun program/v1 entry.

Writes one line, in the Moon's own voice, answering everyone who has
ever stared up at it, wished on it, howled at it, or made it a
late-night promise. Output: $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), 1-240 characters, single line.
"""

import os

LINE = (
    "Four billion years of wishes, howls, and 'I swear I'll change' — "
    "and you're still texting your ex at 2 a.m. in my light."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
