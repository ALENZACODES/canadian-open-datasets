<p align="center"><img src="../../assets/theme-housing.png" alt="Canada building permits monthly" width="100%"></p>

# Canada building permits monthly

*Monthly permit values and dwelling units by province, 2018 to 2026*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 2018 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-building-permits-monthly](https://www.kaggle.com/datasets/johnnykhan1/canada-building-permits-monthly)

## What it is

Canada building permits monthly, tidied from Statistics Canada Table 34-10-0292-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [34-10-0292-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029201).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`building_permits_long.csv`](data/building_permits_long.csv) | 8.2 MB | in this repository |
| [`cover.png`](data/cover.png) | 132 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`permit_values_sa_total_by_province.csv`](data/permit_values_sa_total_by_province.csv) | 14 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 16 KB | in this repository |

## Columns

### `building_permits_long.csv`

Tidy long file of building permits for Canada, provinces and territories, selected aggregates.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `type_of_building` | Text | Building type or aggregate (for example total residential or total non-residential). |
| `type_of_work` | Text | Type of work covered by the permit (this file keeps the total). |
| `variable` | Text | Measure: value of permits, number of permits, or dwelling units created, lost or demolished. |
| `seasonal_adjustment` | Text | Whether the series is seasonally adjusted and whether it is in current or constant dollars. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series (for example v41690973). Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in statcan_table_metadata.csv. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `permit_values_sa_total_by_province.csv`

Seasonally adjusted current-dollar value of all permits, one column per geography.

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
| `nova_scotia` | Float | Published value for nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nunavut` | Float | Published value for nunavut. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ontario` | Float | Published value for ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prince_edward_island` | Float | Published value for prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `quebec` | Float | Published value for quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatchewan` | Float | Published value for saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `yukon` | Float | Published value for yukon. See unit_of_measure and scalar_factor in the long file for the unit. |

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

**Source:** Statistics Canada Table 34-10-0292-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029201. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/34100292-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadabuildingpermitsmonthly,
  author    = {Khan, John},
  title     = {Canada building permits monthly},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-building-permits-monthly}
}
```

APA: Khan, J. (2026). *Canada building permits monthly* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-building-permits-monthly

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada building permits monthly, tidied from Statistics Canada Table 34-10-0292-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [34-10-0292-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029201).

## Coverage

The long file covers January 2018 through August 2026 for Canada, the ten provinces and the three territories. It keeps seven building aggregates (total, residential, non-residential, single, industrial, commercial, and institutional and governmental), types of work total, all five variables, and both unadjusted current-dollar and seasonally adjusted current-dollar series. Census metropolitan areas, constant-dollar series, and detailed building types from the original 375,864-series table were left out.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates the source table once a month. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* Seasonally adjusted permit values for Canada, all buildings, were 13.57 million (see scalar_factor, usually thousands of dollars) in 2026-08.
* In the latest month, residential permits were 8.47 million and non-residential permits were 5.10 million on the same basis.
* The source table includes census metropolitan areas and many detailed building types. Those rows were left out so this file stays focused on Canada and the provinces and territories.

## Example uses

* Follow the value of residential and non-residential permits nationally and by province.
* Compare dwelling units created with units demolished in a province.
* Use the seasonally adjusted current-dollar series as a timely construction signal.

## Caveats

Permit values are intentions, not completed construction. A large project can move a monthly total a lot, especially in a smaller province. Statistics Canada corrected dwelling units demolished figures on June 25, 2025 for 2018 to 2021. Values can be revised again. Single is the published aggregate of that name, not every detailed single-dwelling category.

## Files

* `building_permits_long.csv`: Tidy long file of building permits for Canada, provinces and territories, selected aggregates.
* `permit_values_sa_total_by_province.csv`: Seasonally adjusted current-dollar value of all permits, one column per geography.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 34-10-0292-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
