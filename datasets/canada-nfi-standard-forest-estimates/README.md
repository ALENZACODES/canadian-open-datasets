<p align="center"><img src="../../assets/theme-environment.png" alt="Canada NFI standard forest estimates" width="100%"></p>

# Canada NFI standard forest estimates

*Official area, volume, biomass and carbon tables, 2000 to 2017*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 2000 to 2017 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-nfi-standard-forest-estimates](https://www.kaggle.com/datasets/johnnykhan1/canada-nfi-standard-forest-estimates)

## What it is

A tidy extract of the official National Forest Inventory (NFI) standard statistical reports for Canada: area, tree volume, above-ground biomass and above-ground carbon, with official relative standard errors and confidence intervals when those companion files were published. The reports cover the baseline cycle (2000 to 2006) and the first remeasurement cycle (2007 to 2017), plus official annual change estimates from the first remeasurement reports.

Source: [NFI standard reports](https://nfi.nfis.org/en/standardreports) (Natural Resources Canada). The same NFI program is documented on the Open Government Portal under [Canada's National Forest Inventory Photo Plot Data](https://open.canada.ca/data/en/dataset/6433173f-bca8-44e6-be8e-3e8a19d3c299) and [Canada's National Forest Inventory Ground Plot Data](https://open.canada.ca/data/en/dataset/35c3556c-e48d-41a7-ac50-652257b0a8e8). Official English CSV files were downloaded from nfi.nfis.org on November 9, 2026. This extract uses the public standard reports only. Raw plot data that require an NFI data request are not included.

This is a different product from the National Forestry Database wildfire area-burned tables already on Kaggle. Those tables count fires. These tables estimate forest area, volume, biomass and carbon from the NFI sample.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_national_highlights.csv`](data/canada_national_highlights.csv) | 3 KB | in this repository |
| [`cover.png`](data/cover.png) | 54 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 6 KB | in this repository |
| [`nfi_standard_estimates.csv`](data/nfi_standard_estimates.csv) | 22.2 MB | in this repository |
| [`source_files.csv`](data/source_files.csv) | 155 KB | in this repository |

## Columns

### `canada_national_highlights.csv`

Selected official Canada-wide figures from the national standard reports, for quick reference.

| Column | Type | Description |
|---|---|---|
| `report_cycle` | Text | Official report cycle: baseline (2000 to 2006) or first_remeasurement (2007 to 2017). |
| `cycle_years` | Text | Official years named on the NFI standard reports page for that cycle. |
| `indicator` | Text | Short label for a selected official national figure. |
| `table_id` | Text | Official NFI table number from the file name, such as t4 or t19. |
| `unit` | Text | Unit of value and of confidence_interval, taken from the official title: thousand hectares, million cubic metres, or million tonnes. |
| `value` | Float | Official published figure, copied as text from the source CSV. Official placeholders None and hyphen are stored blank. |
| `relative_standard_error_percent` | Float | Official relative standard error in percent, when an official SE file exists for that table. Blank when no official SE file was published or the official cell was a placeholder. |
| `confidence_interval` | Float | Official confidence interval half-width in the same unit as value, when an official CI file exists. This is the amount published in the NFI CI table, not a separately computed bound. Blank when no official CI file was published. |
| `estimate_source_file` | Text | Relative path of the official estimate CSV under the NFI summaries tree. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, number or integer). |
| `description` | Text | What the column contains. |

### `nfi_standard_estimates.csv`

Tidy long-format extract of official NFI standard report estimates, relative standard errors and confidence intervals.

| Column | Type | Description |
|---|---|---|
| `report_cycle` | Text | Official report cycle: baseline (2000 to 2006) or first_remeasurement (2007 to 2017). |
| `cycle_years` | Text | Official years named on the NFI standard reports page for that cycle. |
| `report_family` | Text | Official report family: baseline reports, first remeasurement reports, or forest change estimate reports. |
| `geography_type` | Text | Geographic population of the official report: Canada, terrestrial ecozone, boreal zone, or managed forest region. |
| `geography` | Text | Official geography label. Canada national tables are labelled Canada. Ecozone, boreal and managed-forest tables use the official row label, including a Canada total row when the official table has one. |
| `table_id` | Text | Official NFI table number from the file name, such as t4 or t19. |
| `table_title` | Text | Official English title from the first line of the source CSV, with HTML tags removed. |
| `unit` | Text | Unit of value and of confidence_interval, taken from the official title: thousand hectares, million cubic metres, or million tonnes. |
| `measure` | Text | estimate for a stock or area in that cycle, or annual_change for the official annual change reports. |
| `class_dimension` | Text | Name of the official class column when present, such as Forest type, Species Group or IUCN category. Empty when the official table has no class column. |
| `class_value` | Text | Official class label, when a class column is present. |
| `variable` | Text | Official column header of the cell, such as an age class, ownership class, or Forest land. |
| `value` | Float | Official published figure, copied as text from the source CSV. Official placeholders None and hyphen are stored blank. |
| `relative_standard_error_percent` | Float | Official relative standard error in percent, when an official SE file exists for that table. Blank when no official SE file was published or the official cell was a placeholder. |
| `confidence_interval` | Text | Official confidence interval half-width in the same unit as value, when an official CI file exists. This is the amount published in the NFI CI table, not a separately computed bound. Blank when no official CI file was published. |
| `estimate_source_file` | Text | Relative path of the official estimate CSV under the NFI summaries tree. |
| `se_source_file` | Text | Relative path of the official relative standard error CSV, when present. |
| `ci_source_file` | Text | Relative path of the official confidence interval CSV, when present. |

### `source_files.csv`

Catalogue of official NFI CSV files linked from the standard reports page, including files that returned HTTP 404.

| Column | Type | Description |
|---|---|---|
| `cycle` | Text | NFI path cycle code, t0 or t1. |
| `cycle_years` | Text | Official years named on the NFI standard reports page for that cycle. |
| `geography_type` | Text | Geographic population of the official report: Canada, terrestrial ecozone, boreal zone, or managed forest region. |
| `table_id` | Text | Official NFI table number from the file name, such as t4 or t19. |
| `measure` | Text | estimate for a stock or area in that cycle, or annual_change for the official annual change reports. |
| `statistic` | Text | Kind of official file: value, relative_standard_error_percent, or confidence_interval. |
| `official_title` | Text | Official English title from the first line of that source CSV. |
| `official_file` | Text | Relative path of the official CSV under the NFI summaries tree. |
| `official_url` | Text | Direct official download URL on nfi.nfis.org. |
| `n_cells` | Integer | Number of official data cells read from that file. |
| `bytes` | Integer | File size in bytes as downloaded. |
| `sha256` | Text | SHA256 of the official file as downloaded on November 9, 2026. Empty for files that returned HTTP 404. |
| `download_status` | Text | ok if the official file was downloaded, or http_404 if the standard reports page linked to a file that was not available. |

## Source and licence

**Source:** Natural Resources Canada, National Forest Inventory standard statistical reports, https://nfi.nfis.org/en/standardreports. Official English CSV files downloaded from https://nfi.nfis.org/resources/general/summaries/ on November 9, 2026. Open Government Portal records: Canada's National Forest Inventory Photo Plot Data, https://open.canada.ca/data/en/dataset/6433173f-bca8-44e6-be8e-3e8a19d3c299, and Canada's National Forest Inventory Ground Plot Data, https://open.canada.ca/data/en/dataset/35c3556c-e48d-41a7-ac50-652257b0a8e8. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadanfistandardforestestimates,
  author    = {Khan, John},
  title     = {Canada NFI standard forest estimates},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-nfi-standard-forest-estimates}
}
```

APA: Khan, J. (2026). *Canada NFI standard forest estimates* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-nfi-standard-forest-estimates

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of the official National Forest Inventory (NFI) standard statistical reports for Canada: area, tree volume, above-ground biomass and above-ground carbon, with official relative standard errors and confidence intervals when those companion files were published. The reports cover the baseline cycle (2000 to 2006) and the first remeasurement cycle (2007 to 2017), plus official annual change estimates from the first remeasurement reports.

Source: [NFI standard reports](https://nfi.nfis.org/en/standardreports) (Natural Resources Canada). The same NFI program is documented on the Open Government Portal under [Canada's National Forest Inventory Photo Plot Data](https://open.canada.ca/data/en/dataset/6433173f-bca8-44e6-be8e-3e8a19d3c299) and [Canada's National Forest Inventory Ground Plot Data](https://open.canada.ca/data/en/dataset/35c3556c-e48d-41a7-ac50-652257b0a8e8). Official English CSV files were downloaded from nfi.nfis.org on November 9, 2026. This extract uses the public standard reports only. Raw plot data that require an NFI data request are not included.

This is a different product from the National Forestry Database wildfire area-burned tables already on Kaggle. Those tables count fires. These tables estimate forest area, volume, biomass and carbon from the NFI sample.

## Coverage

53,512 tidy rows, of which 41,403 are official cycle estimates and 12,109 are official annual change figures, drawn from 357 official CSV files. The standard reports page also linked to 70 files that returned HTTP 404 on November 9, 2026: the baseline (2000 to 2006) managed forest region reports, and the boreal zone annual change reports (except the boreal carbon change table, which was available). Those missing files are listed in source_files.csv and are not estimated here.

In the first remeasurement national reports, forest land in Canada is 369,019.352 thousand hectares, with an official relative standard error of 0.41 percent. Official above-ground carbon is 16,290.412 million tonnes (relative standard error 0.92 percent). Official land cover, including water, totals 735,778.650 thousand hectares, of which 377,210.243 thousand hectares is treed. Forest land by official ownership in that national table: Federal 6,138.743 thousand hectares, Provincial 279,394.240 thousand hectares, Territorial 47,281.665 thousand hectares, Municipal 973.069 thousand hectares, Aboriginal 7,719.113 thousand hectares, Private 24,548.263 thousand hectares, Other 2,964.259 thousand hectares.

In the baseline national reports (2000 to 2006), forest land is 347,575.76 thousand hectares and above-ground carbon is 16,353.268 million tonnes.

The official national annual change reports give 512.608 thousand hectares per year for forest land and -2.322 million tonnes per year for above-ground carbon. Among terrestrial ecozones in the first remeasurement carbon table, Boreal Shield has the largest official above-ground carbon, 4,595.365 million tonnes.

Reports are also published for terrestrial ecozones, the boreal zone, and managed forest regions. The official NFI page notes that the boreal zone and forest management region reports are slightly different populations for statistical estimation, and will have minor differences relative to the national and terrestrial ecozone reports. Official Canada totals therefore can differ across those report families. Managed forest regions are identified by the official numeric codes in the source files; this extract does not add names that are not in those files.

## Updates

This upload is a snapshot of the official standard reports pulled on November 9, 2026, and is not refreshed on a schedule. NFI states that summary reports are periodically updated and improved as new data become available. For a later extract, use the official standard reports page.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Each official wide table was turned into one row per published cell. Official relative standard error and confidence interval files were joined to the matching estimate cells. Official placeholders None and a lone hyphen are stored as blank cells. HTML tags in a few official titles (for IUCN footnotes) were removed. No figures were interpolated, and missing official files were not filled in.

The official confidence interval files publish a single number for each cell. That number is the official interval half-width in the same unit as the estimate (the amount to add and subtract), not a lower or upper bound written out as two columns.

## A few numbers from this snapshot

* First remeasurement forest land in the national reports: 369,019.352 thousand hectares.
* First remeasurement above-ground carbon in the national reports: 16,290.412 million tonnes.
* Official national annual change in forest land: 512.608 thousand hectares per year.

## Example uses

* Compare official forest land and carbon between the baseline and first remeasurement national reports, keeping the two cycles as published.
* Chart official above-ground carbon by terrestrial ecozone, including the official relative standard errors.
* Review official annual change in volume or biomass by forest type and age class, without treating those change figures as a simple subtraction of the two stock tables.

## Caveats

Baseline estimates, first remeasurement estimates, and official annual change estimates are separate official products. Do not assume that the later stock equals the earlier stock plus annual change times the number of years. The official change reports have their own methods and uncertainty, and the official populations are not always identical.

Canada totals from the boreal zone reports and the managed forest region reports can differ from the national and ecozone Canada totals for the reason NFI gives on the reports page: they are slightly different populations for statistical estimation.

Official cells may be blank (placeholders None or a hyphen in the source). Some age classes and IUCN or ownership combinations have large official relative standard errors, sometimes 100 percent. Those cells are kept as published.

IUCN categories appear as official codes (NA, IA, IB, II, III, IV, V, VI, OTHER). Ownership wording differs between cycles: the baseline national ownership table uses Aboriginal, and the first remeasurement national table uses Indigenous. Both words are kept as published.

Raw NFI plot data are not in this extract. They are requested through the official NFI data request process.

## Licence

Contains information licensed under the [Open Government Licence Canada](https://open.canada.ca/en/open-government-licence-canada). Credit: National Forest Inventory, Natural Resources Canada, standard statistical reports, https://nfi.nfis.org/en/standardreports.

## Files

* `nfi_standard_estimates.csv`: one row per official published cell, with joined official standard errors and confidence intervals when those files exist.
* `canada_national_highlights.csv`: a short list of official Canada-wide figures from the national reports.
* `source_files.csv`: every official CSV linked from the standard reports page, with URL, size, SHA256, and download status.
* `data_dictionary.csv`: column dictionary.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
