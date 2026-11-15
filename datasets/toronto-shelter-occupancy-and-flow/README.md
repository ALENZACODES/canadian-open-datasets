<p align="center"><img src="../../assets/theme-housing.png" alt="Toronto Shelter Occupancy and System Flow" width="100%"></p>

# Toronto Shelter Occupancy and System Flow

*Daily occupancy totals and monthly flow, 2021 to 2026*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 1 January 2021 to 8 November 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-shelter-occupancy-and-flow](https://www.kaggle.com/datasets/johnnykhan1/toronto-shelter-occupancy-and-flow)

## What it is

Daily occupancy and capacity of overnight shelter and allied programs run or funded by the City of Toronto, 2021-01-01 to 2026-11-08, plus the City's monthly Shelter System Flow file. The official occupancy file is a daily list of programs, including site addresses. This version rolls those program rows up to citywide and sector totals so you can study capacity and occupancy without a long address-level time series. A snapshot of programs and public addresses is included for the latest date only.

Daily program totals 2021-01-01 to 2026-11-08. Last day in the file (2026-11-08): 6,767 people staying overnight.

Older Kaggle copies of Toronto shelter occupancy stop in 2021. This file includes every later official annual extract, and the 2026 file that the City updated on November 9, 2026.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 69 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 11 KB | in this repository |
| [`shelter_occupancy_citywide_daily.csv`](data/shelter_occupancy_citywide_daily.csv) | 179 KB | in this repository |
| [`shelter_occupancy_daily_by_program_area.csv`](data/shelter_occupancy_daily_by_program_area.csv) | 3.3 MB | in this repository |
| [`shelter_occupancy_daily_by_sector.csv`](data/shelter_occupancy_daily_by_sector.csv) | 4.3 MB | in this repository |
| [`shelter_programs_latest_snapshot.csv`](data/shelter_programs_latest_snapshot.csv) | 32 KB | in this repository |
| [`shelter_system_flow_monthly.csv`](data/shelter_system_flow_monthly.csv) | 81 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `shelter_occupancy_citywide_daily.csv`

Citywide daily totals of people staying overnight, bed and room capacity, and occupancy rates.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Occupancy date (YYYY-MM-DD). |
| `programs` | Integer | Number of distinct programs reporting that day in the group. |
| `service_users` | Integer | Sum of service users staying overnight. |
| `occupied_beds` | Float | Sum of occupied beds (bed-based programs). |
| `unoccupied_beds` | Float | Sum of unoccupied beds. |
| `unavailable_beds` | Float | Sum of unavailable beds. |
| `capacity_actual_beds` | Float | Sum of actual bed capacity. |
| `occupied_rooms` | Float | Sum of occupied rooms (room-based programs). |
| `unoccupied_rooms` | Float | Sum of unoccupied rooms. |
| `unavailable_rooms` | Float | Sum of unavailable rooms. |
| `capacity_actual_rooms` | Float | Sum of actual room capacity. |
| `bed_occupancy_rate` | Float | occupied_beds divided by capacity_actual_beds, from the summed figures. Empty when bed capacity is zero. |
| `room_occupancy_rate` | Float | occupied_rooms divided by capacity_actual_rooms, from the summed figures. Empty when room capacity is zero. |

### `shelter_occupancy_daily_by_program_area.csv`

Daily totals by program area and sector.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Occupancy date (YYYY-MM-DD). |
| `PROGRAM_AREA` | Text | — |
| `SECTOR` | Text | — |
| `programs` | Integer | Number of distinct programs reporting that day in the group. |
| `service_users` | Integer | Sum of service users staying overnight. |
| `occupied_beds` | Float | Sum of occupied beds (bed-based programs). |
| `unoccupied_beds` | Float | Sum of unoccupied beds. |
| `unavailable_beds` | Float | Sum of unavailable beds. |
| `capacity_actual_beds` | Float | Sum of actual bed capacity. |
| `occupied_rooms` | Float | Sum of occupied rooms (room-based programs). |
| `unoccupied_rooms` | Float | Sum of unoccupied rooms. |
| `unavailable_rooms` | Float | Sum of unavailable rooms. |
| `capacity_actual_rooms` | Float | Sum of actual room capacity. |
| `bed_occupancy_rate` | Float | occupied_beds divided by capacity_actual_beds, from the summed figures. Empty when bed capacity is zero. |
| `room_occupancy_rate` | Float | occupied_rooms divided by capacity_actual_rooms, from the summed figures. Empty when room capacity is zero. |

### `shelter_occupancy_daily_by_sector.csv`

Daily totals by sector, program model and overnight service type.

| Column | Type | Description |
|---|---|---|
| `date` | Date | Occupancy date (YYYY-MM-DD). |
| `SECTOR` | Text | — |
| `PROGRAM_MODEL` | Text | — |
| `OVERNIGHT_SERVICE_TYPE` | Text | — |
| `programs` | Integer | Number of distinct programs reporting that day in the group. |
| `service_users` | Integer | Sum of service users staying overnight. |
| `occupied_beds` | Float | Sum of occupied beds (bed-based programs). |
| `unoccupied_beds` | Float | Sum of unoccupied beds. |
| `unavailable_beds` | Float | Sum of unavailable beds. |
| `capacity_actual_beds` | Float | Sum of actual bed capacity. |
| `occupied_rooms` | Float | Sum of occupied rooms (room-based programs). |
| `unoccupied_rooms` | Float | Sum of unoccupied rooms. |
| `unavailable_rooms` | Float | Sum of unavailable rooms. |
| `capacity_actual_rooms` | Float | Sum of actual room capacity. |
| `bed_occupancy_rate` | Float | occupied_beds divided by capacity_actual_beds, from the summed figures. Empty when bed capacity is zero. |
| `room_occupancy_rate` | Float | occupied_rooms divided by capacity_actual_rooms, from the summed figures. Empty when room capacity is zero. |

### `shelter_programs_latest_snapshot.csv`

Program and location list for the latest date in the file, including the official public addresses. This is a snapshot, not a daily time series at the address level.

| Column | Type | Description |
|---|---|---|
| `snapshot_date` | Date | Latest-day value for snapshot_date, from the official program list. |
| `organization_name` | Text | Latest-day value for organization_name, from the official program list. |
| `shelter_group` | Text | Latest-day value for shelter_group, from the official program list. |
| `location_name` | Text | Latest-day value for location_name, from the official program list. |
| `location_address` | Text | Latest-day value for location_address, from the official program list. |
| `location_postal_code` | Text | Latest-day value for location_postal_code, from the official program list. |
| `location_city` | Text | Latest-day value for location_city, from the official program list. |
| `program_name` | Text | Latest-day value for program_name, from the official program list. |
| `program_id` | Text | Latest-day value for program_id, from the official program list. |
| `sector` | Text | Population sector as published (for example Families, Mixed Adult, Youth, or Women). |
| `program_model` | Text | Program model, for example Emergency. |
| `overnight_service_type` | Text | Overnight service type, for example Shelter or Motel/Hotel Shelter. |
| `program_area` | Text | Program area as published. |
| `capacity_type` | Text | Latest-day value for capacity_type, from the official program list. |
| `service_users` | Integer | Sum of service users staying overnight. |
| `occupied_beds` | Float | Sum of occupied beds (bed-based programs). |
| `capacity_actual_beds` | Float | Sum of actual bed capacity. |
| `occupied_rooms` | Float | Sum of occupied rooms (room-based programs). |
| `capacity_actual_rooms` | Float | Sum of actual room capacity. |

### `shelter_system_flow_monthly.csv`

Monthly Shelter System Flow figures (people entering, leaving, and actively homeless), as published.

| Column | Type | Description |
|---|---|---|
| `id` | Text | Shelter System Flow field id, as published (snake_case names). month_start is the first day of the published month. |
| `month` | Date | Shelter System Flow field month, as published (snake_case names). month_start is the first day of the published month. |
| `population_group` | Text | Shelter System Flow field population_group, as published (snake_case names). month_start is the first day of the published month. |
| `returned_from_housing` | Integer | Shelter System Flow field returned_from_housing, as published (snake_case names). month_start is the first day of the published month. |
| `returned_to_shelter` | Integer | Shelter System Flow field returned_to_shelter, as published (snake_case names). month_start is the first day of the published month. |
| `newly_identified` | Integer | Shelter System Flow field newly_identified, as published (snake_case names). month_start is the first day of the published month. |
| `moved_to_housing` | Integer | Shelter System Flow field moved_to_housing, as published (snake_case names). month_start is the first day of the published month. |
| `became_inactive` | Integer | Shelter System Flow field became_inactive, as published (snake_case names). month_start is the first day of the published month. |
| `actively_homeless` | Integer | Shelter System Flow field actively_homeless, as published (snake_case names). month_start is the first day of the published month. |
| `ageunder16` | Integer | Shelter System Flow field ageunder16, as published (snake_case names). month_start is the first day of the published month. |
| `age16_24` | Integer | Shelter System Flow field age16_24, as published (snake_case names). month_start is the first day of the published month. |
| `age25_34` | Integer | Shelter System Flow field age25_34, as published (snake_case names). month_start is the first day of the published month. |
| `age35_44` | Integer | Shelter System Flow field age35_44, as published (snake_case names). month_start is the first day of the published month. |
| `age45_54` | Integer | Shelter System Flow field age45_54, as published (snake_case names). month_start is the first day of the published month. |
| `age55_64` | Integer | Shelter System Flow field age55_64, as published (snake_case names). month_start is the first day of the published month. |
| `age65over` | Integer | Shelter System Flow field age65over, as published (snake_case names). month_start is the first day of the published month. |
| `gender_male` | Integer | Shelter System Flow field gender_male, as published (snake_case names). month_start is the first day of the published month. |
| `gender_female` | Integer | Shelter System Flow field gender_female, as published (snake_case names). month_start is the first day of the published month. |
| `gender_transgender_non_binary_or_two_spirit` | Integer | Shelter System Flow field gender_transgender_non_binary_or_two_spirit, as published (snake_case names). month_start is the first day of the published month. |
| `population_group_percentage` | Text | Shelter System Flow field population_group_percentage, as published (snake_case names). month_start is the first day of the published month. |
| `month_start` | Date | Shelter System Flow field month_start, as published (snake_case names). month_start is the first day of the published month. |

## Source and licence

**Source:** City of Toronto Open Data, Daily Shelter and Overnight Service Occupancy and Capacity (https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/), and Toronto Shelter System Flow (https://open.toronto.ca/dataset/toronto-shelter-system-flow/). Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoshelteroccupancyandflow,
  author    = {Khan, John},
  title     = {Toronto Shelter Occupancy and System Flow},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-shelter-occupancy-and-flow}
}
```

APA: Khan, J. (2026). *Toronto Shelter Occupancy and System Flow* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-shelter-occupancy-and-flow

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Daily occupancy and capacity of overnight shelter and allied programs run or funded by the City of Toronto, 2021-01-01 to 2026-11-08, plus the City's monthly Shelter System Flow file. The official occupancy file is a daily list of programs, including site addresses. This version rolls those program rows up to citywide and sector totals so you can study capacity and occupancy without a long address-level time series. A snapshot of programs and public addresses is included for the latest date only.

Daily program totals 2021-01-01 to 2026-11-08. Last day in the file (2026-11-08): 6,767 people staying overnight.

Older Kaggle copies of Toronto shelter occupancy stop in 2021. This file includes every later official annual extract, and the 2026 file that the City updated on November 9, 2026.

## Files

| File | What is in it |
|---|---|
| `shelter_occupancy_citywide_daily.csv` | Citywide daily totals |
| `shelter_occupancy_daily_by_sector.csv` | Daily totals by sector, program model and service type |
| `shelter_occupancy_daily_by_program_area.csv` | Daily totals by program area and sector |
| `shelter_programs_latest_snapshot.csv` | Programs and public addresses on the latest date |
| `shelter_system_flow_monthly.csv` | Monthly inflows, outflows and actively homeless counts |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from average daily occupancy by year |

## Coverage and refresh

Occupancy is published by Toronto Shelter and Support Services and is updated frequently, often daily. I pulled the annual files and the current 2026 file on November 9, 2026. The Shelter System Flow file is a separate monthly product. Programs open, close and change names, so program counts are not a constant stock of buildings.

## Caveats

* `service_users` is the official overnight count of people staying in the program that night. Bed-based and room-based programs are both in the file. A room can hold more than one person, so do not add occupied beds and occupied rooms and call the total the number of people.
* Occupancy rates are computed from the summed occupied and capacity columns in each group. They can differ from a program-level average of the official rate fields.
* Some people experiencing homelessness are not in this system on a given night.
* The latest-day snapshot includes official public addresses of programs. It is not a daily trace of who stayed at a site.
* Shelter System Flow population groups overlap (for example All Population and Chronic). Do not add those groups together.

## Sources

Daily Shelter and Overnight Service Occupancy and Capacity: https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/

Toronto Shelter System Flow: https://open.toronto.ca/dataset/toronto-shelter-system-flow/

Pulled on November 9, 2026.

## Example uses

* Follow citywide overnight occupancy and occupancy rates through 2022 to 2026.
* Compare family, youth and mixed adult sectors over the same winter.
* Join monthly occupancy averages to the Shelter System Flow actively homeless series.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). This dataset is not endorsed by the City of Toronto.

Changes made here: daily program rows were aggregated to citywide, sector and program-area totals, occupancy rates were computed from those sums, columns were renamed to snake_case, and a latest-day program snapshot was saved. Source counts were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
