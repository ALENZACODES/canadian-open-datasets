<p align="center"><img src="../../assets/theme-public-safety.png" alt="Toronto Bicycle Thefts by Neighbourhood" width="100%"></p>

# Toronto Bicycle Thefts by Neighbourhood

*158-neighbourhood counts from official records, 1975 to 2026*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 1975 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-bicycle-thefts-by-neighbourhood](https://www.kaggle.com/datasets/johnnykhan1/toronto-bicycle-thefts-by-neighbourhood)

## What it is

Bicycle theft occurrences reported to the Toronto Police Service, 1975 to 2026, joined to Toronto's current 158 social planning neighbourhoods. The official file has no neighbourhood field, only map coordinates that the Service offsets to the nearest intersection. I assigned each offset point to a neighbourhood with a point-in-polygon join, then dropped the coordinates, street-level geometry, and bike make, model, colour and cost.

40,583 theft records. 40,195 mapped to a 158-neighbourhood area. Point coordinates were dropped.

Older copies on Kaggle generally stop around 2019 or 2021 and keep the offset points. This version is newer and is already rolled up to the 158-neighbourhood model.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`bicycle_thefts_by_year_and_bike_type.csv`](data/bicycle_thefts_by_year_and_bike_type.csv) | 2 KB | in this repository |
| [`bicycle_thefts_by_year_and_premises.csv`](data/bicycle_thefts_by_year_and_premises.csv) | 2 KB | in this repository |
| [`bicycle_thefts_citywide_by_year.csv`](data/bicycle_thefts_citywide_by_year.csv) | 1 KB | in this repository |
| [`bicycle_thefts_monthly_by_neighbourhood.csv`](data/bicycle_thefts_monthly_by_neighbourhood.csv) | 1.8 MB | in this repository |
| [`bicycle_thefts_yearly_by_neighbourhood.csv`](data/bicycle_thefts_yearly_by_neighbourhood.csv) | 62 KB | in this repository |
| [`cover.png`](data/cover.png) | 79 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |

## Columns

### `bicycle_thefts_by_year_and_bike_type.csv`

Citywide annual counts by bicycle type code.

| Column | Type | Description |
|---|---|---|
| `occurrence_year` | Integer | Year of the occurrence. |
| `bike_type` | Text | Bicycle type code as published by the Toronto Police Service. |
| `thefts` | Integer | Number of bicycle theft records in that group. |

### `bicycle_thefts_by_year_and_premises.csv`

Citywide annual counts by premises type.

| Column | Type | Description |
|---|---|---|
| `occurrence_year` | Integer | Year of the occurrence. |
| `premises_type` | Text | Premises type as published (for example House, Apartment, Commercial, Outside). |
| `thefts` | Integer | Number of bicycle theft records in that group. |

### `bicycle_thefts_citywide_by_year.csv`

Citywide annual counts.

| Column | Type | Description |
|---|---|---|
| `occurrence_year` | Integer | Year of the occurrence. |
| `thefts` | Integer | Number of bicycle theft records in that group. |

### `bicycle_thefts_monthly_by_neighbourhood.csv`

Monthly bicycle theft counts by neighbourhood, premises type, bike type and status. Make, model, colour, cost and coordinates are not included.

| Column | Type | Description |
|---|---|---|
| `occurrence_year` | Integer | Year of the occurrence. |
| `month_num` | Integer | Month number from 1 to 12. |
| `month` | Text | Month name. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon. NSA if the official offset point could not be mapped. |
| `neighbourhood_name` | Text | Neighbourhood name, or NSA. |
| `premises_type` | Text | Premises type as published (for example House, Apartment, Commercial, Outside). |
| `bike_type` | Text | Bicycle type code as published by the Toronto Police Service. |
| `status` | Text | Occurrence status as published (for example Stolen or Recovered). |
| `thefts` | Integer | Number of bicycle theft records in that group. |

### `bicycle_thefts_yearly_by_neighbourhood.csv`

Annual bicycle theft counts by neighbourhood, with recovered counts.

