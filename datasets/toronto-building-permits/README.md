<p align="center"><img src="../../assets/theme-housing.png" alt="Toronto Building Permits 2000 to 2026" width="100%"></p>

# Toronto Building Permits 2000 to 2026

*Monthly counts with names and addresses removed*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 2000 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-building-permits](https://www.kaggle.com/datasets/johnnykhan1/toronto-building-permits)

## What it is

City of Toronto building permits from the official active-permit file and the two official cleared-permit extracts (2000 to 2016, and 2017 on), rolled up by month. The official rows include street addresses, builder names and free-text job descriptions. Those fields are not in this version. What remains is monthly counts by permit type, structure type, status and postal FSA, plus dwelling units created and lost when the City published those figures.

1,064,748 permit records after dropping names, addresses and free-text descriptions. 2000 to 2026.

The source files do not include a 158-neighbourhood identifier. The smallest geography here is the postal FSA (the first three characters of the postal code) and the City's ward grid code is not used as a neighbourhood replacement.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 99 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 7 KB | in this repository |
| [`permits_citywide_monthly.csv`](data/permits_citywide_monthly.csv) | 22 KB | in this repository |
| [`permits_monthly_by_fsa.csv`](data/permits_monthly_by_fsa.csv) | 3.8 MB | in this repository |
| [`permits_monthly_by_source.csv`](data/permits_monthly_by_source.csv) | 69 KB | in this repository |
| [`permits_monthly_by_status.csv`](data/permits_monthly_by_status.csv) | 323 KB | in this repository |
| [`permits_monthly_by_structure.csv`](data/permits_monthly_by_structure.csv) | 2.5 MB | in this repository |
| [`permits_monthly_by_type.csv`](data/permits_monthly_by_type.csv) | 852 KB | in this repository |
| `permits_monthly_detail.csv` | 56.3 MB (3.7 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/toronto-building-permits--permits_monthly_detail.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `permits_citywide_monthly.csv`

Citywide monthly permit counts and dwelling-unit sums.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month_num` | Integer | Month number from 1 to 12. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

### `permits_monthly_by_fsa.csv`

Monthly counts by postal FSA and extract.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `fsa` | Text | First three characters of the postal code, as published. |
| `source_file` | Text | Which official extract the records came from: active, cleared_2017_on, or cleared_2000_2016. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

### `permits_monthly_by_source.csv`

Monthly counts split by official extract (active, cleared since 2017, cleared 2000 to 2016).

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month_num` | Integer | Month number from 1 to 12. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `source_file` | Text | Which official extract the records came from: active, cleared_2017_on, or cleared_2000_2016. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

### `permits_monthly_by_status.csv`

Monthly counts by status and extract.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `status` | Text | Permit status as published. |
| `source_file` | Text | Which official extract the records came from: active, cleared_2017_on, or cleared_2000_2016. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

### `permits_monthly_by_structure.csv`

Monthly counts by structure type and extract.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `structure_type` | Text | Structure type as published. |
| `source_file` | Text | Which official extract the records came from: active, cleared_2017_on, or cleared_2000_2016. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

### `permits_monthly_by_type.csv`

Monthly counts by permit type and extract.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `permit_type` | Text | Permit type as published. |
| `source_file` | Text | Which official extract the records came from: active, cleared_2017_on, or cleared_2000_2016. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

### `permits_monthly_detail.csv`

Monthly counts by type, structure, status, FSA and extract.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year of the issued date, or of the application date when no issued date is present. |
| `month` | Date | Year and month (YYYY-MM) of that same date. |
| `permit_type` | Text | Permit type as published. |
| `structure_type` | Text | Structure type as published. |
| `status` | Text | Permit status as published. |
| `fsa` | Text | First three characters of the postal code, as published. |
| `source_file` | Text | Which official extract the records came from: active, cleared_2017_on, or cleared_2000_2016. |
| `permits` | Integer | Number of permit records in the group. Revisions are counted as they appear in the source. |
| `issued_permits` | Integer | Records with an issued date. |
| `completed_permits` | Integer | Records with a completed date. |
| `dwelling_units_created` | Float | Sum of dwelling units created, when published. |
| `dwelling_units_lost` | Float | Sum of dwelling units lost, when published. |

## Source and licence

**Source:** City of Toronto Open Data, Building Permits - Active Permits (https://open.toronto.ca/dataset/building-permits-active-permits/) and Building Permits - Cleared Permits (https://open.toronto.ca/dataset/building-permits-cleared-permits/). Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026torontobuildingpermits,
  author    = {Khan, John},
  title     = {Toronto Building Permits 2000 to 2026},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-building-permits}
}
```

APA: Khan, J. (2026). *Toronto Building Permits 2000 to 2026* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-building-permits

<details><summary>Full notes from the Kaggle page</summary>

## What this is

City of Toronto building permits from the official active-permit file and the two official cleared-permit extracts (2000 to 2016, and 2017 on), rolled up by month. The official rows include street addresses, builder names and free-text job descriptions. Those fields are not in this version. What remains is monthly counts by permit type, structure type, status and postal FSA, plus dwelling units created and lost when the City published those figures.

1,064,748 permit records after dropping names, addresses and free-text descriptions. 2000 to 2026.

The source files do not include a 158-neighbourhood identifier. The smallest geography here is the postal FSA (the first three characters of the postal code) and the City's ward grid code is not used as a neighbourhood replacement.

## Files

| File | What is in it |
|---|---|
| `permits_citywide_monthly.csv` | Citywide monthly totals |
| `permits_monthly_by_source.csv` | Monthly totals by official extract |
| `permits_monthly_by_type.csv` | Monthly totals by permit type |
| `permits_monthly_by_structure.csv` | Monthly totals by structure type |
| `permits_monthly_by_fsa.csv` | Monthly totals by postal FSA |
| `permits_monthly_by_status.csv` | Monthly totals by status |
| `permits_monthly_detail.csv` | Monthly totals by type, structure, status and FSA |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the annual totals |

## Coverage and refresh

Pulled on November 9, 2026. The City updates the active and recent cleared files frequently. The 2000 to 2016 cleared extract is a historical snapshot (catalogue date 2025-07-08). 2026 figures are year to date.

A permit can appear in the active file until it is cleared, and then in a cleared extract. Do not add the three source files and call the total the number of unique permits ever issued. Use `source_file` when you need to keep them apart, or use the citywide file knowing that active and cleared records are both counted in the month they were issued or applied.

The month used is the issued date when it is present, otherwise the application date.

## Caveats

* Builder names, street numbers, street names, job descriptions and estimated construction costs were dropped. Cost was dropped because many official rows contain a placeholder rather than a dollar amount.
* Dwelling unit fields are frequently blank. Treat those sums as a lower bound on what the City recorded, not a complete housing-unit census.
* FSA values are only as complete as the source postal field.
* Status labels differ between the active and cleared extracts.

## Sources

Building Permits, Active Permits: https://open.toronto.ca/dataset/building-permits-active-permits/

Building Permits, Cleared Permits: https://open.toronto.ca/dataset/building-permits-cleared-permits/

Pulled on November 9, 2026.

## Example uses

* Follow new housing-related permits and dwelling units created by FSA over time.
* Compare interior alteration volume with new construction by structure type.
* Watch how the mix of permit types changed after 2020.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). This dataset is not endorsed by the City of Toronto.

Changes made here: official rows were aggregated to monthly counts, personal names, addresses and free-text descriptions were dropped, and columns were renamed to snake_case. Counts of the remaining records were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
