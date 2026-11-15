<p align="center"><img src="../../assets/theme-population.png" alt="Toronto Neighbourhood Profiles Census 2021" width="100%"></p>

# Toronto Neighbourhood Profiles Census 2021

*Tidy 2021 Census indicators for all 158 neighbourhoods*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** 2021 to 2021 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-profiles-2021](https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-profiles-2021)

## What it is

The City of Toronto's 2021 Census neighbourhood profiles, reshaped from the official 158-neighbourhood workbook into a tidy long table. The City file is wide: each neighbourhood is a column and each census characteristic is a row. This version is one row per neighbourhood and characteristic, with a numeric value column and a small wide extract of commonly used indicators.

158 neighbourhoods and 1730 characteristics. The profiles use Statistics Canada Census of Population 2021 data, compiled by the City. The geography is the current 158-neighbourhood social planning model, not the older 140-neighbourhood model.

Existing Kaggle copies of these profiles are mostly the 2016 140-neighbourhood file, or a 2021 file left in a hard-to-use wide layout with low usability. This version is the 158-neighbourhood 2021 profile in a tidy form.

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`census_profile_2021_long.csv`](data/census_profile_2021_long.csv) | 39.4 MB | in this repository |
| [`characteristic_list.csv`](data/characteristic_list.csv) | 58 KB | in this repository |
| [`cover.png`](data/cover.png) | 68 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 5 KB | in this repository |
| [`neighbourhood_profile_metadata.csv`](data/neighbourhood_profile_metadata.csv) | 18 KB | in this repository |
| [`neighbourhoods.csv`](data/neighbourhoods.csv) | 16 KB | in this repository |
| [`selected_indicators_by_neighbourhood.csv`](data/selected_indicators_by_neighbourhood.csv) | 19 KB | in this repository |

## Columns

### `census_profile_2021_long.csv`

Tidy long table: one row per neighbourhood and 2021 Census characteristic, for all 158 neighbourhoods.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | Neighbourhood number in the 158-neighbourhood model, zero padded. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `classification` | Text | Toronto Strong Neighbourhoods Strategy 2020 designation, as published. |
| `characteristic_id` | Text | Identifier for the census characteristic row, in the order of the official sheet. |
| `characteristic` | Text | Census characteristic label, with extra spaces collapsed. Indentation is kept in indent_level. |
| `indent_level` | Integer | How far the official label was indented, as a rough hierarchy (0 is a heading). |
| `value_raw` | Integer | Value as published, which may be a number, a percent, or a blank. |
| `value_numeric` | Float | Numeric conversion of value_raw, with commas and percent signs removed. Empty when the value is not numeric. |

### `characteristic_list.csv`

Ordered list of census characteristics from the official sheet.

| Column | Type | Description |
|---|---|---|
| `characteristic_id` | Text | Identifier for the census characteristic row, in the order of the official sheet. |
| `characteristic` | Text | Census characteristic label, with extra spaces collapsed. Indentation is kept in indent_level. |
| `indent_level` | Integer | How far the official label was indented, as a rough hierarchy (0 is a heading). |

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `neighbourhood_profile_metadata.csv`

Official neighbourhood metadata sheet from the City workbook.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_full_census_profile_name` | Text | Official neighbourhood metadata column neighbourhood_full_census_profile_name. |
| `hdnum` | Integer | Official neighbourhood metadata column hdnum. |
| `hdname` | Text | Official neighbourhood metadata column hdname. |
| `tsns_designation` | Text | Official neighbourhood metadata column tsns_designation. |
| `neighbourhood_id` | Text | Neighbourhood number in the 158-neighbourhood model, zero padded. |

### `neighbourhoods.csv`

Lookup of the 158 social planning neighbourhoods, with centroids.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | Neighbourhood number in the 158-neighbourhood model, zero padded. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `neighbourhood_label` | Text | Name with the number in parentheses. |
| `classification` | Text | Toronto Strong Neighbourhoods Strategy 2020 designation, as published. |
| `classification_code` | Text | Short classification code. |
| `centroid_longitude` | Text | Longitude of the polygon centroid, WGS84. |
| `centroid_latitude` | Text | Latitude of the polygon centroid, WGS84. |

### `selected_indicators_by_neighbourhood.csv`

A small wide extract of frequently used indicators, one row per neighbourhood.

| Column | Type | Description |
|---|---|---|
| `neighbourhood_id` | Text | Neighbourhood number in the 158-neighbourhood model, zero padded. |
| `neighbourhood_name` | Text | Neighbourhood name. |
| `classification` | Text | Toronto Strong Neighbourhoods Strategy 2020 designation, as published. |
| `population_0_to_14` | Float | Selected 2021 Census indicator: population_0_to_14. See the long file for the official characteristic label. |
| `unemployment_rate` | Float | Selected 2021 Census indicator: unemployment_rate. See the long file for the official characteristic label. |
| `low_income_lim_at_pct` | Float | Selected 2021 Census indicator: low_income_lim_at_pct. See the long file for the official characteristic label. |
| `population_15_to_64` | Float | Selected 2021 Census indicator: population_15_to_64. See the long file for the official characteristic label. |
| `immigrants` | Float | Selected 2021 Census indicator: immigrants. See the long file for the official characteristic label. |
| `population_65_and_over` | Float | Selected 2021 Census indicator: population_65_and_over. See the long file for the official characteristic label. |
| `non_immigrants` | Float | Selected 2021 Census indicator: non_immigrants. See the long file for the official characteristic label. |
| `median_household_income_2020` | Float | Selected 2021 Census indicator: median_household_income_2020. See the long file for the official characteristic label. |
| `population_25pct_sample` | Float | Selected 2021 Census indicator: population_25pct_sample. See the long file for the official characteristic label. |

## Source and licence

**Source:** City of Toronto Open Data, Neighbourhood Profiles 2021, 158-neighbourhood model (https://open.toronto.ca/dataset/neighbourhood-profiles/), compiled from the Statistics Canada 2021 Census of Population. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontoneighbourhoodprofiles2021,
  author    = {Khan, John},
  title     = {Toronto Neighbourhood Profiles Census 2021},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-profiles-2021}
}
```

