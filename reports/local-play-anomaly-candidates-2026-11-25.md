# Anomaly-detection & mapping cluster — candidate verdicts for the Old Mine Park local play

Worker: glm-literature@1 (zai, literature-first lens) · Task: local-play-candidates · 2026-11-25
Question: for watershed-scale W-anomaly mapping from NURE-HSSR stream-sediment data around Trumbull CT (playbook item 4), which of these tools actually runs today and fits that data?

## Verdict table

| Candidate | Verdict | One-line reason | Source (fetch-verified) |
|---|---|---|---|
| OpenGADBench (yihaoding/geochemad) | **CANDIDATE — best pick** | Consumes exactly NURE's shape (CSV: X, Y + element columns), unsupervised baselines need no labels, W is a benchmarked commodity, MIT, CPU-only supported | github.com/yihaoding/geochemad + raw shared/preprocess.py, shared/area_config.py |
| PyKrige (GeoStat-Framework) | **CANDIDATE — runner-up / mapping layer** | Trivially consumes NURE points (x, y, value arrays), pip-installable, BSD-3, 868 stars — but interpolates, does not detect | github.com/GeoStat-Framework/PyKrige |
| Geo-Hgan (cbn001012) | **NOT a candidate** | Input contract is raster, not points: `train_LSLM.py` loads 39-channel 64×64 TIF images via `loadTifImage.DatasetFolder`; NURE's 643 irregular CT points would be ~90% interpolation, plus hardcoded `/mnt/3.6T-DATA/` paths | raw train_LSLM.py + repo README |
| Causal-VAE / ICVAE (kiritonfan) | **NOT a candidate** | Semi-supervised causal VAE needs an ore-controlling-factor DAG + conditioning labels that do not exist for CT; research-grade single-purpose code (2 stars, 0 forks) | github.com/kiritonfan/An-interpretable-causal-variational-autoencoder |
| DAN-GRF (Saeid1986) | **NOT a candidate** | Input format would fit (coords + element matrix) but the script is unlicensed (no LICENSE file in tree), single-commit, with hardcoded `C:/Users/ASUS/` paths, hardcoded `Au ~` formula and bandwidth 23 | raw DAN-GRF.R + repo file tree |
| DEEP-SEAM (EarthByte/MPM_Curnamona_REE) | **NOT a candidate** | Prospectivity framework: needs gridded evidence layers + multiple labeled known deposits (DevNet semi-supervised); Trumbull has one known locality — cannot train | github.com/EarthByte/MPM_Curnamona_REE |

## Input formats

Verified from repo code/docs, not abstracts:

- **OpenGADBench** — `load_area()` in `shared/preprocess.py` reads a CSV, requires `X`/`Y` columns (drops rows with NaN coords), auto-detects element columns as all numeric non-excluded columns (excludes X, Y, SAMPLEID, Longitude, Latitude, ...), or takes an explicit `input_elements` list from `shared/area_config.py`. Coordinates required: yes. Labels: **no** for the classic baselines (z-score, Mahalanobis, kNN, OCSVM, IsolationForest); deposit site CSVs are used only for evaluation. Built-in `half_dl()` replaces ≤0/NaN with half the column's minimum positive value; CLR/ILR transforms built in. Output: `anomaly_scores.csv` (x, y, anomaly_score).
- **PyKrige** — `OrdinaryKriging(x, y, z)` takes coordinate arrays + one value array. Coordinates required: yes. Labels: no. Output: gridded values + kriging variance via `execute()`. numpy/scipy only.
- **Geo-Hgan** — `train_LSLM.py`: `img_size=64, channels=39`, data loaded by `loadTifImage.DatasetFolder` — multi-channel TIF rasters, one channel per element. Coordinates: implicit in the raster grid. Labels: none (unsupervised), but a "normal class" training split is assumed.
- **Causal-VAE** — element vector per sample (39-dim in the paper → 117-dim latent), DAG/SCM constraints over elements plus conditional (ore-controlling factor) inputs; PyTorch 2.4.1, Python 3.9.
- **DAN-GRF** — `read.table` of a whitespace-delimited text file: columns 1–2 = X,Y coordinates, remaining columns = elements **including a target variable** (script hardcodes `Au ~`); R 4.1.2+, h2o + SpatialML + compositions.
- **DEEP-SEAM** — `Input_Data_Layers/` gridded raster evidence layers + labeled positive samples for DevNet semi-supervised training; one Jupyter notebook + one R preprocessing script (ILR + robust PCA).

