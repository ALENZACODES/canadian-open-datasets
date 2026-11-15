<p align="center"><img src="../../assets/theme-housing.png" alt="Canada Housing Affordability Index 1980 to 2026" width="100%"></p>

# Canada Housing Affordability Index 1980 to 2026

*Bank of Canada affordability index, new home prices and the posted 5 year rate*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 1980 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-housing-affordability-repo-import](https://www.kaggle.com/datasets/johnnykhan1/canada-housing-affordability-repo-import)

## What it is

This is the data and code behind my notebook [Canada Housing Affordability Index, 1980 to 2026](https://www.kaggle.com/code/johnnykhan1/canada-housing-affordability-index-1980-to-2026). It asks one question: how much of a typical household's income does it take to own an average priced home in Canada today, compared with the last 45 years, and how much of the swing comes from mortgage rates?

It is a straight import of my GitHub project, so you get the snapshot CSVs, the notebook that pulls and charts them, the three charts it makes, and the requirements file.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`LICENSE`](data/LICENSE) | 1 KB | in this repository |
| [`KAGGLE_NOTES.md`](data/KAGGLE_NOTES.md) | 4 KB | in this repository |
| [`canada-housing-affordability-index-1980-2026.ipynb`](data/canada-housing-affordability-index-1980-2026.ipynb) | 330 KB | in this repository |
| [`charts/01_affordability_index.png`](data/charts/01_affordability_index.png) | 143 KB | in this repository |
| [`charts/02_affordability_vs_rate.png`](data/charts/02_affordability_vs_rate.png) | 172 KB | in this repository |
| [`charts/03_nhpi_yoy.png`](data/charts/03_nhpi_yoy.png) | 55 KB | in this repository |
| [`data/quarterly_afford_nhpi.csv`](data/data/quarterly_afford_nhpi.csv) | 4 KB | in this repository |
| [`data/weekly_posted_5yr.csv`](data/data/weekly_posted_5yr.csv) | 39 KB | in this repository |
| [`requirements.txt`](data/requirements.txt) | 1 KB | in this repository |

## Columns

### `data/quarterly_afford_nhpi.csv`

Quarterly Bank of Canada housing affordability index and New Housing Price Index year over year change, 1980 Q3 to 2026 Q2

| Column | Type | Description |
|---|---|---|
| `date` | Date | First day of the quarter the values refer to (YYYY-MM-DD). |
| `INDINF_AFFORD_Q` | Float | Housing affordability index: housing costs as a share of average household disposable income, as a fraction (0.413 = 41.3%). Higher is less affordable. Bank of Canada series INDINF_AFFORD_Q. |
| `INDINF_NHPI_Q` | Float | New Housing Price Index, percent change from a year earlier (Statistics Canada table 18-10-0205-01 via Bank of Canada series INDINF_NHPI_Q). Empty before 1993 Q1. |

### `data/weekly_posted_5yr.csv`

Weekly posted 5 year conventional mortgage rate at chartered banks, January 1980 to October 2026

| Column | Type | Description |
|---|---|---|
| `date` | Date | Week date as the Bank of Canada gives it (YYYY-MM-DD). |
| `V80691335` | Float | Posted 5 year conventional mortgage rate at chartered banks, percent (Bank of Canada series V80691335). |

## Source and licence

**Source:** Bank of Canada Valet API, https://www.bankofcanada.ca/valet/docs (series INDINF_AFFORD_Q, INDINF_NHPI_Q, V80691335). Affordability index definition: https://www.bankofcanada.ca/rates/indicators/capacity-and-inflation-pressures/real-estate-market-definitions/. New Housing Price Index: Statistics Canada table 18-10-0205-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810020501. Pulled October 18, 2026 by John Khan.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.
- **Licence:** [Bank of Canada terms of use](https://www.bankofcanada.ca/terms/). Source: Bank of Canada. Content may be used, copied and distributed for free with credit to the Bank of Canada and a note of changes made. Not endorsed by the Bank of Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahousingaffordabilityrepoimport,
  author    = {Khan, John},
  title     = {Canada Housing Affordability Index 1980 to 2026},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-housing-affordability-repo-import}
}
```

APA: Khan, J. (2026). *Canada Housing Affordability Index 1980 to 2026* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-housing-affordability-repo-import

<details><summary>Full notes from the Kaggle page</summary>

## What this is

This is the data and code behind my notebook [Canada Housing Affordability Index, 1980 to 2026](https://www.kaggle.com/code/johnnykhan1/canada-housing-affordability-index-1980-to-2026). It asks one question: how much of a typical household's income does it take to own an average priced home in Canada today, compared with the last 45 years, and how much of the swing comes from mortgage rates?

It is a straight import of my GitHub project, so you get the snapshot CSVs, the notebook that pulls and charts them, the three charts it makes, and the requirements file.

## Sources

All three series come from the [Bank of Canada Valet API](https://www.bankofcanada.ca/valet/docs).

* **INDINF_AFFORD_Q**, the Bank of Canada housing affordability index. The Bank defines it as housing costs (mortgage payments plus utilities) divided by average household disposable income, for a representative household buying an average priced resale home with 5% down over 25 years. Full definition: [Bank of Canada real estate market definitions](https://www.bankofcanada.ca/rates/indicators/capacity-and-inflation-pressures/real-estate-market-definitions/).
* **INDINF_NHPI_Q**, the New Housing Price Index, change from a year earlier in percent. The underlying index is Statistics Canada [table 18-10-0205-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810020501). The Bank serves it as a quarterly series.
* **V80691335**, the posted 5 year conventional mortgage rate at chartered banks, weekly.

## How it was built

The notebook calls the Valet API for each series and saves what it got to `data/`. If the API can't be reached it reads those CSVs instead, so it also runs offline. The values are exactly what the API returned on the last run (October 18, 2026). Nothing is smoothed or filled in. The notebook does its own quarterly averaging of the weekly mortgage rate when it needs it.

## Files

| File | What is in it |
|---|---|
| `data/quarterly_afford_nhpi.csv` | 184 quarters, 1980 Q3 to 2026 Q2: affordability index and new home price change |
| `data/weekly_posted_5yr.csv` | 2,442 weeks, January 2, 1980 to October 14, 2026: posted 5 year mortgage rate |
| `canada-housing-affordability-index-1980-2026.ipynb` | The full analysis notebook |
| `charts/` | The three charts the notebook draws |
| `README.md`, `requirements.txt`, `LICENSE` | Project notes, Python packages, MIT licence for the code |

## Column guide

**data/quarterly_afford_nhpi.csv**

* `date`: first day of the quarter (1980-07-01 is 1980 Q3)
* `INDINF_AFFORD_Q`: share of average household disposable income needed to cover housing costs, as a fraction. 0.413 means 41.3%. Higher means less affordable.
* `INDINF_NHPI_Q`: New Housing Price Index, percent change from the same quarter a year earlier. Empty before 1993 Q1 because the Bank's quarterly series starts there.

**data/weekly_posted_5yr.csv**

* `date`: the week's date as the Bank of Canada gives it
* `V80691335`: posted 5 year conventional mortgage rate at chartered banks, percent

## A few numbers from the snapshot

* In 2026 Q2 it took 41.3% of income to carry an average priced home. The average since 1980 is 37.4%.
* The high was 64.7% in 1981 Q3 and the low was 27.5% in 2002 Q1.
* New home prices were 2.3% lower than a year earlier in 2026 Q2. The peak was +11.8% in 2021 Q3.
* The posted 5 year rate ranged from 4.64% to 21.75% over these weeks.

## Updates

This upload is a fixed snapshot from October 18, 2026 and isn't refreshed on a schedule. The Bank publishes the affordability index and the price series quarterly, so if you want newer numbers, run the notebook with internet on and it pulls the latest values.

## Caveats

* The posted rate is the banks' advertised rate. Most borrowers pay less, so treat it as a trend signal, not what people actually paid.
* The affordability index is a national average. It hides big gaps between cities.
* The Bank may revise past values, so a fresh pull can differ slightly from this snapshot.

## Licence

The code is MIT licensed (see `LICENSE`). The data belongs to the Bank of Canada and Statistics Canada and is shared here under their terms, with attribution: [Bank of Canada terms of use](https://www.bankofcanada.ca/terms/) and the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Bank of Canada and Statistics Canada. This data was not changed. This is not an official product of either and neither endorses it.

Author: John Khan


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
