# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Source
Statistics Canada Table 13-10-0834-01, Food insecurity by economic family type.
Table: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310083401
Official release date on the table page, read on 15 November 2026: 2026-04-29.
Full table CSV downloaded on 15 November 2026.

The cube metadata names the Canadian Income Survey, survey number 5200, as the source survey. This is not the Canadian Community Health Survey.

Official note 22 states that, with the release of the 2024 CIS data, Statistics Canada revised estimates from 2018 to 2023 based on population counts from the 2021 Census.

## Processing
Every official row is kept. Columns were renamed to snake case, geography names were trimmed, and reference dates were written as the first day of the year. Published values were not changed. ISO 3166-2:CA and Standard Geographic Classification codes were added for Canada, the provinces and the territories.

The official STATUS symbol is copied into estimate_quality. The symbols A to F follow official note 2: A excellent (CV 0 to 2 percent), B very good (2 to 4), C good (4 to 8), D acceptable (8 to 16), E use with caution (16 to 33.3 percent), and F too unreliable to be published.

This table's Statistics dimension has only Number of persons and Percentage of persons. It does not include confidence intervals, so none are added.

## Derived columns
canada_value and gap_vs_canada use the Canada row with the same year, economic family type, food security status and statistic. gap_vs_canada is filled only on percentage rows. It is an adapted subtraction, not an official statistical test.

## Licence
This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 13-10-0834-01. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.
