<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada income of individuals by source" width="100%"></p>

# Canada income of individuals by source

*Median and average income by source, age, gender and province, 1976 to 2024*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** January 1976 to January 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-income-of-individuals-by-source](https://www.kaggle.com/datasets/johnnykhan1/canada-income-of-individuals-by-source)

## What it is

Income of individuals in Canada by source of income, tidied from Statistics Canada [Table 11-10-0239-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110023901), which comes from the Canadian Income Survey and earlier surveys. Sources include employment income, investment income, retirement income, Old Age Security and GIS, CPP and QPP, child benefits, Employment Insurance, social assistance and other transfers. Dollar values are in 2024 constant dollars.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`income_of_individuals_by_source_annual.csv`](data/income_of_individuals_by_source_annual.csv) | 19.5 MB | in this repository |
| [`statcan_metadata_11-10-0239.csv`](data/statcan_metadata_11-10-0239.csv) | 11 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `income_of_individuals_by_source_annual.csv`

Annual median income, average income and number with income by income source, for Canada, provinces and nine large cities, from Table 11-10-0239.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `age_group` | Text | Age group as published. |
| `gender` | Text | Total, Men+ or Women+, as published. |
| `income_source` | Text | Source of income as published. |
| `statistic` | Text | Median income, average income (both excluding zeros), or number with income. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Boolean | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_11-10-0239.csv`

Official Statistics Canada cube metadata shipped with Table 11-10-0239-01, including notes and the symbol legend. Layout is as published, not tidied.


## Source and licence

**Source:** Statistics Canada Table 11-10-0239-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110023901); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaincomeofindividualsbysource,
  author    = {Khan, John},
  title     = {Canada income of individuals by source},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-income-of-individuals-by-source}
}
```

APA: Khan, J. (2026). *Canada income of individuals by source* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-income-of-individuals-by-source

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Income of individuals in Canada by source of income, tidied from Statistics Canada [Table 11-10-0239-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110023901), which comes from the Canadian Income Survey and earlier surveys. Sources include employment income, investment income, retirement income, Old Age Security and GIS, CPP and QPP, child benefits, Employment Insurance, social assistance and other transfers. Dollar values are in 2024 constant dollars.

## Coverage

1976 to 2024, annual. Two slices of the source table: (1) every geography (Canada, regions, provinces, and nine census metropolitan areas including Toronto) for all people aged 15 and older, all genders; (2) Canada by every age group and gender. Statistics kept: median income, average income and number with income.

## Updates

Statistics Canada adds a new reference year each spring. Snapshot taken on November 13, 2026.

## A few numbers from this snapshot

* Median total income of Canadians aged 15 and older with income was 46,300 dollars in 2024, in 2024 constant dollars, about flat from a year earlier.
* Median total income in Toronto (census metropolitan area) was 44,400 dollars in 2024.
* Median total income in Ontario was 45,700 dollars in 2024.
* Median total income in Alberta was 48,100 dollars in 2024.
* For people aged 65 and older the national median was 39,200 dollars in 2024.
* The file has 98,856 rows covering 25 geographies, 16 income sources and three statistics, from 1976 to 2024.

## Example uses

* Track real income growth by source since 1976.
* Compare how much seniors rely on OAS, GIS and CPP.
* Compare income levels across provinces and big cities like Toronto.
* Study the gender income gap over time.

## Caveats

Estimates come from sample surveys and carry sampling error; small groups are less reliable. Medians and averages exclude people with zero income from that source. Survey methods changed in 1996 and 2012, so compare long runs with care. Empty values mean no figure was published; see status and symbol.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `income_of_individuals_by_source_annual.csv`: Annual median income, average income and number with income by income source, for Canada, provinces and nine large cities, from Table 11-10-0239.
* `statcan_metadata_11-10-0239.csv`: Official cube metadata for Table 11-10-0239-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 11-10-0239-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
