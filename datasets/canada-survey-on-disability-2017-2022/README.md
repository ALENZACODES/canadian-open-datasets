<p align="center"><img src="../../assets/theme-health.png" alt="Canada Survey on Disability, 2017 and 2022" width="100%"></p>

# Canada Survey on Disability, 2017 and 2022

*Prevalence, type, severity, work, education and income*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** 2017 to 2022 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-survey-on-disability-2017-2022](https://www.kaggle.com/datasets/johnnykhan1/canada-survey-on-disability-2017-2022)

## What it is

A tidy extract of six official Statistics Canada tables from the Canadian Survey on Disability (CSD) for 2017 and 2022. The tables cover the number and rate of persons with and without disabilities, severity, type of disability, labour force status, highest certificate, and after-tax income groups, by age group, gender, and province or territory.

Source tables:

* [13-10-0374-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037401): Persons with and without disabilities aged 15 years and over, by age group and gender.
* [13-10-0375-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037501): Severity of disability for persons with disabilities aged 15 years and over, by age group and gender.
* [13-10-0376-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037601): Type of disability for persons with disabilities aged 15 years and over, by age group and gender.
* [13-10-0377-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037701): Labour force status of persons with and without disabilities aged 15 years and over, by age group and gender.
* [13-10-0378-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037801): Highest certificate, diploma or degree for persons with and without disabilities aged 15 years and over, by severity, by age group and gender.
* [13-10-0379-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037901): After-tax total income for persons with and without disabilities aged 25 years and over, by severity, by age group and gender.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. Survey number 3251.

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 54 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 22 KB | in this repository |
| [`disability_prevalence.csv`](data/disability_prevalence.csv) | 2.8 MB | in this repository |
| [`disability_severity.csv`](data/disability_severity.csv) | 4.2 MB | in this repository |
| [`disability_type.csv`](data/disability_type.csv) | 6.3 MB | in this repository |
| [`educational_attainment.csv`](data/educational_attainment.csv) | 44.9 MB | in this repository |
| [`labour_force_status.csv`](data/labour_force_status.csv) | 14.0 MB | in this repository |
| [`official_metadata_13100374.csv`](data/official_metadata_13100374.csv) | 6 KB | in this repository |
| [`official_metadata_13100375.csv`](data/official_metadata_13100375.csv) | 8 KB | in this repository |
| [`official_metadata_13100376.csv`](data/official_metadata_13100376.csv) | 13 KB | in this repository |
| [`official_metadata_13100377.csv`](data/official_metadata_13100377.csv) | 9 KB | in this repository |
| [`official_metadata_13100378.csv`](data/official_metadata_13100378.csv) | 10 KB | in this repository |
| [`official_metadata_13100379.csv`](data/official_metadata_13100379.csv) | 9 KB | in this repository |
| [`prevalence_by_province.csv`](data/prevalence_by_province.csv) | 4 KB | in this repository |
| `after_tax_income_groups.csv` | 50.8 MB (2.7 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-survey-on-disability-2017-2022--after_tax_income_groups.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `after_tax_income_groups.csv`

Official CSD after-tax income group counts, rates and 95% confidence intervals, by disability status and severity, age group, gender and geography. Income is linked from the Census and refers to calendar years 2015 and 2020.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `disability` | Text | Disability status as published, including persons with disabilities, persons without disabilities, and (where the table has it) severity classes or the total population. |
| `after_tax_income_group` | Text | After-tax income group as published. For the 2022 CSD the official notes say the income year is 2020, linked from the 2021 Census. For the 2017 CSD the income year is 2015, linked from the 2016 Census. |
| `estimate_type` | Text | The kind of official figure: number of persons, percentage of persons, or the low or high 95% confidence interval for either of those. |
| `unit_of_measure` | Text | Unit of measure for value, as published (Number or Percent). |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so a number of persons is already in persons and a percentage is already in percent. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. E means use with caution. F means too unreliable to be published. .. means not available for a specific reference period. See the symbol legend in the official metadata files. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `disability_prevalence.csv`

Official CSD counts, rates and 95% confidence intervals for persons with and without disabilities, by age group, gender and geography, 2017 and 2022.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `disability` | Text | Disability status as published, including persons with disabilities, persons without disabilities, and (where the table has it) severity classes or the total population. |
| `estimate_type` | Text | The kind of official figure: number of persons, percentage of persons, or the low or high 95% confidence interval for either of those. |
| `unit_of_measure` | Text | Unit of measure for value, as published (Number or Percent). |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so a number of persons is already in persons and a percentage is already in percent. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. E means use with caution. F means too unreliable to be published. .. means not available for a specific reference period. See the symbol legend in the official metadata files. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `disability_severity.csv`

Official CSD counts, rates and 95% confidence intervals by global severity class, age group, gender and geography, 2017 and 2022.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `severity_of_disability` | Text | Official global severity class as published: persons with disabilities, all severity levels; Mild; Moderate; Severe; or Very severe. The official notes say the class names are a grouping of the global severity score, not a judgement about a person. |
| `estimate_type` | Text | The kind of official figure: number of persons, percentage of persons, or the low or high 95% confidence interval for either of those. |
| `unit_of_measure` | Text | Unit of measure for value, as published (Number or Percent). |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so a number of persons is already in persons and a percentage is already in percent. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. E means use with caution. F means too unreliable to be published. .. means not available for a specific reference period. See the symbol legend in the official metadata files. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `disability_type.csv`

Official CSD counts, rates and 95% confidence intervals by disability type, age group, gender and geography, 2017 and 2022.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `disability_type` | Text | Official disability type as published, or the total population with disabilities. A person may have more than one type. |
| `estimate_type` | Text | The kind of official figure: number of persons, percentage of persons, or the low or high 95% confidence interval for either of those. |
| `unit_of_measure` | Text | Unit of measure for value, as published (Number or Percent). |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so a number of persons is already in persons and a percentage is already in percent. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. E means use with caution. F means too unreliable to be published. .. means not available for a specific reference period. See the symbol legend in the official metadata files. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `educational_attainment.csv`

Official CSD counts, rates and 95% confidence intervals of highest certificate, diploma or degree, by disability status and severity, age group, gender and geography, 2017 and 2022.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `disability` | Text | Disability status as published, including persons with disabilities, persons without disabilities, and (where the table has it) severity classes or the total population. |
| `highest_certificate` | Text | Highest certificate, diploma or degree as published, including the official total and a not specified category. |
| `estimate_type` | Text | The kind of official figure: number of persons, percentage of persons, or the low or high 95% confidence interval for either of those. |
| `unit_of_measure` | Text | Unit of measure for value, as published (Number or Percent). |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so a number of persons is already in persons and a percentage is already in percent. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. E means use with caution. F means too unreliable to be published. .. means not available for a specific reference period. See the symbol legend in the official metadata files. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `labour_force_status.csv`

Official CSD labour force status counts, rates and 95% confidence intervals by disability status, age group, gender and geography. Labour force status comes from the 2016 and 2021 Census reference weeks.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `disability` | Text | Disability status as published, including persons with disabilities, persons without disabilities, and (where the table has it) severity classes or the total population. |
| `labour_force_status` | Text | Labour force status as published: total, in the labour force, employed, unemployed, not in labour force, or not specified. The official notes say these figures come from the 2016 and 2021 Census reference weeks, not from a CSD labour question, and that the unemployed percentage is not an unemployment rate. |
| `estimate_type` | Text | The kind of official figure: number of persons, percentage of persons, or the low or high 95% confidence interval for either of those. |
| `unit_of_measure` | Text | Unit of measure for value, as published (Number or Percent). |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so a number of persons is already in persons and a percentage is already in percent. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. |
| `status` | Boolean | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. E means use with caution. F means too unreliable to be published. .. means not available for a specific reference period. See the symbol legend in the official metadata files. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_13100374.csv`

Official Statistics Canada metadata, notes and symbol legend for table 13-10-0374-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. Later rows in this file hold the dimension and note sections of the official metadata download. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

### `official_metadata_13100375.csv`

Official Statistics Canada metadata, notes and symbol legend for table 13-10-0375-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. Later rows in this file hold the dimension and note sections of the official metadata download. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

### `official_metadata_13100376.csv`

Official Statistics Canada metadata, notes and symbol legend for table 13-10-0376-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. Later rows in this file hold the dimension and note sections of the official metadata download. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

### `official_metadata_13100377.csv`

Official Statistics Canada metadata, notes and symbol legend for table 13-10-0377-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. Later rows in this file hold the dimension and note sections of the official metadata download. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

### `official_metadata_13100378.csv`

Official Statistics Canada metadata, notes and symbol legend for table 13-10-0378-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. Later rows in this file hold the dimension and note sections of the official metadata download. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

### `official_metadata_13100379.csv`

Official Statistics Canada metadata, notes and symbol legend for table 13-10-0379-01.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. Later rows in this file hold the dimension and note sections of the official metadata download. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

### `prevalence_by_province.csv`

Convenience summary of official prevalence counts and rates for persons aged 15 years and over, total gender, by geography, 2017 and 2022. Built from disability_prevalence.csv, not a separate official table.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Canadian Survey on Disability, stored as January 1 of that year (2017-01-01 or 2022-01-01). Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population. Age is calculated as of Census day in the previous year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the ten provinces, the three territories, and official regional groupings (Atlantic provinces, Prairie provinces, Territories). |
| `age_group` | Text | Age group as published in this official table. Age is calculated as of Census day in the previous year. |
| `gender` | Text | Gender grouping as published: Total, gender; Men+; or Women+. The official notes say gender was not collected in 2017, so the 2017 sex variable is combined with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons. |
| `n_persons_with_disabilities` | Float | Official number of persons with disabilities in this geography, year, age group and gender (estimate type Number of persons). Taken from disability_prevalence.csv, not a separate official table. |
| `n_total_population` | Float | Official number of persons in the total population with and without disabilities in this geography, year, age group and gender. Taken from disability_prevalence.csv, not a separate official table. |
| `percent` | Float | Official percentage of persons with disabilities in this geography, year, age group and gender. Taken from disability_prevalence.csv, not a separate official table. |
| `percent_ci_low` | Float | Official low 95% confidence interval for the percentage of persons with disabilities. |
| `percent_ci_high` | Float | Official high 95% confidence interval for the percentage of persons with disabilities. |
| `status_percent` | Text | Official status symbol on the percentage of persons with disabilities. Empty means a regular published value. |

## Source and licence

**Source:** Statistics Canada, Canadian Survey on Disability, 2017 and 2022 (survey 3251). Official tables 13-10-0374-01 to 13-10-0379-01, downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 13-10-0374-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037401, https://www150.statcan.gc.ca/n1/tbl/csv/13100374-eng.zip) 13-10-0375-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037501, https://www150.statcan.gc.ca/n1/tbl/csv/13100375-eng.zip) 13-10-0376-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037601, https://www150.statcan.gc.ca/n1/tbl/csv/13100376-eng.zip) 13-10-0377-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037701, https://www150.statcan.gc.ca/n1/tbl/csv/13100377-eng.zip) 13-10-0378-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037801, https://www150.statcan.gc.ca/n1/tbl/csv/13100378-eng.zip) 13-10-0379-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037901, https://www150.statcan.gc.ca/n1/tbl/csv/13100379-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadasurveyondisability20172022,
  author    = {Khan, John},
  title     = {Canada Survey on Disability, 2017 and 2022},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-survey-on-disability-2017-2022}
}
```

APA: Khan, J. (2026). *Canada Survey on Disability, 2017 and 2022* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-survey-on-disability-2017-2022

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of six official Statistics Canada tables from the Canadian Survey on Disability (CSD) for 2017 and 2022. The tables cover the number and rate of persons with and without disabilities, severity, type of disability, labour force status, highest certificate, and after-tax income groups, by age group, gender, and province or territory.

Source tables:

* [13-10-0374-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037401): Persons with and without disabilities aged 15 years and over, by age group and gender.
* [13-10-0375-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037501): Severity of disability for persons with disabilities aged 15 years and over, by age group and gender.
* [13-10-0376-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037601): Type of disability for persons with disabilities aged 15 years and over, by age group and gender.
* [13-10-0377-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037701): Labour force status of persons with and without disabilities aged 15 years and over, by age group and gender.
* [13-10-0378-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037801): Highest certificate, diploma or degree for persons with and without disabilities aged 15 years and over, by severity, by age group and gender.
* [13-10-0379-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310037901): After-tax total income for persons with and without disabilities aged 25 years and over, by severity, by age group and gender.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. Survey number 3251.

## Coverage

Each official table has the two survey years 2017 and 2022, and 17 official geographies: Canada, the ten provinces, the three territories, and the official regional groupings Atlantic provinces, Prairie provinces and Territories.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. The Canadian Survey on Disability is conducted every 5 years. For a later release, use the official Statistics Canada tables.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case. Official values, quality symbols and suppressed cells were not altered. Rows with a letter F (too unreliable to be published) or ".." (not available for a specific reference period) are kept, with the value left blank. prevalence_by_province.csv is a convenience summary of the prevalence table, not a separate official table.

## A few numbers from this snapshot

* In 2022, 7,977,610 persons aged 15 years and over in Canada had a disability, or 27.0% of that population (95% confidence interval 26.6% to 27.3%).
* In 2017 the same official figure was 6,246,640 persons, or 22.3%.
* In 2022 the rate was 29.9% among Women+ and 23.9% among Men+.
* The 2022 rate was 20.1% at ages 15 to 24 years and 40.4% at ages 65 years and over.
* Among the provinces, the 2022 rate was highest in Nova Scotia at 37.9% and lowest in Quebec at 21.0%. Among the territories it was 19.3% in Nunavut and 31.4% in Yukon.
* Among persons with disabilities aged 25 to 64 years, 61.8% were employed in the 2021 Census reference week used by this table, compared with 77.8% of persons without disabilities.
* Among persons with disabilities aged 15 years and over in 2022, 39.0% were in the mild severity class and 21.1% were in the very severe class.
* Among the same group, the most common official disability types were pain-related (61.8%), flexibility (40.3%), mobility (39.2%) and mental health-related (38.6%). A person may have more than one type, so these shares do not add to 100%.
* Among persons with disabilities aged 25 years and over, 19.7% were in the $20,000 to $29,999 after-tax income group, and 3.6% were in the $100,000 or more group, compared with 15.0% and 7.2% of persons without disabilities. The 2022 CSD income figures are linked from the 2021 Census and refer to calendar year 2020.

## Example uses

* Compare official disability rates by province or territory and by age group in 2017 and 2022.
* Look at employment for persons with and without disabilities, after reading the official note that labour force status comes from the Census reference week, not from a 2017 or 2022 CSD labour question, and that the unemployed percentage in the table is not an unemployment rate.
* Compare after-tax income groups and educational attainment by disability status and severity.

## Caveats

The survey population is Canadians aged 15 years and over living in private dwellings. It excludes people living in institutions and other collective dwellings, on Canadian Armed Force bases, and on First Nations reserves.

The CSD identifies persons with disabilities using the Disability Screening Questions, which follow the social model of disability. Only persons who report a limitation in day-to-day activities are identified as having a disability. See the official [Canadian Survey on Disability, 2022: Concepts and Methods Guide](https://www150.statcan.gc.ca/n1/pub/89-654-x/89-654-x2023004-eng.htm).

Age is calculated as of Census day in the previous year. Collection took place in 2017 and 2022 for a sample selected from the 2016 and 2021 Census population.

Gender was not collected in the 2017 CSD. The official tables combine the 2017 sex variable with the 2022 two-category gender variable. Men+ includes men and some non-binary persons. Women+ includes women and some non-binary persons.

Estimates flagged E should be used with caution. Estimates flagged F are too unreliable to be published and have a blank value in this extract. Official 95% confidence intervals are included.

The sum of category values may differ from the total because of rounding.

Labour force status in table 13-10-0377-01 comes from the 2016 and 2021 Census of Population, not from the CSD questionnaires. The data reflect the Census reference weeks of May 1 to May 7, 2016 and May 2 to May 8, 2021. The official table notes that the percentages for unemployed are not unemployment rates.

After-tax income in table 13-10-0379-01 is linked from the Census. For the 2022 CSD the income year is 2020. For the 2017 CSD the income year is 2015.

Severity classes are a grouping of an official global severity score. The official notes say the class names are not a judgement about a person, only a way to order the score.

This extract does not include the later CSD labour-detail tables 13-10-0882-01 to 13-10-0898-01.

## Files

* `disability_prevalence.csv`: tidy extract of table 13-10-0374-01.
* `disability_severity.csv`: tidy extract of table 13-10-0375-01.
* `disability_type.csv`: tidy extract of table 13-10-0376-01.
* `labour_force_status.csv`: tidy extract of table 13-10-0377-01.
* `educational_attainment.csv`: tidy extract of table 13-10-0378-01.
* `after_tax_income_groups.csv`: tidy extract of table 13-10-0379-01.
* `prevalence_by_province.csv`: convenience summary of official prevalence counts and rates by geography for persons aged 15 years and over, total gender, in 2017 and 2022.
* `data_dictionary.csv`: column dictionary for the files in this extract.
* `official_metadata_13100374.csv` through `official_metadata_13100379.csv`: official Statistics Canada table metadata, notes and symbol legend for each source table.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, Canadian Survey on Disability, 2017 and 2022, tables 13-10-0374-01 to 13-10-0379-01. The published values were not changed. Columns were renamed and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
