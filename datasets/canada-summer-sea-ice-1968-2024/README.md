<p align="center"><img src="../../assets/theme-environment.png" alt="Canada summer sea ice area 1968 to 2024" width="100%"></p>

# Canada summer sea ice area 1968 to 2024

*Canadian Ice Service summer and September ice area by region*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1968 to 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-summer-sea-ice-1968-2024](https://www.kaggle.com/datasets/johnnykhan1/canada-summer-sea-ice-1968-2024)

## What it is

Canadian Environmental Sustainability Indicators (CESI) sea ice area tables for 1968 to 2024, tidied into a long CSV. The values come from weekly regional ice charts in the Canadian Ice Service Digital Archive and were compiled by Environment and Climate Change Canada's Climate Research Division. The Northern Canadian Waters total series and the Northwest Passage routes are also saved as smaller companion files.

Source dataset: [Sea ice in Canada](https://open.canada.ca/data/en/dataset/8ca062f1-edef-48d8-91ac-7ff236ffd9e8) (Environment and Climate Change Canada, CESI, based on the Canadian Ice Service Digital Archive).

English CSV tables were pulled on November 9, 2026 from https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/sea-ice/2025/

Indicator page: https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/sea-ice.html

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 84 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`northern_canadian_waters_summer_total.csv`](data/northern_canadian_waters_summer_total.csv) | 2 KB | in this repository |
| [`northwest_passage_summer.csv`](data/northwest_passage_summer.csv) | 25 KB | in this repository |
| [`sea_ice_area_long.csv`](data/sea_ice_area_long.csv) | 182 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `northern_canadian_waters_summer_total.csv`

Average summer total sea ice area in the Northern Canadian Waters (figure 1).

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the summer or September ice area value. |
| `sea_ice_area` | Float | Average summer sea ice area in the Northern Canadian Waters, as published (millions of square kilometres). |
| `area_unit` | Text | Unit as published: millions of square kilometres for the Northern Canadian Waters total series, and thousands of square kilometres for the sub-region, multi-year and Northwest Passage series. |

### `northwest_passage_summer.csv`

Average summer total and multi-year sea ice area on the northern and southern Northwest Passage routes (figure 7).

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the summer or September ice area value. |
| `domain` | Text | Grouping used in the CESI tables: Northern Canadian Waters, Canadian Arctic domain, or Northwest Passage. |
| `region` | Text | Region or route name as published, with the unit text removed from the column title. |
| `season` | Text | summer (25 June to 15 October for the Canadian Arctic domain, as described by CESI) or September. |
| `ice_type` | Text | total sea ice or multi-year sea ice (ice that has survived at least one summer melt). |
| `area` | Float | Sea ice area in the unit given in area_unit. |
| `area_unit` | Text | Unit as published: millions of square kilometres for the Northern Canadian Waters total series, and thousands of square kilometres for the sub-region, multi-year and Northwest Passage series. |

### `sea_ice_area_long.csv`

Tidy long file of CESI sea ice area series, 1968 to 2024.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Calendar year of the summer or September ice area value. |
| `domain` | Text | Grouping used in the CESI tables: Northern Canadian Waters, Canadian Arctic domain, or Northwest Passage. |
| `region` | Text | Region or route name as published, with the unit text removed from the column title. |
| `season` | Text | summer (25 June to 15 October for the Canadian Arctic domain, as described by CESI) or September. |
| `ice_type` | Text | total sea ice or multi-year sea ice (ice that has survived at least one summer melt). |
| `area` | Float | Sea ice area in the unit given in area_unit. |
| `area_unit` | Text | Unit as published: millions of square kilometres for the Northern Canadian Waters total series, and thousands of square kilometres for the sub-region, multi-year and Northwest Passage series. |

## Source and licence

**Source:** Environment and Climate Change Canada, Canadian Environmental Sustainability Indicators, Sea ice in Canada, https://open.canada.ca/data/en/dataset/8ca062f1-edef-48d8-91ac-7ff236ffd9e8. Based on the Canadian Ice Service Digital Archive. English CSVs from https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/sea-ice/2025/ downloaded on November 9, 2026. Indicator page: https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/sea-ice.html. Prepared by John Khan in Toronto, Ontario. Contains information licensed under the Open Government Licence – Canada, https://open.canada.ca/en/open-government-licence-canada.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadasummerseaice19682024,
  author    = {Khan, John},
  title     = {Canada summer sea ice area 1968 to 2024},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-summer-sea-ice-1968-2024}
}
```

APA: Khan, J. (2026). *Canada summer sea ice area 1968 to 2024* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-summer-sea-ice-1968-2024

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canadian Environmental Sustainability Indicators (CESI) sea ice area tables for 1968 to 2024, tidied into a long CSV. The values come from weekly regional ice charts in the Canadian Ice Service Digital Archive and were compiled by Environment and Climate Change Canada's Climate Research Division. The Northern Canadian Waters total series and the Northwest Passage routes are also saved as smaller companion files.

Source dataset: [Sea ice in Canada](https://open.canada.ca/data/en/dataset/8ca062f1-edef-48d8-91ac-7ff236ffd9e8) (Environment and Climate Change Canada, CESI, based on the Canadian Ice Service Digital Archive).

English CSV tables were pulled on November 9, 2026 from https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/sea-ice/2025/

Indicator page: https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/sea-ice.html

## Coverage

1,824 rows from 1968 through 2024. Series include average summer total sea ice in the Northern Canadian Waters and its sub-regions, September total sea ice in the Canadian Arctic domain, summer and September multi-year ice, and summer total and multi-year ice on the northern and southern routes of the Northwest Passage. Summer for the Canadian Arctic domain is defined by CESI as 25 June to 15 October. Area units are kept as published: millions of square kilometres for the Northern Canadian Waters total, and thousands of square kilometres for the other series.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. CESI updates the sea ice indicators when a new summer season is added. For later years, use the Open Government portal page or the indicator page above.

## A few numbers from this snapshot

* The tables run from 1968 through 2024.
* Average summer sea ice area in the Northern Canadian Waters was 1.26 million square kilometres in 1968 and 0.74 million square kilometres in 2024.

## Example uses

* Plot the long summer ice series for northern Canadian waters.
* Compare sub-regions such as Hudson Bay and the Beaufort Sea.
* Track multi-year ice in the Canadian Arctic domain or on the Northwest Passage routes.

## Caveats

These are seasonal area indicators, not daily ice charts. Sub-region values are in thousands of square kilometres and the Northern Canadian Waters total is in millions; do not add series that use different units. Multi-year ice is ice that has survived at least one summer melt, as defined by CESI. Values incorporate satellite data, surface observations, aircraft and ship reports, model results and ice forecaster expertise, as described in the CESI methods. This is not an official Government of Canada product and Environment and Climate Change Canada does not endorse it.

## Files

* `sea_ice_area_long.csv`: Tidy long file of CESI sea ice area series, 1968 to 2024.
* `northern_canadian_waters_summer_total.csv`: Average summer total sea ice area in the Northern Canadian Waters (figure 1).
* `northwest_passage_summer.csv`: Average summer total and multi-year sea ice area on the northern and southern Northwest Passage routes (figure 7).
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, Canadian Environmental Sustainability Indicators, Sea ice in Canada, based on the Canadian Ice Service Digital Archive. The published values were not changed. Column titles were split into tidy fields. Environment and Climate Change Canada does not endorse this upload.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
