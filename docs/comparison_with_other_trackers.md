# How this database compares with other trackers of Medicaid GLP-1 coverage

Prepared October 25, 2026. Each statement about another source quotes or paraphrases that source as checked on this date; items not checked are marked.

## What this database records
- All 50 states (DC excluded, as in NBER w34949), 2022 to present.
- Coverage of each weight-management GLP-1 (Wegovy, Saxenda, Zepbound) separately, with start and end dates by month (`frozen_nber_w34949/`, `data/`) and pause/resume dates (`legacy_2025_maddie_potter/GLP1_Coverage_with_PA_QL_Date.csv`).
- Prior authorization and quantity limits (yes/no, with start and end dates), and PA stringency tiers at adoption.
- A written evidence note and full citations for every state, with source PDFs saved by state in OneDrive.
- From late 2025 on, a dated change log (`data/state_coverage_events.csv`) with an evidence tier for each change.

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

## Policy features not yet tracked (candidates)
- PA criteria details over time: BMI thresholds, comorbidity list, lifestyle program, step therapy, age limits.
- Reauthorization rules (for example, required percent weight loss) and approval duration.
- Fee-for-service vs managed care differences, and whether the state uses a uniform PDL.
- Age carve-outs (EPSDT coverage under 21).
- Grandfathering or transition rules for people already on treatment when coverage ends.
- Gating of diabetes-labeled GLP-1s (for example, a type 2 diabetes diagnosis code requirement).
- Coverage for other labeled indications (cardiovascular disease, sleep apnea, MASH).
- Participation in the CMS BALANCE model.
