# Canada and US Government Bond Yields 1990–2026

Author: John Khan
Data snapshot: pulled 2026-10-17. Bank of Canada data runs to 2026-10-15, US Treasury data to 2026-10-16.

Daily government bond yields for Canada and the United States in CSV form:
- **Canada:** Government of Canada benchmark bond yields (2, 3, 5, 7, 10 years, long bond, Real Return Bond), average yields on marketable bonds by maturity band, and treasury bill yields. All from the Bank of Canada.
- **US:** the full Treasury par yield curve from 1990, and the real (TIPS) yield curve from 2003. Both from the US Department of the Treasury.
- **Joined panel:** a daily Canada–US file with ready-made spreads and curve slopes.

All yields are in percent per year.

## Files

| File | Frequency | Coverage | Contents |
|---|---|---|---|
| `canada_us_yields_daily_panel.csv` | Business daily (days both markets published) | 2001-01 → 2026-10 | Canada 2y/5y/10y/long/RRB, US 3m/2y/5y/10y/30y, the latest weekly Canadian 3-month T-bill yield, Canada-minus-US spreads at 2y and 10y, 10y−2y slopes for both, US 10y−3m slope |
| `canada_benchmark_bond_yields_daily.csv` | Business daily | 2001-01 → 2026-10 | `ca_2y`, `ca_3y`, `ca_5y`, `ca_7y`, `ca_10y`, `ca_long`, `ca_real_return_long` |
| `canada_marketable_bond_avg_yields_daily.csv` | Business daily | 2001-01 → 2026-10 | Average yields of Government of Canada marketable bonds: 1–3y, 3–5y, 5–10y, over 10y |
| `canada_tbill_yields_weekly.csv` | Weekly (Wednesday) | 2000-01 → 2026-10 | Treasury bill yields: 1 month, 3 months, 6 months, 1 year |
| `canada_tbill_auction_yields.csv` | Each auction (about every two weeks) | 2000-01 → 2026-10 | Average auction yields: 3 months, 6 months, 1 year, plus the 1-month bills issued May 2024 to July 2025 |
| `us_treasury_par_yield_curve_daily.csv` | Business daily | 1990-01 → 2026-10 | Par yields from 1 month to 30 years (`us_1m` … `us_30y`) |
| `us_treasury_real_yield_curve_daily.csv` | Business daily | 2003-01 → 2026-10 | Real par yields: 5, 7, 10, 20, 30 years |
| `scripts/build_dataset.py` | — | — | Rebuilds every file from the public sources (`--refresh` to re-download) |

## Coverage notes
Values are left empty where the source did not publish. Nothing is interpolated.

US Treasury par curve:
- 1-month from 2001-07-31;
- 2-month from 2018-10-16;
- 4-month from 2022-10-19;
- 1.5-month (6-week, `us_6w`) from 2025-02-18;
- 20-year from 1993-10-01;
- the 30-year has a gap from February 2002 to February 2006, when the Treasury suspended the bond.

US real curve:
- 20-year from 2004-07-27;
- 30-year from 2010-02-22.

Canadian 1-month auction bills were issued only from May 2024 to July 2025, during the move away from Bankers' Acceptances after CDOR ended.

## Column notes
- `ca_long` is the Government of Canada long-term benchmark bond (around 30 years).
- `ca_real_return_long` is the long Real Return Bond yield, a real yield. `ca_long − ca_real_return_long` is a simple breakeven inflation rate.
- `ca_tbill_3m_last_weekly` in the panel is the most recent weekly 3-month T-bill yield on or before that date, up to 7 days old.
- Spreads and slopes are in percentage points. For example, `spread_2y_ca_minus_us = ca_2y − us_2y`.

## Sources
- **Bank of Canada Valet API** (https://www.bankofcanada.ca/valet/docs), groups `bond_yields_all` and `TBILL_ALL`.
  - Series IDs: `BD.CDN.{2,3,5,7,10}YR.DQ.YLD`, `BD.CDN.LONG.DQ.YLD`, `BD.CDN.RRB.DQ.YLD`, `CDN.AVG.*`
  - T-bills: V80691342, V80691344–V80691346; auctions: V80691303–V80691305, V1592248173.
- **U.S. Department of the Treasury**, Daily Treasury Par Yield Curve Rates and Daily Treasury Par Real Yield Curve Rates (https://home.treasury.gov/resource-center/data-chart-center/interest-rates).

## Licence
- **Bank of Canada data:** free to use, copy and distribute, provided the Bank of Canada is credited as the source and changes are indicated, without implying endorsement (https://www.bankofcanada.ca/terms/).
- **US Treasury data:** a work of the US federal government and in the public domain in the United States.
- **Changes made here:**
  - JSON and yearly CSV files combined into one CSV per series group;
  - columns renamed;
  - the panel joined on common dates, with derived spreads and slopes.
- This dataset is not endorsed by the Bank of Canada or the US Treasury.

## Suggested uses
- Yield curve inversion and recession studies.
- Modelling the Canada–US rate gap and the Canadian dollar. The companion dataset *Canadian Dollar Exchange Rates 2007-2026* joins on date.
- Fitting term-structure models (Nelson–Siegel and similar).
- Breakeven inflation and real rates.
