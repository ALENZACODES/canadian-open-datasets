<p align="center"><img src="../../assets/theme-prices.png" alt="Canada industrial and raw materials prices" width="100%"></p>

# Canada industrial and raw materials prices

*Monthly IPPI and RMPI producer price indexes by product, 1956 to 2026*

**Theme:** [Prices and inflation](../../README.md#prices-and-inflation) · **Coverage:** 1956 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-industrial-and-raw-materials-price-indexes](https://www.kaggle.com/datasets/johnnykhan1/canada-industrial-and-raw-materials-price-indexes)

## What it is

Canada's two main producer price indexes, tidied from Statistics Canada. The Industrial Product Price Index ([Table 18-10-0266-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810026601)) measures prices that manufacturers receive for goods leaving the factory gate. The Raw Materials Price Index ([Table 18-10-0268-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810026801)) measures prices that manufacturers pay for raw materials such as crude oil, metals, grains and logs.

## Who it helps

Households watching the cost of living, budget planners, journalists, analysts and students studying inflation in Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`ippi_industrial_product_price_index_monthly.csv`](data/ippi_industrial_product_price_index_monthly.csv) | 19.3 MB | in this repository |
| [`rmpi_raw_materials_price_index_monthly.csv`](data/rmpi_raw_materials_price_index_monthly.csv) | 4.1 MB | in this repository |
| [`statcan_metadata_18-10-0266.csv`](data/statcan_metadata_18-10-0266.csv) | 34 KB | in this repository |
| [`statcan_metadata_18-10-0268.csv`](data/statcan_metadata_18-10-0268.csv) | 8 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `ippi_industrial_product_price_index_monthly.csv`

Monthly Industrial Product Price Index by product group, Canada, from Table 18-10-0266.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `napcs_product` | Text | Product group from the North American Product Classification System, with its code in brackets, as published. |
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

### `rmpi_raw_materials_price_index_monthly.csv`

Monthly Raw Materials Price Index by product group, Canada, from Table 18-10-0268.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `napcs_product` | Text | Product group from the North American Product Classification System, with its code in brackets, as published. |
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

### `statcan_metadata_18-10-0266.csv`

Official Statistics Canada cube metadata shipped with Table 18-10-0266-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `statcan_metadata_18-10-0268.csv`

Official Statistics Canada cube metadata shipped with Table 18-10-0268-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 18-10-0266-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810026601); Statistics Canada Table 18-10-0268-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810026801); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaindustrialandrawmaterialspriceinde,
  author    = {Khan, John},
  title     = {Canada industrial and raw materials prices},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-industrial-and-raw-materials-price-indexes}
}
```

APA: Khan, J. (2026). *Canada industrial and raw materials prices* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-industrial-and-raw-materials-price-indexes

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada's two main producer price indexes, tidied from Statistics Canada. The Industrial Product Price Index ([Table 18-10-0266-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810026601)) measures prices that manufacturers receive for goods leaving the factory gate. The Raw Materials Price Index ([Table 18-10-0268-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810026801)) measures prices that manufacturers pay for raw materials such as crude oil, metals, grains and logs.

## Coverage

IPPI from January 1956 and RMPI from January 1981, both to September 2026, monthly. Canada level, by NAPCS product group.

## Updates

Statistics Canada publishes these indexes monthly. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* The Industrial Product Price Index stood at 150.7 (January 2020 = 100) in September 2026, up 14.5 percent from a year earlier.
* The Raw Materials Price Index stood at 182.7 in September 2026, up 27.0 percent from a year earlier.
* Crude energy products were at 182.5 in September 2026, up 55.2 percent from a year earlier.
* The IPPI file has 125,776 rows for 394 product groups from January 1956, and the RMPI file has 29,253 rows for 84 groups from January 1981.

## Example uses

* Lead indicators for consumer inflation.
* Study pass through from oil, metals and lumber prices to factory prices.
* Deflate industry sales or build input cost models.
* Forecast producer inflation.

## Caveats

Most series use January 2020 = 100, a few newer ones use July 2024 = 100; check unit_of_measure before comparing levels. Recent months can be revised. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `ippi_industrial_product_price_index_monthly.csv`: Monthly Industrial Product Price Index by product group, Canada, from Table 18-10-0266.
* `rmpi_raw_materials_price_index_monthly.csv`: Monthly Raw Materials Price Index by product group, Canada, from Table 18-10-0268.
* `statcan_metadata_18-10-0266.csv`: Official cube metadata for Table 18-10-0266-01, as published.
* `statcan_metadata_18-10-0268.csv`: Official cube metadata for Table 18-10-0268-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 18-10-0266-01, Table 18-10-0268-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
