<p align="center"><img src="../../assets/theme-housing.png" alt="Canada rental vacancy rates" width="100%"></p>

# Canada rental vacancy rates

*CMHC vacancy rates for row and apartment stock in Canadian CMAs*

**Theme:** [Housing and homelessness](../../README.md#housing-and-homelessness) · **Coverage:** 1989 to 2025 · **Kaggle:** [https://www.kaggle.com/datasets/johnnykhan1/canada-rental-vacancy-rates](https://www.kaggle.com/datasets/johnnykhan1/canada-rental-vacancy-rates)

## What it is

Annual rental vacancy rates for privately initiated row and apartment structures of three units and over in Canadian census metropolitan areas, tidied from Statistics Canada Table 34-10-0132 (CMHC).

Source table: [34-10-0132](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013201).

## Who it helps

Home buyers, renters, mortgage brokers and agents, housing researchers, shelter planners and city staff in Toronto, across Ontario and the rest of Canada.

## Files

| File | Size | Where |
|---|---:|---|
| [`data_dictionary.csv`](data/data_dictionary.csv) | 18 KB | in this repository |
| [`rental_vacancy_long.csv`](data/rental_vacancy_long.csv) | 490 KB | in this repository |
| [`rental_vacancy_selected_cmas.csv`](data/rental_vacancy_selected_cmas.csv) | 21 KB | in this repository |
| [`statcan_table_metadata.csv`](data/statcan_table_metadata.csv) | 11 KB | in this repository |

## Columns

### `data_dictionary.csv`

Column dictionary for every CSV in this dataset.

| Column | Type | Description |
|---|---|---|
| `column` | Text | Name of the column being described |
| `file` | Text | File that contains the column |
| `type` | Text | Data type of the column |
| `description` | Text | Plain-language description of the column |

### `rental_vacancy_long.csv`

Long tidy file of rental vacancy rates by geography and year.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | tistics Canada symbol when present.nReference period as published by Statistics Canada. |
| `geo` | Text | iGeography name as published by Statistics Canada. |
| `dguid` | Text | tStatistics Canada Dissemination Geography Unique Identifier. |
| `unit_of_measure` | Text | aU |
| `unit_of_measure_id` | Text | Statistics Canada numeric code for the unit of measure. |
| `scalar_factor` | Text | oScale of value (for example units, thousands or millions).f measure for value. |
| `scalar_id` | Text | Statistics Canada numeric code for the scalar factor.St |
| `vector` | Text | nStatistics Canada vector identifier for the series.a |
| `coordinate` | Integer | dSitatistics Canada coordinate string inside the table.t |
| `value` | Float | lPublished value. Empty when Statistics Canada did not publish a figure. |
| `status` | Text | iStatistics Canada status symbol when a value is missing or qualified.o |
| `symbol` | Text | Ad |
| `terminated` | Boolean | utm biefr of decimal places Statistics Canada uses when displaying the value. Statistics Canada terminated this series, otherwise empty. |
| `decimals` | Integer | N |

### `rental_vacancy_selected_cmas.csv`

Wide file for selected large CMAs.

| Column | Type | Description |
|---|---|---|
| `ref_date` | Date | Reference period as published by Statistics Canada. |
| `alma_quebec` | Float | Vacancy rate (%) for alma quebec. |
| `amos_quebec` | Float | Vacancy rate (%) for amos quebec. |
| `baie_comeau_quebec` | Float | Vacancy rate (%) for baie comeau quebec. |
| `bathurst_new_brunswick` | Float | Vacancy rate (%) for bathurst new brunswick. |
| `bay_roberts_newfoundland_and_labrador` | Float | Vacancy rate (%) for bay roberts newfoundland and labrador. |
| `bracebridge_ontario` | Float | Vacancy rate (%) for bracebridge ontario. |
| `brandon_manitoba` | Float | Vacancy rate (%) for brandon manitoba. |
| `brant_ontario` | Float | Vacancy rate (%) for brant ontario. |
| `brighton_ontario` | Float | Vacancy rate (%) for brighton ontario. |
| `brock_ontario` | Float | Vacancy rate (%) for brock ontario. |
| `brockville_ontario` | Float | Vacancy rate (%) for brockville ontario. |
| `brooks_alberta` | Float | Vacancy rate (%) for brooks alberta. |
| `campbell_river_british_columbia` | Float | Vacancy rate (%) for campbell river british columbia. |
| `campbellton_new_brunswick_quebec` | Float | Vacancy rate (%) for campbellton new brunswick quebec. |
| `camrose_alberta` | Float | Vacancy rate (%) for camrose alberta. |
| `canmore_alberta` | Float | Vacancy rate (%) for canmore alberta. |
| `census_agglomerations_10_000_to_49_999` | Float | Vacancy rate (%) for census agglomerations 10 000 to 49 999. |
| `centre_wellington_ontario` | Float | Vacancy rate (%) for centre wellington ontario. |
| `chatham_ontario` | Float | Vacancy rate (%) for chatham ontario. |
| `cobourg_ontario` | Float | Vacancy rate (%) for cobourg ontario. |
| `cold_lake_alberta` | Float | Vacancy rate (%) for cold lake alberta. |
| `collingwood_ontario` | Float | Vacancy rate (%) for collingwood ontario. |
| `corner_brook_newfoundland_and_labrador` | Float | Vacancy rate (%) for corner brook newfoundland and labrador. |
| `courtenay_british_columbia` | Float | Vacancy rate (%) for courtenay british columbia. |
| `cowansville_quebec` | Float | Vacancy rate (%) for cowansville quebec. |
| `cranbrook_british_columbia` | Float | Vacancy rate (%) for cranbrook british columbia. |
| `dawson_creek_british_columbia` | Float | Vacancy rate (%) for dawson creek british columbia. |
| `dolbeau_mistassini_quebec` | Float | Vacancy rate (%) for dolbeau mistassini quebec. |
| `duncan_british_columbia` | Float | Vacancy rate (%) for duncan british columbia. |
| `dunnville_ontario` | Float | Vacancy rate (%) for dunnville ontario. |
| `east_hants_nova_scotia` | Float | Vacancy rate (%) for east hants nova scotia. |
| `edmundston_new_brunswick` | Float | Vacancy rate (%) for edmundston new brunswick. |
| `elliot_lake_ontario` | Float | Vacancy rate (%) for elliot lake ontario. |
| `essex_ontario` | Float | Vacancy rate (%) for essex ontario. |
| `estevan_saskatchewan` | Float | Vacancy rate (%) for estevan saskatchewan. |
| `fort_mcmurray_alberta` | Float | Vacancy rate (%) for fort mcmurray alberta. |
| `fort_st_john_british_columbia` | Float | Vacancy rate (%) for fort st john british columbia. |
| `gander_newfoundland_and_labrador` | Float | Vacancy rate (%) for gander newfoundland and labrador. |
| `gasp_quebec` | Float | Vacancy rate (%) for gasp quebec. |
| `grand_falls_windsor_newfoundland_and_labrador` | Float | Vacancy rate (%) for grand falls windsor newfoundland and labrador. |
| `grande_prairie_alberta` | Float | Vacancy rate (%) for grande prairie alberta. |
| `gravenhurst_ontario` | Float | Vacancy rate (%) for gravenhurst ontario. |
| `greater_napanee_ontario` | Float | Vacancy rate (%) for greater napanee ontario. |
| `haldimand_county` | Float | Vacancy rate (%) for haldimand county. |
| `haldimand_ontario` | Float | Vacancy rate (%) for haldimand ontario. |
| `hanover_manitoba` | Float | Vacancy rate (%) for hanover manitoba. |
| `hawkesbury_ontario_part_ontario_quebec` | Float | Vacancy rate (%) for hawkesbury ontario part ontario quebec. |
| `high_river_alberta` | Float | Vacancy rate (%) for high river alberta. |
| `huntsville_ontario` | Float | Vacancy rate (%) for huntsville ontario. |
| `ingersoll_ontario` | Float | Vacancy rate (%) for ingersoll ontario. |
| `joliette_quebec` | Float | Vacancy rate (%) for joliette quebec. |
| `kapuskasing_ontario` | Float | Vacancy rate (%) for kapuskasing ontario. |
| `kawartha_lakes_ontario` | Float | Vacancy rate (%) for kawartha lakes ontario. |
| `kenora_ontario` | Float | Vacancy rate (%) for kenora ontario. |
| `kentville_nova_scotia` | Float | Vacancy rate (%) for kentville nova scotia. |
| `kincardine_ontario` | Float | Vacancy rate (%) for kincardine ontario. |
| `kings_subdivision_ontario` | Float | Vacancy rate (%) for kings subdivision ontario. |
| `kirkland_lake_ontario` | Float | Vacancy rate (%) for kirkland lake ontario. |
| `kitimat_british_columbia` | Float | Vacancy rate (%) for kitimat british columbia. |
| `la_tuque_quebec` | Float | Vacancy rate (%) for la tuque quebec. |
| `labrador_city_newfoundland_and_labrador` | Float | Vacancy rate (%) for labrador city newfoundland and labrador. |
| `lachute_quebec` | Float | Vacancy rate (%) for lachute quebec. |
| `lacombe_alberta` | Float | Vacancy rate (%) for lacombe alberta. |
| `lambton_shores_ontario` | Float | Vacancy rate (%) for lambton shores ontario. |
| `leamington_ontario` | Float | Vacancy rate (%) for leamington ontario. |
| `les_les_de_la_madeleine_quebec` | Float | Vacancy rate (%) for les les de la madeleine quebec. |
| `lloydminster_saskatchewan_alberta` | Float | Vacancy rate (%) for lloydminster saskatchewan alberta. |
| `mackenzie_no_23_alberta` | Float | Vacancy rate (%) for mackenzie no 23 alberta. |
| `magog_quebec` | Float | Vacancy rate (%) for magog quebec. |
| `matane_quebec` | Float | Vacancy rate (%) for matane quebec. |
| `meaford_ontario` | Float | Vacancy rate (%) for meaford ontario. |
| `midland_ontario` | Float | Vacancy rate (%) for midland ontario. |
| `miramichi_new_brunswick` | Float | Vacancy rate (%) for miramichi new brunswick. |
| `mississippi_mills_ontario` | Float | Vacancy rate (%) for mississippi mills ontario. |
| `mont_laurier_quebec` | Float | Vacancy rate (%) for mont laurier quebec. |
| `montmagny_quebec` | Float | Vacancy rate (%) for montmagny quebec. |
| `moose_jaw_saskatchewan` | Float | Vacancy rate (%) for moose jaw saskatchewan. |
| `nanticoke_ontario` | Float | Vacancy rate (%) for nanticoke ontario. |
| `new_glasgow_nova_scotia` | Float | Vacancy rate (%) for new glasgow nova scotia. |
| `norfolk_ontario` | Float | Vacancy rate (%) for norfolk ontario. |
| `north_battleford_saskatchewan` | Float | Vacancy rate (%) for north battleford saskatchewan. |
| `north_grenville_ontario` | Float | Vacancy rate (%) for north grenville ontario. |
| `north_perth_ontario` | Float | Vacancy rate (%) for north perth ontario. |
| `okotoks_alberta` | Float | Vacancy rate (%) for okotoks alberta. |
| `orillia_ontario` | Float | Vacancy rate (%) for orillia ontario. |
| `owen_sound_ontario` | Float | Vacancy rate (%) for owen sound ontario. |
| `parksville_british_columbia` | Float | Vacancy rate (%) for parksville british columbia. |
| `pembroke_ontario` | Float | Vacancy rate (%) for pembroke ontario. |
| `penticton_british_columbia` | Float | Vacancy rate (%) for penticton british columbia. |
| `petawawa_ontario` | Float | Vacancy rate (%) for petawawa ontario. |
| `port_alberni_british_columbia` | Float | Vacancy rate (%) for port alberni british columbia. |
| `port_hope_ontario` | Float | Vacancy rate (%) for port hope ontario. |
| `portage_la_prairie_manitoba` | Float | Vacancy rate (%) for portage la prairie manitoba. |
| `powell_river_british_columbia` | Float | Vacancy rate (%) for powell river british columbia. |
| `prince_albert_saskatchewan` | Float | Vacancy rate (%) for prince albert saskatchewan. |
| `prince_edward_ontario` | Float | Vacancy rate (%) for prince edward ontario. |
| `prince_rupert_british_columbia` | Float | Vacancy rate (%) for prince rupert british columbia. |
| `pr_vost_quebec` | Float | Vacancy rate (%) for pr vost quebec. |
| `queens_nova_scotia` | Float | Vacancy rate (%) for queens nova scotia. |
| `quesnel_british_columbia` | Float | Vacancy rate (%) for quesnel british columbia. |
| `rawdon_quebec` | Float | Vacancy rate (%) for rawdon quebec. |
| `red_deer_county_alberta` | Float | Vacancy rate (%) for red deer county alberta. |
| `rimouski_quebec` | Float | Vacancy rate (%) for rimouski quebec. |
| `rivi_re_du_loup_quebec` | Float | Vacancy rate (%) for rivi re du loup quebec. |
| `roberval_quebec` | Float | Vacancy rate (%) for roberval quebec. |
| `rouyn_noranda_quebec` | Float | Vacancy rate (%) for rouyn noranda quebec. |
| `saint_f_licien_quebec` | Float | Vacancy rate (%) for saint f licien quebec. |
| `saint_georges_quebec` | Float | Vacancy rate (%) for saint georges quebec. |
| `saint_hyacinthe_quebec` | Float | Vacancy rate (%) for saint hyacinthe quebec. |
| `saint_lin_laurentides_quebec` | Float | Vacancy rate (%) for saint lin laurentides quebec. |
| `sainte_sophie_quebec` | Float | Vacancy rate (%) for sainte sophie quebec. |
| `sainte_ad_le_quebec` | Float | Vacancy rate (%) for sainte ad le quebec. |
| `sainte_marie_quebec` | Float | Vacancy rate (%) for sainte marie quebec. |
| `salaberry_de_valleyfield_quebec` | Float | Vacancy rate (%) for salaberry de valleyfield quebec. |
| `salmon_arm_british_columbia` | Float | Vacancy rate (%) for salmon arm british columbia. |
| `saugeen_shores_ontario` | Float | Vacancy rate (%) for saugeen shores ontario. |
| `scugog_ontario` | Float | Vacancy rate (%) for scugog ontario. |
| `sept_les_quebec` | Float | Vacancy rate (%) for sept les quebec. |
| `smith_falls_ontario` | Float | Vacancy rate (%) for smith falls ontario. |
| `sorel_tracy_quebec` | Float | Vacancy rate (%) for sorel tracy quebec. |
| `south_huron_ontario` | Float | Vacancy rate (%) for south huron ontario. |
| `squamish_british_columbia` | Float | Vacancy rate (%) for squamish british columbia. |
| `steinbach_manitoba` | Float | Vacancy rate (%) for steinbach manitoba. |
| `stratford_ontario` | Float | Vacancy rate (%) for stratford ontario. |
| `strathmore_alberta` | Float | Vacancy rate (%) for strathmore alberta. |
| `strathroy_ontario` | Float | Vacancy rate (%) for strathroy ontario. |
| `strathroy_ontario_terminated_with_1997_10` | Float | Vacancy rate (%) for strathroy ontario terminated with 1997 10. |
| `summerland_british_columbia` | Float | Vacancy rate (%) for summerland british columbia. |
| `summerside_prince_edward_island` | Float | Vacancy rate (%) for summerside prince edward island. |
| `swift_current_saskatchewan` | Float | Vacancy rate (%) for swift current saskatchewan. |
| `sylvan_lake_alberta` | Float | Vacancy rate (%) for sylvan lake alberta. |
| `temiskaming_shores_ontario` | Float | Vacancy rate (%) for temiskaming shores ontario. |
| `terrace_british_columbia` | Float | Vacancy rate (%) for terrace british columbia. |
| `the_nation_ontario` | Float | Vacancy rate (%) for the nation ontario. |
| `thetford_mines_quebec` | Float | Vacancy rate (%) for thetford mines quebec. |
| `thompson_manitoba` | Float | Vacancy rate (%) for thompson manitoba. |
| `tillsonburg_ontario` | Float | Vacancy rate (%) for tillsonburg ontario. |
| `timmins_ontario` | Float | Vacancy rate (%) for timmins ontario. |
| `truro_nova_scotia` | Float | Vacancy rate (%) for truro nova scotia. |
| `val_d_or_quebec` | Float | Vacancy rate (%) for val d or quebec. |
| `vernon_british_columbia` | Float | Vacancy rate (%) for vernon british columbia. |
| `victoriaville_quebec` | Float | Vacancy rate (%) for victoriaville quebec. |
| `wallaceburg_ontario` | Float | Vacancy rate (%) for wallaceburg ontario. |
| `west_grey_ontario` | Float | Vacancy rate (%) for west grey ontario. |
| `west_hants_nova_scotia` | Float | Vacancy rate (%) for west hants nova scotia. |
| `west_nipissing_ontario` | Float | Vacancy rate (%) for west nipissing ontario. |
| `wetaskiwin_alberta` | Float | Vacancy rate (%) for wetaskiwin alberta. |
| `williams_lake_british_columbia` | Float | Vacancy rate (%) for williams lake british columbia. |
| `wood_buffalo_alberta` | Float | Vacancy rate (%) for wood buffalo alberta. |
| `woodstock_ontario` | Float | Vacancy rate (%) for woodstock ontario. |
| `yarmouth_nova_scotia` | Float | Vacancy rate (%) for yarmouth nova scotia. |
| `yellowknife_northwest_territories` | Float | Vacancy rate (%) for yellowknife northwest territories. |
| `yorkton_saskatchewan` | Float | Vacancy rate (%) for yorkton saskatchewan. |

### `statcan_table_metadata.csv`

Official Statistics Canada cube metadata.

| Column | Type | Description |
|---|---|---|
| `Cube Title` | Text | Official title of the Statistics Canada data table. |
| `Product Id` | Text | Statistics Canada product ID for the table. |
| `CANSIM Id` | Text | Legacy CANSIM identifier for the table, when available. |
| `URL` | Text | URL of the Statistics Canada table. |
| `Cube Notes` | Text | Official notes associated with the Statistics Canada table. |
| `Archive Status` | Text | Status indicating whether the table is current or archived. |
| `Frequency` | Text | Publication frequency of the table. |
| `Start Reference Period` | Text | First reference period available in the table. |
| `End Reference Period` | Date | Last reference period available in the table. |
| `Total number of dimensions` | Integer | Number of dimensions in the table. |

## Source and licence

**Source:** Statistics Canada Table 34-10-0132, Vacancy rates, row and apartment structures of three units and over, privately initiated in census metropolitan areas (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013201). Downloaded on November 9, 2026. Prepared by John Khan in Toronto, Ontario. Statistics Canada Open Licence: https://www.statcan.gc.ca/en/terms-conditions/open-licence. Downloaded from the official open data release and reshaped into tidy CSV files by John Khan, November 2026.

- **Licence:** [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada. This is an adaptation of Statistics Canada data; it does not constitute an endorsement by Statistics Canada.

The published values were not changed beyond what is described here. The full licence terms for this folder are in [LICENSE.md](LICENSE.md).

## Citation

No DOI has been minted for this dataset yet; please cite the Kaggle page.

```bibtex
@misc{khan2026canadarentalvacancyrates,
  author    = {Khan, John},
  title     = {Canada rental vacancy rates},
  year      = {2026},
  publisher = {Kaggle},
  address   = {Toronto, Ontario, Canada},
  url       = {https://www.kaggle.com/datasets/johnnykhan1/canada-rental-vacancy-rates}
}
```

APA: Khan, J. (2026). *Canada rental vacancy rates* [Data set]. Kaggle. https://www.kaggle.com/datasets/johnnykhan1/canada-rental-vacancy-rates

<details><summary>Full notes from the Kaggle page</summary>

## What this is

Annual rental vacancy rates for privately initiated row and apartment structures of three units and over in Canadian census metropolitan areas, tidied from Statistics Canada Table 34-10-0132 (CMHC).

Source table: [34-10-0132](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013201).

## Coverage

Annual series from 1989-01-01 to 2025-01-01 for CMAs and related geographies as published.

## Updates

Snapshot from November 9, 2026. CMHC publishes vacancy rates annually. This upload is not auto refreshed.

## A few numbers from this snapshot

* The vacancy table covers 1989-01-01 to 2025-01-01 across 167 geographies.
* In 2025-01-01, 99 geographies have a published vacancy rate.

## Example uses

* Compare rental tightness across Canadian cities.
* Join vacancy to asking rents, starts or population growth.
* Feature for housing affordability models.

## Caveats

* Rates cover privately initiated row and apartment stock of three or more units. They do not cover every rental dwelling.
* Survey methods and geography boundaries can change over long histories.
* A low vacancy rate means a tight market, not a measure of homelessness or waiting lists.

## Files

* `rental_vacancy_long.csv`: tidy long file.
* `rental_vacancy_selected_cmas.csv`: wide file for selected large CMAs.
* `data_dictionary.csv`, `statcan_table_metadata.csv`, `cover.png`.

## Licence

Shared under the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Source: Statistics Canada Table 34-10-0132 (CMHC). Not an official Statistics Canada or CMHC product.

Author: John Khan, Toronto, Ontario.

</details>

---
Compiled by John Khan, Toronto, Ontario. Part of the [Canadian Open Datasets](../../README.md) catalogue.
