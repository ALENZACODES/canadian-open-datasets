<p align="center"><img src="../../assets/theme-environment.png" alt="Canada AHCCD temperature and precipitation" width="100%"></p>

# Canada AHCCD temperature and precipitation

*Station annual series from official homogenized daily data*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1840 to 2023 (precipitation to December 2017) · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-ahccd-temp-precipitation](https://www.kaggle.com/datasets/johnnykhan1/canada-ahccd-temp-precipitation)

## What it is

Station annual temperature and precipitation series prepared from official Adjusted and Homogenized Canadian Climate Data daily files. Third-generation homogenized temperature, update to 2023, and second-generation adjusted precipitation, updated to December 2017, are stored in separate files, with official station IDs, metadata, generation and end-year columns, and official joined-station flags. Annual values are computed only when official non-missing daily values cover at least 80% of the days in the year. No anomaly series is included.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 3 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 3 KB | in this repository |
| [`annual_max_temperature_gen3_2023.csv`](data/annual_max_temperature_gen3_2023.csv) | 30.5 MB | in this repository |
| [`annual_mean_temperature_gen3_2023.csv`](data/annual_mean_temperature_gen3_2023.csv) | 30.5 MB | in this repository |
| [`annual_min_temperature_gen3_2023.csv`](data/annual_min_temperature_gen3_2023.csv) | 30.7 MB | in this repository |
| [`annual_total_precipitation_v2017.csv`](data/annual_total_precipitation_v2017.csv) | 20.7 MB | in this repository |
| [`cover.png`](data/cover.png) | 99 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 21 KB | in this repository |
| [`example_official_daily_mean_temp_1012010.csv`](data/example_official_daily_mean_temp_1012010.csv) | 762 KB | in this repository |
| [`precipitation_stations_v2017.csv`](data/precipitation_stations_v2017.csv) | 73 KB | in this repository |
| [`temperature_stations_gen3_2023.csv`](data/temperature_stations_gen3_2023.csv) | 117 KB | in this repository |

## Columns

### `SOURCE_MANIFEST.csv`

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | — |
| `title` | Text | — |
| `url` | Text | — |
| `licence` | Text | — |
| `release_date` | Text | — |
| `retrieval_date` | Date | — |
| `file_name` | Text | — |
| `checksum_sha256` | Text | — |
| `notes` | Text | — |

### `annual_max_temperature_gen3_2023.csv`

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | Official AHCCD station identifier. |
| `station_name_header` | Text | Station name as printed in the official daily file header. |
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |
| `year` | Integer | Calendar year of the adapted annual value, or of an official daily example row. |
| `variable` | Text | Official climate variable, as described in the daily file header. |
| `unit` | Text | Official unit: degrees Celsius for temperature, millimetres for precipitation. |
| `value` | Float | For annual files, the adapted annual mean or total, only when the completeness rule is met. For the example daily file, the official daily value. |
| `annual_statistic` | Text | mean of official daily values for temperature, or sum of official daily values for precipitation. |
| `n_valid_days` | Integer | Number of official non-missing daily values in the calendar year. |
| `n_calendar_days` | Integer | Number of calendar days in the year, 365 or 366. |
| `n_missing_days` | Integer | n_calendar_days minus n_valid_days. |
| `completeness_ratio` | Float | n_valid_days divided by n_calendar_days. |
| `completeness_threshold` | Float | 0.80. This threshold is stated here and is not an official AHCCD cutoff. |
| `completeness_met` | Boolean | True when completeness_ratio is at least 0.80. Annual values are computed only in those years. |
| `completeness_rule` | Text | The completeness rule used for the adapted annual value. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `station_joined` | Boolean | Whether the official daily header describes the station as joined or not joined. |
| `joined_status` | Text | Official joined wording from the daily file header. |
| `updated_statement` | Text | Official update statement from the daily file header. |
| `product_zip` | Text | Official bulk zip file name. |
| `source_file` | Text | Official station daily file name inside the zip. |

### `annual_mean_temperature_gen3_2023.csv`

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | Official AHCCD station identifier. |
| `station_name_header` | Text | Station name as printed in the official daily file header. |
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |
| `year` | Integer | Calendar year of the adapted annual value, or of an official daily example row. |
| `variable` | Text | Official climate variable, as described in the daily file header. |
| `unit` | Text | Official unit: degrees Celsius for temperature, millimetres for precipitation. |
| `value` | Float | For annual files, the adapted annual mean or total, only when the completeness rule is met. For the example daily file, the official daily value. |
| `annual_statistic` | Text | mean of official daily values for temperature, or sum of official daily values for precipitation. |
| `n_valid_days` | Integer | Number of official non-missing daily values in the calendar year. |
| `n_calendar_days` | Integer | Number of calendar days in the year, 365 or 366. |
| `n_missing_days` | Integer | n_calendar_days minus n_valid_days. |
| `completeness_ratio` | Float | n_valid_days divided by n_calendar_days. |
| `completeness_threshold` | Float | 0.80. This threshold is stated here and is not an official AHCCD cutoff. |
| `completeness_met` | Boolean | True when completeness_ratio is at least 0.80. Annual values are computed only in those years. |
| `completeness_rule` | Text | The completeness rule used for the adapted annual value. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `station_joined` | Boolean | Whether the official daily header describes the station as joined or not joined. |
| `joined_status` | Text | Official joined wording from the daily file header. |
| `updated_statement` | Text | Official update statement from the daily file header. |
| `product_zip` | Text | Official bulk zip file name. |
| `source_file` | Text | Official station daily file name inside the zip. |

### `annual_min_temperature_gen3_2023.csv`

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | Official AHCCD station identifier. |
| `station_name_header` | Text | Station name as printed in the official daily file header. |
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |
| `year` | Integer | Calendar year of the adapted annual value, or of an official daily example row. |
| `variable` | Text | Official climate variable, as described in the daily file header. |
| `unit` | Text | Official unit: degrees Celsius for temperature, millimetres for precipitation. |
| `value` | Float | For annual files, the adapted annual mean or total, only when the completeness rule is met. For the example daily file, the official daily value. |
| `annual_statistic` | Text | mean of official daily values for temperature, or sum of official daily values for precipitation. |
| `n_valid_days` | Integer | Number of official non-missing daily values in the calendar year. |
| `n_calendar_days` | Integer | Number of calendar days in the year, 365 or 366. |
| `n_missing_days` | Integer | n_calendar_days minus n_valid_days. |
| `completeness_ratio` | Float | n_valid_days divided by n_calendar_days. |
| `completeness_threshold` | Float | 0.80. This threshold is stated here and is not an official AHCCD cutoff. |
| `completeness_met` | Boolean | True when completeness_ratio is at least 0.80. Annual values are computed only in those years. |
| `completeness_rule` | Text | The completeness rule used for the adapted annual value. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `station_joined` | Boolean | Whether the official daily header describes the station as joined or not joined. |
| `joined_status` | Text | Official joined wording from the daily file header. |
| `updated_statement` | Text | Official update statement from the daily file header. |
| `product_zip` | Text | Official bulk zip file name. |
| `source_file` | Text | Official station daily file name inside the zip. |

### `annual_total_precipitation_v2017.csv`

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | Official AHCCD station identifier. |
| `station_name_header` | Text | Station name as printed in the official daily file header. |
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |
| `year` | Integer | Calendar year of the adapted annual value, or of an official daily example row. |
| `variable` | Text | Official climate variable, as described in the daily file header. |
| `unit` | Text | Official unit: degrees Celsius for temperature, millimetres for precipitation. |
| `value` | Float | For annual files, the adapted annual mean or total, only when the completeness rule is met. For the example daily file, the official daily value. |
| `annual_statistic` | Text | mean of official daily values for temperature, or sum of official daily values for precipitation. |
| `n_valid_days` | Integer | Number of official non-missing daily values in the calendar year. |
| `n_calendar_days` | Integer | Number of calendar days in the year, 365 or 366. |
| `n_missing_days` | Integer | n_calendar_days minus n_valid_days. |
| `completeness_ratio` | Float | n_valid_days divided by n_calendar_days. |
| `completeness_threshold` | Float | 0.80. This threshold is stated here and is not an official AHCCD cutoff. |
| `completeness_met` | Boolean | True when completeness_ratio is at least 0.80. Annual values are computed only in those years. |
| `completeness_rule` | Text | The completeness rule used for the adapted annual value. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `station_joined` | Boolean | Whether the official daily header describes the station as joined or not joined. |
| `joined_status` | Text | Official joined wording from the daily file header. |
| `updated_statement` | Text | Official update statement from the daily file header. |
| `product_zip` | Text | Official bulk zip file name. |
| `source_file` | Text | Official station daily file name inside the zip. |

### `data_dictionary.csv`

| Column | Type | Description |
|---|---|---|
| `column` | Text | — |
| `file` | Text | — |
| `type` | Text | — |
| `description` | Text | — |

### `example_official_daily_mean_temp_1012010.csv`

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | Official AHCCD station identifier. |
| `date` | Date | Official daily date in the example file. |
| `year` | Integer | Calendar year of the adapted annual value, or of an official daily example row. |
| `month` | Integer | Month of an official daily example row. |
| `day` | Integer | Day of an official daily example row. |
| `value` | Float | For annual files, the adapted annual mean or total, only when the completeness rule is met. For the example daily file, the official daily value. |
| `observation_flag` | Text | Official daily flag character as published. Missing days typically have flag M. Flag meanings are not invented here. |
| `is_missing` | Boolean | True when the official daily value is the missing sentinel (about -9999.9) or has flag M. |
| `variable` | Text | Official climate variable, as described in the daily file header. |
| `unit` | Text | Official unit: degrees Celsius for temperature, millimetres for precipitation. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `product_zip` | Text | Official bulk zip file name. |
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |

### `precipitation_stations_v2017.csv`

| Column | Type | Description |
|---|---|---|
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `station_name` | Text | Official station name from the station list. |
| `station_id` | Text | Official AHCCD station identifier. |
| `period_from_year` | Integer | Official start year from the station list. |
| `period_from_month` | Integer | Official start month from the station list. |
| `period_to_year` | Integer | Official end year from the station list. |
| `period_to_month` | Integer | Official end month from the station list. |
| `latitude` | Text | Official latitude in degrees, from the station list. |
| `longitude` | Text | Official longitude in degrees, from the station list. |
| `elevation_m` | Integer | Official elevation in metres, from the station list. |
| `stations_joined_official` | Boolean | Official stns joined flag from the precipitation station list (Yes or No). |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `source_list` | Text | Official station list file name. |

### `temperature_stations_gen3_2023.csv`

| Column | Type | Description |
|---|---|---|
| `station_id` | Text | Official AHCCD station identifier. |
| `station_name` | Text | Official station name from the station list. |
| `province_code` | Text | Official province or territory code as published in the station list or daily header. |
| `period_from_year` | Integer | Official start year from the station list. |
| `period_from_month` | Integer | Official start month from the station list. |
| `period_to_year` | Integer | Official end year from the station list. |
| `period_to_month` | Integer | Official end month from the station list. |
| `percent_missing_official` | Float | Official percent missing from the temperature station list. |
| `latitude` | Text | Official latitude in degrees, from the station list. |
| `longitude` | Text | Official longitude in degrees, from the station list. |
| `elevation_m` | Integer | Official elevation in metres, from the station list. |
| `joined_official` | Boolean | Official Joined flag from the temperature station list (y or n). |
| `rcs_official` | Boolean | Official RCS flag from the temperature station list. |
| `iso3166_2` | Text | ISO 3166-2:CA code added from the official province or territory code. |
| `sgc` | Integer | Standard Geographic Classification province or territory code added from the official province or territory code. |
| `province_or_territory` | Text | Province or territory name corresponding to the official code. |
| `generation` | Text | third generation for the 2023 homogenized temperature product, or second generation for the 2017 adjusted precipitation product. |
| `product_vintage` | Integer | Official product vintage: 2023 for temperature, 2017 for precipitation. |
| `end_year` | Integer | Official update end year of the product: 2023 for temperature, 2017 for precipitation. |
| `source_list` | Text | Official station list file name. |

## Source and licence

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaahccdtempprecipitation,
  author    = {Khan, John},
  title     = {Canada AHCCD temperature and precipitation},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-ahccd-temp-precipitation}
}
```

APA: Khan, J. (2026). *Canada AHCCD temperature and precipitation* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ahccd-temp-precipitation

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Station annual temperature and precipitation series prepared from official Adjusted and Homogenized Canadian Climate Data daily files. Third-generation homogenized temperature, update to 2023, and second-generation adjusted precipitation, updated to December 2017, are stored in separate files, with official station IDs, metadata, generation and end-year columns, and official joined-station flags. Annual values are computed only when official non-missing daily values cover at least 80% of the days in the year. No anomaly series is included.

## Coverage

Temperature stations from the official 2023 third-generation list, with daily records ending in 2023 as published. Precipitation stations from the official list updated to December 2017. Canada-wide station network, not 30-year climate normals.

## Updates

This upload is a snapshot downloaded on 15 November 2026 from https://crd-data-donnees-rdc.ec.gc.ca/CDAS/products/EC_data/AHCCD_daily/. The official temperature product is an update to 2023. The official precipitation product is updated to December 2017.

## A few numbers from this snapshot

* The temperature product is the official third-generation homogenized daily temperature for Canada, update to 2023: 780 mean-temperature stations, 780 maximum, and 780 minimum, matching the official station list of 780 stations.
* The precipitation product is official second-generation adjusted daily total precipitation, updated to December 2017: 463 official station files and 463 official station-list rows.
* On 1 October 1913, the official homogenized daily mean temperature at station 1012010, Cowichan Bay Cherry, British Columbia, was 10.2 degrees Celsius, as published in the official daily file.
* Annual files are adapted from those official daily values. An annual temperature mean or precipitation total is computed only when official non-missing daily values cover at least 80% of the calendar days in the year. Years that do not meet that rule are kept with a blank value and completeness_met set to false. No anomaly series is included.
* Temperature and precipitation come from different generations and end years (2023 and 2017). They are stored in separate files and should not be treated as one vintage.

## Example uses

* Use official station metadata, IDs and joined flags with the annual files.
* Filter to years where completeness_met is true before computing trends from the annual series.
* Keep the 2023 temperature vintage and the 2017 precipitation vintage separate.

## Caveats

Annual values are adapted from official daily data using the stated 80% completeness rule; they are not a separately published official annual AHCCD table. Temperature and precipitation are different generations and end years. Joined stations are official composite records. No anomaly series is included.

## Files

* `annual_mean_temperature_gen3_2023.csv`: Adapted annual mean of official third-generation homogenized daily mean temperature, 2023 vintage. An annual value is computed only when at least 80% of calendar days in the year have an official non-missing daily value.
* `annual_max_temperature_gen3_2023.csv`: Adapted annual mean of official third-generation homogenized daily maximum temperature, 2023 vintage, with the same 80% completeness rule.
* `annual_min_temperature_gen3_2023.csv`: Adapted annual mean of official third-generation homogenized daily minimum temperature, 2023 vintage, with the same 80% completeness rule.
* `annual_total_precipitation_v2017.csv`: Adapted annual total of official second-generation adjusted daily total precipitation, 2017 vintage, with the same 80% completeness rule.
* `temperature_stations_gen3_2023.csv`: Official third-generation homogenized temperature station list, update to 2023, with station IDs, coordinates, official period, official percent missing, joined and RCS flags, and ISO 3166-2:CA codes.
* `precipitation_stations_v2017.csv`: Official adjusted precipitation station list, updated to December 2017, with station IDs, coordinates, official period, joined flag, and ISO 3166-2:CA codes.
* `example_official_daily_mean_temp_1012010.csv`: Official homogenized daily mean temperature for station 1012010, Cowichan Bay Cherry, British Columbia, kept so the official 10.2 degrees Celsius value on 1 October 1913 can be reproduced.
* `SOURCE_MANIFEST.csv`: Official zip and station-list identifiers, retrieval date and checksums.
* `data_dictionary.csv`: Column dictionary.
* `METHODS.md`: Methods note, including homogenisation notes and the completeness rule.
* `CITATION.txt`: Suggested citation, with DOI pending.

## Licence

This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, Adjusted and Homogenized Canadian Climate Data (AHCCD). This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.

Suggested citation: John Khan. 2026. Canada AHCCD temperature and precipitation [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ahccd-temp-precipitation. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
