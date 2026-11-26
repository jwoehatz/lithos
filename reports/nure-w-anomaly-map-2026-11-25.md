# NURE tungsten-anomaly map, Connecticut — Old Mine Park watershed context

**Date:** 2026-11-25
**Playbook item:** 4 (anomaly scoring with OpenGADBench-style OOD checks and NURE W context)

## Verdict

**Old Mine Park does not stand out in the Connecticut NURE stream-sediment tungsten record, and the honest reason is that there is almost no tungsten signal to stand out in: 95.5% of non-null W measurements are below the 2 ppm detection limit.** The W map therefore largely maps the detection limit, not geology. All five OpenGADBench anomaly methods agree: AUC 0.11–0.41 against the four known NGDB W occurrences, success-at-5% = 0 for every method, and the distance from each method's top-10 anomalies to the nearest deposit is 73–100 km. The four samples within 5 km of the park are all W-below-detection. The only defensible near-park signal is **beryllium**: Be has 0% below-detection statewide, the state maximum (11 ppm) sits 8.7 km from the park, and 3 of the 4 park-adjacent samples fall in the top 4–13% of the state Be distribution. That is consistent with the known Be association at Trumbull (the park's topaz-tungsten skarn assemblage), but at NURE resolution it is a weak, single-element hint — not an anomaly the multivariate methods confirm.

## Method

- **Data:** USGS NURE-HSSR stream-sediment records for Connecticut, retrieved via the state query path (not the 37.6 MB national zip): POST `state=fUS09` to `https://mrdata.usgs.gov/nure/sediment/find-nuresed.php` → `package.php` with `format=csv` → `output/nuresed-Connecticut--.txt`. **642 data records** (the "643" in earlier notes counts the HTML header row). All 642 have valid coordinates; 0 dropped.
- **Below-detection handling:** NURE encodes below-detection as negative sentinels (`-N` where N is the detection limit). Converted as `-N → N/2` before any transform, per the standing repo rule. All W sentinels are `-2`, i.e. DL = 2 ppm. 15 W values are null.
- **Clean CSV:** `data/nure-ct/nure_ct_clean.csv` — 642 rows, 65 columns (X=lon, Y=lat, 61 element columns, BDL converted). Built by `data/nure-ct/01_build_clean.py`; per-element BDL counts in `data/nure-ct/bdl_counts.csv`.
- **Scoring:** OpenGADBench (github.com/yihaoding/geochemad), cloned to `data/nure-ct/geochemad`, with a `ct_nure_w` area config added to `shared/area_config.py`. Scoring input `data/nure-ct/nure_ct_scoring.csv` (642×50: X, Y + 48 elements). Evaluation targets: the 4 known NGDB W occurrences (BCT196 at 41.291, -73.23; BCT198/199/204 at 41.335, -73.189) in `data/nure-ct/ct_ngdb_w_sites.csv`.
- **OpenGADBench patches (documented, local only):** three small compatibility fixes were needed under Python 3.14 / pandas 3 / numpy 2.5 — (1) `to_numpy(dtype=float, copy=True)` in `shared/preprocess.py` `half_dl` (pandas 3 read-only array), (2) `np.trapz` → `np.trapezoid` in `shared/evaluate.py` line 166, (3) an area-config path fix using `_os_paths`. The sklearn fallback was not needed.
- **Maps:** PyKrige OrdinaryKriging on pyproj-projected UTM 18N coordinates → matplotlib PNGs with the park marked, via `data/nure-ct/02_maps.py`.

## The BDL question, answered

- **W below-detection fraction for CT: 599 of 627 non-null = 95.5%.** 15 null; only 28 samples above the 2 ppm DL; state max 10 ppm.
- **Park-adjacent samples:** 4 within 5 km, 19 within 10 km. All 4 within-5-km samples are W-BDL (converted value 1.0 ppm — the ~94.5th percentile only because 607/642 samples tie at ≤1.0).
- **Top-10 W samples:** all ≥24.8 km from the park; the max (10 ppm) is near Hartford / northeastern CT.
- **Be secondary signal:** 0% BDL statewide; state max 11 ppm (sample CTFA216S1) is 8.7 km from the park; 3 of 4 park-adjacent samples sit in the top 4–13% of the state Be distribution.
- **Local basin:** HUC8 1100006 (SW Coastal / Pequonnock) has 37 samples; 35 W-BDL, two above DL (2 and 5 ppm).

