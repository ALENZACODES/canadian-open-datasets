<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada labour productivity by province" width="100%"></p>

# Canada labour productivity by province

*Output per hour, hours worked, jobs and value added by industry, 2011 on*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 2011 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-labour-productivity-by-province](https://www.kaggle.com/datasets/johnnykhan1/canada-labour-productivity-by-province)

## What it is

Annual labour productivity and related measures for every province and territory, tidied from Statistics Canada [Table 36-10-0713-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610071301). Includes real value added per hour worked, hours, jobs, compensation, unit labour cost and labour share.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`labour_productivity_by_province_industry_annual.csv`](data/labour_productivity_by_province_industry_annual.csv) | 8.5 MB | in this repository |
| [`statcan_metadata_36-10-0713.csv`](data/statcan_metadata_36-10-0713.csv) | 24 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `labour_productivity_by_province_industry_annual.csv`

Annual labour productivity, real and nominal value added, hours worked, jobs, compensation, unit labour cost and labour share, by province or territory and industry sector, from Table 36-10-0713.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `measure` | Text | Productivity or related measure as published. |
| `naics` | Text | Industry sector or aggregate with its code in brackets. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Date | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_36-10-0713.csv`

Official Statistics Canada cube metadata shipped with Table 36-10-0713-01, including notes and the symbol legend. Layout is as published, not tidied.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official table title. |
| `Product Id` | Text | Statistics Canada product identifier for the table. |
| `CANSIM Id` | Text | Former CANSIM identifier for the table. |
| `URL` | Text | Link to the table on the Statistics Canada website. |
| `Cube Notes` | Text | Note numbers that apply to the whole table. |
| `Archive Status` | Text | Whether the table is current or archived. |
| `Frequency` | Text | Release frequency of the table. |
| `Start Reference Period` | Text | First reference period in the table. |
| `End Reference Period` | Date | Last reference period in the table at download time. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

## Source and licence

**Source:** Statistics Canada Table 36-10-0713-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610071301); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadalabourproductivitybyprovince,
  author    = {Khan, John},
  title     = {Canada labour productivity by province},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-labour-productivity-by-province}
}
```

APA: Khan, J. (2026). *Canada labour productivity by province* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-labour-productivity-by-province

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Annual labour productivity and related measures for every province and territory, tidied from Statistics Canada [Table 36-10-0713-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610071301). Includes real value added per hour worked, hours, jobs, compensation, unit labour cost and labour share.

## Coverage

2011 to 2025, annual. Kept: all two digit NAICS sectors plus the all industries, goods and services aggregates; detailed sub industries from the source were left out to keep the file small.

## Updates

Updated yearly at the source. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Labour productivity in Canada was 65.00 dollars of real value added per hour worked in 2025, up 1.7 percent from a year earlier.
* Labour productivity in Ontario was 64.00 dollars of real value added per hour worked in 2025, up 1.6 percent from a year earlier.
* Labour productivity in Alberta was 78.30 dollars of real value added per hour worked in 2025, up 1.8 percent from a year earlier.
* Canada had 21,146,255 jobs in 2025, about flat from a year earlier.
* The file has 51,750 rows for 15 geographies, 23 industry groups and 10 measures, from 2011 to 2025.

## Example uses

* Explain Canada's productivity gap by province and sector.
* Compare hours worked per job across provinces.
* Track jobs and real value added by industry.
* Join with GDP and wage data for growth accounting.

## Caveats

In this release the compensation, compensation per hour, unit labour cost and labour share rows are published empty for the industry groups kept here, so they have no values in this file. Measures have different units and scales (dollars, hours, jobs, percent; units, thousands or millions); always check unit_of_measure and scalar_factor. Empty values mean no figure was published, often for confidentiality.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `labour_productivity_by_province_industry_annual.csv`: Annual labour productivity, real and nominal value added, hours worked, jobs, compensation, unit labour cost and labour share, by province or territory and industry sector, from Table 36-10-0713.
* `statcan_metadata_36-10-0713.csv`: Official cube metadata for Table 36-10-0713-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0713-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