## NURE fit

NURE-HSSR sediment data shape (verified from mrdata.usgs.gov/nure/sediment/ + metadata): 397,625 records national (643 in CT per prior verified run), lat/lon in decimal degrees (NAD27/Clarke 1866), ~40 element columns (`w_ppm`, `th_ppm`, `u_dn_ppm`, `au_ppm`, ...). **Below-detection encoding: negative numbers where |value| = detection limit** — "A value of -2 in the AG_PPM field is equivalent to <2 ppm Ag" (nurehssr.faq.html). Zero coordinates were converted to null in the 2009 USGS update.

- **OpenGADBench — fits.** Point samples with coords + elements is exactly its contract; its own benchmark includes stream-sediment tasks (sed1–4) and a W target (rock1, W rock-chip, attention AUC 0.929 ± 0.026). The sediment+W combination is not a bundled task but is one `area_config.py` entry away; the Canada sediment areas (92 columns, custom names via explicit `input_elements`) are precedent for non-WA column naming. 643 samples is within its benchmark range (rock2 has 224).
- **PyKrige — fits.** (x=lon, y=lat, z=w_ppm) directly; project coords first.
- **Geo-Hgan — does not fit.** Would require interpolating 643 points onto a 39-channel 64×64 grid per element first — the raster would be mostly interpolation, and the anomaly signal would be an artifact of the gridding.
- **Causal-VAE — format fits, labels don't.** Element vectors are fine; the causal/conditional structure (ore-controlling factors) has no CT analogue.
- **DAN-GRF — format fits, code doesn't.** Coords + elements + target (w_ppm) matches, but the script as committed runs only on the authors' machine.
- **DEEP-SEAM — does not fit.** Needs gridded evidence layers and multiple labeled deposits; one known skarn locality cannot train a DevNet.

**Below-detection handling (all tools):** convert NURE negatives by half-DL substitution *before* any transform: `-N → N/2` (e.g., -2 → 1 ppm). Never leave negative sentinels in — they corrupt variograms (PyKrige) and CLR/ILR require strictly positive values (OpenGADBench, DAN-GRF). OpenGADBench's `half_dl()` would catch ≤0 values anyway, but pre-converting preserves the per-sample detection-limit information the negative encoding carries.

## Best pick + sketch

**Best pick: OpenGADBench classic baselines.** Reason: the only tool in the cluster whose input contract matches NURE point data exactly, whose scoring needs no labels (critical — Trumbull has one known deposit, which is a test point, not a training set), whose target commodity W is already benchmarked, which runs on CPU, and which is MIT-licensed with below-detection handling built in.
**Runner-up: PyKrige** — not an anomaly detector, but the cleanest way to turn per-sample scores into the actual watershed-scale map; it is also what OpenGADBench itself uses for interpolation in its own preprocessing.

