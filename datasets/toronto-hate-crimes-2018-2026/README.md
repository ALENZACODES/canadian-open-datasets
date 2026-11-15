<p align="center"><img src="../../assets/theme-public-safety.png" alt="Toronto Hate Crimes 2018 to 2026" width="100%"></p>

# Toronto Hate Crimes 2018 to 2026

*Verified occurrences by neighbourhood, including disability bias*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 2014 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-hate-crimes-2018-2026](https://www.kaggle.com/datasets/johnnykhan1/toronto-hate-crimes-2018-2026)

## What it is

Verified hate crime occurrences investigated by the Toronto Police Service Hate Crime Unit, reported from 2018 through 2025. Bias categories in the official file are age, mental or physical disability, race, ethnicity, language, religion, sexual orientation, gender, and other similar factors. This version keeps those flags, including disability, and adds tidy neighbourhood yearly counts plus a long table of bias mentions.

2,041 verified occurrences, reported 2018 to 2025. 3 recorded a disability bias.

The official catalogue notes that the file includes occurrences by reported date since 2018. Some occurrence dates are earlier than 2018 because the event was reported later.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 67 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 7 KB | in this repository |
| [`hate_crime_bias_mentions.csv`](data/hate_crime_bias_mentions.csv) | 290 KB | in this repository |
| [`hate_crime_events.csv`](data/hate_crime_events.csv) | 429 KB | in this repository |
| [`hate_crimes_bias_by_year.csv`](data/hate_crimes_bias_by_year.csv) | 1 KB | in this repository |
| [`hate_crimes_citywide_by_year.csv`](data/hate_crimes_citywide_by_year.csv) | 1 KB | in this repository |
| [`hate_crimes_yearly_by_neighbourhood.csv`](data/hate_crimes_yearly_by_neighbourhood.csv) | 36 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `hate_crime_bias_mentions.csv`

Long table: one row for each bias category recorded on an event.

| Column | Type | Description |
|---|---|---|
| `reported_year` | Integer | Year the occurrence was reported to police. |
| `occurrence_year` | Integer | Year the occurrence took place, which can be earlier than the reported year. |
| `neighbourhood_id` | Text | 158-neighbourhood model number, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `division` | Text | Toronto Police Service division code. |
| `location_type` | Text | Type of location as published (for example a house, a school, or a place of worship). |
| `primary_offence` | Text | Primary offence as recorded by the Hate Crime Unit. |
| `bias_category` | Text | Short bias category code (age, disability, race, ethnicity, language, religion, sexual_orientation, gender). |
| `bias_label` | Text | Readable bias category name. |
| `bias_detail` | Text | The specific bias recorded (for example Jewish, Black, or Gay). Yes when the source only flagged the category. |
| `multiple_bias` | Boolean | Whether more than one bias category was recorded. |
| `arrest_made` | Boolean | Whether an arrest was recorded. |

### `hate_crime_events.csv`

One row per verified hate crime occurrence, with bias flags including mental or physical disability.

| Column | Type | Description |
|---|---|---|
| `occurrence_year` | Integer | Year the occurrence took place, which can be earlier than the reported year. |
| `occurrence_date` | Date | Occurrence date (YYYY-MM-DD). |
| `reported_year` | Integer | Year the occurrence was reported to police. |
| `reported_date` | Date | Reported date (YYYY-MM-DD). |
| `division` | Text | Toronto Police Service division code. |
| `location_type` | Text | Type of location as published (for example a house, a school, or a place of worship). |
| `primary_offence` | Text | Primary offence as recorded by the Hate Crime Unit. |
| `multiple_bias` | Boolean | Whether more than one bias category was recorded. |
| `arrest_made` | Boolean | Whether an arrest was recorded. |
| `neighbourhood_id` | Text | 158-neighbourhood model number, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `neighbourhood_id_140` | Text | Older 140-neighbourhood model number. |
| `neighbourhood_name_140` | Text | Older 140-neighbourhood model name. |
| `bias_age` | Text | Detail recorded for age bias. Empty when that bias was not recorded. |
| `has_age_bias` | Boolean | True when a age bias was recorded on the event. |
| `bias_disability` | Boolean | Detail recorded for mental or physical disability bias. Empty when that bias was not recorded. |
| `has_disability_bias` | Boolean | True when a mental or physical disability bias was recorded on the event. |
| `bias_race` | Text | Detail recorded for race bias. Empty when that bias was not recorded. |
| `has_race_bias` | Boolean | True when a race bias was recorded on the event. |
| `bias_ethnicity` | Text | Detail recorded for ethnicity bias. Empty when that bias was not recorded. |
| `has_ethnicity_bias` | Boolean | True when a ethnicity bias was recorded on the event. |
| `bias_language` | Text | Detail recorded for language bias. Empty when that bias was not recorded. |
| `has_language_bias` | Boolean | True when a language bias was recorded on the event. |
| `bias_religion` | Text | Detail recorded for religion bias. Empty when that bias was not recorded. |
| `has_religion_bias` | Boolean | True when a religion bias was recorded on the event. |
| `bias_sexual_orientation` | Text | Detail recorded for sexual orientation bias. Empty when that bias was not recorded. |
| `has_sexual_orientation_bias` | Boolean | True when a sexual orientation bias was recorded on the event. |
| `bias_gender` | Text | Detail recorded for gender bias. Empty when that bias was not recorded. |
| `has_gender_bias` | Boolean | True when a gender bias was recorded on the event. |

### `hate_crimes_bias_by_year.csv`

Citywide annual counts of bias mentions by category.

| Column | Type | Description |
|---|---|---|
| `reported_year` | Integer | Year the occurrence was reported to police. |
| `bias_category` | Text | Short bias category code (age, disability, race, ethnicity, language, religion, sexual_orientation, gender). |
| `bias_label` | Text | Readable bias category name. |
| `mentions` | Integer | Number of events in which that bias category was recorded. An event with more than one bias appears in more than one row. |

### `hate_crimes_citywide_by_year.csv`

Citywide annual counts by reported year.

| Column | Type | Description |
|---|---|---|
| `reported_year` | Integer | Year the occurrence was reported to police. |
| `events` | Integer | Number of hate crime occurrences reported in that neighbourhood and year. |

### `hate_crimes_yearly_by_neighbourhood.csv`

Annual occurrence counts by neighbourhood, with a column for each bias category.

| Column | Type | Description |
|---|---|---|
| `reported_year` | Integer | Year the occurrence was reported to police. |
| `neighbourhood_id` | Text | 158-neighbourhood model number, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `events` | Integer | Number of hate crime occurrences reported in that neighbourhood and year. |
| `disability_bias` | Integer | Occurrences with a mental or physical disability bias recorded. |
| `race_bias` | Integer | Occurrences with a race bias recorded. |
| `religion_bias` | Integer | Occurrences with a religion bias recorded. |
| `ethnicity_bias` | Integer | Occurrences with an ethnicity bias recorded. |
| `sexual_orientation_bias` | Integer | Occurrences with a sexual orientation bias recorded. |
| `gender_bias` | Integer | Occurrences with a gender bias recorded. |
| `age_bias` | Integer | Occurrences with an age bias recorded. |
| `language_bias` | Integer | Occurrences with a language bias recorded. |
| `arrest_made` | Integer | Whether an arrest was recorded. |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | 158-neighbourhood model number, or NSA. |
| `neighbourhood_name` | Text | Neighbourhood name in the 158-neighbourhood model. |
| `neighbourhood_label` | Text | Name with the number in parentheses. |
| `classification` | Text | Neighbourhood Improvement Area, Emerging Neighbourhood, or neither. |
| `classification_code` | Text | Short classification code. |
| `centroid_longitude` | Text | Longitude of the polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the polygon centroid, WGS84. |

## Source and licence

**Source:** City of Toronto Open Data, Hate Crimes (https://open.toronto.ca/dataset/hate-crimes-open-data/), published by the Toronto Police Service Hate Crime Unit. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto. TPS Public Safety Data Portal terms also apply.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontohatecrimes20182026,
  author    = {Khan, John},
  title     = {Toronto Hate Crimes 2018 to 2026},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-hate-crimes-2018-2026}
}
```

APA: Khan, J. (2026). *Toronto Hate Crimes 2018 to 2026* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-hate-crimes-2018-2026

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Verified hate crime occurrences investigated by the Toronto Police Service Hate Crime Unit, reported from 2018 through 2025. Bias categories in the official file are age, mental or physical disability, race, ethnicity, language, religion, sexual orientation, gender, and other similar factors. This version keeps those flags, including disability, and adds tidy neighbourhood yearly counts plus a long table of bias mentions.

2,041 verified occurrences, reported 2018 to 2025. 3 recorded a disability bias.

The official catalogue notes that the file includes occurrences by reported date since 2018. Some occurrence dates are earlier than 2018 because the event was reported later.

## Files

| File | What is in it |
|---|---|
| `hate_crime_events.csv` | One row per occurrence, with a column for each bias category |
| `hate_crime_bias_mentions.csv` | One row per bias recorded on an event |
| `hate_crimes_yearly_by_neighbourhood.csv` | Annual counts by neighbourhood, with bias columns |
| `hate_crimes_citywide_by_year.csv` | Citywide counts by reported year |
| `hate_crimes_bias_by_year.csv` | Citywide bias mentions by year and category |
| `neighbourhoods.csv` | 158-neighbourhood lookup |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the citywide yearly series |

## Coverage and refresh

Pulled on November 9, 2026 from the City of Toronto Open Data portal. Resource last modified: 2026-07-20. The Hate Crime Unit updates this file periodically. Late verification can change recent years.

## Caveats

* These are occurrences verified by the Hate Crime Unit, not every reported incident and not every form of hate in the city.
* An event can carry more than one bias. In the mentions file, that event appears once per bias recorded. Do not sum mentions across categories and call the total the number of events.
* Occurrence year and reported year can differ. Use reported year if you want a stable reporting-period series.
* `NSA` means the location was not mapped to a neighbourhood.
* Neighbourhood ids follow the current 158-neighbourhood model. The `_140` columns keep the older model for historical joins.

## Sources

Toronto Police Service Hate Crime Unit, Hate Crimes Open Data, on the City of Toronto Open Data portal: https://open.toronto.ca/dataset/hate-crimes-open-data/

Neighbourhoods: https://open.toronto.ca/dataset/neighbourhoods/

Pulled on November 9, 2026.

## Example uses

* Track disability-bias and religion-bias occurrences over time.
* Compare neighbourhood counts with the neighbourhood crime rates file on `neighbourhood_id`.
* See which location types appear most often for a given bias category.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). This table is also published by the Toronto Police Service on the Public Safety Data Portal and is subject to the Toronto Police Service terms of use (https://data.torontopolice.on.ca/pages/terms-of-use). This dataset is not endorsed by the City of Toronto or the Toronto Police Service.

Changes made here: columns renamed to snake_case, neighbourhood names cleaned, bias flags standardized, and long, yearly and citywide tables added. Occurrence counts were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
