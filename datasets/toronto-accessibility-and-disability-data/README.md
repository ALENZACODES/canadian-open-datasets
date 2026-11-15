<p align="center"><img src="../../assets/theme-health.png" alt="Toronto Accessibility and Disability Data" width="100%"></p>

# Toronto Accessibility and Disability Data

*Parking, washrooms, libraries and TTC wheelchair boarding flags*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** Snapshot of 9 November 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-accessibility-and-disability-data](https://www.kaggle.com/datasets/johnnykhan1/toronto-accessibility-and-disability-data)

## What it is

A neighbourhood-level accessibility bundle for Toronto, built from official City and TTC open data on November 9, 2026. It brings together accessible parking stalls, park washrooms and their accessible features, accessible washrooms in civic buildings, public library branches, and TTC stop wheelchair-boarding flags from the current GTFS schedule. Each site is joined to the current 158 social planning neighbourhoods.

669 accessible parking stalls, 147 park washrooms with accessible features, 37 accessible civic washrooms, 8,059 TTC stops marked accessible.

I looked for a public Wheel-Trans trips or stop table on the City of Toronto Open Data catalogue and did not find one. The closest official access layer in this bundle is the TTC GTFS `wheelchair_boarding` flag on stops and stations.

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`accessibility_by_neighbourhood.csv`](data/accessibility_by_neighbourhood.csv) | 10 KB | in this repository |
| [`accessibility_facilities.csv`](data/accessibility_facilities.csv) | 233 KB | in this repository |
| [`accessible_parking_stalls.csv`](data/accessible_parking_stalls.csv) | 109 KB | in this repository |
| [`civic_building_washrooms.csv`](data/civic_building_washrooms.csv) | 29 KB | in this repository |
| [`cover.png`](data/cover.png) | 61 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 13 KB | in this repository |
| [`library_branches.csv`](data/library_branches.csv) | 21 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |
| [`park_washrooms.csv`](data/park_washrooms.csv) | 72 KB | in this repository |
| [`ttc_stop_accessibility_by_neighbourhood.csv`](data/ttc_stop_accessibility_by_neighbourhood.csv) | 5 KB | in this repository |
| [`ttc_stops_accessibility.csv`](data/ttc_stops_accessibility.csv) | 1.5 MB | in this repository |

## Columns

### `accessibility_by_neighbourhood.csv`

Counts of each facility layer by neighbourhood.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `facilities` | Float | Value for facilities. Counts of facilities or accessible facilities in the neighbourhood. |
| `accessible_parking_stall_count` | Float | Value for accessible_parking_stall_count. Counts of facilities or accessible facilities in the neighbourhood. |
| `accessible_parking_stall_accessible` | Float | Value for accessible_parking_stall_accessible. Counts of facilities or accessible facilities in the neighbourhood. |
| `library_branch_count` | Float | Value for library_branch_count. Counts of facilities or accessible facilities in the neighbourhood. |
| `park_washroom_count` | Float | Value for park_washroom_count. Counts of facilities or accessible facilities in the neighbourhood. |
| `park_washroom_accessible` | Float | Value for park_washroom_accessible. Counts of facilities or accessible facilities in the neighbourhood. |
| `civic_building_washroom_count` | Float | Value for civic_building_washroom_count. Counts of facilities or accessible facilities in the neighbourhood. |
| `civic_building_washroom_accessible` | Float | Value for civic_building_washroom_accessible. Counts of facilities or accessible facilities in the neighbourhood. |
| `stops` | Float | Number of TTC stops in the neighbourhood. |
| `accessible_stops` | Float | Stops with wheelchair_boarding = 1. |
| `not_accessible_stops` | Float | Stops with wheelchair_boarding = 2. |
| `unknown_stops` | Float | Stops with wheelchair_boarding = 0 or missing. |

### `accessibility_facilities.csv`

Combined civic facilities (accessible parking stalls, park washrooms, civic washrooms, library branches, and TTC stations when present) with neighbourhood ids.

