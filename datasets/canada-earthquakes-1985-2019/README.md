<p align="center"><img src="../../assets/theme-environment.png" alt="Canada earthquakes 1985 to 2019" width="100%"></p>

# Canada earthquakes 1985 to 2019

*NRCan located earthquakes with magnitude, depth and place*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1985 to 2019 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-earthquakes-1985-2019](https://www.kaggle.com/datasets/johnnykhan1/canada-earthquakes-1985-2019)

## What it is

Located earthquakes for Canada and nearby areas from the Natural Resources Canada English archive CSV. Columns were renamed to snake_case, an empty trailing column was dropped, and a clean region_or_note field was kept from the free text that followed the place name.

Source dataset: [Earthquakes in Canada](https://open.canada.ca/data/en/dataset/4cedd37e-0023-41fe-8eff-bea45385e469) (Natural Resources Canada, Earthquakes Canada).

CSV pulled on November 9, 2026 from https://ftp.maps.canada.ca/pub/nrcan_rncan/Earthquakes_Tremblement-de-terre/canadian-earthquakes_tremblements-de-terre-canadien/eqarchive-en.csv

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`BUILD_RESULT.json`](data/BUILD_RESULT.json) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 62 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`earthquakes_annual_summary.csv`](data/earthquakes_annual_summary.csv) | 1 KB | in this repository |
| [`earthquakes_canada_1985_2019.csv`](data/earthquakes_canada_1985_2019.csv) | 9.8 MB | in this repository |
| [`earthquakes_magnitude_4_and_up.csv`](data/earthquakes_magnitude_4_and_up.csv) | 253 KB | in this repository |

## Columns

### `data_dictionary.csv`

- `column`: Name of the column being described - `file`: File that contains the column - `type`: Data type of the column - `description`: Plain-language description of the column

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `earthquakes_annual_summary.csv`

Annual event counts and magnitude summary.

| Column | Type | Description |
|---|---|---|
| `event_year` | Integer | UTC calendar year of the event, derived from event_time_utc. |
| `event_count` | Integer | Number of events in the year after dropping rows missing latitude, longitude or magnitude. |
| `max_magnitude` | Float | Largest magnitude recorded in that year. |
| `median_magnitude` | Float | Median magnitude in that year. |
| `mean_depth_km` | Float | Mean depth in kilometres for events in that year. |

### `earthquakes_canada_1985_2019.csv`

All located events from the NRCan English archive CSV, tidied.

| Column | Type | Description |
|---|---|---|
| `event_time_utc` | Date | Origin time in Coordinated Universal Time as published (ISO 8601 with +0000 offset). |
| `latitude` | Text | Epicentre latitude in decimal degrees. |
| `longitude` | Text | Epicentre longitude in decimal degrees. |
| `depth_km` | Float | Depth of the event below the surface in kilometres. Many values are nominal or poorly constrained. |
| `magnitude` | Float | Event magnitude as published. Negative values appear for very small events. |
| `magnitude_type` | Text | Magnitude scale code (for example ML, MN, Mw, mb, MS). |
| `place` | Text | Distance and direction from the nearest named place, as published. |
| `region_or_note` | Text | Province, territory, state or free text note that followed the place field in the source file (spelling and punctuation retained). |
| `event_date` | Date | Calendar date of the event in UTC (YYYY-MM-DD), derived from event_time_utc. |
| `event_year` | Integer | UTC calendar year of the event, derived from event_time_utc. |

### `earthquakes_magnitude_4_and_up.csv`

Subset of events with magnitude 4.0 or higher.

| Column | Type | Description |
|---|---|---|
| `event_time_utc` | Date | Origin time in Coordinated Universal Time as published (ISO 8601 with +0000 offset). |
| `latitude` | Text | Epicentre latitude in decimal degrees. |
| `longitude` | Text | Epicentre longitude in decimal degrees. |
| `depth_km` | Float | Depth of the event below the surface in kilometres. Many values are nominal or poorly constrained. |
| `magnitude` | Float | Event magnitude as published. Negative values appear for very small events. |
| `magnitude_type` | Text | Magnitude scale code (for example ML, MN, Mw, mb, MS). |
| `place` | Text | Distance and direction from the nearest named place, as published. |
| `region_or_note` | Text | Province, territory, state or free text note that followed the place field in the source file (spelling and punctuation retained). |
| `event_date` | Date | Calendar date of the event in UTC (YYYY-MM-DD), derived from event_time_utc. |
| `event_year` | Integer | UTC calendar year of the event, derived from event_time_utc. |

## Source and licence

**Source:** Natural Resources Canada, Earthquakes Canada, Earthquakes in Canada, via open.canada.ca, Open Government Licence Canada

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaearthquakes19852019,
  author    = {Khan, John},
  title     = {Canada earthquakes 1985 to 2019},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-earthquakes-1985-2019}
}
```

APA: Khan, J. (2026). *Canada earthquakes 1985 to 2019* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-earthquakes-1985-2019

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Located earthquakes for Canada and nearby areas from the Natural Resources Canada English archive CSV. Columns were renamed to snake_case, an empty trailing column was dropped, and a clean region_or_note field was kept from the free text that followed the place name.

Source dataset: [Earthquakes in Canada](https://open.canada.ca/data/en/dataset/4cedd37e-0023-41fe-8eff-bea45385e469) (Natural Resources Canada, Earthquakes Canada).

CSV pulled on November 9, 2026 from https://ftp.maps.canada.ca/pub/nrcan_rncan/Earthquakes_Tremblement-de-terre/canadian-earthquakes_tremblements-de-terre-canadien/eqarchive-en.csv

## Coverage

101,365 events with latitude, longitude and magnitude, from 1985 through 2019. The file covers Canada and nearby areas (including parts of Alaska and Washington State) as published by Earthquakes Canada. Magnitude types include ML, MN, Mw and others.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. The Open Government CSV ends in 2019. For events after 2019, use the live search on https://www.earthquakescanada.nrcan.gc.ca/

## A few numbers from this snapshot

* 101,365 located events remain after dropping rows that were missing latitude, longitude or magnitude.
* 2,605 of those events have magnitude 4.0 or higher.
* The largest magnitude in the file is 7.7. It occurred at 2012-10-28T03:04:06+0000 near 83 km SSW of Sandspit.

## Example uses

* Map epicentres and filter by magnitude or depth.
* Count events by year or by region_or_note for hazard screens.
* Study the magnitude 4 and up subset for felt event patterns.

## Caveats

Depth is often poorly known and many depths are nominal. Province and state spellings in region_or_note changed over the years (BC vs B.C., QC vs QUE.). Negative magnitudes are valid for very small events. This archive stops at the end of 2019.

## Files

* `earthquakes_canada_1985_2019.csv`: All located events from the NRCan English archive CSV, tidied.
* `earthquakes_annual_summary.csv`: Annual event counts and magnitude summary.
* `earthquakes_magnitude_4_and_up.csv`: Subset of events with magnitude 4.0 or higher.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Natural Resources Canada, Earthquakes Canada, Earthquakes in Canada archive. The published values were not changed. Columns were renamed and summary files were derived. This is not an official Government of Canada product and Natural Resources Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
