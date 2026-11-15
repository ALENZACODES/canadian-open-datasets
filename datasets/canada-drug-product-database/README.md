<p align="center"><img src="../../assets/theme-health.png" alt="Canada Drug Product Database" width="100%"></p>

# Canada Drug Product Database

*Health Canada DPD products, ingredients, forms and status*

**Theme:** [Health, disability and wellbeing](../../README.md#health-disability-and-wellbeing) · **Coverage:** Snapshot of 9 November 2026 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-drug-product-database](https://www.kaggle.com/datasets/johnnykhan1/canada-drug-product-database)

## What it is

Analysis-ready tables from the Health Canada Drug Product Database (DPD): products, active ingredients, pharmaceutical forms, routes of administration, schedules and status history. Tables join on drug_code.

Documentation: [DPD API](https://health-products.canada.ca/api/documentation/dpd-documentation-en.html).

## Who it helps

Patients and caregivers, disability advocates, public health teams, pharmacists, food security groups and health researchers.

## Files

| File | Size | Where |
|---|---:|---|
| [`active_ingredients.csv`](data/active_ingredients.csv) | 4.3 MB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 3 KB | in this repository |
| [`drug_products.csv`](data/drug_products.csv) | 8.0 MB | in this repository |
| [`pharmaceutical_forms.csv`](data/pharmaceutical_forms.csv) | 1.1 MB | in this repository |
| [`routes_of_administration.csv`](data/routes_of_administration.csv) | 1.3 MB | in this repository |
| [`schedules.csv`](data/schedules.csv) | 1.4 MB | in this repository |
| [`status_history.csv`](data/status_history.csv) | 2.9 MB | in this repository |

## Columns

### `active_ingredients.csv`

Active ingredients linked by drug_code.

| Column | Type | Description |
|---|---|---|
| `dosage_unit` | Text | Dosage unit for the active ingredient strength. |
| `dosage_value` | Float | Dosage value for the active ingredient. |
| `drug_code` | Integer | Health Canada drug code linking product, ingredient, form, route and status tables. |
| `ingredient_name` | Text | Active ingredient name. |
| `strength` | Float | Strength value. |
| `strength_unit` | Text | Strength unit. |

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `drug_products.csv`

Drug products with latest status fields joined on drug_code.

| Column | Type | Description |
|---|---|---|
| `drug_code` | Integer | Health Canada drug code linking product, ingredient, form, route and status tables. |
| `class_name` | Text | Product class such as Human, Veterinary or Disinfectant. |
| `drug_identification_number` | Integer | Drug Identification Number (DIN) when assigned. |
| `brand_name` | Text | Brand name of the drug product. |
| `descriptor` | Text | Optional descriptor text from the database. |
| `number_of_ais` | Integer | Number of active ingredients reported for the product. |
| `ai_group_no` | Integer | Active ingredient group number. |
| `company_name` | Text | Company name associated with the product. |
| `last_update_date` | Date | Last update date in the Drug Product Database extract. |
| `status` | Text | Latest market status for the product (from status history). |
| `history_date` | Date | Date attached to the status record. |
| `original_market_date` | Date | Original market date when provided. |
| `expiration_date` | Date | Expiration date when provided. |

### `pharmaceutical_forms.csv`

Pharmaceutical forms linked by drug_code.

| Column | Type | Description |
|---|---|---|
| `drug_code` | Integer | Health Canada drug code linking product, ingredient, form, route and status tables. |
| `pharmaceutical_form_code` | Integer | Code for the pharmaceutical form. |
| `pharmaceutical_form_name` | Text | Pharmaceutical form name such as tablet or cream. |

### `routes_of_administration.csv`

Routes of administration linked by drug_code.

| Column | Type | Description |
|---|---|---|
| `drug_code` | Integer | Health Canada drug code linking product, ingredient, form, route and status tables. |
| `route_of_administration_code` | Integer | Code for the route of administration. |
| `route_of_administration_name` | Text | Route of administration name such as oral or topical. |

### `schedules.csv`

Schedule classifications linked by drug_code.

| Column | Type | Description |
|---|---|---|
| `drug_code` | Integer | Health Canada drug code linking product, ingredient, form, route and status tables. |
| `schedule_name` | Text | Schedule classification when present. |

### `status_history.csv`

Full status history linked by drug_code.

| Column | Type | Description |
|---|---|---|
| `drug_code` | Integer | Health Canada drug code linking product, ingredient, form, route and status tables. |
| `status` | Text | Latest market status for the product (from status history). |
| `history_date` | Date | Date attached to the status record. |
| `original_market_date` | Date | Original market date when provided. |
| `external_status_code` | Integer | External status code from Health Canada. |
| `expiration_date` | Text | Expiration date when provided. |
| `lot_number` | Text | Lot number when present on a status record. |

## Source and licence

**Source:** Health Canada Drug Product Database API (https://health-products.canada.ca/api/documentation/dpd-documentation-en.html), also listed on open.canada.ca dataset bf55e42a-63cb-4556-bfd8-44f26e5a36fe. Pulled November 9, 2026. Prepared by John Khan in Toronto, Ontario. Open Government Licence – Canada: https://open.canada.ca/en/open-government-licence-canada. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadadrugproductdatabase,
  author    = {Khan, John},
  title     = {Canada Drug Product Database},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-drug-product-database}
}
```

APA: Khan, J. (2026). *Canada Drug Product Database* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-drug-product-database

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Analysis-ready tables from the Health Canada Drug Product Database (DPD): products, active ingredients, pharmaceutical forms, routes of administration, schedules and status history. Tables join on drug_code.

Documentation: [DPD API](https://health-products.canada.ca/api/documentation/dpd-documentation-en.html).

## Coverage

Full API extract as of November 9, 2026. Product count in this snapshot: 58,414.

## Updates

Snapshot from November 9, 2026. Health Canada updates the DPD continuously. This upload is not auto refreshed.

## A few numbers from this snapshot

* drug_products.csv has 58,414 products.
* active_ingredients.csv has 121,003 ingredient rows.
* Class mix: Human 51074, Disinfectant 3817, Veterinary 3360, Radiopharmaceutical 163.

## Example uses

* Look up active ingredients by brand name or DIN.
* Build features for pharmacovigilance or formulary analysis.
* Compare human and veterinary product inventories.

## Caveats

* Status in drug_products.csv is the latest history row by history_date, not a separate official current-status feed.
* Some free-text fields are empty. Strength and dosage fields are strings as published.
* This is a snapshot of the public API, not a substitute for the official DPD search for regulatory decisions.

## Licence

Shared under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). Source: Health Canada. Not an official Health Canada product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
