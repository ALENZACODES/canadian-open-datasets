# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Source
Statistics Canada Table 14-10-0353-01, Homeless Shelter Capacity in Canada, from Housing, Infrastructure and Communities Canada.
Table: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035301
Official release date on the table page, read on 15 November 2026: 2026-09-11.
Full table CSV downloaded on 15 November 2026.

Population for the per 10,000 figures comes from Statistics Canada Table 17-10-0009-01, quarterly estimates, using the July 1 value in the same calendar year.
Table: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901
Official release date on the table page, read on 15 November 2026: 2026-09-23.

## Processing
Every official row in the capacity cube is kept. Columns were renamed to snake case, geography names were trimmed, and reference dates were written as the first day of the year. Published capacity values were not changed. ISO 3166-2:CA and Standard Geographic Classification codes were added for Canada, the provinces and the territories. Community rows keep their published DGUID when the cube provides one.

This package describes capacity only. It does not include occupancy or homelessness counts.

## Classification change in 2021
Official table note 1 states: until 2021, shelters serving the "Women with or without children" sub-target population were included in the "General-women" target population statistics. Starting in 2021, statistics from this sub-target population are included in the "Family" target population. classification_break is True on General - women and Family rows so those series are not compared across 2021 without that note.

## Derived columns
beds_per_10000 appears only on the provincial file, and only for Number of beds, Total, target population, by shelter type. The denominator is July 1 population of the same year from table 17-10-0009. Shelter types are not summed, and nested target populations are not used for the rate, so official totals are not double counted.

## Licence
This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 14-10-0353 and 17-10-0009. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.
