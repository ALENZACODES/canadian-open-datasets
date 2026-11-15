"""Build the Canadian dollar exchange-rate dataset from the Bank of Canada Valet API.

Author: John Khan
Source: https://www.bankofcanada.ca/valet/docs (terms: https://www.bankofcanada.ca/terms/)
Run with --refresh to re-download the raw JSON; otherwise the saved files in raw/ are used.
"""
import json
import os
import re
import sys
import urllib.request

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "raw")
OUT = os.path.join(ROOT, "data")
GROUPS = ["FX_RATES_DAILY", "FX_RATES_MONTHLY", "FX_RATES_ANNUAL", "LEGACY_NOON_RATES",
          "CEER_DAILY", "CEER_MONTHLY_NOMINAL", "CEER_MONTHLY_REAL"]
API = "https://www.bankofcanada.ca/valet/observations/group/{}/json?start_date=1900-01-01"


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

    def add(d, names, file):
        for sid, col in names.items():
            s = d["seriesDetail"][sid]
            catalog.append({"file": file, "column": col, "series_id": sid,
                            "label": s["label"], "description": s.get("description", "")})

    # Daily, monthly and annual averages since 2017
    for group, prefix, file in [("FX_RATES_DAILY", "FX", "fx_daily_2017_2026.csv"),
                                ("FX_RATES_MONTHLY", "FXM", "fx_monthly_2017_2026.csv"),
                                ("FX_RATES_ANNUAL", "FXA", "fx_annual_2017_2025.csv")]:
        d = load(group, refresh)
        names = {sid: "cad_per_" + sid[len(prefix):len(prefix) + 3].lower() for sid in d["seriesDetail"]}
        df = frame(d, names)
        if group == "FX_RATES_MONTHLY":
            df["date"] = df["date"].dt.strftime("%Y-%m")
        if group == "FX_RATES_ANNUAL":
            df = df.rename(columns={"date": "year"}); df["year"] = df["year"].dt.year
        df.to_csv(os.path.join(OUT, file), index=False)
        add(d, names, file)

    # Legacy noon rates 2007-2017
    d = load("LEGACY_NOON_RATES", refresh)
    names = {}
    for sid, s in d["seriesDetail"].items():
        code = s["label"].replace("_NOON", "").lower()
        desc = s.get("description", "")
        if sid == "IEXE0105":
            col = "cad_per_usd_90day_forward"
        elif sid in ("IEXE0124", "IEXE0125"):
            col = "usd_cad_forward_points_" + ("3m" if sid == "IEXE0124" else "6m")
        elif "(local)" in desc or "(old)" in desc or "(fixed)" in desc:
            col = "cad_per_" + code + "_" + re.sub(r"\W", "", desc.split("(")[-1]).lower()
        else:
            col = "cad_per_" + code
        names[sid] = col
    assert len(set(names.values())) == len(names), "duplicate column names"
    df = frame(d, names)
    df = df.dropna(axis=1, how="all")
    names = {k: v for k, v in names.items() if v in df.columns}
    df.to_csv(os.path.join(OUT, "fx_noon_daily_2007_2017.csv"), index=False)
    add(d, names, "fx_noon_daily_2007_2017.csv")

    # Long USD/CAD series: noon rate until 2017-04-28, daily average from 2017-01-03
    noon = df[["date", "cad_per_usd"]].dropna().assign(method="noon")
    noon = noon[noon.date < "2017-01-03"]
    daily = pd.read_csv(os.path.join(OUT, "fx_daily_2017_2026.csv"), parse_dates=["date"])
    avg = daily[["date", "cad_per_usd"]].dropna().assign(method="daily_average")
    long = pd.concat([noon, avg]).sort_values("date")
    long["usd_per_cad"] = (1 / long["cad_per_usd"]).round(6)
    long.to_csv(os.path.join(OUT, "usd_cad_daily_2007_2026.csv"), index=False)

    # Canadian effective exchange rate (CEER) indices
    ceer = {"CEER_BROADN": "ceer_broad", "CEER_BROADN_XUS": "ceer_broad_ex_us",
            "CEER_MCN": "ceer_major_currencies", "CEER_OITPN": "ceer_other_partners"}
    d = load("CEER_DAILY", refresh)
    frame(d, ceer).to_csv(os.path.join(OUT, "ceer_daily_1999_2026.csv"), index=False)
    add(d, ceer, "ceer_daily_1999_2026.csv")
    dn = load("CEER_MONTHLY_NOMINAL", refresh); dr = load("CEER_MONTHLY_REAL", refresh)
    nom = {k + "M": v + "_nominal" for k, v in ceer.items()}
    real = {"CEER_BROADM": "ceer_broad_real", "CEER_BROAD_XUSM": "ceer_broad_ex_us_real",
            "CEER_MCM": "ceer_major_currencies_real", "CEER_OITPM": "ceer_other_partners_real"}
    m = frame(dn, nom).merge(frame(dr, real), on="date", how="outer")
    m["date"] = m["date"].dt.strftime("%Y-%m")
    m.to_csv(os.path.join(OUT, "ceer_monthly_1999_2026.csv"), index=False)
    add(dn, nom, "ceer_monthly_1999_2026.csv"); add(dr, real, "ceer_monthly_1999_2026.csv")

    pd.DataFrame(catalog).to_csv(os.path.join(OUT, "series_catalog.csv"), index=False)


if __name__ == "__main__":
    main(refresh="--refresh" in sys.argv)
