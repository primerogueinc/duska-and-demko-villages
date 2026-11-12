#!/usr/bin/env python3
"""Build index.html from data/*.json and site/template.html.

Usage: python3 build.py
The page is static. Data is inlined so it opens from disk, from GitHub Pages,
or anywhere else without a server. Same pattern as the Duska and Demko repos.
"""
import datetime
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
NAMES = ["places", "jurisdictions", "holdings", "hypotheses", "crossnotes", "timeline",
         "batches", "requests", "sources", "role", "basemap", "decisions", "searches", "epidemics"]
SENNE, INACOVCE = "PL-P-001", "PL-P-002"


def km(a, b):
    """Great-circle distance in kilometres between two places."""
    la1, lo1, la2, lo2 = map(math.radians, (a["lat"], a["lon"], b["lat"], b["lon"]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(h))


def srcs(value):
    return value if isinstance(value, list) else [value]


def main():
    data = {n: json.loads((ROOT / "data" / f"{n}.json").read_text(encoding="utf-8")) for n in NAMES}
    data["built"] = datetime.date.today().isoformat()

    known = {s["id"] for s in data["sources"]} | {"training"}
    hyp = {h["id"] for h in data["hypotheses"]}
    ids = [p["id"] for p in data["places"]]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate place id")

    def check(where, value):
        for s in srcs(value):
            if s not in known:
                raise SystemExit(f"{where}: unknown source {s}")

    for p in data["places"]:
        for f in p["facts"]:
            check(p["id"], f["src"])
        for n in p["names"]:
            check(p["id"], n["src"])
    for c in data["jurisdictions"]["civil"]:
        check("civil " + c["from"], c["src"])
    for c in data["jurisdictions"]["church"]:
        for s in c["steps"]:
            check(c["rite"] + " " + s["when"], s["src"])
    for group in ("holdings", "hypotheses", "crossnotes", "timeline", "epidemics"):
        for x in data[group]:
            check(x.get("id", x.get("year")), x["src"])
    for b in data["batches"]:
        for hid in b["raised"] + b["resolved"]:
            if hid not in hyp:
                raise SystemExit(f"{b['id']} refers to unknown hypothesis {hid}")

    by = {p["id"]: p for p in data["places"]}
    a, b = by[SENNE], by[INACOVCE]
    data["home_km"] = round(km(a, b), 1)
    rows = []
    for p in data["places"]:
        if p["kind"] == "home":
            continue
        approx = p["coord"] == "approximate"
        da, db = km(a, p), km(b, p)
        if da > 200:  # far-off archives are in the gazetteer, not the distance table
            continue
        rnd = (lambda v: int(round(v))) if (approx or da >= 20) else (lambda v: round(v, 1))
        rows.append({"id": p["id"], "name": p["name"], "senne": rnd(da), "inacovce": rnd(db), "approx": approx, "_k": da})
    rows.sort(key=lambda r: r.pop("_k"))
    data["distances"] = rows

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    marker = "/*__DATA__*/{}"
    if marker not in template:
        raise SystemExit("template is missing the data marker")
    (ROOT / "index.html").write_text(template.replace(marker, payload), encoding="utf-8")
    print(f"index.html built: {len(data['places'])} places, {len(data['holdings'])} record sets, "
          f"{len(data['hypotheses'])} hypotheses, {len(data['crossnotes'])} notes, "
          f"Senné to Iňačovce {data['home_km']} km")


if __name__ == "__main__":
    main()
