# Notes on the rules

What the coded fields mean in the documents, and features too rarely stated to code as columns. Prepared November 15, 2026 from the criteria text in `data/state_coverage_evidence_sources.csv`; quotations are from that file's fields, which cite the state documents.

## Lifestyle and "diet trial" requirements differ in kind

The `step_therapy` field records these. They range from counselling to a supervised programme of fixed length:

- Counselling and a plan, no minimum duration: Mississippi requires counselling on diet and physical activity and a written obesity treatment plan; "no minimum diet-trial duration is set."
- A documented trial of fixed length: Delaware, "Documented failure of at least a three-month low-calorie diet trial and increased physical activity"; Kansas, at least 3 months of documented lifestyle modification; New Hampshire (before 2026), a 3-month low-calorie diet trial with stated calories (1,200 kcal/day for women, 1,600 for men).
- A supervised programme: Rhode Island, a weight-management programme with "monthly meetings for at least 6 months before drug therapy"; Utah, at least 6 months of a dietitian-prescribed reduced-calorie diet with exercise, and at renewal the patient must be "still followed by a registered dietician."
- A drug step in place of a diet step: Massachusetts (from 2025) requires a phentermine trial; Virginia (June 2023) a non-GLP-1 weight-loss drug; Pennsylvania's managed care form requires a diabetes diagnosis or antidiabetic use.

The documents say what must be documented. They do not say how strictly a state checks, so the same wording can bind differently in different states.

## First approval and renewal

"Renewal" means re-approval when the first authorization ends. The length of the first authorization is not a column in this release. Six states state it: Missouri (Wegovy, four weeks at a time), Delaware (3 months), Tennessee (3 months expected from 1/1/2026), New Hampshire (6 months, before 2026), Wisconsin (up to 183 days from 7/1/2026) and Mississippi (12 months under version V11). Michigan and Pennsylvania give an authorization length of 6 months without separating first from renewal. The other nine covering states do not state it. The usual renewal test is weight loss of 5 percent from baseline (4 percent for Saxenda in Delaware and New Hampshire).

## BMI is a rule for starting, not for staying

BMI thresholds apply at initiation. No state document in the collection requires BMI to be reported at set intervals during treatment. What happens to a patient who started at a high BMI and has reached a low one is stated by only four states:

- Continue while the loss is kept: North Carolina (adults who "lost 5% of pretreatment weight and maintains it"); Mississippi (adults who "achieved or maintained weight loss of 5 percent or more from baseline").
- Stop at a floor: Virginia (2024 Q3 form), "renewals no longer granted once the member reaches BMI below 25"; Wisconsin (from 7/1/2026), no renewal if BMI is below 18.5.
- Virginia's 2024 Q3 form also measures the 5 percent loss "compared with the most recent authorization," a test a patient at a stable weight cannot keep meeting.

The other covering states' documents are silent, or no renewal rule is documented (California, Kansas, Massachusetts, Minnesota, Rhode Island, South Carolina).

## Managed care

`ffs_mco_scope` records whom the coded rule binds. For 13 of the 17 covering states the record is a statewide list or criteria that apply to managed care plans as well as fee-for-service (California through a pharmacy carve-out; Kansas, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, North Carolina, South Carolina, Tennessee, Utah, Virginia, Wisconsin). In four states the coded rules come partly or wholly from a managed care plan's policy, and plans may apply their own criteria: Delaware (the state PDL criteria apply to fee-for-service members only), New Hampshire, Pennsylvania and Rhode Island. In those four the rules describe one plan and may not describe every enrollee.

## People with both Medicare and Medicaid

Not coded. Dual-eligible enrollees get drug coverage through Medicare Part D, which does not cover drugs for weight loss; a state Medicaid program that covers these drugs may pay for them for dual-eligible enrollees. One state document in the collection addresses this: Mississippi (V11) requires that Part D be exhausted, including an appeal, with the denial letter submitted.

## How each rule is dated, quarter by quarter

The evidence file holds one set of rules per state, from the most recent document coded. In November 2026 we compared, state by state, the earliest document in the collection with the coded one, for six rules: prior authorization, BMI, lifestyle or step requirement, renewal, quantity limit, and preferred product. `criteria_status_by_quarter.csv` gives one of six classes for each covered state-quarter and rule. Observed: a document dated in or before the quarter states the rule. Dated by a later document: a later document states the rule and gives the date it began or was last revised. For example, Michigan's Drug Utilization Review Board minutes of September 5, 2023 say that prior authorization applied "since MDHHS implemented coverage on February 1, 2022", so the 2022 quarters are documented by a 2023 document. Bracketed: the same rule is in a document before the quarter and a document after it. Carried back: only a later document states the rule. Absent by inference: the documents covering the quarter were read and state no such rule, and we assume there was none; this is an assumption, not a finding. No information: nothing in hand covers the quarter.

In the 13 states checked (202 covered state-quarters, 1,212 cells) the shares are: observed 50.8 percent, dated by a later document 5.0, bracketed 0.8, carried back 9.0, absent by inference 10.7, no information 23.6. Of the 687 observed, bracketed and later-dated cells, 97 (14 percent) rest on a document that was read but is not in the collection (tier 2). By rule, carried back is highest for renewal (20 percent), lifestyle or step (15 percent) and BMI (13 percent), and absent by inference is highest for quantity limit (32 percent). On 2026-11-17 six states (Kansas, Wisconsin, Delaware, Virginia, New Hampshire, Rhode Island) were extended back to 2021 Q1, because the prescription record shows they were paying for these drugs from the start of the window; most of their newly added quarters are classed no information, because the rule documents then in force are not in hand, and that is why the no-information share rose from 5 percent to 24 percent between the November 15 and November 17 versions. Covered quarters with at least one rule carried back, by state: Michigan 9/17, Wisconsin 5/22, Mississippi 12/12, California 0/12, Kansas 1/22, Pennsylvania 0/11, Delaware 0/22, New Hampshire 6/20, Virginia 6/22, Massachusetts 0/9, Missouri 0/7, Rhode Island 5/22, South Carolina 3/4; that is 47 of 202 covered state-quarters (23 percent); before the November 2026 document checks it was 111 of 181 (61 percent). Mississippi's 12 rest on criteria documents that could not be downloaded in November 2026; without Mississippi the count would be 35 of 202 (17 percent). Minnesota, North Carolina, Tennessee and Utah had none marked and were not re-read. `docs/criteria_history_log.md` records what was compared in each state and every Internet Archive search with its result, and `docs/documents_still_to_find.md` lists the documents that would resolve the remaining cells. If you hold a document that contradicts an assumption here, please let us know at simonkos@iu.edu with its URL or the file, and we will add it to the deposited collection.