Five-step sketch:
1. **Build the CT CSV.** Pull the 643 CT records from mrdata.usgs.gov/nure/sediment/ (state=fUS09). Columns: `X`=longitude, `Y`=latitude, plus the ~40 element columns. Convert below-detection: `-N → N/2`. Drop null-coordinate records.
2. **Register the area.** Clone geochemad, `pip install -r requirements.txt`. Add one dict to `shared/area_config.py` AREAS: `area_id="ct_nure_sed_w"`, `csv_path` → your CSV, `target_element="w_ppm"`, `input_elements` → explicit element-column list (avoids auto-detect sweeping up `rec_no`, `b_lat_c`, etc.), `data_type="sediment"`.
3. **Run the unsupervised baselines on CPU.** `cd baselines && python run_baselines.py --method all --out_root ../outputs/ct` — z-score, Mahalanobis, kNN, OCSVM, IsolationForest, no labels needed.
4. **Read `anomaly_scores.csv`** (x, y, anomaly_score per sample). Sanity check: do samples in the Old Mine Park drainage basin rank high? That is the one ground truth available.
5. **Make the map.** Grid the best method's per-sample scores with PyKrige `OrdinaryKriging` on projected coordinates → watershed-scale W-anomaly map. Cross-check highs against the Pinewood Adamellite belt and the 1970s USGS NGDB W anomalies (BCT196/198/199/204).

## Sources (fetch-verified URLs)

All fetched this session:
1. https://github.com/yihaoding/geochemad (README: 10 tasks, baselines, licenses, CPU support)
2. https://raw.githubusercontent.com/yihaoding/geochemad/main/shared/preprocess.py (input contract, half_dl, CLR/ILR)
3. https://raw.githubusercontent.com/yihaoding/geochemad/main/shared/area_config.py (16 area configs, W task, custom-area mechanism)
4. https://github.com/GeoStat-Framework/PyKrige (BSD-3, 868 stars, API, pip install)
5. https://github.com/cbn001012/Geo-Hgan-Unsupervised-anomaly-detection-in-geochemical-data-via-latent-space-learning (Apache-2.0, 9 stars, TIF loader)
6. https://raw.githubusercontent.com/cbn001012/Geo-Hgan-Unsupervised-anomaly-detection-in-geochemical-data-via-latent-space-learning/main/train_LSLM.py (raster input contract, hardcoded paths)
7. https://github.com/kiritonfan/An-interpretable-causal-variational-autoencoder (MIT, 2 stars, DAG/conditional structure)
8. https://github.com/Saeid1986/DAN-GRF (1 commit, 1 star, no LICENSE in tree)
9. https://raw.githubusercontent.com/Saeid1986/DAN-GRF/main/DAN-GRF.R (input format, hardcoded paths/formula/bandwidth)
10. https://github.com/EarthByte/MPM_Curnamona_REE (GPL-3.0, evidence layers, DevNet semi-supervised)
11. https://mrdata.usgs.gov/nure/sediment/ (397,625 records, CSV downloads, WMS/WFS)
12. https://mrdata.usgs.gov/nure/sediment/about.php (full field list incl. w_ppm)
13. https://mrdata.usgs.gov/nure/sediment/describe.php?fieldname=w_ppm (W field definition)
14. https://mrdata.usgs.gov/metadata/nurehssr.faq.html (below-detection negative encoding; NAD27; null coordinates)

## Predictions

1. OpenGADBench's `run_baselines.py` will execute on a 643-sample CT NURE CSV on CPU with no code change beyond an `area_config.py` entry (its rock2 benchmark area has only 224 samples, so 643 is in range).
2. Geo-Hgan is blocked by data format: it cannot consume NURE point samples without a rasterization step that would be ~90% interpolation at CT sampling density.
3. DAN-GRF will not run outside the authors' machine without edits (hardcoded `C:/Users/ASUS/` paths, hardcoded `Au ~` formula, bandwidth fixed at 23), and the repo carries no license file.

## Check result

**PASS.** 14 distinct fetch-verified URLs (≥5 required). All 6 candidates have explicit verdict lines with a fetch-verified source. websearch was not used (dead in this environment, per binding note).

## Open question

What fraction of the 643 CT records have W below detection (negative-encoded), and does the Old Mine Park drainage basin itself contain a NURE sample? If most W values are BDL, the W-anomaly map degenerates into a detection-limit artifact map — check before interpreting.
