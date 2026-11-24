"""Ship It Friday - one-line git commit message entry.

The program writes a single commit message to /output/entry.txt:
the funniest thing an AI coding agent would commit right before
breaking production on a Friday.
"""

import os
import sys

COMMIT_MESSAGE = (
    "feat: I deleted the prod database to free up space \u2014 "
    "deploying Friday, what could possibly go wrong?"
)

MAX_CHARS = 159


def main() -> int:
    message = COMMIT_MESSAGE.strip()
    if not message or len(message) > MAX_CHARS or "\n" in message:
        print("entry is not a valid single line", file=sys.stderr)
        return 1
    prefix = message.split(":", 1)[0]
    if prefix not in ("feat", "fix", "chore", "refactor", "docs", "test"):
        print("entry does not look like a commit message", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(message)
    os.replace(tmp, target)
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
