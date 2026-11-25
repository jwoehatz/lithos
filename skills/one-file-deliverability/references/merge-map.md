# Merge map

Look up a would-be extra file before saving it. Left column: what you were about to save. Right: where it goes instead.

| Would-be file | Where it goes in the single deliverable |
|---|---|
| Research notes, findings, interview notes | "Notes" or "Research notes" appendix, one subheading per topic or source |
| Source list, links, citations | "Sources" section at the end of the document, or a Sources sheet |
| Decision log, assumptions, open questions | Short "Assumptions and open questions" section near the end |
| Per-source extract (one per site, file or ticket) | Appendix subsection per source in a document, or one sheet per source in a workbook |
| Several CSVs or tables | One workbook, one sheet per table, plus a Summary sheet first |
| Raw data behind a chart | A Data sheet in the workbook, or an appendix table in the document |
| Chart or image (PNG, SVG) | Embedded in the document, deck or workbook; drawn in memory, never saved loose |
| Draft, `_v2`, `final`, `copy` | The same filename, edited in place |
| Second format of the same content (md beside docx, pdf beside docx) | Nothing, unless the user asked for that format too |
| Page previews, thumbnails, converted copies for checking | Scratch folder, deleted after the check |
| Helper, build or validation script | Run inline in the code tool; print results |
| Log or validation output | Printed in the code run; a one-line summary in the closing note if it matters |
| Subagent or helper output | Returned as text, or appended to the single notes file |
| Many small input text files | A bundle in scratch (`scripts/pack.py`), read by manifest range |
| Per-step JSON state | One JSON with a key per step, in scratch |

## When an extra file is unavoidable

- The user asked for it by name or format.
- The formats cannot be combined (a workbook the user will filter plus a document they will print).
- The deliverable would exceed a size the user's tools can open.

Say which of these applied in the closing note.
