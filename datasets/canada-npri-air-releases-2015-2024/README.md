<p align="center"><img src="../../assets/theme-environment.png" alt="Canada NPRI air releases 2015 to 2024" width="100%"></p>

# Canada NPRI air releases 2015 to 2024

*Industry, province and substance releases to air from the NPRI*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 2015 to 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-npri-air-releases-2015-2024](https://www.kaggle.com/datasets/johnnykhan1/canada-npri-air-releases-2015-2024)

## What it is

National Pollutant Release Inventory (NPRI) ten year tables for releases to air, tidied from Environment and Climate Change Canada open data. English industry, province by substance, and substance national tables for 2015 through 2024 were kept. French duplicate columns were dropped. A national annual rollup and a top industries file for the latest year were added.

Source dataset: [Ten-year data tables by province, industry and substance – releases](https://open.canada.ca/data/en/dataset/80298f8d-b23e-4f29-9f03-661a95949d0f) (Environment and Climate Change Canada, NPRI).

CSV files pulled on November 9, 2026 from the ECCC data mart linked on the Open Government Portal.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`air_releases_by_industry.csv`](data/air_releases_by_industry.csv) | 85 KB | in this repository |
| [`air_releases_by_province_substance.csv`](data/air_releases_by_province_substance.csv) | 431 KB | in this repository |
| [`air_releases_by_substance.csv`](data/air_releases_by_substance.csv) | 77 KB | in this repository |
| [`air_releases_national_annual.csv`](data/air_releases_national_annual.csv) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 49 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`top25_industries_2024.csv`](data/top25_industries_2024.csv) | 2 KB | in this repository |

## Columns

### `air_releases_by_industry.csv`

Ten year NPRI releases to air by industry and year.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | NPRI reporting year. |
| `industry_en` | Text | Industry name in English as published in the NPRI ten year industry table. |
| `naics` | Integer | North American Industry Classification System (NAICS) code as published. |
| `releases_to_air_tonnes` | Float | Total reported releases to air in tonnes for that row. |
| `facility_count` | Integer | Number of facilities contributing to the row as published. |

### `air_releases_by_province_substance.csv`

Ten year NPRI releases to air by province, substance and year.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | NPRI reporting year. |
| `province` | Text | Province or territory code or name as published (for example AB, ON, QC). |
| `cas_number` | Text | Chemical Abstracts Service registry number for the substance, when published. |
| `substance_en` | Text | Substance name in English as published. |
| `releases_to_air_tonnes` | Float | Total reported releases to air in tonnes for that row. |
| `facility_count` | Integer | Number of facilities contributing to the row as published. |

### `air_releases_by_substance.csv`

Ten year NPRI releases to air by substance and year (national).

| Column | Type | Description |
|---|---|---|
| `year` | Integer | NPRI reporting year. |
| `cas_number` | Text | Chemical Abstracts Service registry number for the substance, when published. |
| `substance_en` | Text | Substance name in English as published. |
| `releases_to_air_tonnes` | Float | Total reported releases to air in tonnes for that row. |
| `facility_count` | Integer | Number of facilities contributing to the row as published. |

### `air_releases_national_annual.csv`

National annual totals rolled up from the substance table.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | NPRI reporting year. |
| `total_releases_to_air_tonnes` | Float | Sum of substance level releases to air in tonnes for the year. |
| `substance_count` | Integer | Number of distinct substances in the national annual rollup. |
| `reporting_facility_rows` | Integer | Sum of facility_count across substance rows for the year (not a unique facility count). |

### `data_dictionary.csv`

- `column`: Name of the column being described - `file`: File that contains the column - `type`: Data type of the column - `description`: Plain-language description of the column

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `top25_industries_2024.csv`

Twenty five industries with the largest releases to air in 2024.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | NPRI reporting year. |
| `industry_en` | Text | Industry name in English as published in the NPRI ten year industry table. |
| `naics` | Integer | North American Industry Classification System (NAICS) code as published. |
| `releases_to_air_tonnes` | Float | Total reported releases to air in tonnes for that row. |
| `facility_count` | Integer | Number of facilities contributing to the row as published. |

## Source and licence

**Source:** Environment and Climate Change Canada, National Pollutant Release Inventory, Ten-year data tables by province, industry and substance – releases, via open.canada.ca, Open Government Licence Canada

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadanpriairreleases20152024,
  author    = {Khan, John},
  title     = {Canada NPRI air releases 2015 to 2024},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-npri-air-releases-2015-2024}
}
```

APA: Khan, J. (2026). *Canada NPRI air releases 2015 to 2024* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-npri-air-releases-2015-2024

<details><summary>Full notes from the Kaggle page</summary>

## What this is

National Pollutant Release Inventory (NPRI) ten year tables for releases to air, tidied from Environment and Climate Change Canada open data. English industry, province by substance, and substance national tables for 2015 through 2024 were kept. French duplicate columns were dropped. A national annual rollup and a top industries file for the latest year were added.

Source dataset: [Ten-year data tables by province, industry and substance – releases](https://open.canada.ca/data/en/dataset/80298f8d-b23e-4f29-9f03-661a95949d0f) (Environment and Climate Change Canada, NPRI).

CSV files pulled on November 9, 2026 from the ECCC data mart linked on the Open Government Portal.

## Coverage

Years 2015 through 2024. Tables cover reported releases to air by industry (with NAICS), by province and substance, and by substance at the national level. Facility counts are as published in each source table.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. NPRI usually publishes a new reporting year each spring. For a later year, download the ten year tables again from the Open Government Portal.

## A few numbers from this snapshot

* In 2024, the substance table rollup totals about 2,805,759 tonnes of releases to air.
* The industry with the largest releases to air in 2024 in this file is Oil and gas extraction at about 888,127 tonnes.
* Industry, province and substance tables can disagree slightly when summed because they are published as separate aggregations.

## Example uses

* Track national releases to air over the last decade.
* Rank industries or substances by reported air releases.
* Compare provincial substance totals for a chosen year.

## Caveats

NPRI covers facilities that meet reporting thresholds. It is not a complete inventory of all Canadian air emissions. The national annual file sums substance rows and is not an official NPRI national total product. Facility count summed across substances double counts facilities that report more than one substance. Province codes follow the published table spellings.

## Files

* `air_releases_by_industry.csv`: Ten year NPRI releases to air by industry and year.
* `air_releases_by_province_substance.csv`: Ten year NPRI releases to air by province, substance and year.
* `air_releases_by_substance.csv`: Ten year NPRI releases to air by substance and year (national).
* `air_releases_national_annual.csv`: National annual totals rolled up from the substance table.
* `top25_industries_2024.csv`: Twenty five industries with the largest releases to air in 2024.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, National Pollutant Release Inventory, ten year releases tables. The published values were not changed. Columns were renamed, French duplicate columns were dropped, and summary files were derived. This is not an official Government of Canada product and Environment and Climate Change Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
