# Methods note

Prepared by John Khan in Toronto, Ontario on 15 November 2026.

## Source
Public Health Agency of Canada, opioid and stimulant related harms.
Portal: https://open.canada.ca/data/en/dataset/1092497d-6c72-4e66-930b-9d6337e64af5
Download: https://health-infobase.canada.ca/src/data/substance-related-harms/download/HealthInfobase-SubstanceHarmsData.zip
The Open Government record, read on 15 November 2026, is licensed under the Open Government Licence Canada and gave a date modified of 2026-09-22.
The source README states that national figures are based on data reported as of 12 August 2026 and that the file was last updated 22 September 2026.

## Hospitalisation and emergency department measures
The source README states that the Canadian Institute for Health Information collected and provided the data used for reporting opioid- and stimulant-related poisoning hospitalisations and emergency department visits. This package does not include those two metrics, because a separate clearance to redistribute an Institute product was not obtained. Deaths (from chief coroners and chief medical examiners) and emergency medical services responses are kept.

## Processing
Only official rows with Source equal to Deaths or Emergency Medical Services (EMS) are kept. Column names were converted to snake case. The official Source column is labelled metric in this file to underline that the measures are separate and are not added together. Published values are kept in value_published. Suppr. is flagged and left empty in the numeric column. year and is_partial_period are taken from the published year_quarter label. as_of_date and file_updated_date are taken from the source README.

## Licence
This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Public Health Agency of Canada, SubstanceHarmsData.csv (deaths and EMS measures only). This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it.
