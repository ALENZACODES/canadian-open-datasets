<p align="center"><img src="../../assets/theme-health.png" alt="Canada disability income, poverty and work" width="100%"></p>

# Canada disability income, poverty and work

*Income, poverty rates and labour market results by disability status*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** January 2013 to January 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-disability-income-poverty-and-work](https://www.kaggle.com/datasets/johnnykhan1/canada-disability-income-poverty-and-work)

## What it is

How people with disabilities fare on income, poverty and work in Canada, tidied from three Statistics Canada tables: [Table 11-10-0088-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110008801) and [Table 11-10-0090-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110009001) from the Canadian Income Survey, and [Table 14-10-0477-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410047701) from the Labour Force Survey disability questions.

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 8 KB | in this repository |
| [`income_by_disability_status_annual.csv`](data/income_by_disability_status_annual.csv) | 9.6 MB | in this repository |
| [`labour_market_by_disability_status_annual.csv`](data/labour_market_by_disability_status_annual.csv) | 10.0 MB | in this repository |
| [`low_income_by_disability_status_annual.csv`](data/low_income_by_disability_status_annual.csv) | 1.1 MB | in this repository |
| [`statcan_metadata_11-10-0088.csv`](data/statcan_metadata_11-10-0088.csv) | 10 KB | in this repository |
| [`statcan_metadata_11-10-0090.csv`](data/statcan_metadata_11-10-0090.csv) | 10 KB | in this repository |
| [`statcan_metadata_14-10-0477.csv`](data/statcan_metadata_14-10-0477.csv) | 12 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `income_by_disability_status_annual.csv`

Annual income of individuals by disability status, age group, gender and income source (aggregate, average, median, counts), Canada, from Table 11-10-0088.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `disability_status` | Text | Disability status as published. |
| `age_group` | Text | Age group as published. |
| `gender` | Text | Gender as published. |
| `income_source` | Text | Income source as published. |
| `statistic` | Text | Statistic as published. |
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
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `labour_market_by_disability_status_annual.csv`

Annual labour market indicators (employment, participation and unemployment rates, wages, hours) for persons with and without disabilities, by region, gender, age and education or immigrant status, estimates only, from Table 14-10-0477.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `labour_market_indicators` | Text | Labour market indicators as published. |
| `statistic` | Text | Statistic as published. |
| `gender` | Text | Gender as published. |
| `disability` | Text | Disability as published. |
| `age_group` | Text | Age group as published. |
| `socio_demographic_characteristics` | Text | Socio demographic characteristics as published. |
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

### `low_income_by_disability_status_annual.csv`

Annual poverty and low income statistics by disability status, age and gender, family type and low income line, Canada, from Table 11-10-0090.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `disability_status` | Text | Disability status as published. |
| `age_group_and_gender` | Text | Age group and gender as published. |
| `economic_family_type` | Text | Economic family type as published. |
| `low_income_lines` | Text | Low income lines as published. |
| `statistic` | Text | Statistic as published. |
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
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_11-10-0088.csv`

Official Statistics Canada cube metadata shipped with Table 11-10-0088-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `statcan_metadata_11-10-0090.csv`

Official Statistics Canada cube metadata shipped with Table 11-10-0090-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `statcan_metadata_14-10-0477.csv`

Official Statistics Canada cube metadata shipped with Table 14-10-0477-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 11-10-0088-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110008801); Statistics Canada Table 11-10-0090-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110009001); Statistics Canada Table 14-10-0477-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410047701); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadadisabilityincomepovertyandwork,
  author    = {Khan, John},
  title     = {Canada disability income, poverty and work},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-disability-income-poverty-and-work}
}
```

APA: Khan, J. (2026). *Canada disability income, poverty and work* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-disability-income-poverty-and-work

<details><summary>Full notes from the Kaggle page</summary>

## What this is

How people with disabilities fare on income, poverty and work in Canada, tidied from three Statistics Canada tables: [Table 11-10-0088-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110008801) and [Table 11-10-0090-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110009001) from the Canadian Income Survey, and [Table 14-10-0477-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410047701) from the Labour Force Survey disability questions.

## Coverage

Income and poverty 2013 to 2024, Canada. Labour market 2022 to 2025, Canada and regions. For the labour market table only the point estimates were kept; standard errors and confidence bounds are in the source.

## Updates

Updated yearly at the source. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Median total income was 38,100 dollars for people with disabilities and 50,900 dollars for people without, in 2024 (2024 constant dollars).
* Using the 2023 base Market Basket Measure, 12.6 percent of people with disabilities lived in poverty in 2024, against 8.4 percent of people without disabilities.
* The employment rate for people aged 25 to 64 was 67.0 percent with a disability and 82.9 percent without, in 2025.
* Files: income 44,160 rows (2013 to 2024), poverty 4,320 rows, labour market 44,712 rows (2022 to 2025).

## Example uses

* Measure the income and poverty gap for people with disabilities.
* Track the employment gap by age, gender and education.
* Support work on the Canada Disability Benefit and accessibility policy.
* Compare government transfer reliance by disability status.

## Caveats

Estimates come from sample surveys and carry sampling error; check status flags for quality. Income values are in 2024 constant dollars. The labour market series only start in 2022. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `income_by_disability_status_annual.csv`: Annual income of individuals by disability status, age group, gender and income source (aggregate, average, median, counts), Canada, from Table 11-10-0088.
* `low_income_by_disability_status_annual.csv`: Annual poverty and low income statistics by disability status, age and gender, family type and low income line, Canada, from Table 11-10-0090.
* `labour_market_by_disability_status_annual.csv`: Annual labour market indicators (employment, participation and unemployment rates, wages, hours) for persons with and without disabilities, by region, gender, age and education or immigrant status, estimates only, from Table 14-10-0477.
* `statcan_metadata_11-10-0088.csv`: Official cube metadata for Table 11-10-0088-01, as published.
* `statcan_metadata_11-10-0090.csv`: Official cube metadata for Table 11-10-0090-01, as published.
* `statcan_metadata_14-10-0477.csv`: Official cube metadata for Table 14-10-0477-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 11-10-0088-01, Table 11-10-0090-01, Table 14-10-0477-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
