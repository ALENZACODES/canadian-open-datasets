<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada monetary aggregates M1 M2 M3" width="100%"></p>

# Canada monetary aggregates M1 M2 M3

*Monthly money supply, deposits and bank loans in Canada, 1953 to 2026*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** January 1953 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-monetary-aggregates-m1-m2-m3](https://www.kaggle.com/datasets/johnnykhan1/canada-monetary-aggregates-m1-m2-m3)

## What it is

Canada's money supply measures and their parts, tidied from Statistics Canada [Table 10-10-0116-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010011601), which republishes Bank of Canada month end banking and financial statistics, seasonally adjusted. Includes the monetary base, M1+, M1++, M2, M2+, M2++, M3, chartered bank deposits by type, and personal, business and residential mortgage loans.

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_monetary_aggregates_monthly.csv`](data/canada_monetary_aggregates_monthly.csv) | 8.3 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`statcan_metadata_10-10-0116.csv`](data/statcan_metadata_10-10-0116.csv) | 11 KB | in this repository |

## Columns

### `canada_monetary_aggregates_monthly.csv`

Monthly monetary aggregates (M1+, M1++, M2, M2+, M2++, M3 and older definitions), deposits and chartered bank loans in dollars, from Table 10-10-0116.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `series` | Text | Monetary aggregate, deposit or loan series name as published in the source table. |
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
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_10-10-0116.csv`

Official Statistics Canada cube metadata shipped with Table 10-10-0116-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 10-10-0116-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010011601); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadamonetaryaggregatesm1m2m3,
  author    = {Khan, John},
  title     = {Canada monetary aggregates M1 M2 M3},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-monetary-aggregates-m1-m2-m3}
}
```

APA: Khan, J. (2026). *Canada monetary aggregates M1 M2 M3* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-monetary-aggregates-m1-m2-m3

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada's money supply measures and their parts, tidied from Statistics Canada [Table 10-10-0116-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010011601), which republishes Bank of Canada month end banking and financial statistics, seasonally adjusted. Includes the monetary base, M1+, M1++, M2, M2+, M2++, M3, chartered bank deposits by type, and personal, business and residential mortgage loans.

## Coverage

January 1953 to August 2026, monthly, Canada. Many older definitions stop early and carry a terminated flag.

## Updates

Updated monthly at the source. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* M1+ (gross) was 1.824 trillion dollars in August 2026 (seasonally adjusted, month end), up 7.0 percent from a year earlier.
* M2++ (gross) was 5.347 trillion dollars in August 2026 (seasonally adjusted, month end), up 6.3 percent from a year earlier.
* The file has 52,312 rows covering 66 series from January 1953 to August 2026.

## Example uses

* Study money growth and inflation in Canada.
* Track deposit shifts between chequing, notice and term accounts as rates change.
* Model growth in residential mortgage and business lending.
* Build features for interest rate or GDP nowcasts.

## Caveats

Series definitions changed over the decades; keep to one definition when building long runs. Check the adjustment column and scalar_factor (values are in millions of dollars where stated). Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `canada_monetary_aggregates_monthly.csv`: Monthly monetary aggregates (M1+, M1++, M2, M2+, M2++, M3 and older definitions), deposits and chartered bank loans in dollars, from Table 10-10-0116.
* `statcan_metadata_10-10-0116.csv`: Official cube metadata for Table 10-10-0116-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 10-10-0116-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
