<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada Household Debt, Debt Service and Wealth" width="100%"></p>

# Canada Household Debt, Debt Service and Wealth

*Debt to income, debt service ratios and wealth by quintile, 1990 to 2026*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** 1990 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-household-debt-and-wealth](https://www.kaggle.com/datasets/johnnykhan1/canada-household-debt-and-wealth)

## What it is

A tidy extract of three official Statistics Canada tables on household debt and household finances. Together they show how much Canadian households owe, how that debt compares with their income, how much of their income goes to interest and principal payments, and how assets, debts and net worth are spread across income and wealth quintiles, age groups, homeowners and renters, and generations.

Source tables:

* [38-10-0238-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810023801): Household sector credit market summary table, seasonally adjusted estimates.
* [11-10-0065-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110006501): Debt service indicators of households, national balance sheet accounts.
* [36-10-0660-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610066001): Distributions of household economic accounts, wealth, by characteristic, Canada, quarterly.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The credit market and debt service tables run from the first quarter of 1990 to the second quarter of 2026. The wealth distribution table runs from 2010 to the fourth quarter of 2025.

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 65 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 10 KB | in this repository |
| [`household_credit_market_summary.csv`](data/household_credit_market_summary.csv) | 179 KB | in this repository |
| [`household_debt_service_indicators.csv`](data/household_debt_service_indicators.csv) | 1.2 MB | in this repository |
| [`household_wealth_distribution.csv`](data/household_wealth_distribution.csv) | 18.1 MB | in this repository |
| [`official_metadata_11100065.csv`](data/official_metadata_11100065.csv) | 3 KB | in this repository |
| [`official_metadata_36100660.csv`](data/official_metadata_36100660.csv) | 9 KB | in this repository |
| [`official_metadata_38100238.csv`](data/official_metadata_38100238.csv) | 2 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `household_credit_market_summary.csv`

Official quarterly household sector credit market summary for Canada, seasonally adjusted: credit market debt to disposable income, consumer credit and mortgage liabilities to disposable income, outstanding credit market debt, consumer credit, non-mortgage loans and mortgages from the national balance sheet, and the matching financial flows (net new borrowing in the quarter). Ratios in units, dollar values in millions. First quarter of 1990 to second quarter of 2026.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference quarter stored as the first day of the quarter (1990-01-01 is the first quarter of 1990, 2026-04-01 is the second quarter of 2026). Balance sheet stocks are at the end of that quarter. In household_wealth_distribution.csv the published quarters are the fourth quarter of each year from 2010 to 2019 and every quarter from 2020 to 2025; other quarters before 2020 are kept with status .. and an empty value. |
| `geo` | Text | Geography as published. Canada only in all three files. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for Canada (2021A000011124). |
| `credit_category` | Text | household_credit_market_summary.csv only. Line as published: Credit market debt to disposable income; Consumer credit and mortgage liabilities to disposable income; Credit market debt, Consumer credit, Non-mortgage loans and Mortgages from the national balance sheet (amount owed at the end of the quarter); and the same four lines as a financial flow (net change from transactions in the quarter, at quarterly rates). |
| `unit_of_measure` | Text | Unit of measure for value, as published: Ratio, Dollars or Percent. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: millions for total dollar values, units for ratios, percentages and per household dollar values. A total dollar value of 1000 means 1,000 million dollars. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Total dollar values are in millions; per household values are in dollars. Ratios are published as a percentage of disposable income, so 176.37 means debt equal to 176.37% of disposable income. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. Empty in all three files in this snapshot. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `household_debt_service_indicators.csv`

Official quarterly debt service indicators of Canadian households: household income and outlays, disposable income, interest paid, total, mortgage and non mortgage debt payments, obligated principal payments, and the debt service ratios built from them (total, mortgage, non mortgage, and interest only). Seasonally adjusted at annual rates or unadjusted. Dollar values in millions, ratios in units. First quarter of 1990 to second quarter of 2026.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference quarter stored as the first day of the quarter (1990-01-01 is the first quarter of 1990, 2026-04-01 is the second quarter of 2026). Balance sheet stocks are at the end of that quarter. In household_wealth_distribution.csv the published quarters are the fourth quarter of each year from 2010 to 2019 and every quarter from 2020 to 2025; other quarters before 2020 are kept with status .. and an empty value. |
| `geo` | Text | Geography as published. Canada only in all three files. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for Canada (2021A000011124). |
| `seasonal_adjustment` | Text | household_debt_service_indicators.csv only. Seasonally adjusted at annual rates means the quarterly flow is shown as if it held for a full year. Unadjusted means the raw quarterly flow. |
| `debt_service_item` | Text | household_debt_service_indicators.csv only. Item as published, for example Household income, Disposable income, Total debt payments, Mortgage interest paid, Total obligated payments of principal and Debt service ratio. Lines starting Plus, Equals or Of which are parts of the build up shown in the official table. Two labels, Disposable income and Of which: consumer debt, carry a trailing space in the official file and are kept exactly as published. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Ratio, Dollars or Percent. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: millions for total dollar values, units for ratios, percentages and per household dollar values. A total dollar value of 1000 means 1,000 million dollars. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Total dollar values are in millions; per household values are in dollars. Ratios are published as a percentage of disposable income, so 176.37 means debt equal to 176.37% of disposable income. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. Empty in all three files in this snapshot. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `household_wealth_distribution.csv`

Official distributions of household wealth for Canada: total, financial and non financial assets, real estate, pensions, mortgage and other liabilities, and net worth, by income quintile, wealth quintile, age of the major income earner, household type, main income source, housing tenure and generation. Published as total value (millions of dollars), share of the total (percent) and value per household (dollars). Fourth quarter only from 2010 to 2019, then every quarter from 2020 to the fourth quarter of 2025.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference quarter stored as the first day of the quarter (1990-01-01 is the first quarter of 1990, 2026-04-01 is the second quarter of 2026). Balance sheet stocks are at the end of that quarter. In household_wealth_distribution.csv the published quarters are the fourth quarter of each year from 2010 to 2019 and every quarter from 2020 to 2025; other quarters before 2020 are kept with status .. and an empty value. |
| `geo` | Text | Geography as published. Canada only in all three files. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for Canada (2021A000011124). |
| `household_characteristic` | Text | household_wealth_distribution.csv only. Household group as published: All households; income quintiles (based on equivalized household disposable income); wealth quintiles (based on net worth); age group of the major income earner; one person or multiple person households; main source of household income; housing tenure (owner, owner with mortgage, owner without mortgage, renter); generation; and income quintile by age group crossings. |
| `wealth_component` | Text | household_wealth_distribution.csv only. Balance sheet item as published: Total assets, Financial assets, Life insurance and pensions, Other financial assets, Non-financial assets, Real estate, Other non-financial assets, Total liabilities, Mortgage liabilities, Other liabilities, and Net worth (wealth). Items are nested, so add only items at the same level. |
| `statistic` | Text | household_wealth_distribution.csv only. Value is the total for the group in millions of dollars. Distribution of value is the group's share of the all households total for that item, in percent. Value per household is the average per household in the group, in dollars. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Ratio, Dollars or Percent. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: millions for total dollar values, units for ratios, percentages and per household dollar values. A total dollar value of 1000 means 1,000 million dollars. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Text | The published value. Total dollar values are in millions; per household values are in dollars. Ratios are published as a percentage of disposable income, so 176.37 means debt equal to 176.37% of disposable income. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. Empty in all three files in this snapshot. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_11100065.csv`

Official Statistics Canada metadata, notes and symbol legend for table 11-10-0065-01.

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

### `official_metadata_36100660.csv`

Official Statistics Canada metadata, notes and symbol legend for table 36-10-0660-01.

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

### `official_metadata_38100238.csv`

Official Statistics Canada metadata, notes and symbol legend for table 38-10-0238-01.

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

**Source:** Statistics Canada, national balance sheet accounts, household debt service indicators and distributions of household economic accounts. Official tables downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 38-10-0238-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810023801, https://www150.statcan.gc.ca/n1/tbl/csv/38100238-eng.zip) 11-10-0065-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110006501, https://www150.statcan.gc.ca/n1/tbl/csv/11100065-eng.zip) 36-10-0660-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610066001, https://www150.statcan.gc.ca/n1/tbl/csv/36100660-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahouseholddebtandwealth,
  author    = {Khan, John},
  title     = {Canada Household Debt, Debt Service and Wealth},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-household-debt-and-wealth}
}
```

APA: Khan, J. (2026). *Canada Household Debt, Debt Service and Wealth* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-household-debt-and-wealth

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of three official Statistics Canada tables on household debt and household finances. Together they show how much Canadian households owe, how that debt compares with their income, how much of their income goes to interest and principal payments, and how assets, debts and net worth are spread across income and wealth quintiles, age groups, homeowners and renters, and generations.

Source tables:

* [38-10-0238-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810023801): Household sector credit market summary table, seasonally adjusted estimates.
* [11-10-0065-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110006501): Debt service indicators of households, national balance sheet accounts.
* [36-10-0660-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610066001): Distributions of household economic accounts, wealth, by characteristic, Canada, quarterly.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The credit market and debt service tables run from the first quarter of 1990 to the second quarter of 2026. The wealth distribution table runs from 2010 to the fourth quarter of 2025.

## Files

* household_credit_market_summary.csv: 1,460 rows. 10 seasonally adjusted lines over 146 quarters: two debt to disposable income ratios, four outstanding debt amounts and four matching financial flows.
* household_debt_service_indicators.csv: 8,468 rows. 29 income, payment and ratio lines, seasonally adjusted at annual rates and unadjusted, over 146 quarters.
* household_wealth_distribution.csv: 118,272 rows. 11 wealth items for 56 household groups, each as a total, a share of the total and a value per household, over 64 quarters (34 with published values).
* data_dictionary.csv: every column in every file, with its type and meaning.
* official_metadata_*.csv: the official Statistics Canada notes, member lists and symbol legend for each table.

## A few numbers from this snapshot

* In the second quarter of 2026, household credit market debt was 176.37 percent of disposable income, or about 1.76 dollars of debt for every dollar of disposable income. The highest value in this table was 188.22 in the third quarter of 2022.
* Household credit market debt outstanding was 3,280.9 billion dollars at the end of the second quarter of 2026, of which mortgages were 2,446.9 billion and consumer credit 678.7 billion.
* The seasonally adjusted debt service ratio was 14.52 in the second quarter of 2026: 7.72 for mortgages and 6.80 for non mortgage debt. The interest only ratio was 8.51. Over the full series the ratio ranged from 10.69 in the second quarter of 1993 to 15.17 in the first quarter of 2023.
* In the fourth quarter of 2025, average net worth was 1,078,642 dollars per household. It was 3,543,579 dollars in the highest wealth quintile and -4,608 dollars in the lowest, where debts are larger than assets. The highest wealth quintile held 65.7% of all household net worth.
* In the same quarter, average total liabilities were 172,275 dollars per household where the major income earner was less than 35 years old, against 56,842 dollars at 65 years and over.

## Caveats

* Ratios are published as a percentage of disposable income. A debt to income value of 176.37 means debt equal to 176.37% of a year of disposable income.
* In this snapshot the debt service ratio equals total debt payments divided by the line Equals: disposable income before payment of interest, both from the same table and the same seasonal adjustment. Check the official definitions before building your own ratio.
* In the credit market summary, financial flows are seasonally adjusted at quarterly rates (official note), while the debt service table shows flows at annual rates or unadjusted. Do not mix the two without converting. Balance sheet amounts are stocks at the end of the quarter.
* Line items are nested. Credit market debt includes consumer credit, non mortgage loans and mortgages. In the wealth file, total assets include financial and non financial assets, and net worth is total assets less total liabilities. Add only items at the same level, and do not add unadjusted and seasonally adjusted rows.
* The wealth distribution table spreads national balance sheet totals across household groups. The official notes point to the Survey of Financial Security for accuracy indicators of these estimates. Before 2020 only fourth quarter values are published; the other quarters are kept with status .. and an empty value. For the income quintile by age group crossings, only total assets, total liabilities and net worth are published.
* Income quintiles use equivalized household disposable income (OECD modified scale). Wealth quintiles use household net worth. Age groups and generations refer to the major income earner. Renters include subsidized renters.
* Life insurance and pensions exclude public plans such as CPP, QPP and OAS. Values are revised as new source data arrive, so recent quarters will change.

## Example uses

* Track household leverage before and after the 2008 financial crisis, the pandemic and the 2022 to 2023 rate increases.
* Model how changes in interest rates feed into the mortgage and non mortgage debt service ratios.
* Compare wealth and debt gaps between income quintiles, wealth quintiles, age groups, homeowners and renters, or generations.
* Join with mortgage rates, insolvency counts, CPI or GDP data to study household financial stress.
* Teach household balance sheets, stocks and flows, and seasonally adjusted annual rates.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. Statistics Canada updates all three tables each quarter.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case and reference periods were stored as dates. Official values, labels, status symbols and termination flags were not altered. No rows were added or removed.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, tables 38-10-0238-01, 11-10-0065-01 and 36-10-0660-01. The published values were not changed. Columns were renamed and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
