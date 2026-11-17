# What this dataset tracks, and at what level

Data frozen on November 16, 2026. The next update is planned for one quarter later.

This page says what is recorded, for which products, at what level of detail, and what is left out. Column-by-column coding rules are in `docs/coverage_dimensions_codebook.md`.

## The five products

| Name in the files | Product | Notes |
|---|---|---|
| `saxenda` | Saxenda (liraglutide injection) | Generic liraglutide for weight management is counted with it |
| `wegovy_injection` | Wegovy pen (semaglutide injection) | Includes the higher-dose pen where a state lists it |
| `wegovy_tablet` | Wegovy tablet (oral semaglutide for weight management) | A separate product from the pen |
| `zepbound` | Zepbound (tirzepatide injection) | |
| `foundayo` | Foundayo (orforglipron tablet) | A different drug from the Wegovy tablet |

"Coverage" in these files means Medicaid coverage for weight loss in adults. A state that pays for Wegovy only to reduce cardiovascular risk, or Zepbound only for sleep apnea, is not counted as covering.

## Three levels of detail

### 1. By state and product: `data/state_drug_coverage.csv`

One row per state, product and spell of coverage, for the 17 states that ever covered. A second spell is a second row (Massachusetts covered Wegovy for adults from 1/2/2024 to 1/1/2025 and again from 2/17/2026 to 7/3/2026).

| Column | Meaning |
|---|---|
| `start_date`, `end_date` | First day covered and first day not covered (YYYY-MM-DD). A blank end date means no end is documented as of the freeze date |
| `start_basis` | How the start date is known (see below) |
| `end_basis` | How the end date is known |
| `status_on_2026_11_16` | `covered`; `covered_restricted` (covered under criteria much narrower than the label); `ended`; `not_covered_for_weight_loss` (listed only for another use); `not_named` (no document in hand names the product); `unknown` |
| `preferred_status` | Preferred or non-preferred placement, with the document date |
| `quantity_limit` | The limit for this product, where a document states one |
| `uses_covered` | Weight management, and any other uses the documents name |
| `source` | The documents the row rests on |
| `last_document_date` | Date of the most recent document in hand for the state. Coverage after this date is assumed to continue unless an end is documented |
| `notes` | Anything a reader needs to interpret the row |

Values of `start_basis`:

- `stated_in_document`: a state document gives the date.
- `first_listing`: the date of the earliest document in hand that lists the product. Coverage may have begun earlier, so this is the latest possible start.
- `bounded`: the product is absent from one dated document and present in a later one; the start is between the two, and the later date is recorded.
- `evidence_file`: the date recorded in the evidence file since the version used in NBER Working Paper 34949; the basis was not re-derived in November 2026.
- `not_supported`: no document in hand supports the recorded date (Missouri, Zepbound).
- `prescriptions_observed`: no dated document gives a start, and the state was paying for the product before its earliest dated document. The date is the first day of the first quarter with prescriptions in the CMS State Drug Utilization Data, or the first day of the data window (2021-01-01) when prescriptions are present from the first quarter. Used for Saxenda and the Wegovy injection in six states (Kansas, Wisconsin, Delaware, Virginia, New Hampshire, Rhode Island), decided 2026-11-17 on two grounds. First, prescriptions per 100,000 enrollees exceed every never-covering state in each quarter from the recorded date, and the never-covering states have the same pediatric EPSDT route, so that route cannot explain the margin. Second, Wegovy had no adolescent approval until December 23, 2022, so its 2021 and 2022 prescriptions were adult use on the label. Where a document predates the superseded start it agrees: Wisconsin's PA form of 07/2021 names Saxenda, Delaware's state plan has covered obesity drugs with co-morbid conditions and prior authorization since 2019, Kansas's criteria run back to 2007, and plan policies list the drugs in Virginia (criteria of 12/6/2022 adapted from the state PDL) and Rhode Island (the largest plan, from 7/2018). Rhode Island has the closest margin (Saxenda 11.4 per 100,000 in 2021 Q1 against a never-covering maximum of 5.9). Each row's notes give the counts; the superseded dates remain in the files as document dates, and the two Kansas bulletins (9/19/2023 and 4/1/2024) are in the events file.

`data/state_quarter_drug_panel.csv` is built from this file by `code/build_state_quarter_drug_panel.py`: one row per state, quarter (2021Q1 to 2026Q4) and product, with `covered_any`, `covered_full` and a `basis` column that separates documented quarters from quarters after the last document in hand.

The Wegovy tablet and Foundayo are recorded only where a document in hand names them: Delaware, Kansas, Mississippi, Missouri and Wisconsin. For the other 12 states the status is `not_named`. That means no document we have names the product; it does not mean the state excludes it. Several of those states' latest documents predate both products. A later search of current drug lists could fill these rows.

### 2. By state and period: the rules that apply to the whole class

Most rules are written once for all weight-loss products in a state, so they are recorded by state and period and not by product:

