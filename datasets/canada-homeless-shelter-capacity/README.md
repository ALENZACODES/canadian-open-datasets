<p align="center"><img src="../../assets/theme-housing.png" alt="Canada homeless shelter capacity" width="100%"></p>

# Canada homeless shelter capacity

*Official shelter bed capacity by type, 2016 to 2025*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 1 January 2016 to 23 September 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-homeless-shelter-capacity](https://www.kaggle.com/datasets/johnnykhan1/canada-homeless-shelter-capacity)

## What it is

Official homeless shelter capacity in Canada from [Table 14-10-0353-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035301), the national capacity series maintained with the National Service Provider List. The files report capacity, not occupancy. A flag marks the official 2021 change in how some women's and family shelters are classified. A provincial file adds beds per 10,000 people, using July 1 population of the same year, without adding shelter types together.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 3 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 50 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 7 KB | in this repository |
| [`shelter_capacity.csv`](data/shelter_capacity.csv) | 22.7 MB | in this repository |
| [`shelter_capacity_provincial_beds.csv`](data/shelter_capacity_provincial_beds.csv) | 87 KB | in this repository |
| [`statcan_metadata_14-10-0353.csv`](data/statcan_metadata_14-10-0353.csv) | 31 KB | in this repository |

## Columns

### `SOURCE_MANIFEST.csv`

Source table identifiers, official release dates, retrieval date, and SHA256 checksums.

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | Short identifier for the official source in this package. |
| `title` | Text | Official or documented title of the source table, workbook, or file. |
| `url` | Text | Official source URL. |
| `licence` | Text | Licence name for the source, such as the Statistics Canada Open Licence or the Open Government Licence to Canada. |
| `release_date` | Date | Official release date or official product update statement, as recorded for this snapshot. |
| `retrieval_date` | Date | Date the source file was downloaded, as YYYY MM DD. |
| `file_name` | Text | Name of the downloaded source file. |
| `checksum_sha256` | Text | SHA256 checksum of the downloaded source file. |
| `notes` | Text | Short note about how the source was used in this package. |

### `data_dictionary.csv`

Column dictionary for every data file in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name in the data file. |
| `file` | Text | Data file that contains the column. |
| `type` | Text | Documented value type, such as string, integer, numeric, or boolean. |
| `description` | Text | Plain language description of the column. |

### `shelter_capacity.csv`

Official shelter and bed counts by community, shelter type, and target population from table 14-10-0353. This is capacity, not occupancy.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `type_of_shelter` | Text | Emergency shelter, transitional housing or domestic violence shelter, as published. These types are not added together in this package. |
| `target_population` | Text | Target population as published, including a total and nested groups. Nested groups should not be added to the total. |
| `statistic` | Text | Number of shelters or number of beds. Both are capacity counts, not occupancy. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `ref_period` | Date | Reference period as published. |
| `year` | Integer | Calendar year of the reference period. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `classification_break` | Boolean | True for General - women and Family rows. Official note 1 of the table says that, until 2021, shelters serving women with or without children were included in General - women, and that from 2021 those shelters are included in Family. |
| `classification_break_year` | Integer | 2021 on rows affected by that official classification change. Empty on other target populations. |

### `shelter_capacity_provincial_beds.csv`

Official number of beds for Canada, the provinces, and the territories, total target population, by shelter type, with an adapted beds per 10,000 people figure. Shelter types are not added together.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `type_of_shelter` | Text | Emergency shelter, transitional housing or domestic violence shelter, as published. These types are not added together in this package. |
| `target_population` | Text | Target population as published, including a total and nested groups. Nested groups should not be added to the total. |
| `statistic` | Text | Number of shelters or number of beds. Both are capacity counts, not occupancy. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `ref_period` | Date | Reference period as published. |
| `year` | Integer | Calendar year of the reference period. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `classification_break` | Boolean | True for General - women and Family rows. Official note 1 of the table says that, until 2021, shelters serving women with or without children were included in General - women, and that from 2021 those shelters are included in Family. |
| `classification_break_year` | Text | 2021 on rows affected by that official classification change. Empty on other target populations. |
| `population` | Integer | July 1 population from table 17-10-0009 for the same year and geography. Filled only on the provincial beds file. |
| `beds_per_10000` | Float | Official number of beds times 10,000, divided by July 1 population of the same year. This is an adapted figure, not an official Statistics Canada or Housing, Infrastructure and Communities Canada rate. |

### `statcan_metadata_14-10-0353.csv`

Official Statistics Canada cube metadata for table 14-10-0353, including dimensions, members, and notes. The file has several sections, not one flat table.

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

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahomelesssheltercapacity,
  author    = {Khan, John},
  title     = {Canada homeless shelter capacity},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-homeless-shelter-capacity}
}
```

APA: Khan, J. (2026). *Canada homeless shelter capacity* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-homeless-shelter-capacity

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Official homeless shelter capacity in Canada from [Table 14-10-0353-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035301), the national capacity series maintained with the National Service Provider List. The files report capacity, not occupancy. A flag marks the official 2021 change in how some women's and family shelters are classified. A provincial file adds beds per 10,000 people, using July 1 population of the same year, without adding shelter types together.

## Coverage

2016 to 2025, annual capacity counts for Canada, the provinces and territories, and 472 published geographies including communities.

## Updates

This upload is a snapshot downloaded on 15 November 2026. The table page gave a release date of 2026-09-11.

## A few numbers from this snapshot

* The capacity file has 127,030 rows, matching the official cube row count, for 2016 to 2025 and 472 geographies.
* In 2025, Canada had 23,483 emergency shelter beds, total target population, as published in table 14-10-0353.
* That official count is 5.64 beds per 10,000 people when divided by July 1 2025 population from table 17-10-0009. The per 10,000 figure is adapted, not an official rate.
* The same official emergency shelter capacity line was 15,409 beds in 2016.

## Example uses

* Look up official emergency, transitional and domestic violence shelter capacity.
* Compare provincial capacity per 10,000 people, using the same-year population estimate.
* Avoid mixing pre-2021 and post-2021 General - women and Family counts without the official classification note.

## Caveats

These figures are capacity, not occupancy or a count of people experiencing homelessness. Do not add shelter types together, and do not add nested target populations to the total, or official totals will be double counted. General - women and Family series are affected by the official 2021 classification change. Beds per 10,000 people is an adapted figure that will change if population estimates are revised.

## Files

* `shelter_capacity.csv`: Official shelter and bed counts by community, shelter type and target population. This is capacity, not occupancy. A classification_break flag marks General - women and Family rows, which change meaning in 2021.
* `shelter_capacity_provincial_beds.csv`: Official Number of beds for Canada, the provinces and the territories, total target population, by shelter type, with beds per 10,000 people. Types are not added together.
* `SOURCE_MANIFEST.csv`: Source table identifiers, release dates, retrieval date and checksums.
* `data_dictionary.csv`: Column dictionary for every CSV.
* `METHODS.md`: Methods note.
* `CITATION.txt`: Suggested citation, with DOI pending.
* `statcan_metadata_14-10-0353.csv`: Official cube metadata for Table 14-10-0353-01.

## Licence

This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 14-10-0353 and 17-10-0009. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Suggested citation: John Khan. 2026. Canada homeless shelter capacity [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-homeless-shelter-capacity. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
