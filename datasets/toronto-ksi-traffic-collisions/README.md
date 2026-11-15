<p align="center"><img src="../../assets/theme-public-safety.png" alt="Toronto KSI Traffic Collisions 2006 to 2026" width="100%"></p>

# Toronto KSI Traffic Collisions 2006 to 2026

*Collision-level KSI file without streets or coordinates, 2006 to 2026*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 2006 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-ksi-traffic-collisions](https://www.kaggle.com/datasets/johnnykhan1/toronto-ksi-traffic-collisions)

## What it is

Motor vehicle collisions in Toronto in which someone was killed or seriously injured (KSI), 2006 to 2026. The official City file is person-level: several rows can belong to one collision, and it includes street names, map coordinates, ages and other personal fields. This version rolls the file up to one row per collision, keeps neighbourhood and the involvement flags, and drops street names, coordinates, age, and person-level condition fields.

7,677 KSI collisions, 2006 to 2026. 1,109 fatal injuries in the file. Street names and coordinates dropped.

The last well known Kaggle copies of Toronto KSI stop around 2018 or 2019. This file includes the current City extract, updated on the catalogue on 2026-11-09.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 83 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`ksi_by_year_and_impact_type.csv`](data/ksi_by_year_and_impact_type.csv) | 5 KB | in this repository |
| [`ksi_citywide_by_year.csv`](data/ksi_citywide_by_year.csv) | 1 KB | in this repository |
| [`ksi_collisions.csv`](data/ksi_collisions.csv) | 1.7 MB | in this repository |
| [`ksi_yearly_by_neighbourhood.csv`](data/ksi_yearly_by_neighbourhood.csv) | 105 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `ksi_by_year_and_impact_type.csv`

Citywide annual counts by impact type.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the collision. |
| `impact_type` | Text | Impact type as published. |
| `collisions` | Integer | Number of KSI collisions. |

### `ksi_citywide_by_year.csv`

Citywide annual collision and injury counts.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the collision. |
| `collisions` | Integer | Number of KSI collisions. |
| `fatal_collisions` | Integer | Collisions whose accident class includes Fatal. |
| `fatal_injuries` | Integer | Count of people recorded with a fatal injury. |
| `major_injuries` | Integer | Count of people recorded with a major injury. |
| `pedestrian_collisions` | Integer | Collisions with a pedestrian involvement flag. |
| `cyclist_collisions` | Integer | Collisions with a cyclist involvement flag. |

### `ksi_collisions.csv`

One row per KSI collision. Person-level rows were rolled up. Street names, exact coordinates, ages and other personal fields were dropped.

| Column | Type | Description |
|---|---|---|
| `collision_id` | Text | Official collision identifier from the source file. |
| `occurrence_date` | Date | Collision date (YYYY-MM-DD). Time of day was dropped. |
| `year` | Integer | Calendar year of the collision. |
| `month_num` | Integer | Month number from 1 to 12. |
| `neighbourhood_id` | Text | 158-neighbourhood model number parsed from the source neighbourhood field, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `ward` | Text | City ward name as published. |
| `division` | Text | Police division as published. |
| `accident_class` | Text | Collision class, for example Fatal or Non-Fatal Injury. |
| `accident_location` | Text | Location type, for example at an intersection. |
| `impact_type` | Text | Impact type as published. |
| `visibility` | Text | Weather or visibility condition as published. |
| `light` | Text | Light condition as published. |
| `road_surface` | Text | Road surface condition as published. |
| `road_class` | Text | Road class as published. |
| `traffic_control` | Text | Traffic control present at the location. |
| `people_involved` | Integer | Number of people involved, from the source collision field. |
| `most_severe_injury` | Text | Most severe injury recorded among people in the collision (Fatal, Major, Minor, Minimal, or None). |
| `fatal_injuries` | Integer | Count of people recorded with a fatal injury. |
| `major_injuries` | Integer | Count of people recorded with a major injury. |
| `minor_injuries` | Integer | Count of people recorded with a minor or minimal injury. |
| `pedestrian_involved` | Integer | 1 if any person record was flagged as a pedestrian involvement, else 0. |
| `cyclist_involved` | Integer | 1 if any person record was flagged as a cyclist involvement, else 0. |
| `motorcyclist_involved` | Integer | 1 if any person record was flagged as a motorcyclist involvement, else 0. |
| `older_adult_involved` | Integer | 1 if any person record was flagged as an older adult involvement, else 0. |
| `school_child_involved` | Integer | 1 if any person record was flagged as a school child involvement, else 0. |
| `aggressive` | Integer | 1 if an aggressive driving flag was recorded, else 0. |
| `distracted` | Integer | 1 if a distracted driving flag was recorded, else 0. |
| `red_light` | Integer | 1 if a red light flag was recorded, else 0. |
| `heavy_truck_involved` | Integer | 1 if a heavy truck flag was recorded, else 0. |

