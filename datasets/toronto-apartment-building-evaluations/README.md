<p align="center"><img src="../../assets/theme-housing.png" alt="Toronto apartment building evaluations" width="100%"></p>

# Toronto apartment building evaluations

*RentSafeTO evaluation scores and registration for rental apartments*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 2017 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-apartment-building-evaluations](https://www.kaggle.com/datasets/johnnykhan1/toronto-apartment-building-evaluations)

## What it is

RentSafeTO apartment building evaluations and registration records from the City of Toronto. RentSafeTO is the City's bylaw enforcement program for rental apartment buildings with three or more storeys or 10 or more units. The evaluation file stacks the official pre-2023 extract with the 2023-to-current extract. The registration file describes each registered building.

Sources: [Apartment Building Evaluation](https://open.toronto.ca/dataset/apartment-building-evaluation/) and [Apartment Building Registration](https://open.toronto.ca/dataset/apartment-building-registration/) on Toronto Open Data.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`apartment_evaluations.csv`](data/apartment_evaluations.csv) | 6.6 MB | in this repository |
| [`apartment_registration.csv`](data/apartment_registration.csv) | 1.6 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 21 KB | in this repository |

## Columns

### `apartment_evaluations.csv`

Stacked RentSafeTO apartment building evaluations, combining the pre-2023 extract with the 2023-to-current extract.

| Column | Type | Description |
|---|---|---|
| `row_id` | Text | Source row identifier from the City of Toronto extract. |
| `rsn` | Integer | RentSafeTO site number, used to link evaluations to the registration file. |
| `year_registered` | Float | year registered as published in the City of Toronto RentSafeTO extract. |
| `year_evaluated` | Text | year evaluated as published in the City of Toronto RentSafeTO extract. |
| `year_built` | Float | Year the building was built, as registered or evaluated. |
| `property_type` | Text | Property type as published by the City. |
| `ward` | Integer | Toronto city ward as published. |
| `wardname` | Text | wardname as published in the City of Toronto RentSafeTO extract. |
| `site_address` | Text | Street address of the apartment building. |
| `confirmed_storeys` | Integer | Number of storeys confirmed for the building. |
| `confirmed_units` | Integer | Number of units confirmed for the building. |
| `evaluation_completed_on` | Date | Date the evaluation was completed, as published by the City. |
| `score` | Float | Building evaluation score from the pre-2023 extract, as published. |
| `results_of_score` | Text | results of score as published in the City of Toronto RentSafeTO extract. |
| `no_of_areas_evaluated` | Integer | no of areas evaluated as published in the City of Toronto RentSafeTO extract. |
| `entrance_lobby` | Float | entrance lobby as published in the City of Toronto RentSafeTO extract. |
| `entrance_doors_windows` | Float | entrance doors windows as published in the City of Toronto RentSafeTO extract. |
| `security` | Float | security as published in the City of Toronto RentSafeTO extract. |
| `stairwells` | Float | stairwells as published in the City of Toronto RentSafeTO extract. |
| `laundry_rooms` | Float | laundry rooms as published in the City of Toronto RentSafeTO extract. |
| `internal_guards_handrails` | Float | internal guards handrails as published in the City of Toronto RentSafeTO extract. |
| `garbage_chute_rooms` | Float | garbage chute rooms as published in the City of Toronto RentSafeTO extract. |
| `garbage_bin_storage_area` | Float | garbage bin storage area as published in the City of Toronto RentSafeTO extract. |
| `elevators` | Float | elevators as published in the City of Toronto RentSafeTO extract. |
| `storage_areas_lockers` | Float | storage areas lockers as published in the City of Toronto RentSafeTO extract. |
| `interior_wall_ceiling_floor` | Float | interior wall ceiling floor as published in the City of Toronto RentSafeTO extract. |
| `interior_lighting_levels` | Float | interior lighting levels as published in the City of Toronto RentSafeTO extract. |
| `graffiti` | Float | graffiti as published in the City of Toronto RentSafeTO extract. |
| `exterior_cladding` | Float | exterior cladding as published in the City of Toronto RentSafeTO extract. |
| `exterior_grounds` | Float | exterior grounds as published in the City of Toronto RentSafeTO extract. |
| `exterior_walkways` | Float | exterior walkways as published in the City of Toronto RentSafeTO extract. |
| `balcony_guards` | Float | balcony guards as published in the City of Toronto RentSafeTO extract. |
| `water_pen_ext_bldg_elements` | Float | water pen ext bldg elements as published in the City of Toronto RentSafeTO extract. |
| `parking_area` | Float | parking area as published in the City of Toronto RentSafeTO extract. |
| `other_facilities` | Float | other facilities as published in the City of Toronto RentSafeTO extract. |
| `grid` | Text | grid as published in the City of Toronto RentSafeTO extract. |
| `latitude` | Text | latitude as published in the City of Toronto RentSafeTO extract. |
| `longitude` | Text | longitude as published in the City of Toronto RentSafeTO extract. |
| `x` | Float | x as published in the City of Toronto RentSafeTO extract. |
| `y` | Float | y as published in the City of Toronto RentSafeTO extract. |
| `evaluation_period` | Text | Which official extract the row came from: pre_2023, or 2023_current. |
| `current_building_eval_score` | Text | Current building evaluation score from the 2023-to-current extract, as published. |
| `proactive_building_score` | Text | proactive building score as published in the City of Toronto RentSafeTO extract. |
| `current_reactive_score` | Text | current reactive score as published in the City of Toronto RentSafeTO extract. |
| `numbering_of_property` | Text | numbering of property as published in the City of Toronto RentSafeTO extract. |
| `fencing` | Text | fencing as published in the City of Toronto RentSafeTO extract. |
| `retaining_walls` | Text | retaining walls as published in the City of Toronto RentSafeTO extract. |
| `catch_basins_storm_drainage` | Text | catch basins storm drainage as published in the City of Toronto RentSafeTO extract. |
| `building_exterior` | Text | building exterior as published in the City of Toronto RentSafeTO extract. |
| `windows` | Text | windows as published in the City of Toronto RentSafeTO extract. |
| `ext_receptacle_storage_area` | Text | ext receptacle storage area as published in the City of Toronto RentSafeTO extract. |
| `clothing_drop_boxes` | Text | clothing drop boxes as published in the City of Toronto RentSafeTO extract. |
| `accessory_buildings` | Text | accessory buildings as published in the City of Toronto RentSafeTO extract. |
| `intercom` | Text | intercom as published in the City of Toronto RentSafeTO extract. |
| `emergency_contact_sign` | Text | emergency contact sign as published in the City of Toronto RentSafeTO extract. |
| `lobby_walls_and_ceiling` | Text | lobby walls and ceiling as published in the City of Toronto RentSafeTO extract. |
| `lobby_floors` | Text | lobby floors as published in the City of Toronto RentSafeTO extract. |
| `laundry_room` | Text | laundry room as published in the City of Toronto RentSafeTO extract. |
| `int_receptacle_storage_area` | Text | int receptacle storage area as published in the City of Toronto RentSafeTO extract. |
| `mail_receptacles` | Text | mail receptacles as published in the City of Toronto RentSafeTO extract. |
| `exterior_doors` | Text | exterior doors as published in the City of Toronto RentSafeTO extract. |
| `storage_areas_lockers_maint` | Text | storage areas lockers maint as published in the City of Toronto RentSafeTO extract. |
| `pools` | Text | pools as published in the City of Toronto RentSafeTO extract. |
| `other_amenities` | Text | other amenities as published in the City of Toronto RentSafeTO extract. |
| `parking_areas` | Text | parking areas as published in the City of Toronto RentSafeTO extract. |
| `abandoned_equip_derelict_veh` | Text | abandoned equip derelict veh as published in the City of Toronto RentSafeTO extract. |
| `garbage_compactor_room` | Text | garbage compactor room as published in the City of Toronto RentSafeTO extract. |
| `elevator_maintenance` | Text | elevator maintenance as published in the City of Toronto RentSafeTO extract. |
| `elevator_cosmetics` | Text | elevator cosmetics as published in the City of Toronto RentSafeTO extract. |
| `int_hallway_walls_ceiling` | Text | int hallway walls ceiling as published in the City of Toronto RentSafeTO extract. |
| `interior_hallway_floors` | Text | interior hallway floors as published in the City of Toronto RentSafeTO extract. |
| `int_lobby_hallway_lighting` | Text | int lobby hallway lighting as published in the City of Toronto RentSafeTO extract. |
| `common_area_ventilation` | Text | common area ventilation as published in the City of Toronto RentSafeTO extract. |
| `electrical_services_outlets` | Text | electrical services outlets as published in the City of Toronto RentSafeTO extract. |
| `chute_rooms_maintenance` | Text | chute rooms maintenance as published in the City of Toronto RentSafeTO extract. |
| `stairwell_walls_and_ceiling` | Text | stairwell walls and ceiling as published in the City of Toronto RentSafeTO extract. |
| `stairwell_landing_and_steps` | Text | stairwell landing and steps as published in the City of Toronto RentSafeTO extract. |
| `stairwell_lighting` | Text | stairwell lighting as published in the City of Toronto RentSafeTO extract. |
| `int_handrail_guard_safety` | Text | int handrail guard safety as published in the City of Toronto RentSafeTO extract. |
| `int_handrail_guard_maint` | Text | int handrail guard maint as published in the City of Toronto RentSafeTO extract. |
| `building_cleanliness` | Text | building cleanliness as published in the City of Toronto RentSafeTO extract. |
| `common_area_pests` | Text | common area pests as published in the City of Toronto RentSafeTO extract. |
| `tenant_notification_board` | Text | tenant notification board as published in the City of Toronto RentSafeTO extract. |
| `pest_control_log` | Text | pest control log as published in the City of Toronto RentSafeTO extract. |
| `maintenance_log` | Text | maintenance log as published in the City of Toronto RentSafeTO extract. |
| `cleaning_log` | Text | cleaning log as published in the City of Toronto RentSafeTO extract. |
| `vital_service_plan` | Text | vital service plan as published in the City of Toronto RentSafeTO extract. |
| `electrical_safety_plan` | Text | electrical safety plan as published in the City of Toronto RentSafeTO extract. |
| `state_of_good_repair_plan` | Text | state of good repair plan as published in the City of Toronto RentSafeTO extract. |
| `tenant_service_request_log` | Text | tenant service request log as published in the City of Toronto RentSafeTO extract. |
| `evaluation_year` | Integer | Calendar year of the evaluation, taken from evaluation_completed_on when present, otherwise from a cleaned year_evaluated value. Year values stored as YYYYMM in the source were converted to calendar years. |
| `combined_score` | Float | Single score column: score from the pre-2023 extract, or current_building_eval_score from the 2023-to-current extract. |

### `apartment_registration.csv`

RentSafeTO apartment building registration attributes, including units, storeys, amenities and safety equipment.

| Column | Type | Description |
|---|---|---|
| `row_id` | Text | Source row identifier from the City of Toronto extract. |
| `air_conditioning_type` | Text | air conditioning type as published in the City of Toronto RentSafeTO extract. |
| `amenities_available` | Text | amenities available as published in the City of Toronto RentSafeTO extract. |
| `annual_fire_alarm_test_records` | Boolean | annual fire alarm test records as published in the City of Toronto RentSafeTO extract. |
| `annual_fire_pump_flow_test_records` | Boolean | annual fire pump flow test records as published in the City of Toronto RentSafeTO extract. |
| `approved_fire_safety_plan` | Boolean | approved fire safety plan as published in the City of Toronto RentSafeTO extract. |
| `balconies` | Boolean | balconies as published in the City of Toronto RentSafeTO extract. |
| `barrier_free_accessibilty_entr` | Boolean | barrier free accessibilty entr as published in the City of Toronto RentSafeTO extract. |
| `bike_parking` | Text | bike parking as published in the City of Toronto RentSafeTO extract. |
| `confirmed_storeys` | Integer | Number of storeys confirmed for the building. |
| `confirmed_units` | Integer | Number of units confirmed for the building. |
| `date_of_last_inspection_by_tssa` | Date | date of last inspection by tssa as published in the City of Toronto RentSafeTO extract. |
| `description_of_child_play_area` | Text | description of child play area as published in the City of Toronto RentSafeTO extract. |
| `description_of_indoor_exercise_room` | Text | description of indoor exercise room as published in the City of Toronto RentSafeTO extract. |
| `description_of_outdoor_rec_facilities` | Text | description of outdoor rec facilities as published in the City of Toronto RentSafeTO extract. |
| `elevator_parts_replaced` | Text | elevator parts replaced as published in the City of Toronto RentSafeTO extract. |
| `elevator_status` | Text | elevator status as published in the City of Toronto RentSafeTO extract. |
| `emerg_power_supply_test_records` | Boolean | emerg power supply test records as published in the City of Toronto RentSafeTO extract. |
| `exterior_fire_escape` | Boolean | exterior fire escape as published in the City of Toronto RentSafeTO extract. |
| `facilities_available` | Text | facilities available as published in the City of Toronto RentSafeTO extract. |
| `fire_alarm` | Boolean | fire alarm as published in the City of Toronto RentSafeTO extract. |
| `garbage_chutes` | Boolean | garbage chutes as published in the City of Toronto RentSafeTO extract. |
| `green_bin_location` | Text | green bin location as published in the City of Toronto RentSafeTO extract. |
| `heating_equipment_status` | Text | heating equipment status as published in the City of Toronto RentSafeTO extract. |
| `heating_equipment_year_installed` | Float | heating equipment year installed as published in the City of Toronto RentSafeTO extract. |
| `heating_type` | Text | heating type as published in the City of Toronto RentSafeTO extract. |
| `indoor_garbage_storage_area` | Boolean | indoor garbage storage area as published in the City of Toronto RentSafeTO extract. |
| `intercom` | Boolean | intercom as published in the City of Toronto RentSafeTO extract. |
| `is_there_a_cooling_room` | Text | is there a cooling room as published in the City of Toronto RentSafeTO extract. |
| `is_there_emergency_power` | Text | is there emergency power as published in the City of Toronto RentSafeTO extract. |
| `laundry_room` | Boolean | laundry room as published in the City of Toronto RentSafeTO extract. |
| `laundry_room_hours_of_operation` | Text | laundry room hours of operation as published in the City of Toronto RentSafeTO extract. |
| `laundry_room_location` | Text | laundry room location as published in the City of Toronto RentSafeTO extract. |
| `locker_or_storage_room` | Boolean | locker or storage room as published in the City of Toronto RentSafeTO extract. |
| `no_barrier_free_accessble_units` | Float | no barrier free accessble units as published in the City of Toronto RentSafeTO extract. |
| `no_of_accessible_parking_spaces` | Float | no of accessible parking spaces as published in the City of Toronto RentSafeTO extract. |
| `no_of_elevators` | Float | no of elevators as published in the City of Toronto RentSafeTO extract. |
| `no_of_laundry_room_machines` | Float | no of laundry room machines as published in the City of Toronto RentSafeTO extract. |
| `non_smoking_building` | Text | non smoking building as published in the City of Toronto RentSafeTO extract. |
| `outdoor_garbage_storage_area` | Boolean | outdoor garbage storage area as published in the City of Toronto RentSafeTO extract. |
| `parking_type` | Text | parking type as published in the City of Toronto RentSafeTO extract. |
| `pcode` | Text | pcode as published in the City of Toronto RentSafeTO extract. |
| `pet_restrictions` | Text | pet restrictions as published in the City of Toronto RentSafeTO extract. |
| `pets_allowed` | Boolean | pets allowed as published in the City of Toronto RentSafeTO extract. |
| `prop_management_company_name` | Text | prop management company name as published in the City of Toronto RentSafeTO extract. |
| `property_type` | Text | Property type as published by the City. |
| `recycling_bins_location` | Text | recycling bins location as published in the City of Toronto RentSafeTO extract. |
| `rsn` | Integer | RentSafeTO site number, used to link evaluations to the registration file. |
| `separate_gas_meters_each_unit` | Boolean | separate gas meters each unit as published in the City of Toronto RentSafeTO extract. |
| `separate_hydro_meter_each_unit` | Boolean | separate hydro meter each unit as published in the City of Toronto RentSafeTO extract. |
| `separate_water_meters_ea_unit` | Boolean | separate water meters ea unit as published in the City of Toronto RentSafeTO extract. |
| `site_address` | Text | Street address of the apartment building. |
| `sprinkler_system` | Boolean | sprinkler system as published in the City of Toronto RentSafeTO extract. |
| `sprinkler_system_test_record` | Boolean | sprinkler system test record as published in the City of Toronto RentSafeTO extract. |
| `sprinkler_system_year_installed` | Float | sprinkler system year installed as published in the City of Toronto RentSafeTO extract. |
| `tssa_test_records` | Boolean | tssa test records as published in the City of Toronto RentSafeTO extract. |
| `visitor_parking` | Text | visitor parking as published in the City of Toronto RentSafeTO extract. |
| `ward` | Integer | Toronto city ward as published. |
| `window_type` | Text | window type as published in the City of Toronto RentSafeTO extract. |
| `year_built` | Float | Year the building was built, as registered or evaluated. |
| `year_of_replacement` | Float | year of replacement as published in the City of Toronto RentSafeTO extract. |
| `year_registered` | Float | year registered as published in the City of Toronto RentSafeTO extract. |
| `no_of_storeys` | Text | no of storeys as published in the City of Toronto RentSafeTO extract. |
| `is_there_emergency_power.1` | Float | — |
| `non_smoking_building.1` | Float | — |
| `no_of_units` | Text | no of units as published in the City of Toronto RentSafeTO extract. |
| `no_of_accessibleparking_spaces` | Text | no of accessibleparking spaces as published in the City of Toronto RentSafeTO extract. |
| `facilities_available.1` | Float | — |
| `is_there_a_cooling_room.1` | Float | — |
| `no_barrierfree_accessble_units` | Text | no barrierfree accessble units as published in the City of Toronto RentSafeTO extract. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

## Source and licence

**Source:** City of Toronto Open Data, Apartment Building Evaluation (https://open.toronto.ca/dataset/apartment-building-evaluation/), files apartment-building-evaluations-2023-current.csv and pre-2023-apartment-building-evaluations.csv; Apartment Building Registration (https://open.toronto.ca/dataset/apartment-building-registration/), file apartment-building-registration-data.csv. Downloaded on November 12, 2026. Prepared by John Khan in Toronto, Ontario. Shared under the Open Government Licence Toronto, https://open.toronto.ca/open-data-licence/.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoapartmentbuildingevaluations,
  author    = {Khan, John},
  title     = {Toronto apartment building evaluations},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-apartment-building-evaluations}
}
```

APA: Khan, J. (2026). *Toronto apartment building evaluations* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-apartment-building-evaluations

<details><summary>Full notes from the Kaggle page</summary>

## What this is

RentSafeTO apartment building evaluations and registration records from the City of Toronto. RentSafeTO is the City's bylaw enforcement program for rental apartment buildings with three or more storeys or 10 or more units. The evaluation file stacks the official pre-2023 extract with the 2023-to-current extract. The registration file describes each registered building.

Sources: [Apartment Building Evaluation](https://open.toronto.ca/dataset/apartment-building-evaluation/) and [Apartment Building Registration](https://open.toronto.ca/dataset/apartment-building-registration/) on Toronto Open Data.

## Coverage

City of Toronto rental apartment buildings covered by RentSafeTO. The pre-2023 evaluation extract and the 2023-to-current extract are both included. Registration is the current City extract as of this snapshot.

## Updates

This upload is a snapshot from November 12, 2026 and is not refreshed on a schedule. The City publishes evaluation updates frequently and refreshes registration about once a month. Download the catalogue files again for a later extract.

## A few numbers from this snapshot

* The stacked evaluation file has 18,916 rows (11,760 from the pre-2023 extract and 7,156 from the 2023-to-current extract).
* The registration file has 3,611 apartment buildings.
* The mean combined evaluation score across rows that have a score is 79.6.
* The mean combined evaluation score in 2026 was 90.8.
* Evaluation years in the file run from 2017 to 2026.
* Evaluations are spread across 25 wards.

## Example uses

* Map evaluation scores by ward or by year built.
* Join evaluations to registration on the site number (rsn) to add units, storeys and amenities.
* Watch how scores change across the 2023 methodology break.

## Caveats

The 2023-to-current extract and the pre-2023 extract do not use identical columns. Missing fields after stacking are empty, not zeros. Evaluation methods and score scales can change over time, so compare scores across the 2023 break with care. A building can have more than one evaluation row. Addresses and wards follow the City's published values. This is not an official City product.

## Files

* `apartment_evaluations.csv`: Stacked evaluation extracts.
* `apartment_registration.csv`: Building registration attributes.
* `data_dictionary.csv`: Column dictionary.
* `cover.png`: Cover chart drawn from this snapshot.

## Licence

This dataset is shared under the [Open Government Licence Toronto](https://open.toronto.ca/open-data-licence/). Source: City of Toronto Open Data, RentSafeTO apartment building evaluation and registration files. Columns were renamed and the two evaluation extracts were stacked. This is not an official City of Toronto product and the City does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
