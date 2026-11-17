# Criteria history log

Working record of the document-by-document check of each state's prior authorization rules. One section per state, in the order worked. Classes are defined in `docs/notes_on_the_rules.md`; the sixth class (code `stated_retrospectively`, described to readers as "dated by a later document") means a later document states the rule and gives the date it began or was last revised.

Covered quarters run from the first full quarter after the coverage start date through 2026Q2, or through the last quarter before an end date.

Dating convention: a quarter is classed observed when a document stating the rule is dated on or before the last day of that quarter. The repository's earlier count marked a quarter when it began before the document's date, so the two can differ by one quarter per state.

Scope: the 13 states with marked quarters in the count of November 15, 2026. Minnesota, North Carolina, Tennessee and Utah (32 covered quarters, none marked) were not re-read here.

Documents described as "not in hand" were not in the folders sent for this check; what they say is taken from the repository's own files, and those cells are tier 2.

## Michigan (worked 2026-11-15)

Covered quarters: 2022Q2 to 2026Q2 (17).

### Documents compared

| Document | Date in the document | In the collection | What it states |
|---|---|---|---|
| `MIRx_DUR_board_minutes_20230905.pdf` | September 5, 2023 | yes | p. 3: "since MDHHS implemented coverage on February 1, 2022. All the medications were added to the single PDL as preferred with clinical prior authorization (PA) for appropriateness" |
| `MIRx_PAfaxform_anti-obesity_medications.pdf` | "Revision Date: 08/01/2024" | new; Internet Archive capture of August 18, 2024 | Adults: "initial body mass index (BMI) >= 30 kg/m2", or ">= 27 kg/m2 but < 30 kg/m2 and at least one of the following risk factors: hypertension, coronary artery disease, diabetes, dyslipidemia, sleep apnea". Ages 12 to 17: 95th percentile, or 85th to 94th with a condition. "part of a total treatment plan including a calorie and fat-restricted diet and exercise regimen". Renewal: "maintained a weight loss of >= 5% of weight at time of last prior authorization". No quantity limit on the form. Zepbound not named. |
| `Managed_Care_Common_Formulary_Listing.pdf` | 11/1/2024 | yes | Saxenda, Wegovy and Zepbound pens each "*PDL-P AGE PA"; legend "*PDL-P = PDL Preferred", "QL = Quantity Limitation". No QL code on these rows. |
| `MIRx_PDL.pdf` | "Effective 04/01/2025" (footer "Version 02012025v3") | new; Internet Archive capture of April 2025, the earliest capture of this URL | "Anti-Obesity Agents" marked "Clinical PA required"; Saxenda, Wegovy, Zepbound under Preferred Agents; no footnote 2 ("Quantity limits apply") on these rows. |
| `MI 2025 PDL.pdf` | "Effective 08/01/2025" | yes | Same class and placement; rows now read "Saxenda® (liraglutide)2", "Wegovy® (semaglutide) 2", "Zepbound® (tirzepatide) 2". |
| MDHHS Letter L 25-73; MIRx 1.1.2026 anti-obesity GLP-1 criteria | December 8, 2025; 1/1/2026 | no (read 2026-11-11, tier 2) | URLs are in `docs/documents_still_to_find.md`. |

### Findings

- PA required and preferred placement are the same in every document from September 2023 to August 2025. No revision before 1/1/2026.
- BMI, lifestyle and renewal rules before 2026 rest on one form, revised 08/01/2024. For 2022Q2 to 2024Q2 they are carried back from that form.
- Quantity limit: not marked on the GLP-1 rows on 11/1/2024 or 04/01/2025; marked on 08/01/2025. Classed absent by inference for 2024Q4 to 2025Q2 (an assumption: the separate file `MIRx_quantity_limits.pdf` is not in hand) and no information before 2024Q4. Candidate `criteria_revision` event: quantity limit marked between the 04/01/2025 and 08/01/2025 PDL editions.
- Rule change at 1/1/2026 (BMI 40, five-agent step, non-preferred) is already in `state_coverage_events.csv`.

