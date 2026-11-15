<p align="center"><img src="../../assets/theme-public-safety.png" alt="Canada education and crime severity" width="100%"></p>

# Canada education and crime severity

*CMA and Toronto joins of education, income, density and crime*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 2021 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-education-and-crime](https://www.kaggle.com/datasets/johnnykhan1/canada-education-and-crime)

## What it is

Analysis-ready joins of education attainment with crime measures for Canadian census metropolitan areas and for Toronto's 158 social planning neighbourhoods.

For CMAs, the share of people aged 25 to 64 with a bachelor's degree or higher (2021 Census) is joined to median employment income for that education group (income year 2020), population density (2021), and the police-reported Crime Severity Index (StatCan Table 35-10-0026, year 2025 in this snapshot).

For Toronto neighbourhoods, 2021 Neighbourhood Profiles education and household income are joined to Neighbourhood Crime Rates. Land area is computed from the City of Toronto neighbourhoods geojson so density can be controlled.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`cma_education_income_csi.csv`](data/cma_education_income_csi.csv) | 6 KB | in this repository |
| [`cover.png`](data/cover.png) | 45 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 9 KB | in this repository |
| [`province_education_income_csi.csv`](data/province_education_income_csi.csv) | 2 KB | in this repository |
| [`sources_note.txt`](data/sources_note.txt) | 1 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 29 KB | in this repository |
| [`toronto_neighbourhood_education_crime_2021.csv`](data/toronto_neighbourhood_education_crime_2021.csv) | 35 KB | in this repository |
| [`toronto_neighbourhood_education_crime_2024.csv`](data/toronto_neighbourhood_education_crime_2024.csv) | 35 KB | in this repository |

## Columns

### `cma_education_income_csi.csv`

Analysis-ready CMA table.

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published, or Toronto for citywide TPS rows. |
| `geo_clean` | Text | Geography name with province codes stripped for joining. |
| `geo_level` | Text | Geography level: canada, region, province_or_canada, cma_or_ca, city or neighbourhood. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `population_2021` | Float | 2021 Census population count (or 25% sample population for neighbourhood profiles). |
| `land_area_km2` | Float | Land area in square kilometres. |
| `population_density_per_km2` | Float | Population density per square kilometre. |
| `education_universe` | Float | Denominator for the education share. |
| `bachelor_or_higher_count` | Float | Count of people with a bachelor's degree or higher. |
| `bachelor_or_higher_share` | Float | Share of the education universe with a bachelor's degree or higher (0 to 1). |
| `median_employment_income_bachelor_plus` | Float | Median employment income for bachelor's degree or higher, age 25 to 64, 2020. |
| `csi_year` | Integer | Year of the Crime Severity Index figure. |
| `crime_severity_index` | Float | Police-reported Crime Severity Index. |
| `violent_csi` | Float | Violent Crime Severity Index. |
| `nonviolent_csi` | Float | Non-violent Crime Severity Index. |

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `file` | Text | Name of the column being described |
| `column` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `province_education_income_csi.csv`

Canada and provinces joined to CSI.

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published, or Toronto for citywide TPS rows. |
| `geo_clean` | Text | Geography name with province codes stripped for joining. |
| `geo_level` | Text | Geography level: canada, region, province_or_canada, cma_or_ca, city or neighbourhood. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `population_2021` | Text | 2021 Census population count (or 25% sample population for neighbourhood profiles). |
| `land_area_km2` | Text | Land area in square kilometres. |
| `population_density_per_km2` | Text | Population density per square kilometre. |
| `education_universe` | Float | Denominator for the education share. |
| `bachelor_or_higher_count` | Float | Count of people with a bachelor's degree or higher. |
| `bachelor_or_higher_share` | Float | Share of the education universe with a bachelor's degree or higher (0 to 1). |
| `median_employment_income_bachelor_plus` | Float | Median employment income for bachelor's degree or higher, age 25 to 64, 2020. |
| `csi_year` | Integer | Year of the Crime Severity Index figure. |
| `crime_severity_index` | Float | Police-reported Crime Severity Index. |
| `violent_csi` | Float | Violent Crime Severity Index. |
| `nonviolent_csi` | Float | Non-violent Crime Severity Index. |

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata shipped with the table download, including notes and the symbol legend. Layout is as published, not tidied.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | — |
| `Product Id` | Text | — |
| `CANSIM Id` | Text | — |
| `URL` | Text | — |
| `Cube Notes` | Text | — |
| `Archive Status` | Text | — |
| `Frequency` | Text | — |
| `Start Reference Period` | Text | — |
| `End Reference Period` | Date | — |
| `Total number of dimensions` | Integer | — |

