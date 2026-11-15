<p align="center"><img src="../../assets/theme-environment.png" alt="Canada climate normals 1981 to 2010" width="100%"></p>

# Canada climate normals 1981 to 2010

*Selected city stations: temperature and precipitation normals*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1981 to 2010 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-climate-normals-1981-2010](https://www.kaggle.com/datasets/johnnykhan1/canada-climate-normals-1981-2010)

## What it is

Selected Canadian Climate Normals for 1981 to 2010 from Environment and Climate Change Canada, tidied into long and summary CSVs. Station files for major airports and capital cities were stacked. Degree symbols in the source were kept as published element names.

Source dataset: [Climate Normals 1981-2010](https://open.canada.ca/data/en/dataset/746f9469-ab78-5dcc-b165-4b51e8ab8652) (Environment and Climate Change Canada).

Station CSVs pulled on November 9, 2026 from https://dd.weather.gc.ca/today/climate/observations/normals/csv/1981-2010/

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`climate_normals_long.csv`](data/climate_normals_long.csv) | 3.0 MB | in this repository |
| [`cover.png`](data/cover.png) | 71 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 4 KB | in this repository |
| [`monthly_mean_temp_c.csv`](data/monthly_mean_temp_c.csv) | 2 KB | in this repository |
| [`station_annual_means.csv`](data/station_annual_means.csv) | 2 KB | in this repository |
| [`stations.csv`](data/stations.csv) | 2 KB | in this repository |

## Columns

### `climate_normals_long.csv`

Tidy long file of 1981 to 2010 climate normals elements by month.

| Column | Type | Description |
|---|---|---|
| `station_name` | Text | Climate station name as published (asterisk for WMO temperature and precipitation standards was removed from the tidy files). |
| `province` | Text | Two letter province or territory code. |
| `climate_id` | Text | ECCC climate identifier. |
| `wmo_id` | Text | World Meteorological Organization station id when published. |
| `tc_id` | Text | Transport Canada station id when published. |
| `latitude` | Text | Station latitude in decimal degrees. |
| `longitude` | Text | Station longitude in decimal degrees. |
| `elevation_m` | Float | Station elevation in metres. |
| `section` | Text | Section heading from the normals file (for example Temperature or Precipitation). |
| `element` | Text | Climate element name as published (for example Daily Average (C)). |
| `month` | Text | Month name or Year for the annual value. |
| `month_num` | Integer | Month number 1 to 12, or 0 for the Year column. |
| `value` | Float | Normals value for that element and month. Blank when missing in the source. |
| `data_code` | Text | Normals completeness code A, B, C or D as published. |

### `data_dictionary.csv`

- `column`: Name of the column being described - `file`: File that contains the column - `type`: Data type of the column - `description`: Plain-language description of the column

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `monthly_mean_temp_c.csv`

Monthly mean daily average temperature by station.

| Column | Type | Description |
|---|---|---|
| `climate_id` | Text | ECCC climate identifier. |
| `station_name` | Text | Climate station name as published (asterisk for WMO temperature and precipitation standards was removed from the tidy files). |
| `province` | Text | Two letter province or territory code. |
| `Jan` | Float | Mean daily average temperature in degrees Celsius for Jan. |
| `Feb` | Float | Mean daily average temperature in degrees Celsius for Feb. |
| `Mar` | Float | Mean daily average temperature in degrees Celsius for Mar. |
| `Apr` | Float | Mean daily average temperature in degrees Celsius for Apr. |
| `May` | Float | Mean daily average temperature in degrees Celsius for May. |
| `Jun` | Float | Mean daily average temperature in degrees Celsius for Jun. |
| `Jul` | Float | Mean daily average temperature in degrees Celsius for Jul. |
| `Aug` | Float | Mean daily average temperature in degrees Celsius for Aug. |
| `Sep` | Float | Mean daily average temperature in degrees Celsius for Sep. |
| `Oct` | Float | Mean daily average temperature in degrees Celsius for Oct. |
| `Nov` | Float | Mean daily average temperature in degrees Celsius for Nov. |
| `Dec` | Float | Mean daily average temperature in degrees Celsius for Dec. |

### `station_annual_means.csv`

Annual mean temperature and precipitation for each selected station.

| Column | Type | Description |
|---|---|---|
| `climate_id` | Text | ECCC climate identifier. |
| `station_name` | Text | Climate station name as published (asterisk for WMO temperature and precipitation standards was removed from the tidy files). |
| `province` | Text | Two letter province or territory code. |
| `wmo_id` | Text | World Meteorological Organization station id when published. |
| `tc_id` | Text | Transport Canada station id when published. |
| `latitude` | Text | Station latitude in decimal degrees. |
| `longitude` | Text | Station longitude in decimal degrees. |
| `elevation_m` | Float | Station elevation in metres. |
| `mean_daily_temp_c` | Float | Annual mean of daily average temperature in degrees Celsius for 1981 to 2010. |
| `mean_annual_precip_mm` | Float | Mean annual precipitation in millimetres for 1981 to 2010. |

### `stations.csv`

Selected Canadian climate stations in this snapshot.

| Column | Type | Description |
|---|---|---|
| `climate_id` | Text | ECCC climate identifier. |
| `station_name` | Text | Climate station name as published (asterisk for WMO temperature and precipitation standards was removed from the tidy files). |
| `province` | Text | Two letter province or territory code. |
| `wmo_id` | Text | World Meteorological Organization station id when published. |
| `tc_id` | Text | Transport Canada station id when published. |
| `latitude` | Text | Station latitude in decimal degrees. |
| `longitude` | Text | Station longitude in decimal degrees. |
| `elevation_m` | Float | Station elevation in metres. |

## Source and licence

**Source:** Environment and Climate Change Canada, Climate Normals 1981-2010, via open.canada.ca, Open Government Licence Canada

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaclimatenormals19812010,
  author    = {Khan, John},
  title     = {Canada climate normals 1981 to 2010},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-climate-normals-1981-2010}
}
```

APA: Khan, J. (2026). *Canada climate normals 1981 to 2010* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-climate-normals-1981-2010

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Selected Canadian Climate Normals for 1981 to 2010 from Environment and Climate Change Canada, tidied into long and summary CSVs. Station files for major airports and capital cities were stacked. Degree symbols in the source were kept as published element names.

Source dataset: [Climate Normals 1981-2010](https://open.canada.ca/data/en/dataset/746f9469-ab78-5dcc-b165-4b51e8ab8652) (Environment and Climate Change Canada).

Station CSVs pulled on November 9, 2026 from https://dd.weather.gc.ca/today/climate/observations/normals/csv/1981-2010/

## Coverage

19 selected stations across the provinces and territories, including Toronto, Vancouver, Calgary, Montreal, Winnipeg, Halifax, Ottawa, Edmonton, Regina, Saskatoon, Quebec City, Victoria, Moncton, St. John's, Charlottetown, Yellowknife and Whitehorse. Elements include temperature, precipitation and other published normals fields. Period: 1981 through 2010.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. Climate normals are updated by decade. For the 1991 to 2020 normals, use the Canadian Climate Normals pages on climate.weather.gc.ca.

## A few numbers from this snapshot

* 19 stations are included.
* Among these stations, the warmest annual mean daily average temperature is VANCOUVER INT'L A at 10.4 degrees Celsius.
* Completeness codes A to D follow the published WMO style rules in each source file.

## Example uses

* Compare monthly temperature curves across cities.
* Map annual precipitation by station.
* Join to other city level series for climate context.

## Caveats

This is a selected station subset, not the full national normals archive. Station names that met WMO temperature and precipitation standards had a leading asterisk in the source; that mark was removed in the tidy files. Missing months stay blank. Normals are 30 year averages, not a year by year series.

## Files

* `stations.csv`: Selected Canadian climate stations in this snapshot.
* `climate_normals_long.csv`: Tidy long file of 1981 to 2010 climate normals elements by month.
* `station_annual_means.csv`: Annual mean temperature and precipitation for each selected station.
* `monthly_mean_temp_c.csv`: Monthly mean daily average temperature by station.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, Climate Normals 1981 to 2010. The published values were not changed. Columns were rearranged into tidy tables. This is not an official Government of Canada product and Environment and Climate Change Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