### Points for the evidence file (not changed here)

- `evidence_citation` cites the DUR passage as p. 34; the file has 4 pages and the passage is on p. 3.
- Zepbound start 11/1/2024 is the date of the earliest document in hand listing it; the Common Formulary's table of changes effective November 1, 2024 does not name Zepbound.
- `quantity_limits` = Yes is documented only from 08/01/2025.
- Thresholds on the 08/01/2024 form are BMI 30, or 27 with a risk factor; `pa_stringency` describes 2022 to 2025 as appropriateness PA with BMI unknown.

### Internet Archive searches (all 2026-11-15, run by KS)

| URL or prefix searched | Result |
|---|---|
| `web.archive.org/web/*/mi.primetherapeutics.com/provider/external/medicaid/mi/doc/en-us/*` (link form) | No captures listed |
| `mi.primetherapeutics.com/provider/external/medicaid/mi/doc/en-us/` (typed as prefix, URLs tab) | Nothing found |
| `michigan.magellanrx.com/` (typed as prefix, URLs tab) | 243 URLs captured; filter "obesity" returns 1: `MIRx_PAfaxform_anti-obesity_medications.pdf`, one capture, August 18, 2024. Downloaded. |
| `https://mi.primetherapeutics.com/provider/external/medicaid/mi/doc/en-us/MIRx_PDL.pdf` (exact URL) | Earliest capture April 2025 (edition effective 04/01/2025). Downloaded. |

Not yet searched: `MIRx_PDL.pdf` and `MIRx_quantity_limits.pdf` under `michigan.magellanrx.com` (filter "PDL" and "quantity" on the 243-URL list); earlier revisions of the PA form.

## Wisconsin (worked 2026-11-15)

Covered quarters: 2023Q2 to 2026Q2 (13). The document coded in the evidence file takes effect 7/1/2026, after every covered quarter, so none of its rules apply to the quarters counted.

Compared: form F-00163 (04/2023); ForwardHealth Update 2024-16 (effective July 1, 2024); Update 2026-15 (effective July 1, 2026); quick-reference PDLs effective 01/01/2023, 07/01/2024, 01/01/2025.

- BMI thresholds are the same in 04/2023 and 7/1/2024: "BMI greater than or equal to 27 but less than 30 and has two or more of the following risk factors". The 2024 Update redefines the risk factors.
- Six-month weight loss treatment plan: same wording in both.
- Renewal: the 04/2023 form states no test. Update 2024-16: "weight loss goal of at least 5 percent of their weight from baseline", 12 continuous months maximum, "will not be renewed if a member's BMI is below 24". Carried back for 2023Q2 to 2024Q2.
- None of the three PDLs lists the class; Update 2026-15: "Effective July 1, 2026, ForwardHealth will add weight management agents as a new drug class to the PDL."
- Update 2026-15 names a form revision F-00163 (11/2025), not in hand.

Points for the evidence file: (1) from 7/1/2026, "PA requests for Wegovy injection will only be approved for" MACE, MASH, and ages 12 to 17 with obesity, so adult weight loss with Wegovy injection ends; the events row lists Saxenda and the oral agents but not this. (2) The 2026 rules differ from 2024 to 2026 on lifestyle (agreement to diet in place of a six-month plan) and renewal (reduction in BMI; floor of 18.5 in place of 24); `bmi_adult_criteria` says "unchanged in substance", which is true of BMI only.

Archive searches: none run.

## Mississippi (worked 2026-11-15)

Covered quarters: 2023Q3 to 2026Q2 (12). The coded criteria (V11) take effect 7/1/2026, after every covered quarter.

Compared: Universal PDL effective 10/01/2023, 1/1/2024 (version 2024_3), 04/01/2025 (version 2025_5), 10/1/2026 (version 2026_16). Criteria v1.3, V7 and V11 are not in hand.

