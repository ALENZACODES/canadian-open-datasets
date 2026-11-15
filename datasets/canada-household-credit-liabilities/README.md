<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada household credit liabilities" width="100%"></p>

# Canada household credit liabilities

*Monthly mortgage, non-mortgage and total household credit, 1990 to 2026*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** 1990 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-household-credit-liabilities](https://www.kaggle.com/datasets/johnnykhan1/canada-household-credit-liabilities)

## What it is

Canada household credit liabilities, tidied from Statistics Canada Table 36-10-0639-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [36-10-0639-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610063901).

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 73 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 4 KB | in this repository |
| [`household_credit_liabilities_long.csv`](data/household_credit_liabilities_long.csv) | 5.7 MB | in this repository |
| [`household_credit_sa_headline.csv`](data/household_credit_sa_headline.csv) | 34 KB | in this repository |
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

### `household_credit_liabilities_long.csv`

Tidy long file of household credit liabilities, all published categories, raw and seasonally adjusted.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `seasonality` | Text | Raw (not seasonally adjusted) or seasonally adjusted, as published. |
| `credit_category` | Text | Type of household credit liability, including totals, mortgages, non-mortgage loans and selected lenders. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series (for example v41690973). Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in statcan_table_metadata.csv. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `household_credit_sa_headline.csv`

Seasonally adjusted headline household credit series, one column per category.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `credit_cards` | Float | Seasonally adjusted outstanding amount for credit_cards. See the long file for the unit and scale. |
| `home_equity_lines_of_credit` | Float | Seasonally adjusted outstanding amount for home_equity_lines_of_credit. See the long file for the unit and scale. |
| `mortgage_loans` | Float | Seasonally adjusted outstanding amount for mortgage_loans. See the long file for the unit and scale. |
| `non_mortgage_loans` | Float | Seasonally adjusted outstanding amount for non_mortgage_loans. See the long file for the unit and scale. |
| `of_which_auto_loans` | Float | Seasonally adjusted outstanding amount for of_which_auto_loans. See the long file for the unit and scale. |
| `of_which_real_estate_secured_lending` | Float | Seasonally adjusted outstanding amount for of_which_real_estate_secured_lending. See the long file for the unit and scale. |
| `residential_mortgages` | Float | Seasonally adjusted outstanding amount for residential_mortgages. See the long file for the unit and scale. |
| `total_credit_liabilities_of_households` | Float | Seasonally adjusted outstanding amount for total_credit_liabilities_of_households. See the long file for the unit and scale. |

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

**Source:** Statistics Canada Table 36-10-0639-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610063901. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/36100639-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahouseholdcreditliabilities,
  author    = {Khan, John},
  title     = {Canada household credit liabilities},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-household-credit-liabilities}
}
```

APA: Khan, J. (2026). *Canada household credit liabilities* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-household-credit-liabilities

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada household credit liabilities, tidied from Statistics Canada Table 36-10-0639-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [36-10-0639-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610063901).

## Coverage

The long file keeps the full published table for Canada: all credit categories and both raw and seasonally adjusted series, from January 1990 through August 2026. Categories include total credit liabilities, mortgage and non-mortgage loans, residential and non-residential mortgages, credit cards, auto loans, lines of credit, home equity lines of credit, and selected lender groups.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates this table once a month. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* Seasonally adjusted total credit liabilities of households were 3.30 million (see scalar_factor, usually millions of dollars) in 2026-08.
* Mortgage loans on the same basis were 2.46 million in 2026-08.
* The table is national only. It starts in January 1990 and runs through August 2026.

## Example uses

* Track total household credit and the split between mortgage and non-mortgage loans.
* Follow credit cards, auto loans or home equity lines of credit on their own.
* Compare the growth of household credit with incomes, prices or interest rates from another source.

## Caveats

Some category names, such as Chartered banks, appear under more than one parent (for example under mortgage loans and under non-mortgage loans). Use credit_category together with the official metadata file, or the coordinate and vector columns, when you need a specific series. Figures can be revised. This is outstanding credit, not a rate.

## Files

* `household_credit_liabilities_long.csv`: Tidy long file of household credit liabilities, all published categories, raw and seasonally adjusted.
* `household_credit_sa_headline.csv`: Seasonally adjusted headline household credit series, one column per category.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0639-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
