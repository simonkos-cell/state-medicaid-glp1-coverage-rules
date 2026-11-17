# Change log

Every change to files in `data/` relative to the frozen NBER w34949 version, newest first.

| Date | File | State | Field | Old value | New value | Source | By |
|---|---|---|---|---|---|---|---|
| 2026-11-15 | state_criteria_history.csv; criteria_status_by_quarter.csv; criteria_status_spans.csv; covered_quarters.csv | CA,DE,KS,MA,MI,MO,MS,NH,PA,RI,SC,VA,WI | (new files) | | Rule history by state and period, and a class for every covered state-quarter and rule (observed, dated by a later document, bracketed, carried back, absent by inference, no information). Covered quarters with a rule carried back: 47 of 181, from 111 | docs/criteria_history_log.md; code/build_criteria_status.py | KS |
| 2026-11-15 | state_coverage_events.csv | CA,DE,KS,MI,MS,PA,VA,WI | (9 new rows) | | criteria_revision rows dated from the documents compared | docs/criteria_history_log.md | KS |
| 2026-11-15 | document_manifest.csv | RI | file row | RI/Documents/RI_RITogether_GLP1_notice_2026.pdf | (removed) | File was not the provider notice | KS |
| 2026-11-15 | document_manifest.csv | NH,SC,MO | deposit | yes | no for six vendor or plan documents (cited, not deposited) | Vendor confidentiality or copyright notices on the documents | KS |
| 2026-11-15 | document_manifest.csv | DE,KS,MI,NH,PA,WI | (12 new rows) | | Documents obtained during the criteria history check | docs/criteria_history_log.md | KS |
| 2026-10-25 | state_coverage_events.csv | MA | (new row; 2026-02-17 row expanded) | | Wegovy reinstated 2026-02-17 at parity with Zepbound; Saxenda pediatric only; adult BMI criteria (35+, or 30 to under 35 or 27+ with listed conditions) | MassHealth Pharmacy Facts 269 (Jan 14 2026): "Wegovy®(semaglutide) will be added as a preferred drug managed at parity with Zepbound®", "Effective February 17, 2026" | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MA | wegovy_end_date | Continued coverage through Q1 2026 | 1/1/2025 | MassHealth Prescriber e-Letter Vol. 14 Issue 3 (Oct 2024): Wegovy and Saxenda "will be noncovered agents for the treatment of overweight and obesity in adults" from January 1, 2025; matches the state's evidence note and the Wegovy pause date in GLP1_Coverage_with_PA_QL_Date.csv | KS |
| 2026-10-25 | state_coverage_events.csv | MA | (new rows) | | 2025-01-01 end of Wegovy and Saxenda for adult weight management; 2025-01-06 phentermine step for new starts | MassHealth e-Letter Oct 2024; Pharmacy Facts 235 (Nov 19 2024) | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | DE,KS,MI,NC,PA,RI,TN,UT | criteria columns | not_documented or partial | criteria from retrieved state/MCO documents; UT and RI reclassified more_restrictive | docs/state_notes.md | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | all | 12 new columns | | pa_stringency, bmi_adult_criteria, bmi_adolescent_criteria, step_therapy, age_minimum, quantity_limit_detail, ffs_mco_scope, criteria_as_of, criteria_source, klebanoff_stringency_june2024, khanna_start_quarter, w34949_adoption_quarter; populated for the 17 covering states | docs/coverage_dimensions_codebook.md; docs/state_notes.md | KS |
| 2026-10-25 | outputs/state_coverage_summary.xlsx | all | (new file) | | Generated workbook (by_state, by_state_molecule, events, dimensions) | code/make_summary_workbook.py | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MN | wegovy_start_date, saxenda_start_date | 3/1/2023 (after first fix) | 12/17/2021 | SPA MN-21-0022 approved 12/17/2021 (effective 7/1/2021); Minn. Laws 2021 1st Spec. Sess. ch. 7 art. 1 s. 10; Itasca Medical Care update Feb 17, 2022 | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MS | wegovy_start_date, saxenda_start_date | 10/1/2023 | 7/1/2023 | MS Division of Medicaid Select Covered Obesity Medications PA Criteria v1.3, effective 7/1/2023 | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | NH | zepbound_start_date | 7/14/2025 (after first fix) | 9/1/2024 | NH FFS PDL effective September 1, 2024 lists Zepbound | KS |
| 2026-10-25 | state_coverage_events.csv | NH | end 2026-01-01 source | KFF (tier 2) | NH Medicaid notification Oct 9, 2025 (tier 1) | nh.primetherapeutics.com notification | KS |
| 2026-10-25 | state_coverage_events.csv | VA | (new row) | | restrict 2023-06-23, tightened criteria | JCHC 2023 report Table 4; DMAS RD208 | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | KS | wegovy, saxenda, zepbound start dates | 6/1/2024 | 4/1/2024 | KMAP General Bulletin 24071 (April 17, 2024), effective April 1, 2024; KDHE anti-obesity PA form | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MI | zepbound_start_date | 11/24/2026 | 11/1/2024 | MDHHS Medicaid Health Plan Common Formulary dated 11/1/2024 (spreadsheet date-parsing error) | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | NC | saxenda_start_date, zepbound_start_date | 8/24/2026 | 8/1/2024 | NC Medicaid PDL "Revised 8.1.2024 for addition of weight management agents" | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | NH | zepbound_start_date | 9/24/2026 | 7/14/2025 | Earliest PDL in hand listing Zepbound (effective July 14, 2025); may be earlier | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | NH | zepbound_end_date | 1/26/2026 | 1/1/2026 | Same end as Wegovy and Saxenda (date-parsing error) | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | TN | wegovy_start_date, zepbound_start_date | 8/25/2026 | 8/1/2025 | TennCare PDL effective August 1, 2025; SPA TN-25-0006 | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MN | wegovy_start_date, saxenda_start_date | 6/15/2023 | 3/1/2023 | June 15, 2023 PDL, p. 32: "WEIGHT MANAGEMENT AGENTS section added 3-1-2023" | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | VA | zepbound_start_date | 1/1/2024 | 8/9/2024 | Earliest PDL in hand listing Zepbound (8/9/24); no January 2024 document | KS |
| 2026-10-25 | document_manifest.csv | all | (new file) | | Manifest of the 138 files in the 2025 evidence folder, with deposit flags | docs/audit_2026-10.md | KS |
| 2026-10-25 | state_coverage_events.csv | CA, NH, PA, SC, MI, MA, UT, RI, NC | (new file) | | 11 dated changes, late 2025 to October 2026 | See source columns in file | KS |

