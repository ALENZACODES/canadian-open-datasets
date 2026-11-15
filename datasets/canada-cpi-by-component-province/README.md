<p align="center"><img src="../../assets/theme-prices.png" alt="Canada CPI by item and province" width="100%"></p>

# Canada CPI by item and province

*Monthly CPI by product group for Canada, the provinces and major cities*

**Theme:** [Prices and inflation](../../README.md#prices-and-inflation) · **Coverage:** January 1914 to September 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-cpi-by-component-province](https://www.kaggle.com/datasets/johnnykhan1/canada-cpi-by-component-province)

## What it is

Canada CPI by item and province, tidied from Statistics Canada Table 18-10-0004-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [18-10-0004-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401).

## Who it helps

Households watching the cost of living, budget planners, journalists, analysts and students studying inflation in Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 72 KB | in this repository |
| [`cpi_all_items_by_geo.csv`](data/cpi_all_items_by_geo.csv) | 140 KB | in this repository |
| [`cpi_canada_major_components.csv`](data/cpi_canada_major_components.csv) | 87 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 10 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 45 KB | in this repository |
| `cpi_long.csv` | 130.6 MB (14.7 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-cpi-by-component-province--cpi_long.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `cpi_all_items_by_geo.csv`

All-items CPI, one column per geography, one row per month.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `alberta` | Float | Published value for alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `british_columbia` | Float | Published value for british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `calgary_alberta` | Float | Published value for calgary alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `canada` | Float | Published value for canada. See unit_of_measure and scalar_factor in the long file for the unit. |
| `charlottetown_and_summerside_prince_edward_island` | Float | Published value for charlottetown and summerside prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `edmonton_alberta` | Float | Published value for edmonton alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `halifax_nova_scotia` | Float | Published value for halifax nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `iqaluit_nunavut` | Text | Published value for iqaluit nunavut. See unit_of_measure and scalar_factor in the long file for the unit. |
| `manitoba` | Float | Published value for manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |
| `montr_al_quebec` | Float | Published value for montr al quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `new_brunswick` | Float | Published value for new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `newfoundland_and_labrador` | Float | Published value for newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nova_scotia` | Float | Published value for nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ontario` | Float | Published value for ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ottawa_gatineau_ontario_part_ontario_quebec` | Float | Published value for ottawa gatineau ontario part ontario quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prince_edward_island` | Float | Published value for prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `quebec` | Float | Published value for quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `qu_bec_quebec` | Float | Published value for qu bec quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `regina_saskatchewan` | Float | Published value for regina saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saint_john_new_brunswick` | Float | Published value for saint john new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatchewan` | Float | Published value for saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatoon_saskatchewan` | Float | Published value for saskatoon saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `st_john_s_newfoundland_and_labrador` | Float | Published value for st john s newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `thunder_bay_ontario` | Float | Published value for thunder bay ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `toronto_ontario` | Float | Published value for toronto ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `vancouver_british_columbia` | Float | Published value for vancouver british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `victoria_british_columbia` | Float | Published value for victoria british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `whitehorse_yukon` | Float | Published value for whitehorse yukon. See unit_of_measure and scalar_factor in the long file for the unit. |
| `winnipeg_manitoba` | Float | Published value for winnipeg manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |
| `yellowknife_northwest_territories` | Float | Published value for yellowknife northwest territories. See unit_of_measure and scalar_factor in the long file for the unit. |

### `cpi_canada_major_components.csv`

Selected major CPI components for Canada only, one column per product group.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `alcoholic_beverages_tobacco_products_and_recreational_cannabis` | Float | Index value (2002 = 100 unless the product name says otherwise) for alcoholic_beverages_tobacco_products_and_recreational_cannabis in Canada. |
| `all_items` | Float | Index value (2002 = 100 unless the product name says otherwise) for all_items in Canada. |
| `all_items_excluding_food_and_energy` | Float | Index value (2002 = 100 unless the product name says otherwise) for all_items_excluding_food_and_energy in Canada. |
| `clothing_and_footwear` | Float | Index value (2002 = 100 unless the product name says otherwise) for clothing_and_footwear in Canada. |
| `energy` | Float | Index value (2002 = 100 unless the product name says otherwise) for energy in Canada. |
| `food` | Float | Index value (2002 = 100 unless the product name says otherwise) for food in Canada. |
| `gasoline` | Float | Index value (2002 = 100 unless the product name says otherwise) for gasoline in Canada. |
| `health_and_personal_care` | Float | Index value (2002 = 100 unless the product name says otherwise) for health_and_personal_care in Canada. |
| `homeowners_replacement_cost` | Float | Index value (2002 = 100 unless the product name says otherwise) for homeowners_replacement_cost in Canada. |
| `household_operations_furnishings_and_equipment` | Float | Index value (2002 = 100 unless the product name says otherwise) for household_operations_furnishings_and_equipment in Canada. |
| `recreation_education_and_reading` | Float | Index value (2002 = 100 unless the product name says otherwise) for recreation_education_and_reading in Canada. |
| `rent` | Float | Index value (2002 = 100 unless the product name says otherwise) for rent in Canada. |
| `shelter` | Float | Index value (2002 = 100 unless the product name says otherwise) for shelter in Canada. |
| `transportation` | Float | Index value (2002 = 100 unless the product name says otherwise) for transportation in Canada. |

### `cpi_long.csv`

Tidy long file of the full CPI table: one row per geography, product group and month.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `product` | Text | CPI product or product group, from All-items down to detailed items. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series (for example v41690973). Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in statcan_table_metadata.csv. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Boolean | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

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

**Source:** Statistics Canada Table 18-10-0004-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/18100004-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacpibycomponentprovince,
  author    = {Khan, John},
  title     = {Canada CPI by item and province},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-cpi-by-component-province}
}
```

APA: Khan, J. (2026). *Canada CPI by item and province* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-cpi-by-component-province

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada CPI by item and province, tidied from Statistics Canada Table 18-10-0004-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [18-10-0004-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401).

## Coverage

The long file keeps the full published table: every geography in the cube (Canada, the provinces and the listed cities), every product group, and the full history from January 1914 where a series exists, through September 2026. The index is not seasonally adjusted. The All-items index uses 2002 = 100. Some detailed food items use a 202404 = 100 base; that is labelled in the product name.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates this table once a month, about three weeks after month end. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* For Canada, the All-items CPI was 170.0 (2002 = 100) in 2026-09.
* The Food index for Canada was 201.8 in the latest month.

## Example uses

* Measure inflation for a province or a major city, not just the national All-items index.
* Compare food, shelter, energy and all-items excluding food and energy to see what is driving prices.
* Convert a dollar series into real terms with the All-items index or a matching product group.

## Caveats

Values can be revised. Empty value cells follow Statistics Canada symbols such as .. (not available) or F (too unreliable). Terminated series are marked in the terminated column. City series do not cover every product group. This index is not seasonally adjusted, so month to month moves include regular seasonal patterns.

## Files

* `cpi_long.csv`: Tidy long file of the full CPI table: one row per geography, product group and month.
* `cpi_all_items_by_geo.csv`: All-items CPI, one column per geography, one row per month.
* `cpi_canada_major_components.csv`: Selected major CPI components for Canada only, one column per product group.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 18-10-0004-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
