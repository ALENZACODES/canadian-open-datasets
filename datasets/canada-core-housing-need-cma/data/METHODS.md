# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Sources
Statistics Canada Table 46-10-0085-01, Canadian Housing Survey core housing need, official release date 2026-09-21: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=4610008501
Statistics Canada Table 98-10-0248-01, 2021 Census core housing need, official release date 2022-09-21: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810024801
Full table CSVs downloaded on 15 November 2026.

## The two series are not equivalent
The Canadian Housing Survey and the 2021 Census both report core housing need, but they are not the same series. They use different methods, different years, different tenure labels, and a different Canada universe: the survey's Canada figure is provinces only, while the census Canada figure includes the territories. They are stored in separate files. This package does not build a continuous annual series from them.

## Survey file
The survey table is kept in full. Official counts, official percentages and official 95% confidence intervals are kept. Published years in this download are 2018, 2021, 2022 and 2024, not every year in between.

gap_vs_canada_pp is the official survey percentage minus the official Canada (provinces only) percentage for the same year, tenure and statistic. That gap is adapted. It is not computed for counts or confidence intervals.

## Census file
The 2021 Census cube is wide and very large. This extract keeps Canada, the provinces and territories, and geographies labelled (CMA). It keeps totals on shelter-cost-to-income ratio, dwelling condition, housing suitability and household type, the Number of private households statistic, and the published core need categories. Only the official Total, Owner and Renter tenure members are kept, in a long counts file.

No census rates are computed. Table 98-10-0248 in this extract is a count table. Users who need a census rate should use an official rate table, not a rate computed from these rounded or published counts.

The full census cube is not included.

## Geography crosswalk
cma_geography_crosswalk_2021.csv lists the official geographies in both files, with 2021 vintage DGUIDs, a CMA identifier parsed from 2021S0503 DGUIDs where present, and flags for which source includes each geography. ISO 3166-2:CA and Standard Geographic Classification codes are added for Canada, provinces and territories. They are left blank for CMAs.

## Licence
This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 46-10-0085 and 98-10-0248. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.
