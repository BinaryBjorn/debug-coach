#!/usr/bin/env python3
"""Maak een instructievideo uit een ruwe opname, het kliklog en het script.

Gebruik: python3 videos/maak.py <map> [--plan-only] [--stem test|openai]
  <map>/script.json, <map>/ruw/opname.mov, <map>/ruw/log.json  ->  <map>/uit/
Rekenregels: tests/fixtures/gedeeld/log.schema.json (_regels).
"""
import argparse
import json
import pathlib
import subprocess
import sys

import beeld
from huisstijl import BREEDTE, FPS, HOEKSTRAAL, HOOGTE, KADER, ZOOM

CIRKEL_DIAMETER = 72


def _r(x):
    return round(x, 3)


def opname_info(pad):
    """Beeldsnelheid en duur van de ruwe opname via ffprobe (None als die er niet is)."""
    if not pad.is_file():
        return {"fps": None, "duur": None}
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=r_frame_rate:format=duration", "-of", "json", str(pad)],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
        teller, noemer = d["streams"][0]["r_frame_rate"].split("/")
        return {"fps": _r(float(teller) / float(noemer)), "duur": _r(float(d["format"]["duration"]))}
    except (ValueError, KeyError, IndexError, ZeroDivisionError):
        return {"fps": None, "duur": None}


