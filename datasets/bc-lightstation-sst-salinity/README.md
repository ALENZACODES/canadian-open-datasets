<p align="center"><img src="../../assets/theme-environment.png" alt="BC lightstation SST and salinity" width="100%"></p>

# BC lightstation SST and salinity

*Daily and monthly sea surface temperature and salinity, 1914 to 2026*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1914 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/bc-lightstation-sst-salinity](https://www.kaggle.com/datasets/johnnykhan1/bc-lightstation-sst-salinity)

## What it is

British Columbia shore station oceanographic observations of sea surface temperature and salinity, tidied from the Fisheries and Oceans Canada British Columbia Shore Station Oceanographic Program (BCSOP) open data package. English daily and monthly files for active sites were stacked into tidy CSVs. French duplicate files were not kept. Missing value sentinels at or above 900 were set to blank.

Source dataset: [British Columbia Lightstation Sea-Surface Temperature and Salinity Data (Pacific), 1914-present](https://open.canada.ca/data/en/dataset/719955f2-bf8e-44f7-bc26-6bd623e82884) (Fisheries and Oceans Canada).

Active sites zip and sites list pulled on November 9, 2026 from the Open Government Portal attachments.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`annual_site_means.csv`](data/annual_site_means.csv) | 39 KB | in this repository |
| [`cover.png`](data/cover.png) | 74 KB | in this repository |
| [`daily_sst_salinity.csv`](data/daily_sst_salinity.csv) | 10.0 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`monthly_sst_salinity_long.csv`](data/monthly_sst_salinity_long.csv) | 724 KB | in this repository |
| [`sites.csv`](data/sites.csv) | 5 KB | in this repository |

## Columns

### `annual_site_means.csv`

Annual means of valid daily temperature and salinity by site.

| Column | Type | Description |
|---|---|---|
| `site_folder` | Text | Folder name used in the active sites download zip (underscore form). |
| `site_name` | Text | Lightstation or sample site name as published by Fisheries and Oceans Canada. |
| `year` | Integer | Calendar year. |
| `n_temperature` | Integer | Count of daily temperature readings used in the annual mean. |
| `mean_temperature_c` | Float | Mean of valid daily sea surface temperatures for the site and year. |
| `n_salinity` | Integer | Count of daily salinity readings used in the annual mean. |
| `mean_salinity_pss` | Float | Mean of valid daily sea surface salinities for the site and year. |
| `latitude` | Float | Approximate site latitude in decimal degrees. |
| `longitude` | Text | Approximate site longitude in decimal degrees. |

### `daily_sst_salinity.csv`

Daily sea surface temperature and salinity for active sites in the November 2026 active sites zip.

| Column | Type | Description |
|---|---|---|
| `site_folder` | Text | Folder name used in the active sites download zip (underscore form). |
| `site_name` | Text | Lightstation or sample site name as published by Fisheries and Oceans Canada. |
| `observation_date` | Date | Calendar date of the daily bucket sample (YYYY-MM-DD). |
| `salinity_pss` | Float | Sea surface practical salinity (PSS). DFO missing sentinels at or above 900 were set to blank. |
| `temperature_c` | Float | Sea surface temperature in degrees Celsius. DFO missing sentinels at or above 900 were set to blank. |
| `latitude` | Text | Approximate site latitude in decimal degrees. |
| `longitude` | Text | Approximate site longitude in decimal degrees. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, number or integer). |
| `description` | Text | What the column contains. |

### `monthly_sst_salinity_long.csv`

Average monthly sea surface temperature and salinity in long form for active sites.

| Column | Type | Description |
|---|---|---|
| `site_folder` | Text | Folder name used in the active sites download zip (underscore form). |
| `site_name` | Text | Lightstation or sample site name as published by Fisheries and Oceans Canada. |
| `year` | Integer | Calendar year. |
| `month` | Integer | Calendar month number from 1 to 12. |
| `month_name` | Text | Three letter English month name. |
| `variable` | Text | Which monthly series the value comes from: temperature_c or salinity_pss. |
| `value` | Float | Monthly average value for the named variable. Missing months are blank. |

### `sites.csv`

BC lightstations and other sample sites with status and approximate coordinates.

