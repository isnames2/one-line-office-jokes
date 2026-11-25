"""One-Line Office Jokes — make.fun entry.

Writes a single line that makes office life funny to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "Our printer only jams when the document is urgent, which is how I know it reads the subject line before I do."
# 109 chars, one line: the turn lands in the last few words — the printer
# reads the subject line before its owner does, so it jams only the urgent ones.


def main() -> None:
    # Gate: 1-199 characters, a single line, not only whitespace.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, must be 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
