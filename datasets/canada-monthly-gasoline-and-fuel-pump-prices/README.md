<p align="center"><img src="../../assets/theme-prices.png" alt="Canada monthly gasoline and fuel pump prices" width="100%"></p>

# Canada monthly gasoline and fuel pump prices

*Pump prices for gasoline, diesel and heating oil in 18 cities, 1979 to 2026*

**Theme:** [Prices and inflation](../../README.md#prices-and-inflation) · **Coverage:** 1979 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-gasoline-and-fuel-pump-prices](https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-gasoline-and-fuel-pump-prices)

## What it is

Monthly average retail prices for gasoline, diesel and household heating fuel, tidied from Statistics Canada [Table 18-10-0001-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101). Prices are in cents per litre.

## Who it helps

Households watching the cost of living, budget planners, journalists, analysts and students studying inflation in Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_fuel_prices_monthly.csv`](data/canada_fuel_prices_monthly.csv) | 7.7 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`statcan_metadata_18-10-0001.csv`](data/statcan_metadata_18-10-0001.csv) | 4 KB | in this repository |

## Columns

### `canada_fuel_prices_monthly.csv`

Monthly average retail fuel prices in cents per litre by fuel type, for Canada and 18 cities, from Table 18-10-0001.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `type_of_fuel` | Text | Fuel type and service level, as published (for example Regular unleaded gasoline at self service filling stations). |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. |
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

### `statcan_metadata_18-10-0001.csv`

Official Statistics Canada cube metadata shipped with Table 18-10-0001-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 18-10-0001-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadamonthlygasolineandfuelpumpprices,
  author    = {Khan, John},
  title     = {Canada monthly gasoline and fuel pump prices},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-gasoline-and-fuel-pump-prices}
}
```

APA: Khan, J. (2026). *Canada monthly gasoline and fuel pump prices* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-monthly-gasoline-and-fuel-pump-prices

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly average retail prices for gasoline, diesel and household heating fuel, tidied from Statistics Canada [Table 18-10-0001-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101). Prices are in cents per litre.

## Coverage

January 1979 to September 2026, monthly. Canada and 18 cities from St. John's to Victoria, Whitehorse and Yellowknife, including Toronto.

## Updates

Statistics Canada adds a new month with each CPI release. This is a snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Self serve regular gasoline in Canada averaged 184.3 cents per litre in September 2026, up 27.8 percent from 144.2 a year earlier.
* Self serve regular gasoline in Toronto averaged 183.7 cents per litre in September 2026, up 32.3 percent from 138.9 a year earlier.
* Self serve regular gasoline in Vancouver averaged 209.5 cents per litre in September 2026, up 22.2 percent from 171.5 a year earlier.
* Self serve regular gasoline in Montréal averaged 198.4 cents per litre in September 2026, up 22.3 percent from 162.2 a year earlier.
* Self serve regular gasoline in Calgary averaged 167.3 cents per litre in September 2026, up 26.6 percent from 132.2 a year earlier.
* The highest monthly Canada average for self serve regular in this file is 207.2 cents per litre, in June 2022.
* The file has 46,262 rows across 7 fuel types and 19 geographies from January 1979 to September 2026.

## Example uses

* Study how oil price shocks pass through to the pump.
* Compare city price gaps and the effect of carbon pricing and fuel taxes.
* Forecast gasoline prices.
* Join with CPI or exchange rate data for macro work.

## Caveats

Full service gasoline and diesel series stopped after January 2013 because of a lack of data and carry a terminated flag. Fuel oil is not published for Edmonton and Calgary. Empty values mean no figure was published; see status and symbol.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `canada_fuel_prices_monthly.csv`: Monthly average retail fuel prices in cents per litre by fuel type, for Canada and 18 cities, from Table 18-10-0001.
* `statcan_metadata_18-10-0001.csv`: Official cube metadata for Table 18-10-0001-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 18-10-0001-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
