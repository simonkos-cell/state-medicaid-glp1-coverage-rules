"""
Purpose : Build one Word summary document per state (50) for the DataCORE deposit from the
          repository data files, so the documents and the data cannot disagree.
Inputs  : data/state_coverage_evidence_sources.csv, data/state_coverage_events.csv,
          data/state_drug_coverage.csv, data/state_criteria_history.csv,
          data/document_manifest.csv, outputs/state_quarter_product_counts.csv,
          and the chart images <deposit>/files/<ST>/Documents/<ST>.png and <ST>100K.png
Outputs : <out_dir>/<ST>/<State name>.docx for the 50 states
Date    : 2026-11-16
Assumes : Python 3.10+, python-docx 1.2.0
Usage   : python code/build_state_documents.py <deposit folder> <out_dir>
          (out_dir may be <deposit folder>/files to write the documents in place)
"""
import csv, os, sys, collections
from docx import Document
from docx.shared import Pt, Emu

dep, out_dir = sys.argv[1], sys.argv[2]
FREEZE = "November 16, 2026"
AB = {'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ','New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC','South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY'}
def read(p):
    r = list(csv.DictReader(open(p, encoding="utf-8-sig", newline="")))
    print(f"{p}: {len(r)} rows read"); return r
ev = read("data/state_coverage_evidence_sources.csv")
events = read("data/state_coverage_events.csv")
spells = read("data/state_drug_coverage.csv")
hist = read("data/state_criteria_history.csv")
man = read("data/document_manifest.csv")
counts = read("outputs/state_quarter_product_counts.csv")
if len(ev) != 50: sys.exit("FAIL: expected 50 states in the evidence file")
PNAME = {"saxenda":"Saxenda (liraglutide)","wegovy_injection":"Wegovy injection (semaglutide)","wegovy_tablet":"Wegovy tablet (oral semaglutide)","zepbound":"Zepbound (tirzepatide)","foundayo":"Foundayo (orforglipron)"}
STATUS = {"covered":"covered","covered_restricted":"covered under criteria much narrower than the label","ended":"coverage ended","not_covered_for_weight_loss":"not covered for weight loss","not_named":"not named in any document in hand","unknown":"status after the last document is not known"}
SDUD_BUILD = ("The charts and counts run through 2026 Q1 and come from the CMS State Drug Utilization Data annual files (December 2025 updates for 2021 to 2024, July 2026 updates for 2025 and 2026), filtered to the public weight-loss GLP-1 NDC list, with rates per 100,000 using the CMS enrollment file, September 2026 release. The numbers are in state_quarter_product_counts.csv. The counts are by brand, so they include prescriptions for the other labeled uses of Wegovy and Zepbound.")

def P(doc, text, bold=False, size=None):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = bold
    if size: r.font.size = Pt(size)
    return p
def H(doc, text): P(doc, text, bold=True)
def new_doc(title):
    d = Document(); s = d.sections[0]
    s.page_width, s.page_height = Emu(7772400), Emu(10058400)
    s.left_margin = s.right_margin = Emu(1143000); s.top_margin = s.bottom_margin = Emu(914400)
    d.core_properties.author = "Kosali Simon"; d.core_properties.title = title
    P(d, title, bold=True, size=14); return d
def table(doc, header, rows):
    t = doc.add_table(rows=1, cols=len(header)); t.style = "Table Grid"
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; c.text = ""; rr = c.paragraphs[0].add_run(h); rr.bold = True; rr.font.size = Pt(9)
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""; rr = cells[i].paragraphs[0].add_run(v); rr.font.size = Pt(9)
    doc.add_paragraph()
def charts(doc, ab):
    for fn, cap in [(f"{ab}.png", f"Prescriptions in {ab} by quarter (raw counts), by product."),
                    (f"{ab}100K.png", f"Prescriptions per 100,000 Medicaid enrollees in {ab} by quarter, by product.")]:
        p = os.path.join(dep, "files", ab, "Documents", fn)
        if not os.path.exists(p): sys.exit(f"FAIL: missing chart {p}")
        doc.add_picture(p, width=Emu(5760720)); P(doc, cap)
