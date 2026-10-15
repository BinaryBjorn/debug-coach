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
CIRKEL_DUUR = 0.6   # hoe lang de klikcirkel in beeld blijft, in seconden
RAMP = 0.4          # duur van in- en uitzoomen, in seconden


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
        if klik:
            # kliktijdstip in de uitvoer, en de klik in pixels van de opname (onbegrensd: de cirkel wordt later begrensd)
            t_klik = min(max(t_uit + (klik[0]["t"] - t0 - begin), t_uit), t_uit + sd)
            klikpunt = [(klik[0]["x"] - g["x"]) * s, (klik[0]["y"] - g["y"]) * s, _r(t_klik)]
        else:
            klikpunt = None
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
            "zoomfactor": ZOOM if zoomdoel is not None else 1.0,
            "_klik": klikpunt,
        })
        t_uit += sd
        bron_vorige = begin + hd
    opname = opname or {}
    k = kader(bw, bh)
    verloop = zoomverloop(stappen, bw, bh)
    for st in stappen:
        klikpunt = st.pop("_klik")
        if klikpunt is not None:
            st["cirkel"] = cirkelpunt(klikpunt, verloop, bw, bh, k)
    return {
        "totaal": _r(t_uit),
        "opname": {"breedte": bw, "hoogte": bh, "fps": opname.get("fps"), "duur": opname.get("duur")},
        "uitvoer": {"breedte": BREEDTE, "hoogte": HOOGTE, "fps": FPS},
        "kader": k,
        "zoomverloop": verloop,
        "stappen": stappen,
    }


def zoomverloop(stappen, bw, bh):
    """Sleutelpunten [t, zoom, cx, cy] in uitvoertijd, lineair tussen de punten.

    Een stap met een zoomdoel staat op ZOOM van het kliktijdstip (zonder klik: 0,4 s na het begin van de stap)
    tot 0,4 s voor het einde; ervoor en erna 0,4 s in- en uitzoomen. Volgen twee zoomstappen elkaar te snel op,
    dan schuift het beeld ingezoomd van het ene doel naar het andere. Elders 1x."""
    punten = [[0.0, 1.0, bw / 2.0, bh / 2.0]]
    vorige = None   # (einde van het vasthouden, doel) van de vorige zoomstap
    for st in stappen:
        if st["zoomdoel"] is None:
            continue
        cx, cy = st["zoomdoel"]
        t_klik = st.get("_klik")[2] if st.get("_klik") else st["uit_begin"] + RAMP
        h0 = min(max(t_klik, st["uit_begin"]), st["uit_einde"])
        h1 = max(h0, st["uit_einde"] - RAMP)
        if vorige is not None and vorige[0] + RAMP > h0 - RAMP:
            punten.append([h0, ZOOM, cx, cy])   # ingezoomd doorschuiven
        else:
            if vorige is not None:
                punten.append([vorige[0] + RAMP, 1.0] + vorige[1])
            start = max(h0 - RAMP, punten[-1][0])
            if start < h0:
                punten.append([start, 1.0, cx, cy])
            punten.append([h0, ZOOM, cx, cy])
        if h1 > h0:
            punten.append([h1, ZOOM, cx, cy])
        vorige = (h1, [cx, cy])
    if vorige is not None:
        punten.append([vorige[0] + RAMP, 1.0] + vorige[1])
    uit = []
    for p in punten:   # punten op hetzelfde tijdstip: het laatste wint
        p = [_r(p[0]), _r(p[1]), _r(p[2]), _r(p[3])]
        if uit and uit[-1][0] >= p[0]:
            uit[-1] = p
        else:
            uit.append(p)
    return uit


def zoom_op(verloop, t):
    """Zoom en middelpunt op tijdstip t (lineair tussen de sleutelpunten)."""
    if t <= verloop[0][0]:
        return verloop[0][1:]
    for a, b in zip(verloop, verloop[1:]):
        if t <= b[0]:
            f = (t - a[0]) / (b[0] - a[0])
            return [a[i] + (b[i] - a[i]) * f for i in (1, 2, 3)]
    return verloop[-1][1:]


def venster(z, cx, cy, bw, bh):
    """Linkerbovenhoek van het ingezoomde venster, binnen de opname gehouden (zoals in zoompan)."""
    vx = min(max(cx - bw / z / 2, 0), bw - bw / z)
    vy = min(max(cy - bh / z / 2, 0), bh - bh / z)
    return vx, vy


