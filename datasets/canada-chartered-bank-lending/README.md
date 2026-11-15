<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada bank mortgage and other lending" width="100%"></p>

# Canada bank mortgage and other lending

*Chartered bank funds advanced and outstanding balances, monthly*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** January 2013 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-chartered-bank-lending](https://www.kaggle.com/datasets/johnnykhan1/canada-chartered-bank-lending)

## What it is

Monthly chartered bank lending amounts and residential mortgage interest rates from the Bank of Canada's official A4 tables. The amounts file covers funds advanced and outstanding balances for insured and uninsured residential mortgages by term, consumer credit, and business loans, including non-residential mortgages. The rates file covers interest rates charged on new and existing residential mortgages.

Sources: [A4_FUNDS_MONTHLY](https://www.bankofcanada.ca/valet/observations/group/A4_FUNDS_MONTHLY/csv) and [A4_RATES_MORTGAGES](https://www.bankofcanada.ca/valet/observations/group/A4_RATES_MORTGAGES/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`bank_lending_amounts.csv`](data/bank_lending_amounts.csv) | 1.7 MB | in this repository |
| [`bank_mortgage_interest_rates.csv`](data/bank_mortgage_interest_rates.csv) | 803 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`series_catalog.csv`](data/series_catalog.csv) | 10 KB | in this repository |

## Columns

### `bank_lending_amounts.csv`

Monthly funds advanced and outstanding balances for chartered bank residential mortgages, consumer credit and business loans, in millions of dollars.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `series_id` | Text | Bank of Canada Valet series identifier. |
| `series_label` | Text | Short official label for the series. |
| `series_description` | Text | Official Valet description of the series. |
| `value` | Float | Observation value. Empty when the Bank did not publish a figure for that date. |
| `flow` | Text | Whether the row is funds advanced (a flow) or outstanding balances (a stock). |
| `product_group` | Text | Lending group: residential mortgages, consumer credit, business loans, or variable-rate mortgages. |
| `insurance_status` | Text | Insured or uninsured, when the series is a residential mortgage aggregate. |
| `detail` | Text | Rate term or product detail, such as variable rate or fixed rate of five years and over. |

### `bank_mortgage_interest_rates.csv`

Monthly interest rates charged on new and existing chartered bank residential mortgages, insured and uninsured, by term.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `series_id` | Text | Bank of Canada Valet series identifier. |
| `series_label` | Text | Short official label for the series. |
| `series_description` | Text | Official Valet description of the series. |
| `value` | Float | Observation value. Empty when the Bank did not publish a figure for that date. |
| `flow` | Text | Whether the row is funds advanced (a flow) or outstanding balances (a stock). |
| `product_group` | Text | Lending group: residential mortgages, consumer credit, business loans, or variable-rate mortgages. |
| `insurance_status` | Text | Insured or uninsured, when the series is a residential mortgage aggregate. |
| `detail` | Text | Rate term or product detail, such as variable rate or fixed rate of five years and over. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `series_catalog.csv`

Official Valet identifiers, labels and descriptions.

| Column | Type | Description |
|---|---|---|
| `id` | Text | Official Valet series metadata field (id). |
| `label` | Text | Official Valet series metadata field (label). |
| `description` | Text | Official Valet series metadata field (description). |
| `date_format` | Text | Official Valet series metadata field (date_format). |
| `source_group` | Text | Valet group the series was taken from. |

## Source and licence

**Source:** Bank of Canada Valet group A4_FUNDS_MONTHLY: https://www.bankofcanada.ca/valet/observations/group/A4_FUNDS_MONTHLY/csv; Bank of Canada Valet group A4_RATES_MORTGAGES: https://www.bankofcanada.ca/valet/observations/group/A4_RATES_MORTGAGES/csv. Documentation: https://www.bankofcanada.ca/valet/docs. Terms of use: https://www.bankofcanada.ca/terms/. Downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario.

- **Licence:** [Bank of Canada terms of use](https://www.bankofcanada.ca/terms/). Source: Bank of Canada. Content may be used, copied and distributed for free with credit to the Bank of Canada and a note of changes made. Not endorsed by the Bank of Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacharteredbanklending,
  author    = {Khan, John},
  title     = {Canada bank mortgage and other lending},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-chartered-bank-lending}
}
```

APA: Khan, J. (2026). *Canada bank mortgage and other lending* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-chartered-bank-lending

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly chartered bank lending amounts and residential mortgage interest rates from the Bank of Canada's official A4 tables. The amounts file covers funds advanced and outstanding balances for insured and uninsured residential mortgages by term, consumer credit, and business loans, including non-residential mortgages. The rates file covers interest rates charged on new and existing residential mortgages.

Sources: [A4_FUNDS_MONTHLY](https://www.bankofcanada.ca/valet/observations/group/A4_FUNDS_MONTHLY/csv) and [A4_RATES_MORTGAGES](https://www.bankofcanada.ca/valet/observations/group/A4_RATES_MORTGAGES/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Coverage

Month-end observations from 2013-01-01 to 2026-08-01 for amounts, and from 2013-01-01 to 2026-08-01 for mortgage rates.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. The Bank of Canada updates these tables monthly. Call the official Valet endpoint for a later month.

## A few numbers from this snapshot

* Outstanding insured residential mortgages at chartered banks were 378,658 dollars (millions as published, check series description) in 2026-08.
* Outstanding uninsured residential mortgages were 1.25 million in the same month.
* Funds advanced on uninsured residential mortgages were 39,079 in 2026-08.
* The amounts file has 8,364 rows from 2013-01-01 to 2026-08-01. The mortgage rate file has 3,936 rows. Official units are millions of dollars for amounts and percent for rates.

## Example uses

* Watch the mix of insured and uninsured mortgage balances.
* Compare funds advanced (new lending) with outstanding balances (the stock of credit).
* Join mortgage rates charged by banks to CORRA or the policy rate.

## Caveats

Amounts are month-end figures in millions of dollars, as published by the Bank of Canada. Rates are in percent. The flow and insurance_status columns were derived from the official series descriptions so the file is easier to filter; always check series_description if a classification looks off. Variable-rate breakdowns and consumer-credit lines are stocks or flows according to the description. These are chartered bank figures, not the entire credit-union or non-bank mortgage market.

## Files

* `bank_lending_amounts.csv`: Funds advanced and outstanding balances.
* `bank_mortgage_interest_rates.csv`: Mortgage interest rates charged by chartered banks.
* `series_catalog.csv`: Official series list.
* `data_dictionary.csv`: Column dictionary.
* `cover.png`: Cover chart of insured and uninsured mortgages outstanding.

## Licence

Bank of Canada data are used under the Bank's [terms of use](https://www.bankofcanada.ca/terms/). Please credit the Bank of Canada. The Bank gives no warranty on accuracy. This dataset is not endorsed by the Bank of Canada. The Kaggle licence is set to Other because no standard licence matches these terms exactly. 

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
