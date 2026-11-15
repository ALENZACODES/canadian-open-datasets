<p align="center"><img src="../../assets/theme-environment.png" alt="Canada wave buoys, selected stations" width="100%"></p>

# Canada wave buoys, selected stations

*DFO MEDS wave and weather records from 12 long-running buoys*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1 January 1987 to 28 March 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-wave-buoys-selected](https://www.kaggle.com/datasets/johnnykhan1/canada-wave-buoys-selected)

## What it is

A tidy extract of Fisheries and Oceans Canada's Canadian Wave Data archive for 12 selected long-record buoys: four in the Pacific, four in the Atlantic and four in the Great Lakes. Daily, monthly and annual summaries were computed from the official hourly CSV files. The full hourly archives are not repeated here; each station file in this pack points to the official zip.

Source portal: [Canadian Wave Data](https://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/index-eng.htm) (Fisheries and Oceans Canada, Marine Environmental Data Section). Station list from the official inventory [B_PW_INV.JSON](https://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/WAVE/waveshare/INVENTORY/B_PW_INV.JSON), and hourly files from the official All CSV Data zips, downloaded on November 9, 2026. Format notes: https://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/formats-eng.html#CSV.

Official citation: DFO (2026). Marine Environmental Data Section Archive, https://meds-sdmm.dfo-mpo.gc.ca, Ecosystem and Oceans Science, Department of Fisheries and Oceans Canada. Data obtained on 2026/11/09.

This is a different product from the Canadian Hydrographic Service monthly Great Lakes water-level set already on Kaggle, and from the BC lightstation sea surface temperature and salinity set.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`annual_wave_stats.csv`](data/annual_wave_stats.csv) | 40 KB | in this repository |
| [`cover.png`](data/cover.png) | 156 KB | in this repository |
| [`daily_wave_stats.csv`](data/daily_wave_stats.csv) | 24.1 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 10 KB | in this repository |
| [`monthly_wave_stats.csv`](data/monthly_wave_stats.csv) | 946 KB | in this repository |
| [`stations.csv`](data/stations.csv) | 4 KB | in this repository |

## Columns

### `annual_wave_stats.csv`

Annual peaks and means assembled from the daily summary table.

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | MEDS station identifier, for example C46184. |
| `station_name` | Text | Official station name used in this extract, taken from the latest inventory entry for the identifier. |
| `region` | Text | Grouping used in this extract (Pacific, Atlantic or Great Lakes), based on the station's published location. |
| `year` | Integer | UTC year. |
| `n_days` | Integer | Number of distinct UTC dates in the year with at least one official row. |
| `n_obs` | Float | Number of official rows in the period, including rows whose wave values were later excluded from the means and maxima. |
| `n_vcar_used` | Float | Number of official VCAR values used in the mean and maximum (flag not 4, height between 0 and 30 metres inclusive, and not more than 5 metres away from VWH$ when both are present). |
| `max_vcar_m` | Float | Maximum of usable VCAR values (metres). |
| `max_vcmx_m` | Float | Maximum of usable VCMX values (maximum zero crossing wave height, metres), after dropping flag 4 and heights outside 0 to 30 metres. |
| `mean_vcar_m` | Float | Mean of usable VCAR values (characteristic significant wave height, metres). |
| `mean_sst_c` | Float | Mean of SSTP (sea surface temperature, degrees Celsius). |

### `daily_wave_stats.csv`

Daily means and maxima from official hourly rows, after dropping quality flag 4 (erroneous) wave values, wave heights above 30 metres, and VCAR values that disagree with VWH$ by more than 5 metres.

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | MEDS station identifier, for example C46184. |
| `date` | Date | UTC calendar date of the daily summary. |
| `n_obs` | Float | Number of official rows in the period, including rows whose wave values were later excluded from the means and maxima. |
| `n_q_flag_1` | Float | Number of official rows with quality flag 1 (good). |
| `n_q_flag_7` | Float | Number of official rows with quality flag 7 (off position). |
| `n_q_flag_0` | Float | Number of official rows with quality flag 0 (no quality control performed). |
| `n_q_flag_4` | Float | Number of official rows with quality flag 4 (erroneous). Those wave height and period values are excluded from the means and maxima. |
| `n_vcar_used` | Float | Number of official VCAR values used in the mean and maximum (flag not 4, height between 0 and 30 metres inclusive, and not more than 5 metres away from VWH$ when both are present). |
| `n_vcar_excluded` | Float | Number of official non-null VCAR values excluded as flag 4, as a height outside 0 to 30 metres, or as more than 5 metres away from a present VWH$ value. Official files often use 10000 as a fill value. |
| `mean_vcar_m` | Float | Mean of usable VCAR values (characteristic significant wave height, metres). |
| `max_vcar_m` | Float | Maximum of usable VCAR values (metres). |
| `mean_vwh_m` | Float | Mean of usable VWH$ values (buoy-reported significant wave height, metres), after dropping flag 4 and heights outside 0 to 30 metres. |
| `max_vwh_m` | Float | Maximum of usable VWH$ values (metres). |
| `max_vcmx_m` | Float | Maximum of usable VCMX values (maximum zero crossing wave height, metres), after dropping flag 4 and heights outside 0 to 30 metres. |
| `mean_vtpk_s` | Float | Mean of VTPK (peak period, seconds) on rows that are not flag 4 and have a period between 0 and 60 seconds, exclusive of 0. |
| `mean_wind_speed_1_ms` | Float | Mean of the first WSPD column (horizontal wind speed, metres per second), over official rows with a value. The wave-height exclusion rule is not applied here. |
| `max_gust_speed_1_ms` | Float | Maximum of the first GSPD column (gust wind speed, metres per second). |
| `mean_pressure_1_mbar` | Float | Mean of the first ATMS column (atmospheric pressure at sea level, millibars). |
| `mean_air_temp_c` | Float | Mean of DRYT (dry bulb temperature, degrees Celsius). |
| `mean_sst_c` | Float | Mean of SSTP (sea surface temperature, degrees Celsius). |
| `mean_latitude` | Text | Mean of published latitudes in the period, in decimal degrees (north positive). |
| `mean_longitude` | Text | Mean longitude in the period, converted from the official west-positive values to standard decimal degrees (east positive). |
| `station_name` | Text | Official station name used in this extract, taken from the latest inventory entry for the identifier. |
| `region` | Text | Grouping used in this extract (Pacific, Atlantic or Great Lakes), based on the station's published location. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, number or integer). |
| `description` | Text | What the column contains. |

### `monthly_wave_stats.csv`

Monthly means and maxima using the same wave-value rule as the daily file.

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | MEDS station identifier, for example C46184. |
| `year` | Integer | UTC year. |
| `month` | Integer | UTC month, 1 to 12. |
| `n_obs` | Float | Number of official rows in the period, including rows whose wave values were later excluded from the means and maxima. |
| `n_q_flag_1` | Float | Number of official rows with quality flag 1 (good). |
| `n_q_flag_7` | Float | Number of official rows with quality flag 7 (off position). |
| `n_q_flag_0` | Float | Number of official rows with quality flag 0 (no quality control performed). |
| `n_q_flag_4` | Float | Number of official rows with quality flag 4 (erroneous). Those wave height and period values are excluded from the means and maxima. |
| `n_vcar_used` | Float | Number of official VCAR values used in the mean and maximum (flag not 4, height between 0 and 30 metres inclusive, and not more than 5 metres away from VWH$ when both are present). |
| `n_vcar_excluded` | Float | Number of official non-null VCAR values excluded as flag 4, as a height outside 0 to 30 metres, or as more than 5 metres away from a present VWH$ value. Official files often use 10000 as a fill value. |
| `mean_vcar_m` | Float | Mean of usable VCAR values (characteristic significant wave height, metres). |
| `max_vcar_m` | Float | Maximum of usable VCAR values (metres). |
| `mean_vwh_m` | Float | Mean of usable VWH$ values (buoy-reported significant wave height, metres), after dropping flag 4 and heights outside 0 to 30 metres. |
| `max_vwh_m` | Float | Maximum of usable VWH$ values (metres). |
| `max_vcmx_m` | Float | Maximum of usable VCMX values (maximum zero crossing wave height, metres), after dropping flag 4 and heights outside 0 to 30 metres. |
| `mean_vtpk_s` | Float | Mean of VTPK (peak period, seconds) on rows that are not flag 4 and have a period between 0 and 60 seconds, exclusive of 0. |
| `mean_wind_speed_1_ms` | Float | Mean of the first WSPD column (horizontal wind speed, metres per second), over official rows with a value. The wave-height exclusion rule is not applied here. |
| `max_gust_speed_1_ms` | Float | Maximum of the first GSPD column (gust wind speed, metres per second). |
| `mean_pressure_1_mbar` | Float | Mean of the first ATMS column (atmospheric pressure at sea level, millibars). |
| `mean_air_temp_c` | Float | Mean of DRYT (dry bulb temperature, degrees Celsius). |
| `mean_sst_c` | Float | Mean of SSTP (sea surface temperature, degrees Celsius). |
| `mean_latitude` | Text | Mean of published latitudes in the period, in decimal degrees (north positive). |
| `mean_longitude` | Text | Mean longitude in the period, converted from the official west-positive values to standard decimal degrees (east positive). |
| `station_name` | Text | Official station name used in this extract, taken from the latest inventory entry for the identifier. |
| `region` | Text | Grouping used in this extract (Pacific, Atlantic or Great Lakes), based on the station's published location. |

### `stations.csv`

The 12 selected buoys, with official inventory attributes and the observation date range found in each official hourly CSV.

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | MEDS station identifier, for example C46184. |
| `station_name` | Text | Official station name used in this extract, taken from the latest inventory entry for the identifier. |
| `region` | Text | Grouping used in this extract (Pacific, Atlantic or Great Lakes), based on the station's published location. |
| `inventory_first_start` | Date | Earliest official inventory start date for this identifier. |
| `inventory_last_end` | Date | Latest official inventory end date for this identifier. |
| `inventory_total_days` | Integer | Sum of official inventory total-day values across deployments for this identifier. |
| `inventory_n_deployments` | Integer | Number of official inventory deployment rows for this identifier. |
| `inventory_latest_latitude` | Text | Latitude in decimal degrees from the latest inventory deployment, as published (north positive). |
| `inventory_latest_longitude` | Text | Longitude in decimal degrees from the latest inventory deployment, as published (east positive, so west is negative). |
| `inventory_latest_depth_m` | Integer | Water depth in metres from the latest inventory deployment, as published. |
| `observed_first_datetime_utc` | Date | Earliest observation timestamp in the official hourly CSV, in UTC. |
| `observed_last_datetime_utc` | Date | Latest observation timestamp in the official hourly CSV, in UTC. |
| `n_observations` | Integer | Number of official hourly (or other official sampling) rows in the official CSV for this station. |
| `official_csv_url` | Text | Official All CSV Data zip URL on the MEDS archive. |
| `official_station_page` | Text | Official MEDS download page for this station identifier. |

## Source and licence

**Source:** Fisheries and Oceans Canada, Marine Environmental Data Section, Canadian Wave Data, https://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/index-eng.htm. Station inventory https://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/WAVE/waveshare/INVENTORY/B_PW_INV.JSON. Official All CSV Data zips from https://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/csvData/. CSV format description https://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/formats-eng.html#CSV. Citation: DFO (2026). Marine Environmental Data Section Archive, https://meds-sdmm.dfo-mpo.gc.ca, Ecosystem and Oceans Science, Department of Fisheries and Oceans Canada. Data obtained on 2026/11/09. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026. Wave height and period means and maxima exclude official quality flag 4 (erroneous), wave heights above 30 metres, and VCAR values that differ from VWH$ by more than 5 metres when both are present, because the official files often use 10000 as a fill value and occasionally report an inconsistent VCAR on a flagged-good row.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadawavebuoysselected,
  author    = {Khan, John},
  title     = {Canada wave buoys, selected stations},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-wave-buoys-selected}
}
```

APA: Khan, J. (2026). *Canada wave buoys, selected stations* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-wave-buoys-selected

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of Fisheries and Oceans Canada's Canadian Wave Data archive for 12 selected long-record buoys: four in the Pacific, four in the Atlantic and four in the Great Lakes. Daily, monthly and annual summaries were computed from the official hourly CSV files. The full hourly archives are not repeated here; each station file in this pack points to the official zip.

Source portal: [Canadian Wave Data](https://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/index-eng.htm) (Fisheries and Oceans Canada, Marine Environmental Data Section). Station list from the official inventory [B_PW_INV.JSON](https://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/WAVE/waveshare/INVENTORY/B_PW_INV.JSON), and hourly files from the official All CSV Data zips, downloaded on November 9, 2026. Format notes: https://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/formats-eng.html#CSV.

Official citation: DFO (2026). Marine Environmental Data Section Archive, https://meds-sdmm.dfo-mpo.gc.ca, Ecosystem and Oceans Science, Department of Fisheries and Oceans Canada. Data obtained on 2026/11/09.

This is a different product from the Canadian Hydrographic Service monthly Great Lakes water-level set already on Kaggle, and from the BC lightstation sea surface temperature and salinity set.

## Coverage

2,369,566 official observations across 12 stations were summarized into 109,111 daily rows and 3,901 monthly rows. The earliest observation in this extract is 1987-09-20 23:13:00 UTC and the latest is 2025-03-28 23:39:00 UTC. End dates differ by station; some official inventory end dates are earlier or later than the last row in the CSV zip.

The selected stations, with observation counts from the official CSVs, are: C46184 North Nomad (Pacific): 250,817 observations from 1987-09-20 to 2025-03-28; C46205 West Dixon Entrance (Pacific): 248,914 observations from 1988-11-22 to 2024-10-16; C46204 West Sea Otter (Pacific): 252,913 observations from 1989-09-07 to 2024-10-09; C46206 La Perouse Bank (Pacific): 237,882 observations from 1988-11-22 to 2022-04-17; C44139 Banquereau Bank (Atlantic): 191,904 observations from 1988-12-02 to 2022-12-14; C44137 East Scotian Slope (Atlantic): 218,147 observations from 1988-11-30 to 2022-12-20; C44258 Halifax Harbour (Atlantic): 140,739 observations from 2000-02-11 to 2022-11-24; C44141 Laurentian Fan (Atlantic): 170,503 observations from 1990-09-05 to 2017-01-05; C45132 Port Stanley (Great Lakes): 170,832 observations from 1989-09-08 to 2022-03-25; C45136 Slate Island (Great Lakes): 159,763 observations from 1989-09-30 to 2022-02-01; C45139 West Lake Ontario (Great Lakes): 163,290 observations from 1991-05-15 to 2022-03-24; C45137 Georgian Bay (Great Lakes): 163,862 observations from 1989-10-18 to 2021-07-08.

## Updates

This upload is a snapshot pulled on November 9, 2026 and is not refreshed on a schedule. For later observations, use the official MEDS download pages.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Wave height and period means and maxima do not use official rows with quality flag 4 (erroneous), do not use wave heights below 0 or above 30 metres, and do not use a VCAR value that differs from a present VWH$ value by more than 5 metres. The official CSVs often store 10000, and occasionally other very large numbers, in the VCAR column; those values are not real wave heights. A smaller number of official rows, including some flagged 1 (good), report a VCAR many metres away from the buoy-reported VWH$ on the same row; those VCAR values are also dropped. Of 2,369,566 official non-null VCAR values in this extract, 327,316 were excluded by that rule, including 70 that failed the VCAR to VWH$ comparison. `n_obs` still counts every official row. `n_vcar_used` and `n_vcar_excluded` show how many VCAR values entered the wave statistics. Wind, air temperature, sea surface temperature and pressure means use every official numeric value, because the quality flag is defined on the wave spectra rather than on those other sensors.

Longitudes in the official CSV are west-positive. In this extract they were converted to standard decimal degrees with west negative, which matches the sign used in the official inventory.

## A few numbers from this snapshot

* 2,369,566 official observations were summarized for 12 buoys.
* The highest annual maximum usable VCAR in this extract is 18.98 m at C46206 La Perouse Bank in 2018.
* Observation spans differ by station. See `stations.csv` for each first and last timestamp.

## Example uses

* Compare annual maximum significant wave height at the Pacific and Atlantic stations, using the usable VCAR column, and cross-check with `max_vwh_m`.
* Chart the seasonal cycle of monthly mean sea surface temperature at a Great Lakes station.
* Use `n_vcar_used` and the quality-flag counts when deciding whether to go back to the official hourly zip.

## Caveats

Buoy configuration, hull, sensors and even location can change while the same identifier stays in use. MEDS asks users to refer to the quality flag, the latitude and longitude columns, and the configuration spreadsheet compiled from buoy status reports. Some identifiers have more than one inventory deployment.

VCAR and VTPK were recomputed from spectra by MEDS for data posted before 2 April 2020. After that date only values reported by the buoy are provided. VWH$ and VCMX are buoy-reported. A day can have official rows but no usable VCAR if every height was a fill value, flag 4, or inconsistent with VWH$; those daily VCAR columns are then blank.

The 30 metre cap and the 5 metre VCAR to VWH$ tolerance are cleaning rules for this extract, not official MEDS limits. Flag 7 means the buoy may be off position; those rows can still contribute if the height passes the rules above. Early air temperature or other values can be unusual; inspect the official hourly file before relying on a single extreme.

## Licence

Contains information licensed under the [Open Government Licence Canada](https://open.canada.ca/en/open-government-licence-canada).

## Files

* `stations.csv`: the 12 selected buoys and links to the official hourly zips.
* `daily_wave_stats.csv`: daily means and maxima from the official hourly rows, with the wave-value rule above.
* `monthly_wave_stats.csv`: monthly means and maxima using the same rule.
* `annual_wave_stats.csv`: annual peaks and means from the daily table.
* `data_dictionary.csv`: column dictionary.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
