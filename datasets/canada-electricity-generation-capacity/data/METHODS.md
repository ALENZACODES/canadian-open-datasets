# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Sources
Statistics Canada Table 25-10-0020-01, electricity generation, official release date 2026-10-16: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2510002001
Statistics Canada Table 25-10-0022-01, installed capacity, official release date 2026-10-19: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2510002201
Statistics Canada Table 25-10-0023-01, thermal capacity by fuel, official release date 2026-10-19: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2510002301
Full table CSVs downloaded on 15 November 2026.

No Canadian Energy Regulator files are used. The tables contain observed historical years only. No projected rows were added.

## Processing
Every official row is kept. Columns were renamed to snake case, geography names were trimmed, and reference dates were written as the first day of the year. Published values were not changed. ISO 3166-2:CA and Standard Geographic Classification codes were added.

Generation is kept in official megawatt hours. Capacity is kept in official kilowatts, and a megawatt column is added by dividing kilowatts by 1,000. That conversion is adapted.

technology_crosswalk.csv maps each official type to a technology group and a series role. Official totals and official subtotals are labelled as such. Exclusive types are the published leaf types that are summed in the reconciliation check. Official subtotals are not included in that sum, so they are not double counted.

## Shares and reconciliation
generation_share and capacity_share divide a published value by the official total for the same geography, year and class of producer, using Total all classes of electricity producer in the share files. No capacity factor is calculated.

The reconciliation residual is the exclusive sum minus the official total. It is a check, not an official residual series. From 2014, Statistics Canada often suppresses the combustible-fuel leaf types and publishes Total electricity production from combustible fuels instead. In those years the official combustible fuels total is used in the exclusive sum, which is recorded in reconciliation_method.

## Licence
This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 25-10-0020, 25-10-0022 and 25-10-0023. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.