- PA and placement are the same from 10/01/2023 to 04/01/2025: "All agents require MANUAL PA"; Saxenda and Wegovy preferred.
- The 04/01/2025 edition adds: "Wegovy Initial Authorization: Age 18 years or older AND Documented diagnosis of Body Mass Index (BMI) >/= 30 AND History of </= 6 claims with Wegovy in the past 9 months".
- No quantity limit in the class in the first three editions; "Quantity Limit" with amounts first appears in the edition effective 10/1/2026.
- Lifestyle and renewal rules are known only from V7 (10/30/2025) and are carried back to 2023Q3.

Points for the evidence file: `quantity_limits` = Yes is documented only from 10/1/2026; Contrave was preferred in the 10/01/2023 edition and absent from 1/1/2024.

Archive searches: none run. Earlier searches recorded in `docs/notes_on_the_rules.md` found nothing.

## California (worked 2026-11-15)

Covered quarters: 2023Q1 to 2025Q4 (12).

Compared: Contract Drugs Lists dated January 17, 2023, February 1, 2024, August 1, 2025 and September 1, 2025; Medi-Cal Rx alert of June 14, 2024.

- Same entry in all four lists: "Restricted to 1) Chronic weight management; and 2) Maximum quantity of 1 carton". All quarters between the first and last list are bracketed on restriction and quantity limit (classed observed, since the first list predates them).
- The alert adds BMI codes from April 30, 2024.
- No BMI value, lifestyle, step, renewal or preferred tier in any list: classed absent by inference.

Points for the evidence file: the file `CA_zepboundcoverage_2024.pdf` is the Code I alert, not a Zepbound notice. Dates printed in the files differ from the manifest: "CA PDL 2024" is February 1, 2024; "CA PDL 2025" is August 1, 2025; the file named FINAL is September 1, 2025. `criteria_as_of` 8/1/2025 can move to 1/17/2023 for the restriction and quantity limit.

Archive searches: none needed.

## Kansas (worked 2026-11-15)

Covered quarters: 2024Q2 to 2026Q2 (9). The coded criteria were last reviewed 8/19/2026, after every covered quarter.

Compared: PDLs dated 02/01/2023, 12/01/2024, 08/01/2025. No criteria document is in hand.

- 02/01/2023: no anti-obesity class. 12/01/2024: Zepbound preferred; Saxenda and Wegovy "Non-Preferred, Prior Authorization Required". 08/01/2025: Wegovy and Zepbound preferred; Saxenda non-preferred.
- BMI and lifestyle rules are known only from the 8/19/2026 criteria: carried back for all 9 quarters.
- Renewal: the repository records checkpoints from the 1/17/2024 version (3, 5, 6 percent) that differ from the 2026 version, so the rule changed at an undocumented date.
- The PDLs state no quantity limits for any class: no information.

Points for the evidence file: `preferred_status` reads "Not documented" and can be filled from the two PDLs.

Archive searches: none run.

## Pennsylvania (worked 2026-11-15)

Covered quarters: 2023Q2 to 2025Q4 (11).

Compared: Statewide PDL dated January 9, 2023; effective January 8, 2024 (v12); effective July 7, 2025 (v2); SPA PA-26-0003.

- Same in all three PDLs: Saxenda and Wegovy preferred with "PA, QL"; Zepbound added January 8, 2024. "Prior authorization guidelines for drugs and products included in the Statewide PDL apply to FFS and the Pennsylvania Medical Assistance MCOs."
- BMI, lifestyle and renewal rules are known only from the plan policy v1.2025, which says the criteria were revised "according to DHS revisions effective 09/02/2024". Carried back for 2023Q2 to 2024Q3.

Points for the evidence file: `quantity_limits` and PA are documented from January 9, 2023 in a state document; the statewide PDL statement above bears on `ffs_mco_scope`, which lists Pennsylvania among the four states coded from one plan.

Archive searches: none run.

## Delaware (worked 2026-11-15)

Covered quarters: 2023Q1 to 2026Q2 (14).

Compared: 23 DE Reg 464 (final order effective December 11, 2019); PDL revised 01/17/2023; SPA DE-24-0010 (effective August 1, 2024); PDL revised 8/4/2025; PDL effective 11/2/2026; SPA DE-26-0003.

