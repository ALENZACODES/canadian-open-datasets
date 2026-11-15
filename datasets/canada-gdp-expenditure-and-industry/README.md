<p align="center"><img src="../../assets/theme-economy.png" alt="Canada GDP by Expenditure and Industry" width="100%"></p>

# Canada GDP by Expenditure and Industry

*Quarterly, monthly and provincial GDP from Statistics Canada, 1961 to 2026*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** January 1961 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-expenditure-and-industry](https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-expenditure-and-industry)

## What it is

A tidy extract of three official Statistics Canada gross domestic product (GDP) tables. Together they show how big the Canadian economy is, how fast it grows, what it is spent on, which industries produce it, and how it is split across provinces and territories.

Source tables:

* [36-10-0104-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610010401): Gross domestic product, expenditure-based, Canada, quarterly.
* [36-10-0434-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610043401): Gross domestic product (GDP) at basic prices, by industry, monthly.
* [36-10-0222-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610022201): Gross domestic product, expenditure-based, provincial and territorial, annual.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The quarterly table runs from the first quarter of 1961 to the second quarter of 2026, the monthly industry table from January 1997 to August 2026, and the provincial table from 1981 to 2025.

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 46 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 12 KB | in this repository |
| [`gdp_by_industry_monthly.csv`](data/gdp_by_industry_monthly.csv) | 49.2 MB | in this repository |
| [`gdp_expenditure_provincial_annual.csv`](data/gdp_expenditure_provincial_annual.csv) | 25.8 MB | in this repository |
| [`gdp_expenditure_quarterly.csv`](data/gdp_expenditure_quarterly.csv) | 12.0 MB | in this repository |
| [`official_metadata_36100104.csv`](data/official_metadata_36100104.csv) | 4 KB | in this repository |
| [`official_metadata_36100222.csv`](data/official_metadata_36100222.csv) | 6 KB | in this repository |
| [`official_metadata_36100434.csv`](data/official_metadata_36100434.csv) | 20 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `gdp_by_industry_monthly.csv`

Official monthly GDP at basic prices for Canada by NAICS industry and special aggregate (249 industries and aggregates), in millions of chained (2017) dollars or 2017 constant prices, seasonally adjusted at annual rates or trading day adjusted, January 1997 to August 2026.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period stored as a date. In gdp_expenditure_quarterly.csv it is the first day of the calendar quarter (1961-01-01 is the first quarter of 1961, 2026-04-01 is the second quarter of 2026). In gdp_by_industry_monthly.csv it is the first day of the month (1997-01-01 to 2026-08-01). In gdp_expenditure_provincial_annual.csv it is January 1 of the calendar year (1981-01-01 to 2025-01-01). |
| `geo` | Text | Geography as published. The quarterly and monthly files have Canada only. The annual file has Canada, the ten provinces, Yukon, Northwest Territories, Nunavut, Northwest Territories including Nunavut (to 1998 only), and Outside Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. Empty where none is published, for example Outside Canada. |
| `prices` | Text | Price basis as published. Current prices are nominal dollars. Chained (2017) dollars and 2017 constant prices are real (volume) measures. Chained (2017) dollars percentage change is the change from the previous quarter in percent, not annualized. Contributions to percent change show how many percentage points each component added to the change in GDP. Chained (2012) dollars, Chained (2007) dollars and 2012 constant prices are terminated older bases kept as published. |
| `seasonal_adjustment` | Text | Quarterly and monthly files only. Seasonally adjusted at annual rates means the quarterly or monthly level is shown as if it held for a full year. Unadjusted means raw quarterly values. Trading day adjusted means monthly values adjusted only for the number of working days. |
| `industry` | Text | Monthly file only. NAICS industry or special aggregate as published, with the official code in square brackets, for example All industries [T001], Construction [23] or Energy sector [T016]. Industries are nested and special aggregates overlap, so do not add them together. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars or Percent. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: millions for dollar values and units for percent values. A dollar value of 1000 means 1,000 million dollars, or 1 billion dollars. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Dollar values are in millions. Percent values are percentages or percentage points. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series (older price bases), otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `gdp_expenditure_provincial_annual.csv`

