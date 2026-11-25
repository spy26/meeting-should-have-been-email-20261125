"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one line of plain text (max 200 chars), a single joke about a meeting
that should have been an email, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is a constant: no input, no network,
no randomness, so every run produces byte-identical output.
"""

import os

LINE = "We spent an hour in a meeting about the email nobody read, to write a second email nobody will read."


def main() -> None:
    # Gate the artifact ourselves before writing: one line, 1-200 chars.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE, "entry line violates the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file must be exactly one line, 1-200 chars.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
