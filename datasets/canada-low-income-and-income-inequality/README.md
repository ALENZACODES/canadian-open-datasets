<p align="center"><img src="../../assets/theme-jobs-and-income.png" alt="Canada Low Income and Income Inequality" width="100%"></p>

# Canada Low Income and Income Inequality

*Poverty rates, Gini coefficients and income deciles, 1976 to 2024*

**Theme:** [Jobs, wages and income](../../README.md#jobs-wages-and-income) · **Coverage:** January 1976 to January 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-low-income-and-income-inequality](https://www.kaggle.com/datasets/johnnykhan1/canada-low-income-and-income-inequality)

## What it is

A tidy extract of three official Statistics Canada income tables covering 49 years, 1976 to 2024. Together they show how many people live below each of Canada's low income lines, how deep their low income is, how unequal incomes are before and after taxes and transfers, and what each income decile earns.

Source tables:

* [11-10-0135-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013501): Low income statistics by age, gender and economic family type.
* [11-10-0134-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013401): Gini coefficients of adjusted market, total and after-tax income.
* [11-10-0193-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110019301): Upper income limit, income share and average of adjusted market, total and after-tax income by income decile.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The figures come from the Survey of Consumer Finances (1976 to 1992), a mix of that survey and the Survey of Labour and Income Dynamics (1993 to 1997), the Survey of Labour and Income Dynamics (1998 to 2011) and the Canadian Income Survey (2012 onward).

## Who it helps

Job seekers, employers, unions, policy analysts, poverty researchers and students looking at work and income across Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 62 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 9 KB | in this repository |
| [`gini_coefficients.csv`](data/gini_coefficients.csv) | 210 KB | in this repository |
| [`income_deciles.csv`](data/income_deciles.csv) | 9.8 MB | in this repository |
| [`official_metadata_11100134.csv`](data/official_metadata_11100134.csv) | 7 KB | in this repository |
| [`official_metadata_11100135.csv`](data/official_metadata_11100135.csv) | 15 KB | in this repository |
| [`official_metadata_11100193.csv`](data/official_metadata_11100193.csv) | 8 KB | in this repository |
| `low_income_statistics.csv` | 88.9 MB (5.7 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/canada-low-income-and-income-inequality--low_income_statistics.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `data_dictionary.csv`

Column dictionary for every tidy CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, numeric or integer). |
| `description` | Text | What the column contains. |

### `gini_coefficients.csv`

Official Gini coefficients of adjusted market income, adjusted total income and adjusted after-tax income, for Canada, provinces and territories, 1976 to 2024.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the income data, stored as January 1 of that year (1976-01-01 to 2024-01-01). Income refers to the full calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the provinces, the territories, official regional groupings, and in low_income_statistics.csv also eight census metropolitan areas. The official notes say estimates for Canada do not include the territories before 2018. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `income_concept` | Text | Income concept as published: adjusted market income, adjusted total income (market income plus government transfers) or adjusted after-tax income. Adjusted means divided by the square root of household size. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Number, Percent or 2024 constant dollars. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so values are already in persons, percent, dollars or Gini points. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Float | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. Gini coefficients run from 0 (equal) to 1 (unequal). |
| `status` | Text | Statistics Canada status symbol. A to E are data quality grades based on the coefficient of variation (A excellent, B very good, C good, D acceptable, E use with caution) and come with a published value. F means too unreliable to be published and .. means not available for that reference period; in both cases value is empty. Empty status means no grade was given. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `income_deciles.csv`

Official upper income limit, share of income and average income by income decile, for adjusted market, total and after-tax income, in 2024 constant dollars, for Canada, provinces and territories, 1976 to 2024.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the income data, stored as January 1 of that year (1976-01-01 to 2024-01-01). Income refers to the full calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the provinces, the territories, official regional groupings, and in low_income_statistics.csv also eight census metropolitan areas. The official notes say estimates for Canada do not include the territories before 2018. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `income_concept` | Text | Income concept as published: adjusted market income, adjusted total income (market income plus government transfers) or adjusted after-tax income. Adjusted means divided by the square root of household size. |
| `income_decile` | Text | Income decile as published, from Lowest decile to Highest decile, plus Total deciles. The highest decile has no upper income limit. |
| `statistic` | Text | The kind of official figure. In low_income_statistics.csv: number of persons in low income, percentage of persons in low income, or average gap ratio. In income_deciles.csv: upper income limit, share of income, or average income. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Number, Percent or 2024 constant dollars. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so values are already in persons, percent, dollars or Gini points. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. Gini coefficients run from 0 (equal) to 1 (unequal). |
| `status` | Text | Statistics Canada status symbol. A to E are data quality grades based on the coefficient of variation (A excellent, B very good, C good, D acceptable, E use with caution) and come with a published value. F means too unreliable to be published and .. means not available for that reference period; in both cases value is empty. Empty status means no grade was given. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `low_income_statistics.csv`

Official number of persons in low income, percentage of persons in low income and average gap ratio, under seven low income lines (LIM after tax, LICO after and before tax, and four Market Basket Measure bases), by age, gender and economic family type, for Canada, provinces, territories and selected census metropolitan areas, 1976 to 2024.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference year of the income data, stored as January 1 of that year (1976-01-01 to 2024-01-01). Income refers to the full calendar year. |
| `geo` | Text | Geography name as published by Statistics Canada: Canada, the provinces, the territories, official regional groupings, and in low_income_statistics.csv also eight census metropolitan areas. The official notes say estimates for Canada do not include the territories before 2018. |
| `dguid` | Text | Statistics Canada Dissemination Geography Unique Identifier for the geography. |
| `persons_in_low_income` | Text | Population group as published: all persons, age groups, Men+ and Women+, and economic family types. Men+ and Women+ include some non-binary persons. Before 2021 this was the sex of the person. |
| `low_income_line` | Text | Low income line as published: Low income measure after tax (LIM-AT), Low income cut-offs after tax and before tax (1992 base), or the Market Basket Measure on its 2000, 2008, 2018 or 2023 base. The Market Basket Measure is Canada's Official Poverty Line. |
| `statistic` | Text | The kind of official figure. In low_income_statistics.csv: number of persons in low income, percentage of persons in low income, or average gap ratio. In income_deciles.csv: upper income limit, share of income, or average income. |
| `unit_of_measure` | Text | Unit of measure for value, as published: Number, Percent or 2024 constant dollars. |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | Scale of value as published. In these tables the official scale is units, so values are already in persons, percent, dollars or Gini points. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor. |
| `vector` | Text | Statistics Canada vector identifier for the series. Useful if you want to pull the same series again. |
| `coordinate` | Text | Statistics Canada coordinate string that locates the series inside the official table. |
| `value` | Float | The published value. Empty when Statistics Canada did not publish a figure for that cell (see status). Official values were not altered. Gini coefficients run from 0 (equal) to 1 (unequal). |
| `status` | Text | Statistics Canada status symbol. A to E are data quality grades based on the coefficient of variation (A excellent, B very good, C good, D acceptable, E use with caution) and come with a published value. F means too unreliable to be published and .. means not available for that reference period; in both cases value is empty. Empty status means no grade was given. |
| `symbol` | Text | Additional Statistics Canada symbol when present, otherwise empty. |
| `terminated` | Text | t if Statistics Canada has terminated this series, otherwise empty. |
| `decimals` | Integer | Number of decimal places Statistics Canada uses when displaying the value. |

### `official_metadata_11100134.csv`

Official Statistics Canada metadata, notes and symbol legend for table 11-10-0134-01.


### `official_metadata_11100135.csv`

Official Statistics Canada metadata, notes and symbol legend for table 11-10-0135-01.


### `official_metadata_11100193.csv`

Official Statistics Canada metadata, notes and symbol legend for table 11-10-0193-01.


## Source and licence

**Source:** Statistics Canada, Centre for Housing and Income Statistics. Official tables downloaded on November 10, 2026 from the Statistics Canada full table CSV zips: 11-10-0135-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013501, https://www150.statcan.gc.ca/n1/tbl/csv/11100135-eng.zip) 11-10-0134-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013401, https://www150.statcan.gc.ca/n1/tbl/csv/11100134-eng.zip) 11-10-0193-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110019301, https://www150.statcan.gc.ca/n1/tbl/csv/11100193-eng.zip) Prepared by John Khan in Toronto, Ontario. Shared under the Statistics Canada Open Licence, https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadalowincomeandincomeinequality,
  author    = {Khan, John},
  title     = {Canada Low Income and Income Inequality},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-low-income-and-income-inequality}
}
```

APA: Khan, J. (2026). *Canada Low Income and Income Inequality* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-low-income-and-income-inequality

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of three official Statistics Canada income tables covering 49 years, 1976 to 2024. Together they show how many people live below each of Canada's low income lines, how deep their low income is, how unequal incomes are before and after taxes and transfers, and what each income decile earns.

Source tables:

* [11-10-0135-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013501): Low income statistics by age, gender and economic family type.
* [11-10-0134-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013401): Gini coefficients of adjusted market, total and after-tax income.
* [11-10-0193-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110019301): Upper income limit, income share and average of adjusted market, total and after-tax income by income decile.

The official English CSV files were downloaded from Statistics Canada on November 10, 2026. The figures come from the Survey of Consumer Finances (1976 to 1992), a mix of that survey and the Survey of Labour and Income Dynamics (1993 to 1997), the Survey of Labour and Income Dynamics (1998 to 2011) and the Canadian Income Survey (2012 onward).

## Files

* low_income_statistics.csv: 470,016 rows. Number and percentage of persons in low income and the average gap ratio, by population group, low income line and geography.
* gini_coefficients.csv: 1,995 rows. Gini coefficients of adjusted market, total and after-tax income.
* income_deciles.csv: 65,121 rows. Upper income limit, income share and average income by decile, in 2024 constant dollars.
* data_dictionary.csv: every column in every file, with its type and meaning.
* official_metadata_*.csv: the official Statistics Canada notes, member lists and symbol legend for each table.

## A few numbers from this snapshot

* In 2024, 11.0% of people in Canada, or 4,477,500 persons, lived below the Market Basket Measure (2023 base), which is Canada's Official Poverty Line.
* By that same line, the 2024 rate was 11.5% for persons under 18 years and 5.4% for persons 65 years and over.
* Among persons under 18 years in one parent families where the parent is a woman+, the 2024 rate was 29.7%.
* Among the provinces in 2024, the rate was lowest in Quebec at 7.0% and highest in British Columbia at 13.0%. In Ontario it was 12.5%.
* Under the relative Low income measure after tax, 12.5% of persons were in low income in 2024.
* The Gini coefficient of adjusted after-tax income for Canada was 0.305 in 2024, against 0.436 for adjusted market income, so taxes and transfers narrowed measured inequality. In 1976 the after-tax figure was 0.3.
* In 2024 the highest after-tax income decile received 23.3% of all adjusted after-tax income, and the lowest decile received 2.7%.

## Coverage

All three tables run every year from 1976 to 2024 for Canada, the ten provinces and the regional groupings. Yukon, the Northwest Territories, Nunavut and the Territories grouping start in 2018. The low income table also has eight census metropolitan areas: Québec, Montréal, Ottawa-Gatineau, Toronto, Winnipeg, Calgary, Edmonton and Vancouver. Not every low income line exists for every year, and the territories have no figures before 2018. The Market Basket Measure 2023 base starts in 2020, and older bases stop where Statistics Canada stopped them.

## Caveats

* Statistics Canada notes that estimates for Canada do not include the territories before 2018.
* The surveys changed over time. From 2021 the Canadian Income Survey uses a richer tax file source, and from 2022 it has a larger sample and covers persons 15 years and over instead of 16 and over. With the 2024 release, Statistics Canada revised 2018 to 2023 using 2021 Census population counts. Be careful when you compare across these breaks.
* Rows with status F (too unreliable to be published) or .. (not available for that reference period) are kept, with value left blank. Status A to E is a data quality grade on a published value. Treat E values with caution.
* Low income rates for 2020 are much lower than for 2019 or 2022. 2020 was the year temporary pandemic benefits were paid, so read that dip in context rather than as an error.
* Men+ and Women+ include some non-binary persons. Before 2021 this variable was sex.
* Dollar values in income_deciles.csv are in 2024 constant dollars as published.

## Example uses

* Track Canada's Official Poverty Line rate by province and age group.
* Compare how different low income lines rank the same provinces.
* Measure how much taxes and transfers reduce inequality, by comparing market and after-tax Gini coefficients.
* Join with CPI, housing or labour data to study what moves poverty rates.
* Teach time series with structural breaks and survey quality flags.

## Updates

This upload is a snapshot from November 10, 2026 and is not refreshed on a schedule. Statistics Canada updates these tables once a year when it releases the Canadian Income Survey.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

Column names were changed to snake_case and reference years were stored as dates. Official values and quality symbols were not altered. No rows were added or removed.

## Licence

This dataset is shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Credit: Statistics Canada, tables 11-10-0135-01, 11-10-0134-01 and 11-10-0193-01. The published values were not changed. Columns were renamed and the file layout was tidied. This is not an official Statistics Canada product and Statistics Canada does not endorse it.

Author: John Khan, Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