def kader(bw, bh):
    """Schaal en positie van het scherm in de uitvoer: past in 84% van breedte en hoogte, gecentreerd."""
    f = min(KADER * BREEDTE / bw, KADER * HOOGTE / bh)
    w, h = int(round(bw * f)), int(round(bh * f))
    w -= w % 2
    h -= h % 2
    return {"factor": _r(f), "breedte": w, "hoogte": h, "x": (BREEDTE - w) // 2, "y": (HOOGTE - h) // 2}


def maak_plan(script, log, opname=None):
    s = log["scherm"]["schaal"]
    g = log["gebied"]
    t0 = log["opname"]["start_video_gemeten"]
    bw, bh = g["breedte"] * s, g["hoogte"] * s
    vw, vh = bw / ZOOM, bh / ZOOM

    def pixel(x, y):
        px = min(max((x - g["x"]) * s, vw / 2), bw - vw / 2)
        py = min(max((y - g["y"]) * s, vh / 2), bh - vh / 2)
        return [int(round(px)), int(round(py))]

    stappen = []
    t_uit = 0.0
    bron_vorige = 0.0
    for st in script["stappen"]:
        ev = [e for e in log["events"] if e["stap"] == st["id"]]
        if ev:
            begin = min(e["t"] for e in ev) - t0
            hd = max(e["t"] for e in ev) - min(e["t"] for e in ev) + 0.5
        else:
            begin, hd = bron_vorige, 0.0   # geen events: het laatste kader van de vorige stap blijft staan
        sd = max(st["duur_s"], hd)
        klik = [e for e in ev if e["handeling"] == "klik"]
        if klik:
            zoomdoel = pixel(klik[0]["x"], klik[0]["y"])
        elif "zoomdoel" in st:
            zoomdoel = pixel(st["zoomdoel"][0], st["zoomdoel"][1])
        else:
            zoomdoel = None
        stappen.append({
            "id": st["id"],
            "tekst": st["tekst"],
            "duur_s": st["duur_s"],
            "bron_begin": _r(begin),
            "bron_einde": _r(begin + hd),
            "handelingsduur": _r(hd),
            "stapduur": _r(sd),
            "bevriezen": st["duur_s"] > hd,
            "uit_begin": _r(t_uit),
            "uit_einde": _r(t_uit + sd),
            "zoomdoel": zoomdoel,
        })
        t_uit += sd
        bron_vorige = begin + hd
    opname = opname or {}
    return {
        "totaal": _r(t_uit),
        "opname": {"breedte": bw, "hoogte": bh, "fps": opname.get("fps"), "duur": opname.get("duur")},
        "uitvoer": {"breedte": BREEDTE, "hoogte": HOOGTE, "fps": FPS},
        "kader": kader(bw, bh),
        "stappen": stappen,
    }


def maak_beelden(plan, uit):
    k = plan["kader"]
    beeld.achtergrond(str(uit / "achtergrond.png"), BREEDTE, HOOGTE)
    beeld.masker(str(uit / "masker.png"), k["breedte"], k["hoogte"], HOEKSTRAAL)
    beeld.cirkel(str(uit / "cirkel.png"), CIRKEL_DIAMETER)


def render(plan, map_, uit, slug):
    """Knipt per stap de handeling uit de opname, bevriest het laatste kader tot de stapduur,
    en zet het scherm met afgeronde hoeken op de achtergrond."""
    k = plan["kader"]
    duur_opname = plan["opname"]["duur"]
    n = len(plan["stappen"])
    delen = ["[0:v]fps=%d,split=%d%s" % (FPS, n, "".join("[b%d]" % i for i in range(n)))]
    for i, st in enumerate(plan["stappen"]):
        begin = st["bron_begin"]
        einde = st["bron_einde"]
        if duur_opname is not None:
            begin = min(begin, max(duur_opname - 1.0 / FPS, 0))
            einde = min(einde, duur_opname)
        einde = max(einde, begin + 1.0 / FPS)   # minstens één kader om te bevriezen
        delen.append("[b%d]trim=start=%.3f:end=%.3f,setpts=PTS-STARTPTS,"
                     "tpad=stop_mode=clone:stop_duration=%.3f,trim=duration=%.3f,setpts=PTS-STARTPTS[s%d]"
                     % (i, begin, einde, st["stapduur"], st["stapduur"], i))
    delen.append("%sconcat=n=%d:v=1:a=0[reeks]" % ("".join("[s%d]" % i for i in range(n)), n))
    delen.append("[reeks]scale=%d:%d,format=yuva420p[scherm]" % (k["breedte"], k["hoogte"]))
    delen.append("[2:v]format=gray[m]")
    delen.append("[scherm][m]alphamerge[rond]")
    delen.append("[1:v][rond]overlay=%d:%d:shortest=1,format=yuv420p[v]" % (k["x"], k["y"]))
    args = ["ffmpeg", "-v", "error", "-y",
            "-i", str(map_ / "ruw" / "opname.mov"),
            "-loop", "1", "-framerate", str(FPS), "-i", str(uit / "achtergrond.png"),
            "-loop", "1", "-framerate", str(FPS), "-i", str(uit / "masker.png"),
            "-filter_complex", ";".join(delen), "-map", "[v]",
            "-t", "%.3f" % plan["totaal"], "-r", str(FPS),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            str(uit / (slug + ".mp4"))]
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ffmpeg faalde: " + r.stderr[-1500:])


def main(argv=None):
    ap = argparse.ArgumentParser(description="Maak een instructievideo uit opname, kliklog en script.")
    ap.add_argument("map")
    ap.add_argument("--plan-only", action="store_true", help="schrijf enkel uit/plan.json")
    ap.add_argument("--stem", choices=["test", "openai"], default="test")
    a = ap.parse_args(argv)

    map_ = pathlib.Path(a.map)
    script = json.loads((map_ / "script.json").read_text())
    log = json.loads((map_ / "ruw" / "log.json").read_text())
    slug = script.get("slug") or map_.name
    uit = map_ / "uit"
    uit.mkdir(parents=True, exist_ok=True)

    plan = maak_plan(script, log, opname_info(map_ / "ruw" / "opname.mov"))
    (uit / "plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")
    print("plan: %s (%d stappen, %.1f s)" % (uit / "plan.json", len(plan["stappen"]), plan["totaal"]))
    if a.plan_only:
        return 0

    maak_beelden(plan, uit)
    render(plan, map_, uit, slug)
    print("video: %s" % (uit / (slug + ".mp4")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
