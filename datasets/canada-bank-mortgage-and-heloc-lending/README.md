<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada bank mortgage and HELOC lending" width="100%"></p>

# Canada bank mortgage and HELOC lending

*Quarterly chartered bank mortgages, insured share and home equity lines*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** January 1982 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-bank-mortgage-and-heloc-lending](https://www.kaggle.com/datasets/johnnykhan1/canada-bank-mortgage-and-heloc-lending)

## What it is

Mortgage and home equity lending by Canada's chartered banks, tidied from two Bank of Canada tables published by Statistics Canada. [Table 10-10-0134-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010013401) gives mortgage loans outstanding at quarter end, split into insured and uninsured residential, farm and non farm non residential, plus the flows behind them. [Table 10-10-0135-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010013501) gives home equity lines of credit, combined mortgage and HELOC plans, loan to value bands and utilization rates.

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`chartered_bank_heloc_quarterly.csv`](data/chartered_bank_heloc_quarterly.csv) | 292 KB | in this repository |
| [`chartered_bank_mortgage_loans_quarterly.csv`](data/chartered_bank_mortgage_loans_quarterly.csv) | 2.5 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`statcan_metadata_10-10-0134.csv`](data/statcan_metadata_10-10-0134.csv) | 3 KB | in this repository |
| [`statcan_metadata_10-10-0135.csv`](data/statcan_metadata_10-10-0135.csv) | 10 KB | in this repository |

## Columns

### `chartered_bank_heloc_quarterly.csv`

Quarterly home equity lines of credit, residential secured lending, loan to value bands and utilization bands, from Table 10-10-0135.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `heloc_series` | Text | HELOC or residential secured lending series name as published. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `chartered_bank_mortgage_loans_quarterly.csv`

Quarterly chartered bank mortgage loans outstanding and flows (increases, decreases, purchases, sales) by type of mortgage, from Table 10-10-0134.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `mortgages` | Text | Mortgage aggregate as published. |
| `increases_and_decreases` | Text | Stock or flow component as published. |
| `type_of_mortgage` | Text | Type of mortgage as published. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
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

### `statcan_metadata_10-10-0134.csv`

Official Statistics Canada cube metadata shipped with Table 10-10-0134-01, including notes and the symbol legend. Layout is as published, not tidied.

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

### `statcan_metadata_10-10-0135.csv`

Official Statistics Canada cube metadata shipped with Table 10-10-0135-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 10-10-0134-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010013401); Statistics Canada Table 10-10-0135-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010013501); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadabankmortgageandheloclending,
  author    = {Khan, John},
  title     = {Canada bank mortgage and HELOC lending},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-bank-mortgage-and-heloc-lending}
}
```

APA: Khan, J. (2026). *Canada bank mortgage and HELOC lending* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-bank-mortgage-and-heloc-lending

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Mortgage and home equity lending by Canada's chartered banks, tidied from two Bank of Canada tables published by Statistics Canada. [Table 10-10-0134-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010013401) gives mortgage loans outstanding at quarter end, split into insured and uninsured residential, farm and non farm non residential, plus the flows behind them. [Table 10-10-0135-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010013501) gives home equity lines of credit, combined mortgage and HELOC plans, loan to value bands and utilization rates.

## Coverage

Mortgages from Q1 1982 and HELOCs from Q1 2019, both to Q2 2026, quarterly, Canada.

## Updates

Updated quarterly at the source. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Chartered banks held 1.75 trillion dollars of residential mortgages in Canada (insured plus uninsured) at the end of Q2 2026, up 2.1 percent from a year earlier.
* Insured mortgages were 24.7 percent of that residential book, down from 24.9 percent a year earlier.
* Residential real estate secured lending by the banks was 2,083,977 in Q2 2026 in the published units, and stand alone HELOCs were 29,803. Read as millions of dollars, which fits the size of the mortgage file, that is about 2.08 trillion and 29.8 billion dollars.
* The mortgage file has 14,142 rows from Q1 1982; the HELOC file has 1,110 rows from Q1 2019.

## Example uses

* Track how the insured share of bank mortgages has changed since the mortgage rule changes.
* Study HELOC balances and how much of each line is drawn.
* Model bank mortgage growth against the policy rate.
* Combine with household credit data for a fuller picture of housing debt.

## Caveats

There is a large step up in insured residential balances around late 2011 and 2012; check the source notes before reading it as a change in lending. Mortgage values are in millions of dollars. The HELOC table is published with a unit of dollars and a scalar of units, but its totals line up with the mortgage table in millions; the values were left exactly as published. Bank coverage and reporting forms change over time. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `chartered_bank_mortgage_loans_quarterly.csv`: Quarterly chartered bank mortgage loans outstanding and flows (increases, decreases, purchases, sales) by type of mortgage, from Table 10-10-0134.
* `chartered_bank_heloc_quarterly.csv`: Quarterly home equity lines of credit, residential secured lending, loan to value bands and utilization bands, from Table 10-10-0135.
* `statcan_metadata_10-10-0134.csv`: Official cube metadata for Table 10-10-0134-01, as published.
* `statcan_metadata_10-10-0135.csv`: Official cube metadata for Table 10-10-0135-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 10-10-0134-01, Table 10-10-0135-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
