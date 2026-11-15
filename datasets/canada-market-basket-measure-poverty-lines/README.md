<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada Market Basket Measure poverty lines" width="100%"></p>

# Canada Market Basket Measure poverty lines

*Official poverty thresholds by region and family size, 2002 to 2025*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 2002 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-market-basket-measure-poverty-lines](https://www.kaggle.com/datasets/johnnykhan1/canada-market-basket-measure-poverty-lines)

## What it is

Canada's Official Poverty Line thresholds, tidied from Statistics Canada [Table 11-10-0104-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110010401). The Market Basket Measure is the cost of a basket of food, clothing, shelter, transportation and other needs for a reference family in each of 66 regions. A family is below the line when its disposable income is under the threshold for its region and size.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`mbm_thresholds_by_region_family_size.csv`](data/mbm_thresholds_by_region_family_size.csv) | 3.2 MB | in this repository |
| [`statcan_metadata_11-10-0104.csv`](data/statcan_metadata_11-10-0104.csv) | 7 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `mbm_thresholds_by_region_family_size.csv`

Annual Market Basket Measure thresholds in current dollars by MBM region, base year and family size, from Table 11-10-0104.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `mbm_base` | Text | Base year of the Market Basket Measure methodology. |
| `family_size` | Text | Family size the threshold applies to. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Integer | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Date | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_11-10-0104.csv`

Official Statistics Canada cube metadata shipped with Table 11-10-0104-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 11-10-0104-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110010401); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadamarketbasketmeasurepovertylines,
  author    = {Khan, John},
  title     = {Canada Market Basket Measure poverty lines},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-market-basket-measure-poverty-lines}
}
```

APA: Khan, J. (2026). *Canada Market Basket Measure poverty lines* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-market-basket-measure-poverty-lines

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada's Official Poverty Line thresholds, tidied from Statistics Canada [Table 11-10-0104-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110010401). The Market Basket Measure is the cost of a basket of food, clothing, shelter, transportation and other needs for a reference family in each of 66 regions. A family is below the line when its disposable income is under the threshold for its region and size.

## Coverage

2002 to 2025, annual, in current dollars, for the 2000, 2008, 2018 and 2023 base baskets, family sizes 1 to 10.

## Updates

A new reference year is added each spring. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* For a family of four the 2023 base poverty line in Toronto was 62,880 dollars in 2025.
* Across the 65 regions the four person line ranged from 46,852 dollars in Quebec, population 30,000 to 99,999 to 104,808 dollars in Nunavut, Iqaluit.
* For one person living alone in Toronto the line was 31,440 dollars.
* The file has 22,840 rows for 66 regions, four base years and family sizes from 1 to 10 persons, from 2002 to 2025.

## Example uses

* Compare the cost of a modest standard of living across cities and rural areas.
* Pair with income data to estimate poverty rates.
* Study how housing costs pushed thresholds up after 2020.
* Build cost of living features for regional models.

## Caveats

Use one base year at a time; thresholds from different bases are not comparable. Values are in current dollars, not adjusted for inflation. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `mbm_thresholds_by_region_family_size.csv`: Annual Market Basket Measure thresholds in current dollars by MBM region, base year and family size, from Table 11-10-0104.
* `statcan_metadata_11-10-0104.csv`: Official cube metadata for Table 11-10-0104-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 11-10-0104-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
