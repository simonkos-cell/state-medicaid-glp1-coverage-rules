# Documents: what we obtained, and what remains a gap

> Update, 2026-11-16: the Internet Archive index lists captures of several documents described below as unavailable, including earlier Mississippi criteria versions and earlier Rhode Island plan policies. See `docs/wayback_capture_inventory_2026-11-16.md`. The captures have not yet been downloaded or read.

Last updated 2026-11-15. This is the final document status for the deposited version of
the collection. Section 1 records items that were open on 2026-11-11 and have since been
obtained. Section 2 lists what remains unobtained, what each would settle, and why the
attempt failed. Nothing in section 2 changes a coverage date or a coverage status in
`data/state_coverage_evidence_sources.csv`; each is either confirmation of a fact already
established from another document, or detail on a dimension recorded as unknown.

## 1. Obtained since 2026-11-11

1. **New Hampshire weight-management criteria in force before 1/1/2026.** Obtained from a
   Wayback capture dated 2024-10-04 of the Magellan Rx fee-for-service criteria document.
   Recorded in the evidence file with `criteria_as_of` 6/10/2024: BMI 30, or 27 with a
   very-high-risk factor, or waist circumference above 102 cm (men) and 88 cm (women), or
   two other risk factors; 5% renewal threshold (4% for Saxenda); pediatric 1%.

2. **South Carolina criteria for Wegovy and Saxenda.** Obtained from the SCDHHS
   prescription benefits document, with the Select Health notice as corroboration of the
   1/1/2026 removal. Recorded with `criteria_as_of` 11/5/2025: no published BMI threshold,
   prior authorization plus dietary counseling and a physical activity attestation, Wegovy
   preferred and Saxenda non-preferred.

3. **Utah 2026-06-30 scheduled end.** Upgraded to tier 1 from the state prior
   authorization form, which states that coverage may not continue past 6/30/2026.

4. **Delaware and Pennsylvania state plan amendments.** SPA DE-26-0003 and SPA PA-26-0003,
   both tier 1.

## 2. Remaining gaps

### Affects a recorded dimension, not a date or status

1. **Delaware's list of agents covered for weight loss, at the 1/1/2026 vintage.**
   Partly closed on 2026-11-15. The list SPA DE-26-0003 points at is the Obesity Treatment
   Agents class of the Delaware Medicaid PDL, and the edition effective 11/2/2026 is now in
   the collection (DE_PDL_2026-11-02.pdf). It gives the molecules and the preferred split,
   which are recorded in the evidence file. What remains open is the edition in force on
   1/1/2026, since the state publishes the PDL at a single "latest version" download link
   and earlier editions are reachable only through archive captures. That vintage would date
   the addition of orforglipron (Foundayo) and of the Wegovy tablet, which the current
   edition lists without a start date. Also open: the fee-for-service prior authorization
   form for the class, which is where the BMI criteria live; the PDL itself carries none.

2. **Mississippi anti-obesity criteria: the PDF of V11, and the V5 edition (1/1/2025).**
   Closed as unobtainable on 2026-11-15. The current edition, V11 effective 7/1/2026, was
   located and its content entered, and the Universal PDL effective 10/1/2026 is in hand as a
   PDF supplying the quantity limits and the preferred split. The V11 PDF itself could not be
   saved: medicaid.ms.gov returned a vendor error to the browser all day, and the Internet
   Archive holds no capture of the file, of the provider-education notice, or of any
   anti-obesity document under that path. The V11 content was therefore entered from two
   agreeing automated reads of the live state URL, every cell it fills says so, and the
   V7-to-V11 event stays at tier 2. V5 (1/1/2025), which with V7 would settle clues C003 and
   C004 on what changed on 10/30/2025, is unobtainable for the same reason. The file-naming
   pattern is recorded for a later attempt:
   `/wp-content/uploads/<YYYY>/<MM>/Anti-obesity-Select-Agents-PA-Criteria-<date>-to-Current.V<n>.pdf`.

3. **The SCDHHS Single Preferred Drug List dated 12/1/2025.**
   Partly closed on 2026-11-15. The edition effective 11/1/2026 is now in the collection and
   stands in place of the 10/1/2026 edition: it has no anti-obesity class at all, and its
   only GLP-1 class holds diabetes products. Bulletin MB# 24-016 of 5/8/2024 is also in hand
   and establishes that the single PDL binds managed care members. What remains open is the
   12/1/2025 edition, the last one with a weight management class, which would document the
   preferred split in the final month of coverage. The lists are published by the pharmacy
   contractor at southcarolina.fhsc.com, not on scdhhs.gov, which is why earlier searches of
   the agency site returned nothing, and that site carries no archive of prior editions.
   Note that a PDL alone cannot establish coverage or its absence: the document states that
   it "should not be used for verification of coverage".

### Confirmation of facts already established

4. **Pennsylvania DHS, "Prior Authorization of Obesity Treatment Agents - Pharmacy
   Services", issued 11/24/2025.** The 1/1/2026 exclusion is already tier 1 from SPA
   PA-26-0003, with an MCO form effective 1/1/2026 as corroboration. Why not obtained: the
   DHS bulletin search needs a session, and the direct URLs found were from 2023.

5. **TennCare Criteria PDL effective 1/1/2026.** The 12/01/2025 notice already states the
   three-month approval change.

6. **Virginia DMAS memo issuing the service authorization form effective 9/30/2024.** Would
   move the Virginia 2024 restrict event from tier 2 to tier 1. The event is established
   from dated copies of the form itself.

7. **Jefferson Health Plans obesity treatment agents policy effective 1/1/2026.** Duplicate
   evidence for Pennsylvania. Not on the fetch allowlist.

8. **North Carolina reinstatement notice of 12/12/2025.** Closed 2026-11-15: the bulletin
   (dated 12/19/2025) is in the deposit at NC/Documents/NC_reinstatement_bulletin_2025-12-19.pdf
   and the event row points at it.

## States with no document folder

North Dakota and Texas have no folder in the original 2025 document collection and none was
ever created; the archive holds 48 state folders. Both are never-covering states, and their
verification rests on the evidence file rows (PDL checks and the KFF cross-check) and on the
SDUD charts, which were added to the deposit for both states in November 2026.

## How documents were handed over

A saved PDF attached in a chat session, read directly from the file. A direct URL to a
document also worked. For pages requiring a session, a PDF print was used. Where only an
archived copy existed, the Wayback capture date is recorded in the source field.