## Open issues to check (not yet changed)
- Criteria documents retrieved 2026-10-25 for DE, KS, MI, NC, PA, RI, TN, UT (see docs/state_notes.md); UT and RI reclassified to more_restrictive. Still to obtain: SC (criteria in the Single PDL, not posted separately); NH (the older NH Healthy Families NH.PMN.50 revision; current version excludes GLP-1s).
- Two stringency disagreements with Klebanoff et al. (MN, MS) to resolve against their appendix.
- Oral GLP-1 agents (oral semaglutide, orforglipron) not yet tracked; add columns when a state lists one.
Full audit against the state documents: `docs/audit_2026-10.md`.
- Kansas: start revised to 4/1/2024 (same quarter as before). Open question whether Saxenda and Wegovy were paid without PDL PA before April 2024 (the April 2024 bulletin adds PDL PA to them; SDUD shows some 2023 use).
- Reconciliation with Khanna et al. eTable 1 (docs/audit_2026-10.md): NH, MN, KS (and VA by one quarter) have paid Saxenda or Wegovy claims in SDUD before the PDL dates in this file, which are lower bounds on coverage. Needs a quarterly SDUD check by product before any change to start dates or to the w34949 cohorts. MS may be 2023 Q3 (July 2023 PDL Rev 8, not in folder).
- Mississippi: start now 7/1/2023 (PA criteria effective date), one quarter earlier than the 10/1/2023 PDL; w34949 adoption quarter moves from 2023 Q4 to 2023 Q3.
- Minnesota: start now 12/17/2021 (SPA approval), which moves the w34949 adoption quarter from 2023 Q2 to 2021 Q4 (or 2022 Q1 if keyed to first claims). Zepbound 12/1/2024 not verified (RA notes cite a January 1, 2025 PDL not in the folder).
- Coverage before the PDL listing date: SDUD shows Saxenda claims from 2019 to 2021 in NH, VA, KS, RI, DE, WI, so the start dates for those states mark the PDL class listing, not first coverage. Khanna et al. excluded DE and KS on this ground. Needs a decision on the exposure definition (any weight-loss GLP-1 versus Wegovy/Zepbound) before the next w34949 revision.
- South Carolina: no documents in the folder; obtain the November 2024 Single PDL cited in the evidence file.
- California: Zepbound start (10/1/2024) not pinned by a document between the Feb 2024 and 2025 Contract Drugs Lists.
- Missouri: implementation date lies between the October 15, 2024 SmartPA proposal and the February 1, 2025 PDL; Wegovy is non-preferred in the obesity class, so "NA" understates it.
- Rhode Island: 10/18/2022 is a class review date in the January 10, 2023 PDL; earlier coverage cannot be excluded without a 2022 PDL.
- West Virginia: Wegovy PA memo (9/25/24) cited in RA notes is not in the folder.
- Georgia: Saxenda non-preferred with PA for ages 12 to 17 (RA notes); check before using Georgia as never-treated in an adolescent analysis.
- Delaware: `legacy_2025_maddie_potter/GLP1_Coverage_with_PA_QL_Date.csv` gives end dates of 3/1/2026, while the evidence file says "Continued coverage through Q1 2026" and 2026 trackers show Delaware covering. 3/1/2026 may be the end of data collection, not an end of coverage.
- Virginia: a service-authorization form dated July 31, 2025 (cited by a tracker) needs checking for any criteria change in 2025 Q3.
- Utah pilot end (June 30, 2026) rests on one news source; find the Utah Medicaid notice.

