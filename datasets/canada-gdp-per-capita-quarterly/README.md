<p align="center"><img src="../../assets/theme-economy.png" alt="Canada GDP per capita quarterly" width="100%"></p>

# Canada GDP per capita quarterly

*Real and nominal GDP, income, spending and housing investment per person*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** January 1981 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-per-capita-quarterly](https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-per-capita-quarterly)

## What it is

Per person measures of the Canadian economy, tidied from Statistics Canada [Table 36-10-0706-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610070601): gross domestic product per capita, household disposable income per capita, household final consumption per capita and residential investment per capita, in current and chained 2017 dollars with percentage changes.

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`gdp_per_capita_quarterly.csv`](data/gdp_per_capita_quarterly.csv) | 415 KB | in this repository |
| [`statcan_metadata_36-10-0706.csv`](data/statcan_metadata_36-10-0706.csv) | 3 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `gdp_per_capita_quarterly.csv`

Quarterly GDP per capita, household disposable income per capita, household consumption per capita and residential investment per capita, current and chained 2017 dollars, from Table 36-10-0706.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `prices` | Text | Current prices, chained 2017 dollars, or their percentage changes. |
| `estimates` | Text | Per capita measure as published. |
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
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_36-10-0706.csv`

Official Statistics Canada cube metadata shipped with Table 36-10-0706-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 36-10-0706-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610070601); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadagdppercapitaquarterly,
  author    = {Khan, John},
  title     = {Canada GDP per capita quarterly},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-per-capita-quarterly}
}
```

APA: Khan, J. (2026). *Canada GDP per capita quarterly* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-gdp-per-capita-quarterly

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Per person measures of the Canadian economy, tidied from Statistics Canada [Table 36-10-0706-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610070601): gross domestic product per capita, household disposable income per capita, household final consumption per capita and residential investment per capita, in current and chained 2017 dollars with percentage changes.

## Coverage

Q1 1981 to Q2 2026, quarterly, seasonally adjusted at annual rates, Canada.

## Updates

Released with each quarterly GDP report. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Real GDP per capita was 60,944 chained 2017 dollars (annualized) in Q2 2026, up 1.6 percent from a year earlier.
* The highest quarter in this file was Q3 2022 at 61,020 dollars.
* Household disposable income per capita at current prices was 44,914 dollars in Q2 2026, up 5.2 percent from a year earlier.
* The file has 2,548 rows from Q1 1981 to Q2 2026.

## Example uses

* Separate growth from population growth.
* Study the recent fall in output per person.
* Compare income and spending per person through recessions.
* Use as a clean quarterly macro target for forecasting.

## Caveats

Values are annualized. Percentage change rows use percent as the unit, not dollars; check unit_of_measure. Recent quarters are revised. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `gdp_per_capita_quarterly.csv`: Quarterly GDP per capita, household disposable income per capita, household consumption per capita and residential investment per capita, current and chained 2017 dollars, from Table 36-10-0706.
* `statcan_metadata_36-10-0706.csv`: Official cube metadata for Table 36-10-0706-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0706-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
