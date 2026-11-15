# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Source
Environment and Climate Change Canada, National Inventory Report, IPCC sector file GHG_IPCC_Can_Prov_Terr.csv.
Portal: https://open.canada.ca/data/en/dataset/779c7bcf-4982-47eb-af1b-a33618a05e5b
File: https://data-donnees.az.ec.gc.ca/api/file?path=/substances/monitor/canada-s-official-greenhouse-gas-inventory/A-IPCC-Sector/GHG_IPCC_Can_Prov_Terr.csv
Official date published on the Open Government record, read on 15 November 2026: 2026-04-14.
Downloaded on 15 November 2026.

Population for per person figures comes from Statistics Canada table 17-10-0009, July 1 of the same inventory year.
Table: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901
Official release date on the table page, read on 15 November 2026: 2026-09-23.

## GWP set
Government of Canada states that IPCC Fifth Assessment Report 100-year global warming potentials are required for UNFCCC inventory reporting (Decision 18/CMA.1). See https://www.canada.ca/en/environment-climate-change/services/climate-change/greenhouse-gas-emissions/quantification-guidance/global-warming-potentials.html

## Processing
Column names were converted to snake case. Gas columns were coerced to numbers. The published suppression flag x is stored as an empty numeric value. The published lowercase canada label on one Agriculture series is kept in region_published and is not treated as a second national total.

sector_level is taken from the official tree: 0 inventory total (source Total), 1 source total, 2 category, 3 sub-category, 4 sub-sub-category. is_subtotal follows the official Total flag, and is also True on the inventory total.

The official inventory total equals Energy plus Industrial Processes and Product Use plus Agriculture plus Waste. It does not include land use, land use change and forestry, which remains a separate source. lulucf_treatment records that rule.

pre_1999_nwt_nunavut is True on the official combined Northwest Territories and Nunavut series.

## Derived columns
index_1990 uses 1990 as the base year, with 1990 equal to 100. The official co2eq_kt series is kept beside the index. share_of_canada uses the official Canada series for the same year and category identifier. t_co2eq_per_person is calculated only on official inventory totals, and only when a same-year July 1 population figure can be matched, including the historical combined territories label to Northwest Territories including Nunavut in table 17-10-0009.

## Licence
This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, National Inventory Report IPCC sector file. This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.
Population estimates are used under the Statistics Canada Open Licence: https://www.statcan.gc.ca/en/reference/licence
