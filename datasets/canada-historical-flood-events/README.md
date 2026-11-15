<p align="center"><img src="../../assets/theme-environment.png" alt="Canada historical flood events" width="100%"></p>

# Canada historical flood events

*NRCan inventory of flood locations and events, 1696 to 2025*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1800s to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-historical-flood-events](https://www.kaggle.com/datasets/johnnykhan1/canada-historical-flood-events)

## What it is

A tidy extract of Natural Resources Canada's Historical Flood Events (HFE) inventory: one table of flood events and one table of the localities reported as affected. Coordinates in the location file were converted from the official Canada Atlas Lambert (EPSG:3978) points to longitude and latitude.

Source dataset: [Historical Flood Events (HFE)](https://open.canada.ca/data/en/dataset/fe83a604-aa5a-4e46-903c-685f8b0cc33c) (Natural Resources Canada). English GeoPackage downloaded from the official FTP file [https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/historical_flood_event_en.gpkg.zip](https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/historical_flood_event_en.gpkg.zip) on November 9, 2026. The GeoPackage file date inside the zip is 10 December 2025. Product specifications: https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/HFE_ProductSpecifications.pdf.

This is a different product from the Public Safety Canada Canadian Disaster Database.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 76 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 7 KB | in this repository |
| [`events_by_year_cause.csv`](data/events_by_year_cause.csv) | 8 KB | in this repository |
| [`events_by_year_province.csv`](data/events_by_year_province.csv) | 13 KB | in this repository |
| [`flood_events.csv`](data/flood_events.csv) | 2.0 MB | in this repository |
| [`flood_locations.csv`](data/flood_locations.csv) | 12.4 MB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `events_by_year_cause.csv`

Event counts by year and flood cause code.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Event year as published. |
| `flood_cause` | Text | Cause code as published (freshet, heavy rain, coastal storm, frazil, beaver dam failure, municipal water main break, dam failure, or unknown). |
| `n_events` | Integer | Number of events in that year and group. |

### `events_by_year_province.csv`

Event counts by year and the published province or territory code on the event table.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Event year as published. |
| `province_territory` | Text | Province or territory code. On the event table this may list more than one code, separated by commas. |
| `province_territory_description` | Text | Province or territory name corresponding to the code field. |
| `n_events` | Integer | Number of events in that year and group. |

### `flood_events.csv`

One row per flood event in the inventory, including a count of linked location rows.

| Column | Type | Description |
|---|---|---|
| `id` | Text | Row identifier from the official GeoPackage layer. |
| `uuid` | Text | Record UUID from the official layer. |
| `event_id` | Text | Event identifier shared by the event layer and its location rows. |
| `event_name` | Text | Event name when published (for example a named storm). Blank if none was given. |
| `year` | Integer | Event year as published. |
| `start_date` | Text | Start date as published. Some early events carry only a year. |
| `end_date` | Date | End date as published. Left blank when the source had no end date (n/a - nd). |
| `season` | Text | Season as published (spring, summer, fall, winter, or unknown). |
| `province_territory` | Text | Province or territory code. On the event table this may list more than one code, separated by commas. |
| `province_territory_description` | Text | Province or territory name corresponding to the code field. |
| `flood_cause` | Text | Cause code as published (freshet, heavy rain, coastal storm, frazil, beaver dam failure, municipal water main break, dam failure, or unknown). |
| `flood_cause_description` | Text | Official description of the cause code. |
| `death` | Text | yes, no or unknown, as coded in the inventory. This is not a count of fatalities. |
| `evacuation` | Text | yes, no or unknown, as coded in the inventory. This is not a count of people evacuated. |
| `event_summary` | Text | Event-level summary from the official event layer. |
| `source` | Text | Source class on the event layer. |
| `source_description` | Text | Description of the event-layer source class. |
| `precipitation_analysis_url` | Text | Precipitation analysis document URL when published (events after 1 January 1980 caused by heavy rain or a coastal storm). |
| `precipitation_animation_url` | Text | Precipitation animation URL when published. |
| `precipitation_data_url` | Text | Precipitation data URL when published. |
| `n_locations` | Integer | Number of location rows linked to this event in the official location layer. |

### `flood_locations.csv`

One row per reported locality affected by a flood event, with WGS84 coordinates converted from the official Canada Atlas Lambert points.

| Column | Type | Description |
|---|---|---|
| `id` | Text | Row identifier from the official GeoPackage layer. |
| `uuid` | Text | Record UUID from the official layer. |
| `event_id` | Text | Event identifier shared by the event layer and its location rows. |
| `event_name` | Text | Event name when published (for example a named storm). Blank if none was given. |
| `year` | Integer | Event year as published. |
| `start_date` | Text | Start date as published. Some early events carry only a year. |
| `end_date` | Date | End date as published. Left blank when the source had no end date (n/a - nd). |
| `locality` | Text | Place name reported as affected. The official point sits on this locality, not on a mapped flood footprint. |
| `season` | Text | Season as published (spring, summer, fall, winter, or unknown). |
| `province_territory` | Text | Province or territory code. On the event table this may list more than one code, separated by commas. |
| `province_territory_description` | Text | Province or territory name corresponding to the code field. |
| `flood_cause` | Text | Cause code as published (freshet, heavy rain, coastal storm, frazil, beaver dam failure, municipal water main break, dam failure, or unknown). |
| `flood_cause_description` | Text | Official description of the cause code. |
| `death` | Text | yes, no or unknown, as coded in the inventory. This is not a count of fatalities. |
| `evacuation` | Text | yes, no or unknown, as coded in the inventory. This is not a count of people evacuated. |
| `rainfall_mm` | Float | Rainfall amount in millimetres when published. |
| `intensity` | Text | Intensity as published (for example low, unknown). |
| `comment` | Text | Source comment or narrative for the location. |
| `link_1` | Text | First source link when published. |
| `link_2` | Text | Second source link when published. |
| `source_1` | Text | Primary source class for the location row (for example provincial). |
| `source_1_description` | Text | Description of the primary source class. |
| `source_2` | Text | Secondary source class when published. |
| `source_2_description` | Text | Description of the secondary source class. |
| `geometry_source` | Text | How the official point was placed (for example CGNDB). |
| `geometry_source_description` | Text | Description of the geometry source. |
| `weather_station` | Text | Weather station reference when published. |
| `precipitation_analysis_url` | Text | Precipitation analysis document URL when published (events after 1 January 1980 caused by heavy rain or a coastal storm). |
| `precipitation_data_url` | Text | Precipitation data URL when published. |
| `longitude` | Text | Longitude in decimal degrees (WGS84), converted from the official EPSG:3978 point. Approximate; the official point is a locality, not a flood outline. |
| `latitude` | Text | Latitude in decimal degrees (WGS84), converted from the official EPSG:3978 point. Approximate; the official point is a locality, not a flood outline. |
| `x_lambert_m` | Float | Easting in metres, NAD83 / Canada Atlas Lambert (EPSG:3978), as stored in the GeoPackage. |
| `y_lambert_m` | Float | Northing in metres, NAD83 / Canada Atlas Lambert (EPSG:3978), as stored in the GeoPackage. |

## Source and licence

**Source:** Natural Resources Canada, Historical Flood Events (HFE), https://open.canada.ca/data/en/dataset/fe83a604-aa5a-4e46-903c-685f8b0cc33c. English GeoPackage https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/historical_flood_event_en.gpkg.zip. Product specifications https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/HFE_ProductSpecifications.pdf.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahistoricalfloodevents,
  author    = {Khan, John},
  title     = {Canada historical flood events},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-historical-flood-events}
}
```

APA: Khan, J. (2026). *Canada historical flood events* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-historical-flood-events

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of Natural Resources Canada's Historical Flood Events (HFE) inventory: one table of flood events and one table of the localities reported as affected. Coordinates in the location file were converted from the official Canada Atlas Lambert (EPSG:3978) points to longitude and latitude.

Source dataset: [Historical Flood Events (HFE)](https://open.canada.ca/data/en/dataset/fe83a604-aa5a-4e46-903c-685f8b0cc33c) (Natural Resources Canada). English GeoPackage downloaded from the official FTP file [https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/historical_flood_event_en.gpkg.zip](https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/historical_flood_event_en.gpkg.zip) on November 9, 2026. The GeoPackage file date inside the zip is 10 December 2025. Product specifications: https://ftp.maps.canada.ca/pub/nrcan_rncan/Floods_Inondation/historical_flood_event_downloads/HFE_ProductSpecifications.pdf.

This is a different product from the Public Safety Canada Canadian Disaster Database.

## Coverage

1,684 events and 7,844 location rows, with years from 1696 to 2025. 1,681 events have at least one location row; 3 events have none. 7,844 location points were converted to WGS84.

Event totals by cause: freshet 691, heavy rain 570, coastal storm 174, unknown 149, beaver dam failure 40, frazil 35, municipal water main break 19, dam failure 6.

Location rows by province or territory: QC 3487, NB 1853, NS 1125, BC 457, ON 405, MB 203, AB 115, PE 54, SK 50, NL 47, NT 30, YT 17, NU 1. Coverage is uneven. Quebec alone accounts for 3,487 of the 7,844 location rows, and some territories have very few records. That reflects the compiled sources, not a complete national count of floods.

Of the events, 1,202 are from 1980 onward. The extract includes 18 events and 22 location rows dated 2025 in the 10 December 2025 GeoPackage, so 2025 should not be treated as a complete year.

## Updates

This upload is a snapshot of the 10 December 2025 English GeoPackage, pulled on November 9, 2026, and is not refreshed on a schedule. For a later extract, use the official HFE download or the NRCan map service.

## A few numbers from this snapshot

* 1,684 events are in the event table, from 1696 to 2025.
* 7,844 location rows are in the location table.
* 69 events are coded death=yes and 306 are coded evacuation=yes. Those flags are not counts of people, and many rows are coded unknown.
* The most common cause in the event table is freshet (691 events).

## Example uses

* Map localities affected in a chosen year or by a named storm.
* Chart the number of inventory events by year after 1980.
* Compare cause mix by province, keeping the uneven coverage in mind.

## Caveats

NRCan states that no consultation was conducted with the various providers and stakeholders of the historic flood data, that disparities among sources leave an incomplete product, and that no warranty is given as to accuracy or completeness. The absence of information does not mean that no flooding has occurred.

Event positions do not indicate where the flooding occurred. Points are placed on the reported locality (often a CGNDB place name). Multi-locality events are a set of those points, not a flood extent. death and evacuation are yes/no/unknown flags as published, not fatality or evacuee counts.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada).

## Files

* `flood_locations.csv` — reported localities, attributes and converted coordinates.
* `flood_events.csv` — one row per event, with a count of linked locations.
* `events_by_year_province.csv` — event counts by year and published province or territory code.
* `events_by_year_cause.csv` — event counts by year and cause.
* `data_dictionary.csv` — column dictionary.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
