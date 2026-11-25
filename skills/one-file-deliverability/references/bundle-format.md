# Bundle format v1

A bundle is one UTF-8 plain-text `.txt` file holding several text files, made by `scripts/pack.py` and read by `scripts/read_section.py`. Use it for one multi-step job where the file count is the limit. It is not a long-term store: once the job is done, unpack it or drop it.

## Layout

```text
===== BUNDLE v1 =====
# Plain-text bundle of several files. Do not read it whole: read this manifest, then
# print only the line range you need (sed -n 'START,ENDp' or read_section.py --file).
# sentinel: =====   bundle: 1 of 2   entries: 3
# columns: start-end bytes sha256/16 part path
# 10-14 312 9f1c0a7e55b2d4c1 1/1 notes/meeting.md
# 16-200 10025 4c6fb27042d765d8 1/1 data/sales.csv
# 202-260 2480 0b9e3d17aa40c2f8 1/2 logs/app.log
===== END MANIFEST =====

===== FILE: notes/meeting.md =====
...exact file text...
===== END FILE: notes/meeting.md =====

===== FILE: logs/app.log (part 1/2) =====
...
===== END FILE: logs/app.log (part 1/2) =====
```

- **Manifest rows:** `start-end` are the 1-based bundle line numbers of the FILE and END FILE marker lines, so `sed -n 'START,ENDp'` prints the block. `bytes` is the exact size of the content, `sha256/16` the first 16 hex digits of its SHA-256, `part` is `k/n`, and the path comes last (it may contain spaces).
- **Blocks:** the content sits between the two marker lines exactly as stored. When the file does not end with a newline, one is added so the END marker starts its own line; `bytes` says where the real content stops. Line endings (`\n`, `\r\n`) and a leading BOM are kept byte for byte. One blank line follows each block.
- **Paths:** relative, `/`-separated, taken from `--root` (default: the current folder). Unpacking refuses absolute paths and `..`.

## Rules the scripts enforce

| Case | What happens |
|---|---|
| A file line starts with a marker (`===== FILE:`, `===== END FILE:`, `===== BUNDLE`, `===== END MANIFEST`) | pack lengthens the sentinel (`======`, `=======` ...) until no line collides, for the whole run, and prints a note. Line 1 always shows the sentinel in use. |
| Binary (NUL bytes) or not valid UTF-8 | Skipped with a warning naming the file and reason. Convert it first, or deliver it separately. |
| A file bigger than one bundle | Split at line ends into `part k/n` blocks, across bundles if needed. `--file` and `--unpack` join the parts; a missing part is an error. |
| More bundles than `--max-bundles` | pack fails without writing anything. |
| Dot-files, `.git`, `__pycache__`, `node_modules` | Skipped unless `--include-hidden` (which still skips those folders). |
| A bundle edited after packing | `--verify`, `--file` and `--unpack` fail: markers moved or a checksum no longer matches. |

Round trip: `read_section.py <all bundles> --unpack DIR` writes every file byte-identical to the original.

## Sizes

- Default `--max-bytes` is 60000 (about 15k tokens of English). On models without tools an attachment over about 20k tokens makes the whole turn fall back to 8 short retrieved snippets, so keep under it.
- Keep the attachment count in mind: chat accepts 20 files per message by default.
- Order is deterministic: inputs in the order given, files inside a folder sorted by path, bundles filled in that order.

## Why plain text and markers

- `.md` files lose their headings when Hatz extracts text, so `#` headings cannot separate files; marker lines survive.
- `.txt` keeps search working on models with tools; JSON or YAML wrappers cost more tokens (about 3% and 8% more in a test) and are not indexed for search.
- Markers are grep-able: `grep -n '^===== FILE:' bundle.txt` lists every block with its line number.
