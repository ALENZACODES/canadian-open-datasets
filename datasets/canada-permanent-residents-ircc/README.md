<p align="center"><img src="../../assets/theme-population.png" alt="Canada permanent residents (IRCC)" width="100%"></p>

# Canada permanent residents (IRCC)

*Monthly PR admissions by province, category and citizenship*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** January 2015 to August 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-permanent-residents-ircc](https://www.kaggle.com/datasets/johnnykhan1/canada-permanent-residents-ircc)

## What it is

Tidied monthly admissions of permanent residents to Canada by province or territory of intended destination and immigration category, plus admissions by country of citizenship. Source workbooks are from Immigration, Refugees and Citizenship Canada (IRCC) open data.

Portal dataset: [Permanent Residents – Monthly IRCC Updates](https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda).

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`canada_monthly_admissions.csv`](data/canada_monthly_admissions.csv) | 3 KB | in this repository |
| [`cover.png`](data/cover.png) | 80 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`permanent_residents_by_citizenship_month.csv`](data/permanent_residents_by_citizenship_month.csv) | 1.1 MB | in this repository |
| [`permanent_residents_by_province_category_month.csv`](data/permanent_residents_by_province_category_month.csv) | 3.9 MB | in this repository |

## Columns

### `canada_monthly_admissions.csv`

Canada-level monthly admissions aggregated from the Canada section of the province file.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | First day of the admission month (YYYY-MM-DD). |
| `admissions` | Float | Number of permanent resident admissions. IRCC suppresses values between 0 and 5 as -- and rounds other values to the nearest 5. Suppressed cells are omitted. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `permanent_residents_by_citizenship_month.csv`

Monthly permanent resident admissions by country of citizenship (from IRCC citizenship workbook).

| Column | Type | Description |
|---|---|---|
| `country_of_citizenship` | Text | Country of citizenship as published. |
| `year` | Integer | Calendar year of admission. |
| `month` | Integer | Month number 1 to 12. |
| `month_label` | Text | Month abbreviation as published. |
| `ref_date` | Date | First day of the admission month (YYYY-MM-DD). |
| `admissions` | Float | Number of permanent resident admissions. IRCC suppresses values between 0 and 5 as -- and rounds other values to the nearest 5. Suppressed cells are omitted. |

### `permanent_residents_by_province_category_month.csv`

Monthly permanent resident admissions by province or territory and immigration category.

| Column | Type | Description |
|---|---|---|
| `province_territory` | Text | Province or territory of intended destination. Canada is the national total section. |
| `immigration_category` | Text | Immigration category, program group, class total or Total, as published. |
| `row_type` | Text | Row classification: geography total, class subtotal, or detailed record. |
| `year` | Integer | Calendar year of admission. |
| `month` | Integer | Month number 1 to 12. |
| `month_label` | Text | Month abbreviation as published. |
| `ref_date` | Date | First day of the admission month (YYYY-MM-DD). |
| `admissions` | Float | Number of permanent resident admissions. IRCC suppresses values between 0 and 5 as -- and rounds other values to the nearest 5. Suppressed cells are omitted. |

## Source and licence

**Source:** Immigration, Refugees and Citizenship Canada open data: EN_ODP-PR-ProvImmCat.xlsx and EN_ODP-PR-Citz.xlsx from https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda downloaded November 9, 2026. Prepared by John Khan in Toronto, Ontario. Open Government Licence – Canada: https://open.canada.ca/en/open-government-licence-canada. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadapermanentresidentsircc,
  author    = {Khan, John},
  title     = {Canada permanent residents (IRCC)},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-permanent-residents-ircc}
}
```

APA: Khan, J. (2026). *Canada permanent residents (IRCC)* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-permanent-residents-ircc

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Tidied monthly admissions of permanent residents to Canada by province or territory of intended destination and immigration category, plus admissions by country of citizenship. Source workbooks are from Immigration, Refugees and Citizenship Canada (IRCC) open data.

Portal dataset: [Permanent Residents – Monthly IRCC Updates](https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda).

## Coverage

Months from 2015-01-01 to 2026-08-01 as published in the downloaded workbooks. The source note is dated August 31, 2026.

## Updates

Snapshot from November 9, 2026. IRCC updates these tables monthly. This upload is not auto refreshed.

## A few numbers from this snapshot

* The province and category file has 46,914 monthly rows from 2015-01-01 to 2026-08-01.
* Canada total permanent resident admissions in August 2026 were 40,225, from the IRCC Total row.
* The citizenship file has 26,654 monthly rows across 218 countries or territories.

## Example uses

* Track immigration category mix over time.
* Compare intended destinations across provinces.
* Feature for labour market or housing demand models.

## Caveats

* IRCC suppresses counts between 0 and 5 (shown as --) and rounds other counts to the nearest 5. Suppressed cells are omitted, not filled.
* Intended destination is not always the same as province of residence after landing.
* Category labels follow IRCC naming and can change when programs are created or closed.
* `canada_monthly_admissions.csv` uses the published Total row, not a sum of categories. Category sums may not match totals because of rounding and suppression.
* Use row_type to keep geography totals separate from detailed categories so you do not double count.

## Licence

Shared under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Immigration, Refugees and Citizenship Canada. Not an official IRCC product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
