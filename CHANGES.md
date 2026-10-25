# Change log

Every change to files in `data/` relative to the frozen NBER w34949 version, newest first.

| Date | File | State | Field | Old value | New value | Source | By |
|---|---|---|---|---|---|---|---|
| 2026-10-25 | state_coverage_events.csv | MA | (new row; 2026-02-17 row expanded) | | Wegovy reinstated 2026-02-17 at parity with Zepbound; Saxenda pediatric only; adult BMI criteria (35+, or 30 to under 35 or 27+ with listed conditions) | MassHealth Pharmacy Facts 269 (Jan 14 2026): "Wegovy®(semaglutide) will be added as a preferred drug managed at parity with Zepbound®", "Effective February 17, 2026" | KS |
| 2026-10-25 | state_coverage_evidence_sources.csv | MA | wegovy_end_date | Continued coverage through Q1 2026 | 1/1/2025 | MassHealth Prescriber e-Letter Vol. 14 Issue 3 (Oct 2024): Wegovy and Saxenda "will be noncovered agents for the treatment of overweight and obesity in adults" from January 1, 2025; matches the state's evidence note and the Wegovy pause date in GLP1_Coverage_with_PA_QL_Date.csv | KS |
| 2026-10-25 | state_coverage_events.csv | MA | (new rows) | | 2025-01-01 end of Wegovy and Saxenda for adult weight management; 2025-01-06 phentermine step for new starts | MassHealth e-Letter Oct 2024; Pharmacy Facts 235 (Nov 19 2024) | KS |
| 2026-10-25 | state_coverage_events.csv | CA, NH, PA, SC, MI, MA, UT, RI, NC | (new file) | | 11 dated changes, late 2025 to October 2026 | See source columns in file | KS |

## Open issues to check (not yet changed)
- Zepbound start dates with a 2026 year in `state_coverage_evidence_sources.csv`: Michigan 11/24/2026, North Carolina 8/24/2026, New Hampshire 9/24/2026, Tennessee 8/25/2026 (Tennessee's Wegovy start also reads 8/25/2026). Likely typos for 2024 or 2025; check against the PDLs in OneDrive.
- New Hampshire Zepbound end date reads 1/26/2026; other withdrawing states read 1/1/2026.
- Delaware: `legacy_2025_maddie_potter/GLP1_Coverage_with_PA_QL_Date.csv` gives end dates of 3/1/2026, while the evidence file says "Continued coverage through Q1 2026" and 2026 trackers show Delaware covering. 3/1/2026 may be the end of data collection, not an end of coverage.
- Michigan's January 1, 2026 restriction and North Carolina's October 1 to December 12, 2025 gap are not in the evidence file (now in `state_coverage_events.csv`).
- Virginia: a service-authorization form dated July 31, 2025 (cited by a tracker) needs checking for any criteria change in 2025 Q3.
- Wisconsin: undated ForwardHealth notice asking prescribers not to start new PA requests during shortages; confirm it predates 2025.
- Utah pilot end (June 30, 2026) rests on one news source; find the Utah Medicaid notice.
