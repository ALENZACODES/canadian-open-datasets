<p align="center"><img src="../../assets/theme-public-safety.png" alt="Toronto Neighbourhood Crime Rates 2014 to 2025" width="100%"></p>

# Toronto Neighbourhood Crime Rates 2014 to 2025

*Annual counts and rates for 158 neighbourhoods, tidy and wide*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 2014 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-crime-rates-2014-2025](https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-crime-rates-2014-2025)

## What it is

Annual crime counts and rates for Toronto's 158 social planning neighbourhoods, 2014 to 2025. Offences are assault, auto theft, bike theft, break and enter, homicide, robbery, shooting and firearm discharges, theft from a motor vehicle, and theft over $5,000. Rates are per 100,000 people as published by the Toronto Police Service.

The official table is wide, with one column per offence and year. This version is reshaped to a tidy long file, plus a compact wide file with one row per neighbourhood and year. I also recover an implied population for each neighbourhood and year from the published count and rate, because the source table only lists a 2025 population estimate.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 76 KB | in this repository |
| [`crime_rates_by_neighbourhood_year.csv`](data/crime_rates_by_neighbourhood_year.csv) | 300 KB | in this repository |
| [`crime_rates_citywide_by_year.csv`](data/crime_rates_citywide_by_year.csv) | 6 KB | in this repository |
| [`crime_rates_long.csv`](data/crime_rates_long.csv) | 1.8 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 6 KB | in this repository |
| [`implied_population_by_neighbourhood_year.csv`](data/implied_population_by_neighbourhood_year.csv) | 62 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |

## Columns

### `crime_rates_by_neighbourhood_year.csv`

Wide table: one row per neighbourhood and year, with a count and rate column for each offence.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | City of Toronto social planning neighbourhood number (158-neighbourhood model), zero padded to three digits. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither, from the City neighbourhoods file. |
| `year` | Integer | Calendar year of the count and rate. |
| `population_2025` | Integer | 2025 population estimate published on the source table (same value on every year of that neighbourhood). |
| `assault_count` | Integer | Count of assault occurrences in this neighbourhood and year. |
| `autotheft_count` | Integer | Count of auto theft occurrences in this neighbourhood and year. |
| `biketheft_count` | Integer | Count of bike theft occurrences in this neighbourhood and year. |
| `breakenter_count` | Integer | Count of break and enter occurrences in this neighbourhood and year. |
| `homicide_count` | Integer | Count of homicide occurrences in this neighbourhood and year. |
| `robbery_count` | Integer | Count of robbery occurrences in this neighbourhood and year. |
| `shooting_count` | Integer | Count of shooting and firearm discharges occurrences in this neighbourhood and year. |
| `theftfrommv_count` | Integer | Count of theft from motor vehicle occurrences in this neighbourhood and year. |
| `theftover_count` | Integer | Count of theft over $5,000 occurrences in this neighbourhood and year. |
| `assault_rate_per_100000` | Float | Assault rate per 100,000 population as published. |
| `autotheft_rate_per_100000` | Float | Auto theft rate per 100,000 population as published. |
| `biketheft_rate_per_100000` | Float | Bike theft rate per 100,000 population as published. |
| `breakenter_rate_per_100000` | Float | Break and enter rate per 100,000 population as published. |
| `homicide_rate_per_100000` | Float | Homicide rate per 100,000 population as published. |
| `robbery_rate_per_100000` | Float | Robbery rate per 100,000 population as published. |
| `shooting_rate_per_100000` | Float | Shooting and firearm discharges rate per 100,000 population as published. |
| `theftfrommv_rate_per_100000` | Float | Theft from motor vehicle rate per 100,000 population as published. |
| `theftover_rate_per_100000` | Float | Theft over $5,000 rate per 100,000 population as published. |

### `crime_rates_citywide_by_year.csv`

Citywide totals by year and offence, summed from the 158 neighbourhoods.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the count and rate. |
| `offence` | Text | Short offence code: assault, autotheft, biketheft, breakenter, homicide, robbery, shooting, theftfrommv, theftover. |
| `offence_label` | Text | Readable offence name. |
| `count` | Integer | Number of reported occurrences in that neighbourhood and year. |
| `neighbourhoods` | Integer | Number of neighbourhoods included in the sum. |
| `implied_city_population` | Integer | Sum of implied neighbourhood populations for that year. |
| `rate_per_100000` | Float | Rate per 100,000 population as published by the Toronto Police Service. |

### `crime_rates_long.csv`

Tidy long table: one row per neighbourhood, year and offence, with counts, rates and implied population.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | City of Toronto social planning neighbourhood number (158-neighbourhood model), zero padded to three digits. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither, from the City neighbourhoods file. |
| `year` | Integer | Calendar year of the count and rate. |
| `offence` | Text | Short offence code: assault, autotheft, biketheft, breakenter, homicide, robbery, shooting, theftfrommv, theftover. |
| `offence_label` | Text | Readable offence name. |
| `count` | Integer | Number of reported occurrences in that neighbourhood and year. |
| `rate_per_100000` | Float | Rate per 100,000 population as published by the Toronto Police Service. |
| `population_2025` | Integer | 2025 population estimate published on the source table (same value on every year of that neighbourhood). |
| `implied_population` | Integer | Population implied by count and the published rate (count divided by rate, times 100,000), rounded to the nearest person. Empty when the rate is zero or missing. |

