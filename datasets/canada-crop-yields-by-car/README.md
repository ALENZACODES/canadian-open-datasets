<p align="center"><img src="../../assets/theme-environment.png" alt="Canada crop yields by agricultural region" width="100%"></p>

# Canada crop yields by agricultural region

*Historic major crop yields by census agricultural region, 1987 to 2025*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1987 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-crop-yields-by-car](https://www.kaggle.com/datasets/johnnykhan1/canada-crop-yields-by-car)

## What it is

Historic actual yields of major field crops by census agricultural region, compiled by Agriculture and Agri-Food Canada from yields provided by Statistics Canada and tidied into a long CSV. A region list and an unweighted crop year summary are included.

Source dataset: [Historic Yields of Major Crops](https://open.canada.ca/data/en/dataset/754a5961-0d27-406c-b5e3-224b6e494e9e) (Agriculture and Agri-Food Canada).

The published table was pulled on November 9, 2026 from https://agriculture.canada.ca/atlas/data_donnees/canadianCropYield/data_donnees/csv/actual/historical_actual_crop_yield_by_CAR.csv

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 100 KB | in this repository |
| [`crop_year_region_summary.csv`](data/crop_year_region_summary.csv) | 30 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`regions.csv`](data/regions.csv) | 2 KB | in this repository |
| [`yields_long.csv`](data/yields_long.csv) | 1.3 MB | in this repository |

## Columns

### `crop_year_region_summary.csv`

Unweighted median, mean and range of regional yields by crop and year.

| Column | Type | Description |
|---|---|---|
| `crop` | Text | Crop name as published (for example Spring Wheat or Canola). |
| `year` | Integer | Crop year from the source YearYYYY columns. |
| `yield_unit` | Text | Unit from the AAFC product specification: bu/ac (bushels per acre) for barley, canola, corn, peas, durum wheat, flax, oats, soybeans, spring wheat and winter wheat; lbs/ac (pounds per acre) for lentils. Left blank for canary seed, fall rye and mustard because those crops are not given a unit in the specification. |
| `n_regions` | Integer | Count of regions with a published yield for that crop and year. |
| `median_yield` | Float | Median of published regional yields for that crop and year. This is an unweighted median of region values, not an official provincial or national yield. |
| `mean_yield` | Float | Unweighted mean of published regional yields for that crop and year. Not an official provincial or national yield. |
| `min_yield` | Float | Lowest published regional yield for that crop and year. |
| `max_yield` | Float | Highest published regional yield for that crop and year. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | File that contains the column |
| `column` | Text | Name of the column being described |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `regions.csv`

Unique census agricultural regions and provinces in this file.

| Column | Type | Description |
|---|---|---|
| `car_uid` | Text | Census agricultural region identifier as published (CAR_UID). |
| `province` | Text | English province name. |
| `region_name` | Text | English census agricultural region or crop reporting unit name as published. Blank when the source left the name empty. |

### `yields_long.csv`

Tidy historic actual crop yields by region, crop and year, 1987 to 2025.

| Column | Type | Description |
|---|---|---|
| `car_uid` | Text | Census agricultural region identifier as published (CAR_UID). |
| `province` | Text | English province name. |
| `region_name` | Text | English census agricultural region or crop reporting unit name as published. Blank when the source left the name empty. |
| `crop` | Text | Crop name as published (for example Spring Wheat or Canola). |
| `year` | Integer | Crop year from the source YearYYYY columns. |
| `yield_value` | Float | Reported yield for that crop, region and year. Blank when the source cell was empty. |
| `yield_unit` | Text | Unit from the AAFC product specification: bu/ac (bushels per acre) for barley, canola, corn, peas, durum wheat, flax, oats, soybeans, spring wheat and winter wheat; lbs/ac (pounds per acre) for lentils. Left blank for canary seed, fall rye and mustard because those crops are not given a unit in the specification. |

## Source and licence

**Source:** Agriculture and Agri-Food Canada, Historic Yields of Major Crops, https://open.canada.ca/data/en/dataset/754a5961-0d27-406c-b5e3-224b6e494e9e. CSV from https://agriculture.canada.ca/atlas/data_donnees/canadianCropYield/data_donnees/csv/actual/historical_actual_crop_yield_by_CAR.csv downloaded on November 9, 2026. Product specification: https://agriculture.canada.ca/atlas/data_donnees/canadianCropYield/supportdocument_documentdesupport/en/ISO_19131_Canadian_Crop_Yields_Data_Product_Specification.pdf. Historic yields were compiled by AAFC from Statistics Canada. Prepared by John Khan in Toronto, Ontario. Contains information licensed under the Open Government Licence – Canada, https://open.canada.ca/en/open-government-licence-canada.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadacropyieldsbycar,
  author    = {Khan, John},
  title     = {Canada crop yields by agricultural region},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-crop-yields-by-car}
}
```

APA: Khan, J. (2026). *Canada crop yields by agricultural region* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-crop-yields-by-car

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Historic actual yields of major field crops by census agricultural region, compiled by Agriculture and Agri-Food Canada from yields provided by Statistics Canada and tidied into a long CSV. A region list and an unweighted crop year summary are included.

Source dataset: [Historic Yields of Major Crops](https://open.canada.ca/data/en/dataset/754a5961-0d27-406c-b5e3-224b6e494e9e) (Agriculture and Agri-Food Canada).

The published table was pulled on November 9, 2026 from https://agriculture.canada.ca/atlas/data_donnees/canadianCropYield/data_donnees/csv/actual/historical_actual_crop_yield_by_CAR.csv

## Coverage

14 crops, 65 regions across the ten provinces, and 16,128 region year values with a published yield. Years run from 1987 through 2025. Crops include barley, canary seed, canola, corn, peas, durum wheat, fall rye, flax, lentils, mustard, oats, soybeans, spring wheat and winter wheat. Units follow the AAFC product specification: bushels per acre for the cereal, oilseed and pulse crops listed there, and pounds per acre for lentils.

## Updates

This upload is a snapshot from November 9, 2026 and is not refreshed on a schedule. AAFC updates the historic yield table as new survey years are added. For later years, download the source CSV from the Open Government portal page above.

## A few numbers from this snapshot

* 65 regions and 14 crops are included.
* 16,128 cells have a published yield.
* The unweighted median of regional canola yields was 30.1 bushels per acre in 2021 and 45.2 bushels per acre in 2025.

## Example uses

* Compare canola or spring wheat yields across prairie regions over time.
* Spot low yield years in a chosen region.
* Join region identifiers to other agricultural or drought tables.

## Caveats

Yields were compiled by AAFC from Statistics Canada historic yields. Census agricultural region boundaries can change over time and are not necessarily the same from one year to the next. Empty cells stay blank. The crop year summary is an unweighted median and mean of the regions that have a value. It is not an official provincial or national yield, which would need area weights that are not in this table. Units for canary seed, fall rye and mustard are not stated in the product specification, so those rows have a blank unit. This is not an official Government of Canada product.

## Files

* `regions.csv`: Unique census agricultural regions and provinces in this file.
* `yields_long.csv`: Tidy historic actual crop yields by region, crop and year, 1987 to 2025.
* `crop_year_region_summary.csv`: Unweighted median, mean and range of regional yields by crop and year.
* `data_dictionary.csv`: column dictionary.
* `cover.png`: cover chart drawn from this snapshot.

## Licence

Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Agriculture and Agri-Food Canada, Historic Yields of Major Crops, compiled from Statistics Canada historic yields. The published values were not changed. Columns were rearranged into tidy tables and a summary was derived. Agriculture and Agri-Food Canada and Statistics Canada do not endorse this upload.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
