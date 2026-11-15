"""Build the Canada and US government bond yield dataset.

Author: John Khan
Sources:
  Bank of Canada Valet API, groups bond_yields_all and TBILL_ALL
    https://www.bankofcanada.ca/valet/docs  (terms: https://www.bankofcanada.ca/terms/)
  U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates and Daily Treasury
    Par Real Yield Curve Rates, https://home.treasury.gov/resource-center/data-chart-center/interest-rates
Run with --refresh to re-download; otherwise the saved files in raw/ are used.
"""
import glob
import json
import os
import sys
import time
import urllib.request

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
OUT = os.path.join(ROOT, "data")
VALET = "https://www.bankofcanada.ca/valet/observations/group/{}/json?start_date=1900-01-01"
UST = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/"
       "{y}/all?type={t}&field_tdr_date_value={y}&page&_format=csv")

CA_BENCH = {"BD.CDN.2YR.DQ.YLD": "ca_2y", "BD.CDN.3YR.DQ.YLD": "ca_3y", "BD.CDN.5YR.DQ.YLD": "ca_5y",
            "BD.CDN.7YR.DQ.YLD": "ca_7y", "BD.CDN.10YR.DQ.YLD": "ca_10y", "BD.CDN.LONG.DQ.YLD": "ca_long",
            "BD.CDN.RRB.DQ.YLD": "ca_real_return_long"}
CA_AVG = {"CDN.AVG.1YTO3Y.AVG": "ca_avg_1to3y", "CDN.AVG.3YTO5Y.AVG": "ca_avg_3to5y",
          "CDN.AVG.5YTO10Y.AVG": "ca_avg_5to10y", "CDN.AVG.OVER.10.AVG": "ca_avg_over10y"}
CA_TBILL = {"V80691342": "tbill_1m", "V80691344": "tbill_3m", "V80691345": "tbill_6m", "V80691346": "tbill_1y",
            "V80691303": "auction_3m", "V80691304": "auction_6m", "V80691305": "auction_1y",
            "V1592248173": "auction_1m_2024_2025"}
US_TENORS = {"1 Mo": "us_1m", "1.5 Month": "us_6w", "2 Mo": "us_2m", "3 Mo": "us_3m", "4 Mo": "us_4m",
             "6 Mo": "us_6m", "1 Yr": "us_1y", "2 Yr": "us_2y", "3 Yr": "us_3y", "5 Yr": "us_5y",
             "7 Yr": "us_7y", "10 Yr": "us_10y", "20 Yr": "us_20y", "30 Yr": "us_30y"}


def valet(group, refresh):
    path = os.path.join(RAW, f"{group}.json")
    if refresh or not os.path.exists(path):
        with urllib.request.urlopen(VALET.format(group), timeout=120) as r:
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
    return df.dropna(how="all", subset=list(names.values())).sort_values("date").reset_index(drop=True)


def treasury(kind, years, refresh):
    t = {"par": "daily_treasury_yield_curve", "real": "daily_treasury_real_yield_curve"}[kind]
    parts = []
    for y in years:
        path = os.path.join(RAW, "treasury", f"{kind}_{y}.csv")
        if refresh or not os.path.exists(path):
            with urllib.request.urlopen(UST.format(y=y, t=t), timeout=120) as r:
                open(path, "wb").write(r.read())
            time.sleep(1)
        parts.append(pd.read_csv(path))
    df = pd.concat(parts, ignore_index=True)
    df["date"] = pd.to_datetime(df.pop("Date"), format="%m/%d/%Y")
    return df.sort_values("date").drop_duplicates("date").reset_index(drop=True)


def main(refresh=False):
    os.makedirs(OUT, exist_ok=True)
    this_year = pd.Timestamp.today().year
    b = valet("bond_yields_all", refresh)
    ca = frame(b, {**CA_BENCH, **CA_AVG})
    ca[["date", *CA_BENCH.values()]].dropna(how="all", subset=list(CA_BENCH.values())).to_csv(
        os.path.join(OUT, "canada_benchmark_bond_yields_daily.csv"), index=False)
    ca[["date", *CA_AVG.values()]].dropna(how="all", subset=list(CA_AVG.values())).to_csv(
        os.path.join(OUT, "canada_marketable_bond_avg_yields_daily.csv"), index=False)

    tb = frame(valet("TBILL_ALL", refresh), CA_TBILL)
    sec = tb[["date", "tbill_1m", "tbill_3m", "tbill_6m", "tbill_1y"]].dropna(how="all", subset=["tbill_1m", "tbill_3m", "tbill_6m", "tbill_1y"])
    auc = tb[["date", "auction_1m_2024_2025", "auction_3m", "auction_6m", "auction_1y"]].dropna(
        how="all", subset=["auction_1m_2024_2025", "auction_3m", "auction_6m", "auction_1y"])
    sec.to_csv(os.path.join(OUT, "canada_tbill_yields_weekly.csv"), index=False)
    auc.to_csv(os.path.join(OUT, "canada_tbill_auction_yields.csv"), index=False)

    par = treasury("par", range(1990, this_year + 1), refresh).rename(columns=US_TENORS)
    par = par[["date"] + [c for c in US_TENORS.values() if c in par.columns]]
    par.to_csv(os.path.join(OUT, "us_treasury_par_yield_curve_daily.csv"), index=False)
    real = treasury("real", range(2003, this_year + 1), refresh)
    real = real.rename(columns={c: "us_real_" + c.lower().replace(" yr", "y").replace(" ", "") for c in real.columns if c != "date"})
    real = real[["date"] + [c for c in real.columns if c != "date"]]
    real.to_csv(os.path.join(OUT, "us_treasury_real_yield_curve_daily.csv"), index=False)

    # Joined panel on days when both markets published
    panel = ca[["date", "ca_2y", "ca_5y", "ca_10y", "ca_long", "ca_real_return_long"]].merge(
        par[["date", "us_3m", "us_2y", "us_5y", "us_10y", "us_30y"]], on="date", how="inner")
    t3 = sec.set_index("date")["tbill_3m"].reindex(panel["date"], method="ffill", tolerance=pd.Timedelta(days=7))
    panel["ca_tbill_3m_last_weekly"] = t3.values
    panel["spread_2y_ca_minus_us"] = (panel.ca_2y - panel.us_2y).round(3)
    panel["spread_10y_ca_minus_us"] = (panel.ca_10y - panel.us_10y).round(3)
    panel["slope_ca_10y_minus_2y"] = (panel.ca_10y - panel.ca_2y).round(3)
    panel["slope_us_10y_minus_2y"] = (panel.us_10y - panel.us_2y).round(3)
    panel["slope_us_10y_minus_3m"] = (panel.us_10y - panel.us_3m).round(3)
    panel.to_csv(os.path.join(OUT, "canada_us_yields_daily_panel.csv"), index=False)


if __name__ == "__main__":
    main(refresh="--refresh" in sys.argv)
