<p align="center"><img src="../../assets/theme-housing.png" alt="Canada housing completions (CMHC)" width="100%"></p>

# Canada housing completions (CMHC)

*Quarterly starts, under construction and completions, all areas*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** January 1948 to July 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-housing-completions-cmhc](https://www.kaggle.com/datasets/johnnykhan1/canada-housing-completions-cmhc)

## What it is

Quarterly housing starts, units under construction and housing completions for Canada and the provinces, tidied from Statistics Canada Table 34-10-0135. The figures are produced by Canada Mortgage and Housing Corporation (CMHC) and published through Statistics Canada.

Source table: [34-10-0135-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013501).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`housing_pipeline_canada_total_units.csv`](data/housing_pipeline_canada_total_units.csv) | 24 KB | in this repository |
| [`housing_pipeline_long.csv`](data/housing_pipeline_long.csv) | 7.3 MB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 4 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `housing_pipeline_canada_total_units.csv`

Wide Canada file for total units, with starts, under construction and completions in separate columns.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `seasonal_adjustment` | Text | Unadjusted, or seasonally adjusted at annual rates, as published by CMHC through Statistics Canada. |
| `housing_completions` | Float | Housing completions for Canada, total units. |
| `housing_starts` | Float | Housing starts for Canada, total units. |
| `housing_under_construction` | Float | Housing units under construction for Canada, total units. |

### `housing_pipeline_long.csv`

Long tidy file of CMHC housing starts, units under construction and completions, by geography, unit type and seasonal adjustment.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `housing_estimate` | Text | Whether the row is housing starts, housing under construction, or housing completions. |
| `type_of_unit` | Text | Dwelling type, such as total units, single-detached, semi-detached, row, multiples, or apartment and other. |
| `seasonal_adjustment` | Text | Unadjusted, or seasonally adjusted at annual rates, as published by CMHC through Statistics Canada. |
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

Official Statistics Canada cube metadata shipped with Table 34-10-0135-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 34-10-0135-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013501, https://www150.statcan.gc.ca/n1/tbl/csv/34100135-eng.zip). Full table CSV downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Figures are produced by Canada Mortgage and Housing Corporation (CMHC).

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahousingcompletionscmhc,
  author    = {Khan, John},
  title     = {Canada housing completions (CMHC)},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-housing-completions-cmhc}
}
```

APA: Khan, J. (2026). *Canada housing completions (CMHC)* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-housing-completions-cmhc

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Quarterly housing starts, units under construction and housing completions for Canada and the provinces, tidied from Statistics Canada Table 34-10-0135. The figures are produced by Canada Mortgage and Housing Corporation (CMHC) and published through Statistics Canada.

Source table: [34-10-0135-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013501).

## Coverage

Quarterly series from 1948-01 to 2026-07 for Canada, the provinces and selected regional aggregates, by dwelling type, unadjusted and seasonally adjusted at annual rates.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. CMHC and Statistics Canada update the table quarterly. Download the table again for a later quarter.

## A few numbers from this snapshot

* Starts on the same basis were 171.
* Units under construction in Canada, unadjusted, were 378,042 in 2022-10-01.
* The long file has 56,546 rows across 13 geographies from 1948-01 to 2026-07.

## Example uses

* Follow the housing supply pipeline from starts through units under construction to completions.
* Compare provincial cycles and the mix of single-detached, row and apartment units.
* Join completions to mortgage rates, population or construction investment.

## Caveats

Seasonally adjusted figures are expressed at annual rates and are not the raw quarterly count. Units under construction are a stock, not a flow; starts and completions are flows. Some early years have missing cells. Geography labels follow Statistics Canada and include regional aggregates such as the Atlantic provinces.

## Files

* `housing_pipeline_long.csv`: Long tidy file by geography, estimate, unit type and seasonal adjustment.
* `housing_pipeline_canada_total_units.csv`: Wide Canada totals.
* `data_dictionary.csv`: Column dictionary.
* `statcan_table_metadata.csv`: Official Statistics Canada notes.
* `cover.png`: Cover chart of Canada starts and completions.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 34-10-0135-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario. Figures are produced by CMHC and published through Statistics Canada.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
