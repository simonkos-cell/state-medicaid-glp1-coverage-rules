# Codebook for the coverage dimensions added October 2026

File: `data/state_coverage_evidence_sources.csv`, one row per state (50 states; DC not included). The original columns (coverage status, Wegovy, Saxenda and Zepbound start and end dates, PA and QL flags, evidence type, citation) are unchanged from the NBER w34949 version except for the dated corrections listed in `CHANGES.md`. The columns below were added on 2026-10-25 from the state documents in the evidence folder and from the state documents found online that day (quoted in `docs/audit_2026-10.md`).

Design choice: slow-moving dimensions (prior authorization stringency, BMI thresholds, step therapy, age limits, quantity limits) are columns on the state row and hold the most recent documented value, with `criteria_as_of` giving the date of the document they come from. Dated changes within a state (a drop, a restart, a tightening) are rows in `data/state_coverage_events.csv`, one row per event with its own source, and are not duplicated as columns. Anything that fits neither goes in `docs/state_notes.md`.

## Columns

| Column | Values | Rule |
|---|---|---|
| `pa_stringency` | `none`, `fda_label`, `more_restrictive`, `not_documented`, `not_applicable` | Compares the documented PA criteria for the preferred weight-loss GLP-1 with the FDA label (adults: BMI 30 or higher, or 27 or higher with one weight-related comorbidity; adolescents 12 and older: BMI at or above the 95th percentile). `none`: no PA. `fda_label`: PA criteria restate the label and add only documentation (weight, diet counselling, no combination GLP-1 use). `more_restrictive`: any of a higher BMI threshold, a required comorbidity at BMI 30 or above, two or more comorbidities at BMI 27 to 30, a required trial of another drug or of a lifestyle program before the GLP-1, a minimum age above the label, or coverage of the GLP-1 only for a non-obesity indication. `not_documented`: the state flags PA but no criteria document is in hand. `not_applicable`: never-covering states. Where the value changed over time the cell says so (Massachusetts). |
| `bmi_adult_criteria` | free text | Verbatim or close paraphrase of the adult BMI and comorbidity rule, with the pre-change rule where a change is documented. |
| `bmi_adolescent_criteria` | free text | Rule for ages 12 to 17, or "Not documented". |
| `step_therapy` | free text | Any drug or program the member must try first, and which GLP-1 is preferred when the PDL makes one of them non-preferred. |
| `age_minimum` | free text | Minimum age in the criteria, or "Not documented". |
| `quantity_limit_detail` | free text | Pens per 28 or 30 days, authorization periods, renewal rules. |
| `ffs_mco_scope` | free text | Whether the documented rule applies to fee-for-service only, to managed care plans, or both; names the MCO when an MCO policy is the source. |
| `criteria_as_of` | m/d/yyyy | Date of the document the criteria columns come from. |
| `criteria_source` | free text | Document title, date and page; URL when the document is online. |
| `klebanoff_stringency_june2024` | text | The June 2024 fee-for-service classification used by Khanna, Wang and Venkataramani (JAMA Health Forum 2026;7(9):e263353), from Klebanoff et al. (JGIM 2026): "none (no PA)" (CA), "PA at FDA label" (PA, MN), "more restrictive than FDA label" (MA, MI, MS, NH, VA), "undetermined" (RI); other states "not classified" or "control state". Recorded so the two codings can be compared; where our `pa_stringency` differs (Minnesota: our December 2021 criteria require a diet trial and a Saxenda step, so we code more restrictive; Mississippi: the 7/1/2023 criteria restate the label, so we code fda_label) the difference is a finding, not an error, and is noted in `docs/state_notes.md`. |
| `khanna_start_quarter` | text | Start quarter from Khanna et al. eTable 1, with their exclusion reason where they excluded the state. |
| `w34949_adoption_quarter` | text | Adoption quarter implied by the file used in the NBER w34949 estimation (`GLP1_Coverage_with_PA_QL_Date.csv`, earliest of the three drug start dates); where this audit changed the date, both values are shown. |

## What is documented and what is not

Criteria are documented from a state document for CA, KS (via the KDHE form and an MCO bulletin restating KDHE criteria), MA, MN, MS, MO, VA (via the JCHC report quoting the DMAS memo) and WI. For DE the SPA gives the comorbidity requirement but no BMI number. For MI, NH, NC, PA, RI, SC, TN and UT the PDL flags PA but the criteria document is not in the folder; the `criteria_source` column names the document to obtain. Rhode Island's criteria come from an MCO policy, not the FFS program.

## Molecules

The file tracks Wegovy, Saxenda and Zepbound. Oral GLP-1 agents for weight management (oral semaglutide; orforglipron, which Kansas already lists on its 2026 PA form) are not yet columns; they should be added as `oral_semaglutide_start_date` and `orforglipron_start_date` pairs when the first state lists one, following the same start and end convention. The older non-GLP-1 anti-obesity drugs (phentermine, Contrave, Qsymia, orlistat) are not tracked except where they appear in a step-therapy rule.