APA: Khan, J. (2026). *Toronto Neighbourhood Profiles Census 2021* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-neighbourhood-profiles-2021

<details><summary>Full notes from the Kaggle page</summary>

## What this is

The City of Toronto's 2021 Census neighbourhood profiles, reshaped from the official 158-neighbourhood workbook into a tidy long table. The City file is wide: each neighbourhood is a column and each census characteristic is a row. This version is one row per neighbourhood and characteristic, with a numeric value column and a small wide extract of commonly used indicators.

158 neighbourhoods and 1730 characteristics. The profiles use Statistics Canada Census of Population 2021 data, compiled by the City. The geography is the current 158-neighbourhood social planning model, not the older 140-neighbourhood model.

Existing Kaggle copies of these profiles are mostly the 2016 140-neighbourhood file, or a 2021 file left in a hard-to-use wide layout with low usability. This version is the 158-neighbourhood 2021 profile in a tidy form.

## Files

| File | What is in it |
|---|---|
| `census_profile_2021_long.csv` | One row per neighbourhood and characteristic |
| `characteristic_list.csv` | The official characteristic order and indent level |
| `selected_indicators_by_neighbourhood.csv` | A compact wide file of selected indicators |
| `neighbourhood_profile_metadata.csv` | The City metadata sheet |
| `neighbourhoods.csv` | 158-neighbourhood lookup and centroids |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the 25% sample population counts |

## Coverage and refresh

The Census is taken every five years. This file is the City's 2021 profile for the 158-neighbourhood model. I pulled the workbook on November 9, 2026. The catalogue resource was last modified on 2023-10-06. The City also publishes older profiles on the 140-neighbourhood model. Those older workbooks are not included here.

## Caveats

* Many counts come from the Census 25% sample. They are rounded by Statistics Canada and will not add perfectly to totals.
* The sum of neighbourhood population counts is not an official city total, because of rounding and the sample. Use official city totals from Statistics Canada if you need the city as a whole.
* Percent figures and dollar figures are mixed in the same value column. Use the characteristic label to know the unit, and prefer `value_numeric` for calculations.
* `indent_level` is a convenience field from leading spaces in the official labels. It is a guide to hierarchy, not an official Statistics Canada code.
* Neighbourhood Improvement Area designations follow the City's TSNS 2020 field in this workbook.

## Sources

City of Toronto Neighbourhood Profiles: https://open.toronto.ca/dataset/neighbourhood-profiles/

The profile values are compiled from the Statistics Canada 2021 Census of Population. Neighbourhood boundaries: https://open.toronto.ca/dataset/neighbourhoods/

Pulled on November 9, 2026.

## Example uses

* Compare median household income and low-income rates across the 158 neighbourhoods.
* Join the tidy file or the selected indicators file to the neighbourhood crime rates or KSI files on `neighbourhood_id`.
* Build a small atlas of age structure, immigration and housing type.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). Census values originate from Statistics Canada and should be credited to Statistics Canada when you use them. This dataset is not endorsed by the City of Toronto or Statistics Canada.

Changes made here: the wide official sheet was melted to a long table, labels were trimmed, a numeric value column was added, and a small wide extract of selected indicators was created. Published values were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
