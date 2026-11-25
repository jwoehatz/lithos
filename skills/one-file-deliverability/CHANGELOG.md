# Changelog

## v2 (2026-11-20)

- Added the three files v1 pointed to but did not ship: `scripts/audit_outputs.py`, `references/merge-map.md`, `references/recipes.md`. Hatz's upload lint flagged them as missing in v1.
- New inputs side of the same problem: step 0 "Pack inputs", `scripts/pack.py` and `scripts/read_section.py`, and a defined plain-text bundle format (`references/bundle-format.md`): manifest with line ranges and checksums, `===== FILE: path =====` markers, byte-identical round trip, collision-safe markers, binaries skipped with a warning, files over the cap split into parts.
- New "Reading a bundle" section: read the manifest, then print only the needed line range; never read a bundle whole on a model with tools.
- New "Hatz limits that shape this" section: 20 attachments per message, 20 kept sandbox outputs, how attached text reaches tool and no-tool models, the 60 KB per-bundle cap, and why bundles are `.txt` with plain markers.
- Description now also triggers on "too many files", the 20-file limit, and pack, bundle or combine requests (644 characters, inside Hatz's 1,024 limit).
- Script paths use the skill folder the system note names (`SKILL_DIR`) instead of a fixed `skills/<name>/...` path, which may not match where an uploaded skill is mounted.
- Added `evals/evals.json` (three test prompts) so the upload lint is clean. Steps 1 to 9, the closing note, examples and checks keep v1's wording, with small additions (bundle mentions, audit flags, a third example).
- Video and media (approved by Jesse, items 1, 2 and 4 of media-proposals.md): new short "Video and media" section. Edit notes for a video go in one sidecar notes file per deliverable in scratch, not one per clip. Cuts, trims, re-encodes and test renders stay in scratch, and the final video is written once under one name. `audit_outputs.py` now flags unplanned video, audio and caption files (.mp4, .mov, .m4v, .mkv, .webm, .avi, .wav, .mp3, .m4a, .aac, .flac, .srt, .vtt); a planned video is never flagged. Recipe in `references/recipes.md`.
- Renamed from `one-file-deliverables` to `one-file-deliverability` (frontmatter name, title, folder and zip).
