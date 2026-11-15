<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada Senior Loan Officer Survey" width="100%"></p>

# Canada Senior Loan Officer Survey

*Quarterly bank lending conditions for mortgages, households and firms*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** April 1999 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-senior-loan-officer-survey](https://www.kaggle.com/datasets/johnnykhan1/canada-senior-loan-officer-survey)

## What it is

The Bank of Canada's Senior Loan Officer Survey, tidied from the official Valet group SLOS. The survey collects the views of Canadian financial institutions on price and non-price lending conditions. Series cover overall business lending, mortgage lending (including insured and uninsured mortgages and HELOCs in the combined measures), and non-mortgage household lending.

Source: Bank of Canada Valet group [SLOS](https://www.bankofcanada.ca/valet/observations/group/SLOS/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`series_catalog.csv`](data/series_catalog.csv) | 2 KB | in this repository |
| [`slos_long.csv`](data/slos_long.csv) | 211 KB | in this repository |
| [`slos_wide.csv`](data/slos_wide.csv) | 5 KB | in this repository |

## Columns

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

### `slos_long.csv`

Tidy long file of Senior Loan Officer Survey balances of opinion, one row per quarter and series.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `series_id` | Text | Bank of Canada Valet series identifier. |
| `series_label` | Text | Short official label for the series. |
| `series_description` | Text | Official Valet description of the series. |
| `value` | Float | Observation value. Empty when the Bank did not publish a figure for that date. |

### `slos_wide.csv`

Wide quarterly file with one column per official survey series.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `SLOS_BUS_LEND` | Float | Overall business lending conditions. Business lending: overall lending conditions (average of price and non-price lending conditions for small business, commercial and corporate combined) |
| `SLOS_BUS_LEND_PC` | Float | Business price lending conditions. Price lending conditions for business lending (average of price lending conditions for small business, commercial and corporate) |
| `SLOS_BUS_LEND_NP` | Float | Business non-price lending conditions. Non-price lending conditions for business lending (average of non-price lending conditions for small business, commercial and corporate) |
| `SLOS_ML_LEND` | Float | Mortgage lending conditions. Mortgage lending: overall lending conditions (average of price and non-price lending conditions for insured mortgages, uninsured mortgages and HELOCs combined) |
| `SLOS_NML_LEND` | Float | Non-mortgage lending conditions. Non-mortgage lending: overall lending conditions (average of price and non-price lending conditions for auto lending and all other consumer lending combined) |
| `SLOS_ML_LEND_NP` | Float | Mortgage non-price lending conditions. Non-price lending conditions for mortgage related lending (average of non-price lending conditions for insured mortgages, uninsured mortgages and HELOCs) |
| `SLOS_ML_LEND_PC` | Float | Mortgage price lending conditions. Price lending conditions for mortgage related lending (average of price lending conditions for insured mortgages, uninsured mortgages and HELOCs) |
| `SLOS_NML_LEND_NP` | Float | Non-mortgage non-price lending conditions. Non-price lending conditions for non-mortgage related lending (average of non-price lending conditions for auto lending and all other consumer lending) |
| `SLOS_NML_LEND_PC` | Float | Non-mortgage price lending conditions. Price lending conditions for non-mortgage related lending (average of price lending conditions for auto lending and all other consumer lending) |

## Source and licence

**Source:** Bank of Canada Valet group SLOS: https://www.bankofcanada.ca/valet/observations/group/SLOS/csv. Documentation: https://www.bankofcanada.ca/valet/docs. Terms of use: https://www.bankofcanada.ca/terms/. Downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario.

- **Licence:** [Bank of Canada terms of use](https://www.bankofcanada.ca/terms/). Source: Bank of Canada. Content may be used, copied and distributed for free with credit to the Bank of Canada and a note of changes made. Not endorsed by the Bank of Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaseniorloanofficersurvey,
  author    = {Khan, John},
  title     = {Canada Senior Loan Officer Survey},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-senior-loan-officer-survey}
}
```

APA: Khan, J. (2026). *Canada Senior Loan Officer Survey* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-senior-loan-officer-survey

<details><summary>Full notes from the Kaggle page</summary>

## What this is

The Bank of Canada's Senior Loan Officer Survey, tidied from the official Valet group SLOS. The survey collects the views of Canadian financial institutions on price and non-price lending conditions. Series cover overall business lending, mortgage lending (including insured and uninsured mortgages and HELOCs in the combined measures), and non-mortgage household lending.

Source: Bank of Canada Valet group [SLOS](https://www.bankofcanada.ca/valet/observations/group/SLOS/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Coverage

Quarterly balances of opinion from 1999-04-01 to 2026-04-01.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. The Bank of Canada publishes the survey quarterly. Call the official Valet endpoint for a later quarter.

## A few numbers from this snapshot

* The mortgage lending conditions balance of opinion was 0.64 in the quarter starting 2026-04-01.
* Overall business lending conditions were -1.04 in the same quarter.
* The survey file has 109 quarterly observations from 1999-04-01 to 2026-04-01, covering 9 balances of opinion.

## Example uses

* See whether banks are tightening or easing mortgage credit.
* Compare price and non-price conditions, or mortgage conditions with business lending.
* Join the balances of opinion to funds advanced, housing starts or policy rates.

## Caveats

The figures are balances of opinion, not dollar amounts or interest rates. A positive number typically means a net tightening or easing according to the official series description; read that description before you interpret the sign. Combined series average several underlying categories. The survey is a qualitative business-lending questionnaire, not a census of every loan.

## Files

* `slos_long.csv`: Long tidy file.
* `slos_wide.csv`: Wide quarterly file.
* `series_catalog.csv`: Official series list.
* `data_dictionary.csv`: Column dictionary.
* `cover.png`: Cover chart of lending-condition balances.

## Licence

Bank of Canada data are used under the Bank's [terms of use](https://www.bankofcanada.ca/terms/). Please credit the Bank of Canada. The Bank gives no warranty on accuracy. This dataset is not endorsed by the Bank of Canada. The Kaggle licence is set to Other because no standard licence matches these terms exactly. 

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