- The sentence the evidence file takes from SPA DE-24-0010 is already in the 2019 order: "Drugs indicated for the treatment of obesity to address weight loss with co-morbid conditions are covered by the DMAP with prior authorization." SPA DE-24-0010 "proposes to amend the State Plan to add coverage of prescribed drugs when medically necessary during drug shortages". So 8/1/2024 is not a criteria date, and the rule is bracketed from 2019 to 2024.
- "Two (2) preferred products required before a non-preferred product will be approved" is in the 01/17/2023, 8/4/2025 and 11/2/2026 editions.
- Saxenda preferred on 01/17/2023 ("Preferred status implementation: 1/1/23"); non-preferred on 8/4/2025.
- No quantity limit in the class in any edition.
- Renewal is classed carried back for 2023Q1 to 2025Q2 because the only version-labelled statement is from the plan policy effective 09.25. This raises Delaware's count of quarters with a carried-back field from 7 to 10; reading the 01.23 policy would settle it.

Points for the evidence file: `step_therapy` says the 2026 PDL "adds" the two-preferred-products rule; it is in the 2023 PDL. `criteria_as_of` 8/1/2024 rests on an SPA about drug shortages.

Archive searches: none run. Earlier searches recorded in `docs/notes_on_the_rules.md` found nothing.

## New Hampshire (worked 2026-11-15)

Covered quarters: 2022Q4 to 2025Q4 (13).

Compared: PDL effective September 1, 2022; weight management criteria approved June 10, 2024 (archive capture of 2024-10-04); PDL effective July 14, 2025; criteria effective 1.1.2026.

- Same in both PDLs: Saxenda and Wegovy preferred; prior approval for the class; "Trial and failure of 2 Preferred products required prior to Non-Preferred products"; no quantity-limit mark.
- The June 10, 2024 criteria list earlier approvals on 01/14/2022, 01/26/2023 and 06/29/2023. Those versions are not in hand, so BMI, diet trial and renewal are carried back for 2022Q4 to 2024Q1.

Points for the evidence file: `preferred_status` reads "Not documented" and can be filled from the two PDLs.

Archive searches: none run in this session; the 2024-10-04 capture was found earlier.

## Virginia (worked 2026-11-15)

Covered quarters: 2023Q1 to 2026Q2 (14).

Compared: PDL version 01/01/2023v5; PDL version 08/09/2024. The service authorization forms are not in hand.

- 2023: Saxenda and Wegovy in the preferred column, "Weight Management Agents SA Form". 2024: Saxenda, Wegovy and Zepbound in the non-preferred column, "The selected GLP-1 Receptor Agonist is Saxenda".
- BMI and renewal before 2024Q3 are carried back from the form effective 7/1/2024, which the repository records as still showing BMI 30, or 27 with two risk factors.
- No quantity limit marked in either PDL.

Points for the evidence file: `preferred_status` reads "Not documented" and can be filled from the two PDLs.

Archive searches: none run in this session.

## Massachusetts (worked 2026-11-15)

Covered quarters: 2024Q2 to 2026Q2 (9).

Compared: MassHealth Drug List of January 02, 2024 (Table 81); Prescriber e-Letter, October 2024; Drug List of August 11, 2025 (Table 81). `MA_PA_2024.pdf` could not be read as text (font encoding) and was not used.

- BMI thresholds (30, or 27 with a comorbid condition) and the 5 percent recertification test are the same in the 2024 and 2025 lists.
- The e-Letter dates each change: Zepbound preferred October 1, 2024; Wegovy and Saxenda non-covered for adults January 1, 2025; phentermine trial January 6, 2025.
- Every cell is observed; none carried back.

Points for the evidence file: `quantity_limits` = No, but the 2024 list requires "requested quantity is ≤ four pens/28 days" for Wegovy.

Archive searches: none needed.

## Missouri (worked 2026-11-15)