## Analysis notes added 2026-10-25
- docs/sdud_quarterly_check_2026-10.md: quarterly SDUD-by-product check for the lower-bound states; KS/VA/WI/DE covered Saxenda from 2019, so they are always-covered under the four-brand definition; how Khanna et al. handled this (excluded DE/KS/WI, kept CA as a PBM-transition case, eTable 5b Saxenda-excluded robustness).
- docs/controls_2026_drop_paper.md: clean comparison group for the 2026 drop paper (DE, KS, MN, MS, VA, WI); MA and MI removed as contaminated, KS added back; pooled DiD cross-check (withdraw 1.42 to 0.30, controls flat, DiD -1.11 per 100 enrollee-months).
- outputs/tables/sdud_quarterly_4states_check.csv, exhibit2_state_by_state_newcontrols.csv: supporting tables.

## Structure decisions and new fields, 2026-11-11

Two definitions settled, four fields added, and a clues file opened. Details in `docs/coverage_dimensions_codebook.md`.

- Molecule set is now time-dependent: Wegovy, Saxenda and generic liraglutide, and Zepbound through 3/31/2026; orforglipron (Foundayo) eligible to count from its FDA approval on 4/1/2026; oral semaglutide from its own approval. The approval date is when a molecule may count, not when a state covers it. No classification in the 2026 Q1 analyses changes.
- State coverage is established by a state-level document (PDL, state plan amendment, bulletin, or a rule binding all plans). A single managed care plan's policy does not make a state a covering state, though it may supply criteria detail, with `ffs_mco_scope` and `criteria_source` naming the level. Checked against Delaware (SPA DE-24-0010 sets the floor) and Rhode Island (FFS PDL applies class-wide manual PA): both remain covering states, so no reclassification follows.
- New columns on `state_coverage_evidence_sources.csv`: `indication_scope`, `preferred_status`, `renewal_criteria`, and start and end pairs for `oral_semaglutide` and `orforglipron`. All seeded as "Not documented" or NA, to be filled from documents. Indication scope and preferred status had no home before; renewal criteria were previously folded into `quantity_limit_detail`.
- New file `data/clues.csv`: unverified claims, kept apart from the evidence and events files, closed only by a document. Ten rows logged, eight open.
- Open and worth noting: C001 records a conflict in Virginia. The 2023-06-23 event row reports BMI 40, or 35 with two chronic conditions, from the JCHC report, while Wayback captures of the DMAS service authorization form show 30/27 on 7/28/2024 and 40/37 on 9/1/2024. Both cannot be right and the DMAS memo is needed. C002 (Delaware, plan amendment effective 1/1/2026) is the priority, because SDUD shows Delaware weight-management fills falling between 2025 Q4 and 2026 Q1.

