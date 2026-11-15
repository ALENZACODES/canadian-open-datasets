<p align="center"><img src="../../assets/theme-public-safety.png" alt="Toronto 311 Service Requests 2020 to 2026" width="100%"></p>

# Toronto 311 Service Requests 2020 to 2026

*Monthly counts by division, type, ward and postal FSA*

**Theme:** [Public safety and city services](../../README.md#public-safety-and-city-services) · **Coverage:** 2020 to 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/toronto-311-service-requests](https://www.kaggle.com/datasets/johnnykhan1/toronto-311-service-requests)

## What it is

Customer-initiated 311 Toronto service requests from 2020 through 2026, rolled up by month, City division, request type, status, ward and postal FSA. The official yearly files include intersection street names. Those streets are not in this version.

2,761,000 customer-initiated 311 requests, 2020 to 2026. Intersection streets were dropped.

311 Toronto takes requests for Solid Waste Management, Transportation Services, Toronto Water, Municipal Licensing and Standards, and Urban Forestry, among other divisions. Channels include telephone, fax, email, online self-serve, mobile and (in earlier years) Twitter, as described on the City catalogue page.

## Who it helps

Residents, community groups, road safety advocates, city councillors, reporters and researchers in Toronto and other Canadian cities.

## Files

| File | Size | Where |
|---|---:|---|
| [`cover.png`](data/cover.png) | 49 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 2 KB | in this repository |
| [`sr311_citywide_monthly.csv`](data/sr311_citywide_monthly.csv) | 2 KB | in this repository |
| [`sr311_monthly_by_division.csv`](data/sr311_monthly_by_division.csv) | 19 KB | in this repository |
| [`sr311_monthly_by_request_type.csv`](data/sr311_monthly_by_request_type.csv) | 1.6 MB | in this repository |
| [`sr311_monthly_by_ward.csv`](data/sr311_monthly_by_ward.csv) | 82 KB | in this repository |
| `sr311_monthly_detail.csv` | 138.1 MB (5.9 MB gzipped) | [release download](https://github.com/ALENZACODES/canadian-open-datasets/releases/download/data-2026-11-15/toronto-311-service-requests--sr311_monthly_detail.csv.gz) |

Files over 50 MB are kept as gzipped downloads on the [release page](https://github.com/ALENZACODES/canadian-open-datasets/releases/tag/data-2026-11-15) so the repository stays light. Unzip with `gunzip` or read directly with `pandas.read_csv(url)`.

## Columns

### `data_dictionary.csv`

Column descriptions for every file.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `sr311_citywide_monthly.csv`

Citywide monthly request counts.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year the request was created. |
| `month_num` | Integer | Month number from 1 to 12. |
| `month` | Date | Year and month (YYYY-MM). |
| `requests` | Integer | Number of customer-initiated requests in the group. |

### `sr311_monthly_by_division.csv`

Monthly counts by City division.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year the request was created. |
| `month` | Date | Year and month (YYYY-MM). |
| `division` | Text | City division that owns the request, as published. |
| `requests` | Integer | Number of customer-initiated requests in the group. |

### `sr311_monthly_by_request_type.csv`

Monthly counts by service request type.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year the request was created. |
| `month` | Date | Year and month (YYYY-MM). |
| `service_request_type` | Text | Service request type, as published. |
| `requests` | Integer | Number of customer-initiated requests in the group. |

### `sr311_monthly_by_ward.csv`

Monthly counts by ward.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year the request was created. |
| `month` | Date | Year and month (YYYY-MM). |
| `ward` | Text | City ward as published. |
| `requests` | Integer | Number of customer-initiated requests in the group. |

### `sr311_monthly_detail.csv`

Monthly request counts by division, section, type, status, ward and FSA. Intersection streets are not included.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Year the request was created. |
| `month_num` | Integer | Month number from 1 to 12. |
| `month` | Date | Year and month (YYYY-MM). |
| `division` | Text | City division that owns the request, as published. |
| `section` | Text | Section within the division, as published. |
| `service_request_type` | Text | Service request type, as published. |
| `status` | Text | Request status at the time of the extract. |
| `ward` | Text | City ward as published. |
| `fsa` | Text | First three characters of the postal code (forward sortation area). |
| `requests` | Integer | Number of customer-initiated requests in the group. |

## Source and licence

**Source:** City of Toronto Open Data, 311 Service Requests - Customer Initiated (https://open.toronto.ca/dataset/311-service-requests-customer-initiated/), years 2020 to 2026. Collected by John Khan on 2026-11-09. Contains information licensed under the Open Government Licence – Toronto.

- **Licence:** [Open Government Licence – Toronto](https://open.toronto.ca/open-data-licence/). Contains information licensed under the Open Government Licence – Toronto.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026toronto311servicerequests,
  author    = {Khan, John},
  title     = {Toronto 311 Service Requests 2020 to 2026},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/toronto-311-service-requests}
}
```

APA: Khan, J. (2026). *Toronto 311 Service Requests 2020 to 2026* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/toronto-311-service-requests

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Customer-initiated 311 Toronto service requests from 2020 through 2026, rolled up by month, City division, request type, status, ward and postal FSA. The official yearly files include intersection street names. Those streets are not in this version.

2,761,000 customer-initiated 311 requests, 2020 to 2026. Intersection streets were dropped.

311 Toronto takes requests for Solid Waste Management, Transportation Services, Toronto Water, Municipal Licensing and Standards, and Urban Forestry, among other divisions. Channels include telephone, fax, email, online self-serve, mobile and (in earlier years) Twitter, as described on the City catalogue page.

## Files

| File | What is in it |
|---|---|
| `sr311_monthly_detail.csv` | Monthly counts by division, section, type, status, ward and FSA |
| `sr311_citywide_monthly.csv` | Citywide monthly totals |
| `sr311_monthly_by_division.csv` | Monthly totals by division |
| `sr311_monthly_by_request_type.csv` | Monthly totals by request type |
| `sr311_monthly_by_ward.csv` | Monthly totals by ward |
| `data_dictionary.csv` | Column descriptions |
| `cover.png` | Cover image drawn from the annual totals |

## Coverage and refresh

Pulled on November 9, 2026 from the City of Toronto Open Data yearly zip files for 2020 through 2026. The 2026 file is a year-to-date extract and will grow as the year continues. Status is the status at the time of each yearly extract, not a live status.

## Caveats

* These are customer-initiated requests received by 311, not every piece of work a City crew does.
* Ward names follow the City's published label for that year. Ward models can change, so compare ward names carefully across years.
* FSA is only the first three characters of the postal code. Some rows have no FSA or no ward.
* Intersection streets were dropped and are not recoverable from this file.

## Sources

311 Service Requests, Customer Initiated: https://open.toronto.ca/dataset/311-service-requests-customer-initiated/

Pulled on November 9, 2026.

## Example uses

* Follow seasonal spikes in a request type such as water or waste.
* Compare request volumes across wards and divisions.
* Join FSAs to other Toronto or census files that use the same three-character postal codes.

## Licence

Contains information licensed under the Open Government Licence – Toronto (https://open.toronto.ca/open-data-licence/). This dataset is not endorsed by the City of Toronto.

Changes made here: yearly request files were aggregated to monthly counts, intersection streets were dropped, and columns were renamed to snake_case. Request counts were not altered.

Author: John Khan. Location: Toronto, Ontario.


</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
