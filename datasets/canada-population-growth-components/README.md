<p align="center"><img src="../../assets/theme-population.png" alt="Canada Population Growth Components" width="100%"></p>

# Canada Population Growth Components

*Births, deaths, immigration, emigration and temporary residents, 1946 to 2026*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** January 1946 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-population-growth-components](https://www.kaggle.com/datasets/johnnykhan1/canada-population-growth-components)

## What it is

A tidy extract of three official Statistics Canada tables on where population growth in Canada comes from: births and deaths (natural increase), immigrants, emigrants and returning emigrants, the change in the number of non-permanent residents such as work and study permit holders and asylum claimants, and moves between provinces. Every province and territory is included.

Source tables:

* [17-10-0008-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000801): Estimates of the components of demographic growth, annual.
* [17-10-0040-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710004001): Estimates of the components of international migration, quarterly.
* [17-10-0059-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710005901): Estimates of the components of natural increase, quarterly.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The annual table covers 1971/1972 to 2025/2026, where each year runs from July 1 to June 30. The two quarterly tables run from the first quarter of 1946 to the second quarter of 2026.

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`components_of_growth_annual.csv`](data/components_of_growth_annual.csv) | 864 KB | in this repository |
| [`cover.png`](data/cover.png) | 89 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 10 KB | in this repository |
| [`international_migration_quarterly.csv`](data/international_migration_quarterly.csv) | 2.2 MB | in this repository |
| [`natural_increase_quarterly.csv`](data/natural_increase_quarterly.csv) | 959 KB | in this repository |
| [`official_metadata_17100008.csv`](data/official_metadata_17100008.csv) | 8 KB | in this repository |
| [`official_metadata_17100040.csv`](data/official_metadata_17100040.csv) | 6 KB | in this repository |
| [`official_metadata_17100059.csv`](data/official_metadata_17100059.csv) | 5 KB | in this repository |

## Columns

### `components_of_growth_annual.csv`

Official annual components of population growth for Canada, each province and territory: births, deaths, immigrants, emigrants, returning emigrants, net emigration, net temporary emigration, net non-permanent residents and their inflows and outflows, net interprovincial migration and residual deviation. Each year runs from July 1 to June 30, from 1971/1972 to 2025/2026. Persons.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Start of the reference period. In components_of_growth_annual.csv each year runs from July 1 to June 30 and is stored as July 1 of its first year (1971-07-01 is 1971/1972, 2025-07-01 is 2025/2026). In the two quarterly files it is the first day of the quarter (2026-04-01 is April to June 2026). |
| `ref_period` | Text | components_of_growth_annual.csv only. Reference year exactly as published, for example 2025/2026, meaning July 1, 2025 to June 30, 2026. |
| `geo` | Text | Geography as published: Canada, the ten provinces and the three territories. Before 1991/1992 (annual) or July 1991 (quarterly) only Northwest Territories including Nunavut is published, and Northwest Territories and Nunavut appear separately after that. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `component` | Text | components_of_growth_annual.csv and international_migration_quarterly.csv only. Component as published: Immigrants, Emigrants, Returning emigrants, Net emigration, Net temporary emigration, Net non-permanent residents, Non-permanent residents, inflows, Non-permanent residents, outflows, and, in the annual file only, Births, Deaths, Net interprovincial migration and Residual deviation. Net emigration is emigrants less returning emigrants, plus net temporary emigration up to June 2016. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Persons in the two components files and Number in the natural increase file. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. units in all three files, so a value of 1000 means 1,000 persons or events. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published count of persons or events in the period. Net components can be negative, for example net non-permanent residents when more people leave that group than join it. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. In this snapshot it is set only in natural_increase_quarterly.csv, for the marriage series and for the combined Northwest Territories including Nunavut births and deaths series that ended in 1991. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `international_migration_quarterly.csv`

