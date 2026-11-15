<p align="center"><img src="../../assets/theme-rates-and-markets.png" alt="Canada CORRA overnight rate" width="100%"></p>

# Canada CORRA overnight rate

*Daily Canadian Overnight Repo Rate Average and the compounded index*

**Theme:** [Interest rates, credit and markets](../../README.md#interest-rates-credit-and-markets) · **Coverage:** 12 August 1997 to 10 November 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-corra-overnight-rate](https://www.kaggle.com/datasets/johnnykhan1/canada-corra-overnight-rate)

## What it is

The Canadian Overnight Repo Rate Average (CORRA) and the CORRA Compounded Index, tidied from the Bank of Canada's official Valet groups. CORRA is Canada's risk-free rate. It measures the cost of overnight general collateral funding in Canadian dollars, using Government of Canada treasury bills and bonds as collateral for repurchase transactions. The daily file also keeps the Bank's transparency metrics: volume, number of submitters, and percentile rates.

Sources: [CORRA](https://www.bankofcanada.ca/valet/observations/group/CORRA/csv) and [CORRA_COMPOUNDED_INDEX](https://www.bankofcanada.ca/valet/observations/group/CORRA_COMPOUNDED_INDEX/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Who it helps

Borrowers, mortgage professionals, lenders, investors, finance students and economists tracking Canadian rates, credit and the dollar.

## Files

| File | Size | Where |
|---|---:|---|
| [`corra_compounded_index.csv`](data/corra_compounded_index.csv) | 38 KB | in this repository |
| [`corra_daily.csv`](data/corra_daily.csv) | 362 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`series_catalog.csv`](data/series_catalog.csv) | 3 KB | in this repository |

## Columns

### `corra_compounded_index.csv`

Daily CORRA Compounded Index, based at 100 on 12 June 2020.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `corra_compounded_index` | Float | CORRA Compounded Index, starting at 100 on 12 June 2020. |

### `corra_daily.csv`

Daily CORRA, transparency metrics, publication status and calculation methodology.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Observation date as published by the Bank of Canada, YYYY-MM-DD. |
| `corra` | Float | Canadian Overnight Repo Rate Average, in percent. |
| `total_volume_dollars` | Text | Total nominal dollar volume of CORRA-eligible trades before the bottom 25 percent is trimmed. |
| `trimmed_volume_dollars` | Text | Nominal dollar volume of CORRA-eligible trades after the bottom 25 percent is trimmed. |
| `minimum_volume_threshold_dollars` | Text | Dollar volume removed during the trimming step of the CORRA calculation. |
| `number_of_submitters` | Text | Number of unique data submitters used in the CORRA calculation before trimming. |
| `rate_at_trim` | Text | Rate at which the bottom 25 percent of volume was trimmed, in percent. |
| `rate_at_percentile_5` | Text | Rate at the 5th volume-weighted percentile of the trimmed trading volume, in percent. |
| `rate_at_percentile_25` | Text | Rate at the 25th volume-weighted percentile of the trimmed trading volume, in percent. |
| `rate_at_percentile_75` | Text | Rate at the 75th volume-weighted percentile of the trimmed trading volume, in percent. |
| `rate_at_percentile_95` | Text | Rate at the 95th volume-weighted percentile of the trimmed trading volume, in percent. |
| `publication_status` | Text | Whether CORRA was published on that date. |
| `calculation_methodology` | Text | Methodology used to calculate CORRA on that date, as published. |
| `weighted_mean_rate` | Text | Volume-weighted average rate of eligible overnight repurchase transactions, in percent. |
| `mode_rate` | Text | Modal rate, the interest-rate level with the largest traded volume among eligible CORRA transactions, in percent. |

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

## Source and licence

**Source:** Bank of Canada Valet group CORRA: https://www.bankofcanada.ca/valet/observations/group/CORRA/csv; Bank of Canada Valet group CORRA_COMPOUNDED_INDEX: https://www.bankofcanada.ca/valet/observations/group/CORRA_COMPOUNDED_INDEX/csv. Documentation: https://www.bankofcanada.ca/valet/docs. Terms of use: https://www.bankofcanada.ca/terms/. Downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario.

- **Licence:** [Bank of Canada terms of use](https://www.bankofcanada.ca/terms/). Source: Bank of Canada. Content may be used, copied and distributed for free with credit to the Bank of Canada and a note of changes made. Not endorsed by the Bank of Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacorraovernightrate,
  author    = {Khan, John},
  title     = {Canada CORRA overnight rate},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-corra-overnight-rate}
}
```

APA: Khan, J. (2026). *Canada CORRA overnight rate* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-corra-overnight-rate

<details><summary>Full notes from the Kaggle page</summary>

## What this is

The Canadian Overnight Repo Rate Average (CORRA) and the CORRA Compounded Index, tidied from the Bank of Canada's official Valet groups. CORRA is Canada's risk-free rate. It measures the cost of overnight general collateral funding in Canadian dollars, using Government of Canada treasury bills and bonds as collateral for repurchase transactions. The daily file also keeps the Bank's transparency metrics: volume, number of submitters, and percentile rates.

Sources: [CORRA](https://www.bankofcanada.ca/valet/observations/group/CORRA/csv) and [CORRA_COMPOUNDED_INDEX](https://www.bankofcanada.ca/valet/observations/group/CORRA_COMPOUNDED_INDEX/csv). Documentation: https://www.bankofcanada.ca/valet/docs.

## Coverage

Daily CORRA from 1997-08-12 to 2026-11-10. The compounded index runs from 2020-06-12 to 2026-11-10.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. The Bank of Canada publishes CORRA on business days. Call the official Valet endpoint for a later date.

## A few numbers from this snapshot

* CORRA was 2.52 percent on 2026-11-10.
* Trimmed dollar volume that day was 41.36 billion dollars, from 14 unique submitters.
* The daily file has 7,307 observations from 1997-08-12 to 2026-11-10. Volume and percentile fields are populated on more recent dates; the rate itself starts in 1997.
* The compounded index is based at 100 on 2020-06-12 and ends at 118 on 2026-11-10.

## Example uses

* Track Canada's risk-free overnight rate against the Bank of Canada policy rate.
* Study volume, submitter counts and the distribution of trades around the published rate.
* Use the compounded index when you need a cumulative measure of overnight rates.

## Caveats

Volume and percentile metrics are empty on many earlier dates; the rate itself is still published. Publication status and calculation methodology are text fields. The compounded index is provided by the Bank for information only. Weekend and holiday gaps are expected in a business-day series.

## Files

* `corra_daily.csv`: Daily CORRA and transparency metrics.
* `corra_compounded_index.csv`: Daily compounded index.
* `series_catalog.csv`: Official series list.
* `data_dictionary.csv`: Column dictionary.
* `cover.png`: Cover chart of CORRA.

## Licence

Bank of Canada data are used under the Bank's [terms of use](https://www.bankofcanada.ca/terms/). Please credit the Bank of Canada. The Bank gives no warranty on accuracy. This dataset is not endorsed by the Bank of Canada. The Kaggle licence is set to Other because no standard licence matches these terms exactly. 

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
