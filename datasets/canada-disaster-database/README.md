<p align="center"><img src="../../assets/theme-environment.png" alt="Canadian Disaster Database" width="100%"></p>

# Canadian Disaster Database

*Historical disaster events across Canada from Public Safety*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 10 January 1900 to 22 December 2022 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-disaster-database](https://www.kaggle.com/datasets/johnnykhan1/canada-disaster-database)

## What it is

Historical disaster events in Canada from the Canadian Disaster Database (CDD), including category, dates, impacts and cost fields when reported.

Portal: [Canadian Disaster Database](https://open.canada.ca/data/en/dataset/1c3d15f9-9cfa-4010-8462-0d67e493d9b9).

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`canadian_disasters.csv`](data/canadian_disasters.csv) | 2.2 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |

## Columns

### `canadian_disasters.csv`

Canadian Disaster Database event extract (English).

| Column | Type | Description |
|---|---|---|
| `event_id` | Float | Unique event identifier in the Canadian Disaster Database. |
| `event_category_name` | Text | High-level event category. |
| `event_group_name` | Text | Event group. |
| `event_subgroup_name` | Text | Event subgroup. |
| `event_type` | Text | Event type code or label. |
| `event_type_description` | Text | Event type description. |
| `magnitude` | Float | Magnitude when applicable (for example earthquake magnitude). |
| `event_start_date` | Date | Event start date. |
| `event_end_date` | Date | Event end date. |
| `injured` | Float | Number of people injured when reported. |
| `dead` | Float | Number of deaths when reported. |
| `evacuated` | Float | Number of people evacuated when reported. |
| `place` | Text | Place description as published. |
| `comment` | Text | Event comments as published. |
| `total_cost` | Float | Total estimated cost when reported. |
| `ogd_costs` | Float | ogd costs as published in the CDD extract. |
| `municipal_costs` | Float | municipal costs as published in the CDD extract. |
| `fed_dfaa_payments` | Float | fed dfaa payments as published in the CDD extract. |
| `prov_dfaa_payments` | Float | prov dfaa payments as published in the CDD extract. |
| `prov_dept_payments` | Float | prov dept payments as published in the CDD extract. |
| `insurance_payments` | Float | insurance payments as published in the CDD extract. |
| `ngo_payments` | Float | ngo payments as published in the CDD extract. |
| `utility_people_affected` | Float | utility people affected as published in the CDD extract. |
| `geog_obj` | Text | geog obj as published in the CDD extract. |
| `provinces_affected_provinces_affect_es` | Text | provinces affected provinces affect es as published in the CDD extract. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

## Source and licence

**Source:** Public Safety Canada, Canadian Disaster Database extract (https://open.canada.ca/data/en/dataset/1c3d15f9-9cfa-4010-8462-0d67e493d9b9), downloaded November 9, 2026. Prepared by John Khan in Toronto, Ontario. Open Government Licence – Canada. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadadisasterdatabase,
  author    = {Khan, John},
  title     = {Canadian Disaster Database},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-disaster-database}
}
```

APA: Khan, J. (2026). *Canadian Disaster Database* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-disaster-database

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Historical disaster events in Canada from the Canadian Disaster Database (CDD), including category, dates, impacts and cost fields when reported.

Portal: [Canadian Disaster Database](https://open.canada.ca/data/en/dataset/1c3d15f9-9cfa-4010-8462-0d67e493d9b9).

## Coverage

CDD English extract as published (file dated 2022 on the portal). 1,490 events in this snapshot.

## Updates

Snapshot from November 9, 2026. Not auto refreshed.

## A few numbers from this snapshot

* The extract has 1,490 disaster events.
* Date range (start): 1900-01-10 to 2022-12-22.
* Most common category in this snapshot: Disaster (1053 events).

## Example uses

* Summarize disasters by province and category.
* Study reported costs and evacuations over time.
* Join to weather or hazard layers for research.

## Caveats

* Cost and impact fields are often missing. Absence of a number is not proof of zero impact.
* Event geography can span multiple provinces.
* Definitions and collection practices change over a long historical record.

## Licence

Shared under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Public Safety Canada. Not an official Public Safety product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
