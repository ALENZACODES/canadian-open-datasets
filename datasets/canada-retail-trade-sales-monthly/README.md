<p align="center"><img src="../../assets/theme-economy.png" alt="Canada retail trade sales monthly" width="100%"></p>

# Canada retail trade sales monthly

*Monthly retail sales by industry for Canada, the provinces and major cities*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** January 2017 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-retail-trade-sales-monthly](https://www.kaggle.com/datasets/johnnykhan1/canada-retail-trade-sales-monthly)

## What it is

Canada retail trade sales monthly, tidied from Statistics Canada Table 20-10-0056-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [20-10-0056-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010005601).

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 75 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`retail_trade_sales_long.csv`](data/retail_trade_sales_long.csv) | 14.2 MB | in this repository |
| [`retail_trade_total_sa_by_geo.csv`](data/retail_trade_total_sa_by_geo.csv) | 21 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 6 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `retail_trade_sales_long.csv`

Tidy long file of monthly retail trade sales by geography and industry.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `naics` | Text | Industry group based on the North American Industry Classification System, including sector totals. |
| `sales_type` | Text | Total retail sales or retail e-commerce sales. |
| `adjustment` | Text | Unadjusted or seasonally adjusted, as published. |
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

### `retail_trade_total_sa_by_geo.csv`

Seasonally adjusted total retail trade sales, one column per geography.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `alberta` | Float | Published value for alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `british_columbia` | Float | Published value for british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `canada` | Float | Published value for canada. See unit_of_measure and scalar_factor in the long file for the unit. |
| `manitoba` | Float | Published value for manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |
| `montr_al_quebec` | Float | Published value for montr al quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `new_brunswick` | Float | Published value for new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `newfoundland_and_labrador` | Float | Published value for newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `northwest_territories` | Float | Published value for northwest territories. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nova_scotia` | Float | Published value for nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nunavut` | Float | Published value for nunavut. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ontario` | Float | Published value for ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prince_edward_island` | Float | Published value for prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `quebec` | Float | Published value for quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatchewan` | Float | Published value for saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `toronto_ontario` | Float | Published value for toronto ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `vancouver_british_columbia` | Float | Published value for vancouver british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `yukon` | Float | Published value for yukon. See unit_of_measure and scalar_factor in the long file for the unit. |

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

**Source:** Statistics Canada Table 20-10-0056-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010005601. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/20100056-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaretailtradesalesmonthly,
  author    = {Khan, John},
  title     = {Canada retail trade sales monthly},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-retail-trade-sales-monthly}
}
```

APA: Khan, J. (2026). *Canada retail trade sales monthly* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-retail-trade-sales-monthly

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada retail trade sales monthly, tidied from Statistics Canada Table 20-10-0056-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [20-10-0056-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010005601).

## Coverage

The long file keeps the full published table: Canada, the provinces and territories, and the listed census metropolitan areas, all NAICS industry groups in the cube, total retail sales and e-commerce sales, unadjusted and seasonally adjusted, from January 2017 through August 2026.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates this table once a month. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* Seasonally adjusted total retail sales in Canada were 74.57 million (see scalar_factor, usually thousands of dollars) in 2026-08.
* The table starts in January 2017 and runs through August 2026. It replaced the older, now inactive, table 20-10-0008-01.

## Example uses

* Follow national or provincial retail sales, including the seasonally adjusted total.
* Compare store types such as grocery, food and beverage, or motor vehicle and parts dealers.
* Look at retail e-commerce sales where the series is published.

## Caveats

E-commerce sales are not available for every geography or industry. Figures are often in thousands of dollars; always read scalar_factor. Values can be revised. Seasonal adjustment is published by Statistics Canada and can move when models are updated.

## Files

* `retail_trade_sales_long.csv`: Tidy long file of monthly retail trade sales by geography and industry.
* `retail_trade_total_sa_by_geo.csv`: Seasonally adjusted total retail trade sales, one column per geography.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 20-10-0056-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