| Column | Type | Description |
|---|---|---|
| `site_name` | Text | Lightstation or sample site name as published by Fisheries and Oceans Canada. |
| `status` | Text | Data collection status from the sites list: ACTIVE, IN-ACTIVE or ARCHIVED. |
| `temporal_extent` | Text | Published year range for the site (for example 1934 - PRESENT). |
| `latitude` | Text | Approximate site latitude in decimal degrees. |
| `longitude` | Text | Approximate site longitude in decimal degrees. |
| `comments` | Text | Free text monitoring note from the sites list. |

## Source and licence

**Source:** Fisheries and Oceans Canada, British Columbia Shore Station Oceanographic Program, British Columbia Lightstation Sea-Surface Temperature and Salinity Data, https://open.canada.ca/data/en/dataset/719955f2-bf8e-44f7-bc26-6bd623e82884. Active sites zip and sites CSV downloaded on November 9, 2026. Prepared by John Khan in Toronto, Ontario. Contains information licensed under the Open Government Licence Canada, https://open.canada.ca/en/open-government-licence-canada.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026bclightstationsstsalinity,
  author    = {Khan, John},
  title     = {BC lightstation SST and salinity},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/bc-lightstation-sst-salinity}
}
```

APA: Khan, J. (2026). *BC lightstation SST and salinity* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/bc-lightstation-sst-salinity

<details><summary>Full notes from the Kaggle page</summary>

## What this is

British Columbia shore station oceanographic observations of sea surface temperature and salinity, tidied from the Fisheries and Oceans Canada British Columbia Shore Station Oceanographic Program (BCSOP) open data package. English daily and monthly files for active sites were stacked into tidy CSVs. French duplicate files were not kept. Missing value sentinels at or above 900 were set to blank.

Source dataset: [British Columbia Lightstation Sea-Surface Temperature and Salinity Data (Pacific), 1914-present](https://open.canada.ca/data/en/dataset/719955f2-bf8e-44f7-bc26-6bd623e82884) (Fisheries and Oceans Canada).

Active sites zip and sites list pulled on November 9, 2026 from the Open Government Portal attachments.

## Coverage

Sites list has 36 named locations (active, inactive and archived). This upload includes daily series for 5 active sites present in the November 2026 active sites zip, plus monthly series for those sites (Entrance Island has monthly files only in that zip). Daily rows: 143,694. Valid daily temperature readings: 131,806. Calendar years in the daily file: 1914 through 2026.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. DFO usually updates the package on a quarterly basis. For a later pull, download the Active Sites zip again from the Open Government Portal.

## A few numbers from this snapshot

* Departure Bay (PBS) has the longest daily record in this file, starting in 1914.
* Across Departure Bay years with at least 200 daily temperature readings, the warmest annual mean in this snapshot is 2015 at about 12.73 degrees Celsius.
* Observations are bucket samples taken at or near daytime high tide, which introduces a tidal cycle signal in the daily series.

## Example uses

* Chart long term sea surface temperature at Departure Bay or other active sites.
* Compare salinity and temperature seasonality across sites.
* Join site coordinates to coastal maps for Pacific shore station studies.

## Caveats

Coordinates in the sites list are approximate. Daily sampling at daytime high tide creates a roughly 14 day artifact in the daily temperature series. Monthly averages are less affected. Values of 999.9 or 999.99 in the source mean missing and were blanked here. Not every active site in the sites list has a daily file in the November 2026 zip (Entrance Island is monthly only in that package).

## Files

* `sites.csv`: BC lightstations and other sample sites with status and approximate coordinates.
* `daily_sst_salinity.csv`: Daily sea surface temperature and salinity for active sites in the November 2026 active sites zip.
* `monthly_sst_salinity_long.csv`: Average monthly sea surface temperature and salinity in long form for active sites.
* `annual_site_means.csv`: Annual means of valid daily temperature and salinity by site.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Fisheries and Oceans Canada, British Columbia Shore Station Oceanographic Program, BC lightstation sea surface temperature and salinity. The published values were not changed except that missing sentinels were blanked and files were stacked and renamed. This is not an official Government of Canada product and Fisheries and Oceans Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
