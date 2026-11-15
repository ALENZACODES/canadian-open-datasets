<p align="center"><img src="../../assets/theme-housing.png" alt="Canada asking rent and paid rent" width="100%"></p>

# Canada asking rent and paid rent

*Experimental quarterly asking and paid rent for Canadian metro areas*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** January 2019 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-asking-and-paid-rent](https://www.kaggle.com/datasets/johnnykhan1/canada-asking-and-paid-rent)

## What it is

Canada asking rent and paid rent, tidied from Statistics Canada Table 46-10-0092-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [46-10-0092-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4610009201).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`asking_and_paid_rent_long.csv`](data/asking_and_paid_rent_long.csv) | 1.5 MB | in this repository |
| [`asking_rent_apartment_1_bedroom_by_cma.csv`](data/asking_rent_apartment_1_bedroom_by_cma.csv) | 11 KB | in this repository |
| [`cover.png`](data/cover.png) | 78 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 12 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 5 KB | in this repository |

## Columns

### `asking_and_paid_rent_long.csv`

Tidy long file of experimental asking and paid rent by metro area and unit type.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `geo` | Text | Geography name as published by Statistics Canada. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `rental_unit_type` | Text | Rental unit type and bedroom count, as published in the experimental rent table. |
| `estimate_type` | Text | Average asking rent or average paid rent. |
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

### `asking_rent_apartment_1_bedroom_by_cma.csv`

Average asking rent for a 1-bedroom apartment, one column per census metropolitan area.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada (YYYY-MM-DD). For monthly tables this is the first day of the month. For quarterly tables it is the first day of the quarter. For annual tables it is January 1 of the year. |
| `abbotsford_mission_census_metropolitan_area_cma` | Float | Published value for abbotsford mission census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `all_census_metropolitan_areas` | Float | Published value for all census metropolitan areas. See unit_of_measure and scalar_factor in the long file for the unit. |
| `barrie_census_metropolitan_area_cma` | Float | Published value for barrie census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `belleville_quinte_west_census_metropolitan_area_cma` | Float | Published value for belleville quinte west census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `brantford_census_metropolitan_area_cma` | Float | Published value for brantford census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `calgary_census_metropolitan_area_cma` | Float | Published value for calgary census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `chilliwack_census_metropolitan_area_cma` | Float | Published value for chilliwack census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `drummondville_census_metropolitan_area_cma` | Text | Published value for drummondville census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `edmonton_census_metropolitan_area_cma` | Float | Published value for edmonton census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `fredericton_census_metropolitan_area_cma` | Float | Published value for fredericton census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `greater_sudbury_census_metropolitan_area_cma` | Float | Published value for greater sudbury census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `guelph_census_metropolitan_area_cma` | Float | Published value for guelph census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `halifax_census_metropolitan_area_cma` | Float | Published value for halifax census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `hamilton_census_metropolitan_area_cma` | Float | Published value for hamilton census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `kamloops_census_metropolitan_area_cma` | Float | Published value for kamloops census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `kelowna_census_metropolitan_area_cma` | Float | Published value for kelowna census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `kingston_census_metropolitan_area_cma` | Float | Published value for kingston census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `kitchener_cambridge_waterloo_census_metropolitan_area_cma` | Float | Published value for kitchener cambridge waterloo census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `lethbridge_census_metropolitan_area_cma` | Float | Published value for lethbridge census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `london_census_metropolitan_area_cma` | Float | Published value for london census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `moncton_census_metropolitan_area_cma` | Float | Published value for moncton census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `montr_al_census_metropolitan_area_cma` | Float | Published value for montr al census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `nanaimo_census_metropolitan_area_cma` | Float | Published value for nanaimo census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `oshawa_census_metropolitan_area_cma` | Float | Published value for oshawa census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ottawa_gatineau_ontario_part_census_metropolitan_area_cma` | Float | Published value for ottawa gatineau ontario part census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `ottawa_gatineau_quebec_part_census_metropolitan_area_cma` | Float | Published value for ottawa gatineau quebec part census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `peterborough_census_metropolitan_area_cma` | Float | Published value for peterborough census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `qu_bec_census_metropolitan_area_cma` | Float | Published value for qu bec census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `red_deer_census_metropolitan_area_cma` | Float | Published value for red deer census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `regina_census_metropolitan_area_cma` | Float | Published value for regina census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saguenay_census_metropolitan_area_cma` | Text | Published value for saguenay census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saint_john_census_metropolitan_area_cma` | Float | Published value for saint john census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `saskatoon_census_metropolitan_area_cma` | Float | Published value for saskatoon census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `sherbrooke_census_metropolitan_area_cma` | Float | Published value for sherbrooke census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `st_catharines_niagara_census_metropolitan_area_cma` | Float | Published value for st catharines niagara census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `st_john_s_census_metropolitan_area_cma` | Float | Published value for st john s census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `thunder_bay_census_metropolitan_area_cma` | Float | Published value for thunder bay census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `toronto_census_metropolitan_area_cma` | Float | Published value for toronto census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `trois_rivi_res_census_metropolitan_area_cma` | Float | Published value for trois rivi res census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `vancouver_census_metropolitan_area_cma` | Float | Published value for vancouver census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `victoria_census_metropolitan_area_cma` | Float | Published value for victoria census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `windsor_census_metropolitan_area_cma` | Float | Published value for windsor census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |
| `winnipeg_census_metropolitan_area_cma` | Float | Published value for winnipeg census metropolitan area cma. See unit_of_measure and scalar_factor in the long file for the unit. |

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

**Source:** Statistics Canada Table 46-10-0092-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4610009201. Full table CSV downloaded on November 9, 2026 from https://www150.statcan.gc.ca/n1/tbl/csv/46100092-eng.zip. Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaaskingandpaidrent,
  author    = {Khan, John},
  title     = {Canada asking rent and paid rent},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-asking-and-paid-rent}
}
```

