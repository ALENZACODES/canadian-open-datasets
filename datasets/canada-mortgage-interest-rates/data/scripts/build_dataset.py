"""Build the Canada Mortgage & Interest Rates dataset from the Bank of Canada Valet API.

Author: John Khan
Source: Bank of Canada Valet API (https://www.bankofcanada.ca/valet/docs)
Terms:  https://www.bankofcanada.ca/terms/  (free reuse with attribution)

Run:  python scripts/build_dataset.py
Writes cleaned CSVs to ./data and raw JSON responses to ./raw.
"""
import json
import time
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
DATA = ROOT / "data"
BASE = "https://www.bankofcanada.ca/valet"
RAW.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)


def get_json(path, fname):
    url = f"{BASE}/{path}"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    d = r.json()
    (RAW / fname).write_text(json.dumps(d))
    time.sleep(0.5)  # be polite to the API
    return d


def obs_to_frame(d):
    rows = []
    for o in d["observations"]:
        row = {"date": o["d"]}
        for k, v in o.items():
            if k == "d":
                continue
            val = v.get("v") if isinstance(v, dict) else None
            row[k] = pd.to_numeric(val, errors="coerce") if val not in (None, "") else None
        rows.append(row)
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date").reset_index(drop=True)


def series(ids, fname, rename):
    frames = []
    for sid in ids:
        d = get_json(f"observations/{sid}/json", f"series_{sid}.json")
        frames.append(obs_to_frame(d).set_index("date"))
    df = pd.concat(frames, axis=1, sort=True).rename(columns=rename).reset_index()
    df.to_csv(DATA / fname, index=False, float_format="%.4f")
    return df


def group(gid, fname, colmap):
    d = get_json(f"observations/group/{gid}/json", f"group_{gid}.json")
    df = obs_to_frame(d)
    df = df.rename(columns=colmap)[["date"] + list(colmap.values())]
    df.to_csv(DATA / fname, index=False, float_format="%.4f")
    return df


catalog = []


def note(file, sid, name, label, freq, unit):
    catalog.append(dict(file=file, column=name, boc_series_id=sid, label=label, frequency=freq, unit=unit))


# 1. Policy & money-market rates (business daily)
pol = {"V39079": "policy_rate_target", "AVG.INTWO": "corra"}
series(pol, "boc_policy_rate_daily.csv", pol)
note("boc_policy_rate_daily.csv", "V39079", "policy_rate_target", "Target for the overnight rate", "business daily", "%")
note("boc_policy_rate_daily.csv", "AVG.INTWO", "corra", "Canadian Overnight Repo Rate Average (CORRA)", "business daily", "%")

# 2. Government of Canada benchmark bond yields (business daily)
bonds = {"BD.CDN.2YR.DQ.YLD": "goc_2y_yield", "BD.CDN.5YR.DQ.YLD": "goc_5y_yield", "BD.CDN.10YR.DQ.YLD": "goc_10y_yield"}
series(bonds, "goc_benchmark_bond_yields_daily.csv", bonds)
for k, v in bonds.items():
    note("goc_benchmark_bond_yields_daily.csv", k, v, f"Government of Canada benchmark bond yield, {v.split('_')[1]}", "business daily", "%")

# 3. Chartered bank posted rates (weekly, Wednesdays)
posted = {"V80691311": "prime_rate", "V80691333": "posted_1y_conventional_mortgage",
          "V80691334": "posted_3y_conventional_mortgage", "V80691335": "posted_5y_conventional_mortgage"}
series(posted, "chartered_bank_posted_rates_weekly.csv", posted)
labels = {"V80691311": "Prime rate", "V80691333": "Conventional mortgage, 1-year",
          "V80691334": "Conventional mortgage, 3-year", "V80691335": "Conventional mortgage, 5-year (posted / benchmark)"}
for k, v in posted.items():
    note("chartered_bank_posted_rates_weekly.csv", k, v, labels[k], "weekly", "%")

# 4 & 5. Rates and volumes on new (funds advanced) and outstanding mortgages, chartered banks (monthly)
terms = ["total", "variable", "fixed_lt1y", "fixed_1to3y", "fixed_3to5y", "fixed_5yplus"]
term_lbl = ["Total", "Variable rate", "Fixed rate, <1 year", "Fixed rate, 1 to <3 years",
            "Fixed rate, 3 to <5 years", "Fixed rate, 5 years and over"]
