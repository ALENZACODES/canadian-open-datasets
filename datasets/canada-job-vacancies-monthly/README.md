<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada job vacancies by industry" width="100%"></p>

# Canada job vacancies by industry

*Monthly vacancies, vacancy rates and payroll jobs, 2015 to 2026*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** January 2015 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-job-vacancies-monthly](https://www.kaggle.com/datasets/johnnykhan1/canada-job-vacancies-monthly)

## What it is

Monthly and quarterly job vacancies, payroll employees and job vacancy rates from the Job Vacancy and Wage Survey, tidied from Statistics Canada. The headline monthly file is seasonally adjusted by industry for Canada (Table 14-10-0406). A second file gives unadjusted monthly totals for Canada, the provinces and the territories (Table 14-10-0371). A third file gives the seasonally adjusted quarterly industry series for Canada (Table 14-10-0400).

Source tables: [14-10-0406-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410040601), [14-10-0371-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037101) and [14-10-0400-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410040001).

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 8 KB | in this repository |
| [`job_vacancies_by_province.csv`](data/job_vacancies_by_province.csv) | 692 KB | in this repository |
| [`job_vacancies_canada_by_industry.csv`](data/job_vacancies_canada_by_industry.csv) | 1.4 MB | in this repository |
| [`job_vacancies_canada_quarterly.csv`](data/job_vacancies_canada_quarterly.csv) | 474 KB | in this repository |
| [`statcan_metadata_14-10-0371.csv`](data/statcan_metadata_14-10-0371.csv) | 5 KB | in this repository |
| [`statcan_metadata_14-10-0400.csv`](data/statcan_metadata_14-10-0400.csv) | 6 KB | in this repository |
| [`statcan_metadata_14-10-0406.csv`](data/statcan_metadata_14-10-0406.csv) | 6 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `job_vacancies_by_province.csv`

Monthly unadjusted job vacancies, payroll employees and vacancy rates for Canada, the provinces and the territories, from Table 14-10-0371.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `statistic` | Text | The published measure, for example job vacancies, payroll employees or the job vacancy rate. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `seasonality` | Text | Seasonally adjusted, or unadjusted for seasonality, as published in the source table. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `job_vacancies_canada_by_industry.csv`

Monthly seasonally adjusted job vacancies, payroll employees and vacancy rates by industry sector for Canada, from Table 14-10-0406.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `naics` | Text | Industry group based on the North American Industry Classification System, including sector totals. |
| `statistic` | Text | The published measure, for example job vacancies, payroll employees or the job vacancy rate. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `seasonality` | Text | Seasonally adjusted, or unadjusted for seasonality, as published in the source table. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `job_vacancies_canada_quarterly.csv`

Quarterly seasonally adjusted job vacancies, payroll employees and vacancy rates by industry sector for Canada, from Table 14-10-0400.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `naics` | Text | Industry group based on the North American Industry Classification System, including sector totals. |
| `statistic` | Text | The published measure, for example job vacancies, payroll employees or the job vacancy rate. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `seasonality` | Text | Seasonally adjusted, or unadjusted for seasonality, as published in the source table. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_14-10-0371.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0371-01, including notes and the symbol legend. Layout is as published, not tidied.


### `statcan_metadata_14-10-0400.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0400-01, including notes and the symbol legend. Layout is as published, not tidied.


### `statcan_metadata_14-10-0406.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0406-01, including notes and the symbol legend. Layout is as published, not tidied.


## Source and licence

**Source:** Statistics Canada Table 14-10-0406-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410040601, https://www150.statcan.gc.ca/n1/tbl/csv/14100406-eng.zip); Statistics Canada Table 14-10-0371-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037101, https://www150.statcan.gc.ca/n1/tbl/csv/14100371-eng.zip); Statistics Canada Table 14-10-0400-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410040001, https://www150.statcan.gc.ca/n1/tbl/csv/14100400-eng.zip). Full table CSV downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadajobvacanciesmonthly,
  author    = {Khan, John},
  title     = {Canada job vacancies by industry},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-job-vacancies-monthly}
}
```

APA: Khan, J. (2026). *Canada job vacancies by industry* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-job-vacancies-monthly

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly and quarterly job vacancies, payroll employees and job vacancy rates from the Job Vacancy and Wage Survey, tidied from Statistics Canada. The headline monthly file is seasonally adjusted by industry for Canada (Table 14-10-0406). A second file gives unadjusted monthly totals for Canada, the provinces and the territories (Table 14-10-0371). A third file gives the seasonally adjusted quarterly industry series for Canada (Table 14-10-0400).

Source tables: [14-10-0406-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410040601), [14-10-0371-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037101) and [14-10-0400-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410040001).

## Coverage

April 2015 through 2026-08 for the monthly files, with 21 industry sectors in the Canada industry tables and 14 geographies in the provincial file.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. Statistics Canada updates these tables monthly. Download the tables again for a later month.

## A few numbers from this snapshot

* Seasonally adjusted job vacancies in Canada were 507,220 in 2026-08, with a vacancy rate of 2.80 percent.
* Payroll employees on the same basis were 17.59 million.
* That vacancy count is +5.4 percent from the same month a year earlier.
* Unadjusted job vacancies in Ontario were 180,460 in 2026-08.
* The monthly industry file has 8,253 rows from 2015-04 to 2026-08. The provincial file has 5,502 rows across 14 geographies.

## Example uses

* Track tightness in the Canadian labour market against unemployment or wage series.
* Compare vacancy rates across industries or across provinces.
* Join the Canada totals to inflation, interest rates or housing activity.

## Caveats

The provincial file is not seasonally adjusted, so month-to-month changes can reflect seasonal hiring. The monthly industry figures are preliminary and are revised when the quarter is finalized; prefer the quarterly file once it is available for that period. Status symbols mark quality. Empty values are unpublished cells, not zeros.

## Files

* `job_vacancies_canada_by_industry.csv`: Monthly seasonally adjusted Canada totals by industry.
* `job_vacancies_by_province.csv`: Monthly unadjusted totals by province and territory.
* `job_vacancies_canada_quarterly.csv`: Quarterly seasonally adjusted Canada totals by industry.
* `data_dictionary.csv`: Column dictionary.
* `statcan_metadata_14-10-0406.csv`: Official metadata for Table 14-10-0406.
* `statcan_metadata_14-10-0371.csv`: Official metadata for Table 14-10-0371.
* `statcan_metadata_14-10-0400.csv`: Official metadata for Table 14-10-0400.
* `cover.png`: Cover chart of the Canada vacancy rate.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 14-10-0406-01, Table 14-10-0371-01, Table 14-10-0400-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
