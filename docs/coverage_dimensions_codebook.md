# Codebook for the coverage dimensions added October 2026

File: `data/state_coverage_evidence_sources.csv`, one row per state (50 states; DC not included). The original columns (coverage status, Wegovy, Saxenda and Zepbound start and end dates, PA and QL flags, evidence type, citation) are unchanged from the NBER w34949 version except for the dated corrections listed in `CHANGES.md`. The columns below were added on 2026-10-25 from the state documents in the evidence folder and from the state documents found online that day (recorded in the authors' audit notes of October 2026).

Design choice: slow-moving dimensions (prior authorization stringency, BMI thresholds, step therapy, age limits, quantity limits) are columns on the state row and hold the most recent documented value, with `criteria_as_of` giving the date of the document they come from. Dated changes within a state (a drop, a restart, a tightening) are rows in `data/state_coverage_events.csv`, one row per event with its own source, and are not duplicated as columns. Anything that fits neither goes in `docs/state_notes.md`.

## Columns

| Column | Values | Rule |
|---|---|---|
| `pa_stringency` | `none`, `fda_label`, `more_restrictive`, `not_documented`, `not_applicable` | Compares the documented PA criteria for the preferred weight-loss GLP-1 with the FDA label (adults: BMI 30 or higher, or 27 or higher with one weight-related comorbidity; adolescents 12 and older: BMI at or above the 95th percentile). `none`: no PA. `fda_label`: PA criteria restate the label and add only documentation (weight, diet counselling, no combination GLP-1 use). `more_restrictive`: any of a higher BMI threshold, a required comorbidity at BMI 30 or above, two or more comorbidities at BMI 27 to 30, a required trial of another drug or of a lifestyle program before the GLP-1, a minimum age above the label, or coverage of the GLP-1 only for a non-obesity indication. `not_documented`: the state flags PA but no criteria document is in hand. `not_applicable`: never-covering states. The value is for the most recent period; `pa_stringency_note` gives the reason and any earlier value (Massachusetts was `fda_label` in 2024). |
| `pa_stringency_note` | free text | Added 2026-11-16. The reason for the class, and the earlier class where it changed. |
| `bmi_adult_criteria` | free text | Verbatim or close paraphrase of the adult BMI and comorbidity rule, with the pre-change rule where a change is documented. |
| `bmi_adolescent_criteria` | free text | Rule for ages 12 to 17, or "Not documented". |
| `step_therapy` | free text | Any drug or program the member must try first, and which GLP-1 is preferred when the PDL makes one of them non-preferred. |
| `age_minimum` | free text | Minimum age in the criteria, or "Not documented". |
| `quantity_limit_detail` | free text | Pens per 28 or 30 days, authorization periods, renewal rules. |
| `indication_scope` | free text | Which FDA-approved indications the state covers these molecules for, and which it keeps when weight-management coverage ends. Weight management, cardiovascular risk reduction, MASH, obstructive sleep apnea, type 2 diabetes. This is what makes a withdrawal incomplete: California kept Wegovy for MASH and cardiovascular risk and Zepbound for sleep apnea by case-by-case prior authorization after ending weight-management coverage on 1/1/2026. It is also the field that puts Alabama, Hawaii, Louisiana and Washington (Wegovy for cardiovascular risk only) and West Virginia (Zepbound for sleep apnea only) in the never-covering group. |
| `preferred_status` | free text | Which weight-management GLP-1 is preferred on the PDL, which are non-preferred, and the date of the listing. Preferred status moves share between covered drugs without changing whether the state covers, so it is not a coverage event. |
| `renewal_criteria` | free text | What the member must show to keep the drug past the first authorization: weight loss achieved, adherence, continued counselling, and the authorization length. Promoted out of `quantity_limit_detail` on 2026-11-11 because continuation rules decide who is cut off and belong with the eligibility fields, not with dose limits. Delaware's five percent loss by six months is the type case. |
| `first_authorization_length` | not a column in this release | Planned 2026-11-15 and described in `docs/notes_on_the_rules.md`; the column is not in the file. Length of the first authorization, coded only from a document that states it, with source and date. `Not documented` where a covering state's documents are silent. Six states state a first-authorization length; two give one authorization length without separating first from renewal, and the entry says so. |
| `status_on_2026_11_16` | `covered`, `covered_restricted`, `ended`, `unknown`, `not_covered` | Added 2026-11-17. State status on the freeze date, derived from the last spell of each product in `data/state_drug_coverage.csv`: `covered` if any product is covered for weight loss, otherwise `covered_restricted`, `unknown` or `ended` in that order. |
| `weight_loss_coverage_end_date` | m/d/yyyy or NA | Added 2026-11-17. For states with status `ended`, the latest product end date. |
| `oral_semaglutide_start_date`, `oral_semaglutide_end_date` | NA | Not filled. The Wegovy tablet is recorded by product and spell in `data/state_drug_coverage.csv`. |
| `orforglipron_start_date`, `orforglipron_end_date` | m/d/yyyy or NA | Orforglipron (Foundayo), same convention. Eligible to count from 4/1/2026, the FDA approval date; see the molecule rule below. |
| `ffs_mco_scope` | free text | Whether the documented rule applies to fee-for-service only, to managed care plans, or both; names the MCO when an MCO policy is the source. |
| `criteria_as_of` | m/d/yyyy | Date of the document the criteria columns come from. |
| `criteria_source` | free text | Document title, date and page; URL when the document is online. |
| `klebanoff_stringency_june2024` | text | The June 2024 fee-for-service classification used by Khanna, Wang and Venkataramani (JAMA Health Forum 2026;7(9):e263353), from Klebanoff et al. (JGIM 2026): "none (no PA)" (CA), "PA at FDA label" (PA, MN), "more restrictive than FDA label" (MA, MI, MS, NH, VA), "undetermined" (RI); other states "not classified" or "control state". Recorded so the two codings can be compared; where our `pa_stringency` differs (Minnesota: our December 2021 criteria require a diet trial and a Saxenda step, so we code more restrictive; Mississippi: the 7/1/2023 criteria restate the label, so we code fda_label) the difference is a finding, not an error, and is noted in `docs/state_notes.md`. |
| `khanna_start_quarter` | text | Start quarter from Khanna et al. eTable 1, with their exclusion reason where they excluded the state. |
| `w34949_adoption_quarter` | text | Adoption quarter implied by the file used in the NBER w34949 estimation (`GLP1_Coverage_with_PA_QL_Date.csv`, earliest of the three drug start dates); where this audit changed the date, both values are shown. |

## What is documented and what is not

As of November 16, 2026, `criteria_source` names the document behind each state's rules, and `data/criteria_status_by_quarter.csv` says, for 13 of the 17 covering states, which quarters each rule is documented for. South Carolina published no criteria document. Rhode Island's criteria come from a managed care plan's policy, not the fee-for-service program. Documents that were read and are not in the collection are listed in `data/document_manifest.csv` (cited, not deposited) or in `docs/documents_still_to_find.md`.

## Molecules, and the date a molecule starts counting

The weight-management set is time-dependent, because a drug cannot be covered before it is approved. Through 3/31/2026 it is Wegovy, Saxenda and its generic liraglutide, and Zepbound. From 4/1/2026, the FDA approval date for orforglipron (Foundayo), that drug joins the set. Oral semaglutide joins from its own approval date.

The approval date is when a molecule becomes eligible to count, not when any state covers it. Each state's own start date still comes from that state's documents. Mississippi, for example, is reported to have made Foundayo preferred on 7/1/2026 (see `data/clues.csv`, C004).

This rule changes no classification in the 2026 Q1 analyses, whose window closes before orforglipron existed.

The older non-GLP-1 anti-obesity drugs (phentermine, Contrave, Qsymia, orlistat) are not tracked except where they appear in a step-therapy rule.

## What counts as state coverage when managed care pays

A state counts as covering when a state-level document establishes the benefit: the preferred drug list, a state plan amendment, a bulletin, or a rule binding all contracted plans. One managed care plan deciding on its own does not make the state a covering state.

A managed care plan's own policy may still supply the criteria detail, and often does, because plans publish fuller criteria documents than states do. Where a criteria value comes from a plan policy rather than a state document, `ffs_mco_scope` names the plan and `criteria_source` cites it, so the reader can see the level the value sits at.

Checked against the two states where this could have bitten, and it does not. Delaware's coverage rests on SPA DE-24-0010, which sets the state coverage floor, with Delaware First Health policy DE.PMN.50 supplying the BMI and diet-trial detail. Rhode Island's fee-for-service PDL applies a manual clinical prior authorization to the whole class, with the Neighborhood Health Plan policy supplying the criteria. Both are covering states under the rule above.

Three delivery arrangements are worth distinguishing when reading a state's documents, and `ffs_mco_scope` should say which applies:

- The state pays all pharmacy claims (California through Medi-Cal Rx).
- Plans pay, but one state preferred drug list binds them all (Indiana since the statewide uniform PDL of 7/5/2023).
- Plans pay and set their own formularies. Only here can one plan's policy differ from the state's position, so only here does the distinction change a reading.

## The clues file

`data/clues.csv` holds claims that are not yet facts. A clue is anything asserted by a source we have not verified: a coauthor's table, another group's supplement, a tracker, a news report, or our own search hit. Nothing in the clues file is coded into `state_coverage_evidence_sources.csv` or `state_coverage_events.csv` until a document closes it.

Each clue carries a `status` of `open`, `confirmed`, `contradicted`, `partly_confirmed`, or `not_found`, with `resolution` saying what settled it and `resolved_date` when. A contradicted clue stays in the file rather than being deleted, so the disagreement is on the record.

Columns: `clue_id`, `state`, `claim`, `asserted_date`, `source`, `source_type`, `date_logged`, `status`, `resolution`, `resolved_date`, `notes`.


## Event type added 2026-11-11

`plan_amendment`: a state plan amendment changed the coverage language, and the documents in hand do not show whether coverage narrowed or widened. Used for Delaware, January 1, 2026 (SPA DE-26-0003). The list of covered agents was found on 2026-11-15 (the Obesity Treatment Agents class of the Delaware PDL, edition effective 11/2/2026), and it shows the class intact, with Wegovy, Zepbound and Foundayo preferred and Saxenda non-preferred. The 1/1/2026 edition is not available, so whether the amendment narrowed the list relative to 2025 is still unknown and the code stays `plan_amendment`.

## Event type added 2026-11-15

`criteria_revision`: a dated, documented change to a state's prior authorization criteria whose net direction is mixed, so neither `restrict` nor a widening code fits. Used for Mississippi, July 1, 2026 (criteria V7 to V11), where the covered molecules widened while the adherence and reauthorization requirements changed shape. A `criteria_revision` event does not change any coverage start or end date; it records that the criteria in force differ before and after the date, which matters for any index built on criteria rather than on coverage alone.

## Projected savings file

`data/projected_savings.csv` records each dollar figure a state or a news report gives for weight-loss GLP-1 spending or savings, with the period, whether the funds are state, federal or total, and what the figure measures.

## Criteria history files added 2026-11-15

The evidence file holds one set of rules per state, from the most recent document coded. These four files say what each rule rested on in each earlier quarter, for the 13 states checked document by document on 2026-11-15. Minnesota, North Carolina, Tennessee and Utah had no quarter marked in the earlier count and were not re-read.

`data/state_criteria_history.csv`: one row per state and period. Columns: `state`, `period_start`, `period_end` (blank where the period is open), the six rule fields (`pa_required`, `bmi_rule`, `lifestyle_or_step`, `renewal_rule`, `quantity_limit`, `preferred_product`), `source_document`, `source_date`, `evidence_tier`, `notes`. A new period starts only where a document shows the rule changed; where a change is bounded but not dated, the notes say so.

`data/criteria_status_by_quarter.csv`: one row per covered state-quarter and rule field. Columns: `state`, `quarter`, `field`, `class`, `rule`, `source_document`, `source_date`, `evidence_tier`, `notes`. The six classes are:

- `observed`: a document dated on or before the last day of the quarter states the rule.
- `stated_retrospectively`: a later document states the rule and gives the date it began or was last revised. Michigan's DUR Board minutes of 9/5/2023, which date prior authorization to 2/1/2022, are the type case. Shown to readers as "dated by a later document".
- `bracketed`: the same rule appears in a document before the quarter and a document after it.
- `carried_back`: only a later document states the rule. This is the number the November 2026 pass set out to reduce.
- `absent_by_inference`: the documents covering the quarter were read and state no such rule, so we assume there was none. An assumption, not a finding, and the notes name the documents read.
- `no_information`: nothing in hand covers the quarter.

`data/criteria_status_spans.csv`: the hand-coded input, one row per state, field and run of quarters, with a short quotation from the document in `notes`. Same columns as the quarter file with `quarter_start` and `quarter_end` in place of `quarter`.

`data/covered_quarters.csv`: `state`, `first_quarter`, `last_quarter`, `basis`. Covered quarters run from the first full quarter after the coverage start date through 2026Q2, or through the last quarter before an end date.

`evidence_tier` in these files follows the repository convention: tier 1 where the document is in the collection, tier 2 where it was read but not saved as a file, and the notes say which.

`code/build_criteria_status.py` expands the spans into the quarter file, fails if any covered state-quarter and field is unclassed or classed twice, and prints the shares by class, by state and by field. `docs/criteria_history_log.md` records what was compared in each state, every archive search with its result, and the corrections these comparisons imply for `data/state_coverage_evidence_sources.csv`, which this pass did not change. `docs/documents_still_to_find.md` lists the documents that would resolve the remaining `carried_back` and `no_information` cells, ordered by how many cells each would settle.
