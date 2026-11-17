# Start here: a guide

## What this is

This is a state-by-state dataset of Medicaid coverage rules for GLP-1 medications used for weight loss (Wegovy, Saxenda, Zepbound, and newer products where a state lists them). Coverage dates and dated changes run from 2021 through November 16, 2026; prescription counts run from 2021 Q1 through 2026 Q1. A codebook and a data dictionary are included. Medicaid is run by each state, and most state programs do not pay for these drugs. Seventeen did at some point since 2021. Seven of the 17 had ended weight-loss coverage by November 16, 2026: California, New Hampshire, Pennsylvania and South Carolina on January 1, 2026, Utah on July 1, 2026, Massachusetts on July 3, 2026, and Rhode Island on October 1, 2026. Utah's coverage was a pilot whose authorizations ended no later than June 30, 2026; that the pilot was not renewed is from secondary sources, and no state notice is in hand.

What is provided:

- **Data files (CSV)**: one row per state, one row per dated change, and one row per state, quarter and drug for prescriptions.
- **A codebook and a data dictionary**: `docs/coverage_dimensions_codebook.md` gives the coding rules, and `docs/data_dictionary.md` defines every column of every file.
- **A Word document for each of the 50 states**: a text description of that state's dates and rules (or, for a state that never covered, of how that was checked), with charts of the state's prescriptions over time from the CMS State Drug Utilization Data (SDUD), so the written record can be compared with what was dispensed.
- **The state documents themselves (PDF)**: preferred drug lists, prior authorization criteria, bulletins and state plan amendments. These and the Word documents are deposited at Indiana University DataCORE (DOI to be added); `data/document_manifest.csv` lists every file.

## What is coded for each state

1. **Start and end dates of coverage, separately for each drug** (Wegovy, Saxenda, Zepbound, oral semaglutide, orforglipron).
2. **Prior authorization**: whether it is required, and a class for how strict it is (none; at the FDA label; stricter than the label).
3. **What a patient has to show**: the adult body mass index (BMI) threshold and the conditions that lower it (for example BMI 30, or 27 with hypertension, diabetes or sleep apnea); the adolescent threshold; the minimum age; and any lifestyle or step requirement, such as a documented three-month diet trial, six months in a supervised weight-management programme, or trying another drug first.
4. **Rules that apply after starting**: how long the first approval lasts, what is required to renew (usually 5 percent weight loss from baseline), and quantity limits.
5. **Which drug is preferred** where the state ranks them, and which uses are covered (weight loss, or only diabetes, cardiovascular or other labeled uses).
6. **Who the rule binds**: fee-for-service only, or managed care plans too.
7. **The date and citation of the document each rule comes from**, and for each dated change an evidence tier.

Some features are stated by so few states that they are not coded as columns and are described in `docs/notes_on_the_rules.md`, for example whether treatment continues once a patient reaches a low BMI.

## The four files

| File | One row is | Use it to |
|---|---|---|
| `data/state_coverage_evidence_sources.csv` | a state | see a state's dates and rules |
| `data/state_coverage_events.csv` | a dated change | see what changed and when |
| `data/state_drug_coverage.csv` | a state, a product and a spell of coverage | see dates, preferred status and quantity limit for each of five products |
| `outputs/state_quarter_product_counts.csv` | a state, a quarter and a drug | see prescriptions paid for |
| `data/document_manifest.csv` | a document | find the source PDF |

## How to use info here for your use case

Each of these files has info that might be useful. If what you find disagrees with what is written here, please let us know (email simonkos@iu.edu), or open an issue on the repository page.

- **A yes/no by state and quarter.** Use `data/state_quarter_drug_panel.csv`, or the spells in `data/state_drug_coverage.csv`. There are 17 states with `coverage_status` equal to `Covered`. `status_on_2026_11_16` says whether each still covered on the freeze date, and `weight_loss_coverage_end_date` gives the date for the seven that had ended (California, New Hampshire, Pennsylvania and South Carolina 1/1/2026; Utah 7/1/2026; Massachusetts 7/3/2026; Rhode Island 10/1/2026).
- **Timing of changes.** Use the events file. North Carolina, for example, ended on 2025-10-01 and was reinstated on 2025-12-12.
- **How strict a state is.** Compare the rule columns. Massachusetts and Mississippi both cover, with different BMI thresholds and different requirements before a first prescription.
- **One drug at a time.** Use `data/state_drug_coverage.csv`, or `data/state_quarter_drug_panel.csv` for a state-by-quarter-by-product panel, to see when a product was added, preferred or dropped.
- **What was dispensed.** Use the counts file. California Wegovy prescriptions were 269,170 in 2025 Q4 and 64,077 in 2026 Q1, the quarter after coverage ended.
- **The proof.** Take any row in the events file, read `evidence_file`, and open that document in the collection.

## How sure are we of each fact

Every dated change has an `evidence_tier`: 1 means a state document is in hand, 2 means a strong secondary source or a state document that was read but could not be saved, 3 means a claim not yet backed by a document. `docs/documents_to_obtain.md` lists the documents that could not be obtained and why.

The rule columns in `state_coverage_evidence_sources.csv` hold each state's rules from one document, the most recent one coded, and `criteria_as_of` gives its date. Rules for earlier quarters are in `state_criteria_history.csv` (one row per state and period), and `criteria_status_by_quarter.csv` says, for every covered state-quarter and each of six rules, what the rule rests on. In the 13 states checked document by document in November 2026, 63 percent of the 894 state-quarter-rule cells are observed (a document dated in or before the quarter states the rule), 12 percent are carried back (only a later document states the rule), 14 percent are absent by inference (the documents covering the quarter were read and state no such rule, so we assume there was none), and 5 percent have no information; the remaining 6 percent are documented by an earlier and a later document that agree, or by a later document that gives the date the rule began. Counted the earlier way, 47 of the 181 covered state-quarters (26 percent) have at least one rule carried back, down from 111 (61 percent); 12 of the 47 are in Mississippi, whose criteria documents could not be downloaded in November 2026. If you hold a document that contradicts one of these assumptions, please let us know at simonkos@iu.edu with its URL or the file, and we will add it to the deposited collection. See `docs/notes_on_the_rules.md`.

Nearly every state requires prior authorization, so the yes/no on that separates states very little; the differences are in the rules themselves.
