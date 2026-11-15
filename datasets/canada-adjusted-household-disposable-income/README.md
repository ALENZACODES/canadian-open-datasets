<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada adjusted household disposable income" width="100%"></p>

# Canada adjusted household disposable income

*Household income plus social transfers in kind by province, 2008 to 2025*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 2008 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-adjusted-household-disposable-income](https://www.kaggle.com/datasets/johnnykhan1/canada-adjusted-household-disposable-income)

## What it is

Adjusted household disposable income for Canada, the provinces and the territories, tidied from Statistics Canada [Table 36-10-0612-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610061201). Adjusted income adds social transfers in kind, such as public health care and education that households receive without paying directly, to ordinary disposable income. The table also shows actual final consumption and household net saving.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`adjusted_household_disposable_income_annual.csv`](data/adjusted_household_disposable_income_annual.csv) | 256 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`statcan_metadata_36-10-0612.csv`](data/statcan_metadata_36-10-0612.csv) | 3 KB | in this repository |

## Columns

### `adjusted_household_disposable_income_annual.csv`

Annual household disposable income, social transfers in kind, adjusted disposable income, actual final consumption and net saving, by province or territory, from Table 36-10-0612.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `estimates` | Text | Household account line as published, for example Adjusted household disposable income. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `statcan_metadata_36-10-0612.csv`

Official Statistics Canada cube metadata shipped with Table 36-10-0612-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 36-10-0612-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610061201); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaadjustedhouseholddisposableincome,
  author    = {Khan, John},
  title     = {Canada adjusted household disposable income},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-adjusted-household-disposable-income}
}
```

APA: Khan, J. (2026). *Canada adjusted household disposable income* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-adjusted-household-disposable-income

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Adjusted household disposable income for Canada, the provinces and the territories, tidied from Statistics Canada [Table 36-10-0612-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610061201). Adjusted income adds social transfers in kind, such as public health care and education that households receive without paying directly, to ordinary disposable income. The table also shows actual final consumption and household net saving.

## Coverage

2008 to 2025, annual, millions of current dollars. In this snapshot the latest year (2025) is published for Canada only; provinces and territories run to 2024.

## Updates

Updated yearly at the source. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Adjusted household disposable income in Canada was 2.33 trillion dollars in 2025, up 3.9 percent from a year earlier.
* Adjusted household disposable income in Ontario was 863.4 billion dollars in 2024, up 8.6 percent from a year earlier.
* Social transfers in kind such as public health care and education added 528.4 billion dollars to Canada's household disposable income of 1.80 trillion dollars in 2025.
* The file has 1,890 rows for 15 geographies and 7 estimates from 2008 to 2025.

## Example uses

* Compare living standards across provinces including public services.
* Study household saving by province.
* Compute per capita adjusted income with population data.
* Show how much public services add to household resources.

## Caveats

Values are in millions of current dollars, not adjusted for inflation or population. Recent years are revised. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `adjusted_household_disposable_income_annual.csv`: Annual household disposable income, social transfers in kind, adjusted disposable income, actual final consumption and net saving, by province or territory, from Table 36-10-0612.
* `statcan_metadata_36-10-0612.csv`: Official cube metadata for Table 36-10-0612-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0612-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
