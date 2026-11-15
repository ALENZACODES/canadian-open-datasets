<p align="center"><img src="../../assets/theme-health.png" alt="Canada cancer incidence rates and counts" width="100%"></p>

# Canada cancer incidence rates and counts

*Official age-standardized rates and counts, 1992 to 2023*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** January 1992 to February 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-cancer-incidence-ccr](https://www.kaggle.com/datasets/johnnykhan1/canada-cancer-incidence-ccr)

## What it is

Official cancer incidence counts and age-standardized rates for Canada, the provinces and the territories, tidied from [Table 13-10-0747-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310074701). Rates are the official Statistics Canada series, age-standardized by the direct method to the final 2021 Canadian postcensal population structure. Counts and rates are kept as separate measures. This dataset does not compute rates. Official suppression codes and confidence intervals are kept.

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 3 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 1 KB | in this repository |
| [`cancer_incidence_counts.csv`](data/cancer_incidence_counts.csv) | 19.0 MB | in this repository |
| [`cover.png`](data/cover.png) | 65 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 10 KB | in this repository |
| [`statcan_metadata_13-10-0747.csv`](data/statcan_metadata_13-10-0747.csv) | 19 KB | in this repository |
| `cancer_average_age_at_diagnosis.csv` | 66.0 MB (4.3 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-cancer-incidence-ccr--cancer_average_age_at_diagnosis.csv.gz) |
| `cancer_incidence_rates.csv` | 87.9 MB (4.4 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-cancer-incidence-ccr--cancer_incidence_rates.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

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
| `notes` | Text | — |

### `cancer_average_age_at_diagnosis.csv`

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `sex` | Text | Sex as published: Both sexes, Males or Females. |
| `primary_types_of_cancer_icd_o_3` | Text | Official primary cancer type, based on ICD-O-3 / SEER groups, as published. |
| `2021_census_population_structure` | Text | Official cube member naming the 2021 Census population structure used for age-standardization. |
| `characteristics` | Text | Official measure name as published in the cube. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Official status symbol: blank, x (suppressed) or .. (not available). These official suppression and availability codes are kept. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `ref_period` | Date | Reference period as published. |
| `year` | Integer | Diagnosis year. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `standard_population` | Text | final 2021 Canadian postcensal population structure, as stated in official table note 13. Filled only on rate rows. |
| `standardization_method` | Text | direct method, as stated in official table note 13. Filled only on rate rows. |
| `measure` | Text | Same as characteristics. Counts, age-standardized rates and average age are separate official measures. |

### `cancer_incidence_counts.csv`

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `sex` | Text | Sex as published: Both sexes, Males or Females. |
| `primary_types_of_cancer_icd_o_3` | Text | Official primary cancer type, based on ICD-O-3 / SEER groups, as published. |
| `2021_census_population_structure` | Text | Official cube member naming the 2021 Census population structure used for age-standardization. |
| `characteristics` | Text | Official measure name as published in the cube. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Official status symbol: blank, x (suppressed) or .. (not available). These official suppression and availability codes are kept. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `ref_period` | Date | Reference period as published. |
| `year` | Integer | Diagnosis year. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `standard_population` | Text | final 2021 Canadian postcensal population structure, as stated in official table note 13. Filled only on rate rows. |
| `standardization_method` | Text | direct method, as stated in official table note 13. Filled only on rate rows. |
| `measure` | Text | Same as characteristics. Counts, age-standardized rates and average age are separate official measures. |

### `cancer_incidence_rates.csv`

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Dissemination Geography Unique Identifier as published by Statistics Canada, when the source provides one. |
| `sex` | Text | Sex as published: Both sexes, Males or Females. |
| `primary_types_of_cancer_icd_o_3` | Text | Official primary cancer type, based on ICD-O-3 / SEER groups, as published. |
| `2021_census_population_structure` | Text | Official cube member naming the 2021 Census population structure used for age-standardization. |
| `characteristics` | Text | Official measure name as published in the cube. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Official status symbol: blank, x (suppressed) or .. (not available). These official suppression and availability codes are kept. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `ref_period` | Date | Reference period as published. |
| `year` | Integer | Diagnosis year. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `standard_population` | Text | final 2021 Canadian postcensal population structure, as stated in official table note 13. Filled only on rate rows. |
| `standardization_method` | Text | direct method, as stated in official table note 13. Filled only on rate rows. |
| `measure` | Text | Same as characteristics. Counts, age-standardized rates and average age are separate official measures. |

### `data_dictionary.csv`

| Column | Type | Description |
|---|---|---|
| `column` | Text | — |
| `file` | Text | — |
| `type` | Text | — |
| `description` | Text | — |

### `statcan_metadata_13-10-0747.csv`

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
@misc{khan2026canadacancerincidenceccr,
  author    = {Khan, John},
  title     = {Canada cancer incidence rates and counts},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-cancer-incidence-ccr}
}
```

APA: Khan, J. (2026). *Canada cancer incidence rates and counts* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-cancer-incidence-ccr

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Official cancer incidence counts and age-standardized rates for Canada, the provinces and the territories, tidied from [Table 13-10-0747-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310074701). Rates are the official Statistics Canada series, age-standardized by the direct method to the final 2021 Canadian postcensal population structure. Counts and rates are kept as separate measures. This dataset does not compute rates. Official suppression codes and confidence intervals are kept.

## Coverage

Diagnosis years 1992 to 2023 as published. Canada, the 10 provinces and the 3 territories. Official Canada and Nova Scotia figures for 2020 to 2023 are not available in the source table.

## Updates

This upload is a snapshot downloaded on 15 November 2026. The official table release date was 2026-02-27.

## A few numbers from this snapshot

* The package has 536,256 official rows for Canada, the 10 provinces and the 3 territories, matching the staged extract from table 13-10-0747. Geographies labelled as excluding a province or territory are not included.
* In 2019, the official age-standardized cancer incidence rate for Canada, both sexes, all primary sites of cancer, was 599.7 per 100,000 population, using the direct method and the final 2021 Canadian postcensal population structure.
* The same official Canada rate was 615.1 per 100,000 in 1992. Official Canada and Nova Scotia rates and counts for 2020 to 2023 are not available in this table because Nova Scotia data are not available for those diagnosis years (official note 20).
* Official case counts are randomly rounded to a multiple of 5. Official age-standardized rates and confidence intervals are calculated by Statistics Canada from the unrounded counts. This dataset does not compute rates.

## Example uses

* Use official age-standardized rates when comparing provinces or years.
* Use official counts with the random-rounding note in mind.
* Treat 2020 to 2023 Canada and Nova Scotia cells marked .. as not available, not as zero.

## Caveats

Do not compute rates from the rounded counts in this file. Official rates already exist and were calculated from unrounded counts. Cases with unknown age are excluded from this table, so counts may not match table 13-10-0111. Official Canada and Nova Scotia figures for 2020 to 2023 are not available because Nova Scotia data are not available for those years.

## Files

* `cancer_incidence_counts.csv`: Official number of new cancer cases from table 13-10-0747, for Canada, the provinces and the territories. Counts are randomly rounded by Statistics Canada. No rates are computed here.
* `cancer_incidence_rates.csv`: Official age-standardized cancer incidence rates and their 95% confidence intervals from table 13-10-0747. Rates use the direct method and the final 2021 Canadian postcensal population structure. These are official rates, not computed in this dataset.
* `cancer_average_age_at_diagnosis.csv`: Official average age at diagnosis and its 95% confidence intervals, as published in table 13-10-0747.
* `SOURCE_MANIFEST.csv`: Source table identifier, release date, retrieval date and checksum.
* `data_dictionary.csv`: Column dictionary.
* `METHODS.md`: Methods note, including the official standard population.
* `CITATION.txt`: Suggested citation, with DOI pending.
* `statcan_metadata_13-10-0747.csv`: Official Statistics Canada cube metadata for Table 13-10-0747-01, including notes on the standard population, random rounding and suppression.

## Licence

This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 13-10-0747. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Suggested citation: John Khan. 2026. Canada cancer incidence rates and counts [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-cancer-incidence-ccr. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
