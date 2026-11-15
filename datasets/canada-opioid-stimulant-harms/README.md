<p align="center"><img src="../../assets/theme-health.png" alt="Canada opioid and stimulant harms" width="100%"></p>

# Canada opioid and stimulant harms

*Official death and EMS figures, 2016 to early 2026*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** January 2016 to September 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-opioid-stimulant-harms](https://www.kaggle.com/datasets/johnnykhan1/canada-opioid-stimulant-harms)

## What it is

Official opioid and stimulant death and emergency medical services figures in Canada, tidied from the Public Health Agency of Canada [open data file](https://open.canada.ca/data/en/dataset/1092497d-6c72-4e66-930b-9d6337e64af5). Hospitalisation and emergency department measures were collected by the Canadian Institute for Health Information and are not included in this package. Each row keeps its official unit, period, suppression flag and the source as-of date.

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 2 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 58 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`source_readme.txt`](data/source_readme.txt) | 1 KB | in this repository |
| [`substance_harms_deaths_ems.csv`](data/substance_harms_deaths_ems.csv) | 1.9 MB | in this repository |

## Columns

### `SOURCE_MANIFEST.csv`

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | — |
| `title` | Text | — |
| `url` | Text | — |
| `licence` | Text | — |
| `release_date` | Date | — |
| `retrieval_date` | Date | — |
| `file_name` | Text | — |
| `checksum_sha256` | Text | — |
| `notes` | Text | — |

### `data_dictionary.csv`

| Column | Type | Description |
|---|---|---|
| `column` | Text | — |
| `file` | Text | — |
| `type` | Text | — |
| `description` | Text | — |

### `substance_harms_deaths_ems.csv`

| Column | Type | Description |
|---|---|---|
| `substance` | Text | Opioids or Stimulants, as published. |
| `metric` | Text | Deaths or Emergency Medical Services (EMS), as published. Hospitalisation and emergency department measures are not in this package. |
| `specific_measure` | Text | Breakdown as published, including overall numbers, age, sex and intent. |
| `region` | Text | Canada, a province or territory, or a sub-provincial region as published. |
| `pruid` | Text | Standard geographic identifier as published in the source file. |
| `time_period` | Text | By year or by quarter, as published. |
| `year_quarter` | Text | Year or year and quarter label as published, including 2026 (Jan to Mar). |
| `aggregator` | Text | Additional grouping label as published. |
| `disaggregator` | Text | Additional split label as published. |
| `unit` | Text | Crude rate, number or percent, as published. |
| `value_published` | Text | Value exactly as published, including the Suppr. flag. |
| `value` | Float | Numeric value. Empty when the published cell is Suppr. or otherwise non numeric. |
| `suppressed` | Boolean | True when the published value is Suppr. |
| `year` | Integer | Calendar year taken from the start of the year_quarter label. For 2026 (Jan to Mar) this is 2026, but the figure is only the first quarter. |
| `is_partial_period` | Boolean | True when the published period is a quarter or a partial year such as 2026 (Jan to Mar). Those rows should not be read as a full calendar year. |
| `as_of_date` | Date | Source README date for the national figures: 12 August 2026, written as 2026-08-12. |
| `file_updated_date` | Date | Source README last updated date: 22 September 2026, written as 2026-09-22. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |

## Source and licence

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaopioidstimulantharms,
  author    = {Khan, John},
  title     = {Canada opioid and stimulant harms},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-opioid-stimulant-harms}
}
```

APA: Khan, J. (2026). *Canada opioid and stimulant harms* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-opioid-stimulant-harms

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Official opioid and stimulant death and emergency medical services figures in Canada, tidied from the Public Health Agency of Canada [open data file](https://open.canada.ca/data/en/dataset/1092497d-6c72-4e66-930b-9d6337e64af5). Hospitalisation and emergency department measures were collected by the Canadian Institute for Health Information and are not included in this package. Each row keeps its official unit, period, suppression flag and the source as-of date.

## Coverage

2016 to the first quarter of 2026 as published, Canada, the provinces and the territories, with a few sub-provincial regions. Deaths and EMS only.

## Updates

This upload is a snapshot downloaded on 15 November 2026. The source README is dated 22 September 2026 and cites data reported as of 12 August 2026.

## A few numbers from this snapshot

* This package keeps 13,100 official rows for deaths and emergency medical services, matching that subset of the source file. 20,150 hospitalisation and emergency department rows were omitted because those measures were collected by the Canadian Institute for Health Information and provided to the Public Health Agency of Canada, and a separate clearance to redistribute that Institute product was not obtained.
* In 2025, the official crude rate of opioid-related deaths in Canada was 13.7 per 100,000, as published. That is the latest complete calendar year in the file.
* The same official line was 7.8 per 100,000 in 2016.
* National figures are based on data reported as of 12 August 2026, according to the source README. The file was last updated 22 September 2026.

## Example uses

* Track official opioid and stimulant death rates, using complete calendar years separately from partial periods.
* Compare EMS figures with death figures without mixing units or metrics.
* See the official as-of date on every row.

## Caveats

Hospitalisation and emergency department measures are omitted, as explained in the methods note. The source cautions that case identification, reporting and available periods differ across jurisdictions. See the source technical notes if they remain available at the URL given in the README. 2026 (Jan to Mar) is a partial period and is flagged. Suppressed cells are flagged and left empty in the numeric column.

## Files

* `substance_harms_deaths_ems.csv`: Official opioid and stimulant death and EMS figures, with units, period, suppression flags, a partial-period flag, and the source as-of date. Hospitalisation and emergency department measures are not included.
* `source_readme.txt`: Source README from the Agency download, including the as-of date.
* `SOURCE_MANIFEST.csv`: Source identifier, dates, retrieval date and checksum.
* `data_dictionary.csv`: Column dictionary.
* `METHODS.md`: Methods note, including the hospital and ED omission.
* `CITATION.txt`: Suggested citation, with DOI pending.

## Licence

This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Public Health Agency of Canada, SubstanceHarmsData.csv (deaths and EMS measures only). This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.

Suggested citation: John Khan. 2026. Canada opioid and stimulant harms [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-opioid-stimulant-harms. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