Official quarterly components of international migration for Canada, each province and territory: immigrants, emigrants, returning emigrants, net emigration, net temporary emigration, net non-permanent residents and non-permanent resident inflows and outflows. First quarter of 1946 to the second quarter of 2026 (April to June 2026); most components start later. Persons.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Start of the reference period. In components_of_growth_annual.csv each year runs from July 1 to June 30 and is stored as July 1 of its first year (1971-07-01 is 1971/1972, 2025-07-01 is 2025/2026). In the two quarterly files it is the first day of the quarter (2026-04-01 is April to June 2026). |
| `geo` | Text | Geography as published: Canada, the ten provinces and the three territories. Before 1991/1992 (annual) or July 1991 (quarterly) only Northwest Territories including Nunavut is published, and Northwest Territories and Nunavut appear separately after that. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `component` | Text | components_of_growth_annual.csv and international_migration_quarterly.csv only. Component as published: Immigrants, Emigrants, Returning emigrants, Net emigration, Net temporary emigration, Net non-permanent residents, Non-permanent residents, inflows, Non-permanent residents, outflows, and, in the annual file only, Births, Deaths, Net interprovincial migration and Residual deviation. Net emigration is emigrants less returning emigrants, plus net temporary emigration up to June 2016. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Persons in the two components files and Number in the natural increase file. |
| `unit_of_measure_id` | Text | Statistics Canada nu |
| `scalar_factor` | Text | Scale of value as published. units in all three files, so a value of 1000 means 1,000 persons or events. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published count of persons or events in the period. Net components can be negative, for example net non-permanent residents when more people leave that group than join it. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. In this snapshot it is set only in natural_increase_quarterly.csv, for the marriage series and for the combined Northwest Territories including Nunavut births and deaths series that ended in 1991. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `natural_increase_quarterly.csv`

Official quarterly births and deaths for Canada, each province and territory, from the first quarter of 1946 to the second quarter of 2026, plus marriages up to the fourth quarter of 2004 when the marriage series ended. Number of events.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Start of the reference period. In components_of_growth_annual.csv each year runs from July 1 to June 30 and is stored as July 1 of its first year (1971-07-01 is 1971/1972, 2025-07-01 is 2025/2026). In the two quarterly files it is the first day of the quarter (2026-04-01 is April to June 2026). |
| `geo` | Text | Geography as published: Canada, the ten provinces and the three territories. Before 1991/1992 (annual) or July 1991 (quarterly) only Northwest Territories including Nunavut is published, and Northwest Territories and Nunavut appear separately after that. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `vital_event` | Text | natural_increase_quarterly.csv only. Births, Deaths or Marriages. Marriages end with October to December 2004 and that series is flagged terminated. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Persons in the two components files and Number in the natural increase file. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. units in all three files, so a value of 1000 means 1,000 persons or events. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Integer | The published count of persons or events in the period. Net components can be negative, for example net non-permanent residents when more people leave that group than join it. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. In this snapshot it is set only in natural_increase_quarterly.csv, for the marriage series and for the combined Northwest Territories including Nunavut births and deaths series that ended in 1991. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_17100008.csv`

Official Statistics Canada metadata, notes and symbol legend for table 17-10-0008-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | — |
| `Product Id` | Text | — |
| `CANSIM Id` | Text | — |
| `URL` | Text | — |
| `Cube Notes` | Text | — |
| `Archive Status` | Text | — |
| `Frequency` | Text | — |
| `Start Reference Period` | Text | — |
| `End Reference Period` | Date | — |
| `Total number of dimensions` | Integer | — |

### `official_metadata_17100040.csv`

Official Statistics Canada metadata, notes and symbol legend for table 17-10-0040-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | — |
| `Product Id` | Text | — |
| `CANSIM Id` | Text | — |
| `URL` | Text | — |
| `Cube Notes` | Text | — |
| `Archive Status` | Text | — |
| `Frequency` | Text | — |
| `Start Reference Period` | Text | — |
| `End Reference Period` | Date | — |
| `Total number of dimensions` | Integer | — |

### `official_metadata_17100059.csv`

Official Statistics Canada metadata, notes and symbol legend for table 17-10-0059-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | — |
| `Product Id` | Text | — |
| `CANSIM Id` | Text | — |
| `URL` | Text | — |
| `Cube Notes` | Text | — |
| `Archive Status` | Text | — |
| `Frequency` | Text | — |
| `Start Reference Period` | Text | — |
| `End Reference Period` | Date | — |
| `Total number of dimensions` | Integer | — |

## Source and licence

**Source:** Statistics Canada, Demographic Estimates Program, components of population growth. Official tables downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 17-10-0008-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000801, https://www150.statcan.gc.ca/n1/tbl/csv/17100008-eng.zip) 17-10-0040-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710004001, https://www150.statcan.gc.ca/n1/tbl/csv/17100040-eng.zip) 17-10-0059-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710005901, https://www150.statcan.gc.ca/n1/tbl/csv/17100059-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadapopulationgrowthcomponents,
  author    = {Khan, John},
  title     = {Canada Population Growth Components},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-population-growth-components}
}
```