| Column | Type | Description |
|---|---|---|
| `layer` | Text | Facility layer: accessible_parking_stall, park_washroom, civic_building_washroom, library_branch, or ttc_station. |
| `source_dataset` | Text | City catalogue slug of the source file. |
| `facility_id` | Float | Identifier from the source file. |
| `name` | Text | Facility or branch name. |
| `address` | Text | Street address as published, when the source has one. |
| `accessible_detail` | Text | Accessibility detail as published (AODA stall type, washroom features, Yes/No, or TTC wheelchair boarding class). |
| `status` | Text | Status or hours note as published, when present. |
| `notes` | Text | Other published attributes kept for context. |
| `source_date_note` | Text | Date or source note from the originating file. |
| `longitude` | Text | Longitude in WGS84, from the official facility or stop location. These are public civic locations, not offset crime points. |
| `latitude` | Text | Latitude in WGS84, from the official facility or stop location. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `is_accessible` | Boolean | True when the source marks the facility accessible, False when it marks it not accessible, empty when the source does not say. |

### `accessible_parking_stalls.csv`

Toronto Parking Authority accessible stalls at off-street surface lots, with AODA type and neighbourhood.

| Column | Type | Description |
|---|---|---|
| `layer` | Text | Facility layer: accessible_parking_stall, park_washroom, civic_building_washroom, library_branch, or ttc_station. |
| `source_dataset` | Text | City catalogue slug of the source file. |
| `facility_id` | Float | Identifier from the source file. |
| `name` | Text | Facility or branch name. |
| `address` | Text | Street address as published, when the source has one. |
| `accessible_detail` | Text | Accessibility detail as published (AODA stall type, washroom features, Yes/No, or TTC wheelchair boarding class). |
| `status` | Text | Status or hours note as published, when present. |
| `notes` | Text | Other published attributes kept for context. |
| `source_date_note` | Text | Date or source note from the originating file. |
| `longitude` | Text | Longitude in WGS84, from the official facility or stop location. These are public civic locations, not offset crime points. |
| `latitude` | Text | Latitude in WGS84, from the official facility or stop location. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |

### `civic_building_washrooms.csv`

Washrooms in City civic buildings, including the official accessible washroom flag.

| Column | Type | Description |
|---|---|---|
| `layer` | Text | Facility layer: accessible_parking_stall, park_washroom, civic_building_washroom, library_branch, or ttc_station. |
| `source_dataset` | Text | City catalogue slug of the source file. |
| `facility_id` | Text | Identifier from the source file. |
| `name` | Text | Facility or branch name. |
| `address` | Text | Street address as published, when the source has one. |
| `accessible_detail` | Boolean | Accessibility detail as published (AODA stall type, washroom features, Yes/No, or TTC wheelchair boarding class). |
| `status` | Text | Status or hours note as published, when present. |
| `notes` | Text | Other published attributes kept for context. |
| `source_date_note` | Text | Date or source note from the originating file. |
| `longitude` | Text | Longitude in WGS84, from the official facility or stop location. These are public civic locations, not offset crime points. |
| `latitude` | Text | Latitude in WGS84, from the official facility or stop location. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `is_accessible` | Boolean | True when the source marks the facility accessible, False when it marks it not accessible, empty when the source does not say. |

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `library_branches.csv`

Toronto Public Library branches, with neighbourhood and a note on public washrooms and parking. The library file does not publish a wheelchair-access flag.

