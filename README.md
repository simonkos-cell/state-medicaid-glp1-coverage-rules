# State Medicaid coverage rules for GLP-1s (weight management)

Owner: Kosali Simon, Indiana University
Started: October 25, 2026. This version: November 17, 2026 (data frozen November 16, 2026).

## Purpose
An updatable record of when each state Medicaid program added, changed, or ended coverage of GLP-1 medications for weight management (Wegovy, Saxenda, Zepbound), with sources.

## Versions
- `frozen_nber_w34949/`: the evidence file and page cited in NBER Working Paper 34949, copied unchanged from Coady Wing's gist (revision 4495b2a7, March 18, 2026). Git tag `nber-w34949-gist-2026-03-18` marks this state of the repository.
- `data/state_coverage_evidence_sources.csv`: the working copy of that same file. It starts identical to the frozen copy; every correction is logged in `CHANGES.md`.
- `data/state_coverage_events.csv`: one row per dated change (end, restrict, reinstate, scheduled_end, plan_amendment, criteria_revision), with source, evidence tier, and date checked.
- `data/state_drug_coverage.csv`: coverage by product and spell for five products (Saxenda, Wegovy injection, Wegovy tablet, Zepbound, Foundayo), with how each start date is known. `data/state_quarter_drug_panel.csv` is the same information by state, quarter and product. `docs/what_is_tracked.md` says what is tracked at which level.
- `legacy_2025_maddie_potter/`: the other 2025 tables built by Maddie Potter and Wei-Lun Lo (adoption months used in w34949 Table 2, PA and quantity-limit dates, PA stringency tiers at adoption). Not in the gist; copied from the medicaid_glp1_short_paper repository.

## Where the evidence documents are saved
Source documents (PDLs, PA criteria, bulletins, state plan amendments), by state, are not in this repository. They are deposited at Indiana University DataCORE with the per-state summary documents and dispensing charts (DOI to be added on publication); `data/document_manifest.csv` lists every file. The `evidence_file` column stores paths relative to the deposit's `files/` folder. A new reader should start with `docs/start_here.md`; every column is defined in `docs/data_dictionary.md`, and `docs/notes_on_the_rules.md` describes what the rules mean in the documents.

## How to cite
If you use these data, please cite:

Wing C, et al. Medicaid Coverage for Obesity Medications: Utilization and Net-of-Rebate Spending. NBER Working Paper 34949. https://www.nber.org/papers/w34949

To identify the version of the data you used, add the repository and its date: Simon K. State Medicaid coverage rules for GLP-1 medications for weight management (version 2026-11-16). GitHub. https://github.com/simonkos-cell/state-medicaid-glp1-coverage-rules

For the exact values used in that paper, cite the gist revision: https://gist.github.com/coadywing/14061c2322ad07fcd042d1aca7a65694/4495b2a7f88e8fa7450d5b2314055b87e3d8df48 (also tagged `nber-w34949-gist-2026-03-18` here).

Machine-readable citation details are in `CITATION.cff`.

## Acknowledgments
Thank you to Maddie Potter and Wei-Lun Lo for assistance with an earlier version of the coverage data and evidence files for NBER Working Paper 34949. The evidence page was first published by Coady Wing.

## Evidence standard
`evidence_tier` in `state_coverage_events.csv`:
- 1 = official state document (PDL, PA criteria, provider bulletin, budget or regulation, state Medicaid web page)
- 2 = KFF or another research tracker, or a Medicaid managed care plan notice
- 3 = news story or advocacy organization statement

Tier 2 or 3 is acceptable documentation, especially when two or more sources agree on the date. When a tier 1 document turns up later, update the row and keep the earlier source in `notes`.

## Making a change
1. Save the source document in the state's folder of the document collection and add a row to `data/document_manifest.csv` with its web address.
2. Edit the row in `data/`, with the relative path in `evidence_file` and today's date in `date_checked`.
3. Add an entry to `CHANGES.md` (date, file, state, field, old value, new value, source).
4. Commit with a message naming the state and change.

## Freezing for a paper
When a paper is submitted, tag the repository (for example, `rl-2026-submission`) and record the version of the DataCORE deposit it used.

## Coverage dimensions (added October 2026)

Beyond the drug start and end dates, the evidence file now contains prior-authorization stringency relative to the FDA label, adult and adolescent BMI criteria, step therapy, age minimum, quantity limits, FFS versus managed-care scope, and the date and source of the criteria document, plus three reconciliation columns (the Klebanoff et al. June 2024 stringency class used by Khanna, Wang and Venkataramani 2026, their start quarter, and the adoption quarter used in NBER w34949). Field definitions and coding rules: `docs/coverage_dimensions_codebook.md`. Per-state oddities and the points where we and Khanna et al. read the record differently: `docs/state_notes.md`. The October 2026 corrections are listed in `CHANGES.md`.

A summary workbook, `outputs/state_coverage_summary.xlsx`, is generated from the CSV files by `code/make_summary_workbook.py` (sheets: by_state, by_state_molecule, events, dimensions). Edit the CSVs and rerun the script; do not edit the workbook.

## Document collection

The primary documents behind this record (state preferred drug lists, prior authorization criteria, bulletins, state plan amendments), the per-state summary documents and the dispensing charts are deposited at Indiana University DataCORE (DOI to be added on publication). This repository holds the machine-readable files, the codebook and the code. Documents published by pharmacy benefit contractors under their own copyright are cited here and in the deposit, not redistributed.
