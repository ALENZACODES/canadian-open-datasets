<p align="center"><img src="../../assets/theme-environment.png" alt="Canada hydrometric daily flow selected" width="100%"></p>

# Canada hydrometric daily flow selected

*Daily mean discharge for major rivers, 2000 to 2024*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1 January 2000 to 31 December 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-hydrometric-daily-flow-selected](https://www.kaggle.com/datasets/johnnykhan1/canada-hydrometric-daily-flow-selected)

## What it is

Daily mean discharge for a selected set of major Canadian rivers from the Water Survey of Canada historical hydrometric archive, accessed through the MSC GeoMet HYDAT daily mean API. Station metadata and an annual summary are included.

Source dataset: [Historical Hydrometric Data](https://open.canada.ca/data/en/dataset/1ee9e14d-0814-5201-a3be-705809d8ee0e) (Environment and Climate Change Canada, Water Survey of Canada / HYDAT).

Daily means pulled on November 9, 2026 from https://api.weather.gc.ca/collections/hydrometric-daily-mean/

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`annual_flow_summary.csv`](data/annual_flow_summary.csv) | 21 KB | in this repository |
| [`cover.png`](data/cover.png) | 69 KB | in this repository |
| [`daily_mean_flow.csv`](data/daily_mean_flow.csv) | 8.3 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`stations.csv`](data/stations.csv) | 1 KB | in this repository |

## Columns

### `annual_flow_summary.csv`

Annual discharge summary by station.

| Column | Type | Description |
|---|---|---|
| `station_number` | Text | Water Survey of Canada station number. |
| `station_name` | Text | Station name as published by HYDAT / GeoMet. |
| `province` | Text | Province or territory code. |
| `year` | Integer | Calendar year. |
| `n_days` | Integer | Count of days with discharge in the summary period. |
| `mean_discharge_m3s` | Float | Mean daily discharge in cubic metres per second. |
| `max_discharge_m3s` | Float | Maximum daily discharge in cubic metres per second. |
| `min_discharge_m3s` | Float | Minimum daily discharge in cubic metres per second. |

### `daily_mean_flow.csv`

Daily mean discharge (and level when present) for selected stations, 2000 to 2024.

| Column | Type | Description |
|---|---|---|
| `station_number` | Text | Water Survey of Canada station number. |
| `station_name` | Text | Station name as published by HYDAT / GeoMet. |
| `province` | Text | Province or territory code. |
| `date` | Date | Calendar date of the daily mean (YYYY-MM-DD). |
| `discharge_m3s` | Float | Daily mean discharge in cubic metres per second. |
| `discharge_symbol` | Text | English discharge quality symbol when published. |
| `level_m` | Text | Daily mean water level in metres when published. |

### `data_dictionary.csv`

- `column`: Name of the column being described - `file`: File that contains the column - `type`: Data type of the column - `description`: Plain-language description of the column

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `stations.csv`

Selected hydrometric stations and coverage in this snapshot.

| Column | Type | Description |
|---|---|---|
| `station_number` | Text | Water Survey of Canada station number. |
| `station_name` | Text | Station name as published by HYDAT / GeoMet. |
| `province` | Text | Province or territory code. |
| `n_days` | Integer | Count of days with discharge in the summary period. |
| `date_start` | Date | First date with data in this snapshot. |
| `date_end` | Date | Last date with data in this snapshot. |
| `mean_discharge_m3s` | Float | Mean daily discharge in cubic metres per second. |
| `max_discharge_m3s` | Float | Maximum daily discharge in cubic metres per second. |

## Source and licence

**Source:** Environment and Climate Change Canada, Water Survey of Canada / HYDAT, Historical Hydrometric Data, MSC GeoMet hydrometric daily mean API, via open.canada.ca, Open Government Licence Canada

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahydrometricdailyflowselected,
  author    = {Khan, John},
  title     = {Canada hydrometric daily flow selected},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-hydrometric-daily-flow-selected}
}
```

APA: Khan, J. (2026). *Canada hydrometric daily flow selected* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-hydrometric-daily-flow-selected

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Daily mean discharge for a selected set of major Canadian rivers from the Water Survey of Canada historical hydrometric archive, accessed through the MSC GeoMet HYDAT daily mean API. Station metadata and an annual summary are included.

Source dataset: [Historical Hydrometric Data](https://open.canada.ca/data/en/dataset/1ee9e14d-0814-5201-a3be-705809d8ee0e) (Environment and Climate Change Canada, Water Survey of Canada / HYDAT).

Daily means pulled on November 9, 2026 from https://api.weather.gc.ca/collections/hydrometric-daily-mean/

## Coverage

13 selected stations on rivers including the Niagara, Ottawa, Fraser, Mackenzie, South Saskatchewan, Athabasca, Peace, Saint John and Red. About 111,726 daily rows from 2000 through 2024 where published. Discharge is in cubic metres per second.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. HYDAT is updated on a quarterly cycle. For later days, query the GeoMet hydrometric daily mean collection or download the HYDAT database.

## A few numbers from this snapshot

* 13 stations are included.
* 111,726 daily rows are in the main file.
* Among these stations, the highest mean discharge in the snapshot window is MACKENZIE RIVER AT ARCTIC RED RIVER (10LC014) at about 9,225 cubic metres per second.

## Example uses

* Plot seasonal hydrographs for a chosen river.
* Compare annual mean flow across basins.
* Study high flow days using the annual maximums.

## Caveats

This is a selected station list, not the full HYDAT archive. Some days are missing or flagged with quality symbols. Station 05AH005 was checked and skipped because the published name did not match the intended South Saskatchewan at Saskatoon target. Values are daily means, not instantaneous peaks.

## Files

* `stations.csv`: Selected hydrometric stations and coverage in this snapshot.
* `daily_mean_flow.csv`: Daily mean discharge (and level when present) for selected stations, 2000 to 2024.
* `annual_flow_summary.csv`: Annual discharge summary by station.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, Water Survey of Canada, Historical Hydrometric Data (HYDAT). The published values were not changed. Columns were renamed and summary files were derived. This is not an official Government of Canada product and Environment and Climate Change Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
