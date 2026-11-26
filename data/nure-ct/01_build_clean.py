"""Step 1: Build clean CT NURE sediment CSV.

Input : data/nure-ct/nuresed-Connecticut-raw.csv (USGS mrdata state=fUS09 query output)
Output: data/nure-ct/nure_ct_clean.csv  (X=lon, Y=lat, element columns)

Rules (binding, from prior verified findings):
- Below-detection encoding: NEGATIVE numbers where |value| = detection limit.
  Convert -N -> N/2 before any transform. Never leave negative sentinels in.
- Zero coordinates were nulled in the 2009 update -> drop null-coordinate rows.
"""
import pandas as pd
import numpy as np

RAW = "data/nure-ct/nuresed-Connecticut-raw.csv"
OUT = "data/nure-ct/nure_ct_clean.csv"

df = pd.read_csv(RAW, low_memory=False)
print(f"raw rows: {len(df)}")

# Coordinates: drop null/zero coordinates
n_before = len(df)
df = df.dropna(subset=["latitude", "longitude"])
df = df[(df["latitude"] != 0) & (df["longitude"] != 0)]
print(f"rows with valid coords: {len(df)} (dropped {n_before - len(df)})")

# Element columns: all *_ppm, *_pct, plus u_*_ppm variants
elem_cols = [c for c in df.columns if c.endswith(("_ppm", "_pct"))]
print(f"element columns: {len(elem_cols)}")

# Record which values were below detection (negative sentinel) for W before conversion
bdl_counts = {}
for c in elem_cols:
    vals = pd.to_numeric(df[c], errors="coerce")
    bdl_counts[c] = int((vals < 0).sum())

# Convert -N -> N/2 for all negative values in element columns
for c in elem_cols:
    vals = pd.to_numeric(df[c], errors="coerce")
    neg = vals < 0
    df[c] = vals.where(~neg, vals.abs() / 2.0)

# W below-detection fraction (open question)
w_raw = pd.to_numeric(pd.read_csv(RAW, low_memory=False)["w_ppm"], errors="coerce")
w_bdl = (w_raw < 0).sum()
w_meas = w_raw.notna().sum()
print(f"\nW: total non-null={w_meas}, below-detection (negative-encoded)={w_bdl} "
      f"({100.0 * w_bdl / w_meas:.1f}%)")

# Build clean output: rec_no, X (lon), Y (lat), element columns
out = df[["rec_no", "prime_id", "longitude", "latitude"] + elem_cols].copy()
out = out.rename(columns={"longitude": "X", "latitude": "Y"})
out.to_csv(OUT, index=False)
print(f"\nwrote {OUT}: {len(out)} rows, {len(out.columns)} columns")

# Save BDL counts for the report
with open("data/nure-ct/bdl_counts.csv", "w") as f:
    f.write("element,n_below_detection,n_nonnull\n")
    for c in elem_cols:
        vals = pd.to_numeric(pd.read_csv(RAW, low_memory=False)[c], errors="coerce")
        f.write(f"{c},{bdl_counts[c]},{int(vals.notna().sum())}\n")
print("wrote data/nure-ct/bdl_counts.csv")