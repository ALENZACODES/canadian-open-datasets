# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Sources
Statistics Canada Table 13-10-0747-01, official release date 2026-02-27: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310074701
Full table CSV downloaded on 15 November 2026 and stream-filtered to Canada, the provinces and the territories.

## Official rates and the standard population
Table note 13 states that cancer incidence rates are age-standardized using the direct method and the final 2021 Canadian postcensal population structure. Age-standardization allows comparisons of incidence rates over time that are unaffected by changes in the age distribution of the population. This package keeps those official rates. It does not compute rates from counts.

Official 95% confidence intervals are kept with the rates. Table note 14 describes how those official intervals were calculated.

## Counts, rounding and suppression
Table note 15 states that case counts are randomly rounded to a lower or higher multiple of 5, and that official age-standardized rates and confidence limits are calculated using the unrounded case counts. Official status codes are kept: x for figures suppressed to meet the confidentiality requirements of the Statistics Act, and .. for figures not available for a specific reference period (table note 16).

Table note 22 states that case counts may not match table 13-10-0111 because cases with unknown age group are excluded here, as they cannot be included in age-standardized rates.

## Coverage note
Table note 20 states that Nova Scotia cancer incidence data are not available for diagnosis years after 2019, and that annual case counts and rate estimates for Nova Scotia and for Canada for the 2020 diagnosis year onward are not provided in this table. Those official empty cells are kept.

## Processing
Published values were not changed. Columns were renamed to snake case, geography names were trimmed, and ISO 3166-2:CA and Standard Geographic Classification codes were added. Counts, age-standardized rates and average age at diagnosis are stored as separate official measures.

## Licence
This dataset contains information licensed under the Statistics Canada Open Licence (https://www.statcan.gc.ca/en/reference/licence). Source: Statistics Canada, Table 13-10-0747. This file is adapted from Statistics Canada official tables. Published values were not changed. Derived columns, such as shares, gaps, indexes or per capita figures, are calculated here and are not official Statistics Canada estimates. This is not an official Statistics Canada product and Statistics Canada does not endorse it.