Covered quarters: 2024Q4 to 2026Q2 (7).

Compared: SmartPA Criteria Proposal (Proposed Date October 15, 2024; image-only PDF, read by eye); PDL effective February 1, 2025; PA form 2575-053, April 2026.

- The proposal reads "First Implementation Date: TBD" and "New Criteria". The earliest document showing the class in force is the PDL effective February 1, 2025. No document in hand supports the 10/1/2024 start, so 2024Q4 is classed no information.
- BMI rule is the same in the proposal and the April 2026 form: bracketed for 2025Q1 to 2026Q1.
- The proposal sets maximum dosing limits and "Default Approval Period: 1 year".

Points for the evidence file: Zepbound start 10/1/2024; `quantity_limits` = No against the limits in the proposal.

Archive searches: none run.

## Rhode Island (worked 2026-11-15)

Covered quarters: 2023Q1 to 2026Q2 (14).

Compared: PDLs updated January 10, 2023; January 17, 2024; October 1, 2024; January 14, 2025 (revised February 21, 2025).

- Same in all four: "Clinical Prior Authorization Required for Entire Class"; Saxenda and Wegovy in the preferred column; "Length of Authorization: 1 Year". Zepbound appears in the non-preferred column from the October 1, 2024 edition.
- BMI, program requirement, renewal and quantity limit come from one plan's policy as reviewed 5/2024 and are carried back for 2023Q1 to 2024Q1.

Points for the evidence file: the file `RI_RITogether_GLP1_notice_2026.pdf` was not the provider notice (misfiled). It has been removed from the manifest and the collection; the notice is cited by URL in the events file.

Archive searches: none run.

## South Carolina (worked 2026-11-15)

Covered quarters: 2025Q1 to 2025Q4 (4).

Compared: bulletin MB# 24-016 (May 8, 2024); a plan's prescription benefits page; Single PDL effective November 1, 2026.

- None of the three is dated in the coverage period or states a rule for it. The bulletin sets up the single PDL from July 1, 2024. The 2026 PDL has no weight management class.
- Preferred placement rests on the PDL effective 12/1/2025 as recorded in the evidence file (tier 2). All other fields are no information.

Archive searches: none run.

## Update, 2026-11-15, after two more documents

**Delaware.** `DE.PMN.50_Anti-Obesity_Medications_01.23.pdf` (Delaware First Health, "Effective Date: 01.23", revision log "Policy developed. 01.23") is now in hand. It states the BMI rule, the diet trial ("Documented failure of at least a three-month trial on a low-calorie diet") and the renewal tests ("After six months of therapy, a six month approval may be granted if a 5% weight reduction has been achieved"; 10% after one year). Renewal for 2023Q1 to 2025Q2 moves from carried back to observed, and BMI and lifestyle move to tier 1. Delaware now has no carried-back cell. The policy does not name Zepbound and has no 4 percent test for Saxenda, which the evidence file records for the 09.25 version. The policy is copyrighted by the plan's parent company: cite, do not deposit.

**Kansas.** The KDHE criteria ("Last Reviewed: August 19, 2026", "Minor updates 11/1/2026") are now in hand. Review history: "Revised Dates: August 14, 2024; January 17, 2024; July 19, 2023; October 19, 2022; ...". The text dates its own exceptions: "This section does not apply for the following drugs: Zepbound(as of 4/1/24), Wegovy(as of 6/1/25), Foundayo (as of 11/1/2026)". BMI, lifestyle, renewal and dose limits for 2024Q3 to 2026Q2 are classed dated by a later document, on the assumption that the August 19, 2026 review did not change them (the last revision listed is August 14, 2024). 2024Q2 stays carried back because the version revised January 17, 2024 is not in hand. The checkpoints the repository recorded from the January 2024 version (3, 5, 6 percent) equal the initial 8-week values in Table 4 of the current document, so no renewal change is evident. The review history also shows the criteria existed from 2007 and were revised in 2021, 2022 and 2023, before the 4/1/2024 start in the evidence file.