## Virginia 2024 Q3 criteria resolved, 2026-11-11

Clue C001 closed. The apparent conflict between the June 2023 event row and the 2024 form captures was not an error in either; it is a gap between announcement and implementation.

- The DMAS bulletin "Upcoming Changes to Service Authorization Criteria for Weight Loss Drugs" (last updated 6/23/2023) announces the tightening but states the criteria apply once "a new service authorization form is in use." The 2023 row is therefore the announcement date, not the binding date, and its notes now say so.
- The service authorization form effective 7/1/2024 (Molina VA-ALL-PF-16714-24, revised 6/1/2024) still carried the pre-2023 thresholds: BMI at least 27 with two or more risk factors, or at least 30. The form effective 9/30/2024 (VA-ALL-PF-17859-24, revised 8/21/2024) carries BMI above 40 with no risk factors, or above 37 with one or more. New event row added at 2024-09-01, which is a bound: the DMAS form on the Wayback Machine showed the old thresholds on 7/28/2024 and the new ones on 9/1/2024.
- The implemented thresholds differ from the announced ones. The bulletin said BMI at least 40, or at least 35 with two or more chronic conditions; the form says above 40, or above 37 with one or more risk factors. This is a finding, not a transcription error, and both are recorded.
- Virginia's `renewal_criteria` filled from the same forms: 5 percent weight loss against the most recent authorization, and no renewal once BMI falls below 25. The 7/1/2024 form used 5 percent of baseline for Wegovy and Zepbound, 4 percent for Saxenda, and allowed renewal without weight-loss response where two or more risk factors were present.
- Still to obtain: the DMAS memo issuing the new form, which would pin the effective date. The forms used here are an MCO's, carrying DMAS criteria, so under the managed-care rule they are criteria detail pending the state document.


## Document hunt, 2026-11-11

- Evidence file: `indication_scope`, `preferred_status`, `renewal_criteria` filled for DE, MI, MS, NC, NH, PA, TN, UT; Mississippi criteria moved to the 10/30/2025 version (Wegovy lower BMI bound needs a check against the PDF); North Carolina quantity limits and criteria source updated.
- Events file: Delaware 2026-01-01 `plan_amendment` (SPA DE-26-0003) and Tennessee 2026-01-01 `restrict` (3-month approvals) added; Pennsylvania end raised to tier 1 (SPA PA-26-0003); Rhode Island end raised to tier 2.
- Clues: C002 confirmed, C003 partly confirmed.
- New file `data/projected_savings.csv` (4 rows).
- Quotes and URLs in `docs/document_hunt_2026-11-11.md`. Script: `code/enter_hunt_2026_11_11.py`.
- South Carolina and Rhode Island criteria unchanged (no new state document found).

- Second batch, same day: Wisconsin 2026-07-01 restrict (ForwardHealth Update 2026-15) and Missouri 2026-04-01 restrict (Wegovy excluded for weight reduction) added; criteria filled for WI and MO; Pennsylvania preferred_status updated from the UHC form effective 1/1/2026. Clues C005 and C006 confirmed, C004 partly confirmed. Script: `code/enter_hunt_2026_11_11b.py`.

## 2026-11-16: pre-release audit corrections

Applied by `code/apply_audit_fixes_2026_11_16.py`. Old and new values for every cell are in `outputs/audit_fixes_2026_11_16_log.csv` (26 entries). Sources are the documents named in each new value; the corrections were listed in `docs/criteria_history_log.md` under "Points for the evidence file" on 2026-11-15.