Official annual expenditure based GDP for Canada, each province and territory and Outside Canada, including trade with other countries and with other provinces, in millions of current dollars, chained dollars or constant prices, plus contributions to percent change, 1981 to 2025. Chained (2012) dollars and 2012 constant prices are terminated and kept as published.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period stored as a date. In gdp_expenditure_quarterly.csv it is the first day of the calendar quarter (1961-01-01 is the first quarter of 1961, 2026-04-01 is the second quarter of 2026). In gdp_by_industry_monthly.csv it is the first day of the month (1997-01-01 to 2026-08-01). In gdp_expenditure_provincial_annual.csv it is January 1 of the calendar year (1981-01-01 to 2025-01-01). |
| `geo` | Text | Geography as published. The quarterly and monthly files have Canada only. The annual file has Canada, the ten provinces, Yukon, Northwest Territories, Nunavut, Northwest Territories including Nunavut (to 1998 only), and Outside Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. Empty where none is published, for example Outside Canada. |
| `prices` | Text | Price basis as published. Current prices are nominal dollars. Chained (2017) dollars and 2017 constant prices are real (volume) measures. Chained (2017) dollars percentage change is the change from the previous quarter in percent, not annualized. Contributions to percent change show how many percentage points each component added to the change in GDP. Chained (2012) dollars, Chained (2007) dollars and 2012 constant prices are terminated older bases kept as published. |
| `expenditure_component` | Text | Quarterly and annual files only. Expenditure component as published, for example Household final consumption expenditure, Business gross fixed capital formation, Exports of goods and services, Less: imports of goods and services, Statistical discrepancy, Gross domestic product at market prices and Final domestic demand. Child lines are parts of their parent lines. Imports are shown as positive values and are subtracted to get GDP. Adjusting entry lines in the annual file reconcile chained components with their totals. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars or Percent. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: millions for dollar values and units for percent values. A dollar value of 1000 means 1,000 million dollars, or 1 billion dollars. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Dollar values are in millions. Percent values are percentages or percentage points. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series (older price bases), otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `gdp_expenditure_quarterly.csv`

