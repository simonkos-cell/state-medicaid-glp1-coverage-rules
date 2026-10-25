# Change log

Every change to files in `data/` relative to the frozen NBER w34949 version, newest first.

| Date | File | State | Field | Old value | New value | Source | By |
|---|---|---|---|---|---|---|---|
| 2026-10-25 | state_coverage_events.csv | CA, NH, PA, SC, MI, MA, UT, RI, NC | (new file) | | 11 dated changes, late 2025 to October 2026 | See source columns in file | KS |

## Open issues to check (not yet changed)
- Zepbound start dates with a 2026 year in `state_coverage_evidence_sources.csv`: Michigan 11/24/2026, North Carolina 8/24/2026, New Hampshire 9/24/2026, Tennessee 8/25/2026 (Tennessee's Wegovy start also reads 8/25/2026). Likely typos for 2024 or 2025; check against the PDLs in OneDrive.
- New Hampshire Zepbound end date reads 1/26/2026; other withdrawing states read 1/1/2026.
- Delaware: `legacy_2025_maddie_potter/GLP1_Coverage_with_PA_QL_Date.csv` gives end dates of 3/1/2026, while the evidence file says "Continued coverage through Q1 2026" and 2026 trackers show Delaware covering. 3/1/2026 may be the end of data collection, not an end of coverage.
- Michigan's January 1, 2026 restriction and North Carolina's October 1 to December 12, 2025 gap are not in the evidence file (now in `state_coverage_events.csv`).
- Virginia: a service-authorization form dated July 31, 2025 (cited by a tracker) needs checking for any criteria change in 2025 Q3.
- Wisconsin: undated ForwardHealth notice asking prescribers not to start new PA requests during shortages; confirm it predates 2025.
- Utah pilot end (June 30, 2026) rests on one news source; find the Utah Medicaid notice.
