# Change log

Every change to files in `data/` relative to the frozen NBER w34949 version, newest first.

| Date | File | State | Field | Old value | New value | Source | By |
|---|---|---|---|---|---|---|---|
| 2026-10-25 | state_coverage_events.csv | MA | (new row; 2026-02-17 row expanded) | | Wegovy reinstated 2026-02-17 at parity with Zepbound; Saxenda pediatric only; adult BMI criteria (35+, or 30 to under 35 or 27+ with listed conditions) | MassHealth Pharmacy Facts 269 (Jan 14 2026): "Wegovy®(semaglutide) will be added as a preferred drug managed at parity with Zepbound®", "Effective February 17, 2026" | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MA | wegovy_end_date | Continued coverage through Q1 2026 | 1/1/2025 | MassHealth Prescriber e-Letter Vol. 14 Issue 3 (Oct 2024): Wegovy and Saxenda "will be noncovered agents for the treatment of overweight and obesity in adults" from January 1, 2025; matches the state's evidence note and the Wegovy pause date in GLP1_Coverage_with_PA_QL_Date.csv | KS |
| 2026-10-25 | state_coverage_events.csv | MA | (new rows) | | 2025-01-01 end of Wegovy and Saxenda for adult weight management; 2025-01-06 phentermine step for new starts | MassHealth e-Letter Oct 2024; Pharmacy Facts 235 (Nov 19 2024) | KS |
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
- Criteria documents to obtain so `pa_stringency` can move off not_documented: MI (MHP Common Formulary PDL PA criteria), NH (DHHS clinical PA criteria), NC (August 2024 weight management criteria), PA (statewide PDL clinical criteria), RI (FFS manual PA criteria), SC (November 2024 PDL and criteria), TN (Optum Rx TennCare criteria PDF), UT (weight loss GLP-1 PA form), DE (BMI threshold behind SPA DE-24-0010).
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
