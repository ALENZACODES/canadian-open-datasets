<p align="center"><img src="../../assets/theme-housing.png" alt="Canada housing stock by dwelling and tenure" width="100%"></p>

# Canada housing stock by dwelling and tenure

*Quarterly count of dwellings by type, tenure and occupancy, 2016 onward*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** April 2016 to April 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-housing-stock-by-dwelling-and-tenure](https://www.kaggle.com/datasets/johnnykhan1/canada-housing-stock-by-dwelling-and-tenure)

## What it is

The number of homes in Canada, tidied from Statistics Canada [Table 36-10-0688-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610068801), the housing stock used in the national accounts. Counts are split by dwelling type (single, double, row, apartment, mobile), tenure (owner, renter, band), occupancy (usual residents, non usual residents, unoccupied) and private or social housing.

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`housing_stock_units_quarterly.csv`](data/housing_stock_units_quarterly.csv) | 15.6 MB | in this repository |
| [`statcan_metadata_36-10-0688.csv`](data/statcan_metadata_36-10-0688.csv) | 6 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name. |
| `file` | Text | CSV file the column belongs to. |
| `type` | Text | Field type. |
| `description` | Text | What the column contains. |

### `housing_stock_units_quarterly.csv`

Quarterly number of private dwellings by province or territory, housing type, occupancy, dwelling type and tenure, for the total economy, from Table 36-10-0688.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. Monthly tables use the first day of the month, quarterly tables use the first day of the quarter, and annual tables use the calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada, with extra whitespace removed. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `institutional_sector` | Text | Institutional sector as published. |
| `housing_type` | Text | Housing type as published. |
| `dwelling_occupation` | Text | Dwelling occupation as published. |
| `dwelling_type` | Text | Dwelling type as published. |
| `tenure_type` | Text | Tenure type as published. |
| `estimate` | Text | Estimate as published. |
| `unit_of_measure` | Text | Unit of measure for value, as published. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value (for example units, thousands or millions). Value is already expressed at this scale. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that period (see status and symbol). |
| `status` | Text | Statistics Canada status symbol when a value is missing or qualified. Empty means a regular published value. See the symbol legend in the official metadata file. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |
| `source_table` | Text | Statistics Canada table identifier this row was taken from. |

### `statcan_metadata_36-10-0688.csv`

Official Statistics Canada cube metadata shipped with Table 36-10-0688-01, including notes and the symbol legend. Layout is as published, not tidied.

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

**Source:** Statistics Canada Table 36-10-0688-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610068801); Statistics Canada Open Licence (https://www.statcan.gc.ca/en/terms-conditions/open-licence)

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadahousingstockbydwellingandtenure,
  author    = {Khan, John},
  title     = {Canada housing stock by dwelling and tenure},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-housing-stock-by-dwelling-and-tenure}
}
```

APA: Khan, J. (2026). *Canada housing stock by dwelling and tenure* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-housing-stock-by-dwelling-and-tenure

<details><summary>Full notes from the Kaggle page</summary>

## What this is

The number of homes in Canada, tidied from Statistics Canada [Table 36-10-0688-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610068801), the housing stock used in the national accounts. Counts are split by dwelling type (single, double, row, apartment, mobile), tenure (owner, renter, band), occupancy (usual residents, non usual residents, unoccupied) and private or social housing.

## Coverage

Q2 2016 to Q2 2026, quarterly, Canada, provinces and territories. Kept: the total economy sector, every tenure and dwelling breakdown at total housing type, and private versus social housing at total dwelling level. The full source cross tab by institutional sector was left out to keep the file small.

## Updates

Updated quarterly at the source. Snapshot taken on November 14, 2026.

## A few numbers from this snapshot

* Canada had 17,517,365 private dwellings in Q2 2026, up 1.4 percent from a year earlier.
* Renter units were 34.2 percent of the national stock, and Ontario had 6,361,509 private dwellings.
* Apartment units numbered 6,444,204, or 36.8 percent of all private dwellings.
* Social housing accounted for 592,984 units.
* The file has 73,472 rows from Q2 2016 to Q2 2026 for 14 geographies.

## Example uses

* Measure how fast the housing stock grows against population growth.
* Track the renter share and the apartment share by province.
* Estimate vacant and non usual resident dwellings.
* Build per household housing supply indicators.

## Caveats

These are experimental national accounts estimates and are revised. Counts are dwellings, not households or buildings. Empty values mean no figure was published.

## Files

* `data_dictionary.csv`: Column dictionary for every CSV.
* `housing_stock_units_quarterly.csv`: Quarterly number of private dwellings by province or territory, housing type, occupancy, dwelling type and tenure, for the total economy, from Table 36-10-0688.
* `statcan_metadata_36-10-0688.csv`: Official cube metadata for Table 36-10-0688-01, as published.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 36-10-0688-01. The published values were not changed. Columns were renamed, the file layout was tidied, and some dimensions were filtered as described above. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