APA: Khan, J. (2026). *Canada asking rent and paid rent* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-asking-and-paid-rent

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada asking rent and paid rent, tidied from Statistics Canada Table 46-10-0092-01. The full table was downloaded on November 9, 2026 and laid out as a long CSV plus a wide CSV so it is easier to chart.

Source table: [46-10-0092-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4610009201).

## Coverage

The long file keeps the full experimental table: all 43 published geographies (the all-CMA aggregate and individual census metropolitan areas), all seven rental unit types, and both average asking rent and average paid rent, quarterly from the first quarter of 2019 through the second quarter of 2026 (the cube ends 2026-04-01).

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Statistics Canada has been publishing this experimental table about once a quarter. If you need a later month, download the table again from Statistics Canada.

## A few numbers from this snapshot

* Average asking rent for a 1-bedroom apartment across all census metropolitan areas was 1,730 dollars in the quarter starting 2026-04-01.
* In Toronto the latest average asking rent for the same unit type was 2,090 dollars.
* In Vancouver it was 2,280 dollars.

## Example uses

* Compare asking rent for a 1-bedroom apartment across large metro areas.
* Look at the gap between asking rent and paid rent in a city.
* Follow rent by unit type, including rooms, apartments and houses.

## Caveats

These are experimental estimates. Methods and coverage can change, and Statistics Canada cautions users about comparability. Asking rent is the advertised rent. Paid rent is what tenants reported paying, which can differ from asking rent. There is no official Canada total in this table, only an all census metropolitan areas aggregate. Smaller CMAs can have more missing cells.

## Files

* `asking_and_paid_rent_long.csv`: Tidy long file of experimental asking and paid rent by metro area and unit type.
* `asking_rent_apartment_1_bedroom_by_cma.csv`: Average asking rent for a 1-bedroom apartment, one column per census metropolitan area.
* `data_dictionary.csv`: column dictionary.
* `statcan_table_metadata.csv`: official Statistics Canada notes, survey name and symbol legend.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 46-10-0092-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
