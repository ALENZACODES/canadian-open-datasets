# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Sources
Statistics Canada Table 20-10-0025-01, New motor vehicle registrations, quarterly, official release date 2026-09-08: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010002501
Full table CSV downloaded on 15 November 2026. Survey 5307, New Motor Vehicle Registration Survey.

## Flow, not stock
The official cube title is New motor vehicle registrations, quarterly, by geographic level. The values are new registrations during the quarter, a flow, not a stock of vehicles in use. That concept is repeated in registration_concept.

## Geography
Only Canada, the provinces and territories, and census metropolitan areas are kept. Census agglomerations and census subdivisions were dropped. CMA rows use the 2016 CMA delineation published in the cube DGUID (2016S0503). Canada and provincial or territorial rows use 2021 Standard Geographic Classification codes.

## Fuel types and shares
Official fuel types are kept. fuel_type_crosswalk.csv documents a fuel_group code for each official type, including the official All fuel types total and the official All zero-emission vehicles subtotal.

bev_phev_share_pct is 100 times (official battery electric plus official plug-in hybrid electric) divided by official All fuel types new registrations for the same geography, quarter and vehicle type. That denominator is stated on each share row. The official zero-emission subtotal is also kept. Because of Random Tabular Adjustment, battery electric plus plug-in hybrid electric may not equal the official zero-emission subtotal.

## Random Tabular Adjustment and missing provinces
Table note 3 states that Random Tabular Adjustment was used, and that related totals and subtotals were also adjusted. rta_adjusted is true for every row. Table note 2 states that data for Newfoundland and Labrador and Alberta are currently not available due to contractual limitations of the existing data sharing agreement. Official .. cells are kept.

## Partial year
The official table is quarterly. 2026 currently includes the first two quarters only. The annual file is an adapted sum of official quarterly values, with is_partial_year true when fewer than four quarters are available. It is not an official annual table. Because of Random Tabular Adjustment, a sum of official quarters may not match a hypothetical official annual total.

## Licence
This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 20-10-0025. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.