| Column | Type | Description |
|---|---|---|
| `layer` | Text | Facility layer: accessible_parking_stall, park_washroom, civic_building_washroom, library_branch, or ttc_station. |
| `source_dataset` | Text | City catalogue slug of the source file. |
| `facility_id` | Text | Identifier from the source file. |
| `name` | Text | Facility or branch name. |
| `address` | Text | Street address as published, when the source has one. |
| `accessible_detail` | Text | Accessibility detail as published (AODA stall type, washroom features, Yes/No, or TTC wheelchair boarding class). |
| `status` | Text | Status or hours note as published, when present. |
| `notes` | Text | Other published attributes kept for context. |
| `source_date_note` | Text | Date or source note from the originating file. |
| `longitude` | Text | Longitude in WGS84, from the official facility or stop location. These are public civic locations, not offset crime points. |
| `latitude` | Text | Latitude in WGS84, from the official facility or stop location. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `is_accessible` | Text | True when the source marks the facility accessible, False when it marks it not accessible, empty when the source does not say. |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `neighbourhood_label` | Text | Name with the number in parentheses. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `classification_code` | Text | Short classification code. |
| `centroid_longitude` | Text | Longitude of the polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the polygon centroid, WGS84. |

### `park_washrooms.csv`

Park and recreation washrooms, including the published accessible features list.

| Column | Type | Description |
|---|---|---|
| `layer` | Text | Facility layer: accessible_parking_stall, park_washroom, civic_building_washroom, library_branch, or ttc_station. |
| `source_dataset` | Text | City catalogue slug of the source file. |
| `facility_id` | Text | Identifier from the source file. |
| `name` | Text | Facility or branch name. |
| `address` | Text | Street address as published, when the source has one. |
| `accessible_detail` | Text | Accessibility detail as published (AODA stall type, washroom features, Yes/No, or TTC wheelchair boarding class). |
| `status` | Text | Status or hours note as published, when present. |
| `notes` | Text | Other published attributes kept for context. |
| `source_date_note` | Date | Date or source note from the originating file. |
| `longitude` | Text | Longitude in WGS84, from the official facility or stop location. These are public civic locations, not offset crime points. |
| `latitude` | Text | Latitude in WGS84, from the official facility or stop location. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `is_accessible` | Boolean | True when the source marks the facility accessible, False when it marks it not accessible, empty when the source does not say. |

### `ttc_stop_accessibility_by_neighbourhood.csv`

TTC stop accessibility counts by neighbourhood.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `stops` | Integer | Number of TTC stops in the neighbourhood. |
| `accessible_stops` | Integer | Stops with wheelchair_boarding = 1. |
| `not_accessible_stops` | Integer | Stops with wheelchair_boarding = 2. |
| `unknown_stops` | Integer | Stops with wheelchair_boarding = 0 or missing. |

### `ttc_stops_accessibility.csv`

TTC stops and stations from the current GTFS feed, with wheelchair_boarding translated to accessible, not_accessible, or no_information.

| Column | Type | Description |
|---|---|---|
| `layer` | Text | Facility layer: accessible_parking_stall, park_washroom, civic_building_washroom, library_branch, or ttc_station. |
| `source_dataset` | Text | City catalogue slug of the source file. |
| `facility_id` | Text | Identifier from the source file. |
| `name` | Text | Facility or branch name. |
| `address` | Text | Street address as published, when the source has one. |
| `accessible_detail` | Text | Accessibility detail as published (AODA stall type, washroom features, Yes/No, or TTC wheelchair boarding class). |
| `status` | Text | Status or hours note as published, when present. |
| `notes` | Text | Other published attributes kept for context. |
| `source_date_note` | Text | Date or source note from the originating file. |
| `longitude` | Text | Longitude in WGS84, from the official facility or stop location. These are public civic locations, not offset crime points. |
| `latitude` | Text | Latitude in WGS84, from the official facility or stop location. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `is_accessible` | Boolean | True when the source marks the facility accessible, False when it marks it not accessible, empty when the source does not say. |

## Source and licence

