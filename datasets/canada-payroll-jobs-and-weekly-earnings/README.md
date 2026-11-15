<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada payroll jobs and weekly earnings" width="100%"></p>

# Canada payroll jobs and weekly earnings

*Monthly payroll employment and average weekly earnings by province*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** January 2001 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-payroll-jobs-and-weekly-earnings](https://www.kaggle.com/datasets/johnnykhan1/canada-payroll-jobs-and-weekly-earnings)

## What it is

Payroll employment and average weekly earnings including overtime from the Survey of Employment, Payrolls and Hours, tidied from Statistics Canada [Table 14-10-0223-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301). The survey counts jobs from payroll records, so it complements the household based Labour Force Survey.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`payroll_employment_weekly_earnings_by_province_monthly.csv`](data/payroll_employment_weekly_earnings_by_province_monthly.csv) | 42.3 MB | in this repository |
| [`statcan_metadata_14-10-0223.csv`](data/statcan_metadata_14-10-0223.csv) | 7 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `payroll_employment_weekly_earnings_by_province_monthly.csv`

Monthly payroll employment and average weekly earnings including overtime, by province or territory and industry, from Table 14-10-0223.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `estimate` | Text | Employment for all employees, or average weekly earnings including overtime. |
| `naics` | Text | Industry group with its NAICS code in brackets. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_14-10-0223.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0223-01, including notes and the symbol legend. Layout is as published, not tidied.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

## Source and licence

**Source:** Statistics Canada Table 14-10-0223-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadapayrolljobsandweeklyearnings,
  author    = {Khan, John},
  title     = {Canada payroll jobs and weekly earnings},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-payroll-jobs-and-weekly-earnings}
}
```

APA: Khan, J. (2026). *Canada payroll jobs and weekly earnings* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-payroll-jobs-and-weekly-earnings

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Payroll employment and average weekly earnings including overtime from the Survey of Employment, Payrolls and Hours, tidied from Statistics Canada [Table 14-10-0223-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301). The survey counts jobs from payroll records, so it complements the household based Labour Force Survey.

## Coverage

January 2001 to August 2026, monthly. Canada, provinces and territories, by industry sector.

## Updates

Released monthly, about two months after the reference month. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Average weekly earnings (industrial aggregate excluding unclassified businesses) in Canada were 1,354.55 dollars in August 2026, up 3.7 percent from a year earlier.
* Average weekly earnings (industrial aggregate excluding unclassified businesses) in Ontario were 1,395.60 dollars in August 2026, up 3.9 percent from a year earlier.
* Payroll employment in Canada was 18,368,488 in August 2026, up 0.3 percent from a year earlier.
* The file has 232,848 rows across 14 geographies and 27 industry groups from January 2001 to August 2026.

## Example uses

* Track wage growth by province and industry.
* Compare payroll jobs with Labour Force Survey employment.
* Build real wage series with CPI data.
* Forecast earnings growth.

## Caveats

Check the table notes for seasonal adjustment and revisions; the latest month is preliminary. Employment counts jobs, not people. Empty values mean no figure was published, often for confidentiality.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `payroll_employment_weekly_earnings_by_province_monthly.csv`: Monthly payroll employment and average weekly earnings including overtime, by province or territory and industry, from Table 14-10-0223.
* `statcan_metadata_14-10-0223.csv`: Official cube metadata for Table 14-10-0223-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 14-10-0223-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
