<p align="center"><img src="../../assets/theme-housing.png" alt="Canada housing starts (CMHC)" width="100%"></p>

# Canada housing starts (CMHC)

*Monthly housing starts for Canada and provinces from CMHC via StatCan*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** June 1990 to September 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-housing-starts-cmhc](https://www.kaggle.com/datasets/johnnykhan1/canada-housing-starts-cmhc)

## What it is

Monthly housing starts for Canada, provinces and selected regions, tidied from Statistics Canada Table 34-10-0159. The figures are produced by Canada Mortgage and Housing Corporation (CMHC) and published through Statistics Canada.

Source table: [34-10-0159](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410015901).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`housing_starts_by_geo.csv`](data/housing_starts_by_geo.csv) | 42 KB | in this repository |
| [`housing_starts_long.csv`](data/housing_starts_long.csv) | 469 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 3 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `housing_starts_by_geo.csv`

Wide file with one column per geography.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. |
| `alberta` | Float | Housing starts for alberta. |
| `atlantic_provinces` | Float | Housing starts for atlantic provinces. |
| `british_columbia` | Float | Housing starts for british columbia. |
| `canada` | Float | Housing starts for canada. |
| `manitoba` | Float | Housing starts for manitoba. |
| `new_brunswick` | Float | Housing starts for new brunswick. |
| `newfoundland_and_labrador` | Float | Housing starts for newfoundland and labrador. |
| `nova_scotia` | Float | Housing starts for nova scotia. |
| `ontario` | Float | Housing starts for ontario. |
| `prairie_provinces` | Float | Housing starts for prairie provinces. |
| `prince_edward_island` | Float | Housing starts for prince edward island. |
| `quebec` | Float | Housing starts for quebec. |
| `saskatchewan` | Float | Housing starts for saskatchewan. |

### `housing_starts_long.csv`

Long tidy file of housing starts by geography and month.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `unit_of_measure` | Text | Unit of measure for value. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. |
| `coordinate` | Integer | Statistics Canada coordinate string inside the table. |
| `value` | Float | Published value. Empty when Statistics Canada did not publish a figure. |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. |
| `symbol` | Text | Additional Statistics Canada symbol when present. |
| `terminated` | Text | t if Statistics Canada terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata shipped with the table download.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official title of the Statistics Canada data table. |
| `Product Id` | Text | Statistics Canada product ID for the table. |
| `CANSIM Id` | Text | Legacy CANSIM identifier for the table, when available. |
| `URL` | Text | URL of the Statistics Canada table. |
| `Cube Notes` | Text | Official notes associated with the Statistics Canada table. |
| `Archive Status` | Text | Status indicating whether the table is current or archived. |
| `Frequency` | Text | Publication frequency of the table. |
| `Start Reference Period` | Text | First reference period available in the table. |
| `End Reference Period` | Date | Last reference period available in the table. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

## Source and licence

**Source:** Statistics Canada Table 34-10-0159, Housing starts, all areas, Canada and provinces (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410015901). Full table CSV downloaded on November 9, 2026. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahousingstartscmhc,
  author    = {Khan, John},
  title     = {Canada housing starts (CMHC)},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-housing-starts-cmhc}
}
```

APA: Khan, J. (2026). *Canada housing starts (CMHC)* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-housing-starts-cmhc

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly housing starts for Canada, provinces and selected regions, tidied from Statistics Canada Table 34-10-0159. The figures are produced by Canada Mortgage and Housing Corporation (CMHC) and published through Statistics Canada.

Source table: [34-10-0159](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410015901).

## Coverage

Monthly series from 1990-06-01 to 2026-09-01 for Canada and provincial geographies as published in the table download.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada and CMHC update housing starts monthly. Download the table again for a later month.

## A few numbers from this snapshot

* Canada housing starts were 250 in the month starting 2026-09-01 (Units, scale thousands).
* That compares with 277 in the same month a year earlier.
* The long file has 5,668 rows across 13 geographies from 1990-06-01 to 2026-09-01.

## Example uses

* Track housing supply against population and prices.
* Compare provincial cycles in residential construction.
* Join to mortgage rates, CPI shelter or labour market series.

## Caveats

* Starts measure construction starts, not completions or inventory of homes for sale.
* Seasonal patterns are strong. Compare year over year or use seasonal adjustment from other CMHC releases if you need it.
* Geography labels follow Statistics Canada. Some regional aggregates appear alongside provinces.
* Values can be missing for some cells. Check status and symbol.

## Files

* `housing_starts_long.csv`: tidy long file.
* `housing_starts_by_geo.csv`: wide file by geography.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes.
* `cover.png`: cover chart.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 34-10-0159 (CMHC). Columns were renamed and the layout was tidied. This is not an official Statistics Canada or CMHC product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