**Source:** City of Toronto Open Data: accessible parking stalls, park washrooms, civic building washrooms, library branch general information, TTC routes and schedules (GTFS), and neighbourhoods. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoaccessibilityanddisabilitydata,
  author    = {Khan, John},
  title     = {Toronto Accessibility and Disability Data},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-accessibility-and-disability-data}
}
```

APA: Khan, J. (2026). *Toronto Accessibility and Disability Data* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-accessibility-and-disability-data

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A neighbourhood-level accessibility bundle for Toronto, built from official City and TTC open data on November 9, 2026. It brings together accessible parking stalls, park washrooms and their accessible features, accessible washrooms in civic buildings, public library branches, and TTC stop wheelchair-boarding flags from the current GTFS schedule. Each site is joined to the current 158 social planning neighbourhoods.

669 accessible parking stalls, 147 park washrooms with accessible features, 37 accessible civic washrooms, 8,059 TTC stops marked accessible.

I looked for a public Wheel-Trans trips or stop table on the City of Toronto Open Data catalogue and did not find one. The closest official access layer in this bundle is the TTC GTFS `wheelchair_boarding` flag on stops and stations.

## Files

| File | What is in it |
|---|---|
| `accessibility_facilities.csv` | Combined civic sites (parking stalls, washrooms, libraries, TTC stations when tagged as stations) |
| `accessible_parking_stalls.csv` | Accessible stalls at Toronto Parking Authority surface lots |
| `park_washrooms.csv` | Park washrooms and published accessible features |
| `civic_building_washrooms.csv` | Washrooms in City buildings, with the official accessible flag |
| `library_branches.csv` | Toronto Public Library branches |
| `ttc_stops_accessibility.csv` | TTC stops and stations with wheelchair boarding class |
| `ttc_stop_accessibility_by_neighbourhood.csv` | TTC stop access counts by neighbourhood |
| `accessibility_by_neighbourhood.csv` | Counts of each layer by neighbourhood |
| `neighbourhoods.csv` | 158-neighbourhood lookup |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from accessible TTC stops by neighbourhood |

## Coverage and refresh

Pulled on November 9, 2026. TTC GTFS was last modified on the catalogue on 2026-11-05. Park washrooms and some other civic files are refreshed through the year. Facility coordinates are the official published locations of public sites, not offset crime points.

## Caveats

* Accessibility flags are only as complete as the source. Library branches do not carry a wheelchair-access field in the official file, so `is_accessible` is left empty there.
* A parking stall `AODA_TYPE` value is kept as published. I did not invent a long-form legend beyond the source column.
* GTFS `wheelchair_boarding` of 0 means no information, not that the stop is inaccessible.
* Washroom status can change with the season. Use the status and date notes in those files.
* This is not a complete inventory of every accessible place in Toronto, and it is not a substitute for the TTC or the City's own access maps.

## Sources

* off-street-parking-surface-lots-accessible-stalls: https://open.toronto.ca/dataset/off-street-parking-surface-lots-accessible-stalls/
* washroom-facilities: https://open.toronto.ca/dataset/washroom-facilities/
* corporate-real-estate-management-portfolio-washrooms: https://open.toronto.ca/dataset/corporate-real-estate-management-portfolio-washrooms/
* library-branch-general-information: https://open.toronto.ca/dataset/library-branch-general-information/
* ttc-routes-and-schedules: https://open.toronto.ca/dataset/ttc-routes-and-schedules/

Neighbourhoods: https://open.toronto.ca/dataset/neighbourhoods/

Pulled on November 9, 2026.

## Example uses

* Map accessible parking stalls and accessible civic washrooms together in each neighbourhood.
* Compare the share of TTC stops marked accessible in Neighbourhood Improvement Areas with the rest of the city.
* Join these neighbourhood counts to the neighbourhood crime, KSI or census profile files on `neighbourhood_id`.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). TTC GTFS is published by the Toronto Transit Commission through the same City catalogue and is subject to the same licence. This dataset is not endorsed by the City of Toronto or the TTC.

Changes made here: files were renamed to snake_case, public sites were joined to the 158-neighbourhood model, TTC wheelchair boarding codes were given readable labels, and neighbourhood counts were added. Source access flags were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
