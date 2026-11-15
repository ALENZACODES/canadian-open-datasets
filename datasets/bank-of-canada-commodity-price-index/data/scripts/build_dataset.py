"""Build the Bank of Canada commodity price index (BCPI) dataset from the Valet API.

Author: John Khan
Source: https://www.bankofcanada.ca/rates/price-indexes/bcpi/ (terms: https://www.bankofcanada.ca/terms/)
Run with --refresh to re-download the raw JSON; otherwise the saved files in raw/ are used.
"""
import json
import os
import sys
import urllib.request

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
OUT = os.path.join(ROOT, "data")
API = "https://www.bankofcanada.ca/valet/observations/group/{}/json?start_date=1900-01-01"
COMPONENTS = {"BCPI": "total", "BCNE": "ex_energy", "ENER": "energy", "MTLS": "metals_minerals",
              "FOPR": "forestry", "AGRI": "agriculture", "FISH": "fish"}
WEIGHTS = {"WTI": "wti_crude", "WCC": "western_canadian_select", "BRENT": "brent_crude",
           "NATURALGAS": "natural_gas", "COAL": "coal", "AGRI": "agriculture",
           "MTLS": "metals_minerals", "FOPR": "forestry", "FISH": "fish"}


def load(group, refresh):
    path = os.path.join(RAW, f"{group}.json")
    if refresh or not os.path.exists(path):
        with urllib.request.urlopen(API.format(group), timeout=120) as r:
            open(path, "wb").write(r.read())
    return json.load(open(path))


def frame(d, names):
    rows = []
    for o in d["observations"]:
        row = {"date": o["d"]}
        for sid, col in names.items():
            v = o.get(sid, {}).get("v")
            row[col] = float(v) if v not in (None, "") else None
        rows.append(row)
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date").reset_index(drop=True)


def main(refresh=False):
    os.makedirs(OUT, exist_ok=True)
    catalog = []
    for group, prefix, file in [("BCPI_WEEKLY", "W", "bcpi_weekly_1972_2026.csv"),
                                ("BCPI_MONTHLY", "M", "bcpi_monthly_1972_2026.csv"),
                                ("BCPI_ANNUAL", "A", "bcpi_annual_1972_2025.csv")]:
        d = load(group, refresh)
        names = {f"{prefix}.{k}": v for k, v in COMPONENTS.items()}
        df = frame(d, names)
        if prefix == "M":
            for c in COMPONENTS.values():
                df[f"{c}_yoy_pct"] = (df[c].pct_change(12, fill_method=None) * 100).round(2)
            df["date"] = df["date"].dt.strftime("%Y-%m")
        if prefix == "A":
            df = df.rename(columns={"date": "year"})
            df["year"] = df["year"].dt.year
        df.to_csv(os.path.join(OUT, file), index=False)
        for sid, col in names.items():
            s = d["seriesDetail"][sid]
            catalog.append({"file": file, "column": col, "series_id": sid, "label": s["label"],
                            "description": s["description"]})

    d = load("BCPI_WEIGHTS", refresh)
    names = {f"WGTS.{k}": v for k, v in WEIGHTS.items()}
    w = frame(d, names)
    w = w.rename(columns={"date": "year"})
    w["year"] = w["year"].dt.year
    w[list(WEIGHTS.values())] = w[list(WEIGHTS.values())].round(4)
    w.to_csv(os.path.join(OUT, "bcpi_weights_1972_2026.csv"), index=False)
    for sid, col in names.items():
        s = d["seriesDetail"][sid]
        catalog.append({"file": "bcpi_weights_1972_2026.csv", "column": col, "series_id": sid,
                        "label": s["label"], "description": s["description"]})
    pd.DataFrame(catalog).to_csv(os.path.join(OUT, "series_catalog.csv"), index=False)


if __name__ == "__main__":
    main(refresh="--refresh" in sys.argv)
