<p align="center"><img src="../../assets/theme-economy.png" alt="Canada merchandise trade by country" width="100%"></p>

# Canada merchandise trade by country

*Monthly exports, imports and trade balance with 28 partners, 1997 to 2026*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** 1997 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-merchandise-trade-by-country](https://www.kaggle.com/datasets/johnnykhan1/canada-merchandise-trade-by-country)

## What it is

Canada's monthly goods trade with its principal trading partners, tidied from Statistics Canada [Table 12-10-0011-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210001101). Covers exports, imports and the trade balance with the United States, the European Union, China, the United Kingdom, Mexico, Japan and 22 more partners.

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_merchandise_trade_by_partner_monthly.csv`](data/canada_merchandise_trade_by_partner_monthly.csv) | 13.8 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`statcan_metadata_12-10-0011.csv`](data/statcan_metadata_12-10-0011.csv) | 4 KB | in this repository |

## Columns

### `canada_merchandise_trade_by_partner_monthly.csv`

Monthly merchandise exports, imports and trade balance in dollars by principal trading partner, on customs and balance of payments bases, from Table 12-10-0011.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `trade` | Text | Import, Export or Trade Balance. |
| `basis` | Text | Customs basis or balance of payments basis. |
| `seasonal_adjustment` | Text | Seasonally adjusted or unadjusted. |
| `trading_partner` | Text | Principal trading partner, or All countries. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_12-10-0011.csv`

Official Statistics Canada cube metadata shipped with Table 12-10-0011-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 12-10-0011-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210001101); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadamerchandisetradebycountry,
  author    = {Khan, John},
  title     = {Canada merchandise trade by country},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-merchandise-trade-by-country}
}
```

APA: Khan, J. (2026). *Canada merchandise trade by country* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-merchandise-trade-by-country

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada's monthly goods trade with its principal trading partners, tidied from Statistics Canada [Table 12-10-0011-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210001101). Covers exports, imports and the trade balance with the United States, the European Union, China, the United Kingdom, Mexico, Japan and 22 more partners.

## Coverage

January 1997 to September 2026, monthly. Customs and balance of payments bases, seasonally adjusted and unadjusted.

## Updates

Released monthly at the source with revisions to recent months. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Canada's merchandise exports to all countries were 78.55 billion dollars in September 2026 (balance of payments basis, seasonally adjusted).
* Merchandise imports from all countries were 73.20 billion dollars in September 2026 (balance of payments basis, seasonally adjusted).
* The merchandise trade balance was a surplus of 5.35 billion dollars in September 2026.
* The United States took 70.2 percent of Canada's merchandise exports in September 2026.
* The file has 93,177 rows for 29 partners, on customs and balance of payments bases, from January 1997 to September 2026.

## Example uses

* Track how dependent Canada's exports are on the United States.
* Study tariff and trade policy effects by partner.
* Forecast the monthly trade balance.
* Join with exchange rates for currency and trade work.

## Caveats

Customs and balance of payments figures differ by design; do not mix them. Values are in dollars at the scale shown in scalar_factor. Recent months are revised. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `canada_merchandise_trade_by_partner_monthly.csv`: Monthly merchandise exports, imports and trade balance in dollars by principal trading partner, on customs and balance of payments bases, from Table 12-10-0011.
* `statcan_metadata_12-10-0011.csv`: Official cube metadata for Table 12-10-0011-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 12-10-0011-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
