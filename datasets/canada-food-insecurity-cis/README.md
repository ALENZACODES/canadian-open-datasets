<p align="center"><img src="../../assets/theme-health.png" alt="Canada household food insecurity" width="100%"></p>

# Canada household food insecurity

*Canadian Income Survey food insecurity, 2018 to 2024*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** 2018 to 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-food-insecurity-cis](https://www.kaggle.com/datasets/johnnykhan1/canada-food-insecurity-cis)

## What it is

Household food insecurity in Canada from the Canadian Income Survey, tidied from [Table 13-10-0834-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310083401). Official quality flags (A to F, including E and F) are kept in their own column. A percentage point gap compares each percentage with the Canada figure for the same year and the same family type and food security status. The table does not publish confidence intervals, so none are added.

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 2 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 50 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 4 KB | in this repository |
| [`food_insecurity_cis.csv`](data/food_insecurity_cis.csv) | 6.4 MB | in this repository |
| [`statcan_metadata_13-10-0834.csv`](data/statcan_metadata_13-10-0834.csv) | 9 KB | in this repository |

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

### `food_insecurity_cis.csv`

Official Canadian Income Survey food insecurity estimates from table 13-10-0834, with quality flags and adapted percentage point gaps against Canada for matched categories.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `economic_family_type` | Text | Economic family type as published. |
| `food_security_status` | Text | Food security status as published, including food secure and marginal, moderate or severe food insecurity. |
| `statistic` | Text | Number of persons or percentage of persons, as published. This table does not include confidence intervals. |
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
| `ref_period` | Date | Reference period as published, usually a calendar year. |
| `year` | Integer | Calendar year of the reference period. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `estimate_quality` | Text | Official Statistics Canada quality symbol from the STATUS column: A excellent, B very good, C good, D acceptable, E use with caution, F too unreliable to be published, plus other official symbols when present. |
| `estimate_quality_label` | Text | Plain language label for the official quality symbol. |
| `canada_value` | Float | Canada figure for the same year, economic family type, food security status and statistic, so categories are matched. |
| `gap_vs_canada` | Float | This percentage minus the matched Canada percentage, in percentage points. Empty on count rows. This is an adapted comparison, not an official test. |

### `statcan_metadata_13-10-0834.csv`

Official Statistics Canada cube metadata for table 13-10-0834, including dimensions, members, and notes. The file has several sections, not one flat table.

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
@misc{khan2026canadafoodinsecuritycis,
  author    = {Khan, John},
  title     = {Canada household food insecurity},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-food-insecurity-cis}
}
```

APA: Khan, J. (2026). *Canada household food insecurity* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-food-insecurity-cis

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Household food insecurity in Canada from the Canadian Income Survey, tidied from [Table 13-10-0834-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310083401). Official quality flags (A to F, including E and F) are kept in their own column. A percentage point gap compares each percentage with the Canada figure for the same year and the same family type and food security status. The table does not publish confidence intervals, so none are added.

## Coverage

2018 to 2024, annual, Canada, the provinces and territorial groups as published, by economic family type and food security status.

## Updates

This upload is a snapshot downloaded on 15 November 2026. The table page gave a release date of 2026-04-29. Estimates for 2018 to 2023 were revised with the 2024 CIS release, as stated in official note 22.

## A few numbers from this snapshot

* The file has 28,560 rows, matching the official cube, for 2018 to 2024. The survey behind the table is the Canadian Income Survey (survey number 5200), not the Canadian Community Health Survey.
* In 2024, 24.0 percent of people in Canada lived in a food insecure household, All persons, as published in table 13-10-0834. The official quality flag on that estimate is A (excellent).
* The same official line was 16.8 percent in 2018.
* The cube does not publish confidence intervals. Quality flags A to F, including E (use with caution) and F (too unreliable to be published), are carried in estimate_quality.

## Example uses

* Track official CIS food insecurity percentages by province and family type.
* Read the official quality flag before using an estimate.
* Compare a province or family type with the matching Canada category.

## Caveats

This is the Canadian Income Survey series, not the Canadian Community Health Survey. Quality flag E means use with caution, and F means too unreliable to be published. The table has no confidence intervals. gap_vs_canada is a simple subtraction of official percentages, not a formal test. Estimates for 2018 to 2023 in this snapshot already include the official 2024 CIS revision to 2021 Census population counts.

## Files

* `food_insecurity_cis.csv`: Official Canadian Income Survey food insecurity counts and percentages, with official quality flags and a percentage point gap against the matching Canada category.
* `SOURCE_MANIFEST.csv`: Source table identifier, release date, retrieval date and checksum.
* `data_dictionary.csv`: Column dictionary for every CSV.
* `METHODS.md`: Methods note.
* `CITATION.txt`: Suggested citation, with DOI pending.
* `statcan_metadata_13-10-0834.csv`: Official cube metadata for Table 13-10-0834-01.

## Licence

This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 13-10-0834-01. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Suggested citation: John Khan. 2026. Canada household food insecurity [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-food-insecurity-cis. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
