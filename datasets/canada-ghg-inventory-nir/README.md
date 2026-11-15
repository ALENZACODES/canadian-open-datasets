<p align="center"><img src="../../assets/theme-environment.png" alt="Canada greenhouse gas inventory" width="100%"></p>

# Canada greenhouse gas inventory

*Official inventory by province and IPCC sector, 1990 to 2024*

**Theme:** [Environment, climate and natural hazards](../../README.md#environment-climate-and-natural-hazards) · **Coverage:** 1990 to 2024 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-ghg-inventory-nir](https://www.kaggle.com/datasets/johnnykhan1/canada-ghg-inventory-nir)

## What it is

Canada's official greenhouse gas inventory, tidied from the IPCC sector file on the [Open Government portal](https://open.canada.ca/data/en/dataset/779c7bcf-4982-47eb-af1b-a33618a05e5b). The detail file keeps the official sector tree and adds sector_level, is_subtotal, a LULUCF treatment label, the GWP set, and a flag for the pre-1999 combined territories series. A totals file keeps the official inventory total, which excludes land use, land use change and forestry, and adds a 1990 index (base year 1990) and tonnes per person using matched July 1 population.

## Who it helps

Climate researchers, farmers, emergency planners, insurers, conservation groups, teachers and students.

## Files

| File | Size | Where |
|---|---:|---|
| [`CITATION.txt`](data/CITATION.txt) | 1 KB | in this repository |
| [`METHODS.md`](data/METHODS.md) | 3 KB | in this repository |
| [`SOURCE_MANIFEST.csv`](data/SOURCE_MANIFEST.csv) | 1 KB | in this repository |
| [`cover.png`](data/cover.png) | 65 KB | in this repository |
| [`data_dictionary.csv`](data/data_dictionary.csv) | 9 KB | in this repository |
| [`ghg_inventory_detail.csv`](data/ghg_inventory_detail.csv) | 13.2 MB | in this repository |
| [`ghg_inventory_totals.csv`](data/ghg_inventory_totals.csv) | 173 KB | in this repository |

## Columns

### `SOURCE_MANIFEST.csv`

Source identifiers, official dates, retrieval date, and SHA256 checksums.

| Column | Type | Description |
|---|---|---|
| `source_id` | Text | Short identifier for the official source in this package. |
| `title` | Text | Official or documented title of the source table, workbook, or file. |
| `url` | Text | Official source URL. |
| `licence` | Text | Licence name for the source, such as the Statistics Canada Open Licence or the Open Government Licence to Canada. |
| `release_date` | Date | Official release date or official product update statement, as recorded for this snapshot. |
| `retrieval_date` | Date | Date the source file was downloaded, as YYYY MM DD. |
| `file_name` | Text | Name of the downloaded source file. |
| `checksum_sha256` | Text | SHA256 checksum of the downloaded source file. |
| `notes` | Text | Short note about how the source was used in this package. |

### `data_dictionary.csv`

Column dictionary for every data file in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Column name in the data file. |
| `file` | Text | Data file that contains the column. |
| `type` | Text | Documented value type, such as string, integer, numeric, or boolean. |
| `description` | Text | Plain language description of the column. |

### `ghg_inventory_detail.csv`

Official National Inventory Report detail rows, with the same official hierarchy flags and documentation columns.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Inventory year. |
| `region_published` | Text | Region name exactly as published. One Agriculture series is labelled canada in lowercase and is left as published. |
| `category_id` | Text | Official category identifier. Inventory totals use 0. |
| `source` | Text | Top level IPCC source as published. |
| `category` | Text | IPCC category as published. Empty on source totals and the inventory total. |
| `sub_category` | Text | IPCC sub category as published. |
| `sub_sub_category` | Text | IPCC sub sub category as published. |
| `total_flag` | Text | Official Total column. y marks a published total at that level of the inventory tree. |
| `co2_kt` | Float | Carbon dioxide, kilotonnes. Empty when the source used a non numeric flag such as x. |
| `ch4_kt` | Float | Methane, kilotonnes. |
| `ch4_co2eq_kt` | Float | Methane as carbon dioxide equivalent, kilotonnes. |
| `n2o_kt` | Float | Nitrous oxide, kilotonnes. |
| `n2o_co2eq_kt` | Float | Nitrous oxide as carbon dioxide equivalent, kilotonnes. |
| `hfcs_co2eq_kt` | Float | Hydrofluorocarbons as carbon dioxide equivalent, kilotonnes. |
| `pfcs_co2eq_kt` | Float | Perfluorocarbons as carbon dioxide equivalent, kilotonnes. |
| `sf6_co2eq_kt` | Float | Sulphur hexafluoride as carbon dioxide equivalent, kilotonnes. |
| `nf3_co2eq_kt` | Float | Nitrogen trifluoride as carbon dioxide equivalent, kilotonnes. |
| `co2eq_kt` | Float | Official total carbon dioxide equivalent, kilotonnes. This is the raw official series and is kept beside the index. |
| `unit` | Text | Unit as published. Figures in this file are in kilotonnes. |
| `region` | Text | Region used for joins. The lowercase canada label is mapped to Canada. Other names match the published label. |
| `gwp_set` | Text | Global warming potential set used for carbon dioxide equivalent figures: IPCC Fifth Assessment Report, 100-year values, as required for UNFCCC inventory reporting. |
| `sector_level` | Integer | 0 official inventory total, 1 source total, 2 category, 3 sub category, 4 sub sub category, taken from the official tree. |
| `is_subtotal` | Boolean | True when the official Total flag is y, or when the row is the official inventory total. Leaf rows are False. |
| `lulucf_treatment` | Text | The official inventory total excludes land use, land use change and forestry. LULUCF rows are kept separately and are labelled as not in that total. |
| `pre_1999_nwt_nunavut` | Boolean | True for the official combined Northwest Territories and Nunavut series used before Nunavut was created in 1999. |
| `co2eq_kt_1990` | Float | Official carbon dioxide equivalent in 1990 for the same region and category identifier. |
| `canada_co2eq_kt` | Float | Official Canada carbon dioxide equivalent in the same year and category identifier, using the published Canada label. |
| `index_1990` | Float | co2eq_kt divided by the 1990 official value for the same region and category identifier, multiplied by 100. The base year is 1990, which equals 100. This is an adapted index. |
| `share_of_canada` | Float | This official value divided by the Canada value for the same year and category identifier. Adapted share, not an official inventory share table. |
| `index_base_year` | Integer | Base year for index_1990. Always 1990. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two digit codes are provinces or territories. Empty when a code is not available for this geography. |

### `ghg_inventory_totals.csv`

Official National Inventory Report totals, with sector level, subtotal flags, LULUCF treatment, the GWP set, a before 1999 NWT and Nunavut flag, and adapted province per capita figures that use a matched official population.

| Column | Type | Description |
|---|---|---|
| `year` | Integer | Inventory year. |
| `region_published` | Text | Region name exactly as published. One Agriculture series is labelled canada in lowercase and is left as published. |
| `category_id` | Text | Official category identifier. Inventory totals use 0. |
| `source` | Text | Top level IPCC source as published. |
| `category` | Text | IPCC category as published. Empty on source totals and the inventory total. |
| `sub_category` | Text | IPCC sub category as published. |
| `sub_sub_category` | Text | IPCC sub sub category as published. |
| `total_flag` | Boolean | Official Total column. y marks a published total at that level of the inventory tree. |
| `co2_kt` | Float | Carbon dioxide, kilotonnes. Empty when the source used a non numeric flag such as x. |
| `ch4_kt` | Float | Methane, kilotonnes. |
| `ch4_co2eq_kt` | Float | Methane as carbon dioxide equivalent, kilotonnes. |
| `n2o_kt` | Float | Nitrous oxide, kilotonnes. |
| `n2o_co2eq_kt` | Float | Nitrous oxide as carbon dioxide equivalent, kilotonnes. |
| `hfcs_co2eq_kt` | Float | Hydrofluorocarbons as carbon dioxide equivalent, kilotonnes. |
| `pfcs_co2eq_kt` | Float | Perfluorocarbons as carbon dioxide equivalent, kilotonnes. |
| `sf6_co2eq_kt` | Float | Sulphur hexafluoride as carbon dioxide equivalent, kilotonnes. |
| `nf3_co2eq_kt` | Float | Nitrogen trifluoride as carbon dioxide equivalent, kilotonnes. |
| `co2eq_kt` | Float | Official total carbon dioxide equivalent, kilotonnes. This is the raw official series and is kept beside the index. |
| `unit` | Text | Unit as published. Figures in this file are in kilotonnes. |
| `region` | Text | Region used for joins. The lowercase canada label is mapped to Canada. Other names match the published label. |
| `gwp_set` | Text | Global warming potential set used for carbon dioxide equivalent figures: IPCC Fifth Assessment Report, 100-year values, as required for UNFCCC inventory reporting. |
| `sector_level` | Integer | 0 official inventory total, 1 source total, 2 category, 3 sub category, 4 sub sub category, taken from the official tree. |
| `is_subtotal` | Boolean | True when the official Total flag is y, or when the row is the official inventory total. Leaf rows are False. |
| `lulucf_treatment` | Text | The official inventory total excludes land use, land use change and forestry. LULUCF rows are kept separately and are labelled as not in that total. |
| `pre_1999_nwt_nunavut` | Boolean | True for the official combined Northwest Territories and Nunavut series used before Nunavut was created in 1999. |
| `co2eq_kt_1990` | Float | Official carbon dioxide equivalent in 1990 for the same region and category identifier. |
| `canada_co2eq_kt` | Float | Official Canada carbon dioxide equivalent in the same year and category identifier, using the published Canada label. |
| `index_1990` | Float | co2eq_kt divided by the 1990 official value for the same region and category identifier, multiplied by 100. The base year is 1990, which equals 100. This is an adapted index. |
| `share_of_canada` | Float | This official value divided by the Canada value for the same year and category identifier. Adapted share, not an official inventory share table. |
| `index_base_year` | Integer | Base year for index_1990. Always 1990. |
| `iso3166_2` | Text | ISO 3166-2:CA code for a province or territory, such as CA-ON. Empty for Canada and for geography groups that are not a single province or territory. |
| `sgc` | Integer | Standard Geographic Classification code. 11124 is Canada. Two digit codes are provinces or territories. Empty when a code is not available for this geography. |
| `population` | Float | July 1 population from table 17-10-0009, joined on the same year and a matched geography name. The combined territories series is joined to Northwest Territories including Nunavut. Filled on the totals file. |
| `t_co2eq_per_person` | Float | Official kilotonnes times 1,000, divided by matched July 1 population, in tonnes per person. Adapted, and only on inventory total rows with a matched official population figure. |

## Source and licence

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.
- **Licence:** [Open Government Licence – Canada 2.0](https://open.canada.ca/en/open-government-licence-canada). Contains information licensed under the Open Government Licence – Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadaghginventorynir,
  author    = {Khan, John},
  title     = {Canada greenhouse gas inventory},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-ghg-inventory-nir}
}
```

APA: Khan, J. (2026). *Canada greenhouse gas inventory* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ghg-inventory-nir

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Canada's official greenhouse gas inventory, tidied from the IPCC sector file on the [Open Government portal](https://open.canada.ca/data/en/dataset/779c7bcf-4982-47eb-af1b-a33618a05e5b). The detail file keeps the official sector tree and adds sector_level, is_subtotal, a LULUCF treatment label, the GWP set, and a flag for the pre-1999 combined territories series. A totals file keeps the official inventory total, which excludes land use, land use change and forestry, and adds a 1990 index (base year 1990) and tonnes per person using matched July 1 population.

## Coverage

1990 to 2024, annual, Canada, the provinces and the territories as published.

## Updates

This upload is a snapshot downloaded on 15 November 2026. The Open Government record gave a date published of 2026-04-14.

## A few numbers from this snapshot

* The detail file has 42,538 rows, matching the official IPCC sector file, for 1990 to 2024.
* Canada's official inventory total, which excludes land use, land use change and forestry, was 684,704.5 kilotonnes of carbon dioxide equivalent in 2024, as published. The 1990 official total was 607,907.1 kilotonnes (index 112.6, where 1990 equals 100).
* Using July 1 population from table 17-10-0009 in the same year, that official total is 16.6 tonnes per person in 2024, compared with 22.0 tonnes per person in 1990. The per person figure is adapted, not an official inventory rate.
* Carbon dioxide equivalent figures use IPCC Fifth Assessment Report, 100-year values, the set required for UNFCCC inventory reporting as stated on the Government of Canada global warming potentials page.

## Example uses

* Track official inventory totals against a stated 1990 base year, while keeping the raw official series.
* Separate official totals from subtotals and leaf categories.
* Compare provincial inventory totals per person only where a same-year official population figure matches.

## Caveats

The official inventory total excludes land use, land use change and forestry. One Agriculture series is labelled canada in lowercase and is left as published. Suppressed cells marked x are empty in the numeric columns. The 1990 index and tonnes per person figures are adapted. The combined territories series covers the years before Nunavut was created in 1999.

## Files

* `ghg_inventory_totals.csv`: Official inventory totals by region and year, excluding land use, land use change and forestry, with a 1990 index (base year stated), Canada share, and tonnes per person using matched July 1 population.
* `ghg_inventory_detail.csv`: Full official IPCC sector file, with sector_level, is_subtotal, LULUCF treatment, GWP set, and a flag for the pre-1999 combined Northwest Territories and Nunavut series.
* `SOURCE_MANIFEST.csv`: Source identifiers, release dates, retrieval date and checksums.
* `data_dictionary.csv`: Column dictionary for every CSV.
* `METHODS.md`: Methods note.
* `CITATION.txt`: Suggested citation, with DOI pending.

## Licence

This dataset contains information licensed under the Open Government Licence Canada (https://open.canada.ca/en/open-government-licence-canada). Source: Environment and Climate Change Canada, National Inventory Report IPCC sector file. This file is adapted from the official source. Published values were not changed. Derived columns are calculated here and are not official estimates of the source agency. This is not an official Government of Canada product and the source agencies do not endorse it. Population estimates in the totals file are used under the Statistics Canada Open Licence: https://www.statcan.gc.ca/en/reference/licence.

Suggested citation: John Khan. 2026. Canada greenhouse gas inventory [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-ghg-inventory-nir. DOI pending.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
