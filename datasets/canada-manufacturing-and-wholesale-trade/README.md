<p align="center"><img src="../../assets/theme-economy.png" alt="Canada Manufacturing and Wholesale Trade" width="100%"></p>

# Canada Manufacturing and Wholesale Trade

*Monthly sales, orders, inventories and ratios by industry, 1992 to 2026*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** 1992 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-manufacturing-and-wholesale-trade](https://www.kaggle.com/datasets/johnnykhan1/canada-manufacturing-and-wholesale-trade)

## What it is

A tidy extract of three official Statistics Canada monthly tables on the goods side of the economy: what Canadian factories sell, the orders they receive and the inventories they hold (Monthly Survey of Manufacturing), and what wholesalers sell and keep in stock (Monthly Wholesale Trade Survey). Both are early signals for GDP, which Statistics Canada publishes later.

Source tables:

* [16-10-0047-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1610004701): Manufacturers' sales, inventories, orders and inventory to sales ratios, by industry (dollars unless otherwise noted).
* [20-10-0074-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010007401): Wholesale trade, sales.
* [20-10-0076-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010007601): Wholesale trade, inventories.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. Manufacturing runs from January 1992 and wholesale trade from January 1993, both to August 2026.

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 106 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 11 KB | in this repository |
| [`manufacturing_by_industry_monthly.csv`](data/manufacturing_by_industry_monthly.csv) | 35.9 MB | in this repository |
| [`official_metadata_16100047.csv`](data/official_metadata_16100047.csv) | 29 KB | in this repository |
| [`official_metadata_20100074.csv`](data/official_metadata_20100074.csv) | 8 KB | in this repository |
| [`official_metadata_20100076.csv`](data/official_metadata_20100076.csv) | 7 KB | in this repository |
| [`wholesale_inventories_monthly.csv`](data/wholesale_inventories_monthly.csv) | 4.0 MB | in this repository |
| [`wholesale_sales_monthly.csv`](data/wholesale_sales_monthly.csv) | 32.5 MB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `manufacturing_by_industry_monthly.csv`

Official Monthly Survey of Manufacturing estimates for Canada: sales of goods manufactured, new orders, unfilled orders, raw materials, goods in process, finished goods and total inventories, and the total inventory to sales and finished goods to sales ratios. Covers total manufacturing, the durable and non-durable aggregates and the 21 NAICS three digit subsectors, unadjusted and seasonally adjusted, January 1992 to August 2026. Dollars in thousands, ratios in units.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference month, stored as the first day of the month (2026-08-01 is August 2026). |
| `geo` | Text | Geography as published. Canada only in the manufacturing and wholesale inventories files. Canada, the ten provinces and the three territories in the wholesale sales file, where Northwest Territories includes Nunavut from January 1993 to December 1998. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `naics_industry` | Text | Industry exactly as published, with its North American Industry Classification System code in square brackets where it has one, for example Food manufacturing [311] or Wholesale trade [41]. Durable goods industries and Non-durable goods industries are official aggregates without a code. In the wholesale files, labels such as Wholesale trade (excluding oilseed and grain) [41 - 41112] are official totals that leave out the named industries. |
| `naics_code` | Text | The code inside the square brackets of naics_industry, copied out for easier filtering (for example 311, 31-33 or 41 - 41112). Empty for the durable and non-durable aggregates. Added here, not a separate official column. |
| `statistic` | Text | manufacturing_by_industry_monthly.csv only. Principal statistic as published: Sales of goods manufactured (shipments); New orders, estimated values of orders received during month; Unfilled orders, estimated values of orders at end of month; Raw materials, fuel, supplies, components, estimated values at end of month; Goods or work in process, estimated values at end of month; Finished goods manufactured, estimated values at end of month; Total inventory, estimated values of total inventory at end of the month; Ratio of total inventory to sales; Ratio of finished goods to sales. |
| `seasonal_adjustment` | Text | Unadjusted or Seasonally adjusted, as published. The official notes say a few new wholesale industries, such as cannabis, are published unadjusted only. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars, or Ratio for the two manufacturing ratio statistics. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. thousands for all dollar values, so 70000000 means 70 billion dollars. units for the two manufacturing ratios. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value: dollars in thousands, or a ratio for the two manufacturing ratio statistics. Empty when Statistics Canada did not publish a figure (status x, F or ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. A, B, C and D are data quality grades (excellent, very good, good, acceptable) on a published value, and E means use with caution. x means suppressed to meet the confidentiality requirements of the Statistics Act, F means too unreliable to be published, and .. means not available for that reference period; for those three the value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. Empty in all three files in this snapshot. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_16100047.csv`

Official Statistics Canada metadata, notes and symbol legend for table 16-10-0047-01.

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

### `official_metadata_20100074.csv`

Official Statistics Canada metadata, notes and symbol legend for table 20-10-0074-01.

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

### `official_metadata_20100076.csv`

Official Statistics Canada metadata, notes and symbol legend for table 20-10-0076-01.

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

### `wholesale_inventories_monthly.csv`

Official monthly end of month wholesale inventories for Canada, for total wholesale trade, its published aggregates and 42 trade groups and industries, unadjusted and seasonally adjusted, January 1993 to August 2026. Dollars in thousands.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference month, stored as the first day of the month (2026-08-01 is August 2026). |
| `geo` | Text | Geography as published. Canada only in the manufacturing and wholesale inventories files. Canada, the ten provinces and the three territories in the wholesale sales file, where Northwest Territories includes Nunavut from January 1993 to December 1998. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `naics_industry` | Text | Industry exactly as published, with its North American Industry Classification System code in square brackets where it has one, for example Food manufacturing [311] or Wholesale trade [41]. Durable goods industries and Non-durable goods industries are official aggregates without a code. In the wholesale files, labels such as Wholesale trade (excluding oilseed and grain) [41 - 41112] are official totals that leave out the named industries. |
| `naics_code` | Text | The code inside the square brackets of naics_industry, copied out for easier filtering (for example 311, 31-33 or 41 - 41112). Empty for the durable and non-durable aggregates. Added here, not a separate official column. |
| `seasonal_adjustment` | Text | Unadjusted or Seasonally adjusted, as published. The official notes say a few new wholesale industries, such as cannabis, are published unadjusted only. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars, or Ratio for the two manufacturing ratio statistics. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. thousands for all dollar values, so 70000000 means 70 billion dollars. units for the two manufacturing ratios. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value: dollars in thousands, or a ratio for the two manufacturing ratio statistics. Empty when Statistics Canada did not publish a figure (status x, F or ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. A, B, C and D are data quality grades (excellent, very good, good, acceptable) on a published value, and E means use with caution. x means suppressed to meet the confidentiality requirements of the Statistics Act, F means too unreliable to be published, and .. means not available for that reference period; for those three the value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. Empty in all three files in this snapshot. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `wholesale_sales_monthly.csv`

Official monthly wholesale sales for Canada, each province and territory, for total wholesale trade, its published aggregates and 42 trade groups and industries, unadjusted and seasonally adjusted, January 1993 to August 2026. Dollars in thousands.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference month, stored as the first day of the month (2026-08-01 is August 2026). |
| `geo` | Text | Geography as published. Canada only in the manufacturing and wholesale inventories files. Canada, the ten provinces and the three territories in the wholesale sales file, where Northwest Territories includes Nunavut from January 1993 to December 1998. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `naics_industry` | Text | Industry exactly as published, with its North American Industry Classification System code in square brackets where it has one, for example Food manufacturing [311] or Wholesale trade [41]. Durable goods industries and Non-durable goods industries are official aggregates without a code. In the wholesale files, labels such as Wholesale trade (excluding oilseed and grain) [41 - 41112] are official totals that leave out the named industries. |
| `naics_code` | Text | The code inside the square brackets of naics_industry, copied out for easier filtering (for example 311, 31-33 or 41 - 41112). Empty for the durable and non-durable aggregates. Added here, not a separate official column. |
| `seasonal_adjustment` | Text | Unadjusted or Seasonally adjusted, as published. The official notes say a few new wholesale industries, such as cannabis, are published unadjusted only. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Dollars, or Ratio for the two manufacturing ratio statistics. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. thousands for all dollar values, so 70000000 means 70 billion dollars. units for the two manufacturing ratios. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value: dollars in thousands, or a ratio for the two manufacturing ratio statistics. Empty when Statistics Canada did not publish a figure (status x, F or ..). Official values were not altered. |
| `status` | Text | Statistics Canada status symbol. A, B, C and D are data quality grades (excellent, very good, good, acceptable) on a published value, and E means use with caution. x means suppressed to meet the confidentiality requirements of the Statistics Act, F means too unreliable to be published, and .. means not available for that reference period; for those three the value is empty. Empty status means a regular published value. |
| `symbol` | Text | Additional Statistics Canada symbol when present. Empty in all three files in this snapshot. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. Empty in all three files in this snapshot. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

## Source and licence

**Source:** Statistics Canada, Monthly Survey of Manufacturing and Monthly Wholesale Trade Survey. Official tables downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 16-10-0047-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1610004701, https://www150.statcan.gc.ca/n1/tbl/csv/16100047-eng.zip) 20-10-0074-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010007401, https://www150.statcan.gc.ca/n1/tbl/csv/20100074-eng.zip) 20-10-0076-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010007601, https://www150.statcan.gc.ca/n1/tbl/csv/20100076-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadamanufacturingandwholesaletrade,
  author    = {Khan, John},
  title     = {Canada Manufacturing and Wholesale Trade},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-manufacturing-and-wholesale-trade}
}
```

APA: Khan, J. (2026). *Canada Manufacturing and Wholesale Trade* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-manufacturing-and-wholesale-trade

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of three official Statistics Canada monthly tables on the goods side of the economy: what Canadian factories sell, the orders they receive and the inventories they hold (Monthly Survey of Manufacturing), and what wholesalers sell and keep in stock (Monthly Wholesale Trade Survey). Both are early signals for GDP, which Statistics Canada publishes later.

Source tables:

* [16-10-0047-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1610004701): Manufacturers' sales, inventories, orders and inventory to sales ratios, by industry (dollars unless otherwise noted).
* [20-10-0074-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010007401): Wholesale trade, sales.
* [20-10-0076-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010007601): Wholesale trade, inventories.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. Manufacturing runs from January 1992 and wholesale trade from January 1993, both to August 2026.

## Files

* manufacturing_by_industry_monthly.csv: 179,226 rows. 9 statistics for total manufacturing, the durable and non durable aggregates and the 21 three digit NAICS subsectors, unadjusted and seasonally adjusted, over 416 months. The official table also has about 330 finer industries (four to six digit NAICS); they were left out to keep the file a practical size, and nothing else was removed.
* wholesale_sales_monthly.csv: 190,836 rows. Sales for 46 published industries and totals in 14 geographies over 404 months.
* wholesale_inventories_monthly.csv: 23,410 rows. End of month inventories for 46 published industries and totals, Canada only, over 404 months.
* data_dictionary.csv: every column in every file, with its type and meaning.
* official_metadata_*.csv: the official Statistics Canada notes, member lists and symbol legend for each table. The manufacturing metadata lists every industry in the full official table.

## A few numbers from this snapshot

All seasonally adjusted, Canada, current dollars.

* Manufacturing sales were 79.9 billion dollars in August 2026, against 78.7 billion dollars in July 2026. The ratio of total inventory to sales was 1.60 in August 2026.
* Unfilled orders for all manufacturing stood at 134.2 billion dollars at the end of August 2026.
* Transportation equipment manufacturing [336] sold 12.0 billion dollars in August 2026 and food manufacturing [311] sold 13.8 billion dollars.
* Total wholesale sales (Wholesale trade [41]) were 136.5 billion dollars in August 2026, against 137.9 billion dollars in July 2026. Ontario wholesalers sold 51.5 billion dollars in August 2026.
* Excluding petroleum products and oilseed and grain, wholesale sales were 91.6 billion dollars in August 2026, against 93.1 billion dollars in July 2026. This is the line on the cover.
* Wholesale inventories were 155.6 billion dollars at the end of August 2026.

## Caveats

* Values are in current dollars, not adjusted for inflation, and recent months are revised in later releases.
* The Wholesale trade [41] total has a break. The official note says it excludes oilseed and grain merchant wholesalers and petroleum product wholesalers from 1993 to 2022 and includes them from 2023. In this snapshot the break shows up earlier: [41] equals the total excluding both (66.9 billion dollars each in December 2020) and then jumps to 96.3 billion dollars in January 2021, when the excluding total was 68.7 billion dollars. For a consistent long series use Wholesale trade (excluding petroleum, petroleum products, and other hydrocarbons and excluding Oilseed and grain) [41 - 412-41112].
* Petroleum product merchant wholesalers [412] went from 28.4 billion dollars in February 2026 to 43.2 billion dollars in March 2026 (seasonally adjusted). The figures are as published; check the official release before reading it as a change in activity.
* Six new orders values for leather and allied product manufacturing [316], in 2016 to 2018, are negative as published. In most months new orders equal sales plus the change in unfilled orders, so a large drop in unfilled orders can push them below zero.
* Seasonally adjusted and unadjusted rows sit in the same file. Filter on seasonal_adjustment before summing or charting, and do not add the industry rows to the totals they belong to.
* Many provincial and territorial wholesale cells are suppressed for confidentiality (status x) or too unreliable to publish (status F), so values are empty there. Status letters A to E grade the quality of published values.
* Manufacturing data up to December 2003 are calibrated to the Annual Survey of Manufactures and Logging, and later data are reconciled with it, so aggregates may differ from that survey. Industries follow NAICS 2012 from 2009 and NAICS 2022 from late 2022, per the official notes.
* The manufacturing file keeps only total manufacturing, the two aggregates and the three digit subsectors. Use the official table for finer industries.

## Example uses

* Track the manufacturing and wholesale cycle as early indicators of goods GDP.
* Use new orders, unfilled orders and the inventory to sales ratio to study turning points.
* Compare industries such as transportation equipment, food and petroleum and coal products through trade shocks.
* Compare wholesale activity across provinces.
* Join with John Khan's Canada retail trade, GDP by industry and building permits datasets on Kaggle.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. Statistics Canada updates both surveys every month.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case, reference months were stored as dates, and a naics_code column was copied out of the published industry label. Official values, labels and status symbols were not altered. The manufacturing file keeps the rows for total manufacturing, the durable and non durable aggregates and the 21 three digit subsectors; the two wholesale files keep every official row.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, tables 16-10-0047-01, 20-10-0074-01 and 20-10-0076-01. The published values were not changed. Columns were renamed, finer manufacturing industries were left out, and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
