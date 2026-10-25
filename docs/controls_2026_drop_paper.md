# Choosing the comparison group for the 2026 coverage-drop paper

Date: 2026-10-25. Written from this repository's audited coverage file and from the group logic in the short-paper code (`code/analysis/09_calculate_numbers.r`, `temp_data/analysis_groups.csv`).

## The design and what a clean control has to be

Treatment is a drop: California, New Hampshire, Pennsylvania and South Carolina ended Medicaid coverage of weight-loss GLP-1s on January 1, 2026. The outcome is SDUD weight-loss GLP-1 prescribing, with a 2025 pre-period and 2026 Q1 as the first post quarter. A clean control must satisfy two conditions at once:

1. It was covering weight-loss GLP-1s throughout the 2025 pre-period (so it has a non-trivial level to compare against, and parallel pre-trends are meaningful); and
2. It did not drop or materially restrict coverage on or near January 1, 2026 (so the post quarter is not itself a partial treatment).

The second condition is the one the current code does not fully enforce.

## What the current code does

`withdraw_states <- c("CA","PA","SC","NH")` names the treated group by hand. The comparison group is then "any state covering by 2024 Q1 that is not a withdrawing state", which yields:

**Comparison group as coded: DE, MA, MI, MN, MS, RI, VA, WI.**

The never-covering group is the 33 states with no adoption date. States adopting after 2024 Q1 (KS, MO, NC, SC, TN, UT) are dropped as "late".

## Problems with that comparison group, given this repository's audit

Three of the eight comparison states changed their own coverage inside the window and are not clean controls:

- **Massachusetts.** Dropped Wegovy and Saxenda for adults on January 1, 2025. It was therefore not covering those agents for adults during the 2025 pre-period, and it restricted again February 17, 2026 and ended July 3, 2026. Massachusetts is partly a treated unit sitting in the control group; it violates condition 1 and condition 2. Remove it, or at most keep it only in a Zepbound-specific analysis for the period Zepbound remained covered.
- **Michigan.** Imposed a severe restriction on January 1, 2026 (BMI 40 or higher, framed as averting bariatric surgery), the same quarter as the treatment. A state changing policy in the post quarter is not a clean control. Remove it, or treat it as a second, differently-dated treated unit.
- **Rhode Island.** Ended coverage October 1, 2026. This is after 2026 Q1, so Rhode Island is a valid control for a Q1 2026 post-period, but it is a future dropper; keep it in the main group and test dropping it.

The code's own `outputs/tables/coverage_end_diagnostic.csv` already lists MA (2025-08-01), MI (2026-02-01) and RI (2026-01-13) as having end dates inside the panel, but the group logic excludes only the four named withdrawal states, not these.

## Kansas is wrongly excluded

Kansas is dropped from the comparison group because its coded adoption quarter is 2024 Q2, one quarter after the 2024 Q1 cutoff. But the SDUD check (`docs/sdud_quarterly_check_2026-10.md`) shows Kansas was paying for Saxenda from 2019 Q1 (about 573 prescriptions per quarter) and Wegovy from 2021 Q4; it was covering a weight-loss GLP-1 throughout the 2025 pre-period and did not drop in 2026. Kansas satisfies both control conditions and should be in the comparison group. Its exclusion is a date artifact of the 2024 Q1 cutoff applied to a start date that marks Zepbound's listing, not the start of coverage.

## Recommended comparison group

Clean controls (covering through 2025, no drop or restriction through 2026 Q1): **DE, KS, MN, MS, VA, WI.**

- Add Kansas (override the "late" exclusion; it was covering since well before 2025).
- Remove Massachusetts (adult drop in 2025) and Michigan (restriction in 2026 Q1) from the main comparison group.
- Keep Rhode Island in the main group; report a version without it.
- Keep the 33 never-covering states as the second comparison group, as in w34949.

Three of the six clean controls (KS, VA, WI) are the early-Saxenda, high-baseline states from the w34949 work. For a drop design this is acceptable because the identifying variation is the within-state change at 2026 Q1, which differences out the level; but any levels comparison should note that these three have inflated baselines from years of Saxenda.

