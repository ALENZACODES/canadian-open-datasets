<p align="center"><img src="../../assets/theme-environment.png" alt="Canada Great Lakes monthly levels" width="100%"></p>

# Canada Great Lakes monthly levels

*CHS coordinated means on IGLD 1985, including Montreal Harbour*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1918 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-great-lakes-monthly-levels](https://www.kaggle.com/datasets/johnnykhan1/canada-great-lakes-monthly-levels)

## What it is

Monthly mean water levels for the Great Lakes coordinated network and for Montreal Harbour, in metres referred to the International Great Lakes Datum 1985 (IGLD 1985). The tables were published by the Canadian Hydrographic Service (CHS), Fisheries and Oceans Canada.

Source pages: [Monthly Historical Great Lakes Means](https://www.tides.gc.ca/en/monthly-historical-great-lakes-means) (date modified 2026-10-22 on the index page when this snapshot was taken).

Tables were read from the official English coordinated-network pages on November 9, 2026. Chart-datum tables that appear on the same pages are not included, so every value in this pack uses one datum.

This is a different product from the Water Survey of Canada HYDAT daily river-flow set already on Kaggle.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`annual_levels.csv`](data/annual_levels.csv) | 65 KB | in this repository |
| [`cover.png`](data/cover.png) | 171 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 4 KB | in this repository |
| [`monthly_climatology.csv`](data/monthly_climatology.csv) | 22 KB | in this repository |
| [`monthly_levels_long.csv`](data/monthly_levels_long.csv) | 444 KB | in this repository |
| [`waterbodies.csv`](data/waterbodies.csv) | 1 KB | in this repository |

## Columns

### `annual_levels.csv`

Annual mean, minimum, maximum and range from the CHS yearly table, plus the record-mean anomaly.

| Column | Type | Description |
|---|---|---|
| `waterbody_id` | Text | Short identifier for the lake or harbour. |
| `waterbody` | Text | Published name (Lake Superior, Lakes Michigan-Huron, Lake St. Clair, Lake Erie, Lake Ontario, or Montreal Harbour). |
| `year` | Integer | Calendar year of the monthly or annual mean. |
| `annual_mean_m_igld1985` | Float | Annual mean water level in metres, IGLD 1985, as published in the CHS yearly table. |
| `annual_min_m_igld1985` | Float | Lowest monthly mean in that year, in metres, IGLD 1985, as published. |
| `annual_max_m_igld1985` | Float | Highest monthly mean in that year, in metres, IGLD 1985, as published. |
| `annual_range_m` | Float | Annual range in metres, as published where present, otherwise maximum minus minimum. |
| `datum` | Text | Vertical datum of the published values. All series here are IGLD 1985. |
| `unit` | Text | Unit of the water level values (metre). |
| `record_mean_m_igld1985` | Float | Mean of the published annual means over the full record for that waterbody, in metres, IGLD 1985. |
| `anomaly_m` | Float | Annual mean minus the record mean for that waterbody, in metres. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `monthly_climatology.csv`

All-time and 2016-2025 monthly average, minimum and maximum levels from the CHS summary tables.

| Column | Type | Description |
|---|---|---|
| `waterbody_id` | Text | Short identifier for the lake or harbour. |
| `waterbody` | Text | Published name (Lake Superior, Lakes Michigan-Huron, Lake St. Clair, Lake Erie, Lake Ontario, or Montreal Harbour). |
| `period` | Text | Climatology window: all-time, or 2016-2025. |
| `statistic` | Text | average, minimum or maximum, as labelled on the CHS summary table. |
| `month` | Integer | Month number, 1 to 12. |
| `month_name` | Text | Month name. |
| `water_level_m_igld1985` | Float | Monthly mean water level in metres referred to the International Great Lakes Datum 1985 (IGLD 1985). |
| `datum` | Text | Vertical datum of the published values. All series here are IGLD 1985. |
| `unit` | Text | Unit of the water level values (metre). |

### `monthly_levels_long.csv`

Monthly mean water levels in metres, IGLD 1985, one row per waterbody-year-month.

| Column | Type | Description |
|---|---|---|
| `waterbody_id` | Text | Short identifier for the lake or harbour. |
| `waterbody` | Text | Published name (Lake Superior, Lakes Michigan-Huron, Lake St. Clair, Lake Erie, Lake Ontario, or Montreal Harbour). |
| `year` | Integer | Calendar year of the monthly or annual mean. |
| `month` | Integer | Month number, 1 to 12. |
| `month_name` | Text | Month name. |
| `water_level_m_igld1985` | Float | Monthly mean water level in metres referred to the International Great Lakes Datum 1985 (IGLD 1985). |
| `datum` | Text | Vertical datum of the published values. All series here are IGLD 1985. |
| `unit` | Text | Unit of the water level values (metre). |

### `waterbodies.csv`

Waterbody list, record span, datum and source page.

| Column | Type | Description |
|---|---|---|
| `waterbody_id` | Text | Short identifier for the lake or harbour. |
| `waterbody` | Text | Published name (Lake Superior, Lakes Michigan-Huron, Lake St. Clair, Lake Erie, Lake Ontario, or Montreal Harbour). |
| `kind` | Text | lake or harbour. |
| `record_start_year` | Integer | First year in the published coordinated-network series. |
| `record_end_year` | Integer | Last year in the published coordinated-network series. |
| `n_years` | Integer | Number of years in the published series. |
| `datum` | Text | Vertical datum of the published values. All series here are IGLD 1985. |
| `unit` | Text | Unit of the water level values (metre). |
| `source_page` | Text | CHS page the table was read from. |
| `record_mean_m_igld1985` | Float | Mean of the published annual means over the full record for that waterbody, in metres, IGLD 1985. |

## Source and licence

**Source:** Fisheries and Oceans Canada, Canadian Hydrographic Service, Monthly Historical Great Lakes Means, https://www.tides.gc.ca/en/monthly-historical-great-lakes-means. Coordinated-network tables for Lake Superior, Lakes Michigan-Huron, Lake St. Clair, Lake Erie, Lake Ontario and Montreal Harbour, metres referred to IGLD 1985.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadagreatlakesmonthlylevels,
  author    = {Khan, John},
  title     = {Canada Great Lakes monthly levels},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-great-lakes-monthly-levels}
}
```

APA: Khan, J. (2026). *Canada Great Lakes monthly levels* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-great-lakes-monthly-levels

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly mean water levels for the Great Lakes coordinated network and for Montreal Harbour, in metres referred to the International Great Lakes Datum 1985 (IGLD 1985). The tables were published by the Canadian Hydrographic Service (CHS), Fisheries and Oceans Canada.

Source pages: [Monthly Historical Great Lakes Means](https://www.tides.gc.ca/en/monthly-historical-great-lakes-means) (date modified 2026-10-22 on the index page when this snapshot was taken).

Tables were read from the official English coordinated-network pages on November 9, 2026. Chart-datum tables that appear on the same pages are not included, so every value in this pack uses one datum.

This is a different product from the Water Survey of Canada HYDAT daily river-flow set already on Kaggle.

## Coverage

Lake Superior, Lakes Michigan-Huron (published as a single coordinated series), Lake St. Clair, Lake Erie and Lake Ontario from 1918 through 2025 (108 years each). Montreal Harbour from 1967 through 2025 (59 years). 7,188 monthly means are in the long file.

Absolute levels are not comparable across waterbodies without an adjustment: Lake Superior sits near 183 m IGLD 1985, Lakes Michigan-Huron near 176 m, Lake Ontario near 75 m, and Montreal Harbour near 6 to 8 m. Use the anomaly column when comparing departures from each record mean.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. For later months, use the CHS historical means pages or the CHS tides and water levels service.

## A few numbers from this snapshot

* Lake Superior's highest annual mean in the record is 183.75 m in 2019 (record mean 183.41 m). The 2025 annual mean is 183.30 m.
* Lakes Michigan-Huron reached a record annual mean of 177.31 m in 2020 (record mean 176.45 m). The 2025 annual mean is 176.27 m.
* Lake Ontario's highest annual mean is 75.37 m in 1952. The 2019 annual mean was 75.27 m. The 2025 annual mean is 74.71 m, close to the record mean of 74.77 m.
* Lake Erie's highest annual mean is 174.90 m in 1986 (record mean 174.18 m). The 2025 annual mean is 174.25 m.
* Montreal Harbour's highest annual mean is 7.53 m in 1973 and the lowest is 5.79 m in 2001 (record mean 6.64 m). The 2025 annual mean is 6.11 m.

## Example uses

* Plot annual mean anomalies for one lake against its record mean.
* Compare the seasonal cycle in the all-time climatology with the 2016-2025 window.
* Put Montreal Harbour beside Lake Ontario while keeping the different absolute datums in mind.

## Caveats

Values are monthly means from the binational coordinated network, not instantaneous gauge readings and not Water Survey of Canada daily HYDAT levels. Michigan and Huron are published as one series. Recent months may later be revised by CHS. Do not mix these IGLD 1985 values with the chart-datum tables on the same CHS pages.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada).

## Files

* `monthly_levels_long.csv` — one row per waterbody, year and month.
* `annual_levels.csv` — published annual mean, minimum, maximum and range, with the record-mean anomaly.
* `monthly_climatology.csv` — all-time and 2016-2025 monthly average, minimum and maximum.
* `waterbodies.csv` — waterbody list, record span and source page.
* `data_dictionary.csv` — column dictionary.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