APA: Khan, J. (2026). *Canada Population Growth Components* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-population-growth-components

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of three official Statistics Canada tables on where population growth in Canada comes from: births and deaths (natural increase), immigrants, emigrants and returning emigrants, the change in the number of non-permanent residents such as work and study permit holders and asylum claimants, and moves between provinces. Every province and territory is included.

Source tables:

* [17-10-0008-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000801): Estimates of the components of demographic growth, annual.
* [17-10-0040-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710004001): Estimates of the components of international migration, quarterly.
* [17-10-0059-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710005901): Estimates of the components of natural increase, quarterly.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The annual table covers 1971/1972 to 2025/2026, where each year runs from July 1 to June 30. The two quarterly tables run from the first quarter of 1946 to the second quarter of 2026.

## Files

* components_of_growth_annual.csv: 7,815 rows. 12 components for 15 geographies over 55 July to June years.
* international_migration_quarterly.csv: 22,043 rows. 8 international migration components for 15 geographies over 322 quarters.
* natural_increase_quarterly.csv: 11,738 rows. Births and deaths for 15 geographies over 322 quarters, plus marriages up to 2004.
* data_dictionary.csv: every column in every file, with its type and meaning.
* official_metadata_*.csv: the official Statistics Canada notes, member lists and symbol legend for each table.

## A few numbers from this snapshot

* From July 1, 2025 to June 30, 2026, Canada had 374,708 births and 337,064 deaths, so births exceeded deaths by 37,644 (this difference is computed here, not a published line). These figures are preliminary.
* Canada received 368,224 immigrants in 2025/2026, against 435,551 in 2024/2025. The highest annual count in the table is 493,236 in 2021/2022.
* Net non-permanent residents were -154,614 in 2025/2026, meaning more people left that group than joined it: 441,442 inflows against 596,056 outflows. The highest annual value is 703,206 in 2023/2024.
* In the quarterly file, net non-permanent residents for Canada were -18,875 in April to June 2026.
* In the natural increase file, Canada recorded 94,381 births and 81,422 deaths in April to June 2026.

## Caveats

* Recent periods are preliminary or updated and will be revised. The official notes give the final, updated and preliminary periods for each component, for example immigrants are final up to 2024/2025 in the annual table and net non-permanent residents are final up to 2022/2023.
* Components overlap. Net emigration is emigrants less returning emigrants (plus net temporary emigration before July 2016), and net non-permanent residents is inflows less outflows. Do not add a net line to the lines it is built from.
* Net interprovincial migration is zero for Canada as a whole by definition (published as 0 from 1998/1999). Use the provincial rows for it.
* Residual deviation is a statistical adjustment that spreads the census error of closure over the intercensal period. In this snapshot it is published up to 2020/2021 only.
* Net temporary emigration is no longer calculated from July 2016 onward, and non-permanent resident inflows and outflows are only published from 2021/2022 (July 2021 in the quarterly file). Periods before a component starts appear as empty values with status ..
* Statistics Canada estimates of non-permanent residents differ from IRCC counts of permit holders and asylum claimants; the two are not fully comparable.
* Northwest Territories and Nunavut are only published combined before 1991/1992 (annual) or July 1991 (quarterly). Newfoundland and Labrador starts in 1949 in the natural increase file.
* Marriages end with October to December 2004 because the source no longer releases them.

## Example uses

* Break population growth into natural increase, permanent immigration and temporary residents, by province.
* Study the 2022 to 2024 surge in non-permanent residents and the reversal that followed.
* Model housing, labour market or school demand from population inflows.
* Compare the seasonality of births and deaths across 80 years of quarterly data.
* Join with John Khan's Canada quarterly population estimates and interprovincial migration datasets on Kaggle.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. Statistics Canada updates the quarterly tables every quarter and the annual table each year.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case. Reference periods were stored as dates, and the annual table also keeps its published July to June label in ref_period. Official values, labels, status symbols and termination flags were not altered. No rows were added or removed.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, tables 17-10-0008-01, 17-10-0040-01 and 17-10-0059-01. The published values were not changed. Columns were renamed and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
