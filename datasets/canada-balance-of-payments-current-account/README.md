<p align="center"><img src="../../assets/theme-economy.png" alt="Canada balance of payments current account" width="100%"></p>

# Canada balance of payments current account

*Quarterly receipts, payments and balances for goods, services and income*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** January 1981 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-balance-of-payments-current-account](https://www.kaggle.com/datasets/johnnykhan1/canada-balance-of-payments-current-account)

## What it is

Canada's balance of payments current account, tidied from Statistics Canada [Table 36-10-0018-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610001801). Shows receipts, payments and balances for goods, services (travel, transportation, commercial and government services), primary income (wages and investment income) and secondary income (transfers).

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_current_account_quarterly.csv`](data/canada_current_account_quarterly.csv) | 2.5 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`statcan_metadata_36-10-0018.csv`](data/statcan_metadata_36-10-0018.csv) | 5 KB | in this repository |

## Columns

### `canada_current_account_quarterly.csv`

Quarterly seasonally adjusted receipts, payments and balances for each current account item, Canada, from Table 36-10-0018.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `receipts_payments_balances` | Text | Receipts, payments or balances, seasonally adjusted. |
| `current_account` | Text | Current account item as published. |
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

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_36-10-0018.csv`

Official Statistics Canada cube metadata shipped with Table 36-10-0018-01, including notes and the symbol legend. Layout is as published, not tidied.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Opoyfne sfroi ifciio na tdlht  ethie na  bttatlhbaeelb  elt.tieta.bllee.. |
| `Product Id` | Text | osnSStatistics Canada product identifier for the table.hleod in the table at download time.IM identifier for the table.at apply to the whole table.e is current or archived.i n the Statistics Canada website.c |
| `CANSIM Id` | Text | fFt eesoeo orrerf nr etue m tnhmffeechdbr ereeeeit   rrapqmCtsbeeeuAalr nneeiNbtc |
| `URL` | Text | hLtlree |
| `Cube Notes` | Text | i Nsertnrokthe at |
| `Archive Status` | Text | Wesib |
| `Frequency` | Text | amFR |
| `Start Reference Period` | Text | — |
| `End Reference Period` | Date | Lu |
| `Total number of dimensions` | Integer | N |

## Source and licence

**Source:** Statistics Canada Table 36-10-0018-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610001801); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadabalanceofpaymentscurrentaccount,
  author    = {Khan, John},
  title     = {Canada balance of payments current account},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-balance-of-payments-current-account}
}
```

APA: Khan, J. (2026). *Canada balance of payments current account* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-balance-of-payments-current-account

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada's balance of payments current account, tidied from Statistics Canada [Table 36-10-0018-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610001801). Shows receipts, payments and balances for goods, services (travel, transportation, commercial and government services), primary income (wages and investment income) and secondary income (transfers).

## Coverage

Q1 1981 to Q2 2026, quarterly, seasonally adjusted, Canada.

## Updates

Released quarterly at the source with revisions. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Canada's current account showed a surplus of 8.84 billion dollars in Q2 2026 (seasonally adjusted, quarterly, not annualized).
* The goods account showed a surplus of 12.20 billion dollars in the same quarter.
* The services account showed a surplus of 26 million dollars in the same quarter.
* The investment income account showed a surplus of 457 million dollars in the same quarter.
* The file has 16,198 rows across 32 current account items from Q1 1981 to Q2 2026.

## Example uses

* Study Canada's external balance and how it moves with oil prices and the dollar.
* Split the current account into trade and investment income drivers.
* Model travel spending flows.
* Use as macro features alongside GDP and exchange rates.

## Caveats

Quarterly values are not annualized. Recent quarters are revised. Values are in the scale shown in scalar_factor. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `canada_current_account_quarterly.csv`: Quarterly seasonally adjusted receipts, payments and balances for each current account item, Canada, from Table 36-10-0018.
* `statcan_metadata_36-10-0018.csv`: Official cube metadata for Table 36-10-0018-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0018-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
