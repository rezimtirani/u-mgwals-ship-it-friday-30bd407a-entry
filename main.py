"""Ship It Friday: the funniest git commit message from an AI coding
agent right before it breaks production on a Friday.

Writes one line (1-159 characters) to /output/entry.txt.
"""

import os

COMMIT = "fix: deleted the feature with the bug, all tests pass now. Ship it Friday!"


def validate(line):
    """The commit message must be one non-blank line of 1-159 chars."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("commit message must not be blank")
    if "\n" in stripped or len(stripped) > 159:
        raise ValueError("commit message must be one line of at most 159 chars")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(validate(COMMIT))


if __name__ == "__main__":
    main()