| Column | Type | Description |
|---|---|---|
| `occurrence_year` | Integer | Year of the occurrence. |
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon. NSA if the official offset point could not be mapped. |
| `neighbourhood_name` | Text | Neighbourhood name, or NSA. |
| `thefts` | Integer | Number of bicycle theft records in that group. |
| `recovered` | Integer | Records whose status is Recovered. |

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | 158-neighbourhood model number assigned by point-in-polygon. NSA if the official offset point could not be mapped. |
| `neighbourhood_name` | Text | Neighbourhood name, or NSA. |
| `neighbourhood_label` | Text | Name with the number in parentheses. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `classification_code` | Text | Short classification code. |
| `centroid_longitude` | Text | Longitude of the polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the polygon centroid, WGS84. |

## Source and licence

**Source:** City of Toronto Open Data, Bicycle Thefts (https://open.toronto.ca/dataset/bicycle-thefts/), published by the Toronto Police Service. Neighbourhood assignment used City neighbourhood boundaries. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto. TPS terms also apply.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontobicycletheftsbyneighbourhood,
  author    = {Khan, John},
  title     = {Toronto Bicycle Thefts by Neighbourhood},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-bicycle-thefts-by-neighbourhood}
}
```

APA: Khan, J. (2026). *Toronto Bicycle Thefts by Neighbourhood* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-bicycle-thefts-by-neighbourhood

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Bicycle theft occurrences reported to the Toronto Police Service, 1975 to 2026, joined to Toronto's current 158 social planning neighbourhoods. The official file has no neighbourhood field, only map coordinates that the Service offsets to the nearest intersection. I assigned each offset point to a neighbourhood with a point-in-polygon join, then dropped the coordinates, street-level geometry, and bike make, model, colour and cost.

40,583 theft records. 40,195 mapped to a 158-neighbourhood area. Point coordinates were dropped.

Older copies on Kaggle generally stop around 2019 or 2021 and keep the offset points. This version is newer and is already rolled up to the 158-neighbourhood model.

## Files

| File | What is in it |
|---|---|
| `bicycle_thefts_monthly_by_neighbourhood.csv` | Monthly counts by neighbourhood, premises, bike type and status |
| `bicycle_thefts_yearly_by_neighbourhood.csv` | Annual neighbourhood counts, with recovered counts |
| `bicycle_thefts_citywide_by_year.csv` | Citywide annual counts |
| `bicycle_thefts_by_year_and_premises.csv` | Annual counts by premises type |
| `bicycle_thefts_by_year_and_bike_type.csv` | Annual counts by bicycle type code |
| `neighbourhoods.csv` | 158-neighbourhood lookup |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the citywide yearly series |

## Coverage and refresh

Pulled on November 9, 2026 from the City of Toronto Open Data portal. Resource last modified: 2026-07-20. The Service refreshes this file periodically. Late reports can still change recent months. A small number of occurrence dates fall in the year before the published start of the series because the theft was reported later.

## Caveats

* Coordinates in the official file are offset to the nearest intersection, so the neighbourhood is the neighbourhood of that offset point, not a precise theft location.
* Records with missing or dummy coordinates are labelled `NSA` and are still included in citywide totals.
* Bike type is the code as published. I did not add a made-up legend for those codes.
* 59 records have an occurrence year before 2014. The Service describes the series as starting in 2014. Those earlier dates are kept in the files and are usually late reports of older events. The cover chart starts in 2014 so the scale stays readable.
* These are reported occurrences, not a complete count of every stolen bicycle in the city.

## Sources

Toronto Police Service, Bicycle Thefts, on the City of Toronto Open Data portal: https://open.toronto.ca/dataset/bicycle-thefts/

Dashboard: https://data.torontopolice.on.ca/pages/c78364ab031747359fa8afb78febdd3d

Neighbourhood boundaries: https://open.toronto.ca/dataset/neighbourhoods/

Pulled on November 9, 2026.

## Example uses

* See which neighbourhoods and premises types account for the most thefts in recent summers.
* Compare recovered shares by neighbourhood.
* Join the yearly file to cycling counts or to the neighbourhood crime rates file on `neighbourhood_id`.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). This table is also published by the Toronto Police Service on the Public Safety Data Portal and is subject to the Toronto Police Service terms of use (https://data.torontopolice.on.ca/pages/terms-of-use). This dataset is not endorsed by the City of Toronto or the Toronto Police Service.

Changes made here: offset points were used only to assign a 158-neighbourhood id and were then dropped, make, model, colour and cost were dropped, columns were renamed, and monthly, yearly and citywide aggregates were added.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