- `state_criteria_history.csv`, MI, `source_document/source_date/evidence_tier/notes`
- `state_coverage_evidence_sources.csv`, Michigan, `bmi_adult_criteria`
- `state_coverage_evidence_sources.csv`, Michigan, `quantity_limit_detail`
- `state_coverage_evidence_sources.csv`, Michigan, `evidence_citation`
- `state_coverage_evidence_sources.csv`, Wisconsin, `bmi_adult_criteria`
- `state_coverage_evidence_sources.csv`, Wisconsin, `indication_scope`
- `state_coverage_evidence_sources.csv`, Mississippi, `quantity_limit_detail`
- `state_coverage_evidence_sources.csv`, Kansas, `preferred_status`
- `state_coverage_evidence_sources.csv`, Pennsylvania, `step_therapy`
- `state_coverage_evidence_sources.csv`, Pennsylvania, `ffs_mco_scope`
- `state_coverage_evidence_sources.csv`, Pennsylvania, `quantity_limit_detail`
- `state_coverage_evidence_sources.csv`, Delaware, `step_therapy`
- `state_coverage_evidence_sources.csv`, Delaware, `criteria_source`
- `state_coverage_evidence_sources.csv`, New Hampshire, `preferred_status`
- `state_coverage_evidence_sources.csv`, Virginia, `preferred_status`
- `state_coverage_evidence_sources.csv`, Delaware, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Kansas, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Massachusetts, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Michigan, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Missouri, `pa_stringency`
- `state_coverage_evidence_sources.csv`, New Hampshire, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Pennsylvania, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Rhode Island, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Utah, `pa_stringency`
- `state_coverage_evidence_sources.csv`, Virginia, `pa_stringency`
- `state_coverage_events.csv`, WI, `description, drugs (2026-07-01 restrict)`

- New column `pa_stringency_note` in the evidence file; `pa_stringency` now has only the five codebook values.
- Pennsylvania `pa_stringency` changed from `more_restrictive` to `fda_label`: the DHS bulletin effective 9/2/2024 applies the GLP-1 diabetes-drug step only to members with diabetes or antidiabetic use in the last 120 days.
- New files: `data/state_drug_coverage.csv` (89 rows; one per state, product and spell for the 17 covering states and five products), `data/state_quarter_drug_panel.csv` (2,040 rows, built by `code/build_state_quarter_drug_panel.py`), and `docs/what_is_tracked.md`.
- Not changed, for a decision: `quantity_limits` is `No` for Massachusetts, Missouri, North Carolina and Rhode Island although `quantity_limit_detail` gives amounts; Delaware `criteria_as_of` (8/1/2024) is the date of an SPA that sets no criteria; the product start and end columns in the evidence file, which differ from `data/state_drug_coverage.csv` in the cases listed in `docs/what_is_tracked.md`.

- 2026-11-16, decided by KS: `quantity_limits` changed from `No` to `Yes` for Massachusetts, Missouri, North Carolina and Rhode Island, where `quantity_limit_detail` gives amounts (MassHealth Drug List of January 2, 2024: 'requested quantity is ≤ four pens/28 days'; Missouri proposal of October 15, 2024, dosing limits table; North Carolina criteria effective August 1, 2024; Rhode Island plan policy reviewed 5/15/2024, tier 2). Tennessee `saxenda_start_date` changed from 1/1/2026 to 8/1/2025 (TennCare provider notice effective August 1, 2025 lists Saxenda as non-preferred with PA and a quantity limit).

- 2026-11-16, manifest: `data/document_manifest.csv` rebuilt by `code/rebuild_manifest_2026_11_16.py` with new columns `source_url`, `source_url_kind` and `file_saved_date`; `bytes` refreshed from the files; document dates corrected for four California lists, the California Code I alert, the Delaware SPA and one Tennessee list. Of 83 source documents, 19 have the URL of the file, 33 the page that lists it, 3 an Internet Archive capture, 1 a related page, and 27 have no URL recorded.
- 2026-11-16, state documents: `code/build_state_documents.py` builds one summary document per state (50) from the data files. In the deposit folder the 31 notes written in 2025 for never-covering states, the 2025 readme and worksheet, and the combined never-covering document of 2026-11-15 were moved to `files/legacy/`; the 17 earlier covering-state documents were replaced. The manifest now has 273 rows and matches the folder file for file.

