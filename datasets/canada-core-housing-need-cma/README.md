<p align="center"><img src="../../assets/theme-housing.png" alt="Canada core housing need by CMA" width="100%"></p>

# Canada core housing need by CMA

*CHS official rates and 2021 Census counts, kept separate*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 2018, 2021, 2022 and 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-core-housing-need-cma](https://www.kaggle.com/datasets/johnnykhan1/canada-core-housing-need-cma)

## What it is

Official core housing need figures for Canada, the provinces and selected census metropolitan areas, from [Table 46-10-0085-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4610008501) and official 2021 Census household counts from [Table 98-10-0248-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810024801). The Canadian Housing Survey and the 2021 Census are stored in separate files. They are not equivalent and are not presented as a continuous annual series. Only official survey rates and official census counts are used. No census rates are computed. A 2021 CMA geography crosswalk is included.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 3 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 1 KB | in this repository |
| [`census_2021_core_need_counts.csv`](data/census_2021_core_need_counts.csv) | 124 KB | in this repository |
| [`chs_core_housing_need.csv`](data/chs_core_housing_need.csv) | 8.7 MB | in this repository |
| [`cma_geography_crosswalk_2021.csv`](data/cma_geography_crosswalk_2021.csv) | 45 KB | in this repository |
| [`cover.png`](data/cover.png) | 56 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 8 KB | in this repository |
| [`statcan_metadata_46-10-0085.csv`](data/statcan_metadata_46-10-0085.csv) | 12 KB | in this repository |
| [`statcan_metadata_98-10-0248.csv`](data/statcan_metadata_98-10-0248.csv) | 209 KB | in this repository |

## Columns

### `SOURCE_MANIFEST.csv`

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | — |
| `title` | Text | — |
| `url` | Text | — |
| `licence` | Text | — |
| `release_date` | Date | — |
| `retrieval_date` | Date | — |
| `file_name` | Text | — |
| `checksum_sha256` | Text | — |
| `notes` | Text | Non-equivalence note for the survey and census series, including the difference between Canada (provinces only) and Census Canada. |

### `census_2021_core_need_counts.csv`

| Column | Type | Description |
|---|---|---|
| `ref_period` | Integer | Reference period as published. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `core_housing_need` | Text | Official 2021 Census core housing need category. |
| `households` | Integer | Official number of private households from the 2021 Census. This is a count, not a rate. |
| `tenure` | Text | Census tenure as Total, Owner or Renter, taken from official tenure members. |
| `join_key` | Text | Documented join key based on the geography name, with the official (CMA) marker removed, for use with the crosswalk. |
| `year` | Integer | Survey year or 2021 for the census extract. |
| `source` | Text | Official source table for the row. |
| `series` | Text | Canadian Housing Survey or 2021 Census. The two series are not equivalent and are not one continuous annual series. |
| `geography_vintage` | Integer | 2021, the Standard Geographic Classification vintage used in both source cubes. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |

### `chs_core_housing_need.csv`

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `tenure_including_first_time_homebuyer_and_social_and_affordable_housing_status` | Text | Official Canadian Housing Survey tenure, including first-time homebuyer and social and affordable housing status. |
| `core_housing_need_statistics` | Text | Official survey statistic, including counts, percentages and 95% confidence intervals. |
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
| `ref_period` | Date | Reference period as published. |
| `year` | Integer | Survey year or 2021 for the census extract. |
| `source` | Text | Official source table for the row. |
| `series` | Text | Canadian Housing Survey or 2021 Census. The two series are not equivalent and are not one continuous annual series. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `canada_provinces_only_value` | Float | Official Canada (provinces only) value of the same survey statistic, year and tenure, used only for the percentage-point gap. |
| `gap_vs_canada_pp` | Float | Official survey percentage minus the official Canada (provinces only) percentage for the same year, tenure and statistic, in percentage points. This gap is adapted. It is not computed for counts or confidence intervals. |

### `cma_geography_crosswalk_2021.csv`

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `cma_uid` | Text | Three-digit CMA code parsed from a 2021S0503 DGUID, where that official DGUID is present. |
| `geo_level` | Text | Canada, province, territory, CMA, or population centre or rural area, as classified from the official name and DGUID. |
| `geography_vintage` | Integer | 2021, the Standard Geographic Classification vintage used in both source cubes. |
| `province_or_territory` | Text | Province or territory implied by the official geography name, where that is unambiguous. Ottawa-Gatineau is left blank. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `in_chs` | Boolean | True when the geography appears in the Canadian Housing Survey file. |
| `in_census_2021` | Boolean | True when the geography appears in the 2021 Census counts file. |
| `chs_geo` | Text | Official survey geography name, when the geography is in the survey file. |
| `census_geo` | Text | Official 2021 Census geography name, when the geography is in the census file. |
| `join_key` | Text | Documented join key based on the geography name, with the official (CMA) marker removed, for use with the crosswalk. |
| `notes` | Text | Non-equivalence note for the survey and census series, including the difference between Canada (provinces only) and Census Canada. |

### `data_dictionary.csv`

| Column | Type | Description |
|---|---|---|
| `column` | Text | — |
| `file` | Text | — |
| `type` | Text | — |
| `description` | Text | — |

### `statcan_metadata_46-10-0085.csv`

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

### `statcan_metadata_98-10-0248.csv`

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
| `End Reference Period` | Text | — |
| `Total number of dimensions` | Text | — |
| `Universe` | Text | — |
| `Variable List` | Text | — |

## Source and licence

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacorehousingneedcma,
  author    = {Khan, John},
  title     = {Canada core housing need by CMA},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-core-housing-need-cma}
}
```

APA: Khan, J. (2026). *Canada core housing need by CMA* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-core-housing-need-cma

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Official core housing need figures for Canada, the provinces and selected census metropolitan areas, from [Table 46-10-0085-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4610008501) and official 2021 Census household counts from [Table 98-10-0248-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810024801). The Canadian Housing Survey and the 2021 Census are stored in separate files. They are not equivalent and are not presented as a continuous annual series. Only official survey rates and official census counts are used. No census rates are computed. A 2021 CMA geography crosswalk is included.

## Coverage

Canadian Housing Survey years 2018, 2021, 2022, 2024 only, Canada (provinces only), provinces, selected CMAs and urban or rural groups. 2021 Census counts for Canada, provinces, territories and CMAs.

## Updates

This upload is a snapshot downloaded on 15 November 2026. Official release dates were 2026-09-21 for the survey table and 2022-09-21 for the census table.

## A few numbers from this snapshot

* The Canadian Housing Survey file has 32,298 official rows and published years 2018, 2021, 2022, 2024 only. It is not a continuous annual series.
* In 2024, 11.6% of households in Canada (provinces only) were in core housing need, total tenure, as published in table 46-10-0085. The official 2018 figure was 11.3%.
* The 2021 Census counts file has official household counts only, for Canada, the provinces and territories, and CMAs. In 2021, 1,451,030 private households in Canada were in core need, total tenure, as published in table 98-10-0248. No census rates are computed in this package.
* The survey and the census use related but different methods, years, tenure labels and Canada universes. They are stored in separate files and must not be treated as one continuous series. A 2021 geography crosswalk is included.

## Example uses

* Use official survey percentages and confidence intervals for the published survey years.
* Use official 2021 Census counts as counts, not as a continuation of the survey and not as a source for computed rates in this package.
* Use the 2021 crosswalk when comparing CMA names and DGUIDs across the two files.

## Caveats

Do not stack the survey and census files into one annual series. The survey Canada figure is provinces only; the census Canada figure includes the territories. No census rates are computed here. Survey years are 2018, 2021, 2022 and 2024 only.

## Files

* `chs_core_housing_need.csv`: Official Canadian Housing Survey core housing need counts, percentages and confidence intervals from table 46-10-0085, including the published years 2018, 2021, 2022 and 2024 only. This is not a continuous annual series.
* `census_2021_core_need_counts.csv`: Official 2021 Census counts of private households by core housing need status and tenure, for Canada, the provinces and territories, and CMAs, from table 98-10-0248. Counts only. No census rates are computed in this package.
* `cma_geography_crosswalk_2021.csv`: Geography crosswalk for the survey and 2021 Census files, with 2021 vintage DGUIDs, CMA identifiers, and flags for which official source includes each geography.
* `SOURCE_MANIFEST.csv`: Source table identifiers, release dates, retrieval date and checksums.
* `data_dictionary.csv`: Column dictionary.
* `METHODS.md`: Methods note, including the non-equivalence of the survey and census series.
* `CITATION.txt`: Suggested citation, with DOI pending.
* `statcan_metadata_46-10-0085.csv`: Official Statistics Canada cube metadata for Table 46-10-0085-01.
* `statcan_metadata_98-10-0248.csv`: Official Statistics Canada cube metadata for Table 98-10-0248-01.

## Licence

This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 46-10-0085 and 98-10-0248. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Suggested citation: John Khan. 2026. Canada core housing need by CMA [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-core-housing-need-cma. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
