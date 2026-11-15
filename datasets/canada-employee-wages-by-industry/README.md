<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada employee wages by industry" width="100%"></p>

# Canada employee wages by industry

*Annual average and median wages by industry, province, gender and age*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 1997 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-employee-wages-by-industry](https://www.kaggle.com/datasets/johnnykhan1/canada-employee-wages-by-industry)

## What it is

Canada employee wages by industry, tidied from Statistics Canada Table 14-10-0064-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [14-10-0064-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410006401).

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`average_weekly_wage_all_industries_by_province.csv`](data/average_weekly_wage_all_industries_by_province.csv) | 3 KB | in this repository |
| [`cover.png`](data/cover.png) | 73 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 9 KB | in this repository |
| `employee_wages_by_industry_long.csv` | 231.1 MB (15.1 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-employee-wages-by-industry--employee_wages_by_industry_long.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `average_weekly_wage_all_industries_by_province.csv`

Average weekly wage, all industries, both full- and part-time, 15 years and over, one column per province plus Canada.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `alberta` | Float | Published value for alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `british_columbia` | Float | Published value for british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `canada` | Float | Published value for canada. See unit_of_measure and scalar_factor in the long file for the unit. |
| `manitoba` | Float | Published value for manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |
| `new_brunswick` | Float | Published value for new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `newfoundland_and_labrador` | Float | Published value for newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nova_scotia` | Float | Published value for nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ontario` | Float | Published value for ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prince_edward_island` | Float | Published value for prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `quebec` | Float | Published value for quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatchewan` | Float | Published value for saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `employee_wages_by_industry_long.csv`

Tidy long file of annual employee wages by industry, geography, gender and age.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `wage_measure` | Text | Wage concept: number of employees, average hourly or weekly wage, or median hourly or weekly wage. |
| `type_of_work` | Text | Type of work covered by the permit (this file keeps the total). |
| `naics` | Text | Industry group based on the North American Industry Classification System, including sector totals. |
| `gender` | Text | Gender grouping published by the Labour Force Survey (Total - Gender, Men+ or Women+). |
| `age_group` | Text | Age group published by the Labour Force Survey. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series (for example v41690973). Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in statcan_table_metadata.csv. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata shipped with the table download, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 14-10-0064-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410006401. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/14100064-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaemployeewagesbyindustry,
  author    = {Khan, John},
  title     = {Canada employee wages by industry},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-employee-wages-by-industry}
}
```

APA: Khan, J. (2026). *Canada employee wages by industry* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-employee-wages-by-industry

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada employee wages by industry, tidied from Statistics Canada Table 14-10-0064-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [14-10-0064-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410006401).

## Coverage

The long file keeps the full published table: Canada and the ten provinces, five wage measures, three types of work, 19 industry groups, three gender groups and four age groups, annually from 1997 to 2025.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates this annual table once a year, in January. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* The average weekly wage in Canada for all industries, both full- and part-time employees, 15 years and over, was 1,329.77 dollars in 2025.
* The table is annual, from 1997 through 2025. Territories are not in this table.

## Example uses

* Compare average or median weekly wages across provinces for all industries.
* Look at wage levels in a specific industry such as construction, health care or professional services.
* Compare wages for Men+ and Women+, or for younger and older workers, in the same industry.

## Caveats

These are Labour Force Survey wage estimates, not payroll totals from the Survey of Employment, Payrolls and Hours. Some detailed industry, age and gender cells can be empty or marked with a quality symbol. Gender labels use Statistics Canada's Men+ and Women+ categories. Figures can be revised.

## Files

* `employee_wages_by_industry_long.csv`: Tidy long file of annual employee wages by industry, geography, gender and age.
* `average_weekly_wage_all_industries_by_province.csv`: Average weekly wage, all industries, both full- and part-time, 15 years and over, one column per province plus Canada.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 14-10-0064-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
