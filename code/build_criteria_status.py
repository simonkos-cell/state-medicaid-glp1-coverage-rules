#!/usr/bin/env python3
"""
Purpose : Expand hand-coded evidence spans into one row per covered
          state-quarter and rule field, check that every covered quarter
          is classed once and only once, and report the share in each class.
Inputs  : data/criteria_status_spans.csv   (hand-coded; one row per state,
                                            field and run of quarters)
          data/covered_quarters.csv        (state, first_quarter, last_quarter)
Outputs : data/criteria_status_by_quarter.csv
          printed shares, overall and by state
Date    : 2026-11-15
Author  : Kosali Simon
Assumes : Python 3.11 or later, standard library only.
Usage   : python code/build_criteria_status.py   (run from the repository root)
"""
import csv, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPANS = ROOT / "data" / "criteria_status_spans.csv"
COVERED = ROOT / "data" / "covered_quarters.csv"
OUT = ROOT / "data" / "criteria_status_by_quarter.csv"

FIELDS = ["pa_required", "bmi_rule", "lifestyle_or_step", "renewal_rule",
          "quantity_limit", "preferred_product"]
CLASSES = ["observed", "stated_retrospectively", "bracketed", "carried_back",
           "absent_by_inference", "no_information"]


def fail(msg):
    sys.exit(f"ERROR: {msg}")


def q_index(q):
    if len(q) != 6 or q[4] != "Q" or q[5] not in "1234" or not q[:4].isdigit():
        fail(f"bad quarter label: {q!r}")
    return int(q[:4]) * 4 + int(q[5]) - 1


def q_label(i):
    return f"{i // 4}Q{i % 4 + 1}"


def read(path):
    if not path.exists():
        fail(f"missing input {path.relative_to(ROOT)}")
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    print(f"read {path.relative_to(ROOT)}: {len(rows)} rows")
    return rows


covered = {}
for r in read(COVERED):
    a, b = q_index(r["first_quarter"]), q_index(r["last_quarter"])
    if b < a or r["state"] in covered:
        fail(f"covered_quarters.csv: bad or duplicate row for {r['state']}")
    covered[r["state"]] = (a, b)
print(f"states with covered quarters: {len(covered)}; "
      f"covered state-quarters: {sum(b - a + 1 for a, b in covered.values())}")

out, seen = [], {}
for n, r in enumerate(read(SPANS), start=2):
    st, fld, cls = r["state"], r["field"], r["class"]
    if st not in covered:
        fail(f"spans line {n}: state {st} not in covered_quarters.csv")
    if fld not in FIELDS:
        fail(f"spans line {n}: unknown field {fld!r}")
    if cls not in CLASSES:
        fail(f"spans line {n}: unknown class {cls!r}")
    if cls != "no_information" and not r["source_document"].strip():
        fail(f"spans line {n}: class {cls} needs a source_document")
    a, b = q_index(r["quarter_start"]), q_index(r["quarter_end"])
    if b < a:
        fail(f"spans line {n}: quarter_end before quarter_start")
    for i in range(a, b + 1):
        if not covered[st][0] <= i <= covered[st][1]:
            fail(f"spans line {n}: {st} {q_label(i)} is not a covered quarter")
        key = (st, fld, i)
        if key in seen:
            fail(f"spans line {n}: {st} {fld} {q_label(i)} already classed on line {seen[key]}")
        seen[key] = n
        out.append({"state": st, "quarter": q_label(i), "field": fld, "class": cls,
                    "rule": r["rule"], "source_document": r["source_document"],
                    "source_date": r["source_date"], "evidence_tier": r["evidence_tier"],
                    "notes": r["notes"]})
print(f"expanded to {len(out)} state-quarter-field rows")

states_done = sorted({r["state"] for r in out})
missing = [(st, f, q_label(i)) for st in states_done for f in FIELDS
           for i in range(covered[st][0], covered[st][1] + 1) if (st, f, i) not in seen]
if missing:
    fail(f"{len(missing)} covered state-quarter-field cells have no class, first: {missing[:5]}")
not_started = sorted(set(covered) - set(states_done))
print(f"states coded: {len(states_done)} ({', '.join(states_done)}); "
      f"not yet coded: {len(not_started)} ({', '.join(not_started) or 'none'})")

out.sort(key=lambda r: (r["state"], FIELDS.index(r["field"]), q_index(r["quarter"])))
with open(OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
print(f"wrote {OUT.relative_to(ROOT)}: {len(out)} rows")


def report(label, rows):
    c = Counter(r["class"] for r in rows)
    tot = sum(c.values())
    parts = [f"{k} {c[k]} ({100 * c[k] / tot:.1f}%)" for k in CLASSES if c[k]]
    print(f"{label}: n={tot}; " + "; ".join(parts))


print("\nShares over state-quarter-field cells, coded states only")
report("ALL", out)
for st in states_done:
    report(st, [r for r in out if r["state"] == st])
print("\nBy field, coded states only")
for fld in FIELDS:
    report(fld, [r for r in out if r["field"] == fld])

print("\nCovered quarters with at least one field carried back (comparable to the repository's earlier count)")
tot_q = tot_m = 0
for st in states_done:
    qs = {r["quarter"] for r in out if r["state"] == st}
    marked = {r["quarter"] for r in out if r["state"] == st and r["class"] == "carried_back"}
    noinfo = {r["quarter"] for r in out if r["state"] == st and r["class"] == "no_information"}
    tot_q += len(qs); tot_m += len(marked)
    print(f"{st}: {len(marked)} / {len(qs)} carried back on some field; {len(noinfo)} / {len(qs)} with no information on some field")
print(f"ALL coded states: {tot_m} / {tot_q} ({100 * tot_m / tot_q:.1f}%)")

print("\nObserved, bracketed and stated-retrospectively cells by evidence tier")
c = Counter(("1" if r["evidence_tier"].strip() == "1" else "2 or mixed")
            for r in out if r["class"] in ("observed", "bracketed", "stated_retrospectively"))
for k in sorted(c):
    print(f"tier {k}: {c[k]}")
