# Data dictionary

Every column of every data file, as frozen on November 16, 2026. Coding rules and the reasons behind them are in `docs/coverage_dimensions_codebook.md`; what is tracked at which level is in `docs/what_is_tracked.md`.

Missing values: `NA` means not applicable; an empty cell means no value recorded; `Not documented` means the rule may exist but no document in hand states it.

## data/state_coverage_evidence_sources.csv (one row per state, 50 rows)

| Column | Meaning |
|---|---|
| `state` | Full state name |
| `coverage_status` | `Covered` if the state covered a GLP-1 for weight loss at any time since 2021 (17 states), otherwise `Not Covered` |
| `status_on_2026_11_16` | Status on the freeze date, derived from `state_drug_coverage.csv`: `covered` (at least one product covered for weight loss); `covered_restricted` (covered under criteria much narrower than the label: Michigan, Virginia); `ended` (seven states; for Utah the state form ends pilot authorizations by 6/30/2026 and the non-renewal is from secondary sources); `unknown` (no state on the freeze date); `not_covered` (the 33 states that never covered). Added 2026-11-17 |
| `weight_loss_coverage_end_date` | For the seven states with status `ended`, the first day no product was covered for weight loss (M/D/YYYY): California, New Hampshire, Pennsylvania and South Carolina 1/1/2026; Utah 7/1/2026; Massachusetts 7/3/2026; Rhode Island 10/1/2026. Otherwise `NA`. Added 2026-11-17 |
| `wegovy_start_date`, `wegovy_end_date` | First and last dates of Wegovy injection coverage as recorded for NBER Working Paper 34949 and corrected since. Text such as "Continued coverage through Q1 2026" means no end was recorded. Ends after 2026 Q1 were filled on 2026-11-17 (Massachusetts Zepbound, Rhode Island, Utah, Wisconsin Wegovy and Saxenda). For dates by product and spell use `state_drug_coverage.csv` |
| `saxenda_start_date`, `saxenda_end_date` | Same, for Saxenda |
| `zepbound_start_date`, `zepbound_end_date` | Same, for Zepbound |
| `oral_semaglutide_start_date`, `oral_semaglutide_end_date` | Not filled; the Wegovy tablet is recorded in `state_drug_coverage.csv` |
| `orforglipron_start_date`, `orforglipron_end_date` | Not filled; Foundayo is recorded in `state_drug_coverage.csv` |
| `prior_authorization` | `Yes` or `No`: whether prior authorization is required |
| `quantity_limits` | `Yes` or `No`: whether a document states a quantity limit for any of the products |
| `primary_evidence_type` | Kinds of evidence behind the coverage dates (PDL, PA criteria, state plan, SDUD and so on) |
| `evidence_citation` | Text of the evidence for the coverage dates, with references separated by a vertical bar |
| `pa_stringency` | `none`, `fda_label`, `more_restrictive`, `not_documented` or `not_applicable`, for the most recent period |
| `pa_stringency_note` | The reason for the class and any earlier value |
| `bmi_adult_criteria` | Adult BMI and comorbidity rule, in words |
| `bmi_adolescent_criteria` | Rule for ages 12 to 17 |
| `step_therapy` | Any lifestyle programme, diet trial or drug that must come first |
| `age_minimum` | Minimum age in the criteria |
| `quantity_limit_detail` | Amounts per period, and authorization lengths where the source gives them together |
| `indication_scope` | Uses covered (weight management, cardiovascular risk, MASH, sleep apnea), and what continues after weight-loss coverage ends |
| `preferred_status` | Preferred and non-preferred placement, with document dates |
| `renewal_criteria` | What must be shown to continue past the first authorization |
| `ffs_mco_scope` | Whether the rule binds fee-for-service, managed care plans, or both, and which plan supplied a rule |
| `criteria_as_of` | Date of the document the rule columns come from (M/D/YYYY) |
| `criteria_source` | Citation of that document, with URL where known |
| `klebanoff_stringency_june2024` | Class assigned by Klebanoff et al. as used in Khanna, Wang and Venkataramani (2026), for comparison |
| `khanna_start_quarter` | Start quarter in Khanna et al., for comparison |
| `w34949_adoption_quarter` | Adoption quarter used in NBER Working Paper 34949, for comparison |

## data/state_drug_coverage.csv (one row per state, product and spell; 17 states, 5 products)

| Column | Meaning |
|---|---|
| `state` | Two-letter code |
| `product` | `saxenda`, `wegovy_injection`, `wegovy_tablet`, `zepbound` or `foundayo` |
| `spell` | 1 for the first period of coverage, 2 for a second |
| `start_date` | First day covered for weight loss (YYYY-MM-DD); empty if never documented as covered |
| `start_basis` | `stated_in_document`, `first_listing`, `bounded`, `evidence_file`, `not_supported` or `prescriptions_observed` (six states; rule in `what_is_tracked.md`); defined in `docs/what_is_tracked.md` |
| `end_date` | First day not covered (YYYY-MM-DD); empty if no end is documented |
| `end_basis` | How the end date is known |
| `status_on_2026_11_16` | `covered`, `covered_restricted`, `ended`, `not_covered_for_weight_loss`, `not_named` or `unknown` |
| `preferred_status` | Placement of this product, with document dates |
| `quantity_limit` | Limit for this product, where stated |
| `uses_covered` | Uses the documents name for this product |
| `source` | Documents the row rests on |
| `last_document_date` | Date of the most recent document in hand for the state |
| `notes` | Anything needed to interpret the row |