- whether prior authorization is required;
- the BMI rule;
- the lifestyle or step requirement (a diet trial, a supervised programme, or another drug first);
- the renewal rule.

`data/state_criteria_history.csv` has one row per state and period. `data/criteria_status_by_quarter.csv` has one row per state, quarter and rule, and says what each cell rests on (observed in a document of that date, dated by a later document, bracketed, carried back from a later document, absent by inference, or no information). In November 2026 these two files cover 13 of the 17 covering states; Minnesota, North Carolina, Tennessee and Utah are not yet in them. Those files also record quantity limit and preferred product by quarter at the class level; the product-level version of those two is in `data/state_drug_coverage.csv`.

Where a class rule has a product exception, the exception is in the text of the rule. Examples: Kansas waives its BMI-40 tier for Zepbound from 4/1/2024 and for Wegovy from 6/1/2025; Delaware and New Hampshire set a 4 percent renewal test for Saxenda where other products have 5 percent.

The state row in `data/state_coverage_evidence_sources.csv` has the most recent documented value of each rule, the managed care scope, and the date and citation of the source. `pa_stringency` has one of five values (`none`, `fda_label`, `more_restrictive`, `not_documented`, `not_applicable`) for the most recent period, and `pa_stringency_note` gives the reason and any earlier value.

### 3. Described, not tracked

A few features are stated by so few states that they are described in `docs/notes_on_the_rules.md` and not coded: the BMI below which treatment stops, rules for people with both Medicare and Medicaid, labeler restrictions, waist-circumference alternatives to BMI, and calorie targets in diet trials.

## Where the two date records differ

`data/state_drug_coverage.csv` is the record to use for product dates. The start and end columns in `data/state_coverage_evidence_sources.csv` are kept as they were for comparison with NBER Working Paper 34949 and differ in these cases:

- Massachusetts: the evidence file cannot show the second Wegovy spell (2/17/2026 to 7/3/2026).
- Missouri: the evidence file records Wegovy as NA; the drug list effective February 1, 2025 lists it as non-preferred.
- Mississippi: the evidence file records Zepbound as NA; the product file dates it 7/1/2026 (bounded between PDL editions).
- North Carolina: the evidence file does not show the break from 10/1/2025 to 12/12/2025.
- All states: the evidence file writes "Continued coverage through Q1 2026" where the product file has a blank end date.

For a table of states, the evidence file has two columns for the state as a whole: `status_on_2026_11_16` (`covered`, `covered_restricted`, `ended`, `unknown` or `not_covered`) and `weight_loss_coverage_end_date`. Seven states have status `ended`: California, New Hampshire, Pennsylvania and South Carolina (1/1/2026), Utah (7/1/2026), Massachusetts (7/3/2026), and Rhode Island (10/1/2026). For Utah the state form ends pilot authorizations by 6/30/2026, and the non-renewal of the pilot is from secondary sources. The same two columns are in the `by_state` sheet of `outputs/state_coverage_summary.xlsx`.

## Prescription counts (SDUD)

`outputs/state_quarter_product_counts.csv` has prescriptions by state, quarter and product from the CMS State Drug Utilization Data, 2021 Q1 to 2026 Q1, for Saxenda, Wegovy and Zepbound. Each state has two charts in the deposit: raw prescription counts by quarter (`<ST>.png`) and prescriptions per 100,000 Medicaid enrollees by quarter (`<ST>100K.png`).

The counts are by brand. They cannot separate weight loss from the other labeled uses of Wegovy and Zepbound, so a state with no weight-loss coverage can still show prescriptions.

## Documents that are cited and not deposited

The source documents are deposited at Indiana University DataCORE. A document is cited and not deposited when it is marked proprietary or confidential, or carries a vendor's or managed care plan's own copyright notice. We have read these documents; the data cite them with the web address and the date retrieved, and a reader who wants the file can obtain it from that address. `data/document_manifest.csv` lists them with `deposit` equal to `no` and the reason.

## What a later update could add

- The Wegovy tablet and Foundayo in the 12 states where no document in hand names them.
- The four states missing from the quarter-by-quarter history.
- Documents listed in `docs/documents_still_to_find.md`, some of which the Internet Archive index shows as captured (`docs/wayback_capture_inventory_2026-11-16.md`).
- Documents for the never-covering states that show prescriptions for Wegovy or Zepbound from 2025.
- The documents behind open clues C014 to C016: a Virginia plan criteria file of 12/6/2022 adapted from the state PDL, the Rhode Island Neighborhood Health Plan weight-loss policy in force since 7/2018, and whatever dated New Hampshire to 2021 Q3 in Khanna et al.
- A state notice confirming that Utah's pilot was not renewed after 6/30/2026; the end date now rests partly on secondary sources.
- Web addresses for the six source documents that have none recorded (`source_url_kind` equal to `not_recorded` in the manifest).
- The Kansas criteria versions revised April 21, 2021, July 21, 2021, October 19, 2022 and January 17, 2024.
