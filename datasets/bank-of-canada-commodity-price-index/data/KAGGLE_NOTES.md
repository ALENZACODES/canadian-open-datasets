# Bank of Canada Commodity Price Index (BCPI) 1972–2026

Author: John Khan
Data snapshot: pulled 2026-10-17 from the Bank of Canada Valet API (weekly to 2026-10-14, monthly to 2026-09, annual to 2025).

The Bank of Canada commodity price index (BCPI) is a chain Fisher price index of the spot or transaction prices, in US dollars, of 26 commodities produced in Canada and sold in world markets. This dataset has:
- the total index and six sub-indices in weekly, monthly and annual form, from 1972;
- the annual weights behind the index.

## Files

| File | Frequency | Coverage | Contents |
|---|---|---|---|
| `bcpi_monthly_1972_2026.csv` | Monthly | 1972-01 → 2026-09 | `total`, `ex_energy`, `energy`, `metals_minerals`, `forestry`, `agriculture`, `fish`, plus a 12-month % change for each (`*_yoy_pct`) |
| `bcpi_weekly_1972_2026.csv` | Weekly (Wed) | 1972-01 → 2026-10 | Same seven indices (average of the five business days ending Wednesday) |
| `bcpi_annual_1972_2025.csv` | Annual | 1972 → 2025 | Same seven indices, annual averages |
| `bcpi_weights_1972_2026.csv` | Annual | 1972 → 2026 | Weights in %, summing to 100 each year: WTI, Western Canadian Select and Brent crude, natural gas, coal, metals and minerals, forestry, agriculture, fish |
| `series_catalog.csv` | — | — | Column ↔ Bank of Canada series ID, label and description |
| `scripts/build_dataset.py` | — | — | Rebuilds every file from the public API (`--refresh` to re-download) |

All indices are set to 100 in January 1972 (see the first row of the monthly and weekly files) and are in US-dollar terms.

## What is in each component
- **Energy:** crude oil (WTI, Western Canadian Select, Brent), natural gas (Henry Hub), metallurgical coal.
- **Metals and minerals:** gold, silver, nickel, copper, aluminium, zinc, potash, lead, iron.
- **Forestry:** pulp, lumber, newsprint.
- **Agriculture:** potatoes, cattle, hogs, wheat, barley, canola, corn.
- **Fish:** finfish and shellfish.

The exact price source for each commodity is listed in `series_catalog.csv` (weights rows) and on the Bank's BCPI page.

## Methodology notes
These notes summarise the Bank of Canada's BCPI page.
- **Weights:**
  - They are based mainly on Statistics Canada input-output tables, which come with a lag.
  - They are projected forward from the latest reference year using price and production-volume proxies.
  - Weights for the current year are estimated from projected prices and reassessed four times a year.
  - Before 1996, the split between the crude oil benchmarks is held at its 1996 shares.
- **Missing source data:** when a source price for the reference period is not yet available, the latest available value is repeated and revised later. **Recent weeks and months can therefore be revised.**
- **Source changes:**
  - lumber moved to CME futures in July 2022, revised back to January 2010;
  - barley changed source in 2018 and again in 2020;
  - Western Canadian Select changed source in March 2025.

Nothing in this dataset is interpolated or adjusted. The only derived columns are the `*_yoy_pct` changes in the monthly file.

## Sources
- Bank of Canada Valet API (https://www.bankofcanada.ca/valet/docs), groups `BCPI_WEEKLY`, `BCPI_MONTHLY`, `BCPI_ANNUAL`, `BCPI_WEIGHTS`.
- BCPI methodology: https://www.bankofcanada.ca/rates/price-indexes/bcpi/

## Licence
Bank of Canada content may be used, copied and distributed for free, provided the Bank of Canada is credited as the source and changes are indicated, without implying endorsement (https://www.bankofcanada.ca/terms/).

Changes made here:
- JSON converted to CSV;
- columns renamed;
- weights rounded to 4 decimals;
- 12-month % changes added to the monthly file.

This dataset is not endorsed by the Bank of Canada.

## Suggested uses
- Studying commodity cycles and the Canadian dollar. The companion dataset *Canadian Dollar Exchange Rates 2007-2026* joins on date.
- Nowcasting the monthly index from the weekly series.
- Teaching index numbers and chain weighting.
