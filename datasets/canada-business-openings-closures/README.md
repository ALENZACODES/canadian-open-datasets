<p align="center"><img src="../../assets/theme-economy.png" alt="Canada business openings and closures" width="100%"></p>

# Canada business openings and closures

*Monthly openings, closures and active businesses, 2015 to 2026*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** 2015 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-business-openings-closures](https://www.kaggle.com/datasets/johnnykhan1/canada-business-openings-closures)

## What it is

Monthly experimental estimates of business openings, closures, entrants, exits and active businesses, tidied from Statistics Canada Table 33-10-0270. The geography file keeps the business sector total for Canada, the provinces, the territories and Toronto. The second file keeps every published industry for Canada.

Source table: [33-10-0270-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310027001).

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`business_dynamics_by_geo.csv`](data/business_dynamics_by_geo.csv) | 2.3 MB | in this repository |
| [`business_dynamics_canada_by_industry.csv`](data/business_dynamics_canada_by_industry.csv) | 5.4 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 11 KB | in this repository |

## Columns

### `business_dynamics_by_geo.csv`

Monthly seasonally adjusted business dynamics for the business sector in Canada, the provinces, the territories and Toronto.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `industry` | Text | Industry group for the business openings and closures estimates. |
| `business_dynamics_measure` | Text | Business dynamics concept: active, opening, reopening, closing or temporarily closed businesses, entrants, exits, or continuing businesses. |
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

### `business_dynamics_canada_by_industry.csv`

Monthly seasonally adjusted business dynamics for Canada by industry, including the business sector total and tourism groupings.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `industry` | Text | Industry group for the business openings and closures estimates. |
| `business_dynamics_measure` | Text | Business dynamics concept: active, opening, reopening, closing or temporarily closed businesses, entrants, exits, or continuing businesses. |
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

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata shipped with Table 33-10-0270-01, including notes and the symbol legend. Layout is as published, not tidied.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Column Cube Title from the official source metadata file, as published. |
| `Product Id` | Text | Column Product Id from the official source metadata file, as published. |
| `CANSIM Id` | Text | Column CANSIM Id from the official source metadata file, as published. |
| `URL` | Text | Column URL from the official source metadata file, as published. |
| `Cube Notes` | Text | Column Cube Notes from the official source metadata file, as published. |
| `Archive Status` | Text | Column Archive Status from the official source metadata file, as published. |
| `Frequency` | Text | Column Frequency from the official source metadata file, as published. |
| `Start Reference Period` | Text | Column Start Reference Period from the official source metadata file, as published. |
| `End Reference Period` | Date | Column End Reference Period from the official source metadata file, as published. |
| `Total number of dimensions` | Integer | Column Total number of dimensions from the official source metadata file, as published. |

## Source and licence

**Source:** Statistics Canada Table 33-10-0270-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310027001, https://www150.statcan.gc.ca/n1/tbl/csv/33100270-eng.zip). Full table CSV downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadabusinessopeningsclosures,
  author    = {Khan, John},
  title     = {Canada business openings and closures},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-business-openings-closures}
}
```

APA: Khan, J. (2026). *Canada business openings and closures* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-business-openings-closures

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly experimental estimates of business openings, closures, entrants, exits and active businesses, tidied from Statistics Canada Table 33-10-0270. The geography file keeps the business sector total for Canada, the provinces, the territories and Toronto. The second file keeps every published industry for Canada.

Source table: [33-10-0270-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310027001).

## Coverage

January 2015 through 2026-07, seasonally adjusted, for 15 geographies in the main file and 32 industry groups in the Canada industry file.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. Statistics Canada updates the table monthly. Download the table again for a later month.

## A few numbers from this snapshot

* Opening businesses in the Canada business sector were 45,874 in 2026-07.
* Closing businesses in the same month were 46,823.
* Active businesses were 937,821.
* Opening businesses in Toronto were 10,410 in 2026-07.
* The geography file has 16,650 rows across 15 geographies from 2015-01 to 2026-07. The Canada-by-industry file has 35,520 rows.

## Example uses

* Watch whether more firms are opening than closing in a given month.
* Compare Toronto with Ontario and with Canada.
* Look at openings and closures in construction, retail or finance in the Canada industry file.

## Caveats

These are experimental estimates. Definitions of openings, reopenings, temporary closures, entrants and exits are in the official metadata and are not interchangeable. The series are seasonally adjusted. Other census metropolitan areas besides Toronto were dropped from the geography file to keep it focused. Industry labels include detailed tourism groupings as well as NAICS sectors.

## Files

* `business_dynamics_by_geo.csv`: Business sector totals by geography.
* `business_dynamics_canada_by_industry.csv`: Canada by industry.
* `data_dictionary.csv`: Column dictionary.
* `statcan_table_metadata.csv`: Official Statistics Canada notes.
* `cover.png`: Cover chart of Canada openings and closures.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 33-10-0270-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