**Result.** Covered quarters with at least one rule carried back: 53 of 181 (29 percent), from 71. Cells carried back: 127 of 894 (14.2 percent).

## Audit of files before commit, 2026-11-15

Checked: 54 PDFs, 14 Word files, 2 spreadsheets and every text file in the repository zip. Git history was checked separately on the same day and the removed file was never committed. Not checked: 62 non-chart files listed in the manifest for states whose folders were not sent.

- `RI_RITogether_GLP1_notice_2026.pdf`: not the provider notice; removed from the manifest.
- Deposit set to no for six vendor files: four New Hampshire files marked "Proprietary & Confidential", `Prescription BenefitsSC.pdf`, `MO_wegovyzep_2024.pdf`.
- `README.md`: journal name removed from the tag example.
- No local paths and no proprietary data in the repository text files.

## Update, 2026-11-15, after the Pennsylvania bulletins and Wisconsin Update 2023-09

**Pennsylvania.** Two DHS Medical Assistance Bulletins with handbook pages are now in hand: issued December 9, 2022, effective January 9, 2023 (`MAB2022120903.pdf`), and issued November 14, 2023, effective January 8, 2024 (`MAB2023111401.pdf`).

- January 9, 2023: "All prescriptions for Obesity Treatment Agents must be prior authorized." Adults: "Has a body mass index (BMI) greater than or equal to 30 kg/m2", or "greater than or equal to 27 kg/m2 and less than 30 kg/m2" with "at least one weight-related comorbidity as determined by the prescriber". "Has been counseled about lifestyle changes and behavioral modification". Renewal: "a percent reduction of baseline body weight that is consistent with the recommended cutoff ... after 3 months of therapy with the maximum recommended/tolerated dose".
- January 8, 2024: the bulletin lists its revisions (under-18 path below the 95th percentile deleted; PDMP search deleted; renewal clarified for dose titration). Adult BMI rule unchanged. "For a GLP-1 receptor agonist (e.g., Saxenda or Wegovy), all requests will be approved for up to 6 months."
- Scope: "The guidelines to determine the medical necessity of Obesity Treatment Agents will be utilized in the fee-for-service and managed care delivery systems."
- Neither version has the diabetes-status prerequisite recorded from the plan policy that reflects the 09/02/2024 revision. Pennsylvania's criteria therefore restate the label thresholds until 09/02/2024, which agrees with Klebanoff's June 2024 coding; the stricter rule dates from 09/02/2024 or later.
- Pennsylvania now has no carried-back cell. Still wanted: the DHS bulletin for the 09/02/2024 revision.

**Wisconsin.** ForwardHealth Update 2023-09 (March 2023, effective April 1, 2023; `2023-09.pdf`) is now in hand.

- It restates the BMI rule and the six-month treatment plan, and "PA requests for anti-obesity drugs will not be renewed if a member's BMI is below 24."
- "The additional clinical criteria for initial and renewal PA requests have not changed." The weight-loss test for renewal is not stated, so it stays carried back for 2023Q2 to 2024Q2.
- No quantity limit in the section: quantity limit for 2023Q2 to 2024Q2 moves from no information to absent by inference.
- Coverage predates April 1, 2023: the Update says ForwardHealth "has revised the clinical criteria", "will honor PA requests for anti-obesity drugs that were approved before April 1, 2023", and "will no longer cover Qsymia for obesity". The 4/1/2023 start in the evidence file is the date of a criteria and form revision, not the start of coverage.

**New Hampshire.** Notice of February 1, 2023 (in hand) lists Weight Management under "CLINICAL PRIOR AUTHORIZATION REVISIONS", effective March 1, 2023. It gives no rule. A copy of the criteria approved June 29, 2023 was located by web search on a vendor test server (`nh.smartrx-dev.lh.primetherapeutics.com`); the request was blocked on 2026-11-15.

**Mississippi.** Web search located `https://medicaid.ms.gov/wp-content/uploads/2023/04/Anti-obesity-Select-Agents-PA-Criteria-V1.3.pdf`; the site was still not responding on 2026-11-15.

