<p align="center"><img src="../../assets/theme-environment.png" alt="Canada NAPS annual air quality" width="100%"></p>

# Canada NAPS annual air quality

*Monthly and annual pollutant means at NAPS stations, 2016 to 2024*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1 January 1974 to 1 December 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-naps-air-quality-annual](https://www.kaggle.com/datasets/johnnykhan1/canada-naps-air-quality-annual)

## What it is

Annual and monthly mean concentrations from Environment and Climate Change Canada's National Air Pollution Surveillance (NAPS) program, stacked from the official English means files for 2016 through 2024. A tidy monthly long file and the official station list are included.

Source dataset: [National Air Pollution Surveillance (NAPS) Program](https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b) (Environment and Climate Change Canada).

Means files and the station list were pulled on November 9, 2026 from the ECCC Data Catalogue at https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 79 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 6 KB | in this repository |
| [`monthly_means_long.csv`](data/monthly_means_long.csv) | 14.6 MB | in this repository |
| [`station_year_pollutant_means.csv`](data/station_year_pollutant_means.csv) | 1.6 MB | in this repository |
| [`stations.csv`](data/stations.csv) | 145 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `monthly_means_long.csv`

Tidy long file of monthly means with the annual statistics repeated on each month row.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the NAPS annual means file. |
| `naps_id` | Text | NAPS station identifier, zero padded to six digits. |
| `city` | Text | City name as published in the means file or station list. |
| `location` | Text | Street or site location as published in the means file. |
| `latitude` | Text | Station latitude in decimal degrees. |
| `longitude` | Text | Station longitude in decimal degrees. |
| `elevation_m` | Float | Station elevation in metres. |
| `pollutant` | Text | Pollutant code: CO, NO, NO2, NOX, O3, PM2.5, PM10 or SO2. |
| `unit` | Text | Concentration unit: ppb for SO2, NO2, O3, NO and NOx; ppm for CO; ug/m3 for PM2.5 and PM10. |
| `annual_mean` | Float | Annual mean concentration when reporting criteria are met. Blank when not reported. |
| `annual_std` | Float | Standard deviation of the annual hourly values when reported. |
| `percent_complete` | Integer | Percent of hours in the year with valid measurements, as published. |
| `month` | Text | Month name for the monthly mean. |
| `monthly_mean` | Float | Monthly mean concentration when at least 50 percent of hours in the month are valid. Blank when not reported. |
| `month_num` | Integer | Month number from 1 (January) to 12 (December). |

### `station_year_pollutant_means.csv`

Monthly and annual mean concentrations by station, pollutant and year, 2016 to 2024.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the NAPS annual means file. |
| `naps_id` | Text | NAPS station identifier, zero padded to six digits. |
| `city` | Text | City name as published in the means file or station list. |
| `location` | Text | Street or site location as published in the means file. |
| `latitude` | Text | Station latitude in decimal degrees. |
| `longitude` | Text | Station longitude in decimal degrees. |
| `elevation_m` | Float | Station elevation in metres. |
| `pollutant` | Text | Pollutant code: CO, NO, NO2, NOX, O3, PM2.5, PM10 or SO2. |
| `unit` | Text | Concentration unit: ppb for SO2, NO2, O3, NO and NOx; ppm for CO; ug/m3 for PM2.5 and PM10. |
| `January` | Float | Mean January concentration when reporting criteria are met. |
| `February` | Float | Mean February concentration when reporting criteria are met. |
| `March` | Float | Mean March concentration when reporting criteria are met. |
| `April` | Float | Mean April concentration when reporting criteria are met. |
| `May` | Float | Mean May concentration when reporting criteria are met. |
| `June` | Float | Mean June concentration when reporting criteria are met. |
| `July` | Float | Mean July concentration when reporting criteria are met. |
| `August` | Text | Mean August concentration when reporting criteria are met. |
| `September` | Float | Mean September concentration when reporting criteria are met. |
| `October` | Float | Mean October concentration when reporting criteria are met. |
| `November` | Float | Mean November concentration when reporting criteria are met. |
| `December` | Float | Mean December concentration when reporting criteria are met. |
| `annual_mean` | Float | Annual mean concentration when reporting criteria are met. Blank when not reported. |
| `annual_std` | Float | Standard deviation of the annual hourly values when reported. |
| `percent_complete` | Integer | Percent of hours in the year with valid measurements, as published. |

### `stations.csv`

NAPS station list (English fields) from the official 2024 station file.

| Column | Type | Description |
|---|---|---|
| `naps_id` | Text | NAPS station identifier, zero padded to six digits. |
| `station_name` | Text | Station name from the NAPS station list. |
| `status_code` | Integer | Status code as published in the NAPS station list. |
| `location_address` | Text | Station address from the NAPS station list. |
| `city` | Text | City name as published in the means file or station list. |
| `province_or_territory` | Text | English province or territory name. |
| `postal_code` | Text | Postal code when published. |
| `timezone_utc_offset` | Float | Timezone offset from UTC as published. |
| `latitude` | Text | Station latitude in decimal degrees. |
| `longitude` | Text | Station longitude in decimal degrees. |
| `elevation_m` | Float | Station elevation in metres. |
| `start_date` | Date | Station start date from the NAPS station list (YYYY-MM-DD). |
| `end_date` | Date | Station end date when published. Blank for stations with no end date in the list. |
| `network` | Text | Monitoring network code as published. |
| `site_type` | Text | Site type code as published. |
| `urbanization` | Text | Urbanization class as published. |
| `neighbourhood` | Text | Neighbourhood class as published. |
| `land_use` | Text | Land use class as published. |
| `scale` | Text | Spatial scale code as published. |
| `cma_or_ca` | Text | Census metropolitan area or agglomeration as published. |
| `aqms_airzone` | Text | Air Quality Management System air zone as published. |

## Source and licence

**Source:** Environment and Climate Change Canada, National Air Pollution Surveillance (NAPS) Program, https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b. Annual means files 2016 to 2024 and StationsNAPS-StationsSNPA.csv downloaded on November 9, 2026 from https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/. Prepared by John Khan in Toronto, Ontario. Contains information licensed under the Open Government Licence – Canada, https://open.canada.ca/en/open-government-licence-canada.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadanapsairqualityannual,
  author    = {Khan, John},
  title     = {Canada NAPS annual air quality},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-naps-air-quality-annual}
}
```

APA: Khan, J. (2026). *Canada NAPS annual air quality* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-naps-air-quality-annual

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Annual and monthly mean concentrations from Environment and Climate Change Canada's National Air Pollution Surveillance (NAPS) program, stacked from the official English means files for 2016 through 2024. A tidy monthly long file and the official station list are included.

Source dataset: [National Air Pollution Surveillance (NAPS) Program](https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b) (Environment and Climate Change Canada).

Means files and the station list were pulled on November 9, 2026 from the ECCC Data Catalogue at https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/

## Coverage

11,629 station, year and pollutant rows from 9 years (2016 to 2024). 338 distinct NAPS identifiers appear in the means tables. Pollutants are carbon monoxide (CO, ppm), nitric oxide (NO, ppb), nitrogen dioxide (NO2, ppb), nitrogen oxides (NOx, ppb), ozone (O3, ppb), sulphur dioxide (SO2, ppb), PM2.5 and PM10 (micrograms per cubic metre). Monthly averages are reported when at least 50 percent of hours in the month are valid. Annual averages and standard deviations are reported when 50 percent of hours in the year are valid and each quarter has at least two valid months, as stated in the source files.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. NAPS continuous annual summaries are posted after the year is quality assured. For later years or hourly values, use the ECCC Data Catalogue or the NAPS data query tool.

## A few numbers from this snapshot

* 11,629 station year pollutant rows are in the main means file.
* 338 NAPS identifiers appear in those tables.
* Among Toronto stations in this file, the unweighted mean of published annual PM2.5 values is 9.4 micrograms per cubic metre in 2023 and 7.0 in 2024.

## Example uses

* Track annual PM2.5 or NO2 at a chosen city.
* Compare summer ozone across stations.
* Join the station list to map monitors by land use or air zone.

## Caveats

This is the official means summary, not the full hourly archive. A blank month or annual value means the reporting rule was not met or the pollutant was not measured at that station year. City curves on the cover are unweighted means of the stations whose city name contains Toronto or Vancouver; they are not official city composites. The station list is the 2024 NAPS list and may include stations that do not appear in every means year. Hourly values are reported in standard local time with no adjustment for daylight saving, as described by NAPS. This is not an official Government of Canada product and Environment and Climate Change Canada does not endorse it.

## Files

* `stations.csv`: NAPS station list (English fields) from the official 2024 station file.
* `station_year_pollutant_means.csv`: Monthly and annual mean concentrations by station, pollutant and year, 2016 to 2024.
* `monthly_means_long.csv`: Tidy long file of monthly means with the annual statistics repeated on each month row.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, National Air Pollution Surveillance (NAPS) Program. The published values were not changed. Columns were renamed and the yearly files were stacked. Environment and Climate Change Canada does not endorse this upload.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
