<p align="center"><img src="../../assets/theme-population.png" alt="Canada non permanent residents" width="100%"></p>

# Canada non permanent residents

*Quarterly counts by permit type and province, plus age and gender, 2021 onward*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** January 2021 to July 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-non-permanent-residents](https://www.kaggle.com/datasets/johnnykhan1/canada-non-permanent-residents)

## What it is

Estimates of non permanent residents in Canada, the temporary residents behind much of recent population growth. Tidied from Statistics Canada [Table 17-10-0121-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710012101) (quarterly, by permit type) and [Table 17-10-0158-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015801) (July 1, by age and gender). Types include work permit holders, study permit holders, people with both, asylum claimants and protected persons, and family members.

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`non_permanent_residents_by_age_gender_annual.csv`](data/non_permanent_residents_by_age_gender_annual.csv) | 1.1 MB | in this repository |
| [`non_permanent_residents_by_type_quarterly.csv`](data/non_permanent_residents_by_type_quarterly.csv) | 477 KB | in this repository |
| [`statcan_metadata_17-10-0121.csv`](data/statcan_metadata_17-10-0121.csv) | 6 KB | in this repository |
| [`statcan_metadata_17-10-0158.csv`](data/statcan_metadata_17-10-0158.csv) | 9 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `non_permanent_residents_by_age_gender_annual.csv`

July 1 number of non permanent residents by province or territory, gender and age group, with median and average age, from Table 17-10-0158.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `gender` | Text | Total, Men+ or Women+. |
| `age_group` | Text | Age group, or Median age or Average age. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `non_permanent_residents_by_type_quarterly.csv`

Quarterly number of non permanent residents by type (work permit, study permit, asylum claimants and others), by province or territory, from Table 17-10-0121.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `npr_type` | Text | Type of non permanent resident as published. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_17-10-0121.csv`

Official Statistics Canada cube metadata shipped with Table 17-10-0121-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `statcan_metadata_17-10-0158.csv`

Official Statistics Canada cube metadata shipped with Table 17-10-0158-01, including notes and the symbol legend. Layout is as published, not tidied.

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
| `End Reference Period` | Text | Last reference period in the table at download time. |
| `Total number of dimensions` | Text | Number of dimensions in the table. |

## Source and licence

**Source:** Statistics Canada Table 17-10-0121-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710012101); Statistics Canada Table 17-10-0158-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015801); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadanonpermanentresidents,
  author    = {Khan, John},
  title     = {Canada non permanent residents},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-non-permanent-residents}
}
```

APA: Khan, J. (2026). *Canada non permanent residents* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-non-permanent-residents

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Estimates of non permanent residents in Canada, the temporary residents behind much of recent population growth. Tidied from Statistics Canada [Table 17-10-0121-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710012101) (quarterly, by permit type) and [Table 17-10-0158-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015801) (July 1, by age and gender). Types include work permit holders, study permit holders, people with both, asylum claimants and protected persons, and family members.

## Coverage

Quarterly from July 2021 to July 2026; annual by age from 2021 to 2026. Canada, provinces and territories. Single year ages were left out; every grouped age band and age measure was kept.

## Updates

Updated quarterly with the population estimates. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Canada had 2,779,774 non permanent residents on July 1, 2026, down 5.3 percent from a year earlier.
* The peak in this file was 2,984,285 on October 1, 2024.
* Asylum claimants, protected persons and related groups numbered 530,090, and Ontario was home to 1,246,301 non permanent residents.
* The quarterly file has 3,234 rows from July 2021; the age and gender file has 9,324 rows from 2021.

## Example uses

* Measure the role of temporary residents in population growth.
* Track the effect of the study permit cap and work permit changes.
* Compare provinces' reliance on temporary residents.
* Model rental demand in large cities.

## Caveats

Estimates are preliminary and revised. Counts are on the first day of each quarter (or July 1 for the age file). Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `non_permanent_residents_by_type_quarterly.csv`: Quarterly number of non permanent residents by type (work permit, study permit, asylum claimants and others), by province or territory, from Table 17-10-0121.
* `non_permanent_residents_by_age_gender_annual.csv`: July 1 number of non permanent residents by province or territory, gender and age group, with median and average age, from Table 17-10-0158.
* `statcan_metadata_17-10-0121.csv`: Official cube metadata for Table 17-10-0121-01, as published.
* `statcan_metadata_17-10-0158.csv`: Official cube metadata for Table 17-10-0158-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 17-10-0121-01, Table 17-10-0158-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
