# State Medicaid coverage rules for GLP-1s (weight management)

Owner: Kosali Simon, Indiana University
Started: October 25, 2026

## Purpose
The living record of when each state Medicaid program added, changed, or ended coverage of GLP-1 medications for weight management (Wegovy, Saxenda, Zepbound), with a source for every date. Project code (the 2026 research letter, the Medicaid GLP-1 economics paper, the Truveta work) should read state dates from here so each change is entered once.

## Versions
- `frozen_nber_w34949/`: the evidence file and page cited in NBER Working Paper 34949, copied unchanged from Coady Wing's gist (revision 4495b2a7, March 18, 2026). Git tag `nber-w34949-gist-2026-03-18` marks this state of the repository.
- `data/state_coverage_evidence_sources.csv`: the working copy of that same file. It starts identical to the frozen copy; every correction is logged in `CHANGES.md`.
- `data/state_coverage_events.csv`: one row per dated change (adopt, restrict, end, reinstate, pilot_end) from late 2025 on, with source, evidence tier, and date checked.
- `legacy_2025_maddie_potter/`: the other 2025 tables built by Maddie Potter and Wei-Lun Lo (adoption months used in w34949 Table 2, PA and quantity-limit dates, PA stringency tiers at adoption). Not in the gist; copied from the medicaid_glp1_short_paper repository.

## Where the evidence documents are saved
Source documents (PDLs, PA criteria, bulletins, press items), by state, are not in this repository because of their size (about 201 MB). They are in Kosali Simon's IU OneDrive:

    MedicaidStateFormularyRulesGLP1s/State Document/<State>/

The `evidence_file` column stores paths relative to `MedicaidStateFormularyRulesGLP1s/`, never full paths. The documents are not public; contact Kosali Simon (simonkos@iu.edu) for access to specific sources.

## How to cite
Simon K. State Medicaid coverage rules for GLP-1 medications for weight management (version 2026-10-25). GitHub. https://github.com/simonkos-cell/state-medicaid-glp1-coverage-rules

Please also cite the paper these data were first built for: Wing C, et al. Medicaid Coverage for Obesity Medications: Utilization and Net-of-Rebate Spending. NBER Working Paper 34949. https://www.nber.org/papers/w34949

For the exact version used in that paper, cite the gist revision: https://gist.github.com/coadywing/14061c2322ad07fcd042d1aca7a65694/4495b2a7f88e8fa7450d5b2314055b87e3d8df48 (also tagged `nber-w34949-gist-2026-03-18` here).

Machine-readable citation details are in `CITATION.cff`.

## Acknowledgments
The 2025 coverage data and evidence files were built by Maddie Potter and Wei-Lun Lo for NBER Working Paper 34949, and the evidence page was first published by Coady Wing.

## Evidence standard
`evidence_tier` in `state_coverage_events.csv`:
- 1 = official state document (PDL, PA criteria, provider bulletin, budget or regulation, state Medicaid web page)
- 2 = KFF or another research tracker, or a Medicaid managed care plan notice
- 3 = news story or advocacy organization statement

Tier 2 or 3 is acceptable documentation, especially when two or more sources agree on the date. When a tier 1 document turns up later, update the row and keep the earlier source in `notes`.

## Making a change
1. Save the source document in the state's OneDrive folder.
2. Edit the row in `data/`, with the relative path in `evidence_file` and today's date in `date_checked`.
3. Add an entry to `CHANGES.md` (date, file, state, field, old value, new value, source).
4. Commit with a message naming the state and change.

## Freezing for a paper
When a paper is submitted, tag the repository (for example, `rl-2026-jno-submission`) and zip the State Document folder as it stands, for deposit with the replication files.
