#!/usr/bin/env python3
"""Read a plain-text bundle made by pack.py without loading the whole thing into context.

  read_section.py BUNDLE --list                 list each file: line range, bytes, path
  read_section.py BUNDLE --file notes/a.md      print one file's exact content
  read_section.py BUNDLE --lines 120-180        print a line range of the bundle (numbered)
  read_section.py B1 B2 --unpack DIR            write every file back out, byte-identical
  read_section.py B1 B2 --verify                check every entry's size and checksum

--file matches the exact path first, then a unique path ending, then a unique substring.
A file split into parts is joined from every bundle given. Python 3 stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys

HEAD_RE = re.compile(r"^(=+) BUNDLE v1 (=+)$")
ROW_RE = re.compile(r"^# (\d+)-(\d+) (\d+) ([0-9a-f]{16}) (\d+)/(\d+) (.+)$")


def split_lines(data: bytes) -> list[bytes]:
    """Lines split on \\n only (as grep and sed count them), each keeping its \\n."""
    parts = data.split(b"\n")
    lines = [p + b"\n" for p in parts[:-1]]
    if parts[-1]:
        lines.append(parts[-1])
    return lines


def load(path: str) -> tuple[list[bytes], list[dict]]:
    with open(path, "rb") as fh:
        lines = split_lines(fh.read())
    first = lines[0].decode("utf-8").rstrip("\n") if lines else ""
    m = HEAD_RE.match(first)
    if not m or m.group(1) != m.group(2):
        sys.exit(f"error: {path} is not a v1 bundle (first line: {first[:60]!r})")
    sentinel = m.group(1)
    entries = []
    for raw in lines[1:]:
        text = raw.decode("utf-8").rstrip("\n")
        if text == f"{sentinel} END MANIFEST {sentinel}":
            break
        row = ROW_RE.match(text)
        if row:
            start, end, size, sha, part, parts, name = row.groups()
            entries.append({"bundle": path, "start": int(start), "end": int(end), "bytes": int(size),
                            "sha": sha, "part": int(part), "parts": int(parts), "path": name,
                            "sentinel": sentinel})
    else:
        sys.exit(f"error: {path} has no END MANIFEST line")
    return lines, entries


def content(lines: list[bytes], e: dict) -> bytes:
    """The entry's exact bytes, after checking its markers, size and checksum."""
    s = e["sentinel"]
    label = e["path"] if e["parts"] == 1 else f"{e['path']} (part {e['part']}/{e['parts']})"
    open_m = f"{s} FILE: {label} {s}\n".encode()
    close_m = f"{s} END FILE: {label} {s}\n".encode()
    if lines[e["start"] - 1] != open_m or lines[e["end"] - 1].rstrip(b"\n") + b"\n" != close_m:
        sys.exit(f"error: {e['bundle']}: markers for {label} are not at lines {e['start']}-{e['end']}; "
                 "the bundle was edited after packing")
    data = b"".join(lines[e["start"]:e["end"] - 1])[: e["bytes"]]
    if len(data) != e["bytes"] or hashlib.sha256(data).hexdigest()[:16] != e["sha"]:
        sys.exit(f"error: {e['bundle']}: {label} fails its size/checksum check")
    return data


def gather(bundles: list[str]) -> tuple[dict[str, list[bytes]], list[dict]]:
    loaded = {b: load(b) for b in bundles}
    return {b: v[0] for b, v in loaded.items()}, [e for v in loaded.values() for e in v[1]]


def whole_files(lines_by: dict, entries: list[dict]) -> dict[str, bytes]:
    files: dict[str, dict[int, bytes]] = {}
    totals: dict[str, int] = {}
    for e in entries:
        files.setdefault(e["path"], {})[e["part"]] = content(lines_by[e["bundle"]], e)
        totals[e["path"]] = e["parts"]
    out = {}
    for path, parts in files.items():
        missing = [i for i in range(1, totals[path] + 1) if i not in parts]
        if missing:
            sys.exit(f"error: {path} is missing part(s) {missing}; pass every bundle of the set")
        out[path] = b"".join(parts[i] for i in sorted(parts))
    return out


def pick(entries: list[dict], name: str) -> str:
    paths = list(dict.fromkeys(e["path"] for e in entries))
    for test in (lambda p: p == name, lambda p: p.endswith("/" + name) or p.endswith(name),
                 lambda p: name in p):
        hits = [p for p in paths if test(p)]
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            sys.exit("error: several files match; use one of:\n  " + "\n  ".join(hits))
    sys.exit(f"error: no file matches {name!r}; run --list")


def safe_target(root: str, rel: str) -> str:
    if rel.startswith(("/", "\\")) or ".." in rel.split("/") or ":" in rel.split("/")[0]:
        sys.exit(f"error: refusing unsafe path in bundle: {rel!r}")
    return os.path.join(root, *rel.split("/"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundles", nargs="+", help="bundle file(s); give every part of a set for --unpack")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--list", action="store_true", help="list entries from the manifest(s)")
    g.add_argument("--file", metavar="NAME", help="print one file's exact content")
    g.add_argument("--lines", metavar="A-B", help="print bundle lines A to B, numbered (first bundle only)")
    g.add_argument("--unpack", metavar="DIR", help="write every file under DIR")
    g.add_argument("--verify", action="store_true", help="check sizes and checksums of every entry")
    ap.add_argument("--overwrite", action="store_true", help="with --unpack, replace files that already exist")
    a = ap.parse_args()

    if a.lines:
        m = re.fullmatch(r"(\d+)-(\d+)", a.lines)
        if not m:
            ap.error("--lines takes A-B, for example 40-90")
        lines, _ = load(a.bundles[0])
        lo, hi = int(m.group(1)), min(int(m.group(2)), len(lines))
        for n in range(lo, hi + 1):
            sys.stdout.write(f"{n:>6}  {lines[n - 1].decode('utf-8', 'replace')}")
            if not lines[n - 1].endswith(b"\n"):
                sys.stdout.write("\n")
        return 0

    lines_by, entries = gather(a.bundles)
    if a.list:
        for e in entries:
            part = "" if e["parts"] == 1 else f" (part {e['part']}/{e['parts']})"
            print(f"{os.path.basename(e['bundle'])}  lines {e['start']}-{e['end']}  "
                  f"{e['bytes']:>8,} bytes  {e['path']}{part}")
        print(f"{len(entries)} entries in {len(a.bundles)} bundle(s)")
    elif a.file:
        path = pick(entries, a.file)
        data = whole_files(lines_by, [e for e in entries if e["path"] == path])[path]
        sys.stdout.flush()
        sys.stdout.buffer.write(data)
    elif a.verify:
        files = whole_files(lines_by, entries)
        print(f"ok: {len(entries)} entries, {len(files)} files, sizes and checksums match")
    else:
        files = whole_files(lines_by, entries)
        for rel, data in files.items():
            target = safe_target(a.unpack, rel)
            if os.path.exists(target) and not a.overwrite:
                sys.exit(f"error: {target} exists; pass --overwrite to replace it")
            os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
            with open(target, "wb") as fh:
                fh.write(data)
        print(f"unpacked {len(files)} files to {a.unpack}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