- 2026-11-16, decided by KS: Delaware `criteria_as_of` changed from 8/1/2024 (the date of an SPA that sets no criteria) to 9/1/2025; the coded policy version (DE.PMN.50) says only that it took effect in September 2025, and the first of the month was entered.
- 2026-11-16, manifest URLs: 22 more source addresses recorded, from the research assistant's 2025 state notes (14), web search (3) and document numbers or file names (5, marked `inferred` and not opened). Six source documents still have no address.

- 2026-11-16, documentation: new `docs/data_dictionary.md` (every column of the 12 data files). `README.md`, `CITATION.cff`, `.gitignore`, `docs/start_here.md`, `docs/coverage_dimensions_codebook.md`, `docs/notes_on_the_rules.md` and the deposit `README.txt` corrected; 33 text edits; the list of old and new wording is kept by the authors. Working records (one-time entry scripts, search logs, analysis notes for specific papers, the duplicate deposit readme) moved out of the public repository and kept by the authors. The deposit gained `files/data_and_documentation/` with copies of four data files and four documentation files. Manifest: 281 rows, matching the deposit folder.
- 2026-11-16, clues: C011 (Kansas, coverage from September 19, 2023), C012 (Michigan bulletin MSA 21-49), C013 (North Dakota and Texas communications) added from the 2025 summary document; not yet checked.

## 2026-11-17: status on the freeze date, Rhode Island state memorandum, Kansas bulletin 23255

