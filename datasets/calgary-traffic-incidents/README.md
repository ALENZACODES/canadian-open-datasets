<p align="center"><img src="../../assets/theme-public-safety.png" alt="Calgary traffic incidents" width="100%"></p>

# Calgary traffic incidents

*City of Calgary traffic incident records with coordinates*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 1 December 2016 to 9 November 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/calgary-traffic-incidents](https://www.kaggle.com/datasets/johnnykhan1/calgary-traffic-incidents)

## What it is

Traffic incident records from the City of Calgary open data portal, with location text, timestamps, quadrant and coordinates.

Portal: [Traffic Incidents](https://data.calgary.ca/d/35ra-9556).

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`calgary_traffic_incidents.csv`](data/calgary_traffic_incidents.csv) | 15.6 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 1 KB | in this repository |
| [`monthly_incident_counts.csv`](data/monthly_incident_counts.csv) | 2 KB | in this repository |

## Columns

### `calgary_traffic_incidents.csv`

Traffic incident records for Calgary.

| Column | Type | Description |
|---|---|---|
| `incident_info` | Text | Short location or incident info text. |
| `description` | Text | Incident description. |
| `start_dt_utc` | Date | Incident start timestamp in UTC. |
| `modified_dt_utc` | Date | Last modified timestamp in UTC. |
| `quadrant` | Text | Calgary quadrant (NW, NE, SW, SE). |
| `longitude` | Text | Longitude. |
| `latitude` | Text | Latitude. |
| `count` | Float | Count field as published by the City of Calgary. |
| `id` | Text | Record id as published. |
| `point` | Text | Point geography as published (WKT). |
| `start_date` | Date | Calendar date of start_dt_utc. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `monthly_incident_counts.csv`

Monthly incident counts derived from start dates.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Month start for aggregated counts. |
| `incidents` | Integer | Number of incident rows in that month. |

## Source and licence

**Source:** City of Calgary Open Data, Traffic Incidents (Socrata 35ra-9556), https://data.calgary.ca/d/35ra-9556 downloaded November 9, 2026. Prepared by John Khan in Toronto, Ontario. City of Calgary Open Data Licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – City of Calgary](https://data.calgary.ca/stories/s/Open-Calgary-Terms-of-Use/u45n-7awa). Contains information licensed under the Open Government Licence – City of Calgary.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026calgarytrafficincidents,
  author    = {Khan, John},
  title     = {Calgary traffic incidents},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/calgary-traffic-incidents}
}
```

APA: Khan, J. (2026). *Calgary traffic incidents* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/calgary-traffic-incidents

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Traffic incident records from the City of Calgary open data portal, with location text, timestamps, quadrant and coordinates.

Portal: [Traffic Incidents](https://data.calgary.ca/d/35ra-9556).

## Coverage

2016-12-06 to 2026-11-09 in this snapshot (65,791 rows).

## Updates

Snapshot from November 9, 2026. Not auto refreshed.

## A few numbers from this snapshot

* Incident file has 65,791 rows from 2016-12-06 to 2026-11-09.
* Quadrant mix: SE 16128, ? 14058, NE 14011, NW 11302.

## Example uses

* Map incidents by quadrant.
* Study seasonal patterns in monthly counts.
* Join to weather or road network layers.

## Caveats

* Records reflect incidents as published by the City of Calgary. Descriptions are short operational text.
* Coordinates can be missing.
* Timestamps are stored in UTC in the source feed.

## Licence

Shared under the City of Calgary Open Data Licence as stated on the portal. Source: City of Calgary. Not an official City of Calgary product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
