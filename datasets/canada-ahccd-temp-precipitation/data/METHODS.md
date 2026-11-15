# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Sources
Environment and Climate Change Canada, Adjusted and Homogenized Canadian Climate Data (AHCCD), official daily bulk files on the CDAS directory: https://crd-data-donnees-rdc.ec.gc.ca/CDAS/products/EC_data/AHCCD_daily/

Temperature, third generation, update to 2023:
- Homog_daily_mean_temp_v2023_Gen3.zip
- Homog_daily_max_temp_v2023_Gen3.zip
- Homog_daily_min_temp_v2023_Gen3.zip
- Temperature_Stations_Gen3_2023.xlsx, titled Third Generation Homogenized Temperature for Canada - update to 2023

Precipitation, second generation, updated to December 2017:
- Adj_Daily_Total_v2017.zip
- Adj_Precipitation_Stations.xls, titled Historical adjusted precipitation stations for Canada - Updated to December 2017

Files were downloaded on 15 November 2026. The two products have different generations and different end years.

## Homogenisation and adjustment
The official temperature product is described as third-generation homogenized temperature. The official precipitation product is described as daily adjusted precipitation. Official station lists and daily file headers record whether a station is joined (a composite record) or not joined. Those official flags are kept. Temperature and precipitation are not the same generation and do not share the same end year.

## Annual completeness rule
The official source is daily. Annual temperature values are the mean of official non-missing daily values in the calendar year. Annual precipitation values are the sum of official non-missing daily values in the calendar year. A year is used only when official non-missing daily values cover at least 80% of the calendar days in that year (365 or 366). Otherwise the annual value is left blank and completeness_met is false. The 80% threshold is stated here; it is not an official AHCCD cutoff published in the station files.

Official missing days are those with the published missing sentinel (about -9999.9 or -9999.99) or with flag M. Official observation flags on non-missing days are not treated as missing. Flag meanings beyond the missing sentinel are not invented here. The official daily example file keeps the published flag characters.

## No anomalies
No anomaly or departure-from-normal series is included, because a baseline period and a completeness rule for that baseline were not taken from an official AHCCD anomaly product in this snapshot.

## Licence
This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, Adjusted and Homogenized Canadian Climate Data (AHCCD) daily temperature and precipitation. This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.