### `data_dictionary.csv`

Column descriptions for every file in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `implied_population_by_neighbourhood_year.csv`

Median implied population by neighbourhood and year, recovered from published counts and rates.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | City of Toronto social planning neighbourhood number (158-neighbourhood model), zero padded to three digits. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `year` | Integer | Calendar year of the count and rate. |
| `implied_population` | Integer | Population implied by count and the published rate (count divided by rate, times 100,000), rounded to the nearest person. Empty when the rate is zero or missing. |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods, with classification and polygon centroid.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | City of Toronto social planning neighbourhood number (158-neighbourhood model), zero padded to three digits. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `neighbourhood_label` | Text | Name with the neighbourhood number in parentheses, as the City publishes it. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither, from the City neighbourhoods file. |
| `classification_code` | Text | Short classification code from the City neighbourhoods file. |
| `centroid_longitude` | Text | Longitude of the neighbourhood polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the neighbourhood polygon centroid, WGS84. |

## Source and licence

**Source:** City of Toronto Open Data, Neighbourhood Crime Rates (https://open.toronto.ca/dataset/neighbourhood-crime-rates/), originally published by the Toronto Police Service. Neighbourhood boundaries and classifications from https://open.toronto.ca/dataset/neighbourhoods/. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto. TPS Public Safety Data Portal terms also apply.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoneighbourhoodcrimerates20142025,
  author    = {Khan, John},
  title     = {Toronto Neighbourhood Crime Rates 2014 to 2025},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-crime-rates-2014-2025}
}
```

APA: Khan, J. (2026). *Toronto Neighbourhood Crime Rates 2014 to 2025* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-crime-rates-2014-2025

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Annual crime counts and rates for Toronto's 158 social planning neighbourhoods, 2014 to 2025. Offences are assault, auto theft, bike theft, break and enter, homicide, robbery, shooting and firearm discharges, theft from a motor vehicle, and theft over $5,000. Rates are per 100,000 people as published by the Toronto Police Service.

The official table is wide, with one column per offence and year. This version is reshaped to a tidy long file, plus a compact wide file with one row per neighbourhood and year. I also recover an implied population for each neighbourhood and year from the published count and rate, because the source table only lists a 2025 population estimate.

## Files

| File | What is in it |
|---|---|
| `crime_rates_long.csv` | One row per neighbourhood, year and offence |
| `crime_rates_by_neighbourhood_year.csv` | One row per neighbourhood and year, with count and rate columns for each offence |
| `crime_rates_citywide_by_year.csv` | Citywide sums and a rate based on implied population |
| `implied_population_by_neighbourhood_year.csv` | Median implied population by neighbourhood and year |
| `neighbourhoods.csv` | Names, Neighbourhood Improvement Area status, and polygon centroids |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the citywide assault series |

## Coverage and refresh

The source was last updated on the City catalogue in 2026 and the CSV used here includes years 2014 through 2025. I pulled the file on November 9, 2026. The Toronto Police Service refreshes neighbourhood crime rates about once a year. 2025 figures can still be revised as late reports are added.

There are 158 neighbourhoods in the file, which matches the current 158-neighbourhood model introduced when the older 140-neighbourhood model was split and redrawn. Do not join these rows to an older 140-neighbourhood boundary file without a crosswalk.

## Caveats

* These are occurrences reported to the Toronto Police Service, not a complete measure of all crime. Reporting practices and late entries change over time.
* Rates use population estimates supplied for this product (the City notes they come from Environics). I did not invent a population series. The `implied_population` column is just the population that makes the published rate match the published count, and it can differ slightly by offence because of rounding.
* `population_2025` is the single 2025 estimate from the source table, repeated on earlier years so you can see it. It is not a 2014 population.
* Citywide rates in `crime_rates_citywide_by_year.csv` are computed from the summed counts and the summed implied populations. They are not a separately published city rate.
* Locations in related incident-level police files are offset to the nearest intersection. This neighbourhood table is already aggregated, and no point coordinates are included.

## Sources

Toronto Police Service, Neighbourhood Crime Rates, published on the City of Toronto Open Data portal: https://open.toronto.ca/dataset/neighbourhood-crime-rates/

The Open Data catalogue package id is `neighbourhood-crime-rates`. Neighbourhood names and classifications come from the City's Neighbourhoods file: https://open.toronto.ca/dataset/neighbourhoods/

A dashboard and further documentation are on the Toronto Police Service Public Safety Data Portal: https://data.torontopolice.on.ca/

Pulled on November 9, 2026. Resource last modified date on the catalogue: 2026-02-20.

## Example uses

* Track which neighbourhoods saw the largest change in auto theft rates after 2020.
* Compare assault and robbery rates in Neighbourhood Improvement Areas with the rest of the city.
* Join the tidy file to census profile indicators on the same 158 neighbourhood identifiers.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). Some of the underlying figures are also published by the Toronto Police Service on the Public Safety Data Portal and are subject to the Toronto Police Service terms of use (https://data.torontopolice.on.ca/pages/terms-of-use). This dataset is not endorsed by the City of Toronto or the Toronto Police Service.

Changes made here: geometry dropped, columns renamed to snake_case, the wide offence-year columns reshaped to long and to a yearly wide table, implied population recovered from counts and rates, and neighbourhood classification and centroids joined from the City neighbourhoods file. Values of the published counts and rates were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
