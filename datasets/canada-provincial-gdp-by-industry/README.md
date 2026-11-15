<p align="center"><img src="../../assets/theme-economy.png" alt="Canada provincial GDP by industry" width="100%"></p>

# Canada provincial GDP by industry

*Annual real and nominal GDP by sector for 13 provinces and territories*

**Theme:** [Economy, trade and business](../../README.md#economy-trade-and-business) · **Coverage:** January 1997 to January 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-provincial-gdp-by-industry](https://www.kaggle.com/datasets/johnnykhan1/canada-provincial-gdp-by-industry)

## What it is

Annual gross domestic product at basic prices by industry for every province and territory, tidied from Statistics Canada [Table 36-10-0402-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610040201). Values are in millions of dollars, both in chained 2017 dollars (real) and current dollars (nominal).

## Who it helps

Business owners, exporters, economists, investors and students following Canada's output, trade and business activity.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`provincial_gdp_by_industry_annual.csv`](data/provincial_gdp_by_industry_annual.csv) | 4.2 MB | in this repository |
| [`statcan_metadata_36-10-0402.csv`](data/statcan_metadata_36-10-0402.csv) | 42 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `provincial_gdp_by_industry_annual.csv`

Annual GDP at basic prices by industry sector for each province and territory, in chained 2017 dollars and current dollars, from Table 36-10-0402.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `prices` | Text | Chained (2017) dollars for real GDP or Current dollars for nominal GDP. |
| `naics` | Text | Industry sector or special aggregate with its NAICS or table code in brackets. |
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
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_36-10-0402.csv`

Official Statistics Canada cube metadata shipped with Table 36-10-0402-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 36-10-0402-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610040201); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaprovincialgdpbyindustry,
  author    = {Khan, John},
  title     = {Canada provincial GDP by industry},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-provincial-gdp-by-industry}
}
```

APA: Khan, J. (2026). *Canada provincial GDP by industry* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-provincial-gdp-by-industry

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Annual gross domestic product at basic prices by industry for every province and territory, tidied from Statistics Canada [Table 36-10-0402-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610040201). Values are in millions of dollars, both in chained 2017 dollars (real) and current dollars (nominal).

## Coverage

1997 to 2024, annual. Ten provinces and three territories. Kept: all two digit NAICS sectors plus special aggregates such as goods producing, service producing, energy, ICT, public sector and cannabis. Detailed sub industries from the source were left out to keep the file small.

## Updates

Statistics Canada releases a new year each fall, about 11 months after the year ends, and revises earlier years. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Ontario's real GDP at basic prices was 876.6 billion chained 2017 dollars in 2024, up 1.2 percent from 2023.
* Across provinces and territories in 2024, real growth ranged from a decline of 3.3 percent in Yukon to growth of 7.5 percent in Nunavut.
* Mining, quarrying, and oil and gas extraction made up 24.2 percent of Alberta's GDP at current prices in 2021, the latest year with both figures published.
* The file has 26,208 rows for 13 provinces and territories and 36 industry groups, from 1997 to 2024.

## Example uses

* Compare the industry mix of provincial economies.
* Track how dependent each province is on energy, finance or public services.
* Compute real growth rates and productivity with employment data.
* Build provincial features for housing or credit models.

## Caveats

In this release, current dollar values run to 2021 and chained 2017 dollar values run to 2024; later current dollar years are empty with status .. (not available). Chained dollar values are not additive across industries, so sub sectors will not sum to totals in real terms. Current dollar values are additive. Values are in millions (see scalar_factor). Empty values mean no figure was published, often for confidentiality in the territories.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `provincial_gdp_by_industry_annual.csv`: Annual GDP at basic prices by industry sector for each province and territory, in chained 2017 dollars and current dollars, from Table 36-10-0402.
* `statcan_metadata_36-10-0402.csv`: Official cube metadata for Table 36-10-0402-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0402-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
