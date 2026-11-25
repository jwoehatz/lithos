#!/usr/bin/env python3
"""Pack text files into one or more plain-text bundles (format: references/bundle-format.md).

Each bundle is a .txt file: a manifest at the top listing every file's line range, byte size
and checksum, then each file between `===== FILE: <path> =====` and `===== END FILE: <path> =====`.
Unpacking (read_section.py --unpack) gives back byte-identical files.

Examples (from the code tool, with the sandbox's own Python):
  pack.py notes/ data.csv log.txt --out work/inputs --max-bytes 60000
  pack.py src/ --out bundle --dry-run

Files are taken in the order given; files inside a folder are sorted by path. Binary or
non-UTF-8 files are skipped with a warning. A file bigger than one bundle is split at line
boundaries into numbered parts. Python 3 standard library only; no network.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

VERSION = "v1"
DEFAULT_MAX_BYTES = 60_000
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}
RESERVE = 700  # bytes kept for the bundle's fixed header lines


def collect(args: list[str], root: str, include_hidden: bool) -> list[tuple[str, str]]:
    """(relative path, real path) pairs: args in the order given, folder contents sorted."""
    found: list[tuple[str, str]] = []
    for arg in args:
        if os.path.isdir(arg):
            paths = []
            for dirpath, dirnames, filenames in os.walk(arg):
                dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS
                               and (include_hidden or not d.startswith("."))]
                for name in filenames:
                    if include_hidden or not name.startswith("."):
                        paths.append(os.path.join(dirpath, name))
            found.extend((rel_name(p, root), p) for p in sorted(paths))
        elif os.path.isfile(arg):
            found.append((rel_name(arg, root), arg))
        else:
            sys.exit(f"error: not a file or folder: {arg}")
    seen: dict[str, str] = {}
    for rel, real in found:
        if rel in seen and os.path.realpath(seen[rel]) != os.path.realpath(real):
            sys.exit(f"error: two inputs share the bundle path {rel!r}; pass --root to disambiguate")
        seen[rel] = real
    unique = list(dict.fromkeys(rel for rel, _ in found))
    return [(rel, seen[rel]) for rel in unique]


def rel_name(path: str, root: str) -> str:
    rel = os.path.relpath(os.path.abspath(path), os.path.abspath(root))
    if rel.startswith(".."):
        rel = os.path.basename(path)
    rel = rel.replace(os.sep, "/")
    if "\n" in rel or "\r" in rel:
        sys.exit(f"error: file name contains a line break: {path!r}")
    return rel


def is_text(data: bytes) -> str | None:
    """None when the bytes are UTF-8 text, else the reason they are not."""
    if b"\x00" in data:
        return "contains NUL bytes (binary)"
    try:
        data.decode("utf-8")
    except UnicodeDecodeError as exc:
        return f"not UTF-8 ({exc.reason} at byte {exc.start})"
    return None


def choose_sentinel(contents: list[bytes]) -> str:
    """The shortest run of '=' (5 or more) that no file line starts a marker with."""
    lines = [line.lstrip(b"\xef\xbb\xbf") for data in contents for line in data.split(b"\n")]
    for width in range(5, 41):
        s = b"=" * width + b" "
        markers = (s + b"FILE:", s + b"END FILE:", s + b"BUNDLE", s + b"END MANIFEST")
        if not any(line.startswith(markers) for line in lines):
            return "=" * width
    sys.exit("error: could not find a sentinel that no file line collides with")


def split_parts(data: bytes, limit: int) -> list[bytes]:
    """Split at line ends (or UTF-8 character edges for very long lines) into chunks <= limit."""
    if len(data) <= limit:
        return [data]
    parts, start = [], 0
    while start < len(data):
        end = min(start + limit, len(data))
        if end < len(data):
            cut = data.rfind(b"\n", start, end)
            if cut >= start:
                end = cut + 1
            else:  # one line longer than the limit: cut on a character boundary
                while end > start + 1 and (data[end] & 0xC0) == 0x80:
                    end -= 1
        parts.append(data[start:end])
        start = end
    return parts


def markers(sentinel: str, path: str, part: int, total: int) -> tuple[bytes, bytes]:
    label = path if total == 1 else f"{path} (part {part}/{total})"
    return (f"{sentinel} FILE: {label} {sentinel}\n".encode(),
            f"{sentinel} END FILE: {label} {sentinel}\n".encode())


def block_bytes(content: bytes) -> bytes:
    """Content as written: a newline is added when it does not end with one (bytes says where)."""
    return content if content == b"" or content.endswith(b"\n") else content + b"\n"


def render(blocks: list[dict], sentinel: str, part: int, total: int) -> bytes:
    head = [
        f"{sentinel} BUNDLE {VERSION} {sentinel}",
        "# Plain-text bundle of several files. Do not read it whole: read this manifest, then",
        "# print only the line range you need (sed -n 'START,ENDp' or read_section.py --file).",
        f"# sentinel: {sentinel}   bundle: {part} of {total}   entries: {len(blocks)}",
        "# columns: start-end bytes sha256/16 part path",
    ]
    first = len(head) + len(blocks) + 3  # + END MANIFEST line + blank line, 1-based
    rows, body, line = [], [], first
    for b in blocks:
        text = block_bytes(b["content"])
        start, end = line, line + 1 + text.count(b"\n")
        rows.append(f"# {start}-{end} {len(b['content'])} "
                    f"{hashlib.sha256(b['content']).hexdigest()[:16]} "
                    f"{b['part']}/{b['parts']} {b['path']}")
        open_m, close_m = markers(sentinel, b["path"], b["part"], b["parts"])
        body.append(open_m + text + close_m + b"\n")
        line = end + 2
    out = "\n".join(head + rows + [f"{sentinel} END MANIFEST {sentinel}", "", ""]).encode()
    return out + b"".join(body)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="files and/or folders to pack")
    ap.add_argument("--out", required=True,
                    help="output name without extension; one bundle -> OUT.txt, several -> OUT-1.txt, OUT-2.txt ...")
    ap.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES,
                    help=f"cap per bundle in bytes (default {DEFAULT_MAX_BYTES})")
    ap.add_argument("--max-bundles", type=int, default=0, help="fail if more bundles than this are needed (0 = no cap)")
    ap.add_argument("--root", default=".", help="paths inside the bundle are relative to this folder (default: cwd)")
    ap.add_argument("--include-hidden", action="store_true", help="also pack dot-files and dot-folders")
    ap.add_argument("--dry-run", action="store_true", help="plan and print the summary without writing")
    a = ap.parse_args()
    if a.max_bytes < 2048:
        ap.error("--max-bytes must be at least 2048")

    out_abs = os.path.abspath(a.out)
    files, skipped = [], []
    for rel, real in collect(a.inputs, a.root, a.include_hidden):
        if os.path.abspath(real).startswith(out_abs) and real.endswith(".txt"):
            skipped.append((rel, "looks like this run's own output bundle"))
            continue
        with open(real, "rb") as fh:
            data = fh.read()
        reason = is_text(data)
        if reason:
            skipped.append((rel, reason))
        else:
            files.append((rel, data))
    if not files:
        for rel, why in skipped:
            print(f"warning: skipped {rel}: {why}", file=sys.stderr)
        sys.exit("error: nothing to pack")

    sentinel = choose_sentinel([d for _, d in files])
    budget = a.max_bytes - RESERVE
    items = []
    for rel, data in files:
        overhead = 2 * len(markers(sentinel, rel, 99, 99)[0]) + 60 + len(rel)
        parts = split_parts(data, budget - overhead)
        items += [{"path": rel, "content": p, "part": i + 1, "parts": len(parts), "cost": len(p) + overhead}
                  for i, p in enumerate(parts)]

    bundles, current, used = [], [], 0
    for item in items:
        if current and used + item["cost"] > budget:
            bundles.append(current)
            current, used = [], 0
        current.append(item)
        used += item["cost"]
    bundles.append(current)
    if a.max_bundles and len(bundles) > a.max_bundles:
        sys.exit(f"error: needs {len(bundles)} bundles at --max-bytes {a.max_bytes}, over --max-bundles "
                 f"{a.max_bundles}; drop inputs or raise a limit")

    total = len(bundles)
    names = [f"{a.out}.txt"] if total == 1 else [f"{a.out}-{i}.txt" for i in range(1, total + 1)]
    for i, (name, blocks) in enumerate(zip(names, bundles), 1):
        data = render(blocks, sentinel, i, total)
        if not a.dry_run:
            os.makedirs(os.path.dirname(os.path.abspath(name)), exist_ok=True)
            with open(name, "wb") as fh:
                fh.write(data)
        flag = "  OVER CAP" if len(data) > a.max_bytes else ""
        print(f"{'(dry run) ' if a.dry_run else ''}{name}: {len(data):,} bytes, {len(blocks)} entries{flag}")
        for b in blocks:
            label = b["path"] if b["parts"] == 1 else f"{b['path']} (part {b['part']}/{b['parts']})"
            print(f"  {label}  {len(b['content']):,} bytes")
    for rel, why in skipped:
        print(f"warning: skipped {rel}: {why}", file=sys.stderr)
    if sentinel != "=====":
        print(f"note: a file contains marker-like lines, so this run uses the sentinel {sentinel!r}")
    print(f"packed {len(files)} files into {total} bundle(s); skipped {len(skipped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