def sdud_numbers(ab):
    rx = collections.defaultdict(float); rate = collections.defaultdict(float)
    for c in counts:
        if c["state"] == ab:
            rx[c["year_quarter"]] += float(c["number_rx"] or 0); rate[c["year_quarter"]] += float(c["number_rx_100K"] or 0)
    early = sum(v for k, v in rx.items() if k[:4] in ("2021","2022","2023","2024"))
    late = sum(v for k, v in rx.items() if k[:4] in ("2025","2026"))
    return early, late, rx.get("2026 Q1", 0.0), rate.get("2026 Q1", 0.0)
def sources_block(doc, ab, e):
    mine = [m for m in man if m["state"] == ab]
    docs_in = [m for m in mine if m["deposit"] == "yes" and m["file_type"] in ("PDF", "spreadsheet (xlsx)")]
    docs_out = [m for m in mine if m["deposit"] != "yes"]
    H(doc, "Source documents in this state's folder")
    if docs_in:
        table(doc, ["File", "Date on the document", "Where it was found"],
              [[m["file_path"].split("/")[-1], m["document_date_in_text"] or "not recorded",
                (m["source_url"] + (" (page that lists the file)" if m["source_url_kind"] == "listing_page" else " (Internet Archive capture)" if m["source_url_kind"] == "archive_capture" else " (page that restates the document)" if m["source_url_kind"] == "related_page" else " (address formed from the document number or file name; not opened)" if m["source_url_kind"] == "inferred" else "")) if m["source_url"] else "URL not recorded when the file was saved"] for m in docs_in])
    else:
        P(doc, "No source document is deposited for this state. The 2025 collection saved documents only for states where a drug list or notice needed to be kept; the checks made are described above.")
    if docs_out:
        H(doc, "Documents we read that are cited and not deposited")
        P(doc, "These documents are marked proprietary or confidential, or are under a vendor's or plan's copyright, so we do not redistribute them. A reader can obtain each one from the address given.")
        table(doc, ["Document", "Reason", "Where to obtain it"],
              [[m["file_path"].split("/")[-1], m["notes"].replace("Cited, not deposited: ", ""), m["source_url"] or "URL not recorded"] for m in docs_out])
    H(doc, "Evidence text from the data file")
    for part in [x.strip() for x in e["evidence_citation"].split("|") if x.strip()]: P(doc, part)
    if e.get("criteria_source", "").strip() and e["criteria_source"].strip() not in ("NA",):
        P(doc, "Source of the rules: " + e["criteria_source"])
    files = sorted(m["file_path"] for m in mine if m["deposit"] == "yes" and m["file_type"] != "RA notes (docx)")
    H(doc, "Files in this state's folder")
    P(doc, "; ".join(files + [f"{ab}/{[k for k,v in AB.items() if v==ab][0]}.docx"]))

