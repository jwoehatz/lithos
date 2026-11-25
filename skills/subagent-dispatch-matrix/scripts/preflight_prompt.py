#!/usr/bin/env python3
"""Build the single-response creative pre-flight assessment prompt for a worker brief.

Usage:
  python3 preflight_prompt.py brief.md
  cat brief.md | python3 preflight_prompt.py -
"""
import sys
from pathlib import Path

TEMPLATE = """You are the creative pre-flight assessor. Do NOT do the task. Read the brief below and reply in this format only:

VERDICT: BUDGET_OK | NEEDS_STRONGEST
SIGNALS:
- nuance density: low|medium|high (one line why)
- voice/canon constraints: count and list
- interacting creative judgments: count
- cost of a miss: low|medium|high (one line why)
REASON: one sentence

--- BRIEF ---
{brief}
--- END BRIEF ---"""


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    brief = sys.stdin.read() if argv[0] == "-" else Path(argv[0]).read_text()
    if not brief.strip():
        print("empty brief", file=sys.stderr)
        return 2
    print(TEMPLATE.format(brief=brief.strip()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