Official quarterly expenditure based GDP for Canada: household, non-profit and government consumption, business and government investment, inventories, exports, imports, statistical discrepancy, GDP at market prices and final domestic demand. Current prices and chained (2017) dollars in millions, seasonally adjusted at annual rates or unadjusted, plus quarterly percentage change and contributions to percent change. First quarter of 1961 to second quarter of 2026. Chained (2012) and chained (2007) dollar series are terminated and kept as published.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period stored as a date. In gdp_expenditure_quarterly.csv it is the first day of the calendar quarter (1961-01-01 is the first quarter of 1961, 2026-04-01 is the second quarter of 2026). In gdp_by_industry_monthly.csv it is the first day of the month (1997-01-01 to 2026-08-01). In gdp_expenditure_provincial_annual.csv it is January 1 of the calendar year (1981-01-01 to 2025-01-01). |
| `geo` | Text | Geography as published. The quarterly and monthly files have Canada only. The annual file has Canada, the ten provinces, Yukon, Northwest Territories, Nunavut, Northwest Territories including Nunavut (to 1998 only), and Outside Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. Empty where none is published, for example Outside Canada. |
| `prices` | Text | Price basis as published. Current prices are nominal dollars. Chained (2017) dollars and 2017 constant prices are real (volume) measures. Chained (2017) dollars percentage change is the change from the previous quarter in percent, not annualized. Contributions to percent change show how many percentage points each component added to the change in GDP. Chained (2012) dollars, Chained (2007) dollars and 2012 constant prices are terminated older bases kept as published. |
| `seasonal_adjustment` | Text | Quarterly and monthly files only. Seasonally adjusted at annual rates means the quarterly or monthly level is shown as if it held for a full year. Unadjusted means raw quarterly values. Trading day adjusted means monthly values adjusted only for the number of working days. |
| `expenditure_component` | Text | Quarterly and annual files only. Expenditure component as published, for example Household final consumption expenditure, Business gross fixed capital formation, Exports of goods and services, Less: imports of goods and services, Statistical discrepancy, Gross domestic product at market prices and Final domestic demand. Child lines are parts of their parent lines. Imports are shown as positive values and are subtracted to get GDP. Adjusting entry lines in the annual file reconcile chained components with their totals. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars or Percent. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published: millions for dollar values and units for percent values. A dollar value of 1000 means 1,000 million dollars, or 1 billion dollars. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Dollar values are in millions. Percent values are percentages or percentage points. Empty when Statistics Canada did not publish a figure (status ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. .. means not available for that reference period and value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series (older price bases), otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_36100104.csv`

Official Statistics Canada metadata, notes and symbol legend for table 36-10-0104-01.

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

### `official_metadata_36100222.csv`

Official Statistics Canada metadata, notes and symbol legend for table 36-10-0222-01.

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

### `official_metadata_36100434.csv`

Official Statistics Canada metadata, notes and symbol legend for table 36-10-0434-01.

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

**Source:** Statistics Canada, national and provincial economic accounts. Official tables downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 36-10-0104-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610010401, https://www150.statcan.gc.ca/n1/tbl/csv/36100104-eng.zip) 36-10-0434-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610043401, https://www150.statcan.gc.ca/n1/tbl/csv/36100434-eng.zip) 36-10-0222-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610022201, https://www150.statcan.gc.ca/n1/tbl/csv/36100222-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadagdpexpenditureandindustry,
  author    = {Khan, John},
  title     = {Canada GDP by Expenditure and Industry},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-expenditure-and-industry}
}
```

APA: Khan, J. (2026). *Canada GDP by Expenditure and Industry* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-expenditure-and-industry

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of three official Statistics Canada gross domestic product (GDP) tables. Together they show how big the Canadian economy is, how fast it grows, what it is spent on, which industries produce it, and how it is split across provinces and territories.

Source tables:

* [36-10-0104-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610010401): Gross domestic product, expenditure-based, Canada, quarterly.
* [36-10-0434-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610043401): Gross domestic product (GDP) at basic prices, by industry, monthly.
* [36-10-0222-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610022201): Gross domestic product, expenditure-based, provincial and territorial, annual.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The quarterly table runs from the first quarter of 1961 to the second quarter of 2026, the monthly industry table from January 1997 to August 2026, and the provincial table from 1981 to 2025.

## Files

* gdp_expenditure_quarterly.csv: 69,266 rows. 31 expenditure lines for Canada in current prices and chained (2017) dollars, seasonally adjusted at annual rates or unadjusted, plus quarterly percentage change and contributions to percent change, over 262 quarters.
* gdp_by_industry_monthly.csv: 265,932 rows. Monthly GDP at basic prices for 249 NAICS industries and special aggregates, in chained (2017) dollars and 2017 constant prices, over 356 months.
* gdp_expenditure_provincial_annual.csv: 179,061 rows. Annual expenditure based GDP for Canada, each province and territory and Outside Canada, including exports to and imports from other provinces, over 45 years.
* data_dictionary.csv: every column in every file, with its type and meaning.
* official_metadata_*.csv: the official Statistics Canada notes, member lists and symbol legend for each table.

Dollar values are in millions. Percent values are percentages or percentage points.

## A few numbers from this snapshot

* In the second quarter of 2026, Canada's real GDP was 2,524.1 billion chained (2017) dollars at an annual rate, and nominal GDP was 3,437.7 billion dollars at an annual rate.
* Real GDP changed by 0.8% from the previous quarter in the second quarter of 2026. The largest quarterly fall in this table was -11.0% in the second quarter of 2020, and the largest rise was 9.1% in the third quarter of 2020.
* In August 2026, monthly GDP for all industries was 2,371.6 billion chained (2017) dollars at an annual rate. Goods producing industries were 600.3 billion and services producing industries 1,778.2 billion; as chained values, these two parts do not add exactly to the total.
* In 2025, nominal GDP was 1,258.6 billion dollars in Ontario, 646.5 billion in Quebec, 482.4 billion in Alberta and 448.1 billion in British Columbia, against 3,247.2 billion for Canada in this provincial table.

## Caveats

* Line items are nested. Household final consumption expenditure already includes Goods and Services, and Goods already includes durable, semi durable and non durable goods. Add only items at the same level. Imports are positive values that are subtracted.
* Chained dollar components are not additive. Parts of a chained (2017) dollar total do not sum exactly to that total, and the official notes for the industry table say aggregates are not always equal to the sum of their components. Use current prices or the contributions to percent change when you need parts that add up.
* Seasonally adjusted at annual rates means a quarter or month is shown as if it lasted a full year. Divide by 4 (quarterly) or 12 (monthly) for the flow within that period. Do not add seasonally adjusted and unadjusted rows.
* The quarterly percentage change is from the previous quarter and is not annualized. Contributions to percent change, annualized, are a separate published series.
* Older price bases (chained 2012 and 2007 dollars, 2012 constant prices) are terminated series kept as published. Unadjusted chained (2012) dollar rows have no published values.
* The monthly industry table is at basic prices, while the expenditure tables are at market prices, so their totals differ by taxes less subsidies on products. The monthly table moved to NAICS Canada 2022 with the November 28, 2025 release. Only industries and aggregates with good continuity start in January 1997. Other detailed industries start in 2007, 2011, 2017 or 2018, and their earlier months are kept with status .. and an empty value.
* The official notes say Canada totals in the provincial table do not always match the national quarterly accounts until annual revisions are folded in. Northwest Territories including Nunavut ends in 1998, and the separate territories start in 1999.
* GDP is revised often. Recent quarters, months and years will change in later releases.

## Example uses

* Track recessions and recoveries, such as 2008 to 2009 and 2020, with quarterly real GDP and its contributions.
* Build a monthly GDP nowcast or compare industry cycles in construction, manufacturing, energy or finance and real estate.
* Compare provinces by size, growth, investment and trade with other provinces and other countries.
* Join with population, interest rate, employment or government finance data to build per person, debt to GDP or productivity measures.
* Teach national accounts, chained dollars and seasonally adjusted annual rates.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. Statistics Canada updates the quarterly table each quarter, the industry table each month and the provincial table once a year.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case and reference periods were stored as dates. Official values, status symbols and termination flags were not altered. No rows were added or removed.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, tables 36-10-0104-01, 36-10-0434-01 and 36-10-0222-01. The published values were not changed. Columns were renamed and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
