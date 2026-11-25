---
name: one-file-deliverability
description: >-
  Keeps a task that produces a downloadable file from filling the file limit
  with intermediate files, and gets a pile of input files under the
  attachment limit. Plans the deliverable set first, keeps scratch work out of
  the output folder, merges notes, data, charts and drafts into one file with
  subheadings, and packs many text files into a few plain-text bundles. Use
  when someone asks for a report, Word doc, PDF, deck, spreadsheet, dashboard,
  export or "write-up", says "put together" or "build me a" file, hits "too
  many files" or the 20-file limit, or asks to pack, bundle or combine files
  into one. Not for answers given only in chat text.
---
# One-file deliverability

This skill makes a file-producing task leave behind only the files the user needs. Every file saved to the output folder is shown to the user as a deliverable and counts against the file limit. Research notes, drafts, per-source extracts, chart images and logs can use up that limit before the real file exists. Good work here means one clean deliverable (or exactly the set the user asked for), no strays, and a clear statement of what was made.

The same limit hits inputs: a job with 40 source files cannot attach them all. Packing them into a few plain-text bundles, one heading line per file, solves that for one multi-step job. It is not a long-term store.

## Hatz limits that shape this

- Chat attaches at most 20 files per message by default, and one sandbox run keeps at most 20 output files. Both are why the default is one file.
- On a model with tools, attached `.txt`, `.md`, `.json` and `.yaml` files go to the sandbox as `uploads/<name>` and are not pasted into context. Read them by section (see Reading a bundle).
- On a model without tools, attached files are pasted in full, unless any one file is over about 20k tokens; then the whole turn drops to 8 short retrieved snippets. So cap each bundle at about 60 KB and make several bundles rather than one giant file.
- Markdown headings are stripped when `.md` files are extracted, so bundles use plain marker lines and the `.txt` extension. JSON or YAML bundles cost more tokens and are not searchable.

## What you need

- **The deliverable request:** what file or files the user wants and in which format. If the format is not stated, pick the most natural single format (a report becomes one document, tabular data one workbook) and say so. Ask only if the choice changes the work materially.
- **The output folder:** where this task's files are saved for the user. Use the one the task or the sandbox already defines. Do not invent a path.
- **Any template or source file the user supplied:** follow it. Do not copy it into the output folder unless it is the file being edited.
- **`SKILL_DIR`:** the folder the system note names for this skill's bundled files (for example `/skills/one-file-deliverability` or `/workspace/tenant-skills/<id>`). If none is named or it is missing, call read_skill for this skill instead of guessing a path. Run every script from the code tool with the sandbox's own Python: `subprocess.run([sys.executable, f"{SKILL_DIR}/scripts/pack.py", "--help"])`.

## How to do it

0. **Pack inputs when the inputs are the problem.** If there are more source files than the attachment limit, or many text files must pass between steps, pack them into scratch: `subprocess.run([sys.executable, f"{SKILL_DIR}/scripts/pack.py", "notes/", "data/", "--out", "<scratch>/inputs", "--max-bytes", "60000"])`. It writes `inputs.txt`, or `inputs-1.txt`, `inputs-2.txt` and so on when one would be too big, and skips binaries with a warning. Bundles are working material, not deliverables, unless the user asked for the bundle itself. A user with the files on their own computer can run the same script there (Python 3, nothing to install) and attach the bundles. Format details: `references/bundle-format.md`.
1. **Plan the deliverable set before creating anything.** Write one line per file the user will receive. The default is one file. Several files are fine only when the user asked for them or the formats cannot be combined; even then, look for a bundle first (sheets in a workbook, appendices in a document). This plan is the yardstick for the final check.
2. **Take a baseline of the output folder.** Run `scripts/audit_outputs.py` with `--dir <output folder> --baseline-out <scratch>/baseline.json`. The baseline must sit outside the output folder; the script refuses otherwise. It shows which files existed before you started. If a file for this deliverable already exists, plan to overwrite it in place. Renamed copies such as `_v2` or `_final` silently use up the limit. Never delete files you did not create in this task.
3. **Keep working material out of the output folder.** Anything the user won't open belongs in one scratch folder outside the output folder, or in memory inside a single code run. This includes helper scripts, build scripts, bundles and validation output: run them inline and print results instead of saving them.
4. **Merge instead of multiplying.** Before saving any extra file, check `references/merge-map.md`. In short: notes, findings, source lists and decision logs go into one notes file with a heading per topic, or better into an appendix of the deliverable. Per-source data goes into one workbook with a sheet per source, or one JSON with a key per source. Charts and images are embedded in the document, deck or workbook. Drafts are edited in place under one filename. Sections are composed in one build script that writes the file once. Open `references/recipes.md` for code patterns.
5. **Write the deliverable once, then revise in place.** Build the whole file in a single pass where you can. For corrections, change and re-save the same filename.
6. **Run visual or quality checks in scratch.** Page-image previews, rendered thumbnails and converted copies go in the scratch folder and are deleted afterwards. Do not leave a second format of the same content (docx plus pdf plus md) unless the user asked for it.
7. **Treat helpers and subagents the same way.** Ask them to return text, or to append to the single notes file. Do not let each one write its own file.
8. **Audit before you finish.** Run `scripts/audit_outputs.py` with `--dir`, `--baseline` and `--planned` listing the planned file names. It reports planned files missing, new unplanned files, stray-looking names and the count against the limit, and exits 1 until clean. Remove only strays that you created in this task. If a stray holds content that matters, merge it into the deliverable first, then remove it. Clean up the scratch folder too, since saved notes can count against the limit. Run the audit again after cleanup.
9. **Tell the user what they got.** Name the final file or files. Do not claim a file exists, or that cleanup worked, unless the audit output shows it.