## Things to think hard about beyond the group

1. **Pre-period window.** Define the pre-period as 2025 Q3 to Q4, which is stable for all six clean controls, rather than "2025" broadly, which pulls in Massachusetts's January 2025 adult drop. The code already uses 2025 Q3 as the base quarter and reports 2025 Q4 separately, which is the right instinct.
2. **South Carolina as a treated unit.** South Carolina only began covering in November 2024 and at low volume, so its drop removes about a year of thin coverage. California, New Hampshire and Pennsylvania are the strong treated states; report the estimate with and without South Carolina.
3. **Suppression.** The fewer-than-11 suppression bites harder on a single-quarter comparison than on w34949's pooled panel. Delaware and Mississippi are small; Kansas, Virginia, Wisconsin and Minnesota are larger and safer. Report how many treated and control state-quarters are suppressed in 2026 Q1 and test the 0-versus-10 imputation as w34949 did.
4. **First-posting data.** 2026 Q1 SDUD is a first posting and will revise; FFS and MCO reporting lag differently by state. Plan the November 2026 Q2 refresh as a robustness check, and note the risk that a control state's Q1 2026 level is understated by late MCO reporting, which would bias the drop estimate.
5. **Molecule mix.** The four treated states differ in what they covered (SC never covered Zepbound; CA, NH, PA covered all three). A weight-loss-GLP-1 total is the headline; a Wegovy-plus-Zepbound version avoids leaning on Saxenda and matches the w34949 robustness discussion.

This note changes nothing in `data/`; it reads the audited coverage file and the short-paper group logic and recommends overriding `comparison_override` and `exclude_states` in `09_calculate_numbers.r` accordingly.

## Reproduced numbers with the recommended controls (cross-check, not the final model)

Computed from `temp_data/analysis_panel.csv` (reaches 2026 Q1), pooled and enrollment-weighted, obesity-labeled GLP-1 prescriptions per 100 enrollee-months, base quarter 2025 Q3. This is an arithmetic reproduction of the base/post comparison, not the full state-and-quarter fixed-effects model with permutation inference, which should be run in the pipeline.

Pooled: withdrawing states 1.42 (2025 Q3) to 0.30 (2026 Q1); clean controls 0.83 to 0.81. DiD = -1.11 per 100 enrollee-months (withdraw change -1.12, control change -0.01).

State by state (second-panel exhibit; full table in `outputs/tables/exhibit2_state_by_state_newcontrols.csv`):

| State | Group | 2025 Q3 | 2025 Q4 | 2026 Q1 | Change Q3 to Q1 | % change | Suppressed Q1 |
|---|---|---|---|---|---|---|---|
| CA | withdraw | 1.51 | 1.49 | 0.38 | -1.13 | -75% | 6 |
| PA | withdraw | 1.49 | 1.58 | 0.07 | -1.42 | -95% | 11 |
| NH | withdraw | 1.08 | 1.12 | 0.13 | -0.95 | -88% | 6 |
| SC | withdraw | 0.13 | 0.12 | 0.05 | -0.08 | -64% | 11 |
| DE | control | 1.21 | 1.37 | 0.78 | -0.43 | -35% | 15 |
| KS | control | 0.89 | 0.95 | 0.61 | -0.28 | -32% | 3 |
| MN | control | 0.94 | 0.97 | 0.78 | -0.17 | -18% | 6 |
| MS | control | 0.57 | 0.65 | 0.68 | +0.12 | +21% | 14 |
| VA | control | 0.27 | 0.25 | 0.23 | -0.04 | -15% | 16 |
| WI | control | 1.53 | 1.61 | 1.83 | +0.30 | +19% | 0 |

Two things to watch: (1) Delaware and Kansas controls fell 32 to 35 percent, more than Minnesota or Virginia; they did not change policy, so this is likely first-posting or MCO reporting lag in 2026 Q1, to confirm in the November Q2 refresh. (2) South Carolina's 2025 level was only 0.13 and its 2026 Q1 has 11 suppressed cells, so it contributes little; report with and without it.
