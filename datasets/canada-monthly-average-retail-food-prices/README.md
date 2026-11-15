<p align="center"><img src="../../assets/theme-prices.png" alt="Canada monthly average retail food prices" width="100%"></p>

# Canada monthly average retail food prices

*Average shelf prices for 110 grocery items by province, 2017 to 2026*

**Theme:** [Prices and inflation](../../README.md#prices-and-inflation) · **Coverage:** 2017 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-average-retail-food-prices](https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-average-retail-food-prices)

## What it is

Monthly average retail prices for 110 everyday grocery and household products in Canada, tidied from Statistics Canada [Table 18-10-0245-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501). Statistics Canada derives these averages from transaction data supplied by Canadian grocery retailers. Prices are in dollars for a stated unit such as per kilogram, 1 litre or 1 dozen.

## Who it helps

Households watching the cost of living, budget planners, journalists, analysts and students studying inflation in Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_average_retail_prices_monthly.csv`](data/canada_average_retail_prices_monthly.csv) | 17.5 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`statcan_metadata_18-10-0245.csv`](data/statcan_metadata_18-10-0245.csv) | 10 KB | in this repository |

## Columns

### `canada_average_retail_prices_monthly.csv`

Monthly average retail prices in dollars for selected grocery and household products, for Canada, the provinces, Whitehorse and Yellowknife, from Table 18-10-0245.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `products` | Text | Product and the unit the price refers to, as published (for example Milk, 1 litre). |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_18-10-0245.csv`

Official Statistics Canada cube metadata shipped with Table 18-10-0245-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 18-10-0245-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadamonthlyaverageretailfoodprices,
  author    = {Khan, John},
  title     = {Canada monthly average retail food prices},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-average-retail-food-prices}
}
```

APA: Khan, J. (2026). *Canada monthly average retail food prices* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-average-retail-food-prices

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly average retail prices for 110 everyday grocery and household products in Canada, tidied from Statistics Canada [Table 18-10-0245-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501). Statistics Canada derives these averages from transaction data supplied by Canadian grocery retailers. Prices are in dollars for a stated unit such as per kilogram, 1 litre or 1 dozen.

## Coverage

January 2017 to September 2026, monthly. Canada and the ten provinces, plus Whitehorse and Yellowknife from September 2025.

## Updates

Statistics Canada adds a new month with each CPI release. This is a snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Ground beef averaged 16.92 dollars per kilogram across Canada in September 2026, up 13.9 percent from 14.85 dollars a year earlier.
* Milk averaged 3.22 dollars for 1 litre across Canada in September 2026, up 3.9 percent from 3.10 dollars a year earlier.
* Eggs averaged 4.83 dollars for 1 dozen across Canada in September 2026, down 1.2 percent from 4.89 dollars a year earlier.
* White bread averaged 3.58 dollars for 675 grams across Canada in September 2026, up 3.5 percent from 3.46 dollars a year earlier.
* Bananas averaged 1.88 dollars per kilogram across Canada in September 2026, up 12.6 percent from 1.67 dollars a year earlier.
* In Ontario, ground beef averaged 17.23 dollars per kilogram in September 2026.
* The file has 142,740 rows covering 110 products and 13 geographies from January 2017 to September 2026.

## Example uses

* Track food inflation for single items rather than the CPI basket.
* Compare grocery prices across provinces.
* Forecast item prices with seasonal time series models.
* Build a monthly grocery cost index for a household basket.

## Caveats

Statistics Canada warns that the products inside a category can change over time, so averages may not be fully comparable from one month to the next. More retailers were added from January 2024. Not all 110 prices are published for Whitehorse and Yellowknife. Empty values mean no figure was published; check status and symbol.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `canada_average_retail_prices_monthly.csv`: Monthly average retail prices in dollars for selected grocery and household products, for Canada, the provinces, Whitehorse and Yellowknife, from Table 18-10-0245.
* `statcan_metadata_18-10-0245.csv`: Official cube metadata for Table 18-10-0245-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 18-10-0245-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
