<p align="center"><img src="../../assets/theme-prices.png" alt="Canada core inflation measures" width="100%"></p>

# Canada core inflation measures

*CPI, CPI-trim, CPI-median and CPI-common from the Bank of Canada*

**Theme:** [Prices and inflation](../../README.md#prices-and-inflation) · **Coverage:** January 1995 to September 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-core-inflation-measures](https://www.kaggle.com/datasets/johnnykhan1/canada-core-inflation-measures)

## What it is

Monthly Consumer Price Index and preferred core inflation measures from the Bank of Canada, tidied from the official Valet group CPI_MONTHLY. The group includes Total CPI, the year-over-year change in Total CPI, and the Bank's preferred core measures: CPI-trim, CPI-median and CPI-common, plus earlier core indicators such as CPIX, CPI-XFET and CPIW.

Source: Bank of Canada Valet group [CPI_MONTHLY](https://www.bankofcanada.ca/valet/observations/group/CPI_MONTHLY/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Who it helps

Households watching the cost of living, budget planners, journalists, analysts and students studying inflation in Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`core_inflation_long.csv`](data/core_inflation_long.csv) | 836 KB | in this repository |
| [`core_inflation_wide.csv`](data/core_inflation_wide.csv) | 19 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`series_catalog.csv`](data/series_catalog.csv) | 2 KB | in this repository |

## Columns

### `core_inflation_long.csv`

Tidy long file of the Bank of Canada CPI and core inflation measures, one row per date and series.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `series_id` | Text | Bank of Canada Valet series identifier. |
| `series_label` | Text | Short official label for the series. |
| `series_description` | Text | Official Valet description of the series. |
| `value` | Float | Observation value. Empty when the Bank did not publish a figure for that date. |

### `core_inflation_wide.csv`

Wide monthly file with one column per official series, including Total CPI, CPI-trim, CPI-median, CPI-common and related indicators.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `V41690973` | Float | Total CPI. The total Consumer Price Index (CPI) measures the average change over time in prices paid by Canadian consumers for a basket of goods and services. It is the primary inflation indicator, as published by Statistics Canada and tracked by the Bank of Canada. |
| `V41690914` | Float | Total CPI (seasonally adjusted). The total Consumer Price Index (CPI), seasonally adjusted. |
| `STATIC_TOTALCPICHANGE` | Float | Total CPI, percentage change year-over-year (unadjusted). The unadjusted percentage change in the total Consumer Price Index (CPI) compared to the same month one year earlier. |
| `CPI_TRIM` | Float | CPI-trim. The monthly value of the trim component of the Consumer Price Index (CPI). This measure excludes CPI components whose rates of change in a given month are located in the tails of the distribution of price changes. |
| `CPI_MEDIAN` | Float | CPI-median. The monthly value of the median Consumer Price I |
| `CPI_COMMON` | Float | CPI-common. The monthly value of the common component of Consumer Price Index (CPI). |
| `ATOM_V41693242` | Float | CPIX, percentage change year-over-year (unadjusted). A measure of core inflation that excludes eight of the most volatile Consumer Price Index (CPI) components: fruit, vegetables, gasoline, fuel oil, natural gas, mortgage interest, inter-city transportation and tobacco products: as well as the effect of changes in indirect taxes on the remaining components. It is expressed as the percentage change over the past 12 months and is not seasonally adjusted. |
| `STATIC_CPIXFET` | Float | CPI-XFET, percentage change year-over-year (unadjusted). The unadjusted 12-month percentage change in the Consumer Price Index (CPI) that excludes food, energy and the effect of changes in indirect taxes. |
| `CPIW` | Float | CPIW, percentage change year-over-year (unadjusted). The year-over-year percentage change in the Consumer Price Index (CPI) with basket weights adjusted inversely to component variability and excluding the effect of changes in indirect taxes. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `series_catalog.csv`

Official Valet identifiers, labels and descriptions for every series in the group.

| Column | Type | Description |
|---|---|---|
| `id` | Text | Official Valet series metadata field (id). |
| `label` | Text | Official Valet series metadata field (label). |
| `description` | Text | Official Valet series metadata field (description). |
| `date_format` | Text | Official Valet series metadata field (date_format). |

## Source and licence

**Source:** Bank of Canada Valet group CPI_MONTHLY: https://www.bankofcanada.ca/valet/observations/group/CPI_MONTHLY/csv. Documentation: https://www.bankofcanada.ca/valet/docs. Terms of use: https://www.bankofcanada.ca/terms/. Downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario.

- **Licence:** [Bank of Canada terms of use](https://www.bankofcanada.ca/terms/). Source: Bank of Canada. Content may be used, copied and distributed for free with credit to the Bank of Canada and a note of changes made. Not endorsed by the Bank of Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacoreinflationmeasures,
  author    = {Khan, John},
  title     = {Canada core inflation measures},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-core-inflation-measures}
}
```

APA: Khan, J. (2026). *Canada core inflation measures* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-core-inflation-measures

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly Consumer Price Index and preferred core inflation measures from the Bank of Canada, tidied from the official Valet group CPI_MONTHLY. The group includes Total CPI, the year-over-year change in Total CPI, and the Bank's preferred core measures: CPI-trim, CPI-median and CPI-common, plus earlier core indicators such as CPIX, CPI-XFET and CPIW.

Source: Bank of Canada Valet group [CPI_MONTHLY](https://www.bankofcanada.ca/valet/observations/group/CPI_MONTHLY/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Coverage

Monthly observations from 1995-01-01 to 2026-09-01. Some core measures begin later than Total CPI.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. The Bank of Canada updates these series monthly. Call the official Valet endpoint for a later month.

## A few numbers from this snapshot

* Total CPI inflation, unadjusted year over year, was 3.10 percent in 2026-09.
* CPI-trim was 1.80 percent, CPI-median was 1.90 percent, and CPI-common was 2.40 percent in the same month.
* The file has 381 monthly observations from 1995-01-01 to 2026-09-01, covering 9 official series.

## Example uses

* Compare headline inflation with CPI-trim, CPI-median and CPI-common.
* Join the year-over-year series to policy rates, CORRA or wage growth.
* Chart how the preferred core measures moved after 2020.

## Caveats

CPI-trim, CPI-median and CPI-common are already year-over-year rates, as are STATIC_TOTALCPICHANGE and the older CPIX, CPI-XFET and CPIW series. V41690973 and V41690914 are index levels, not rates. Do not mix levels and rates on the same axis. Some early cells are empty because a measure had not yet been published.

## Files

* `core_inflation_long.csv`: Long tidy file.
* `core_inflation_wide.csv`: Wide monthly file.
* `series_catalog.csv`: Official series list.
* `data_dictionary.csv`: Column dictionary.
* `cover.png`: Cover chart of headline and core inflation.

## Licence

Bank of Canada data are used under the Bank's [terms of use](https://www.bankofcanada.ca/terms/). Please credit the Bank of Canada. The Bank gives no warranty on accuracy. This dataset is not endorsed by the Bank of Canada. The Kaggle licence is set to Other because no standard licence matches these terms exactly. 

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
