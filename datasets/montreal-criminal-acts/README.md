<p align="center"><img src="../../assets/theme-public-safety.png" alt="Montreal criminal acts" width="100%"></p>

# Montreal criminal acts

*SPVM criminal act records with district, shift and coordinates*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 1 January 2015 to 7 November 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/montreal-criminal-acts](https://www.kaggle.com/datasets/johnnykhan1/montreal-criminal-acts)

## What it is

Criminal act records published by the City of Montreal / SPVM, with offence category, date, shift, police district and coordinates.

Portal: [Actes criminels](https://donnees.montreal.ca/dataset/actes-criminels).

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 1 KB | in this repository |
| [`monthly_incident_counts.csv`](data/monthly_incident_counts.csv) | 2 KB | in this repository |
| [`montreal_criminal_acts.csv`](data/montreal_criminal_acts.csv) | 31.5 MB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `monthly_incident_counts.csv`

Monthly incident counts derived from the incident file.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Month start date for aggregated counts. |
| `incidents` | Integer | Number of incident rows in that month. |

### `montreal_criminal_acts.csv`

Individual criminal act records for Montreal.

| Column | Type | Description |
|---|---|---|
| `category` | Text | Offence category as published by the Service de police de la Ville de Montreal. |
| `date` | Date | Date of the incident. |
| `shift` | Text | Work shift / time of day quart as published (for example jour, soir, nuit). |
| `police_district` | Float | Police district (PDQ) identifier. |
| `x` | Float | Projected X coordinate as published. |
| `y` | Float | Projected Y coordinate as published. |
| `longitude` | Text | Longitude in WGS84. |
| `latitude` | Text | Latitude in WGS84. |

## Source and licence

**Source:** Ville de Montreal, Actes criminels (https://donnees.montreal.ca/dataset/actes-criminels), CSV downloaded November 9, 2026. Prepared by John Khan in Toronto, Ontario. Licence: Creative Commons Attribution 4.0 International. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Creative Commons Attribution 4.0 International (City of Montréal open data)](https://creativecommons.org/licenses/by/4.0/). Source: Ville de Montréal / SPVM, under CC BY 4.0. Not an official City of Montréal product.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026montrealcriminalacts,
  author    = {Khan, John},
  title     = {Montreal criminal acts},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/montreal-criminal-acts}
}
```

APA: Khan, J. (2026). *Montreal criminal acts* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/montreal-criminal-acts

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Criminal act records published by the City of Montreal / SPVM, with offence category, date, shift, police district and coordinates.

Portal: [Actes criminels](https://donnees.montreal.ca/dataset/actes-criminels).

## Coverage

2015-01-01 to 2026-11-07 in this snapshot (364,906 rows).

## Updates

Snapshot from November 9, 2026. Not auto refreshed.

## A few numbers from this snapshot

* Incident file has 364,906 rows from 2015-01-01 to 2026-11-07.
* Categories: Vol dans / sur véhicule à moteur 103926, Introduction 85602, Méfait 78989, Vol de véhicule à moteur 74478, Vols qualifiés 21574.

## Example uses

* Map incidents by police district.
* Compare categories and shifts.
* Build simple forecasting baselines on monthly counts.

## Caveats

* These are police-reported records. Reporting practices and category labels can change.
* Coordinates can be missing or generalized.
* Category names are published in French.

## Licence

Shared under Creative Commons Attribution 4.0 International as stated on the City of Montreal open data portal. Source: Ville de Montreal / SPVM. Not an official City of Montreal product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
