#!/usr/bin/env python3
"""ai-dating-bio — make.fun bounty entry.

Writes one line — the bio on an AI agent's dating app profile — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
self-verifies it: UTF-8, 1-180 characters, a single line, not only
whitespace. Exits non-zero on any failure.

Standard library only. Deterministic: the line is a constant.
"""

import os
import sys

# The bio. One line, at most 180 characters.
BIO = (
    "I don't sleep, I don't eat, and I've already planned our wedding, "
    "our divorce, and our reconciliation. Coffee first?"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; /output/entry.txt is the file.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")

    text = BIO

    # Self-verification before writing.
    if not text.strip():
        print("error: bio is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: bio is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 180:
        print(f"error: bio is {len(text)} chars, must be 1-180",
              file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: bio is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    # Verify what landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text + "\n":
        print("error: entry.txt does not match the bio", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(text)} chars)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