## Video and media

- **One sidecar for editing notes.** Cut lists, timecodes and edit notes for a video go in one notes file per deliverable, named after it (`<video-name>.notes.txt` or `.json`) and kept in scratch, not one notes file per clip. Put the notes into the deliverable only if the user asked.
- **Render once.** Cuts, trims, re-encodes and test renders happen in the scratch folder. Write the final video to the output folder once, under one name: no `_cut2` or `_final` renders. The audit flags unplanned `.mp4`, `.mov`, `.wav`, `.srt` and similar files; a planned video is not flagged. Pattern: `references/recipes.md`.

## Reading a bundle

On a model with tools, never read a bundle whole. Its first lines are a manifest: one row per file with its line range, size and checksum. Read only the manifest (`head -n 40`), or list it with `scripts/read_section.py <bundle> --list`, or find the markers with `grep -n '^===== FILE:' <bundle>` (line 1 names the marker; it gets longer, such as `======`, when a file already contains marker-like lines). Then print only what you need: `read_section.py <bundle> --file <name>` for one file's exact text, or `sed -n 'START,ENDp' <bundle>` for a range. To get the files back, `read_section.py <all bundles> --unpack <scratch dir>`; it checks every checksum and refuses to overwrite.

## What to hand back

A short closing note:

- **Delivered:** each file name, with one line on what it contains (for a merged file, its main sections or sheets).
- **Kept out of your files:** one line only if you merged or discarded working material, for example "research notes are in the Appendix". Skip it if nothing applies.
- Anything that could not be merged and why, if an extra file was unavoidable.

## Example

**Request:** "Research three competitors and give me a Word report with a comparison chart and a spreadsheet of the numbers."

**Plan:** `competitor-report.docx` and `competitor-data.xlsx`, since the user asked for both. Notes on each competitor and the source list go in a "Research notes" appendix of the docx. The chart is drawn in memory and embedded in the docx. Each competitor's data goes on its own sheet of the xlsx. No PNG, CSV, markdown notes or draft copies are saved. The final audit shows exactly two files, and the reply names them.

**Request:** "Update the Q3 summary deck with the new numbers."

**Plan:** Open the existing deck, edit it, and save over the same filename. Do not create `deck_v2.pptx`.

**Request:** "Here are 34 ticket exports; summarize the themes in one doc."

**Plan:** Pack the exports into scratch (two bundles at 60 KB), read each by manifest range, and write `ticket-themes.docx` with a per-ticket appendix table. The bundles stay in scratch; the audit shows one file.

## Check before you answer

- The output folder holds only the planned files, and every one is something the user wants to open.
- No renamed duplicates or `final`, `v2` and `copy` variants, and no leftover chart images, test renders, logs, scripts, bundles or per-source extracts.
- No second format of the same content unless it was requested.
- Scratch files are removed, and only files created in this task were deleted.
- The closing note names the real files shown by the audit.

## Files in this skill

| File | When to use it |
|---|---|
| `references/merge-map.md` | Step 4: look up which would-be separate files merge into what. |
| `references/recipes.md` | Steps 4 to 6: code patterns for embedding charts, writing a multi-sheet workbook, keeping one notes file and previewing in scratch. |
| `references/bundle-format.md` | Step 0 and Reading a bundle: the exact bundle layout, sizes and edge cases. |
| `scripts/pack.py` | Step 0: run it, don't read it. Packs files and folders into bundles under `--max-bytes` (default 60000), optional `--max-bundles`, `--dry-run`. |
| `scripts/read_section.py` | Reading a bundle: `--list`, `--file`, `--lines A-B`, `--unpack DIR`, `--verify`. |
| `scripts/audit_outputs.py` | Steps 2 and 8: run it, don't read it. Start with `--help`. It lists the output folder, flags new, unplanned and stray-looking files, and reports missing planned files. It never deletes anything. |
