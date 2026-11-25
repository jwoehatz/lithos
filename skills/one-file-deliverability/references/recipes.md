# Recipes

Patterns for steps 4 to 6. Each builds the deliverable in one code run and saves nothing else to the output folder. `OUT` is the output folder, `SCRATCH` a folder outside it.

## Notes and data into one document with an appendix

```python
from docx import Document
doc = Document()
doc.add_heading("Competitor report", 0)
for section, text in body_sections:          # main content, composed in memory
    doc.add_heading(section, 1); doc.add_paragraph(text)
doc.add_page_break(); doc.add_heading("Appendix: Research notes", 1)
for source, notes in research_notes.items():  # was one notes file per source
    doc.add_heading(source, 2); doc.add_paragraph(notes)
doc.add_heading("Sources", 1)
for url in sources: doc.add_paragraph(url, style="List Bullet")
doc.save(f"{OUT}/competitor-report.docx")    # the only file written
```

## A chart embedded, never saved loose

```python
import io, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from docx.shared import Inches
fig, ax = plt.subplots(figsize=(6, 3)); ax.bar(names, values)
buf = io.BytesIO(); fig.savefig(buf, format="png", dpi=150, bbox_inches="tight"); plt.close(fig)
buf.seek(0); doc.add_picture(buf, width=Inches(6))   # docx; for pptx: slide.shapes.add_picture(buf, ...)
```

For a workbook, prefer a native chart (`openpyxl.chart.BarChart`) on the data sheet; for an image use `openpyxl.drawing.image.Image(buf)`.

## Several tables into one workbook

```python
import pandas as pd
with pd.ExcelWriter(f"{OUT}/competitor-data.xlsx") as xw:
    summary.to_excel(xw, sheet_name="Summary", index=False)
    for name, df in per_source.items():          # was one CSV per source
        df.to_excel(xw, sheet_name=name[:31], index=False)   # sheet names max 31 chars
```

## One notes file, appended by every step or helper

```python
NOTES = f"{SCRATCH}/notes.txt"
def note(topic, text):
    with open(NOTES, "a", encoding="utf-8") as fh:
        fh.write(f"\n===== {topic} =====\n{text.rstrip()}\n")
```

Helpers return text; the caller calls `note()`. At the end the notes go into the appendix, and the scratch file is deleted.

## Drafts revised in place

```python
doc = Document(f"{OUT}/report.docx")          # open the existing file
# ... edit paragraphs or tables ...
doc.save(f"{OUT}/report.docx")                # same name: no _v2, no _final
```

## Previews and checks in scratch

```python
import subprocess, tempfile, shutil
tmp = tempfile.mkdtemp(dir=SCRATCH)
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, f"{OUT}/report.docx"], check=True)
# render pages from tmp, look, fix the source, re-save the same file
shutil.rmtree(tmp)
```

## Video: one sidecar, render once

```python
import json, shutil, subprocess
SIDE = f"{SCRATCH}/{video_name}.notes.json"           # one sidecar per deliverable, not per clip
notes = {"source": src, "cuts": [{"in": "00:01:05", "out": "00:02:10", "why": "intro"}]}
json.dump(notes, open(SIDE, "w"), indent=1)
work = f"{SCRATCH}/{video_name}.work.mp4"             # cuts, trims, test renders stay here
subprocess.run(["ffmpeg", "-y", "-i", src, "-ss", "00:01:05", "-to", "00:02:10", "-c", "copy", work], check=True)
shutil.copyfile(work, f"{OUT}/{video_name}.mp4")      # final written once, one name
```

## Many inputs, one job

Pack into scratch with `scripts/pack.py`, read by manifest range with `scripts/read_section.py`, and delete the bundles at the end. See `references/bundle-format.md`.