- Evidence file: two new columns after `coverage_status`. `status_on_2026_11_16` (`covered`, `covered_restricted`, `ended`, `unknown`, `not_covered`) is derived from the last spell of each product in `data/state_drug_coverage.csv`; `weight_loss_coverage_end_date` gives the date for the six states with status `ended` (California, New Hampshire, Pennsylvania and South Carolina 1/1/2026; Massachusetts 7/3/2026; Rhode Island 10/1/2026). Utah is `unknown`. The file now has 34 columns.
- Evidence file, end-date columns: ends after 2026 Q1 filled where a state document gives one (Massachusetts `zepbound_end_date` 7/3/2026; Rhode Island `wegovy_end_date`, `saxenda_end_date`, `zepbound_end_date` 10/1/2026; Wisconsin `wegovy_end_date`, `saxenda_end_date` 7/1/2026). A sentence naming the source was added to `evidence_citation` for the three states.
- Rhode Island end of 10/1/2026 moved from tier 2 (one managed care plan's notice) to tier 1: Rhode Island EOHHS memorandum to RI Medicaid Providers dated August 5, 2026, "GLP-1 State Budget Guidance", found by web search on 2026-11-17 and read at the state's address. It names Foundayo, Saxenda, Wegovy and Zepbound. Events file and product file updated; the Rhode Island Foundayo row now has status `ended` with an end date and no start date. The memorandum file was added to the collection later the same day (`RI/Documents/RI_EOHHS_GLP1_State_Budget_Guidance_memo_2026-08-05.pdf`; manifest 284 rows).
- Kansas: KMAP General Bulletin 23255 (October 2023) added to the collection (`KS/Documents/KS_KMAP_GeneralBulletin_23255_20231006.pdf`, from the state portal) and to the manifest (282 rows). Clue C011 marked `confirmed`. Kansas start dates were not changed; decision pending.
- `code/build_state_quarter_drug_panel.py`: a product row with an end date and no start date is now `unknown` before the end date (one case, Rhode Island Foundayo). Panel rebuilt, 2,040 rows.
- `code/make_summary_workbook.py`: `by_state` sheet now has the two status columns; new sheet `by_state_product` (the 89 product-spell rows); readme sheet corrected.
- Text: `docs/start_here.md`, `docs/data_dictionary.md`, `docs/coverage_dimensions_codebook.md`, `docs/what_is_tracked.md`, `docs/state_notes.md` and the deposit README no longer say that four states stopped; they give the states that ended and the dates and describe the new columns. the list of text edits is kept by the authors; data changes are in `outputs/data_changes_2026_11_17_log.csv`; the one-time script is kept by the authors.
- Kansas start dates (decided by KS, 2026-11-17). Neither Kansas bulletin is a start of coverage for Saxenda or Wegovy: SDUD shows Kansas Saxenda prescriptions from 2021 Q1 (421) and Wegovy from 2021 Q4 (148; none in 2021 Q3), above every never-covering state per 100,000 enrollees in each quarter through 2024 Q1, and the state's criteria revised July 19, 2023 name both. Product file: Saxenda start 2021-01-01 (start of the data window), Wegovy start 2021-10-01, new `start_basis` value `prescriptions_observed`; Zepbound stays 2024-04-01 with a note (222 prescriptions in 2024 Q1). Evidence file: `saxenda_start_date` 1/1/2021 and `wegovy_start_date` 10/1/2021 (were 4/1/2024); `w34949_adoption_quarter` is unchanged at 2024 Q2. Events file: two Kansas rows (32 rows in all), 2023-09-19 with new event type `expand` (bulletin 23255) and 2024-04-01 `criteria_revision` (bulletin 24071).
- Kansas criteria history extended back from 2024 Q2 to 2021 Q1: `data/covered_quarters.csv`, 12 new rows in `data/criteria_status_spans.csv` (152), two new rows in `data/state_criteria_history.csv` (29), `data/criteria_status_by_quarter.csv` rebuilt (972 rows). Shares in `docs/notes_on_the_rules.md` updated. New source file `KS/Documents/KS_Weight_Loss_Agents_PA_criteria_draft_2023-07-19.pdf` (manifest 283 rows). The one-time script is kept by the authors; log: `outputs/data_changes_2026_11_17_kansas_log.csv`. The same re-dating was applied to New Hampshire, Virginia, Rhode Island, Delaware and Wisconsin later the same day; see below.
- Utah (decided by KS, 2026-11-17): coded as ended, first day not covered 7/1/2026. The state PA form approves weight-loss authorizations no later than 6/30/2026 under a legislative pilot; that the pilot was not renewed is from secondary sources (tier 3), and no state notice is in hand. Product file, evidence file (`status_on_2026_11_16`, `weight_loss_coverage_end_date`, the three end-date columns) and a new event row (33 rows). Seven states now have status `ended` and none is `unknown`. Log: `outputs/data_changes_2026_11_17_utah_log.csv`.
- One-time scripts named in this file (`enter_*.py`, `add_structure_2026_11.py`, `apply_*.py`, `rebuild_manifest_2026_11_16.py`) and superseded working documents are kept by the authors and are not in the public repository.
- Deposit only: `DEFINITIONS.docx` now says the stringency class takes five values and defines `none` and `not_applicable`; the Pennsylvania step-therapy example was removed because Pennsylvania was reclassed to `fda_label` on 2026-11-16.
- `docs/comparison_with_other_trackers.md`: description brought up to the freeze date (33 events, product file and panel, 10 covering states on November 16, 2026) and a new section saying where this database agrees with and differs from KFF, Khanna et al., Klebanoff et al. and NBER Working Paper 34949.
- Five more states re-dated from the prescription record (decided by KS, 2026-11-17), by the same rule as Kansas plus one more ground: Wegovy had no adolescent approval until 12/23/2022, so its 2021 and 2022 prescriptions cannot be pediatric EPSDT use. Saxenda starts 1/1/2021 in Wisconsin, Delaware, Virginia, New Hampshire and Rhode Island; Wegovy starts 10/1/2021 (WI), 7/1/2021 (DE, VA) and 1/1/2022 (NH, RI); `start_basis` `prescriptions_observed`; counts in each row's notes. Evidence file start-date columns updated; `w34949_adoption_quarter` keeps the paper's quarters. Covered quarters for the rule history extended to 2021 Q1 in all five (202 covered state-quarters, 1,212 cells; 35 new span rows, 5 early-period history rows). New clues C014 (Virginia plan criteria of 12/6/2022 adapted from the DMAS PDL), C015 (Rhode Island Neighborhood Health Plan policy from 7/2018) and C016 (Khanna et al. date New Hampshire to 2021 Q3). Full grounds in `docs/criteria_history_log.md`; log in `outputs/data_changes_2026_11_17_fivestates_log.csv`; the one-time script is kept by the authors.
