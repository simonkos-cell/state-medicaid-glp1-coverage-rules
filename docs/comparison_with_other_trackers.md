# How this database compares with other trackers of Medicaid GLP-1 coverage

Prepared October 25, 2026; the description of this database was updated November 15 and November 17, 2026. Each statement about another source quotes or paraphrases that source as checked on October 25, 2026; items not checked are marked. A Cureus article published November 6, 2026 has not been compared.

## In plain words
For every state, this database records whether Medicaid pays for weight-loss drugs such as Wegovy, when that started, when it stopped, and what a patient has to show to get one. Each fact points to the state's own document, and each state's record is checked against how many prescriptions Medicaid paid for. Other trackers give one or two of these pieces: a count of covering states at a point in time, or the quarter coverage began. None of the sources checked here gives the dated changes through 2026, the criteria behind the yes or no, and the documents together.

## What this database records
- All 50 states. Coverage dates and dated changes run from 2021 through November 16, 2026; prescription counts run from 2021 Q1 through 2026 Q1 (the dispensing profiles also include DC).
- Coverage of each weight-management GLP-1 (Wegovy, Saxenda, Zepbound, and oral semaglutide and orforglipron where a state lists them) separately, with start and end dates (`data/state_coverage_evidence_sources.csv`); by product and spell for Saxenda, the Wegovy injection, the Wegovy tablet, Zepbound and Foundayo (`data/state_drug_coverage.csv`); and as a state by quarter by product panel (`data/state_quarter_drug_panel.csv`).
- The criteria behind the yes or no, each with the date and citation of the document it comes from: prior authorization and a stringency class relative to the FDA label, adult and adolescent BMI thresholds, step therapy and lifestyle requirements, age minimums, quantity limits, renewal rules, preferred and non-preferred placement, indication scope, and fee-for-service versus managed care scope.
- A dated change log (`data/state_coverage_events.csv`, 33 events) covering ends, restrictions, reinstatements, scheduled ends, plan amendments, criteria revisions and one expansion, each with an evidence tier.
- Quarterly SDUD dispensing by state and product through 2026 Q1, as a check on the document record (`outputs/state_quarter_product_counts.csv`).
- The source documents themselves, deposited at IU DataCORE with a manifest (`data/document_manifest.csv`), and a record of the documents that could not be obtained (`docs/documents_to_obtain.md`).
- The values as used in NBER Working Paper 34949, frozen unchanged (`frozen_nber_w34949/`).

## Other sources
| Source | What it reports | How it differs |
|---|---|---|
| KFF, "Medicaid Coverage of and Spending on GLP-1s" (January 2026) | Count and map of states covering GLP-1s for obesity under fee-for-service ("13 State Medicaid Programs ... as of January 2026"), from "Annual KFF survey of state Medicaid officials conducted by Health Management Associates, November 2025" plus public data for nonresponding states and later changes | Point-in-time snapshots (2024, October 2025, January 2026), fee-for-service only, no per-drug effective dates on the page, no state-level download described on the page |
| Milliman, "Evolving landscape of obesity coverage in Medicaid" | Additions and narrowings since a KFF August 2024 baseline, with some dates (per our literature review) | Changes since 2024 only; not checked here for completeness |
| Klebanoff, Chetty, Doshi, J Gen Intern Med 2026;41(7):2003-2006 | Coverage and PA criteria; used by Khanna et al. as "coverage criteria as of June 2024 in fee-for-service Medicaid programs" | Cross-section at one date; details of fields not checked here |
| Khanna, Wang, Venkataramani, JAMA Health Forum 2026;7(9):e263353 | Quarter of coverage start, "obtaining and manually verifying archival records from state Preferred Drug Lists, official announcements and documents on state Medicaid websites, and relevant news articles (eTable 1 in Supplement 1)"; data sharing statement in Supplement 2 | Start quarter only, 2021 to 2024; excluded Delaware, Kansas, Wisconsin ("unclear start dates of coverage") and North Carolina ("restricted coverage only for patients with cardiovascular disease"); supplement not checked here |
| Liu and Rome, JAMA 2024;331(14):1230-1232 | Cross-sectional state coverage and reimbursement | Not checked here |
| Commercial trackers (for example therxindex.com) | Current status by state with a cited state document and verification date | Current status, not a dated history; useful for confirming recent status |

## Consistency check with KFF counts
- This database: 17 states ever covered by 2025 Q3 (MI, NH, RI, CA, DE, PA, VA, MN, WI, MS, MA, KS, NC, MO, SC, TN, UT).
- Minus the four January 1, 2026 withdrawals (CA, NH, PA, SC) gives 13, matching KFF's 13 as of January 2026. A secondary site quoting KFF's January 2026 list names the same 13 states.
- Minus North Carolina (off October 1 to December 12, 2025) gives 16, matching KFF's 16 as of October 2025.
- After January 2026, Utah (7/1/2026), Massachusetts (7/3/2026) and Rhode Island (10/1/2026) ended. That leaves 10 states on November 16, 2026: eight covered, and Michigan and Virginia covered under criteria much narrower than the label. Two commercial trackers read on November 17, 2026 agree: one counts 8 programs plus Michigan and Virginia under strict limits and seven states that ended, and the other names the same seven states. For Utah our end date rests on the state form plus secondary sources; no state notice of non-renewal is in hand.

