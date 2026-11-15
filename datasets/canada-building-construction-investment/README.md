<p align="center"><img src="../../assets/theme-housing.png" alt="Canada building construction investment" width="100%"></p>

# Canada building construction investment

*Monthly residential and non-residential investment, 2017 to 2026*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 2017 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-building-construction-investment](https://www.kaggle.com/datasets/johnnykhan1/canada-building-construction-investment)

## What it is

Monthly investment in building construction, tidied from Statistics Canada Table 34-10-0293. The geography file keeps Canada, the provinces, the territories and Toronto, with residential, non-residential and total structures. The Canada detail file keeps every published structure type and type of work.

Source table: [34-10-0293-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029301).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`investment_by_geo.csv`](data/investment_by_geo.csv) | 3.5 MB | in this repository |
| [`investment_canada_detail.csv`](data/investment_canada_detail.csv) | 11.7 MB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 8 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `investment_by_geo.csv`

Monthly investment for Canada, the provinces, the territories and Toronto, for residential, non-residential and total structures, all types of work combined, in seasonally adjusted and unadjusted current and constant dollars.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `type_of_structure` | Text | Building type or aggregate, such as total residential, total non-residential, or a more detailed structure type. |
| `type_of_work` | Text | Kind of construction work, such as new construction, renovations, conversions, or the total of all types of work. |
| `investment_value` | Text | Whether the series is seasonally adjusted or unadjusted, and whether it is in current dollars or constant dollars. |
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

### `investment_canada_detail.csv`

Monthly Canada detail by type of structure and type of work, in seasonally adjusted and unadjusted current and constant dollars.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `type_of_structure` | Text | Building type or aggregate, such as total residential, total non-residential, or a more detailed structure type. |
| `type_of_work` | Text | Kind of construction work, such as new construction, renovations, conversions, or the total of all types of work. |
| `investment_value` | Text | Whether the series is seasonally adjusted or unadjusted, and whether it is in current dollars or constant dollars. |
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

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata shipped with Table 34-10-0293-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 34-10-0293-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029301, https://www150.statcan.gc.ca/n1/tbl/csv/34100293-eng.zip). Full table CSV downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadabuildingconstructioninvestment,
  author    = {Khan, John},
  title     = {Canada building construction investment},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-building-construction-investment}
}
```

APA: Khan, J. (2026). *Canada building construction investment* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-building-construction-investment

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly investment in building construction, tidied from Statistics Canada Table 34-10-0293. The geography file keeps Canada, the provinces, the territories and Toronto, with residential, non-residential and total structures. The Canada detail file keeps every published structure type and type of work.

Source table: [34-10-0293-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029301).

## Coverage

January 2017 through 2026-08. Seasonally adjusted and unadjusted series are included, in current dollars and in constant dollars (2023=100).

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. Statistics Canada updates the table monthly. Download the table again for a later month.

## A few numbers from this snapshot

* Seasonally adjusted investment in building construction in Canada was 23.54 billion dollars in 2026-08 (current dollars).
* Residential investment was 16.12 billion dollars in the same month.
* That Canada total is +7.9 percent from the same month a year earlier.
* In Toronto, seasonally adjusted total investment was 4.11 billion dollars in 2026-08.
* The geography file has 20,880 rows across 15 geographies from 2017-01 to 2026-08. Values are in dollars, not millions.

## Example uses

* Track residential construction investment against housing starts, completions or mortgage rates.
* Compare Toronto with the Ontario and Canada totals.
* Separate new construction from renovations in the Canada detail file.

## Caveats

Values are in dollars (not millions). A figure of about 23.5 billion is stored as 23500000000. Constant-dollar series use a 2023 base year. Seasonally adjusted series are better for month-to-month comparisons. Census metropolitan area labels such as Toronto, Ontario follow Statistics Canada geography. This extract drops other census metropolitan areas to keep the file focused.

## Files

* `investment_by_geo.csv`: Canada, provinces, territories and Toronto, structure totals.
* `investment_canada_detail.csv`: Canada detail by structure type and type of work.
* `data_dictionary.csv`: Column dictionary.
* `statcan_table_metadata.csv`: Official Statistics Canada notes.
* `cover.png`: Cover chart of residential and non-residential investment.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 34-10-0293-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
