<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada Household Spending, 2010 to 2023" width="100%"></p>

# Canada Household Spending, 2010 to 2023

*Average spending per household by category, province, income and type*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 2010 to 2023 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-household-spending-survey](https://www.kaggle.com/datasets/johnnykhan1/canada-household-spending-survey)

## What it is

A tidy extract of three official Statistics Canada tables from the Survey of Household Spending: how much the average Canadian household spends in a year on food, shelter, transportation, taxes, insurance, gifts and about 360 categories and items in total, by province, by before-tax income quintile and by household type.

Source tables:

* [11-10-0222-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022201): Household spending, Canada, regions and provinces.
* [11-10-0223-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022301): Household spending by household income quintile, Canada, regions and provinces.
* [11-10-0224-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022401): Household spending by household type.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. Reference years are 2010 to 2017, then 2019, 2021 and 2023, since the survey has run every two years from 2017.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 75 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 13 KB | in this repository |
| [`household_spending_by_household_type.csv`](data/household_spending_by_household_type.csv) | 5.3 MB | in this repository |
| [`household_spending_by_province.csv`](data/household_spending_by_province.csv) | 8.5 MB | in this repository |
| [`official_metadata_11100222.csv`](data/official_metadata_11100222.csv) | 29 KB | in this repository |
| [`official_metadata_11100223.csv`](data/official_metadata_11100223.csv) | 30 KB | in this repository |
| [`official_metadata_11100224.csv`](data/official_metadata_11100224.csv) | 29 KB | in this repository |
| `household_spending_by_income_quintile.csv` | 55.8 MB (6.8 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-household-spending-survey--household_spending_by_income_quintile.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `household_spending_by_household_type.csv`

Official average expenditure per household from the Survey of Household Spending, in dollars, for the same 363 categories, split by household type (all classes, one person households, couples with and without children, lone-parent households and other households), Canada only. Reference years 2010 to 2017, then 2019, 2021 and 2023.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Survey of Household Spending, stored as January 1 of that year (2023-01-01 is the 2023 reference year). The survey ran every year from 2010 to 2017 and every two years since, so 2018, 2020 and 2022 do not exist. |
| `geo` | Text | Geography as published: Canada, Atlantic Region, Prairie Region and the ten provinces. The official notes say Canada level figures cover the 10 provinces only; the territories are not included. The household type file has Canada only. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `household_type` | Text | household_spending_by_household_type.csv only. Household type as published: All classes, One person households, Couples without children, Couples with children, Couples with other related or unrelated persons, Lone-parent households with no additional persons, or Other households with related or unrelated persons. |
| `statistic` | Text | Statistic as published. Average expenditure per household in every row. |
| `expenditure_category` | Text | Spending category exactly as published, from Total expenditure down to detailed items such as Rent or Restaurant meals. Categories are nested, so do not add a category to the categories it belongs to. |
| `category_member_id` | Text | Official member ID of the spending category in the table metadata, also the last part of coordinate. Added here from the official metadata, not a separate official column. |
| `parent_category` | Text | The category this category belongs to, from the official metadata parent member ID (for example Food purchased from stores belongs to Food expenditures). Empty for Total expenditure. Added here, not a separate official column. |
| `category_level` | Integer | Depth of the category in the official hierarchy: 0 for Total expenditure, 1 for Total current consumption, Income taxes, Personal insurance payments and pension contributions, and Gifts of money, support payments and charitable contributions, 2 for the main consumption groups such as Food expenditures or Shelter, and so on down to 7. Added here from the official metadata, not a separate official column. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars in every row. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: units in every row, so 105367 means 105,367 dollars per household per year. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | Average expenditure per household in dollars for the reference year, as published. Empty when Statistics Canada did not publish a figure (status F or ..). Discounts and refunds is published as a negative amount. Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. F means too unreliable to be published (the official notes say estimates with a coefficient of variation of 35% or more are suppressed) and .. means not available for that reference year; for both the value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. 64 categories are terminated in this snapshot, with their last values in 2019 or earlier, mostly because the 2019 questionnaire combined or dropped some items. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `household_spending_by_income_quintile.csv`

Official average expenditure per household from the Survey of Household Spending, in dollars, for the same 363 categories, split by before-tax household income quintile (all quintiles, lowest to highest), for Canada, the Atlantic and Prairie regions and each province. Reference years 2010 to 2017, then 2019, 2021 and 2023.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Survey of Household Spending, stored as January 1 of that year (2023-01-01 is the 2023 reference year). The survey ran every year from 2010 to 2017 and every two years since, so 2018, 2020 and 2022 do not exist. |
| `geo` | Text | Geography as published: Canada, Atlantic Region, Prairie Region and the ten provinces. The official notes say Canada level figures cover the 10 provinces only; the territories are not included. The household type file has Canada only. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `income_quintile` | Text | household_spending_by_income_quintile.csv only. Before-tax household income quintile as published: All quintiles, Lowest quintile, Second quintile, Third quintile, Fourth quintile or Highest quintile. Each quintile holds one fifth of households in that geography and year. |
| `statistic` | Text | Statistic as published. Average expenditure per household in every row. |
| `expenditure_category` | Text | Spending category exactly as published, from Total expenditure down to detailed items such as Rent or Restaurant meals. Categories are nested, so do not add a category to the categories it belongs to. |
| `category_member_id` | Text | Official member ID of the spending category in the table metadata, also the last part of coordinate. Added here from the official metadata, not a separate official column. |
| `parent_category` | Text | The category this category belongs to, from the official metadata parent member ID (for example Food purchased from stores belongs to Food expenditures). Empty for Total expenditure. Added here, not a separate official column. |
| `category_level` | Integer | Depth of the category in the official hierarchy: 0 for Total expenditure, 1 for Total current consumption, Income taxes, Personal insurance payments and pension contributions, and Gifts of money, support payments and charitable contributions, 2 for the main consumption groups such as Food expenditures or Shelter, and so on down to 7. Added here from the official metadata, not a separate official column. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars in every row. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: units in every row, so 105367 means 105,367 dollars per household per year. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | Average expenditure per household in dollars for the reference year, as published. Empty when Statistics Canada did not publish a figure (status F or ..). Discounts and refunds is published as a negative amount. Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. F means too unreliable to be published (the official notes say estimates with a coefficient of variation of 35% or more are suppressed) and .. means not available for that reference year; for both the value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. 64 categories are terminated in this snapshot, with their last values in 2019 or earlier, mostly because the 2019 questionnaire combined or dropped some items. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `household_spending_by_province.csv`

Official average expenditure per household from the Survey of Household Spending, in dollars, for 363 spending categories from total expenditure down to detailed items, for Canada (ten provinces), the Atlantic and Prairie regions and each province. Reference years 2010 to 2017, then 2019, 2021 and 2023.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the Survey of Household Spending, stored as January 1 of that year (2023-01-01 is the 2023 reference year). The survey ran every year from 2010 to 2017 and every two years since, so 2018, 2020 and 2022 do not exist. |
| `geo` | Text | Geography as published: Canada, Atlantic Region, Prairie Region and the ten provinces. The official notes say Canada level figures cover the 10 provinces only; the territories are not included. The household type file has Canada only. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `statistic` | Text | Statistic as published. Average expenditure per household in every row. |
| `expenditure_category` | Text | Spending category exactly as published, from Total expenditure down to detailed items such as Rent or Restaurant meals. Categories are nested, so do not add a category to the categories it belongs to. |
| `category_member_id` | Text | Official member ID of the spending category in the table metadata, also the last part of coordinate. Added here from the official metadata, not a separate official column. |
| `parent_category` | Text | The category this category belongs to, from the official metadata parent member ID (for example Food purchased from stores belongs to Food expenditures). Empty for Total expenditure. Added here, not a separate official column. |
| `category_level` | Integer | Depth of the category in the official hierarchy: 0 for Total expenditure, 1 for Total current consumption, Income taxes, Personal insurance payments and pension contributions, and Gifts of money, support payments and charitable contributions, 2 for the main consumption groups such as Food expenditures or Shelter, and so on down to 7. Added here from the official metadata, not a separate official column. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars in every row. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: units in every row, so 105367 means 105,367 dollars per household per year. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | Average expenditure per household in dollars for the reference year, as published. Empty when Statistics Canada did not publish a figure (status F or ..). Discounts and refunds is published as a negative amount. Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. F means too unreliable to be published (the official notes say estimates with a coefficient of variation of 35% or more are suppressed) and .. means not available for that reference year; for both the value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. 64 categories are terminated in this snapshot, with their last values in 2019 or earlier, mostly because the 2019 questionnaire combined or dropped some items. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_11100222.csv`

Official Statistics Canada metadata, notes, category list and symbol legend for table 11-10-0222-01.

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

### `official_metadata_11100223.csv`

Official Statistics Canada metadata, notes, category list and symbol legend for table 11-10-0223-01.

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

### `official_metadata_11100224.csv`

Official Statistics Canada metadata, notes, category list and symbol legend for table 11-10-0224-01.

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

## Source and licence

**Source:** Statistics Canada, Survey of Household Spending. Official tables downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 11-10-0222-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022201, https://www150.statcan.gc.ca/n1/tbl/csv/11100222-eng.zip) 11-10-0223-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022301, https://www150.statcan.gc.ca/n1/tbl/csv/11100223-eng.zip) 11-10-0224-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022401, https://www150.statcan.gc.ca/n1/tbl/csv/11100224-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahouseholdspendingsurvey,
  author    = {Khan, John},
  title     = {Canada Household Spending, 2010 to 2023},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-household-spending-survey}
}
```

APA: Khan, J. (2026). *Canada Household Spending, 2010 to 2023* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-household-spending-survey

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of three official Statistics Canada tables from the Survey of Household Spending: how much the average Canadian household spends in a year on food, shelter, transportation, taxes, insurance, gifts and about 360 categories and items in total, by province, by before-tax income quintile and by household type.

Source tables:

* [11-10-0222-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022201): Household spending, Canada, regions and provinces.
* [11-10-0223-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022301): Household spending by household income quintile, Canada, regions and provinces.
* [11-10-0224-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022401): Household spending by household type.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. Reference years are 2010 to 2017, then 2019, 2021 and 2023, since the survey has run every two years from 2017.

## Files

* household_spending_by_province.csv: 44,265 rows. 363 categories in 13 geographies over 11 reference years.
* household_spending_by_income_quintile.csv: 265,590 rows. The same categories and geographies for all households and each income quintile.
* household_spending_by_household_type.csv: 23,835 rows. The same categories for Canada, for all households and six household types.
* data_dictionary.csv: every column in every file, with its type and meaning.
* official_metadata_*.csv: the official Statistics Canada notes, category list with parent members, corrections and symbol legend for each table.

Each file adds three columns from the official metadata to make the category tree easy to use: category_member_id, parent_category and category_level.

## A few numbers from this snapshot

Average per household, Canada (ten provinces), current dollars, 2023 reference year unless stated.

* Total expenditure was 105,367 dollars in 2023, against 72,075 dollars in 2010. Total current consumption was 76,146 dollars and income taxes were 21,545 dollars.
* Shelter took 24,501 dollars, transportation 12,019 dollars and food 11,933 dollars.
* Households in the lowest income quintile spent 40,091 dollars on current consumption, against 122,479 dollars for the highest quintile.
* Total expenditure was 113,576 dollars in Ontario, 94,321 dollars in Quebec and 116,577 dollars in Alberta.
* One person households had total expenditure of 62,584 dollars and couples with children 153,447 dollars.
* For Canada, Total expenditure equals the sum of its four direct parts, and Total current consumption equals the sum of its main groups, within 2 dollars of rounding in every year.

## Caveats

* These are averages over all households in a group, including households that spent nothing on an item, so an item average is not the typical spending of the households that buy it.
* Values are in current dollars, not adjusted for inflation.
* Categories are nested. Use parent_category and category_level to pick one level before summing, and never add a category to its parent.
* The official notes say the 2019 questionnaire was streamlined, so some series were combined or dropped from 2019 and some 2019 estimates are not directly comparable to earlier years. 64 categories are terminated (terminated is t) with no values after 2019.
* Survey weights use 2011 Census projections for 2010 to 2016, 2016 Census projections for 2017 to 2021 and 2021 Census projections from 2023.
* Canada level figures cover the ten provinces only. Territorial spending for 2012 is in a separate table, 11-10-0126-01.
* Many detailed cells, especially by quintile and in smaller provinces, are suppressed as too unreliable (status F, a coefficient of variation of 35% or more), so values are empty there.
* Discounts and refunds is published as a negative amount, which lowers the total it belongs to.
* From 2014, provincial health insurance premiums are counted with income taxes, not health care. Other official notes on registration fees and insurance premiums in some provinces are in the metadata files.

## Example uses

* Build household budget shares by income quintile or province and track how they changed from 2010 to 2023.
* Compare shelter, transportation and food spending across provinces.
* Weight price changes with real household spending patterns for different income groups.
* Study how taxes, pension contributions and gifts compare with consumption across the income distribution.
* Join with John Khan's Canada CPI by item and province, low income and income inequality, and household debt and wealth datasets on Kaggle.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. Statistics Canada runs the survey every two years.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case and reference years were stored as dates. Three columns (category_member_id, parent_category, category_level) were added from the official metadata. Official values, labels and status symbols were not altered, and every official row was kept.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, Survey of Household Spending, tables 11-10-0222-01, 11-10-0223-01 and 11-10-0224-01. The published values were not changed. Columns were renamed and added and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
