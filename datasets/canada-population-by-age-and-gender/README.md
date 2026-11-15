<p align="center"><img src="../../assets/theme-population.png" alt="Canada population by age and gender" width="100%"></p>

# Canada population by age and gender

*July 1 population estimates by province, five year age group and gender*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** 1971 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-population-by-age-and-gender](https://www.kaggle.com/datasets/johnnykhan1/canada-population-by-age-and-gender)

## What it is

Annual population estimates for Canada, the provinces and the territories on July 1 of each year, by gender and age group, tidied from Statistics Canada [Table 17-10-0005-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000501). Includes five year age groups, broad groups such as 0 to 14, 15 to 64 and 65 and older, and the median and average age.

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_population_by_age_gender_annual.csv`](data/canada_population_by_age_gender_annual.csv) | 10.7 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`statcan_metadata_17-10-0005.csv`](data/statcan_metadata_17-10-0005.csv) | 9 KB | in this repository |

## Columns

### `canada_population_by_age_gender_annual.csv`

Annual July 1 population estimates by province or territory, gender and age group, with median and average age, from Table 17-10-0005.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `gender` | Text | Total, Men+ or Women+, as published. |
| `age_group` | Text | Age group, or Median age or Average age. |
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
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_17-10-0005.csv`

Official Statistics Canada cube metadata shipped with Table 17-10-0005-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 17-10-0005-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000501); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadapopulationbyageandgender,
  author    = {Khan, John},
  title     = {Canada population by age and gender},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-population-by-age-and-gender}
}
```

APA: Khan, J. (2026). *Canada population by age and gender* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-population-by-age-and-gender

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Annual population estimates for Canada, the provinces and the territories on July 1 of each year, by gender and age group, tidied from Statistics Canada [Table 17-10-0005-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000501). Includes five year age groups, broad groups such as 0 to 14, 15 to 64 and 65 and older, and the median and average age.

## Coverage

1971 to 2026, annual, July 1. Canada, provinces and territories (Nunavut from 1991). Single year ages from the source were left out to keep the file small; every grouped age band and age measure was kept.

## Updates

Statistics Canada updates these estimates each September and revises earlier years. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Canada's population was estimated at 41,798,407 on July 1, 2026, up 0.5 percent from a year earlier.
* The median age in Canada was 40.9 years in 2026.
* People aged 65 and older numbered 8,378,381 and children aged 0 to 14 numbered 6,254,277 in 2026.
* Ontario's population was 16,262,121 in 2026.
* The file has 87,048 rows for 15 geographies, three gender groups and 39 age groups or age measures, from 1971 to 2026.

## Example uses

* Measure population ageing and dependency ratios by province.
* Build per capita rates for income, crime or health data.
* Project labour force growth from age structure.
* Compare how immigration has changed age profiles.

## Caveats

Recent years are preliminary and get revised. Gender groups are Men+ and Women+, as defined by Statistics Canada. Median and average age rows use years as the unit, not persons; check unit_of_measure.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `canada_population_by_age_gender_annual.csv`: Annual July 1 population estimates by province or territory, gender and age group, with median and average age, from Table 17-10-0005.
* `statcan_metadata_17-10-0005.csv`: Official cube metadata for Table 17-10-0005-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 17-10-0005-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
