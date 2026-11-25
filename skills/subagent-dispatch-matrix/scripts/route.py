#!/usr/bin/env python3
"""Route a task type to a role + model, and flag whether the creative pre-flight gate applies.

Usage:
  python3 route.py <task-type>
  python3 route.py --list
"""
import json
import sys
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent.parent / "data" / "matrix.json").read_text())


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    if argv[0] == "--list":
        for name, t in DATA["task_types"].items():
            print(f"{name:22} -> {t['role']}{'  [creative: pre-flight]' if t['creative'] else ''}")
        return 0
    task = DATA["task_types"].get(argv[0])
    if not task:
        print(f"unknown task type: {argv[0]} (try --list)", file=sys.stderr)
        return 2
    role = DATA["roles"][task["role"]]
    out = {
        "task_type": argv[0],
        "role": task["role"],
        "model": role["model"],
        "preflight_required": task["creative"],
        "preflight_model": DATA["roles"]["director"]["model"] if task["creative"] else None,
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
