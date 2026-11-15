<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada education and employment income" width="100%"></p>

# Canada education and employment income

*2021 Census median income by highest certificate, province and CMA*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** 2020 income year (2021 Census) · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-education-employment-income](https://www.kaggle.com/datasets/johnnykhan1/canada-education-employment-income)

## What it is

2021 Census employment income by highest certificate, diploma or degree for Canada, the provinces and territories, census metropolitan areas and census agglomerations. Tidied from Statistics Canada Table [98-10-0410-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810041001).

Filters applied so the file stays analysis ready and reasonably sized: total gender, total major field of study, total work activity, income year 2020, and ages Total - Age plus 25 to 64 years. All published education levels are kept in the long file.

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 37 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 7 KB | in this repository |
| [`education_employment_income_long.csv`](data/education_employment_income_long.csv) | 1.7 MB | in this repository |
| [`education_income_cma_ca_age_25_64.csv`](data/education_income_cma_ca_age_25_64.csv) | 380 KB | in this repository |
| [`education_income_cmas_age_25_64.csv`](data/education_income_cmas_age_25_64.csv) | 104 KB | in this repository |
| [`education_income_provinces_age_25_64.csv`](data/education_income_provinces_age_25_64.csv) | 33 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 223 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `file` | Text | Name of the column being described |
| `column` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `education_employment_income_long.csv`

Employment income by highest education for Canada, provinces/territories, CMAs and CAs. Total gender, total field of study, income year 2020, ages Total and 25 to 64.

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published, or Toronto for citywide TPS rows. |
| `geo_level` | Text | Geography level: canada, region, province_or_canada, cma_or_ca, city or neighbourhood. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `gender` | Text | Gender grouping published by the census. |
| `age_group` | Text | Age group published by the census. |
| `education_level` | Text | Highest certificate, diploma or degree. |
| `work_activity` | Text | Work activity during the reference year. |
| `income_year` | Integer | Income reference year (2019 or 2020). |
| `field_of_study` | Text | Major field of study (CIP 2021 summary). |
| `total_population_in_universe` | Integer | Count of people in the census universe for that row. |
| `with_employment_income` | Integer | Number of people with employment income. |
| `median_employment_income` | Float | Median employment income in dollars. |
| `average_employment_income` | Float | Average employment income in dollars. |
| `with_wages_salaries_commissions` | Integer | Number of people with wages, salaries and commissions. |
| `median_wages_salaries_commissions` | Float | Median wages, salaries and commissions in dollars. |
| `average_wages_salaries_commissions` | Float | Average wages, salaries and commissions in dollars. |

### `education_income_cma_ca_age_25_64.csv`

CMAs and census agglomerations, age 25 to 64, selected education levels, 2020 employment income.

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published, or Toronto for citywide TPS rows. |
| `geo_level` | Text | Geography level: canada, region, province_or_canada, cma_or_ca, city or neighbourhood. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `gender` | Text | Gender grouping published by the census. |
| `age_group` | Text | Age group published by the census. |
| `education_level` | Text | Highest certificate, diploma or degree. |
| `work_activity` | Text | Work activity during the reference year. |
| `income_year` | Integer | Income reference year (2019 or 2020). |
| `field_of_study` | Text | Major field of study (CIP 2021 summary). |
| `total_population_in_universe` | Integer | Count of people in the census universe for that row. |
| `with_employment_income` | Integer | Number of people with employment income. |
| `median_employment_income` | Float | Median employment income in dollars. |
| `average_employment_income` | Float | Average employment income in dollars. |
| `with_wages_salaries_commissions` | Integer | Number of people with wages, salaries and commissions. |
| `median_wages_salaries_commissions` | Float | Median wages, salaries and commissions in dollars. |
| `average_wages_salaries_commissions` | Float | Average wages, salaries and commissions in dollars. |

### `education_income_cmas_age_25_64.csv`

Census metropolitan areas, age 25 to 64, selected education levels, 2020 employment income.

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published, or Toronto for citywide TPS rows. |
| `geo_level` | Text | Geography level: canada, region, province_or_canada, cma_or_ca, city or neighbourhood. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `gender` | Text | Gender grouping published by the census. |
| `age_group` | Text | Age group published by the census. |
| `education_level` | Text | Highest certificate, diploma or degree. |
| `work_activity` | Text | Work activity during the reference year. |
| `income_year` | Integer | Income reference year (2019 or 2020). |
| `field_of_study` | Text | Major field of study (CIP 2021 summary). |
| `total_population_in_universe` | Integer | Count of people in the census universe for that row. |
| `with_employment_income` | Integer | Number of people with employment income. |
| `median_employment_income` | Float | Median employment income in dollars. |
| `average_employment_income` | Float | Average employment income in dollars. |
| `with_wages_salaries_commissions` | Integer | Number of people with wages, salaries and commissions. |
| `median_wages_salaries_commissions` | Float | Median wages, salaries and commissions in dollars. |
| `average_wages_salaries_commissions` | Float | Average wages, salaries and commissions in dollars. |

### `education_income_provinces_age_25_64.csv`

Canada and provinces/territories, age 25 to 64, selected education levels, 2020 employment income.

| Column | Type | Description |
|---|---|---|
| `geo` | Text | Geography name as published, or Toronto for citywide TPS rows. |
| `geo_level` | Text | Geography level: canada, region, province_or_canada, cma_or_ca, city or neighbourhood. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier. |
| `gender` | Text | Gender grouping published by the census. |
| `age_group` | Text | Age group published by the census. |
| `education_level` | Text | Highest certificate, diploma or degree. |
| `work_activity` | Text | Work activity during the reference year. |
| `income_year` | Integer | Income reference year (2019 or 2020). |
| `field_of_study` | Text | Major field of study (CIP 2021 summary). |
| `total_population_in_universe` | Integer | Count of people in the census universe for that row. |
| `with_employment_income` | Integer | Number of people with employment income. |
| `median_employment_income` | Float | Median employment income in dollars. |
| `average_employment_income` | Float | Average employment income in dollars. |
| `with_wages_salaries_commissions` | Integer | Number of people with wages, salaries and commissions. |
| `median_wages_salaries_commissions` | Float | Median wages, salaries and commissions in dollars. |
| `average_wages_salaries_commissions` | Float | Average wages, salaries and commissions in dollars. |

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata shipped with the table download, including notes and the symbol legend. Layout is as published, not tidied.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | — |
| `Product Id` | Text | — |
| `CANSIM Id` | Text | — |
| `URL` | Text | — |
| `Cube Notes` | Text | — |
| `Archive Status` | Text | — |
| `Frequency` | Text | — |
| `Start Reference Period` | Text | — |
| `End Reference Period` | Text | — |
| `Total number of dimensions` | Text | — |
| `Universe` | Text | — |
| `Variable List` | Text | — |

## Source and licence

**Source:** Statistics Canada Table 98-10-0410-01, downloaded November 9, 2026. Prepared by John Khan in Toronto, Ontario.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaeducationemploymentincome,
  author    = {Khan, John},
  title     = {Canada education and employment income},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-education-employment-income}
}
```

APA: Khan, J. (2026). *Canada education and employment income* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-education-employment-income

<details><summary>Full notes from the Kaggle page</summary>

## What this is

2021 Census employment income by highest certificate, diploma or degree for Canada, the provinces and territories, census metropolitan areas and census agglomerations. Tidied from Statistics Canada Table [98-10-0410-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810041001).

Filters applied so the file stays analysis ready and reasonably sized: total gender, total major field of study, total work activity, income year 2020, and ages Total - Age plus 25 to 64 years. All published education levels are kept in the long file.

## Files

| File | What is in it |
|---|---|
| `education_employment_income_long.csv` | Full filtered long table (provinces, CMAs, CAs) |
| `education_income_provinces_age_25_64.csv` | Canada and provinces, age 25 to 64, selected levels |
| `education_income_cmas_age_25_64.csv` | CMA only, age 25 to 64, selected levels |
| `education_income_cma_ca_age_25_64.csv` | CMAs and CAs, age 25 to 64, selected levels |
| `data_dictionary.csv` | Column descriptions |
| `statcan_table_metadata.csv` | Official StatCan cube notes |
| `cover.png` | Cover chart |

## Coverage

Census year 2021. Income year 2020. Universe: population aged 15 years and over in private households (25% sample), with age filters as above. Employment income statistics include counts with employment income, median and average employment income, and the wages/salaries/commissions counterparts.

## A few numbers from this snapshot

* For Canada, age 25 to 64, median employment income for bachelor's degree or higher was $63,200 in 2020.
* For the same age group, median employment income with no certificate, diploma or degree was $30,000.
* This snapshot keeps total gender, total field of study, and income year 2020. Age groups kept: Total - Age and 25 to 64 years.

## Caveats

* Income figures can be suppressed or rounded by Statistics Canada. Empty cells follow StatCan symbols in the source cube.
* Field of study is collapsed to the Total in this snapshot. For CIP detail, download Table 98-10-0410 again without that filter.
* Women+ and Men+ rows were dropped to keep the file small. Re-download the cube if you need gender splits.
* This is not an official Statistics Canada product.

## Sources

Statistics Canada, Table 98-10-0410-01, Employment income statistics by highest level of education and major field of study (summary), downloaded November 9, 2026.

## Licence

Shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada, Table 98-10-0410-01. Values were not altered. Columns were renamed and dimensions were filtered as described.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
