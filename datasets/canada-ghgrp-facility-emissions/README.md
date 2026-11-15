<p align="center"><img src="../../assets/theme-environment.png" alt="Canada GHGRP facility emissions" width="100%"></p>

# Canada GHGRP facility emissions

*Facility greenhouse gas reports by gas and source, 2004 to 2024*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 2004 to 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-ghgrp-facility-emissions](https://www.kaggle.com/datasets/johnnykhan1/canada-ghgrp-facility-emissions)

## What it is

A tidy extract of Environment and Climate Change Canada's Greenhouse Gas Reporting Program (GHGRP) facility emissions tables: one row per facility and year with emissions by gas, and a companion table of emissions by official source category for 2022 to 2024. Public contact names, telephone numbers, emails and mailing addresses that appear in the official files are not included in this extract.

Source dataset: [Greenhouse Gas Reporting Program (GHGRP), Greenhouse Gas (GHG) Emissions Data by Facility](https://open.canada.ca/data/en/dataset/a8ba14b7-7f23-462a-bdbb-83b0ef629823) (Environment and Climate Change Canada). Official CSV files were downloaded from the ECCC data mart on November 9, 2026. The files on the mart are dated 24 July 2026, and the official readme states that the data are current as of October 2, 2025. Coverage in these files is 2004 to 2024. Program overview: https://www.canada.ca/en/environment-climate-change/services/climate-change/greenhouse-gas-emissions/facility-reporting/overview-2024.html.

This is a different product from the National Pollutant Release Inventory air releases set already on Kaggle. An NPRI identifier is included when the official file provides one, so the two can be joined where that identifier is present.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`annual_totals.csv`](data/annual_totals.csv) | 3 KB | in this repository |
| [`annual_totals_by_province.csv`](data/annual_totals_by_province.csv) | 9 KB | in this repository |
| [`cover.png`](data/cover.png) | 57 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 12 KB | in this repository |
| [`emissions_by_gas.csv`](data/emissions_by_gas.csv) | 8.4 MB | in this repository |
| [`emissions_by_source.csv`](data/emissions_by_source.csv) | 3.4 MB | in this repository |

## Columns

### `annual_totals.csv`

National sums of facility-reported emissions and the count of reporting facilities, by year.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Reporting (reference) year as published. |
| `n_facilities` | Integer | Count of distinct GHGRP facility identifiers in the group. |
| `total_emissions_tonnes_co2e` | Float | Official facility total in tonnes of carbon dioxide equivalent, excluding carbon dioxide from biomass combustion. |
| `co2_tonnes` | Float | Carbon dioxide emissions in tonnes. This is not a CO2 equivalent figure. |
| `ch4_tonnes_co2e` | Float | Methane emissions in tonnes of carbon dioxide equivalent, using AR5 global warming potentials as stated by ECCC. |
| `n2o_tonnes_co2e` | Float | Nitrous oxide emissions in tonnes of carbon dioxide equivalent, using AR5 global warming potentials as stated by ECCC. |
| `hfc_total_tonnes_co2e` | Float | Total hydrofluorocarbon emissions in tonnes of carbon dioxide equivalent, as published. |
| `pfc_total_tonnes_co2e` | Float | Total perfluorocarbon emissions in tonnes of carbon dioxide equivalent, as published. |
| `sf6_tonnes_co2e` | Float | Sulphur hexafluoride emissions in tonnes of carbon dioxide equivalent, when reported. |
| `co2_biomass_tonnes` | Float | Carbon dioxide from biomass combustion in tonnes. Official totals exclude this quantity. |

### `annual_totals_by_province.csv`

Sums of facility-reported emissions and facility counts by year and province or territory.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Reporting (reference) year as published. |
| `province_territory` | Text | Province or territory of the facility as published. |
| `n_facilities` | Integer | Count of distinct GHGRP facility identifiers in the group. |
| `total_emissions_tonnes_co2e` | Float | Official facility total in tonnes of carbon dioxide equivalent, excluding carbon dioxide from biomass combustion. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `file` | Text | CSV file the column belongs to. |
| `column` | Text | Column name in that file. |
| `type` | Text | Field type (datetime, string, number or integer). |
| `description` | Text | What the column contains. |

### `emissions_by_gas.csv`

One row per reporting facility and year, with emissions by gas and the official total excluding biomass CO2. Public contact fields from the official file are not included.

| Column | Type | Description |
|---|---|---|
| `ghgrp_id` | Text | Official Greenhouse Gas Reporting Program facility identifier. |
| `year` | Integer | Reporting (reference) year as published. |
| `facility_name` | Text | Facility name as published. |
| `facility_location` | Text | Facility street location as published, when given. |
| `city` | Text | Facility city, district or municipality as published. |
| `province_territory` | Text | Province or territory of the facility as published. |
| `postal_code` | Text | Facility postal code as published, when given. |
| `latitude` | Text | Facility latitude in decimal degrees as published. |
| `longitude` | Text | Facility longitude in decimal degrees as published. |
| `npri_id` | Float | National Pollutant Release Inventory identifier when the facility also reports to the NPRI. |
| `naics_code` | Integer | North American Industry Classification System code as published for the facility. |
| `naics_description` | Text | Official English description of the facility NAICS code. |
| `company_legal_name` | Text | Legal name of the reporting company as published. |
| `company_trade_name` | Text | Trade name of the reporting company as published, when given. |
| `company_business_number` | Float | Reporting company business number as published, when given. |
| `co2_tonnes` | Float | Carbon dioxide emissions in tonnes. This is not a CO2 equivalent figure. |
| `ch4_tonnes` | Float | Methane emissions in tonnes. |
| `ch4_tonnes_co2e` | Float | Methane emissions in tonnes of carbon dioxide equivalent, using AR5 global warming potentials as stated by ECCC. |
| `n2o_tonnes` | Float | Nitrous oxide emissions in tonnes. |
| `n2o_tonnes_co2e` | Float | Nitrous oxide emissions in tonnes of carbon dioxide equivalent, using AR5 global warming potentials as stated by ECCC. |
| `co2_biomass_tonnes` | Text | Carbon dioxide from biomass combustion in tonnes. Official totals exclude this quantity. |
| `hfc_23_tonnes` | Float | HFC-23 emissions in tonnes, when reported. |
| `hfc_23_tonnes_co2e` | Float | HFC-23 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_32_tonnes` | Text | HFC-32 emissions in tonnes, when reported. |
| `hfc_32_tonnes_co2e` | Text | HFC-32 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_41_tonnes` | Text | HFC-41 emissions in tonnes, when reported. |
| `hfc_41_tonnes_co2e` | Text | HFC-41 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_43_10mee_tonnes` | Text | HFC-43-10mee emissions in tonnes, when reported. |
| `hfc_43_10mee_tonnes_co2e` | Text | HFC-43-10mee emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_125_tonnes` | Float | HFC-125 emissions in tonnes, when reported. |
| `hfc_125_tonnes_co2e` | Float | HFC-125 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_134_tonnes` | Float | HFC-134 emissions in tonnes, when reported. |
| `hfc_134_tonnes_co2e` | Float | HFC-134 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_134a_tonnes` | Float | HFC-134a emissions in tonnes, when reported. |
| `hfc_134a_tonnes_co2e` | Float | HFC-134a emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_143_tonnes` | Text | HFC-143 emissions in tonnes, when reported. |
| `hfc_143_tonnes_co2e` | Text | HFC-143 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_143a_tonnes` | Float | HFC-143a emissions in tonnes, when reported. |
| `hfc_143a_tonnes_co2e` | Float | HFC-143a emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_152a_tonnes` | Float | HFC-152a emissions in tonnes, when reported. |
| `hfc_152a_tonnes_co2e` | Float | HFC-152a emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_227ea_tonnes` | Float | HFC-227ea emissions in tonnes, when reported. |
| `hfc_227ea_tonnes_co2e` | Float | HFC-227ea emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_236fa_tonnes` | Text | HFC-236fa emissions in tonnes, when reported. |
| `hfc_236fa_tonnes_co2e` | Text | HFC-236fa emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_245ca_tonnes` | Text | HFC-245ca emissions in tonnes, when reported. |
| `hfc_245ca_tonnes_co2e` | Text | HFC-245ca emissions in tonnes of carbon dioxide equivalent, when reported. |
| `hfc_total_tonnes_co2e` | Float | Total hydrofluorocarbon emissions in tonnes of carbon dioxide equivalent, as published. |
| `cf4_tonnes` | Float | CF4 emissions in tonnes, when reported. |
| `cf4_tonnes_co2e` | Float | CF4 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `c2f6_tonnes` | Float | C2F6 emissions in tonnes, when reported. |
| `c2f6_tonnes_co2e` | Float | C2F6 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `c3f8_tonnes` | Text | C3F8 emissions in tonnes, when reported. |
| `c3f8_tonnes_co2e` | Text | C3F8 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `c4f10_tonnes` | Text | C4F10 emissions in tonnes, when reported. |
| `c4f10_tonnes_co2e` | Text | C4F10 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `c4f8_tonnes` | Text | C4F8 emissions in tonnes, when reported. |
| `c4f8_tonnes_co2e` | Text | C4F8 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `c5f12_tonnes` | Text | C5F12 emissions in tonnes, when reported. |
| `c5f12_tonnes_co2e` | Text | C5F12 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `c6f14_tonnes` | Text | C6F14 emissions in tonnes, when reported. |
| `c6f14_tonnes_co2e` | Text | C6F14 emissions in tonnes of carbon dioxide equivalent, when reported. |
| `pfc_total_tonnes_co2e` | Float | Total perfluorocarbon emissions in tonnes of carbon dioxide equivalent, as published. |
| `sf6_tonnes` | Float | Sulphur hexafluoride emissions in tonnes, when reported. |
| `sf6_tonnes_co2e` | Float | Sulphur hexafluoride emissions in tonnes of carbon dioxide equivalent, when reported. |
| `total_emissions_tonnes_co2e` | Float | Official facility total in tonnes of carbon dioxide equivalent, excluding carbon dioxide from biomass combustion. |
| `ghgrp_quantification_requirements` | Text | Whether GHGRP quantification requirements were used, as published. |
| `uses_emission_factors` | Text | Whether emission factors were used, as published. |
| `uses_engineering_estimates` | Text | Whether engineering estimates were used, as published. |
| `uses_mass_balance` | Text | Whether mass balance was used, as published. |
| `uses_monitoring_or_direct_measurement` | Text | Whether monitoring or direct measurement was used, as published. |

### `emissions_by_source.csv`

One row per facility, year and official emission source category, for 2022 to 2024. Public contact fields are not included.

| Column | Type | Description |
|---|---|---|
| `ghgrp_id` | Text | Official Greenhouse Gas Reporting Program facility identifier. |
| `year` | Integer | Reporting (reference) year as published. |
| `facility_name` | Text | Facility name as published. |
| `province_territory` | Text | Province or territory of the facility as published. |
| `naics_code` | Integer | North American Industry Classification System code as published for the facility. |
| `naics_description` | Text | Official English description of the facility NAICS code. |
| `emission_source` | Text | Official emission source code as published in the by-source file. |
| `emission_source_description` | Text | Plain English label matching the official emission source category described in the ECCC readme. |
| `co2_tonnes` | Float | Carbon dioxide emissions in tonnes. This is not a CO2 equivalent figure. |
| `ch4_tonnes` | Float | Methane emissions in tonnes. |
| `ch4_tonnes_co2e` | Float | Methane emissions in tonnes of carbon dioxide equivalent, using AR5 global warming potentials as stated by ECCC. |
| `n2o_tonnes` | Float | Nitrous oxide emissions in tonnes. |
| `n2o_tonnes_co2e` | Float | Nitrous oxide emissions in tonnes of carbon dioxide equivalent, using AR5 global warming potentials as stated by ECCC. |
| `co2_biomass_tonnes` | Float | Carbon dioxide from biomass combustion in tonnes. Official totals exclude this quantity. |
| `hfc_total_tonnes_co2e` | Float | Total hydrofluorocarbon emissions in tonnes of carbon dioxide equivalent, as published. |
| `pfc_total_tonnes_co2e` | Float | Total perfluorocarbon emissions in tonnes of carbon dioxide equivalent, as published. |
| `sf6_tonnes` | Float | Sulphur hexafluoride emissions in tonnes, when reported. |
| `sf6_tonnes_co2e` | Float | Sulphur hexafluoride emissions in tonnes of carbon dioxide equivalent, when reported. |
| `total_emissions_from_source_tonnes_co2e` | Float | Official total for this source category in tonnes of carbon dioxide equivalent, excluding biomass CO2. |
| `total_facility_emissions_tonnes_co2e` | Float | Official facility total for the year in tonnes of carbon dioxide equivalent, repeated on each source row. Do not sum this column across sources. |

## Source and licence

**Source:** Environment and Climate Change Canada, Greenhouse Gas Reporting Program (GHGRP) Greenhouse Gas Emissions Data by Facility, https://open.canada.ca/data/en/dataset/a8ba14b7-7f23-462a-bdbb-83b0ef629823. Emissions by gas file PDGES-GHGRP-GHGEmissionsGES-2004-Present.csv and emissions by source file PDGES-GHGRP-GHGEmissionsSourcesGES-2022-Present.csv, downloaded from the ECCC data mart on November 9, 2026 (files dated 24 July 2026 on the mart). Official files: https://data-donnees.az.ec.gc.ca/api/file?path=%2Fsubstances%2Fmonitor%2Fgreenhouse-gas-reporting-program-ghgrp-facility-greenhouse-gas-ghg-data%2FPDGES-GHGRP-GHGEmissionsGES-2004-Present.csv and https://data-donnees.az.ec.gc.ca/api/file?path=%2Fsubstances%2Fmonitor%2Fgreenhouse-gas-reporting-program-ghgrp-facility-greenhouse-gas-ghg-data%2FPDGES-GHGRP-GHGEmissionsSourcesGES-2022-Present.csv. Program page: https://www.canada.ca/en/environment-climate-change/services/climate-change/greenhouse-gas-emissions/facility-reporting/about.html. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaghgrpfacilityemissions,
  author    = {Khan, John},
  title     = {Canada GHGRP facility emissions},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-ghgrp-facility-emissions}
}
```

APA: Khan, J. (2026). *Canada GHGRP facility emissions* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ghgrp-facility-emissions

<details><summary>Full notes from the Kaggle page</summary>

## What this is

A tidy extract of Environment and Climate Change Canada's Greenhouse Gas Reporting Program (GHGRP) facility emissions tables: one row per facility and year with emissions by gas, and a companion table of emissions by official source category for 2022 to 2024. Public contact names, telephone numbers, emails and mailing addresses that appear in the official files are not included in this extract.

Source dataset: [Greenhouse Gas Reporting Program (GHGRP), Greenhouse Gas (GHG) Emissions Data by Facility](https://open.canada.ca/data/en/dataset/a8ba14b7-7f23-462a-bdbb-83b0ef629823) (Environment and Climate Change Canada). Official CSV files were downloaded from the ECCC data mart on November 9, 2026. The files on the mart are dated 24 July 2026, and the official readme states that the data are current as of October 2, 2025. Coverage in these files is 2004 to 2024. Program overview: https://www.canada.ca/en/environment-climate-change/services/climate-change/greenhouse-gas-emissions/facility-reporting/overview-2024.html.

This is a different product from the National Pollutant Release Inventory air releases set already on Kaggle. An NPRI identifier is included when the official file provides one, so the two can be joined where that identifier is present.

## Coverage

20,685 facility-year rows and 2,843 distinct facility identifiers, for reporting years 2004 to 2024.

In 2024, 1,879 facilities reported a combined official total of 291,662,283 tonnes of carbon dioxide equivalent, excluding carbon dioxide from biomass combustion. In 2023, 1,878 facilities reported 290,675,532 tonnes. The 2024 provincial and territorial totals from this snapshot are: Alberta 152,735,453 tonnes (769 facilities), Ontario 50,975,459 tonnes (418 facilities), Saskatchewan 27,582,626 tonnes (142 facilities), Quebec 21,855,685 tonnes (202 facilities), British Columbia 17,609,700 tonnes (230 facilities), New Brunswick 7,250,282 tonnes (24 facilities), Nova Scotia 6,157,451 tonnes (21 facilities), Newfoundland and Labrador 3,683,023 tonnes (15 facilities), Manitoba 2,365,746 tonnes (37 facilities), Nunavut 705,363 tonnes (8 facilities), Northwest Territories 636,299 tonnes (8 facilities), Prince Edward Island 53,189 tonnes (3 facilities), Yukon 52,007 tonnes (2 facilities).

The count of reporting facilities rose from 617 in 2016 to 1,710 in 2017. The official readme notes that the number of reporting facilities varies from year to year because of program changes (for example lower reporting thresholds), facility start-ups and closures, and improved compliance. Totals across those years are not a like-for-like survey of the same facilities.

The by-source table has 17,151 rows covering 5,602 facility-years from 2022 to 2024, with 9 official source codes. Row counts by official source code: EC_GeneralStationaryCombustionEmissions 5221, EC_OnSiteTransportationEmissions 2431, EC_FugitiveEmissions 2313, EC_FlaringEmissions 2234, EC_VentingEmissions 2143, EC_CO2BiomassCombustion 854, EC_IndustrialProcessEmissions 781, EC_WasteEmissions 666, EC_WastewaterEmissions 428.

## Updates

This upload is a snapshot of the official files dated 24 July 2026, pulled on November 9, 2026, and is not refreshed on a schedule. ECCC states that ongoing analyses may lead to periodic updates. For a later extract, use the official open data record or the ECCC data mart.

## Methodology

Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

## A few numbers from this snapshot

* 1,879 facilities reported in 2024, with an official total of 291,662,283 tonnes of carbon dioxide equivalent excluding biomass CO2.
* Alberta accounted for 152,735,453 tonnes of that 2024 official total, from 769 facilities.
* The by-gas table spans 2004 to 2024 and contains 20,685 facility-year rows.

## Example uses

* Chart the official national facility total by year, taking the 2017 change in reporting numbers into account.
* Compare 2024 provincial totals, or rank facilities within a province and NAICS code.
* Join the by-source table to see how a facility's 2022 to 2024 total is split across official source categories.

## Caveats

The official files include 2,944 facility-year rows with latitude and longitude both equal to 0, and 77 rows with a missing coordinate. Those values are kept as published; they are not missing conversions.


These are facility-reported values for facilities that meet the program's reporting rules, not Canada's official national greenhouse gas inventory. ECCC states that all data in the file are for information purposes only, that data checks have been done for compliance and completeness, and that carbon dioxide equivalent values use global warming potentials from the IPCC Fifth Assessment Report across the whole time series.

The official total column excludes carbon dioxide from biomass combustion, which is provided in a separate column and is present from the 2022 reporting year onward. Do not add biomass CO2 into the official total if you want to stay consistent with ECCC's published total.

The official by-source file excludes information treated as confidential under sections 51 to 53 of the Canadian Environmental Protection Act, 1999, and covers most reporting facilities. The facility-year total on each by-source row is repeated; do not sum that facility-total column across source categories.

Public contact details were removed from this extract. Company and facility names, locations and business identifiers are kept as published.

## Licence

Contains information licensed under the [Open Government Licence Canada](https://open.canada.ca/en/open-government-licence-canada).

## Files

* `emissions_by_gas.csv`: one row per facility and year, with emissions by gas.
* `emissions_by_source.csv`: one row per facility, year and official source category, 2022 to 2024.
* `annual_totals.csv`: national sums and facility counts by year.
* `annual_totals_by_province.csv`: sums and facility counts by year and province or territory.
* `data_dictionary.csv`: column dictionary.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
