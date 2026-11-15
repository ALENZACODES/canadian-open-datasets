<p align="center"><img src="../../assets/theme-population.png" alt="Canada IRCC permits and asylum claims" width="100%"></p>

# Canada IRCC permits and asylum claims

*Official study, work permit and asylum figures, 2015 to 2026*

**Theme:** [Population and immigration](../../README.md#population-and-immigration) · **Coverage:** 2000 to 2026 (monthly from January 2015) · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-ircc-permits-asylum-claims](https://www.kaggle.com/datasets/johnnykhan1/canada-ircc-permits-asylum-claims)

## What it is

Official Immigration, Refugees and Citizenship Canada figures for study permits, Temporary Foreign Worker Program and International Mobility Program work permits, and asylum claims, tidied into one long file. Permit-effective counts, year-end study permit holders, and asylum claims are separately defined measures, with a code book and a workbook and sheet provenance manifest. There is no summed total across programs or measures. Official suppression and rounding flags are kept.

## Who it helps

Newcomers, settlement agencies, planners, school boards, businesses choosing locations and demographers.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 4 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 3 KB | in this repository |
| [`cover.png`](data/cover.png) | 54 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 6 KB | in this repository |
| [`ircc_permits_asylum_claims.csv`](data/ircc_permits_asylum_claims.csv) | 45.7 MB | in this repository |
| [`measure_codebook.csv`](data/measure_codebook.csv) | 3 KB | in this repository |
| [`workbook_sheet_provenance.csv`](data/workbook_sheet_provenance.csv) | 3 KB | in this repository |

## Columns

### `SOURCE_MANIFEST.csv`

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | Short identifier for the workbook in this package. |
| `title` | Text | Official title from row 1 of the sheet. |
| `url` | Text | Direct workbook URL. |
| `licence` | Text | Open Government Licence - Canada. |
| `release_date` | Text | — |
| `retrieval_date` | Date | Date the workbook was downloaded, as YYYY-MM-DD. |
| `file_name` | Text | — |
| `checksum_sha256` | Text | SHA256 checksum of the downloaded workbook. |
| `notes` | Text | — |

### `data_dictionary.csv`

| Column | Type | Description |
|---|---|---|
| `column` | Text | — |
| `file` | Text | — |
| `type` | Text | — |
| `description` | Text | — |

### `ircc_permits_asylum_claims.csv`

| Column | Type | Description |
|---|---|---|
| `program` | Text | IRCC program family as documented in the code book: Study permit, Temporary Foreign Worker Program, International Mobility Program, or Asylum. |
| `measure_code` | Text | Stable code for the official measure. See measure_codebook.csv. |
| `measure` | Text | Official measure description. Permit-effective counts, year-end holders and asylum claims are different measures and must not be added together. |
| `geo` | Text | geo as published or derived in ircc_permits_asylum_claims.csv. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two-digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `category` | Text | Official study level, work-permit program, asylum office type, or official total label. |
| `program_path` | Text | Official label path as it appears in the workbook, including any published program hierarchy. |
| `period` | Text | Reference period as YYYY, YYYY-Qn or YYYY-MM. |
| `period_type` | Text | year, quarter or month, taken from the official workbook headers. |
| `year` | Integer | Calendar year of the official period. |
| `month` | Float | Month number when period_type is month. |
| `quarter` | Text | Quarter number when period_type is quarter. |
| `is_partial_period` | Boolean | True for official 2026 year totals and for 2026 Q3, because the workbooks cover January to August 2026. |
| `is_official_geography_total` | Boolean | True when the row is a published geography or office-type total in the workbook. |
| `is_official_period_total` | Boolean | True when the column is a published quarter total or year total in the workbook. |
| `is_official_total` | Boolean | True when the row is an official geography total or an official period total. These are published IRCC totals, not totals computed for this dataset. |
| `value` | Float | Official published count. Values between 0 and 5 are suppressed as --. Other published values are rounded by IRCC to the closest multiple of 5. Because of rounding, official categories may not sum to official totals. |
| `unit` | Text | Persons, as published by IRCC, after official rounding and suppression. |
| `suppression_flag` | Boolean | True when the official cell is --, meaning a value between 0 and 5 was suppressed. |
| `source_value` | Text | The official cell as published, including -- and thousands separators. |
| `rounding_applied` | Boolean | True when a non-zero numeric value is present. IRCC rounds those values to the closest multiple of 5. Zero is published as 0. |
| `source_file` | Text | Workbook file name. |
| `source_sheet` | Text | Workbook sheet name. |
| `source_row` | Integer | Row number in the official sheet, starting at 1. |

### `measure_codebook.csv`

| Column | Type | Description |
|---|---|---|
| `measure_code` | Text | Stable code for the official measure. See measure_codebook.csv. |
| `measure` | Text | Official measure description. Permit-effective counts, year-end holders and asylum claims are different measures and must not be added together. |
| `program` | Text | IRCC program family as documented in the code book: Study permit, Temporary Foreign Worker Program, International Mobility Program, or Asylum. |
| `unit` | Text | Persons, as published by IRCC, after official rounding and suppression. |
| `definition` | Text | Definition of the official measure. |
| `source_file` | Text | Workbook file name. |
| `portal` | Text | Open Government Portal dataset page. |
| `url` | Text | Direct workbook URL. |
| `do_not_sum_across_measures` | Boolean | Always true. The five measures are separately defined and must not be added together. |

### `workbook_sheet_provenance.csv`

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | Short identifier for the workbook in this package. |
| `workbook_file` | Text | Official workbook file name. |
| `sheet` | Text | Official sheet name. |
| `title` | Text | Official title from row 1 of the sheet. |
| `source_line` | Text | Official source line printed at the bottom of the sheet. |
| `url` | Text | Direct workbook URL. |
| `portal` | Text | Open Government Portal dataset page. |
| `licence` | Text | Open Government Licence - Canada. |
| `retrieval_date` | Date | Date the workbook was downloaded, as YYYY-MM-DD. |
| `checksum_sha256` | Text | SHA256 checksum of the downloaded workbook. |
| `rows_extracted` | Integer | Number of tidy rows extracted from the sheet. |
| `measure_code` | Text | Stable code for the official measure. See measure_codebook.csv. |
| `program` | Text | IRCC program family as documented in the code book: Study permit, Temporary Foreign Worker Program, International Mobility Program, or Asylum. |

## Source and licence

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadairccpermitsasylumclaims,
  author    = {Khan, John},
  title     = {Canada IRCC permits and asylum claims},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-ircc-permits-asylum-claims}
}
```

APA: Khan, J. (2026). *Canada IRCC permits and asylum claims* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ircc-permits-asylum-claims

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Official Immigration, Refugees and Citizenship Canada figures for study permits, Temporary Foreign Worker Program and International Mobility Program work permits, and asylum claims, tidied into one long file. Permit-effective counts, year-end study permit holders, and asylum claims are separately defined measures, with a code book and a workbook and sheet provenance manifest. There is no summed total across programs or measures. Official suppression and rounding flags are kept.

## Coverage

Permit-effective and asylum workbooks cover January 2015 to August 2026. Year-end study permit holders cover 2000 to 2024. Canada, the provinces and the territories, plus not-stated geographies as published.

## Updates

This upload is a snapshot downloaded on 15 November 2026. Four workbooks are sourced as IRCC, August 31, 2026. The year-end study permit workbook is sourced as IRCC, December 31 2024.

## A few numbers from this snapshot

* The long file has 127,202 official cells from five IRCC workbooks. Study permit-effective counts, year-end study permit holders, TFWP and IMP permit-effective counts, and asylum claims are kept as separately defined measures. No cross-program total is created.
* In 2025, the official Canada total for study permit holders, year in which the permit became effective, was 380,310, as published by IRCC. 2026 figures in the same workbooks are partial, covering January to August.
* On 31 December 2024, the official Canada total for study permit holders with a valid permit was 996,375, as published. That year-end stock is a different measure from the permit-effective count and must not be added to it.
* IRCC suppresses values between 0 and 5 as -- and rounds other values to the closest multiple of 5, so official categories may not sum to official totals. Those suppression and rounding flags are kept.

## Example uses

* Use one measure at a time, as defined in the code book.
* Filter official year totals for complete calendar years, and treat 2026 as a partial period.
* Keep suppression and rounding in mind when comparing categories with official totals.

## Caveats

Do not add study, TFWP, IMP and asylum rows together, and do not add year-end holders to permit-effective counts. IRCC rounds most published values to the closest multiple of 5 and suppresses values between 0 and 5, so categories may not sum to official totals. Figures are preliminary and subject to change. 2026 year totals are year-to-date through August.

## Files

* `ircc_permits_asylum_claims.csv`: One long file of official IRCC figures. Study permit-effective counts, year-end study permit holders, TFWP permit-effective counts, IMP permit-effective counts, and asylum claims are separately defined measures. There is no summed total across programs or measures.
* `measure_codebook.csv`: Code book for the five official measures, including the instruction not to add them together.
* `workbook_sheet_provenance.csv`: Workbook and sheet provenance: official title, source line, portal, URL, retrieval date and SHA256 checksum.
* `SOURCE_MANIFEST.csv`: Source workbook identifiers, source lines, retrieval date and checksums.
* `data_dictionary.csv`: Column dictionary.
* `METHODS.md`: Methods note.
* `CITATION.txt`: Suggested citation, with DOI pending.

## Licence

This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Immigration, Refugees and Citizenship Canada open data on study permits, work permits and asylum claimants. This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.

Suggested citation: John Khan. 2026. Canada IRCC permits and asylum claims [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ircc-permits-asylum-claims. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
