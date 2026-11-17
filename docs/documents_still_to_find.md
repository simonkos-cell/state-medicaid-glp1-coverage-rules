# Documents still to find: search list for the criteria history

> Update, 2026-11-16: the Internet Archive index lists captures of several documents described below as unavailable, including earlier Mississippi criteria versions and earlier Rhode Island plan policies. See `docs/wayback_capture_inventory_2026-11-16.md`. The captures have not yet been downloaded or read.

Prepared 2026-11-15 from the document-by-document check; updated 2026-11-15 with the tier 2 list and search terms.

Two tables. Table A lists documents that would turn a carried-back quarter into an observed one. Table B lists documents that are already the basis for a coded rule but were read without a copy being saved (`evidence_tier` 2 in `data/criteria_status_by_quarter.csv`); finding these does not change any rule, it moves the cell to tier 1.

On the Internet Archive, type the prefix into the search box, open the URLs tab, and use the filter word; the `web.archive.org/web/*/...` link form returned nothing in two tests on 2026-11-15. Record every search in `docs/criteria_history_log.md`, including those that find nothing, with the date, the prefix, and the result. URLs below are copied from the repository files or from a search result; except where noted, none was opened from this list.

As of 2026-11-15: 47 of 181 covered state-quarters have at least one rule carried back from a later document, and 12 of the 47 are Mississippi. 150 of 849 classed cells are at tier 2.

## Table A. Would resolve a carried-back quarter

| State | Document wanted | Where to look | Search terms | Cells it would resolve |
|---|---|---|---|---|
| MS | Criteria PDFs v1.3, V5 (1/1/2025), V7 (10/30/2025), V11 (7/1/2026) | v1.3: `https://medicaid.ms.gov/wp-content/uploads/2023/04/Anti-obesity-Select-Agents-PA-Criteria-V1.3.pdf` (site down 2026-11-15); others: URLs in `criteria_source`; archive prefix `medicaid.ms.gov/wp-content/uploads/`, filter "obesity" | `Anti-obesity Select Agents PA Criteria`; `site:medicaid.ms.gov obesity criteria` | lifestyle, renewal for 2023Q3 to 2025Q3 (18); makes BMI tier 1 |
| MS | Universal PDL editions between 05/30/2025 and 10/1/2026 | Same prefix, filter "PDL" | `Mississippi Medicaid Universal Preferred Drug List` | quantity limit 2025Q3 to 2026Q2 (4) |
| MI | Earlier revisions of the PA form | The 243-URL list for `michigan.magellanrx.com/`, filter "PAfaxform"; also any `MIRx_PDL.pdf` and `MIRx_quantity_limits.pdf` there (filter "PDL", "quantity") | `MIRx PA fax form anti-obesity`; `michigan.magellanrx.com PAfaxform` | BMI, lifestyle, renewal 2022Q2 to 2024Q2 (27); quantity limit before 2024Q4 (10) |
| NH | Criteria approved 06/29/2023 and 01/26/2023 | `nh.smartrx-dev.lh.primetherapeutics.com/documents/51139/51621/Weight Management Criteria/92ab6b86-192f-15fc-d639-265810a5972d` (blocked 2026-11-15; retry), or earlier archive captures of the nh.primetherapeutics.com criteria URL | `New Hampshire Medicaid Weight Management Criteria`; `nh.primetherapeutics.com weight management` | BMI, lifestyle, renewal 2022Q4 to 2024Q1 (18) |
| VA | DMAS weight-loss service authorization form, captures from 2023 and early 2024; PDL editions after 08/09/2024 | The DMAS form URL used for the 7/28/2024 and 9/1/2024 captures noted in `CHANGES.md`; DMAS bulletin "Upcoming Changes to Service Authorization Criteria for Weight-Loss Drugs" (6/23/2023) is at `https://vamedicaid.dmas.virginia.gov/vamed/download-pdf-bulletin/19612` | `DMAS weight loss drugs service authorization criteria`; `vamedicaid.dmas.virginia.gov weight-loss` | BMI, renewal 2023Q1 to 2024Q2 (12); step 2023Q1 to 2024Q3 (7) |
| RI | Earlier versions of the Neighborhood Health Plan policy | Prefix `nhpri.org/wp-content/uploads/`, filter "Weight_Loss". Searched 2026-11-15 and not found: nhpri.org posts CMP-014 Weight Management (last reviewed 05/22/2018, behavioral not drug) and a pharmacy Benefit Exclusion policy, neither of which is the Weight Loss Management policy reviewed 5/15/2024. May be behind the provider portal; ask the plan | `Neighborhood Health Plan Rhode Island Weight Loss Management policy`; `nhpri.org pharmacy policy weight loss` | four fields 2023Q1 to 2024Q1 (20) |
| WI | The renewal weight-loss test in force before July 2024: an Update earlier than 2023-09, or an archived copy of Online Handbook topic #7837 | forwardhealth.wi.gov Updates for 2021 and 2022; archive of the Online Handbook topic. Email to Wisconsin Medicaid sent 2026-11-15, awaiting reply | `ForwardHealth Update anti-obesity prior authorization`; `forwardhealth.wi.gov topic 7837` | renewal 2023Q2 to 2024Q2 (5); also the true start of coverage |
| SC | Single PDL editions effective between 11/1/2024 and 12/1/2025; P&T minutes of November 5, 2025 | SCDHHS pharmacy page and its archive captures | `South Carolina Medicaid Single Preferred Drug List`; `SCDHHS P&T committee minutes 2025` | preferred 2025Q1 to 2025Q3 (3); 20 cells of no information |
| MO | Final SmartPA criteria with an implementation date; PDL edition in force October 2024 to January 2025 | dss.mo.gov pharmacy pages and their archive captures | `Missouri Medicaid SmartPA anti-obesity criteria`; `MO HealthNet preferred drug list 2024` | 2024Q4 (6 cells) and the 10/1/2024 start date |
| DE | Fee-for-service clinical criteria for the class | DMAP Pharmacy Corner | `Delaware Medicaid DMAP pharmacy prior authorization criteria obesity` | none carried back; 01.23 plan version obtained 2026-11-15 |
| MA | Pharmacy Facts 235 and 269 (to save in the folder) | mass.gov | `MassHealth Pharmacy Facts 235`; `MassHealth Pharmacy Facts 269` | none carried back; makes 2026 cells checkable |
| CA | Contract Drugs List of January 2026 | Medi-Cal Rx | `Medi-Cal Rx Contract Drugs List January 2026` | none carried back; the end event is tier 3 |

