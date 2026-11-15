<p align="center"><img src="../../assets/theme-energy-and-transport.png" alt="Canada crude oil exports (CER)" width="100%"></p>

# Canada crude oil exports (CER)

*Monthly crude oil export volumes by destination from the CER*

**Theme:** [Energy and transport](../../README.md#energy-and-transport) · **Coverage:** June 1985 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-crude-oil-exports-cer](https://www.kaggle.com/datasets/johnnykhan1/canada-crude-oil-exports-cer)

## What it is

Monthly Canadian crude oil export volumes by destination (PADD districts), from the Canada Energy Regulator.

Portal: [Crude Oil - Exports](https://open.canada.ca/data/en/dataset/0b7bf4b3-423a-45d0-a92b-e69be0b81ce4).

## Who it helps

Drivers and fleet owners, energy analysts, rail and road safety staff, and anyone tracking Canada's power and fuel mix.

## Files

| File | Size | Where |
|---|---:|---|
| [`crude_oil_exports_by_destination_monthly.csv`](data/crude_oil_exports_by_destination_monthly.csv) | 142 KB | in this repository |
| [`crude_oil_exports_total_monthly.csv`](data/crude_oil_exports_total_monthly.csv) | 11 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 1 KB | in this repository |

## Columns

### `crude_oil_exports_by_destination_monthly.csv`

Monthly crude oil exports by destination (PADD).

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | First day of the month for the export period. |
| `year` | Integer | Calendar year. |
| `month` | Text | Month name as published. |
| `padd` | Text | U.S. Petroleum Administration for Defense District (PADD) destination, or other destination label as published. |
| `volume_m3_per_day` | Float | Export volume in cubic metres per day. Empty when the source cell is confidential or missing. |
| `volume_bbl_per_day` | Float | Export volume in barrels per day. Empty when the source cell is confidential or missing. |

### `crude_oil_exports_total_monthly.csv`

Monthly sum of non-confidential destination volumes in bbl/d.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | First day of the month for the export period. |
| `volume_bbl_per_day` | Float | Export volume in barrels per day. Empty when the source cell is confidential or missing. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

## Source and licence

**Source:** Canada Energy Regulator, Crude Oil Exports by destination monthly CSV (https://www.cer-rec.gc.ca/open/imports-exports/crude-oil-exports-by-destination-monthly.csv), listed on open.canada.ca dataset 0b7bf4b3-423a-45d0-a92b-e69be0b81ce4. Downloaded November 9, 2026. Prepared by John Khan in Toronto, Ontario. Open Government Licence – Canada. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacrudeoilexportscer,
  author    = {Khan, John},
  title     = {Canada crude oil exports (CER)},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-crude-oil-exports-cer}
}
```

APA: Khan, J. (2026). *Canada crude oil exports (CER)* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-crude-oil-exports-cer

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Monthly Canadian crude oil export volumes by destination (PADD districts), from the Canada Energy Regulator.

Portal: [Crude Oil - Exports](https://open.canada.ca/data/en/dataset/0b7bf4b3-423a-45d0-a92b-e69be0b81ce4).

## Coverage

1985-06-01 to 2026-08-01.

## Updates

Snapshot from November 9, 2026. Not auto refreshed.

## A few numbers from this snapshot

* Monthly destination file has 3,166 rows from 1985-06-01 to 2026-08-01.
* Latest summed destination volume in this snapshot: 4.24 million bbl/d on 2026-08-01.
* Some early cells are marked Confidential in the source and appear as empty numeric values here.

## Example uses

* Track export volumes to U.S. PADD regions.
* Join to production and price series.
* Feature for energy market models.

## Caveats

* Confidential source cells are empty rather than filled.
* Summing destinations is a convenience total and may not match a separately published Canada total if destinations are incomplete.
* Units are daily average volumes for the month.

## Licence

Shared under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Canada Energy Regulator. Not an official CER product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