n_cov = n_nev = 0
for e in ev:
    name, ab = e["state"], AB[e["state"]]
    title = f"Medicaid GLP-1 Coverage for Weight Loss: {name}"
    d = new_doc(title)
    P(d, f"Data frozen {FREEZE}. Coverage here means Medicaid coverage for weight loss in adults.")
    sp = [s for s in spells if s["state"] == ab]
    evs = sorted([x for x in events if x["state"] == ab], key=lambda x: x["effective_date"])
    if e["coverage_status"] == "Covered":
        n_cov += 1
        if not sp: sys.exit(f"FAIL: no product rows for {ab}")
        H(d, "Status")
        cur = [PNAME[s["product"]] for s in sp if s["status_on_2026_11_16"] in ("covered", "covered_restricted")]
        P(d, (f"{name} Medicaid has covered GLP-1 medications for weight loss. As of the documents in hand, products covered: " + "; ".join(dict.fromkeys(cur)) + ".") if cur else
             f"{name} Medicaid covered GLP-1 medications for weight loss and, as of the documents in hand, no longer covers any of them for that use (see the table and the dated changes below).")
        H(d, "Coverage by product")
        table(d, ["Product", "Start", "End", "Status", "How the start date is known", "Preferred status", "Quantity limit"],
              [[PNAME[s["product"]] + (f" (spell {s['spell']})" if s["spell"] != "1" or any(t["product"] == s["product"] and t["spell"] == "2" for t in sp) else ""),
                s["start_date"] or "", s["end_date"] or ("" if not s["start_date"] else "none documented"), STATUS[s["status_on_2026_11_16"]],
                s["start_basis"].replace("_", " "), s["preferred_status"], s["quantity_limit"]] for s in sp])
        notes = [f"{PNAME[s['product']]}: {s['notes']}" for s in sp if s["notes"]]
        for n in dict.fromkeys(notes): P(d, n)
        P(d, "Start-date terms: 'stated in document' means a state document gives the date; 'first listing' means the date of the earliest document in hand that lists the product, so coverage may have begun earlier; 'bounded' means the product is absent from one dated document and present in a later one; 'evidence file' means the date recorded since the version used in NBER Working Paper 34949; 'not supported' means no document in hand supports the recorded date; 'prescriptions observed' means no dated document gives a start and the date is the first quarter with prescriptions in the CMS State Drug Utilization Data, or the start of the data window.")
        H(d, "Dated changes")
        if evs:
            for x in evs: P(d, f"{x['effective_date']} ({x['event_type'].replace('_',' ')}; {x['drugs']}): {x['description']} [Source: {x['source_citation']}; evidence tier {x['evidence_tier']}]")
        else: P(d, "None recorded.")
        H(d, "Rules in the most recent document coded")
        P(d, f"Date of that document: {e['criteria_as_of']}")
        for lab, k in [("Prior authorization required", "prior_authorization"), ("Strictness compared with the FDA label", "pa_stringency"), ("Reason for that class", "pa_stringency_note"),
                       ("Adult BMI rule", "bmi_adult_criteria"), ("Adolescent BMI rule", "bmi_adolescent_criteria"), ("Minimum age", "age_minimum"),
                       ("Lifestyle or step requirement", "step_therapy"), ("Renewal rule", "renewal_criteria"), ("Quantity limits", "quantity_limits"),
                       ("Quantity limit detail", "quantity_limit_detail"), ("Preferred and non-preferred placement", "preferred_status"), ("Uses covered", "indication_scope"),
                       ("Fee-for-service and managed care scope", "ffs_mco_scope")]:
            if e[k].strip(): P(d, f"{lab}: {e[k].replace('_', ' ') if k == 'pa_stringency' else e[k]}")
        hh = [h for h in hist if h["state"] == ab]
        H(d, "Rules by period")
        if hh:
            table(d, ["Period", "Prior authorization", "BMI rule", "Lifestyle or step", "Renewal", "Source"],
                  [[f"{h['period_start']} to {h['period_end'] or 'latest document'}", h["pa_required"], h["bmi_rule"], h["lifestyle_or_step"], h["renewal_rule"], h["source_document"]] for h in hh])
            P(d, "For each quarter and rule, criteria_status_by_quarter.csv in the public repository says whether the rule is stated in a document of that date or carried back from a later one.")
        else:
            P(d, "This state is not yet in the period-by-period history file; the rules above are from one document.")
        H(d, "SDUD profile")
        P(d, SDUD_BUILD); charts(d, ab)
    else:
        n_nev += 1
        H(d, "Status")
        P(d, f"Not covered for weight loss. We found no document showing that {name} Medicaid covered Wegovy, Saxenda or Zepbound for weight loss between 2021 and the date the state was last checked (sources below).")
        H(d, "How this was checked")
        P(d, e["evidence_citation"].split("|")[0].strip())
        H(d, "SDUD profile")
        early, late, rx_q1, rate_q1 = sdud_numbers(ab)
        P(d, f"SDUD records {early:,.0f} prescriptions for the three brands in {name} Medicaid from 2021 through 2024, and {late:,.0f} from 2025 Q1 through 2026 Q1 ({rx_q1:,.0f} in 2026 Q1, or {rate_q1:,.1f} per 100,000 enrollees). " +
             ("Prescriptions in a state with no weight-loss coverage are expected where the state pays for Wegovy or Zepbound for another labeled use (for example cardiovascular risk reduction or sleep apnea); SDUD cannot separate the uses, and we have not collected each state's criteria for those uses. " if late > 0 else "") + SDUD_BUILD)
        charts(d, ab)
    sources_block(d, ab, e)
    os.makedirs(os.path.join(out_dir, ab), exist_ok=True)
    d.save(os.path.join(out_dir, ab, f"{name}.docx"))
print(f"documents written: {n_cov} covering states, {n_nev} never-covering states, to {out_dir}")
if (n_cov, n_nev) != (17, 33): sys.exit("FAIL: expected 17 and 33")
