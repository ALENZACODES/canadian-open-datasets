# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Sources
IRCC open data, Open Government Licence - Canada: https://open.canada.ca/en/open-government-licence-canada

Study permits (portal https://open.canada.ca/data/en/dataset/90115b00-f9b8-49e8-afa3-b4cff8facaee):
- Permit-effective workbook: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Study-IS_PT_study_level_sign.xlsx
- Year-end holders workbook: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-Study-IS_PT_study_level_year_end.xlsx

Work permits (portal https://open.canada.ca/data/en/dataset/360024f2-17e9-4558-bfc1-3616485d65b9):
- TFWP: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Work-TFWP_PT_program_sign.xlsx
- IMP: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Work-IMP_PT_program_sign.xlsx

Asylum claimants (portal https://open.canada.ca/data/en/dataset/b6cbcf4d-f763-4924-a2fb-8cc4a06e3de4):
- https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-Asylum-OfficeType_Prov.xlsx

Workbooks were downloaded on 15 November 2026. Official source lines are recorded in workbook_sheet_provenance.csv. Four of the workbooks are sourced as IRCC, August 31, 2026. The year-end study permit workbook is sourced as IRCC, December 31 2024.

## Measures
The five measures are defined in measure_codebook.csv. Permit holders with a valid permit on 31 December, permit-effective counts, and asylum claims are different official concepts. They are stored in one long file so they can be filtered, but they must not be added together. No summed total across programs or measures is included.

## Processing
Each official workbook sheet was read, including merged header cells. Monthly, quarterly and annual columns were kept as published and labelled with period_type. Official geography totals and official period totals are flagged. They are IRCC published totals, not totals computed for this dataset. Values between 0 and 5 remain suppressed as --, with suppression_flag set to true. ISO 3166-2:CA and Standard Geographic Classification codes were added for Canada, the provinces and the territories. No codes were invented for not-stated geographies.

2026 year totals and 2026 Q3 are flagged as partial periods because the monthly workbooks cover January to August 2026. August 2026 is a complete month in those files.

## Rounding and suppression
The official notes say that values between 0 and 5 are shown as -- to prevent individuals from being identified, and that all other values are rounded to the closest multiple of 5. As a result of rounding, data may not sum to the totals indicated. Data are preliminary estimates and are subject to change. Those notes are kept in this methods file and in the flags on each row.

The year-end study permit workbook also notes that a unique count may not equal the sum of permit holders in each program, because an individual may hold more than one type of permit over a given period.

## Licence
This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Immigration, Refugees and Citizenship Canada open data on study permits, Temporary Foreign Worker Program and International Mobility Program work permits, and asylum claimants. This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.