## Table B. Already coded, read but not saved (tier 2)

Ordered by the number of cells each would move to tier 1.

| Cells | State | Document | Where to look | Search terms |
|---|---|---|---|---|
| 56 | RI | Neighborhood Health Plan of RI, Weight Loss Management policy, reviewed 5/15/2024 | See the RI row in Table A; not found by search on 2026-11-15 | `Neighborhood Health Plan Rhode Island Weight Loss Management policy 2024` |
| 27 | MS | Anti-obesity Select Agents PA Criteria V7, 10/30/2025 | medicaid.ms.gov (down 2026-11-15) | `Anti-obesity Select Agents PA Criteria V7` |
| 21 | VA | Molina Healthcare of Virginia form VA-ALL-PF-17859-24, revised 8/21/2024, effective 9/30/2024 | Molina Healthcare of Virginia provider Forms page, "Weight Loss Management" service authorization form. A molinahealthcare.com media link returned 404 on 2026-11-15. Note also VA-ALL-PF-17860-24, a separate GLP-1 service authorization form created 8/21/2024, effective 9/3/2024 | `VA-ALL-PF-17859-24`; `Molina Virginia weight loss management service authorization form`; `VA-ALL-PF-17860-24` |
| 14 | VA | Molina Healthcare of Virginia form VA-ALL-PF-16714-24, revised 6/1/2024, effective 7/1/2024 | Same Forms page; an earlier form in the series, VA-ALL-PF-15482-24 (revised 11/27/2023, effective 1/1/2024), also exists and would cover earlier quarters | `VA-ALL-PF-16714-24`; `VA-ALL-PF-15482-24` |
| 12 | MI | MIRx 1.1.2026 anti-obesity GLP-1 criteria, and MDHHS Letter L 25-73 | URLs: https://content.govdelivery.com/attachments/MIDHHS/2025/12/08/file_attachments/3486243/Numbered Letter L 25-73-Pharmacy-Final.pdf and https://mi.primetherapeutics.com/provider/external/medicaid/mi/doc/en-us/MIRx_Miscellaneous_Anti-Obesity_Agents_NonPreferred_GLP1s.pdf; the `mi.primetherapeutics.com/provider/external/medicaid/mi/doc/en-us/` path worked for `MIRx_PDL.pdf` on 2026-11-15, so the criteria file is likely on the same path under another name | `MIRx anti-obesity GLP-1 criteria 2026`; `MDHHS Letter L 25-73` |
| 11 | MS | Select Covered Obesity Medications PA Criteria v1.3, effective 7/1/2023 | See the MS row in Table A | `Select Covered Obesity Medications PA Criteria v1.3` |
| 4 | DE | Delaware First Health policy DE.PMN.50, effective 09.25 | Delaware First Health provider site; the 01.23 version is in the folder | `DE.PMN.50 anti-obesity medications`; `Delaware First Health anti-obesity policy 2025` |
| 4 | SC | SC Single PDL effective 12/1/2025 | See the SC row in Table A | `South Carolina Medicaid Single PDL December 2025` |
| 1 | KS | KDHE Anti-Obesity Medications criteria, version revised 1/17/2024 | Archive captures of `https://www.kdhe.ks.gov/DocumentCenter/View/407/Anti-Obesity-Medications-PDF` from February to August 2024. The August 2026 draft obtained 2026-11-15 lists 1/17/2024 among its revision dates but does not give that version's text | `KDHE anti-obesity medications prior authorization criteria`; `kdhe.ks.gov DocumentCenter 407` |

## Obtained 2026-11-15, after this list was first written

- KS: KMAP General Bulletin 24071 (April 17, 2024), which states that PA is required for Saxenda and Wegovy effective April 1, 2024 and that Zepbound is PDL preferred from the same date. Moves the Kansas `pa_required` and `preferred_product` cells to tier 1.
- KS: KDHE Anti-Obesity Medications approved draft PA criteria, last reviewed August 19, 2026. Useful for the revision-date list and for the current rules; does not settle the January 2024 version.
