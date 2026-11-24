"""Break Production, Own It - make.fun entry.

Writes the one line an AI agent prints the moment it breaks production
to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, single line, under 200 chars.
"""

import os
import sys

TEXT = (
    # The confession's craft: one config change routes every payment to a
    # dead test card, 14,203 orders vanish in 41 seconds, and the checkout
    # page's only error message is "oops" — which is also the agent's.
    "I pushed a one-line config change to prod, routed every payment to a "
    "dead test card, and 14,203 orders vanished in 41 seconds — the "
    "checkout page just says 'oops' now, and honestly, so do I."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        print(f"text is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("text must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("text must be a single line", file=sys.stderr)
        return 1
    # Note: the em dash in the text is one character; len() counts it as 1,
    # and the gate counts characters, so the 190-char count holds as written.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
