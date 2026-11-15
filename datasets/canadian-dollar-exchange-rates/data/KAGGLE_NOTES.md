# Canadian Dollar Exchange Rates 2007–2026

Author: John Khan
Data snapshot: pulled 2026-10-17 from the Bank of Canada Valet API (daily data to 2026-10-16).

Official Bank of Canada exchange rates for the Canadian dollar, in CSV form:
- daily, monthly and annual average rates for 27 currencies since 2017;
- the legacy daily noon rates for about 60 currencies from May 2007 to April 2017;
- one joined USD/CAD series from 2007 to today;
- the Canadian effective exchange rate (CEER) indices since 1999.

Every rate is quoted as **Canadian dollars per one unit of the foreign currency**. For example, `cad_per_usd = 1.4154` means one US dollar cost C$1.4154.

## Files

| File | Frequency | Coverage | Contents |
|---|---|---|---|
| `usd_cad_daily_2007_2026.csv` | Business daily | 2007-05 → 2026-10 | `cad_per_usd`, its inverse `usd_per_cad`, and `method` (`noon` until 2016-12-30, `daily_average` from 2017-01-03) |
| `fx_daily_2017_2026.csv` | Business daily | 2017-01 → 2026-10 | Daily average rates, 27 currencies (`cad_per_usd`, `cad_per_eur`, `cad_per_gbp`, `cad_per_jpy`, `cad_per_cny`, …) |
| `fx_monthly_2017_2026.csv` | Monthly | 2017-01 → 2026-09 | Monthly averages published by the Bank, same columns (`date` is `YYYY-MM`) |
| `fx_annual_2017_2025.csv` | Annual | 2017 → 2025 | Annual averages published by the Bank, same columns |
| `fx_noon_daily_2007_2017.csv` | Business daily | 2007-05 → 2017-04 | Legacy noon rates for about 60 currencies, plus the 90-day forward USD rate and 3- and 6-month USD/CAD forward points |
| `ceer_daily_1999_2026.csv` | Business daily | 1999-01 → 2026-10 | Nominal CEER: broad, broad excluding the US dollar, major currencies, other important trading partners (1999 = 100) |
| `ceer_monthly_1999_2026.csv` | Monthly | 1999-01 → 2026-09 | Nominal and real CEER, same four baskets (real to 2026-06) |
| `series_catalog.csv` | — | — | Every column ↔ Bank of Canada series ID, label and description |
| `scripts/build_dataset.py` | — | — | Rebuilds every file from the public API (`--refresh` to re-download) |

## Coverage gaps
Values are left empty where the Bank did not publish a rate. Nothing is interpolated.
- VND ends in 2019.
- RUB and SAR end in April 2026.
- MYR and THB are missing from 2020 to April 2026.
- PLN starts in May 2026.
- In the legacy noon file, several currencies stop before 2017 because they were redenominated or dropped: VEB, SKK, GHC, and the fixed MMK rate.

## Methodology notes
- **Daily average rates (2017 onward)** are indicative rates. The Bank of Canada derives them from averages of aggregated price quotes from financial institutions and publishes them each business day by 16:30 ET.
- **Noon rates (2007–2017)** were the Bank's earlier benchmark, last updated 28 April 2017. The joined USD/CAD file switches from noon to daily average on 2017-01-03. The two methods differ slightly, so don't read the join as a market move.
- **CEER** is a trade-weighted index of the Canadian dollar against major trading partners' currencies (1999 = 100). A rise means the Canadian dollar strengthened.
- These are not trading rates and should not be used to value transactions.

## Sources
Bank of Canada Valet API (https://www.bankofcanada.ca/valet/docs). Groups used:
- `FX_RATES_DAILY`, `FX_RATES_MONTHLY`, `FX_RATES_ANNUAL`
- `LEGACY_NOON_RATES`
- `CEER_DAILY`, `CEER_MONTHLY_NOMINAL`, `CEER_MONTHLY_REAL`

The series ID for every column is in `series_catalog.csv`.

## Licence
Bank of Canada content may be used, copied and distributed for free, provided the Bank of Canada is credited as the source and changes are indicated, without implying endorsement (https://www.bankofcanada.ca/terms/).

Changes made here:
- JSON converted to CSV;
- columns renamed;
- USD/CAD joined across the 2017 method change;
- `usd_per_cad` added as the inverse of `cad_per_usd`.

This dataset is not endorsed by the Bank of Canada.

## Suggested uses
- Currency conversion of Canadian financial data at official rates.
- Studying the Canadian dollar against oil prices and interest-rate differentials.
- Volatility modelling and forecasting.
- Teaching time-series methods on a clean, well-documented daily series.
