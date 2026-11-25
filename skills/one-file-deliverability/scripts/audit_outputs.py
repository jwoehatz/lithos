#!/usr/bin/env python3
"""Audit an output folder against a baseline and the planned deliverables. Never deletes anything.

Step 2 (before creating files): snapshot the folder, saving the snapshot OUTSIDE it.
  audit_outputs.py --dir OUTPUT --baseline-out /tmp/scratch/baseline.json

Step 8 (before answering): compare against the snapshot and the plan.
  audit_outputs.py --dir OUTPUT --baseline /tmp/scratch/baseline.json --planned report.docx data.xlsx

The report lists: planned files present and missing; files new since the baseline that were not
planned (strays you probably created); stray-looking names (_v2, final, copy, draft, temp, logs,
loose images and scripts, unplanned video/audio/caption renders such as .mp4 .mov .wav .srt); pre-existing files changed in this task; and the total file count
against --limit. Exit code 0 when clean, 1 when there are strays or missing planned files.
Python 3 stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

STRAY_NAME = re.compile(r"(?i)(_v\d+|[-_ ]final|[-_ ]copy|\(\d+\)|draft|backup|\.bak$|\.tmp$|~$|scratch|temp)")
STRAY_EXT = {".log", ".png", ".jpg", ".jpeg", ".svg", ".py", ".sh", ".ipynb", ".pyc", ".tmp"}
MEDIA_EXT = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".wav", ".mp3", ".m4a", ".aac", ".flac",
             ".srt", ".vtt"}


def snapshot(root: str) -> dict[str, dict]:
    files = {}
    for dirpath, _, names in os.walk(root):
        for name in sorted(names):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            with open(full, "rb") as fh:
                digest = hashlib.sha256(fh.read()).hexdigest()
            files[rel] = {"bytes": os.path.getsize(full), "sha256": digest}
    return files


def inside(path: str, root: str) -> bool:
    path, root = os.path.realpath(path), os.path.realpath(root)
    return path == root or path.startswith(root + os.sep)


def stray_looking(rel: str) -> str | None:
    name = rel.rsplit("/", 1)[-1]
    if STRAY_NAME.search(name):
        return "name looks like a copy, draft or temp file"
    ext = os.path.splitext(name)[1].lower()
    if ext in STRAY_EXT:
        return "working-file type (image, log or script) that is usually embedded or kept in scratch"
    if ext in MEDIA_EXT:
        return "media render, audio or caption file not in the plan; cuts and test renders belong in scratch"
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", required=True, help="the output folder to audit")
    ap.add_argument("--baseline-out", metavar="FILE", help="write a snapshot of --dir to FILE (outside --dir)")
    ap.add_argument("--baseline", metavar="FILE", help="snapshot written earlier with --baseline-out")
    ap.add_argument("--planned", nargs="*", default=None, help="planned deliverable names, relative to --dir")
    ap.add_argument("--limit", type=int, default=20, help="file limit to report against (default 20)")
    ap.add_argument("--json", action="store_true", help="print the report as JSON")
    a = ap.parse_args()

    if not os.path.isdir(a.dir):
        if not a.baseline_out:
            ap.error(f"--dir {a.dir} does not exist")
        os.makedirs(a.dir)  # an empty, new output folder is a valid baseline
    now = snapshot(a.dir)

    if a.baseline_out:
        if inside(a.baseline_out, a.dir):
            ap.error("--baseline-out must be outside --dir, or it becomes a stray itself")
        os.makedirs(os.path.dirname(os.path.abspath(a.baseline_out)), exist_ok=True)
        with open(a.baseline_out, "w", encoding="utf-8") as fh:
            json.dump({"dir": os.path.abspath(a.dir), "files": now}, fh, indent=1, sort_keys=True)
        print(f"baseline: {len(now)} file(s) in {a.dir} saved to {a.baseline_out}")
        for rel in now:
            print(f"  existing: {rel}")
        return 0

    base: dict[str, dict] = {}
    if a.baseline:
        with open(a.baseline, encoding="utf-8") as fh:
            base = json.load(fh)["files"]
    planned = [os.path.normpath(p).replace(os.sep, "/") for p in (a.planned or [])]

    new = [r for r in now if r not in base]
    changed = [r for r in now if r in base and base[r]["sha256"] != now[r]["sha256"]]
    report = {
        "dir": a.dir,
        "total_files": len(now),
        "limit": a.limit,
        "planned_present": [p for p in planned if p in now],
        "planned_missing": [p for p in planned if p not in now],
        "new_unplanned": [r for r in new if r not in planned] if a.planned is not None else [],
        "new_files": new,
        "preexisting_changed": changed,
        "preexisting_removed": [r for r in base if r not in now],
        "stray_looking": {r: why for r in new if (why := stray_looking(r)) and r not in planned},
        "baseline_used": bool(a.baseline),
    }
    clean = not report["planned_missing"] and not report["new_unplanned"] and not report["stray_looking"]
    report["verdict"] = "clean" if clean else "needs attention"

    if a.json:
        print(json.dumps(report, indent=1))
    else:
        print(f"output folder: {a.dir}  ({len(now)} file(s), limit {a.limit})")
        if not a.baseline:
            print("  note: no --baseline given, so every file counts as new")
        for label, key in (("planned, present", "planned_present"), ("PLANNED, MISSING", "planned_missing"),
                           ("NEW, NOT PLANNED (stray if you made it)", "new_unplanned"),
                           ("pre-existing, changed in this task", "preexisting_changed"),
                           ("pre-existing, now gone", "preexisting_removed")):
            for rel in report[key]:
                print(f"  {label}: {rel}")
        for rel, why in report["stray_looking"].items():
            print(f"  STRAY-LOOKING: {rel} ({why})")
        if len(now) > a.limit:
            print(f"  OVER LIMIT: {len(now)} files > {a.limit}")
        print(f"verdict: {report['verdict']}. This script deletes nothing; remove only strays you created.")
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main())