## Where this database agrees with the other sources, and where it differs

The comparison uses what was recorded from each source on October 25, 2026 in the evidence file columns `khanna_start_quarter` and `klebanoff_stringency_june2024`. Our start quarter here is the quarter of the earliest product start date in the evidence file.

Differences of kind:

- Time. KFF gives counts at three dates and Klebanoff et al. one date (June 2024); Khanna et al. give a start quarter for 2021 to 2024. This database gives dated starts, ends and changes through November 16, 2026, including seven ends and one reinstatement that fall after the other sources' windows.
- Detail. The other sources give a yes or no, a start quarter, or a three-way stringency class. This database adds dates by product and spell, six rules by period (prior authorization, BMI, lifestyle or step, renewal, quantity limit, preferred product), what each quarter's rule rests on, the source documents, and prescription counts as a check.
- Scope. KFF and Klebanoff et al. describe fee-for-service programs. This database records for each state whether the coded rule binds managed care plans as well (`ffs_mco_scope`).

Agreement and difference on the same facts:

- Counts of covering states: agree with KFF at both dates checked (16 in October 2025, 13 in January 2026).
- Start quarter, against Khanna et al., for the 12 states where they give one: the same quarter in 6 (California, Massachusetts, Michigan, Mississippi, Pennsylvania, South Carolina); ours earlier in 5 (Minnesota by one quarter, from the state PA criteria of December 2021; New Hampshire, Delaware, Rhode Island and Virginia by two to eight quarters, re-dated from the prescription record on 2026-11-17); ours later in 1 (North Carolina: they date the earlier cardiovascular-only coverage, we date weight-loss coverage from 8/1/2024). A one-quarter gap can come from dating convention alone: a start late in a quarter is the next quarter under a first-full-quarter rule.
- Unclear starts: Khanna et al. excluded Kansas and Wisconsin for unclear start dates, and our record agrees that no document gives a clean start in those states. From 2026-11-17, six states (Kansas, Wisconsin, Delaware, Virginia, New Hampshire, Rhode Island) are dated from the prescription record (`start_basis` `prescriptions_observed`): prescriptions per 100,000 enrollees exceed every never-covering state in each quarter from the recorded start, and Wegovy prescriptions before its adolescent approval of December 23, 2022 cannot be pediatric EPSDT use. The rule, the counts and the corroborating documents are in `docs/what_is_tracked.md` and the state rows.
- Not in their sample: Missouri, Tennessee and Utah (starts in 2024 Q4 and 2025 Q3).
- Stringency, against Klebanoff et al. (June 2024), for the 8 states with a class from them: the same class in 6 (California, Massachusetts, Michigan, New Hampshire, Pennsylvania, Virginia) and a different class in 2 (Minnesota: theirs at the FDA label, ours more restrictive; Mississippi: theirs more restrictive, ours at the FDA label). Our class is for the most recent document coded and theirs for June 2024, so a difference can be a change in the state's rules over time and need not be a disagreement about the same date.
- NBER Working Paper 34949: the adoption quarters used in the paper are kept in `w34949_adoption_quarter`. They differ from the current start dates in Kansas, Minnesota, Mississippi and the five states re-dated from the prescription record on 2026-11-17 (Wisconsin, Delaware, Virginia, New Hampshire, Rhode Island).

## Policy features: tracked, and not yet tracked
Tracked as of November 15, 2026 (all were candidates on October 25): BMI thresholds and comorbidity conditions, lifestyle programme and step therapy requirements, age limits, reauthorization rules and approval duration, fee-for-service versus managed care scope, and coverage for other labeled indications where a state document states it.

Not yet tracked:
- Criteria history before the earliest document in hand; 47 of 202 covered state-quarters have at least one rule carried back from a later document (12 of them in Mississippi), each marked in `data/criteria_status_by_quarter.csv`.
- Age carve-outs (EPSDT coverage under 21).
- Grandfathering or transition rules for people already on treatment when coverage ends.
- Gating of diabetes-labeled GLP-1s (for example, a type 2 diabetes diagnosis code requirement), recorded for South Carolina only.
- Participation in the CMS BALANCE model.
- A single index of stringency built from the criteria fields.

## Limits relative to the other sources
- KFF surveys state Medicaid officials directly; this database reads published documents and has no such channel.
- The coding was done by one team without an independent second coder.
- One state's current criteria (Mississippi, version V11) were read from the state website but could not be saved as a file; the cells say so.
