# Canada Mortgage & Interest Rates (1969–2026)

Author: John Khan
Data snapshot: pulled 2026-10-17 from the Bank of Canada Valet API (latest observations: daily to 2026-10-15, weekly to 2026-10-14, monthly lending to 2026-07).

Official Canadian mortgage and interest-rate series in CSV form: the Bank of Canada policy rate, CORRA, Government of Canada benchmark bond yields, chartered-bank prime and posted mortgage rates (including the 5-year conventional "benchmark" rate), actual rates and dollar volumes on new and outstanding residential mortgages split by insured/uninsured and fixed/variable term, historical residential mortgage credit, the Senior Loan Officer Survey on mortgage lending conditions, and total CPI.

## Files

| File | Frequency | Coverage | Contents |
|---|---|---|---|
| `canada_mortgage_monthly_panel.csv` | Monthly | 2013-01 → 2026-10 | One row per month joining everything below (start-of-month label; daily/weekly series take the last value in the month, bond yields the monthly mean), plus derived `cpi_yoy_pct`, `spread_5y_posted_minus_goc5y`, `spread_prime_minus_policy` |
| `boc_policy_rate_daily.csv` | Business daily | 1997-08 → 2026-10 | `policy_rate_target` (V39079, from 2009-04), `corra` (AVG.INTWO) |
| `goc_benchmark_bond_yields_daily.csv` | Business daily | 2001-01 → 2026-10 | 2-, 5-, 10-year GoC benchmark yields |
| `chartered_bank_posted_rates_weekly.csv` | Weekly (Wed) | 1975-01 → 2026-10 | Prime rate; 1-, 3-, 5-year conventional posted mortgage rates (1- and 3-year from 1980) |
| `mortgage_lending_rates_monthly.csv` | Monthly | 2013-01 → 2026-07 | Effective interest rates (%) on residential mortgages at chartered banks: new (funds advanced) vs outstanding × insured vs uninsured × total/variable/fixed <1y/1–3y/3–5y/5y+ |
| `mortgage_lending_volumes_monthly.csv` | Monthly | 2013-01 → 2026-07 | Same breakdown, CAD millions (outstanding balances start 2016-07) |
| `residential_mortgage_credit_monthly_1969_2020.csv` | Monthly | 1969-01 → 2020-09 | Total and chartered-bank residential mortgage credit (SA and NSA), total household credit; series discontinued by the source after 2020-09 |
| `slos_mortgage_lending_quarterly.csv` | Quarterly | 2017Q1 → 2026Q2 | Senior Loan Officer Survey balance of opinion, mortgage price and non-price lending conditions |
| `cpi_total_monthly.csv` | Monthly | 1995-01 → 2026-08 | Total CPI (index 2002=100) |
| `series_catalog.csv` | — | — | Every column ↔ source series ID, label, frequency, unit |
| `scripts/build_dataset.py` | — | — | Fully reproducible build from the public API |

## Column naming
`rate_{new|outstanding}_{insured|uninsured}_{total|variable|fixed_lt1y|fixed_1to3y|fixed_3to5y|fixed_5yplus}` (percent) and `cad_mn_…` (CAD millions) with the same pattern. All rates are in percent.

## Sources
- Bank of Canada Valet API — https://www.bankofcanada.ca/valet/docs
  - Policy rate V39079; CORRA AVG.INTWO; bond yields BD.CDN.{2,5,10}YR.DQ.YLD
  - Posted rates (group CHARTERED_BANK_INTEREST): V80691311, V80691333, V80691334, V80691335
  - Lending rates/volumes (groups A4_RATES_MORTGAGES, A4_FUNDS_MORTGAGES): V122667724–V122667798
  - Historical credit (E2): V122736, V122746, V122738, V122748, V36408
  - SLOS: SLOS_ML_LEND_PC, SLOS_ML_LEND_NP
  - Total CPI V41690973 (a Statistics Canada series redistributed by the Bank of Canada)

## Licence
Bank of Canada content may be freely used, copied and distributed with attribution to the Bank of Canada as the source and an indication of changes made, without implying endorsement (https://www.bankofcanada.ca/terms/). Changes made here: JSON → CSV, renamed columns, monthly resampling and derived spreads in the panel file. CPI originates from Statistics Canada (Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence).
This dataset is not endorsed by the Bank of Canada or Statistics Canada.

## Notes & caveats
- The October 2026 row of the panel is a partial month (data to mid-October).
- Posted rates are advertised rates; borrowers typically pay less. The `mortgage_lending_rates_monthly.csv` effective rates show what was actually charged.
- `posted_5y_conventional_mortgage` (V80691335) is the 5-year conventional posted rate published by the Bank of Canada and commonly referenced as the "benchmark" rate in mortgage qualification rules.
- Missing values are left empty; nothing is interpolated.

## Planned extension
Statistics Canada New Housing Price Index (table 18-10-0205-01) and the CMHC 5-year conventional lending rate (table 34-10-0145-01) may be added in a later version.