## data/state_quarter_drug_panel.csv (one row per state, quarter and product; built by code/build_state_quarter_drug_panel.py)

| Column | Meaning |
|---|---|
| `state` | Two-letter code (17 covering states) |
| `quarter` | 2021Q1 to 2026Q4 |
| `product` | As above |
| `covered_any` | 1 if a spell of weight-loss coverage overlaps the quarter |
| `covered_full` | 1 if a spell covers every day of the quarter |
| `basis` | `documented`; `after_last_document` (coverage assumed to continue past the state's last document); `not_named`; `unknown` |

## data/state_coverage_events.csv (one row per dated change)

| Column | Meaning |
|---|---|
| `state` | Two-letter code |
| `event_type` | `end`, `restrict`, `reinstate`, `scheduled_end`, `plan_amendment`, `criteria_revision` or `expand` (coverage widened; Kansas, 9/19/2023) |
| `drugs` | Products affected |
| `population` | Members affected |
| `effective_date` | YYYY-MM-DD; the description says where the date is a bound |
| `description` | What changed, with quotations from the source |
| `source_citation` | The document |
| `evidence_tier` | 1 state document in hand; 2 strong secondary source or a state document read but not saved; 3 claim not yet backed by a document |
| `source_url` | Web address of the source |
| `evidence_file` | Path of the document in the deposit, where it is deposited |
| `date_checked` | Date the row was last checked |
| `checked_by` | Initials of the person who checked it |
| `notes` | Open points |

## data/state_criteria_history.csv (one row per state and period; 13 states)

| Column | Meaning |
|---|---|
| `state` | Two-letter code |
| `period_start`, `period_end` | Dates the rules applied; an empty end means the latest document |
| `pa_required`, `bmi_rule`, `lifestyle_or_step`, `renewal_rule`, `quantity_limit`, `preferred_product` | The six rules for the period, in words |
| `source_document`, `source_date` | Documents and their dates |
| `evidence_tier` | As in the events file |
| `notes` | How the period was dated |

## data/criteria_status_by_quarter.csv (one row per state, quarter and rule; built by code/build_criteria_status.py)

| Column | Meaning |
|---|---|
| `state`, `quarter` | Two-letter code; quarter as 2023Q1 |
| `field` | One of the six rules |
| `class` | `observed`, `stated_retrospectively`, `bracketed`, `carried_back`, `absent_by_inference` or `no_information`; defined in the codebook |
| `rule` | The rule, in words |
| `source_document`, `source_date` | The document the cell rests on |
| `evidence_tier` | 1 document in the collection; 2 read but not saved |
| `notes` | Quotation or reasoning |

## data/criteria_status_spans.csv (hand-coded input to the quarter file)

Same columns as the quarter file, with `quarter_start` and `quarter_end` in place of `quarter`.

## data/covered_quarters.csv

| Column | Meaning |
|---|---|
| `state` | Two-letter code (13 states) |
| `first_quarter`, `last_quarter` | First and last covered quarter used in the quarter file |
| `basis` | How the range was set |

## data/document_manifest.csv (one row per file in the deposit, and per document cited and not deposited)

| Column | Meaning |
|---|---|
| `state` | Two-letter code; empty for files that are not state-specific |
| `file_path` | Path under `files/` in the deposit |
| `file_type` | PDF, chart, state summary, data file and so on |
| `bytes` | File size |
| `document_date_in_text` | Date printed on the document |
| `deposit` | `yes` if the file is in the deposit; `no` if it is cited and not deposited |
| `source_url` | Web address |
| `source_url_kind` | `file` (the address returned this file); `listing_page` (the page that lists it); `archive_capture`; `related_page`; `inferred` (formed from the document number or file name, not opened); `generated` (built by this project); `not_recorded` |
| `file_saved_date` | Date the file was saved in the collection |
| `notes` | Reason a document is not deposited, and other remarks |

## data/clues.csv (claims not yet confirmed by a document)

| Column | Meaning |
|---|---|
| `clue_id`, `state` | Identifier and state |
| `claim`, `asserted_date` | What is claimed and the date claimed |
| `source`, `source_type` | Where the claim came from |
| `date_logged` | Date entered |
| `status` | `open`, `confirmed`, `contradicted`, `partly_confirmed` or `not_found` |
| `resolution`, `resolved_date` | What settled it, and when |
| `notes` | Remarks |

## data/projected_savings.csv

| Column | Meaning |
|---|---|
| `state`, `amount`, `period` | State, dollar figure and the period it refers to |
| `funds` | State, federal or total |
| `what_it_measures` | Spending or savings, as the source describes it |
| `source`, `source_url`, `date_checked`, `notes` | Citation and remarks |

## outputs/state_quarter_product_counts.csv (prescriptions from CMS State Drug Utilization Data)

| Column | Meaning |
|---|---|
| `state` | Two-letter code (50 states and DC) |
| `year`, `quarter`, `year_quarter` | Calendar year and quarter |
| `product_name` | WEGOVY, SAXENDA or ZEPBOUND, by brand; all uses of the brand are included |
| `number_rx` | Prescriptions paid by Medicaid |
| `enrollment` | Median monthly Medicaid enrollment in the quarter |
| `number_rx_100K` | Prescriptions per 100,000 enrollees |
