<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada Employment Insurance beneficiaries" width="100%"></p>

# Canada Employment Insurance beneficiaries

*Seasonally adjusted regular EI beneficiaries by province, sex and age*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** January 1997 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-employment-insurance-beneficiaries](https://www.kaggle.com/datasets/johnnykhan1/canada-employment-insurance-beneficiaries)

## What it is

Monthly counts of people receiving regular Employment Insurance benefits in Canada, tidied from Statistics Canada [Table 14-10-0011-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410001101). Regular benefits go to people who lose a job through no fault of their own and are available for work. A second measure counts beneficiaries who reported no earnings. Counts are seasonally adjusted and refer to the Labour Force Survey reference week, usually the week containing the 15th.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`ei_regular_beneficiaries_monthly.csv`](data/ei_regular_beneficiaries_monthly.csv) | 10.7 MB | in this repository |
| [`statcan_metadata_14-10-0011.csv`](data/statcan_metadata_14-10-0011.csv) | 4 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `ei_regular_beneficiaries_monthly.csv`

Monthly number of people receiving regular Employment Insurance benefits by province or territory, sex and age group, from Table 14-10-0011.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `beneficiary_detail` | Text | Regular benefits, or regular benefits without declared earnings, as published. |
| `sex` | Text | Sex group as published. |
| `age_group` | Text | Age group as published. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_14-10-0011.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0011-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 14-10-0011-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410001101); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaemploymentinsurancebeneficiaries,
  author    = {Khan, John},
  title     = {Canada Employment Insurance beneficiaries},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-employment-insurance-beneficiaries}
}
```

APA: Khan, J. (2026). *Canada Employment Insurance beneficiaries* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-employment-insurance-beneficiaries

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly counts of people receiving regular Employment Insurance benefits in Canada, tidied from Statistics Canada [Table 14-10-0011-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410001101). Regular benefits go to people who lose a job through no fault of their own and are available for work. A second measure counts beneficiaries who reported no earnings. Counts are seasonally adjusted and refer to the Labour Force Survey reference week, usually the week containing the 15th.

## Coverage

January 1997 to August 2026, monthly. Canada, provinces and territories, by sex and by age group (15 to 24, 25 to 54, 55 and over).

## Updates

Statistics Canada releases a new month roughly two months after the reference month. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* 541,320 people in Canada received regular Employment Insurance benefits in August 2026, down 2.9 percent from a year earlier.
* Ontario had 185,210 regular beneficiaries in August 2026, against 183,990 a year earlier.
* Young people aged 15 to 24 made up 44,600 of Canada's regular beneficiaries in August 2026.
* The peak in this file is 1.65 million regular beneficiaries in May 2021.
* The file has 74,048 rows across 16 geographies, by sex and four age groups, from January 1997 to August 2026.

## Example uses

* Track labour market stress month by month alongside the Labour Force Survey.
* Compare EI reliance across provinces and age groups.
* Study EI use after the emergency benefits of 2020 ended.
* Build early warning features for unemployment forecasts.

## Caveats

The EI statistics program was suspended for the March to September 2020 reference months while most people were on the Canada Emergency Response Benefit, and Statistics Canada asks for caution with those months. The current and previous month are subject to revision. Program rule changes affect comparisons over time. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `ei_regular_beneficiaries_monthly.csv`: Monthly number of people receiving regular Employment Insurance benefits by province or territory, sex and age group, from Table 14-10-0011.
* `statcan_metadata_14-10-0011.csv`: Official cube metadata for Table 14-10-0011-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 14-10-0011-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