### `toronto_neighbourhood_education_crime_2021.csv`

Toronto neighbourhoods with 2021 crime rates.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | Toronto 158-neighbourhood model number, or NSA when not mapped. |
| `neighbourhood_name` | Text | Toronto neighbourhood name. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `median_household_income_2020` | Float | Median total income of household in 2020 ($). |
| `population_2021` | Float | 2021 Census population count (or 25% sample population for neighbourhood profiles). |
| `education_universe` | Float | Denominator for the education share. |
| `bachelor_or_higher_count` | Float | Count of people with a bachelor's degree or higher. |
| `bachelor_or_higher_share` | Float | Share of the education universe with a bachelor's degree or higher (0 to 1). |
| `land_area_km2` | Float | Land area in square kilometres. |
| `population_density_per_km2` | Float | Population density per square kilometre. |
| `crime_year` | Integer | Year of the neighbourhood crime rates. |
| `total_major_crime_rate_per_100000` | Float | Sum of the major crime rates listed in this file for that neighbourhood and year. |
| `assault_rate_per_100000` | Float | Assault rate per 100,000 population. |
| `autotheft_rate_per_100000` | Float | Auto theft rate per 100,000 population. |
| `biketheft_rate_per_100000` | Float | Bicycle theft rate per 100,000 population. |
| `breakenter_rate_per_100000` | Float | Break and enter rate per 100,000 population. |
| `homicide_rate_per_100000` | Float | Homicide rate per 100,000 population. |
| `robbery_rate_per_100000` | Float | Robbery rate per 100,000 population. |
| `shooting_rate_per_100000` | Float | Shooting rate per 100,000 population. |
| `theftfrommv_rate_per_100000` | Float | Theft from motor vehicle rate per 100,000 population. |
| `theftover_rate_per_100000` | Float | Theft over rate per 100,000 population. |

### `toronto_neighbourhood_education_crime_2024.csv`

Toronto neighbourhoods with 2024 crime rates.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | Toronto 158-neighbourhood model number, or NSA when not mapped. |
| `neighbourhood_name` | Text | Toronto neighbourhood name. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `median_household_income_2020` | Float | Median total income of household in 2020 ($). |
| `population_2021` | Float | 2021 Census population count (or 25% sample population for neighbourhood profiles). |
| `education_universe` | Float | Denominator for the education share. |
| `bachelor_or_higher_count` | Float | Count of people with a bachelor's degree or higher. |
| `bachelor_or_higher_share` | Float | Share of the education universe with a bachelor's degree or higher (0 to 1). |
| `land_area_km2` | Float | Land area in square kilometres. |
| `population_density_per_km2` | Float | Population density per square kilometre. |
| `crime_year` | Integer | Year of the neighbourhood crime rates. |
| `total_major_crime_rate_per_100000` | Float | Sum of the major crime rates listed in this file for that neighbourhood and year. |
| `assault_rate_per_100000` | Float | Assault rate per 100,000 population. |
| `autotheft_rate_per_100000` | Float | Auto theft rate per 100,000 population. |
| `biketheft_rate_per_100000` | Float | Bicycle theft rate per 100,000 population. |
| `breakenter_rate_per_100000` | Float | Break and enter rate per 100,000 population. |
| `homicide_rate_per_100000` | Float | Homicide rate per 100,000 population. |
| `robbery_rate_per_100000` | Float | Robbery rate per 100,000 population. |
| `shooting_rate_per_100000` | Float | Shooting rate per 100,000 population. |
| `theftfrommv_rate_per_100000` | Float | Theft from motor vehicle rate per 100,000 population. |
| `theftover_rate_per_100000` | Float | Theft over rate per 100,000 population. |

