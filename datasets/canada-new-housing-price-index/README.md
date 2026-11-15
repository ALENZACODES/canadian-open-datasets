<p align="center"><img src="../../assets/theme-housing.png" alt="Canada New Housing Price Index" width="100%"></p>

# Canada New Housing Price Index

*Monthly new house and land prices for Canada, provinces and cities*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** January 1981 to September 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-new-housing-price-index](https://www.kaggle.com/datasets/johnnykhan1/canada-new-housing-price-index)

## What it is

Canada New Housing Price Index, tidied from Statistics Canada Table 18-10-0205-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [18-10-0205-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810020501).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 80 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 9 KB | in this repository |
| [`nhpi_long.csv`](data/nhpi_long.csv) | 7.8 MB | in this repository |
| [`nhpi_total_house_and_land_by_geo.csv`](data/nhpi_total_house_and_land_by_geo.csv) | 107 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 6 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `nhpi_long.csv`

Tidy long file of the New Housing Price Index for every published geography and index type.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `index_type` | Text | New Housing Price Index component: Total (house and land), House only, or Land only. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series (for example v41690973). Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in statcan_table_metadata.csv. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `nhpi_total_house_and_land_by_geo.csv`

Total (house and land) index, one column per geography, one row per month.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `alberta` | Float | Published value for alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `atlantic_region` | Float | Published value for atlantic region. See unit_of_measure and scalar_factor in the long file for the unit. |
| `british_columbia` | Float | Published value for british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `calgary_alberta` | Float | Published value for calgary alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `canada` | Float | Published value for canada. See unit_of_measure and scalar_factor in the long file for the unit. |
| `charlottetown_prince_edward_island` | Float | Published value for charlottetown prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `edmonton_alberta` | Float | Published value for edmonton alberta. See unit_of_measure and scalar_factor in the long file for the unit. |
| `greater_sudbury_ontario` | Float | Published value for greater sudbury ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `guelph_ontario` | Float | Published value for guelph ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `halifax_nova_scotia` | Float | Published value for halifax nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `hamilton_ontario` | Float | Published value for hamilton ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `kelowna_british_columbia` | Float | Published value for kelowna british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `kitchener_cambridge_waterloo_ontario` | Float | Published value for kitchener cambridge waterloo ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `london_ontario` | Float | Published value for london ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `manitoba` | Float | Published value for manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |
| `montr_al_quebec` | Float | Published value for montr al quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `new_brunswick` | Float | Published value for new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `newfoundland_and_labrador` | Float | Published value for newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nova_scotia` | Float | Published value for nova scotia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ontario` | Float | Published value for ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `oshawa_ontario` | Float | Published value for oshawa ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ottawa_gatineau_ontario_part_ontario_quebec` | Float | Published value for ottawa gatineau ontario part ontario quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ottawa_gatineau_quebec_part_ontario_quebec` | Float | Published value for ottawa gatineau quebec part ontario quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prairie_region` | Float | Published value for prairie region. See unit_of_measure and scalar_factor in the long file for the unit. |
| `prince_edward_island` | Float | Published value for prince edward island. See unit_of_measure and scalar_factor in the long file for the unit. |
| `quebec` | Float | Published value for quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `qu_bec_quebec` | Float | Published value for qu bec quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `regina_saskatchewan` | Float | Published value for regina saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saint_john_fredericton_and_moncton_new_brunswick` | Float | Published value for saint john fredericton and moncton new brunswick. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatchewan` | Float | Published value for saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatoon_saskatchewan` | Float | Published value for saskatoon saskatchewan. See unit_of_measure and scalar_factor in the long file for the unit. |
| `sherbrooke_quebec` | Float | Published value for sherbrooke quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `st_catharines_niagara_ontario` | Float | Published value for st catharines niagara ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `st_john_s_newfoundland_and_labrador` | Float | Published value for st john s newfoundland and labrador. See unit_of_measure and scalar_factor in the long file for the unit. |
| `toronto_ontario` | Float | Published value for toronto ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `trois_rivi_res_quebec` | Float | Published value for trois rivi res quebec. See unit_of_measure and scalar_factor in the long file for the unit. |
| `vancouver_british_columbia` | Float | Published value for vancouver british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `victoria_british_columbia` | Float | Published value for victoria british columbia. See unit_of_measure and scalar_factor in the long file for the unit. |
| `windsor_ontario` | Float | Published value for windsor ontario. See unit_of_measure and scalar_factor in the long file for the unit. |
| `winnipeg_manitoba` | Float | Published value for winnipeg manitoba. See unit_of_measure and scalar_factor in the long file for the unit. |

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

**Source:** Statistics Canada Table 18-10-0205-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810020501. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/18100205-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadanewhousingpriceindex,
  author    = {Khan, John},
  title     = {Canada New Housing Price Index},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-new-housing-price-index}
}
```

APA: Khan, J. (2026). *Canada New Housing Price Index* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-new-housing-price-index

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada New Housing Price Index, tidied from Statistics Canada Table 18-10-0205-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [18-10-0205-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810020501).

## Coverage

The long file keeps the full published table: Canada, regions, provinces and the listed metropolitan areas, for Total (house and land), House only and Land only, from January 1981 through September 2026.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada usually updates this table once a month. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* The Canada total (house and land) index was 120.2 in 2026-09.
* That was -2.0% different from the same month a year earlier.
* In the latest month the house-only index was 121.4 and the land-only index was 116.3.

## Example uses

* Follow new home prices nationally and in a specific city such as Toronto, Vancouver or Calgary.
* Separate the house component from the land component.
* Compare new home price growth with CPI shelter or with rents in another dataset.

## Caveats

The New Housing Price Index tracks contractors selling prices of new homes (house and land). It is not a resale price index and it is not a rent index. Not every city is in the table for every period. Values can be revised. Empty cells follow Statistics Canada symbols.

## Files

* `nhpi_long.csv`: Tidy long file of the New Housing Price Index for every published geography and index type.
* `nhpi_total_house_and_land_by_geo.csv`: Total (house and land) index, one column per geography, one row per month.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 18-10-0205-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