**Result.** Covered quarters with at least one rule carried back: 47 of 181 (26 percent); 35 of 181 (19 percent) without Mississippi. Cells carried back: 109 of 894 (12.2 percent).

## Update, 2026-11-15, Wisconsin forms and a hearing decision

In hand: form F-00163 (07/2021), form F-00163 (09/2022), and Division of Hearings and Appeals decision MPA-218601 (petition filed May 31, 2025; hearing July 16, 2025).

- Both earlier forms have the same adult BMI rule as the 04/2023 form ("BMI greater than or equal to 27 but less than 30 and has two or more of the following risk factors", the same five risk factors) and the same six-month weight loss treatment plan question, with a minimum age of 16 where the 04/2023 form has 18. The BMI and lifestyle rules were therefore in place from 07/2021.
- The 07/2021 form names Saxenda ("Members must be 12 years of age or older to take Saxenda and Xenical"). Neither earlier form names Wegovy; the forms name drugs only where an adolescent rule differs, so this does not show whether Wegovy was covered for adults before 04/2023.
- None of the forms states the weight-loss test for renewal. The hearing decision quotes the Saxenda renewal rule as applied in 2025, after the July 2024 Update. Renewal for 2023Q2 to 2024Q2 stays carried back.
- For the evidence file: Saxenda was on the Wisconsin PA form by 07/2021, so `saxenda_start_date` of 4/1/2023 is too late. Moving it would add covered quarters before 2023Q2, which are not classed here.
- The hearing decision is one member's appeal (name redacted in the decision) and is dated August 26, 2025; no cell depends on it.

Open question sent to a Wisconsin Medicaid contact: which Updates added Saxenda and Wegovy to the anti-obesity PA, and whether an archived Online Handbook topic #7837 from 2023 exists.

## Update, 2026-11-15, Pennsylvania bulletin effective September 2, 2024

In hand: `mab2024080702.pdf` (issued August 7, 2024, effective September 2, 2024; handbook pages "Replacing January 8, 2024").

- The step added on September 2, 2024 applies to members with diabetes only. A preferred GLP-1 obesity drug requires one of: "A diagnosis of diabetes mellitus or a history of an antidiabetic drug in the last 120 days" together with failure of the preferred GLP-1 diabetes drugs; or "Does not have a diagnosis of diabetes mellitus or a history of an antidiabetic drug in the last 120 days".
- For the evidence file: `pa_stringency` and `step_therapy` describe this as requiring "concurrent diabetes or antidiabetic use in past 120 days before a preferred GLP-1". The handbook pages say the opposite for members without diabetes: they meet the guideline with no step. The basis for coding Pennsylvania `more_restrictive` should be re-read against this bulletin.
- Adult BMI rule unchanged from January 9, 2023. All Pennsylvania cells are now tier 1 from three state bulletins and three PDLs.
- The search-list entry for this bulletin is closed.

## Update, 2026-11-17, Kansas extended back to 2021 Q1

In hand since 2026-11-17: `KS_KMAP_GeneralBulletin_23255_20231006.pdf` (October 2023) and `KS_Weight_Loss_Agents_PA_criteria_draft_2023-07-19.pdf` (approved draft with "Revised Dates: July 19, 2023"; PDF created July 12, 2023).