def cirkelpunt(klikpunt, verloop, bw, bh, k):
    """[x, y, t]: de klik in uitvoercoördinaten van het ingezoomde kader op het kliktijdstip,
    begrensd tot het zichtbare scherm."""
    px, py, t = klikpunt
    z, cx, cy = zoom_op(verloop, t)
    vx, vy = venster(z, cx, cy, bw, bh)
    f = k["breedte"] / float(bw)
    x = k["x"] + (px - vx) * z * f
    y = k["y"] + (py - vy) * z * f
    x = min(max(x, k["x"]), k["x"] + k["breedte"])
    y = min(max(y, k["y"]), k["y"] + k["hoogte"])
    return [int(round(x)), int(round(y)), t]


def _expr_lineair(verloop, i):
    """ffmpeg-uitdrukking in de tijd `it` voor kolom i van het zoomverloop (geneste if's)."""
    expr = "%.4f" % verloop[-1][i]
    for a, b in reversed(list(zip(verloop, verloop[1:]))):
        if b[0] <= a[0]:
            continue
        stuk = "(%.4f+(%.4f)*(it-%.3f)/%.3f)" % (a[i], b[i] - a[i], a[0], b[0] - a[0])
        expr = "if(lt(it,%.3f),%s,%s)" % (b[0], stuk, expr)
    return "if(lt(it,%.3f),%.4f,%s)" % (verloop[0][0], verloop[0][i], expr)


def vtt_tijd(t):
    ms = int(round(t * 1000))
    return "%02d:%02d:%02d.%03d" % (ms // 3600000, ms // 60000 % 60, ms // 1000 % 60, ms % 1000)


def schrijf_vtt(plan, pad):
    """Eén cue per stap met de gesproken tekst, op de tijden uit het plan."""
    regels = ["WEBVTT", ""]
    for i, st in enumerate(plan["stappen"], 1):
        regels += [str(i), "%s --> %s" % (vtt_tijd(st["uit_begin"]), vtt_tijd(st["uit_einde"])),
                   " ".join(st["tekst"].split()), ""]
    pad.write_text("\n".join(regels))


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
    bw, bh = plan["opname"]["breedte"], plan["opname"]["hoogte"]
    v = plan["zoomverloop"]
    delen.append("[reeks]zoompan=z='%s':x='clip(%s-iw/zoom/2,0,iw-iw/zoom)':y='clip(%s-ih/zoom/2,0,ih-ih/zoom)'"
                 ":d=1:s=%dx%d:fps=%d[zoom]" % (_expr_lineair(v, 1), _expr_lineair(v, 2), _expr_lineair(v, 3), bw, bh, FPS))
    delen.append("[zoom]scale=%d:%d,format=yuva420p[scherm]" % (k["breedte"], k["hoogte"]))
    delen.append("[2:v]format=gray[m]")
    delen.append("[scherm][m]alphamerge[rond]")
    delen.append("[1:v][rond]overlay=%d:%d:shortest=1[v0]" % (k["x"], k["y"]))
    vorige = "v0"
    for i, st in enumerate(s for s in plan["stappen"] if s.get("cirkel")):
        x, y, t = st["cirkel"]
        tot = max(min(t + CIRKEL_DUUR, st["uit_einde"]), t + 1.0 / FPS)
        delen.append("[%s][3:v]overlay=%d:%d:enable='between(t,%.3f,%.3f)'[c%d]"
                     % (vorige, x - CIRKEL_DIAMETER // 2, y - CIRKEL_DIAMETER // 2, t, tot, i))
        vorige = "c%d" % i
    delen.append("[%s]format=yuv420p[v]" % vorige)
    args = ["ffmpeg", "-v", "error", "-y",
            "-i", str(map_ / "ruw" / "opname.mov"),
            "-loop", "1", "-framerate", str(FPS), "-i", str(uit / "achtergrond.png"),
            "-loop", "1", "-framerate", str(FPS), "-i", str(uit / "masker.png"),
            "-loop", "1", "-framerate", str(FPS), "-i", str(uit / "cirkel.png"),
            "-i", str(uit / (slug + ".vtt")),
            "-filter_complex", ";".join(delen), "-map", "[v]", "-map", "4:s",
            "-t", "%.3f" % plan["totaal"], "-r", str(FPS),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:s", "mov_text", "-movflags", "+faststart",
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
    schrijf_vtt(plan, uit / (slug + ".vtt"))
    render(plan, map_, uit, slug)
    print("video: %s" % (uit / (slug + ".mp4")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
