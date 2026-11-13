#!/usr/bin/env python3
"""One satellite image per place on the map, at village level.

  python tools/place_imagery.py [--only PL-P-001,PL-P-002] [--redo]
  python tools/place_imagery.py --engine rwi --rwi /path/to/roger-wilco-imaging-pre-alpha

Two engines.

  own   (default) This file's own reader: the newest clear Sentinel-2 scene of the last growing season, cut to a box round
        the place and stretched for the eye. It runs no code from any other repo.
  rwi   Roger Wilco Imagery's baseline picker, imported from a read-only checkout of that repo and called unchanged. Its
        output folder is pointed at a staging folder, so nothing is written to the checkout. Images made this way are
        credited "Roger Wilco Imagery".

Source for both: Copernicus Sentinel-2 L2A, read from the Element 84 Earth Search catalogue and the open Sentinel COG
bucket on AWS. Terms: Copernicus Sentinel data legal notice (free, full and open; reproduction, distribution and
adaptation allowed). The credit "Contains modified Copernicus Sentinel data <year>" is printed on each image and stored
beside it in data/imagery.json.

Image centres are settlement points from OpenStreetMap's geocoder, (c) OpenStreetMap contributors, ODbL 1.0, kept in
tools/place_centres.json: asked once, at one request a second, and not asked again.

Limits kept: 10 or 20 metres to the pixel, one image per place, no marker, nothing at the level of a house or a parcel.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "imagery"
INDEX = ROOT / "data" / "imagery.json"
CENTRES = ROOT / "tools" / "place_centres.json"
EARTH_SEARCH = "https://earth-search.aws.element84.com/v1"
WIDE = {"PL-P-023", "PL-P-024", "PL-P-030", "PL-P-031", "PL-P-032", "PL-P-033", "PL-P-034", "PL-P-040", "PL-P-041", "PL-P-042",
        "PL-P-043"}   # towns and cities: 8 x 6 km at 20 m. Everything else: 4 x 3 km at 10 m.
LICENCE = "Copernicus Sentinel data legal notice: free, full and open; reproduction, distribution and adaptation allowed."
LICENCE_URL = "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice"
NOT_CLEAR = (0, 1, 3, 8, 9, 10, 11)   # scene classes: no data, defective, shadow, cloud, cloud, cirrus, snow


def box(lat, lon, w_km, h_km):
    dlat = (h_km / 2) / 111.32
    dlon = (w_km / 2) / (111.32 * math.cos(math.radians(lat)))
    return [round(lon - dlon, 5), round(lat - dlat, 5), round(lon + dlon, 5), round(lat + dlat, 5)]


def caption(im: Image.Image, dst: Path, text: str):
    w, h = im.size
    strip = 13
    out = Image.new("RGB", (w, h + strip), (20, 20, 20))
    out.paste(im.convert("RGB"), (0, 0))
    ImageDraw.Draw(out).text((4, h + 1), text, fill=(235, 235, 235), font=ImageFont.load_default())
    out.save(dst, quality=80, optimize=True, progressive=True)
    return out.size


# ------------------------------------------------------------------ own engine
def own_window(src, bbox, res):
    from rasterio.warp import transform_bounds
    from rasterio.windows import from_bounds
    left, bottom, right, top = transform_bounds("EPSG:4326", src.crs, *bbox, densify_pts=21)
    shape = (max(1, round((top - bottom) / res)), max(1, round((right - left) / res)))
    return from_bounds(left, bottom, right, top, transform=src.transform), shape


def own_read(href, bbox, res, nearest=False):
    import rasterio
    from rasterio.enums import Resampling
    with rasterio.open(href) as src:
        win, shape = own_window(src, bbox, res)
        return src.read(1, window=win, out_shape=shape, boundless=True, fill_value=0,
                        resampling=Resampling.nearest if nearest else Resampling.bilinear)


def own_pick(client, bbox, res):
    """Newest scene whose box is whole and clear: last growing season first, then any date in the last year."""
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    year = now.year if now.month >= 6 else now.year - 1
    spans = [(dt.datetime(year, 5, 15, tzinfo=dt.timezone.utc), min(now, dt.datetime(year, 9, 30, tzinfo=dt.timezone.utc))),
             (now - dt.timedelta(days=365), now)]
    tried = 0
    for start, end in spans:
        items = list(client.search(collections=["sentinel-2-l2a"], bbox=bbox, datetime=f"{start.isoformat()}/{end.isoformat()}",
                                   query={"eo:cloud_cover": {"lt": 30}},
                                   sortby=[{"field": "properties.datetime", "direction": "desc"}], max_items=60).items())
        for it in items:
            if tried >= 25:
                return None, tried
            tried += 1
            try:
                scl = own_read(it.assets["scl"].href, bbox, res, nearest=True)
            except Exception:  # noqa: BLE001  one unreadable scene never stops a place
                continue
            if (scl == 0).mean() > 0.01 or np.isin(scl, NOT_CLEAR).mean() > 0.02:
                continue
            bands = [own_read(it.assets[k].href, bbox, res).astype("float32") for k in ("red", "green", "blue")]
            p = it.properties
            shifted = (not p.get("earthsearch:boa_offset_applied")) and float(str(p.get("s2:processing_baseline", "0")) or 0) >= 4.0
            rgb = (np.dstack(bands) - (1000.0 if shifted else 0.0)) / 10000.0
            return dict(item=it, rgb=rgb, clear=float(1 - np.isin(scl, NOT_CLEAR).mean())), tried
    return None, tried


def own_look(rgb):
    """One stretch for all three bands, set on brightness, so colours keep their balance. Gamma lifts the fields."""
    lum = rgb.mean(axis=2)
    lo, p95, hi = np.percentile(lum, [1, 95, 99.5])
    hi = max(min(hi, p95 * 1.5), lo + 0.02)   # a few white roofs must not darken the whole picture
    x = np.clip((rgb - lo * 0.9) / (hi * 1.05 - lo * 0.9), 0, 1) ** (1 / 1.6)
    return Image.fromarray((x * 255).astype("uint8"))


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--engine", choices=["own", "rwi"], default="own")
    ap.add_argument("--rwi", help="read-only checkout of the Roger Wilco imaging repo (engine rwi)")
    ap.add_argument("--only", help="comma-separated place ids")
    ap.add_argument("--redo", action="store_true", help="make again the images already listed")
    ap.add_argument("--stage", default="/tmp/place-imagery-stage")
    a = ap.parse_args()

    from pystac_client import Client
    client = Client.open(EARTH_SEARCH)
    if a.engine == "rwi":
        rwi = Path(a.rwi).resolve()
        sys.path.insert(0, str(rwi / "scripts"))
        import baseline_backfill as bb  # noqa: E402  (Roger Wilco Imagery)
        import cloudmask  # noqa: E402
        import pickup  # noqa: E402
        stage = Path(a.stage)
        stage.mkdir(parents=True, exist_ok=True)
        bb.OUT = stage                     # its picker writes here, never into the checkout
        pickup.QUICKLOOK_ONLY = True       # JPEG quicklook and a georeference sidecar, no GeoTIFF
        head = (rwi / ".git" / "HEAD").read_text().strip()
        rwi_commit = (rwi / ".git" / head.split(" ", 1)[1]).read_text().strip() if head.startswith("ref:") else head

    places = json.loads((ROOT / "data" / "places.json").read_text())
    centres = json.loads(CENTRES.read_text())
    index = json.loads(INDEX.read_text()) if INDEX.exists() else {"images": []}
    done = {x["place"]: x for x in index["images"]}
    only = set(a.only.split(",")) if a.only else None
    OUT.mkdir(exist_ok=True)

    for p in places:
        pid = p["id"]
        if (only and pid not in only) or not centres.get(pid):
            continue
        if pid in done and not (a.redo or only):
            continue
        c = centres[pid]
        w_km, h_km, res = (8, 6, 20) if pid in WIDE else (4, 3, 10)
        bbox = box(c["lat"], c["lon"], w_km, h_km)
        if a.engine == "rwi":
            got, errors, tries, found, best = bb.pick(pickup, cloudmask, client, dict(id=pid, bbox=bbox, res_m=res), {}, 1, 365, 30, 20, 0.6)
            if not got:
                print(pid, p["name"], "no clear scene; tries", tries, "best", best, errors[:1], flush=True)
                continue
            g = got[0]
            t, scene, clear = dt.datetime.fromisoformat(g["datetime"]), g["id"], g["clear_frac"]
            im = Image.open(stage / pid / g["files"][0])
            built = f"Roger Wilco Imagery (roger-wilco-imaging-pre-alpha @{rwi_commit[:7]}: pickup.py, cloudmask.py, baseline_backfill.py)"
            credit = f"Contains modified Copernicus Sentinel data {t.year}. Roger Wilco Imagery."
        else:
            r, tries = own_pick(client, bbox, res)
            if r is None:
                print(pid, p["name"], "no clear scene; tries", tries, flush=True)
                continue
            t, scene, clear = r["item"].datetime, r["item"].id, round(r["clear"], 3)
            im = own_look(r["rgb"])
            built = "tools/place_imagery.py in this repo, own engine"
            credit = f"Contains modified Copernicus Sentinel data {t.year}"
        dst = OUT / f"{pid}.jpg"
        w, h = caption(im, dst, credit)
        done[pid] = dict(
            place=pid, name=p["name"], file=f"imagery/{pid}.jpg", width=w, height=h, bytes=dst.stat().st_size,
            sha256=hashlib.sha256(dst.read_bytes()).hexdigest(),
            taken=t.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), scene=scene, satellite="Sentinel-2 (L2A)",
            ground_km=[w_km, h_km], metres_per_pixel=res, clear=clear, centre=[c["lat"], c["lon"]],
            credit=credit, licence=LICENCE, licence_url=LICENCE_URL,
            centre_credit="Centre point: (c) OpenStreetMap contributors, ODbL 1.0",
            built_with=built,
            alt=f"Satellite image of {p['name']} and the land round it, {w_km} by {h_km} kilometres, {t:%-d %B %Y}.")
        index["images"] = sorted(done.values(), key=lambda x: x["place"])
        INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2, separators=(",", ": ")) + "\n")
        print(pid, p["name"], scene, t.date(), "clear", clear, dst.stat().st_size, "bytes", flush=True)


if __name__ == "__main__":
    main()