- Bulletin 23255: for dates of service on and after September 19, 2023, coverage "will include all AOMs that are rebate eligible". No products named.
- Criteria revised July 19, 2023: list of agents includes "Liraglutide (Saxenda®)" and "Semaglutide (Wegovy™)"; adults "BMI ≥ 30 kg/m2" or 27 with a comorbidity; Table 4 "High-cost" agents are Saxenda and Wegovy, with "Adults: BMI ≥ 40 kg/m2". Review history back to June 15, 2011; "Initial Approval: September 14, 2007".
- SDUD (`outputs/state_quarter_product_counts.csv`): Kansas Saxenda 421 prescriptions in 2021 Q1; Wegovy 0 in 2021 Q3 and 148 in 2021 Q4; Zepbound 0 in 2023 Q4 and 222 in 2024 Q1.
- Decision (KS, 2026-11-17): Kansas covered quarters run from 2021 Q1. Saxenda start 1/1/2021 (start of the window), Wegovy start 10/1/2021, both with `start_basis` `prescriptions_observed`. The bulletins are events, not starts.
- Spans added for 2021 Q1 to 2024 Q1: 2023 Q3 to 2024 Q1 observed from the July 2023 criteria; 2021 Q1 to 2023 Q2 no information on BMI, lifestyle, renewal and quantity limit (versions revised April 21, 2021, July 21, 2021 and October 19, 2022 are not in hand), PA dated by the later document; preferred product absent by inference from 2023 Q1 (no anti-obesity class in the PDL dated 02/01/2023).
- The two spans that cited bulletin 24071 as not in hand now cite the file (tier 1).

**Result.** 162 covered state-quarters and 972 cells in the 13 states checked. Cells: observed 579 (59.6 percent), dated by a later document 52 (5.3), bracketed 10 (1.0), carried back 109 (11.2), absent by inference 129 (13.3), no information 93 (9.6). Covered quarters with at least one rule carried back: 47 of 194 (24 percent).

Still to find for Kansas: the criteria versions revised April 21, 2021, July 21, 2021, October 19, 2022 and January 17, 2024.

## Update, 2026-11-17, five more states dated from the prescription record

Decision (KS, 2026-11-17): Wisconsin, Delaware, Virginia, New Hampshire and Rhode Island are re-dated the same way as Kansas. The grounds, in full:

1. SDUD prescriptions per 100,000 enrollees exceed every one of the 33 never-covering states in each quarter from the recorded start. Saxenda in 2021 Q1, against a never-covering maximum of 5.9 per 100,000: Wisconsin 55.8 (651 prescriptions), Delaware 46.1 (115), Virginia 22.3 (336), New Hampshire 16.0 (32), Rhode Island 11.4 (34).
2. The never-covering states have the same pediatric EPSDT route, so EPSDT cannot explain the margin; and Wegovy had no adolescent approval until December 23, 2022, so its 2021 and 2022 prescriptions (first quarters: Wisconsin 2021 Q4, 368; Delaware 2021 Q3, 12; Virginia 2021 Q3, 33; New Hampshire 2022 Q1, 48; Rhode Island 2022 Q1, 74) were adult use on the label.
3. Documents that predate the superseded starts agree where they exist: Wisconsin form F-00163 (07/2021, in the collection) names Saxenda with adult BMI criteria; Delaware's state plan has covered obesity drugs with co-morbid conditions and PA since December 11, 2019 (23 DE Reg 464, in the collection); Virginia plan criteria revised 12/6/2022, "Adapted from DMAS Preferred Drug List", list Saxenda and Wegovy (clue C014); the Rhode Island Neighborhood Health Plan weight-loss policy has run since 7/2018 (clue C015). New Hampshire has no pre-2022 document in hand, but Khanna et al. date it to 2021 Q3 (clue C016).

New starts (basis `prescriptions_observed`): Saxenda 1/1/2021 in all five (start of the data window); Wegovy 10/1/2021 (WI), 7/1/2021 (DE, VA), 1/1/2022 (NH, RI). Zepbound dates are unchanged (post-launch documents). The superseded dates remain in the files as document dates. Covered quarters for the rule history now run from 2021 Q1 in all six re-dated states; the newly added quarters are classed observed where the Wisconsin forms and the Delaware state plan apply, and no information otherwise.

**Result.** 202 covered state-quarters and 1,212 cells in the 13 states checked: observed 616 (50.8 percent), dated by a later document 61 (5.0), bracketed 10 (0.8), carried back 109 (9.0), absent by inference 130 (10.7), no information 286 (23.6). Covered quarters with at least one rule carried back: 47 of 202 (23 percent).

Still to find: the documents behind clues C014 to C016, and any Wisconsin form earlier than 07/2021.