blocks = [("new", "insured", "Funds advanced"), ("new", "uninsured", "Funds advanced"),
          ("outstanding", "insured", "Outstanding balances"), ("outstanding", "uninsured", "Outstanding balances")]


def a4_map(start, prefix, file, unit):
    m, i = {}, start
    for flow, ins, flow_lbl in blocks:
        for t, tl in zip(terms, term_lbl):
            sid = f"V{i}"
            col = f"{prefix}_{flow}_{ins}_{t}"
            m[sid] = col
            note(file, sid, col, f"Residential mortgages, {ins}, {tl} - {flow_lbl}", "monthly (month-end)", unit)
            i += 1
    return m


group("A4_RATES_MORTGAGES", "mortgage_lending_rates_monthly.csv",
      a4_map(122667775, "rate", "mortgage_lending_rates_monthly.csv", "%"))
group("A4_FUNDS_MORTGAGES", "mortgage_lending_volumes_monthly.csv",
      a4_map(122667724, "cad_mn", "mortgage_lending_volumes_monthly.csv", "CAD millions"))

# 6. Historical residential mortgage credit outstanding (monthly, 1969-2020, series discontinued)
credit = {"V122736": "res_mortgage_credit_total_nsa", "V122746": "res_mortgage_credit_total_sa",
          "V122738": "res_mortgage_credit_banks_nsa", "V122748": "res_mortgage_credit_banks_sa",
          "V36408": "household_credit_total_nsa"}
series(credit, "residential_mortgage_credit_monthly_1969_2020.csv", credit)
for k, v in credit.items():
    note("residential_mortgage_credit_monthly_1969_2020.csv", k, v, v.replace("_", " "), "monthly", "CAD millions")

# 7. Senior Loan Officer Survey: mortgage lending conditions (quarterly)
slos = {"SLOS_ML_LEND_PC": "slos_mortgage_price_conditions", "SLOS_ML_LEND_NP": "slos_mortgage_nonprice_conditions"}
group("slos_mortgage_lending", "slos_mortgage_lending_quarterly.csv", slos)
note("slos_mortgage_lending_quarterly.csv", "SLOS_ML_LEND_PC", "slos_mortgage_price_conditions", "Mortgage price lending conditions, balance of opinion", "quarterly", "balance of opinion")
note("slos_mortgage_lending_quarterly.csv", "SLOS_ML_LEND_NP", "slos_mortgage_nonprice_conditions", "Mortgage non-price lending conditions, balance of opinion", "quarterly", "balance of opinion")

# 8. Total CPI (for real-rate calculations)
series({"V41690973": "cpi_total"}, "cpi_total_monthly.csv", {"V41690973": "cpi_total"})
note("cpi_total_monthly.csv", "V41690973", "cpi_total", "Total CPI (Statistics Canada vector, served by Bank of Canada)", "monthly", "index 2002=100")

pd.DataFrame(catalog).to_csv(DATA / "series_catalog.csv", index=False)

# 9. Analysis-ready monthly panel (month-end / last available value in the month)
def monthly(f, how="last"):
    df = pd.read_csv(DATA / f, parse_dates=["date"]).set_index("date")
    return getattr(df.resample("MS"), how)()

panel = pd.concat(sort=True, objs=[
    monthly("boc_policy_rate_daily.csv"),
    monthly("goc_benchmark_bond_yields_daily.csv", "mean").add_suffix("_avg"),
    monthly("chartered_bank_posted_rates_weekly.csv"),
    monthly("mortgage_lending_rates_monthly.csv"),
    monthly("mortgage_lending_volumes_monthly.csv"),
    monthly("cpi_total_monthly.csv"),
], axis=1)
panel["cpi_yoy_pct"] = panel["cpi_total"].pct_change(12, fill_method=None) * 100
panel["spread_5y_posted_minus_goc5y"] = panel["posted_5y_conventional_mortgage"] - panel["goc_5y_yield_avg"]
panel["spread_prime_minus_policy"] = panel["prime_rate"] - panel["policy_rate_target"]
panel = panel.loc["2013-01-01":].dropna(how="all")
panel.index.name = "month"
panel.reset_index().to_csv(DATA / "canada_mortgage_monthly_panel.csv", index=False, float_format="%.4f")
print("done:", sorted(p.name for p in DATA.glob("*.csv")))
