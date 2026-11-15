<p align="center"><img src="../../assets/theme-public-safety.png" alt="Toronto Shootings and Firearm Discharges" width="100%"></p>

# Toronto Shootings and Firearm Discharges

*Neighbourhood event counts without offset map points, 2004 to 2026*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 2004 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-shootings-firearm-discharges](https://www.kaggle.com/datasets/johnnykhan1/toronto-shootings-firearm-discharges)

## What it is

Every shooting and firearm discharge occurrence reported to the Toronto Police Service from 2004 through 2026, aggregated to Toronto's 158 social planning neighbourhoods. The official file includes map coordinates that the Service offsets to the nearest intersection. Those coordinates, and the raw geometry, are not in this version. You get a tidy event file without points, plus monthly and yearly neighbourhood counts.

6,893 events from 2004 to 2026. 2026: 116 events.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 92 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |
| [`shooting_events.csv`](data/shooting_events.csv) | 753 KB | in this repository |
| [`shootings_citywide_by_year.csv`](data/shootings_citywide_by_year.csv) | 1 KB | in this repository |
| [`shootings_citywide_by_year_and_type.csv`](data/shootings_citywide_by_year_and_type.csv) | 1 KB | in this repository |
| [`shootings_monthly_by_neighbourhood.csv`](data/shootings_monthly_by_neighbourhood.csv) | 338 KB | in this repository |
| [`shootings_yearly_by_neighbourhood.csv`](data/shootings_yearly_by_neighbourhood.csv) | 82 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods, with classification and centroid.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | Neighbourhood number in the current 158-neighbourhood model, zero padded. NSA means the location was not mapped to a neighbourhood. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `neighbourhood_label` | Text | Name with the number in parentheses. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `classification_code` | Text | Short classification code. |
| `centroid_longitude` | Text | Longitude of the polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the polygon centroid, WGS84. |

### `shooting_events.csv`

One row per shooting or firearm discharge event, with dates, division, neighbourhood and casualty counts. Point coordinates and geometry were dropped.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the occurrence. |
| `occurrence_date` | Date | Occurrence date (YYYY-MM-DD). |
| `month` | Text | Month name as published. |
| `month_num` | Integer | Month number from 1 to 12. |
| `day_of_week` | Text | Day of week of the occurrence. |
| `hour` | Integer | Hour of the occurrence, 0 to 23. |
| `time_range` | Text | Time of day group as published (for example Night, Evening). |
| `division` | Text | Toronto Police Service division code at the time of the file. |
| `event_type` | Text | Shooting or Firearm Discharge, as classified in the source. |
| `deaths` | Integer | Number of deaths recorded for the event. Zero when none were recorded. |
| `injuries` | Integer | Number of injuries recorded for the event. Zero when none were recorded. |
| `neighbourhood_id` | Text | Neighbourhood number in the current 158-neighbourhood model, zero padded. NSA means the location was not mapped to a neighbourhood. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `neighbourhood_id_140` | Text | Neighbourhood number in the older 140-neighbourhood model, kept for historical joins. |
| `neighbourhood_name_140` | Text | Neighbourhood name in the older 140-neighbourhood model. |

### `shootings_citywide_by_year.csv`

Citywide annual totals, including events not mapped to a neighbourhood.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the occurrence. |
| `events` | Integer | Number of events in that neighbourhood, month and type. |
| `deaths` | Integer | Number of deaths recorded for the event. Zero when none were recorded. |
| `injuries` | Integer | Number of injuries recorded for the event. Zero when none were recorded. |

### `shootings_citywide_by_year_and_type.csv`

Citywide annual totals split by event type.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the occurrence. |
| `event_type` | Text | Shooting or Firearm Discharge, as classified in the source. |
| `events` | Integer | Number of events in that neighbourhood, month and type. |
| `deaths` | Integer | Number of deaths recorded for the event. Zero when none were recorded. |
| `injuries` | Integer | Number of injuries recorded for the event. Zero when none were recorded. |

### `shootings_monthly_by_neighbourhood.csv`

Monthly event, death and injury counts by neighbourhood and event type.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the occurrence. |
| `month_num` | Integer | Month number from 1 to 12. |
| `month` | Text | Month name as published. |
| `neighbourhood_id` | Text | Neighbourhood number in the current 158-neighbourhood model, zero padded. NSA means the location was not mapped to a neighbourhood. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `event_type` | Text | Shooting or Firearm Discharge, as classified in the source. |
| `events` | Integer | Number of events in that neighbourhood, month and type. |
| `deaths` | Integer | Number of deaths recorded for the event. Zero when none were recorded. |
| `injuries` | Integer | Number of injuries recorded for the event. Zero when none were recorded. |

### `shootings_yearly_by_neighbourhood.csv`

Annual totals by neighbourhood, with shootings and firearm discharges split out.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the occurrence. |
| `neighbourhood_id` | Text | Neighbourhood number in the current 158-neighbourhood model, zero padded. NSA means the location was not mapped to a neighbourhood. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `events` | Integer | Number of events in that neighbourhood, month and type. |
| `deaths` | Integer | Number of deaths recorded for the event. Zero when none were recorded. |
| `injuries` | Integer | Number of injuries recorded for the event. Zero when none were recorded. |
| `shootings` | Integer | Events classified as Shooting. |
| `firearm_discharges` | Integer | Events classified as Firearm Discharge. |

## Source and licence

**Source:** City of Toronto Open Data, Shootings and Firearm Discharges (https://open.toronto.ca/dataset/shootings-firearm-discharges/), published by the Toronto Police Service. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto. TPS Public Safety Data Portal terms also apply.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoshootingsfirearmdischarges,
  author    = {Khan, John},
  title     = {Toronto Shootings and Firearm Discharges},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-shootings-firearm-discharges}
}
```

APA: Khan, J. (2026). *Toronto Shootings and Firearm Discharges* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-shootings-firearm-discharges

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Every shooting and firearm discharge occurrence reported to the Toronto Police Service from 2004 through 2026, aggregated to Toronto's 158 social planning neighbourhoods. The official file includes map coordinates that the Service offsets to the nearest intersection. Those coordinates, and the raw geometry, are not in this version. You get a tidy event file without points, plus monthly and yearly neighbourhood counts.

6,893 events from 2004 to 2026. 2026: 116 events.

## Files

| File | What is in it |
|---|---|
| `shooting_events.csv` | One row per event, without coordinates |
| `shootings_monthly_by_neighbourhood.csv` | Monthly counts by neighbourhood and event type |
| `shootings_yearly_by_neighbourhood.csv` | Annual neighbourhood totals, with shootings and discharges split |
| `shootings_citywide_by_year.csv` | Citywide annual totals |
| `shootings_citywide_by_year_and_type.csv` | Citywide annual totals by type |
| `neighbourhoods.csv` | 158-neighbourhood lookup and centroids |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the citywide yearly series |

## Coverage and refresh

I pulled the City of Toronto Open Data CSV on November 9, 2026. The catalogue resource last modified date was 2026-07-20. The Service has published this series since 2004 and refreshes it periodically through the year. Late reports can still change the most recent months.

## Caveats

* These are occurrences reported to the Toronto Police Service, including some that may later have been deemed unfounded, as noted on the City catalogue page.
* `NSA` in the neighbourhood fields means the event was not mapped to a neighbourhood (often a missing or out-of-city location).
* The 158-neighbourhood identifiers are the current City model. The `_140` columns keep the older 140-neighbourhood model so you can join historical files. Neighbourhood boundaries changed when the City went from 140 to 158 areas, so those two ids are not interchangeable.
* Death and injury figures are the counts recorded on the source event, not a complete public-health dataset.
* Do not treat dropped coordinates as something you can recover from this file. If you need the official offset points, use the City catalogue.

## Sources

Toronto Police Service, Shootings and Firearm Discharges, on the City of Toronto Open Data portal: https://open.toronto.ca/dataset/shootings-firearm-discharges/

Dashboard and further notes: https://data.torontopolice.on.ca/pages/shootings

Neighbourhood names also come from the City Neighbourhoods file: https://open.toronto.ca/dataset/neighbourhoods/

Pulled on November 9, 2026.

## Example uses

* Follow the yearly path of shooting events by neighbourhood after 2018.
* Compare injuries and deaths as a share of events in each police division or neighbourhood.
* Join the yearly file to census profiles or to the neighbourhood crime rates file on `neighbourhood_id`.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). This table is also published by the Toronto Police Service on the Public Safety Data Portal and is subject to the Toronto Police Service terms of use (https://data.torontopolice.on.ca/pages/terms-of-use). This dataset is not endorsed by the City of Toronto or the Toronto Police Service.

Changes made here: point coordinates and geometry were dropped, columns were renamed to snake_case, neighbourhood names were cleaned of trailing numbers, and monthly, yearly and citywide aggregates were added. Event counts were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