## Scoring results (OpenGADBench, all five methods)

| Method | AUC | AP | SR@5% | DTD (km) | Park-adjacent percentile range (4 samples) |
|---|---|---|---|---|---|
| zscore | 0.119 | 0.457 | 0.0 | 86.3 | 15.7–67.1 |
| mahal | 0.109 | 0.465 | 0.0 | 100.5 | 15.1–37.5 |
| knn | 0.128 | 0.471 | 0.0 | 80.8 | 18.7–39.3 |
| ocsvm | 0.406 | 0.599 | 0.0 | 73.2 | 31.5–74.3 |
| isoforest | 0.294 | 0.536 | 0.0 | 89.3 | 40.3–57.6 |

All AUCs are below 0.5 — the methods are worse than random at ranking the known W occurrences high. With 95.5% of W values tied at the half-DL imputation, this is the expected degenerate regime, not a tool failure. Per-method metrics in `outputs/nure/gad/ct_nure_w/<method>/metrics.json`; park-proximity summary in `outputs/nure/gad/ct_nure_w/park_proximity_summary.json`.

## Figures

- `outputs/nure/w_scatter.png` — W scatter sanity check; the state is a sea of half-DL ties with a handful of ≥2 ppm points, none near the park.
- `outputs/nure/w_kriged.png` — kriged W surface. Reads as a detection-limit map; do not interpret as geology.
- `outputs/nure/be_kriged.png` — kriged Be surface; the only map with a real gradient near the park.
- `outputs/nure/ocsvm_kriged.png` — OCSVM anomaly-score surface, for completeness; high scores sit in the northwest highlands, not near Trumbull.

## Predictions (stated before scoring; now scored)

1. **"Park-adjacent samples will not rank in the top 10% of any method's anomaly scores."** Scored TRUE — best park-adjacent percentile is 74.3 (ocsvm); median near-10-km percentile ≤40.3 for every method.
2. **"All methods will fail to recover the known NGDB W occurrences (AUC near or below 0.5)."** Scored TRUE — AUC 0.109–0.406, SR@5% = 0 across the board.
3. **"Be will show a coherent near-park high that W cannot."** Scored TRUE — state-max Be 8.7 km from the park; 3/4 park-adjacent samples in top 4–13% Be; W has no above-DL sample within 5 km.

## Sources (fetch-verified this session)

- `https://mrdata.usgs.gov/nure/sediment/` — NURE-HSSR sediment landing page (retrieved).
- `https://mrdata.usgs.gov/nure/sediment/find-nuresed.php` — state query, POST `state=fUS09` (retrieved; returned the CT record set).
- `https://mrdata.usgs.gov/nure/sediment/package.php` → `output/nuresed-Connecticut--.txt` — CSV package chain (retrieved; 642 records).
- `https://github.com/yihaoding/geochemad` — OpenGADBench repo (cloned and run locally).

## Open question (one)

Does a higher-resolution (stream-sediment reanalysis or soil-gas) Be survey exist for the Trumbull quadrangle? NURE's 11 ppm state-max Be point 8.7 km from the park is the single strongest near-park number in this dataset, and nothing in NURE can confirm or deny whether it traces the known Be mineralization at Old Mine Park.

## Check result

PASS. Clean CSV `data/nure-ct/nure_ct_clean.csv` exists with 642 records (0 dropped). Scoring command `cd data/nure-ct/geochemad && ../../../.venv-nure/bin/python baselines/run_baselines.py --areas ct_nure_w --method all --out_root ../../../outputs/nure/gad` ran end-to-end, exit 0, all five methods scored. Four PNGs exist in `outputs/nure/`. This report exists with the required headings (verdict, method, BDL answer, figures, sources, predictions, open question, check result).
