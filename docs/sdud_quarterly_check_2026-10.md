# Quarterly SDUD check for the four lower-bound states, October 2026

Question: for the four states where the coverage dates in this repository looked like lower bounds (New Hampshire, Minnesota, Kansas, Virginia), does the SDUD show weight-loss GLP-1 claims paid well before the documented adoption quarter, and if so does that make the state an always-covered unit rather than an adopter within the 2019 to 2024 panel?

Data: the quarterly state-by-product panel shipped with the w34949 estimation code (`temp_data/SDUD_raw_panel.csv` in Coady Wing's repository), covering 2019 Q1 to 2024 Q3, restricted here to Saxenda, Wegovy and Zepbound. The quarterly counts are in `outputs/tables/sdud_quarterly_4states_check.csv`. These are filled-claim counts; suppressed cells (fewer than 11) are absent, so small early volumes are understated, not overstated.

## What the series show

| State | File adoption quarter | First Saxenda fill | First Wegovy fill | Mean Saxenda rx/quarter before adoption | Reading |
|---|---|---|---|---|---|
| New Hampshire | 2022 Q3 | 2020 Q1 | 2022 Q1 | 46 (14 quarters, 2020 to 2022) | Saxenda paid from 2020 Q1, two and a half years before the PDL class was added. Wegovy appears 2022 Q1, the quarter it was first marketed, and jumps at 2023 Q1. |
| Minnesota | 2021 Q4 (SPA) | 2021 Q4 | 2021 Q4 | 0 (no pre-period fills) | Nothing before 2021 Q4, then both drugs appear together in 2021 Q4, the SPA-approval quarter. This is a true adoption, and it lands in the quarter our corrected date says. |
| Kansas | 2024 Q2 | 2019 Q1 | 2021 Q4 | 573 (21 quarters, 2019 to 2024) | Saxenda paid every quarter from the start of the panel, hundreds per quarter; Wegovy from 2021 Q4 and a sharp jump at 2023 Q1. The 2024 Q2 "adoption" is only when Zepbound became preferred. |
| Virginia | 2023 Q1 | 2019 Q1 | 2021 Q3 | 424 (16 quarters, 2019 to 2022) | Saxenda paid every quarter from 2019, hundreds per quarter; Wegovy from 2021 Q3 and a sharp jump at 2023 Q1. |

## Conclusion

Three distinct patterns, not one:

1. **Minnesota is a clean adopter.** No weight-loss GLP-1 fills before 2021 Q4, then coverage begins at the SPA-approval quarter. The corrected date (December 2021) and the data agree. Minnesota should stay a treated unit, dated 2021 Q4.

2. **Kansas and Virginia were covering Saxenda throughout the panel.** Both paid 400 to 600 Saxenda prescriptions per quarter from 2019 Q1, before Wegovy or Zepbound existed. Under a treatment definition of "covers any weight-loss GLP-1" these two are always-covered within 2019 to 2024, not 2023 or 2024 adopters, and they cannot serve as clean treated units for a staggered-adoption design keyed to that definition. This is exactly why Khanna et al. excluded Kansas (and is consistent with their excluding Delaware and Wisconsin). What does change at a datable quarter in these states is the arrival of Wegovy (2021 Q3 to Q4) and the large take-up at 2023 Q1; a design keyed to Wegovy-or-Zepbound coverage, not Saxenda, would treat the 2023 jump as the event.

3. **New Hampshire is in between.** Saxenda from 2020 Q1 but at a low level (mean 46 per quarter, a tenth of Kansas or Virginia), with the real take-up in Wegovy from 2023. New Hampshire covered Saxenda before the panel's midpoint but at a volume small enough that the 2022 Q3 PDL listing and the 2023 Wegovy surge are the economically meaningful events.

## Implication for w34949

The absorbing, any-weight-loss-GLP-1 treatment definition currently assigns Kansas (2024 Q2) and Virginia (2023 Q1) a single adoption quarter, but both were paying for Saxenda across the whole panel, so their "pre-period" is not a no-coverage period. Two defensible fixes, for Coady to choose:

- Recode the treatment as coverage of Wegovy or Zepbound (the newer, higher-efficacy agents), which gives Kansas and Virginia a real 2021 to 2023 event and keeps them as treated units; or
- Treat Kansas and Virginia (and likely Delaware and Wisconsin) as always-covered and move them out of the adopter cohort, as Khanna et al. did.

Minnesota is unaffected either way. New Hampshire is a judgment call that the two definitions would treat differently; the Wegovy-based definition dates it to 2023, the any-GLP-1 definition to 2020.

This note uses only the panel that the estimation already reads, so it can be reproduced from the existing pipeline. It does not change any file in `data/`.

## Postscript: the treatment definition in the code, and all 14 adopters

Checked in Coady Wing's repository: `code/build/01_make_ndc_lookup.r` line 33 sets `obesity_brands <- c("WEGOVY", "SAXENDA", "ZEPBOUND", "LIRAGLUTIDE-WM")`, so Saxenda (branded and generic) counts as a weight-loss GLP-1 for both the outcome and, via `14_clean_coverage.r`, the adoption timing. The question is therefore not whether Saxenda "should" count (the code says it does) but whether the coverage dates match the Saxenda claims the code is already counting.

Pre-adoption Saxenda volume for all 14 adopters (mean filled prescriptions per quarter in quarters before the coded adoption quarter; suppressed cells omitted, so these understate):

| State | Coded adoption | First Saxenda fill | Saxenda before adoption | First Wegovy fill | Reading |
|---|---|---|---|---|---|
| Minnesota | 2021 Q4 | 2021 Q4 | none | 2021 Q4 | clean adopter |
| Massachusetts | 2024 Q1 | 2024 Q1 | none | 2024 Q1 | clean adopter |
| Michigan | 2022 Q1 | 2021 Q3 | 21 over 2q | 2022 Q1 | negligible pre-period; adoption date fine |
| Pennsylvania | 2023 Q1 | 2021 Q2 | 27 over 7q | 2022 Q1 | small pre-period; adoption date fine |
| Mississippi | 2023 Q3 | 2022 Q4 | 29 over 3q | 2022 Q4 | small pre-period; adoption date fine |
| North Carolina | 2024 Q3 | 2021 Q3 | 13 over 7q | 2024 Q2 | negligible; adoption date fine |
| South Carolina | 2024 Q4 | 2019 Q4 | 16 over 6q | 2024 Q2 | negligible; adoption date fine |
| New Hampshire | 2022 Q3 | 2020 Q1 | 65 over 10q | 2022 Q1 | modest pre-period; borderline |
| Delaware | 2023 Q1 | 2019 Q1 | 165 over 16q | 2021 Q3 | material pre-period |
| Virginia | 2023 Q1 | 2019 Q1 | 424 over 16q | 2021 Q3 | large pre-period |
| Kansas | 2024 Q2 | 2019 Q1 | 573 over 21q | 2021 Q4 | large pre-period |
| Wisconsin | 2023 Q2 | 2019 Q1 | 1148 over 17q | 2021 Q4 | large pre-period |
| California | 2023 Q1 | 2019 Q1 | 2645 over 16q | 2021 Q3 | very large pre-period |

Two groups emerge. MN, MA, MI, PA, MS, NC, SC have no or negligible Saxenda before their coded adoption quarter, so their dates are fine. CA, WI, KS, VA, DE (and NH to a lesser degree) were paying for Saxenda in volume for years before the coded date, so by the code's own four-brand definition they were covering a weight-loss GLP-1 across the panel and their coded adoption quarter marks a later event (the arrival of Wegovy or Zepbound), not the start of coverage.

California is the sharp case: it is a treated state in the published analysis with 2,645 Saxenda prescriptions per quarter from 2019, and the code dates its adoption to 2023 Q1. Khanna et al. excluded Kansas, Delaware and Wisconsin for this reason but kept California, and noted that California drove their opposite-signed state-level result. The same pre-period coverage is present in the w34949 data.

This does not resolve which definition is right; it shows the choice is consequential and names the five states (CA, WI, KS, VA, DE, plus NH as borderline) where the any-Saxenda and the Wegovy-or-Zepbound definitions disagree on the adoption quarter. The decision belongs with the estimation; this note surfaces it from the data the estimation already uses.

## What Khanna et al. did with these choices (checked in their supplement)

Their eTable 1 and eTable 5 show they confronted the same issue:

- **Early-Saxenda states: excluded.** Delaware ("data showing significant prescriptions prior to this date"), Kansas ("coverage of obesity-labeled GLP-1 RA at the start of the study period") and Wisconsin ("unclear coverage start date and potential for significantly restricted coverage") are dropped. This matches the pattern we found and is option (b) above.
- **California: kept, with a documented reason.** Their eTable 1 note says California's 2022 Saxenda and Wegovy claims arose because prior authorizations were suspended during the 2022 Medi-Cal Rx pharmacy-benefit-manager transition, with coverage formally starting January 2023. On that reading the large pre-2023 California volume is a transition artifact, not standing policy coverage, which is why they kept California as a 2023 Q1 adopter. This distinguishes California from Kansas, Virginia and Wisconsin and should be carried into w34949 rather than treating California's pre-period like theirs.
- **Saxenda-excluded robustness: already run.** Their eTable 5b excludes liraglutide formulations (Saxenda and Victoza). The obesity-labeled ATT moves only from 6.48 to 6.22 per 1,000 and the total-GLP-1 ATT strengthens from 4.17 to 4.85 (and becomes significant, p=0.01). Dropping the weakly effective agent does not overturn their result.
- **Balanced-panel robustness (eTable 5d)** uses Minnesota, Virginia, New Hampshire and Michigan as the long-follow-up treated states; the obesity-labeled effect holds (5.93).

### Revised implication for w34949

The issue is not that the four-brand definition is wrong, but that w34949 keeps Kansas, Virginia, Wisconsin and Delaware as treated adopters where Khanna et al. excluded them, and the SDUD confirms those four were paying for Saxenda across the panel. The clean responses, both of which Khanna et al. demonstrate leave the result standing, are: (1) add a Saxenda-excluded (or Wegovy-or-Zepbound-only) robustness specification; and (2) report the estimate dropping KS, VA, WI, DE from the treated cohort. California can stay in both papers for the PBM-transition reason documented above. Minnesota is a clean adopter under any choice.
