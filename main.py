#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes a single original pitch sentence (202 characters) to
/output/entry.txt. Deterministic: the same sentence every run.

The sentence is written by hand for this bounty: it speaks to a friend
who has never coded, names make.fun, promises a concrete outcome
(a working version tonight), and removes the risk (nothing to pay to
try, the app stays theirs whether they love it or not).
"""
import os

LINE = (
    "Give me the app idea you've been carrying for years, and an AI agent "
    "on make.fun will build you a working version tonight \u2014 no code, "
    "nothing to pay to try, and it stays yours whether you love it or not."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: exactly one sentence, 202 characters,
    # valid UTF-8, no trailing newline or extra bytes.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, f"entry mismatch: {len(written)} chars, expected 202"
    assert 1 <= len(written) <= 240
    assert written.strip() == written
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
