<p align="center"><img src="../../assets/theme-population.png" alt="Canada quarterly population estimates" width="100%"></p>

# Canada quarterly population estimates

*Quarterly population counts for Canada, the provinces and territories*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** January 1946 to July 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-population-estimates-quarterly](https://www.kaggle.com/datasets/johnnykhan1/canada-population-estimates-quarterly)

## What it is

Canada quarterly population estimates, tidied from Statistics Canada Table 17-10-0009-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [17-10-0009-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901).

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 46 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`population_estimates_by_geo.csv`](data/population_estimates_by_geo.csv) | 43 KB | in this repository |
| [`population_estimates_long.csv`](data/population_estimates_long.csv) | 304 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 4 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `population_estimates_by_geo.csv`

Quarterly population, one column per geography.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `alberta` | Float | Published value for alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `british_columbia` | Float | Published value for british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `canada` | Float | Published value for canada. See unit_of_measure and scalar_factor in the long file for the unit. |
| `manitoba` | Float | Published value for manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |
| `new_brunswick` | Float | Published value for new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `newfoundland_and_labrador` | Float | Published value for newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `northwest_territories` | Float | Published value for northwest territories. See unit_of_measure and scalar_factor in the long file for the unit. |
| `northwest_territories_including_nunavut` | Float | Published value for northwest territories including nunavut. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nova_scotia` | Float | Published value for nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nunavut` | Float | Published value for nunavut. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ontario` | Float | Published value for ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prince_edward_island` | Float | Published value for prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `quebec` | Float | Published value for quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatchewan` | Float | Published value for saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `yukon` | Float | Published value for yukon. See unit_of_measure and scalar_factor in the long file for the unit. |

### `population_estimates_long.csv`

Tidy long file of quarterly population estimates for Canada, provinces and territories.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series (for example v41690973). Useful if you want to pull the same series again. |
| `coordinate` | Integer | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in statcan_table_metadata.csv. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

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

**Source:** Statistics Canada Table 17-10-0009-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/17100009-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadapopulationestimatesquarterly,
  author    = {Khan, John},
  title     = {Canada quarterly population estimates},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-population-estimates-quarterly}
}
```

APA: Khan, J. (2026). *Canada quarterly population estimates* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-population-estimates-quarterly

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada quarterly population estimates, tidied from Statistics Canada Table 17-10-0009-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [17-10-0009-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901).

## Coverage

The long file keeps the full published table: Canada, the ten provinces and the territories, quarterly from January 1, 1946 through July 1, 2026. July 1, 2026 is a preliminary postcensal estimate, as noted in the official table metadata.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates quarterly demographic estimates four times a year. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* Canada's estimated population was 41.80 million on 2026-07-01.
* That was 189,425 people, or 0.46%, higher than on 2025-07-01.
* Nunavut and the Northwest Territories are shown separately from July 1, 1991. Before that date the combined series is in the file.

## Example uses

* Build a provincial or national per person series (sales, credit, housing) with a matching quarterly population.
* Compare population growth across provinces and territories.
* Chart long-run population from 1946 to today.

## Caveats

Estimates are revised. In this snapshot, estimates are final intercensal to April 1, 2021, final postcensal from July 1, 2021 to July 1, 2023, updated postcensal from October 1, 2023 to April 1, 2026, and preliminary postcensal for July 1, 2026 (see note 3 in statcan_table_metadata.csv). These are estimates, not census counts.

## Files

* `population_estimates_long.csv`: Tidy long file of quarterly population estimates for Canada, provinces and territories.
* `population_estimates_by_geo.csv`: Quarterly population, one column per geography.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 17-10-0009-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