### `ksi_yearly_by_neighbourhood.csv`

Annual collision and injury counts by neighbourhood.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the collision. |
| `neighbourhood_id` | Text | 158-neighbourhood model number parsed from the source neighbourhood field, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `collisions` | Integer | Number of KSI collisions. |
| `fatal_collisions` | Integer | Collisions whose accident class includes Fatal. |
| `fatal_injuries` | Integer | Count of people recorded with a fatal injury. |
| `major_injuries` | Integer | Count of people recorded with a major injury. |
| `pedestrian_collisions` | Integer | Collisions with a pedestrian involvement flag. |
| `cyclist_collisions` | Integer | Collisions with a cyclist involvement flag. |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | 158-neighbourhood model number parsed from the source neighbourhood field, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `neighbourhood_label` | Text | Name with the number in parentheses. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `classification_code` | Text | Short classification code. |
| `centroid_longitude` | Text | Longitude of the polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the polygon centroid, WGS84. |

## Source and licence

**Source:** City of Toronto Open Data, Motor Vehicle Collisions Involving Killed or Seriously Injured Persons (https://open.toronto.ca/dataset/motor-vehicle-collisions-involving-killed-or-seriously-injured-persons/), from Toronto Police Service collision records. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoksitrafficcollisions,
  author    = {Khan, John},
  title     = {Toronto KSI Traffic Collisions 2006 to 2026},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-ksi-traffic-collisions}
}
```

APA: Khan, J. (2026). *Toronto KSI Traffic Collisions 2006 to 2026* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-ksi-traffic-collisions

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Motor vehicle collisions in Toronto in which someone was killed or seriously injured (KSI), 2006 to 2026. The official City file is person-level: several rows can belong to one collision, and it includes street names, map coordinates, ages and other personal fields. This version rolls the file up to one row per collision, keeps neighbourhood and the involvement flags, and drops street names, coordinates, age, and person-level condition fields.

7,677 KSI collisions, 2006 to 2026. 1,109 fatal injuries in the file. Street names and coordinates dropped.

The last well known Kaggle copies of Toronto KSI stop around 2018 or 2019. This file includes the current City extract, updated on the catalogue on 2026-11-09.

## Files

| File | What is in it |
|---|---|
| `ksi_collisions.csv` | One row per collision, without streets or coordinates |
| `ksi_yearly_by_neighbourhood.csv` | Annual counts by neighbourhood |
| `ksi_citywide_by_year.csv` | Citywide annual counts |
| `ksi_by_year_and_impact_type.csv` | Annual counts by impact type |
| `neighbourhoods.csv` | 158-neighbourhood lookup |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the citywide yearly series |

## Coverage and refresh

The City of Toronto Transportation Services Division receives this collision data from the Toronto Police Service for collisions in the city's right-of-way that involve a serious injury or a fatality. I pulled the file on November 9, 2026. Recent months can still be revised as late reports arrive.

## Caveats

* A collision can appear only if it met the City's KSI criteria. This is not a file of every traffic collision in Toronto.
* Injury counts are from the people listed on the collision, using the injury field as published. `fatal_collisions` uses the accident class field, which can differ slightly from the count of fatal injuries.
* Neighbourhood ids were parsed from the source neighbourhood text. When that field was empty the row is `NSA`.
* Involvement flags (pedestrian, cyclist, and so on) are 1 when any person record on the collision carried that flag.
* Times of day, street names and coordinates were dropped.

## Sources

City of Toronto, Motor Vehicle Collisions Involving Killed or Seriously Injured Persons: https://open.toronto.ca/dataset/motor-vehicle-collisions-involving-killed-or-seriously-injured-persons/

The underlying collision records come from the Toronto Police Service. Neighbourhoods: https://open.toronto.ca/dataset/neighbourhoods/

Pulled on November 9, 2026.

## Example uses

* Follow pedestrian and cyclist KSI collisions by neighbourhood over time.
* Compare fatal and major injury counts on major arterial roads versus local streets using `road_class`.
* Join the yearly neighbourhood file to census profiles on `neighbourhood_id`.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). Underlying collision records come from the Toronto Police Service and are also subject to the Toronto Police Service terms of use where they apply (https://data.torontopolice.on.ca/pages/terms-of-use). This dataset is not endorsed by the City of Toronto or the Toronto Police Service.

Changes made here: person-level rows were aggregated to one collision row, street names, coordinates, times, ages and personal condition fields were dropped, neighbourhood ids were parsed, and yearly aggregates were added.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