## Source and licence

**Source:** Statistics Canada Tables 98-10-0384, 98-10-0003, 35-10-0026, 98-10-0410 (November 9, 2026). City of Toronto Neighbourhood Profiles and Crime Rates. Prepared by John Khan in Toronto, Ontario.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.
- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaeducationandcrime,
  author    = {Khan, John},
  title     = {Canada education and crime severity},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-education-and-crime}
}
```

APA: Khan, J. (2026). *Canada education and crime severity* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-education-and-crime

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Analysis-ready joins of education attainment with crime measures for Canadian census metropolitan areas and for Toronto's 158 social planning neighbourhoods.

For CMAs, the share of people aged 25 to 64 with a bachelor's degree or higher (2021 Census) is joined to median employment income for that education group (income year 2020), population density (2021), and the police-reported Crime Severity Index (StatCan Table 35-10-0026, year 2025 in this snapshot).

For Toronto neighbourhoods, 2021 Neighbourhood Profiles education and household income are joined to Neighbourhood Crime Rates. Land area is computed from the City of Toronto neighbourhoods geojson so density can be controlled.

## Files

| File | What is in it |
|---|---|
| `cma_education_income_csi.csv` | CMA education, income, density, CSI |
| `province_education_income_csi.csv` | Canada and provinces joined to CSI where available |
| `toronto_neighbourhood_education_crime_2021.csv` | Toronto neighbourhoods with 2021 crime rates |
| `toronto_neighbourhood_education_crime_2024.csv` | Same census fields with 2024 crime rates |
| `data_dictionary.csv` | Column descriptions |
| `statcan_table_metadata.csv` | Official CSI cube notes |
| `sources_note.txt` | Short list of source tables |
| `cover.png` | Cover scatterplot |

## Coverage

Census year 2021 for education, income and density. CSI year 2025. Toronto crime years 2021 and 2024 in separate files. Neighbourhood ids follow the current 158-neighbourhood model and match the other Toronto open data files in this series.

## A few numbers from this snapshot

* The CMA analysis table has 35 census metropolitan areas after the join.
* Simple Pearson correlation between bachelor's-or-higher share and CSI (2025) across those CMAs is -0.238 in this snapshot.
* Toronto neighbourhood file covers 158 neighbourhoods with 2021 census education and 2021 crime rates.
* Correlation is not causation. Income and density are included so you can run a controlled check.

## Caveats

* Correlation is not causation. Places with more university graduates often differ on income, age structure, policing, nightlife and reporting practices. The starter notebook runs a simple regression with income and density controls; that still does not identify a causal effect.
* CSI and neighbourhood crime rates measure different things. CSI is a weighted index across many offence types for a CMA. Neighbourhood rates are offence-specific rates per 100,000.
* Education for Toronto neighbourhoods uses the age 15 and over highest certificate universe in the Neighbourhood Profiles. CMA education uses age 25 to 64 from Table 98-10-0384.
* Density for Toronto neighbourhoods uses population from the 25% sample profile divided by geodesic land area from the neighbourhood polygons. It is an approximation.
* Values can be revised when Statistics Canada or the City of Toronto update their files.

## Sources

Statistics Canada Tables 98-10-0384-01, 98-10-0003-01, 35-10-0026-01, 98-10-0410-01, downloaded November 9, 2026.

City of Toronto Neighbourhood Profiles and Neighbourhood Crime Rates (Open Government Licence – Toronto).

## Licence

StatCan figures: [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Toronto figures: [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Not an official Statistics Canada or City of Toronto product.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
