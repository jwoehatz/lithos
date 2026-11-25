#!/usr/bin/env python3
"""Check that the named-agent fleet's configured models match data/matrix.json.

Reads the `model:` frontmatter line from each <agents-dir>/<Name>.md (backup files ignored).
Exits 1 on any drift, so it works as a pre-dispatch sanity check.

Usage:
  python3 check_fleet.py [agents-dir]   (default: ~/.config/opencode/agents)
"""
import json
import re
import sys
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent.parent / "data" / "matrix.json").read_text())


def configured_model(path):
    in_fm = False
    for i, line in enumerate(path.read_text().splitlines()):
        if line.strip() == "---":
            if in_fm:
                return None
            in_fm = i == 0
            continue
        m = re.match(r"^model:\s*(\S+)", line)
        if in_fm and m:
            return m.group(1)
    return None


def main(argv):
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    agents = Path(argv[0] if argv else "~/.config/opencode/agents").expanduser()
    if not agents.is_dir():
        print(f"agents dir not found: {agents}", file=sys.stderr)
        return 2
    drift = 0
    for name, expected in sorted(DATA["fleet"].items()):
        f = agents / f"{name}.md"
        if not f.exists():
            print(f"MISSING  {name}")
            drift += 1
            continue
        actual = configured_model(f)
        ok = actual == expected
        drift += not ok
        print(f"{'OK     ' if ok else 'DRIFT  '}  {name:15} {actual}{'' if ok else f'  (matrix: {expected})'}")
    known = set(DATA["fleet"])
    for f in sorted(agents.glob("*.md")):
        if f.stem not in known:
            print(f"UNLISTED {f.stem:15} {configured_model(f)}")
    print("FLEET OK" if not drift else f"FLEET DRIFT: {drift}")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
