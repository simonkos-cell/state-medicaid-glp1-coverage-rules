"""
Purpose : Expand data/state_drug_coverage.csv (one row per state, product and spell of
          coverage) into a state by quarter by product panel for the 17 covering states.
Inputs  : data/state_drug_coverage.csv
Outputs : data/state_quarter_drug_panel.csv, one row per state, quarter (2021Q1 to the
          quarter of the freeze date) and product, with:
            covered_any   1 if a spell of weight-loss coverage overlaps the quarter
            covered_full  1 if a spell covers every day of the quarter
            basis         documented | after_last_document | not_named | unknown
          Coverage here means coverage for weight loss in adults. A product approved only
          for another use in a state (for example Wegovy for cardiovascular risk) is 0.
Date    : 2026-11-16; revised 2026-11-17 (rows with an end date and no start date)
Assumes : Python 3.10+, standard library only.
Usage   : python code/build_state_quarter_drug_panel.py   (from the repository root)
"""
import csv, sys
from datetime import date

FREEZE = date(2026, 11, 16)
PRODUCTS = ["saxenda", "wegovy_injection", "wegovy_tablet", "zepbound", "foundayo"]
sp = list(csv.DictReader(open("data/state_drug_coverage.csv", encoding="utf-8")))
print(f"spell rows read: {len(sp)}")
states = sorted({r["state"] for r in sp})
if len(states) != 17:
    sys.exit(f"FAIL: expected 17 states, found {len(states)}")

def d(s):
    y, m, dd = map(int, s.split("-")); return date(y, m, dd)

def quarters():
    y, q = 2021, 1
    while True:
        start = date(y, 3*q-2, 1)
        if start > FREEZE: break
        end = date(y + (q == 4), (3*q) % 12 + 1, 1)   # first day of the next quarter
        yield f"{y}Q{q}", start, end
        y, q = (y, q+1) if q < 4 else (y+1, 1)

out = []
for st in states:
    for p in PRODUCTS:
        rows = [r for r in sp if r["state"] == st and r["product"] == p]
        if not rows:
            sys.exit(f"FAIL: no row for {st} {p}")
        last_doc = d(rows[0]["last_document_date"])
        status = rows[-1]["status_on_2026_11_16"]
        spells = [(d(r["start_date"]), d(r["end_date"]) if r["end_date"] else None) for r in rows if r["start_date"]]
        for q, qs, qe in quarters():
            any_, full = 0, 0
            for s, e in spells:
                e_eff = e if e else date(9999, 1, 1)      # e is the first day not covered
                if s < qe and e_eff > qs: any_ = 1
                if s <= qs and e_eff >= qe: full = 1
            if not spells:
                # a row with an end date and no start date: an end is documented, the start is not
                ends = [d(r["end_date"]) for r in rows if r["end_date"]]
                if status == "not_named": basis = "not_named"
                elif ends and qs < max(ends): basis = "unknown"
                else: basis = "documented"
            elif any(e is None for _, e in spells) and qs > last_doc:
                basis = "unknown" if status == "unknown" else "after_last_document"
            else:
                basis = "documented"
            out.append(dict(state=st, quarter=q, product=p, covered_any=any_, covered_full=full, basis=basis))

with open("data/state_quarter_drug_panel.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
nq = len(list(quarters()))
print(f"panel rows written: {len(out)} = {len(states)} states x {nq} quarters x {len(PRODUCTS)} products")
if len(out) != len(states) * nq * len(PRODUCTS):
    sys.exit("FAIL: panel is not balanced")
from collections import Counter
print("basis:", dict(Counter(r["basis"] for r in out)))
print("covered_any = 1:", sum(r["covered_any"] for r in out), " covered_full = 1:", sum(r["covered_full"] for r in out))
