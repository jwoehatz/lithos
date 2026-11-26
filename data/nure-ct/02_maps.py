"""Step 4: Maps for the NURE CT W-anomaly run.

Produces (outputs/nure/):
  w_scatter.png      - sanity-check scatter of W (BDL vs above-DL) with park marked
  w_kriged.png       - PyKrige ordinary kriging of W (converted -N -> N/2) + variance panel
  be_kriged.png      - Be kriged map (secondary signal: state-max Be is 8.7 km from park)
  ocsvm_kriged.png   - best anomaly-score kriged map (ocsvm; scoring degenerate, shown for completeness)

Coordinates projected with pyproj UTM zone 18N (EPSG:26918, NAD83 approx for NAD27 data at this scale).
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pyproj import Transformer
from pykrige.ok import OrdinaryKriging

PARK = (41.31, -73.19)
PARK_LABEL = "Old Mine Park"

tf = Transformer.from_crs("EPSG:4326", "EPSG:26918", always_xy=True)

def to_utm(lon, lat):
    return tf.transform(lon, lat)

def park_km(ax):
    px, py = to_utm(PARK[1], PARK[0])
    ax.plot(px / 1000, py / 1000, "k*", markersize=16, markeredgecolor="white", zorder=10)
    ax.annotate(PARK_LABEL, (px / 1000, py / 1000), textcoords="offset points",
                xytext=(8, 8), fontsize=9, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.8, ec="k", lw=0.5))

def krige_map(df, val_col, title, out_png, score_desc=None):
    x, y = to_utm(df["X"].values, df["Y"].values)
    x, y = x / 1000.0, y / 1000.0  # km
    v = df[val_col].values.astype(float)
    ok = OrdinaryKriging(x, y, v, variogram_model="spherical", coordinates_type="euclidean",
                         nlags=12, enable_plotting=False)
    gridx = np.arange(x.min() - 10, x.max() + 10, 1.0)
    gridy = np.arange(y.min() - 10, y.max() + 10, 1.0)
    z, ss = ok.execute("grid", gridx, gridy)

    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    for ax, field, cmap, lab in [
        (axes[0], z, "viridis", score_desc or val_col),
        (axes[1], np.sqrt(ss), "magma", "kriging std dev"),
    ]:
        pcm = ax.pcolormesh(gridx, gridy, field, cmap=cmap, shading="auto")
        ax.scatter(x, y, c="k", s=4, alpha=0.35, zorder=5)
        park_km(ax)
        fig.colorbar(pcm, ax=ax, label=lab, shrink=0.85)
        ax.set_xlabel("Easting (km, UTM 18N)")
        ax.set_ylabel("Northing (km, UTM 18N)")
    axes[0].set_title(f"{title}\n(ordinary kriging, spherical variogram)")
    axes[1].set_title("Kriging uncertainty (std dev)")
    fig.tight_layout()
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print(f"wrote {out_png}")

# ── Load data ────────────────────────────────────────────────────────────────
clean = pd.read_csv("data/nure-ct/nure_ct_clean.csv", low_memory=False)
raw = pd.read_csv("data/nure-ct/nuresed-Connecticut-raw.csv", low_memory=False)
raw["w_raw"] = pd.to_numeric(raw["w_ppm"], errors="coerce")

# ── Figure 1: W scatter sanity check ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 9))
bdl = raw["w_raw"] < 0
above = raw["w_raw"] > 0
ax.scatter(raw.loc[bdl, "longitude"], raw.loc[bdl, "latitude"], c="lightgray",
           s=18, label=f"below detection (<2 ppm), n={bdl.sum()}", edgecolor="k", lw=0.2)
sc = ax.scatter(raw.loc[above, "longitude"], raw.loc[above, "latitude"],
                c=raw.loc[above, "w_raw"], cmap="YlOrRd", s=70, vmin=0, vmax=10,
                edgecolor="k", lw=0.4, label=f"above detection, n={above.sum()}")
ax.plot(*reversed(PARK), "k*", markersize=18, markeredgecolor="white", zorder=10)
ax.annotate(PARK_LABEL, reversed(PARK), textcoords="offset points", xytext=(8, 8),
            fontsize=10, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.8, ec="k", lw=0.5))
plt.colorbar(sc, ax=ax, label="W (ppm)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("NURE-HSSR stream sediment W, Connecticut (n=642)\n"
             "95.5% of samples below the 2 ppm detection limit")
ax.legend(loc="lower left")
fig.tight_layout()
fig.savefig("outputs/nure/w_scatter.png", dpi=150)
plt.close(fig)
print("wrote outputs/nure/w_scatter.png")

# ── Figure 2: W kriged (scoring degenerated -> krige W itself per brief) ──────
w_df = clean[["X", "Y", "w_ppm"]].dropna()
krige_map(w_df, "w_ppm",
          "NURE stream-sediment W (ppm), kriged\n"
          "WARNING: 95.5% of values are the half-DL fill (1.0 ppm) — this surface largely maps the detection limit",
          "outputs/nure/w_kriged.png")

# ── Figure 3: Be kriged (secondary signal) ───────────────────────────────────
be_df = clean[["X", "Y", "be_ppm"]].dropna()
krige_map(be_df, "be_ppm",
          "NURE stream-sediment Be (ppm), kriged\n"
          "State max (11 ppm) is 8.7 km SW of the park; park-adjacent samples in top 4-13%",
          "outputs/nure/be_kriged.png")

# ── Figure 4: best anomaly score kriged (ocsvm, for completeness) ─────────────
oc = pd.read_csv("outputs/nure/gad/ct_nure_w/ocsvm/anomaly_scores.csv")
oc = oc.rename(columns={"x": "X", "y": "Y"})
krige_map(oc, "anomaly_score",
          "OpenGADBench ocsvm anomaly score, kriged\n"
          "Scoring degenerate vs known W sites (AUC 0.41, SR@5%=0) — shown for completeness",
          "outputs/nure/ocsvm_kriged.png", score_desc="ocsvm anomaly score")

print("done")