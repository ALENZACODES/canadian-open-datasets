<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada union membership and coverage" width="100%"></p>

# Canada union membership and coverage

*Unionization and collective agreement coverage by province, age and industry*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 1997 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-union-membership-and-coverage](https://www.kaggle.com/datasets/johnnykhan1/canada-union-membership-and-coverage)

## What it is

Union membership and collective agreement coverage of employees in Canada from the Labour Force Survey, tidied from Statistics Canada [Table 14-10-0129-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410012901) (by province, gender and age) and [Table 14-10-0132-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410013201) (by industry and gender).

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`statcan_metadata_14-10-0129.csv`](data/statcan_metadata_14-10-0129.csv) | 6 KB | in this repository |
| [`statcan_metadata_14-10-0132.csv`](data/statcan_metadata_14-10-0132.csv) | 8 KB | in this repository |
| [`union_status_by_geography_annual.csv`](data/union_status_by_geography_annual.csv) | 4.9 MB | in this repository |
| [`union_status_by_industry_annual.csv`](data/union_status_by_industry_annual.csv) | 1.7 MB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_14-10-0129.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0129-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `statcan_metadata_14-10-0132.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0132-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `union_status_by_geography_annual.csv`

Annual union members, collective agreement coverage and rates by province, gender and age group, from Table 14-10-0129.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `union_status` | Text | Union measure as published. |
| `gender` | Text | Total, Men+ or Women+. |
| `age_group` | Text | Age group as published. |
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

### `union_status_by_industry_annual.csv`

Annual union members, collective agreement coverage and rates by industry and gender, Canada, from Table 14-10-0132.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `union_status` | Text | Union measure as published. |
| `naics` | Text | Industry with NAICS codes in brackets. |
| `gender` | Text | Total, Men+ or Women+. |
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

## Source and licence

**Source:** Statistics Canada Table 14-10-0129-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410012901); Statistics Canada Table 14-10-0132-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410013201); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaunionmembershipandcoverage,
  author    = {Khan, John},
  title     = {Canada union membership and coverage},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-union-membership-and-coverage}
}
```

APA: Khan, J. (2026). *Canada union membership and coverage* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-union-membership-and-coverage

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Union membership and collective agreement coverage of employees in Canada from the Labour Force Survey, tidied from Statistics Canada [Table 14-10-0129-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410012901) (by province, gender and age) and [Table 14-10-0132-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410013201) (by industry and gender).

## Coverage

1997 to 2025, annual. Canada and the ten provinces; industries for Canada.

## Updates

A new year is added each winter. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* The unionization rate in Canada was 28.5 percent in 2025, against 28.3 percent a year earlier.
* The unionization rate in Ontario was 24.4 percent in 2025, against 24.5 percent a year earlier.
* The unionization rate in Quebec was 36.6 percent in 2025, against 36.0 percent a year earlier.
* By industry in 2025, collective agreement coverage ranged from 3.0 percent in agriculture to 77.5 percent in public sector.
* The geography file has 28,710 rows and the industry file has 9,135 rows, from 1997 to 2025.

## Example uses

* Track the long decline in private sector unionization.
* Compare union coverage across provinces and age groups.
* Study the union wage premium with earnings data.
* Teach panel data methods with clean annual series.

## Caveats

Counts are in thousands of employees; rates are percentages, so check unit_of_measure. The Labour Force Survey excludes the territories and people living on reserves. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `union_status_by_geography_annual.csv`: Annual union members, collective agreement coverage and rates by province, gender and age group, from Table 14-10-0129.
* `union_status_by_industry_annual.csv`: Annual union members, collective agreement coverage and rates by industry and gender, Canada, from Table 14-10-0132.
* `statcan_metadata_14-10-0129.csv`: Official cube metadata for Table 14-10-0129-01, as published.
* `statcan_metadata_14-10-0132.csv`: Official cube metadata for Table 14-10-0132-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 14-10-0129-01, Table 14-10-0132-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
